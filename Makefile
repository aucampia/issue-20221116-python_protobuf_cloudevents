# https://www.gnu.org/software/make/manual/make.html
.PHONY: all
all:

########################################################################
# boiler plate
########################################################################
SHELL=bash
.SHELLFLAGS=-ec -o pipefail

current_makefile:=$(lastword $(MAKEFILE_LIST))
current_makefile_dirname:=$(dir $(current_makefile))
current_makefile_dirname_abspath:=$(dir $(abspath $(current_makefile)))
current_makefile_dirname_realpath:=$(dir $(realpath $(current_makefile)))

ifneq ($(filter all vars,$(VERBOSE)),)
dump_var=$(info var $(1)=$($(1)))
dump_vars=$(foreach var,$(1),$(call dump_var,$(var)))
else
dump_var=
dump_vars=
endif

ifneq ($(filter all targets,$(VERBOSE)),)
__ORIGINAL_SHELL:=$(SHELL)
SHELL=$(warning Building $@$(if $<, (from $<))$(if $?, ($? newer)))$(TIME) $(__ORIGINAL_SHELL)
endif

########################################################################
# variables
########################################################################

localstatedir?=var
generated_dir?=$(localstatedir)/generated

########################################################################
# targets
########################################################################

.PHONY: configure
configure: ## configure the project

.PHONY: validate
validate: ## validate everything

.PHONY: validate-fix
validate-fix: ## fix auto-fixable validation errors

.PHONY: test
test: ## run the project's tests

.PHONY: generate
generate: ## generate all outputs

.PHONY: all
all: ## do everything
all: validate generate

.PHONY: clean
clean: ## clean outputs
clean: clean-var/

########################################################################
# python
########################################################################

py_source=./src ./tests ./devscripts
poetry=python -m poetry

.PHONY: python-configure
configure: python-configure
python-configure:
	$(poetry) install

.PHONY: python-validate-static
validate-static: python-validate-static
python-validate-static:
	$(poetry) run mypy --show-error-codes --show-error-context $(CLI_ARGS)
	$(poetry) run codespell $(or $(CLI_ARGS),$(py_source) *.md)
	$(poetry) run isort --check --diff $(or $(CLI_ARGS),$(py_source))
	$(poetry) run black --check --diff $(or $(CLI_ARGS),$(py_source))
	$(poetry) run flake8 $(or $(CLI_ARGS),$(py_source))
	$(poetry) export --without-hashes --dev --format requirements.txt | $(poetry) run safety check --full-report --stdin

.PHONY: python-validate-fix
validate-fix: python-validate-fix
python-validate-fix:
	$(poetry) run pycln --config=pyproject.toml $(or $(CLI_ARGS),$(py_source))
	$(poetry) run isort $(or $(CLI_ARGS),$(py_source))
	$(poetry) run black $(or $(CLI_ARGS),$(py_source))

.PHONY: python-test
test: python-test
pytest_args=--cov-report term --cov-report xml
python-test:
	$(poetry) run pytest $(pytest_args) $(CLI_ARGS)

.PHONY: python-validate
validate: python-validate
python-validate: python-validate-static python-test

########################################################################
# buf targets
########################################################################

protbuf_dir=spec/proto
buf=poetry run buf
buf_format_args=--exclude-path spec/proto/io/cloudevents/v1/cloudevents.proto

.PHONY: buf-validate
validate: buf-validate
buf-validate: ## buf validation
	$(buf) lint
	$(buf) format --diff $(buf_format_args)

.PHONY: buf-validate-fix
validate-fix: buf-validate-fix
buf-validate-fix: ## fix auto-fixable buf validation errors
	$(buf) format --write $(buf_format_args)

.PHONY: buf-generate
generate: buf-generate
buf-generate: ## generate buf outputs
	\rm -rv generated/*proto*/ || :
	$(buf) generate --include-imports
	touch generated/betterproto/_bpbgen/py.typed
	poetry run protol --in-place --python-out generated/protol/_plgen --exclude-google-imports buf
	touch generated/protol/_plgen/py.typed

$(generated_dir)/main.dsc: | $(generated_dir)/
	$(buf) build --as-file-descriptor-set -o $(@) -vv --debug

.PHONY: buf-export
generate: buf-export
buf-export: | $(localstatedir)/buf/ ## export proto files
	$(buf) export -o $(localstatedir)/buf/exported

.PHONY: buf-mod-update
buf-mod-update: # Update buf modules
	$(buf) mod update $(protbuf_dir)

########################################################################
# other
########################################################################


fetch: spec/proto/io/cloudevents/v1/cloudevents.proto

spec/proto/io/cloudevents/v1/cloudevents.proto:
	mkdir -vp $(dir $(@))
	curl -L https://github.com/cloudevents/spec/raw/3da5643ebceb39637406a7e30903dbac81cf92d2/cloudevents/formats/cloudevents.proto -o $(@)

########################################################################
# utility targets
########################################################################

.PHONY: help
help: ## Show this message.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(current_makefile) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: .FORCE
.FORCE:
$(force_targets): .FORCE

## Create directories
.PRECIOUS: %/
%/:
	mkdir -vp $(@)

## Clean directories
.PHONY: clean-%/
clean-%/:
	@{ test -d $(*) && { set -x; rm -vr $(*); set +x; } } || echo "directory $(*) does not exist ... nothing to clean"

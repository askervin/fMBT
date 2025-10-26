VPATH ?= .

dist_noinst_SCRIPTS = \
	setup.py

# scripts
dist_noinst_SCRIPTS +=		\
	fmbt3-editor		\
	fmbt3-log		\
	lsts32dot		\
	fmbt3-view		\
	remote_py3aal
# end of scripts

# modules
dist_noinst_SCRIPTS +=		\
	aalmodel.py		\
	fmbt.py			\
	fmbt_config.py		\
	fmbtpng.py     	        \
	lsts3.py                \
	pycosh.py
# end of modules

utils_installer: $(dist_noinst_SCRIPTS)
	cp $(addprefix $(VPATH)/,$(dist_noinst_SCRIPTS)) . || true
	touch $@

if MINGW
else
# extensions
# end of extensions
all-local: utils_installer ../utils/eye4graphics.cc ../utils/eye4graphics.h
	VPATH='$(VPATH)' CC='$(CXX)' PKG_CONFIG='$(PKG_CONFIG)' python3 setup.py build

install-exec-local:
	$(PYTHON) setup.py install --root=$(DESTDIR)/ --prefix=$(PYTHON_PREFIX) --install-layout=deb
	for f in $(dist_noinst_SCRIPTS); do \
		head -n 1 "$(PYTHON_PREFIX)/bin/$$f" 2>/dev/null | grep -q '#!python' && { \
			echo "fix shebang in $(PYTHON_PREFIX)/bin/$$f"; \
			sed -i '1s|^#!python|#!/usr/bin/env python|' "$(PYTHON_PREFIX)/bin/$$f"; \
		}; \
	done; \
	true
endif

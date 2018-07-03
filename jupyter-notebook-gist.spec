#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyter-notebook-gist
Version  : 0.5.0
Release  : 17
URL      : http://pypi.debian.net/jupyter-notebook-gist/jupyter-notebook-gist-0.5.0.tar.gz
Source0  : http://pypi.debian.net/jupyter-notebook-gist/jupyter-notebook-gist-0.5.0.tar.gz
Summary  : Create a gist from the Jupyter Notebook UI
Group    : Development/Tools
License  : MPL-2.0 MPL-2.0-no-copyleft-exception
Requires: jupyter-notebook-gist-python3
Requires: jupyter-notebook-gist-python
Requires: ipython
Requires: jupyter
Requires: notebook
Requires: requests
Requires: six
Requires: widgetsnbextension
BuildRequires : ipython
BuildRequires : jupyter
BuildRequires : notebook
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest

BuildRequires : python3-dev
BuildRequires : requests
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : widgetsnbextension

%description
### jupyter-notebook-gist
[![Build Status](https://travis-ci.org/mozilla/jupyter-notebook-gist.svg?branch=master)](https://travis-ci.org/mozilla/jupyter-notebook-gist)

%package python
Summary: python components for the jupyter-notebook-gist package.
Group: Default
Requires: jupyter-notebook-gist-python3

%description python
python components for the jupyter-notebook-gist package.


%package python3
Summary: python3 components for the jupyter-notebook-gist package.
Group: Default
Requires: python3-core

%description python3
python3 components for the jupyter-notebook-gist package.


%prep
%setup -q -n jupyter-notebook-gist-0.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521134443
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

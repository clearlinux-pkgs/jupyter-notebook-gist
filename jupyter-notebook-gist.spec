#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jupyter-notebook-gist
Version  : 0.5.0
Release  : 33
URL      : http://pypi.debian.net/jupyter-notebook-gist/jupyter-notebook-gist-0.5.0.tar.gz
Source0  : http://pypi.debian.net/jupyter-notebook-gist/jupyter-notebook-gist-0.5.0.tar.gz
Summary  : Create a gist from the Jupyter Notebook UI
Group    : Development/Tools
License  : MPL-2.0
Requires: jupyter-notebook-gist-license = %{version}-%{release}
Requires: jupyter-notebook-gist-python = %{version}-%{release}
Requires: jupyter-notebook-gist-python3 = %{version}-%{release}
Requires: ipython
Requires: jupyter
Requires: notebook
Requires: requests
Requires: six
Requires: widgetsnbextension
BuildRequires : buildreq-distutils3
BuildRequires : ipython
BuildRequires : jupyter
BuildRequires : notebook
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : requests
BuildRequires : setuptools_scm
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : widgetsnbextension

%description
### jupyter-notebook-gist
[![Build Status](https://travis-ci.org/mozilla/jupyter-notebook-gist.svg?branch=master)](https://travis-ci.org/mozilla/jupyter-notebook-gist)

%package license
Summary: license components for the jupyter-notebook-gist package.
Group: Default

%description license
license components for the jupyter-notebook-gist package.


%package python
Summary: python components for the jupyter-notebook-gist package.
Group: Default
Requires: jupyter-notebook-gist-python3 = %{version}-%{release}

%description python
python components for the jupyter-notebook-gist package.


%package python3
Summary: python3 components for the jupyter-notebook-gist package.
Group: Default
Requires: python3-core
Provides: pypi(jupyter_notebook_gist)
Requires: pypi(ipython)
Requires: pypi(jupyter)
Requires: pypi(notebook)
Requires: pypi(requests)
Requires: pypi(six)
Requires: pypi(widgetsnbextension)

%description python3
python3 components for the jupyter-notebook-gist package.


%prep
%setup -q -n jupyter-notebook-gist-0.5.0
cd %{_builddir}/jupyter-notebook-gist-0.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583536967
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jupyter-notebook-gist
cp %{_builddir}/jupyter-notebook-gist-0.5.0/LICENSE %{buildroot}/usr/share/package-licenses/jupyter-notebook-gist/ece3df1263c100f93c427face535a292723d38e7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jupyter-notebook-gist/ece3df1263c100f93c427face535a292723d38e7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

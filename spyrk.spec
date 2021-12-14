#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : spyrk
Version  : 0.0.4
Release  : 23
URL      : https://files.pythonhosted.org/packages/6d/b9/8d168df047a4aa9318ab701fd8232f17ed0153ca5ba45685bb6fbb59319a/spyrk-0.0.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/6d/b9/8d168df047a4aa9318ab701fd8232f17ed0153ca5ba45685bb6fbb59319a/spyrk-0.0.4.tar.gz
Summary  : Python module for Spark devices
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: spyrk-license = %{version}-%{release}
Requires: spyrk-python = %{version}-%{release}
Requires: spyrk-python3 = %{version}-%{release}
Requires: cached-property
Requires: hammock
BuildRequires : buildreq-distutils3
BuildRequires : cached-property
BuildRequires : hammock
BuildRequires : python-mock
Patch1: fixdeps.patch

%description
=====
        
        Python module for Spark devices.

%package license
Summary: license components for the spyrk package.
Group: Default

%description license
license components for the spyrk package.


%package python
Summary: python components for the spyrk package.
Group: Default
Requires: spyrk-python3 = %{version}-%{release}

%description python
python components for the spyrk package.


%package python3
Summary: python3 components for the spyrk package.
Group: Default
Requires: python3-core
Provides: pypi(spyrk)
Requires: pypi(cached_property)
Requires: pypi(hammock)
Requires: pypi(mock)

%description python3
python3 components for the spyrk package.


%prep
%setup -q -n spyrk-0.0.4
cd %{_builddir}/spyrk-0.0.4
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603405154
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/spyrk
cp %{_builddir}/spyrk-0.0.4/LICENSE %{buildroot}/usr/share/package-licenses/spyrk/84dca3c4c2a464f21963f4ebaefbd0042094d286
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/spyrk/84dca3c4c2a464f21963f4ebaefbd0042094d286

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

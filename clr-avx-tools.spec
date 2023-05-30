#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
#
Name     : clr-avx-tools
Version  : 53
Release  : 59
URL      : https://github.com/clearlinux/clr-avx-tools/archive/v53/clr-avx-tools-53.tar.gz
Source0  : https://github.com/clearlinux/clr-avx-tools/archive/v53/clr-avx-tools-53.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: clr-avx-tools-bin = %{version}-%{release}
Requires: clr-avx-tools-data = %{version}-%{release}
Requires: clr-avx-tools-license = %{version}-%{release}
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the clr-avx-tools package.
Group: Binaries
Requires: clr-avx-tools-data = %{version}-%{release}
Requires: clr-avx-tools-license = %{version}-%{release}

%description bin
bin components for the clr-avx-tools package.


%package data
Summary: data components for the clr-avx-tools package.
Group: Data

%description data
data components for the clr-avx-tools package.


%package license
Summary: license components for the clr-avx-tools package.
Group: Default

%description license
license components for the clr-avx-tools package.


%prep
%setup -q -n clr-avx-tools-53
cd %{_builddir}/clr-avx-tools-53

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685474040
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1685474040
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-avx-tools
cp %{_builddir}/clr-avx-tools-%{version}/COPYING %{buildroot}/usr/share/package-licenses/clr-avx-tools/04319952ed7b0f3b3a70ae4d5d9f954317b8f970 || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/clr-avx2-move.pl
/usr/bin/clr-python-avx2
/usr/bin/clr-python-avx512
/usr/bin/elf-move.py
/usr/bin/filemap-verify.py
/usr/bin/pypi-dep-fix.py

%files data
%defattr(-,root,root,-)
/usr/share/clr-avx-tools/avxjudge.make
/usr/share/clr-avx-tools/avxjudge.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-avx-tools/04319952ed7b0f3b3a70ae4d5d9f954317b8f970

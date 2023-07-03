#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : glib-networking
Version  : 2.76.1
Release  : 51
URL      : https://download.gnome.org/sources/glib-networking/2.76/glib-networking-2.76.1.tar.xz
Source0  : https://download.gnome.org/sources/glib-networking/2.76/glib-networking-2.76.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: glib-networking-data = %{version}-%{release}
Requires: glib-networking-lib = %{version}-%{release}
Requires: glib-networking-libexec = %{version}-%{release}
Requires: glib-networking-license = %{version}-%{release}
Requires: glib-networking-locales = %{version}-%{release}
Requires: glib-networking-services = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gnutls-dev
BuildRequires : gnutls-dev32
BuildRequires : libproxy-dev
BuildRequires : openssl-dev
BuildRequires : openssl-dev32
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Network-related giomodules for glib
glib-networking contains the implementations of certain GLib networking features
that cannot be implemented directly in GLib itself because of their
dependencies.

%package data
Summary: data components for the glib-networking package.
Group: Data

%description data
data components for the glib-networking package.


%package lib
Summary: lib components for the glib-networking package.
Group: Libraries
Requires: glib-networking-data = %{version}-%{release}
Requires: glib-networking-libexec = %{version}-%{release}
Requires: glib-networking-license = %{version}-%{release}

%description lib
lib components for the glib-networking package.


%package lib32
Summary: lib32 components for the glib-networking package.
Group: Default
Requires: glib-networking-data = %{version}-%{release}
Requires: glib-networking-license = %{version}-%{release}

%description lib32
lib32 components for the glib-networking package.


%package libexec
Summary: libexec components for the glib-networking package.
Group: Default
Requires: glib-networking-license = %{version}-%{release}

%description libexec
libexec components for the glib-networking package.


%package license
Summary: license components for the glib-networking package.
Group: Default

%description license
license components for the glib-networking package.


%package locales
Summary: locales components for the glib-networking package.
Group: Default

%description locales
locales components for the glib-networking package.


%package services
Summary: services components for the glib-networking package.
Group: Systemd services
Requires: systemd

%description services
services components for the glib-networking package.


%package tests
Summary: tests components for the glib-networking package.
Group: Default
Requires: glib-networking = %{version}-%{release}
Requires: gsettings-desktop-schemas

%description tests
tests components for the glib-networking package.


%prep
%setup -q -n glib-networking-2.76.1
cd %{_builddir}/glib-networking-2.76.1
pushd ..
cp -a glib-networking-2.76.1 build32
popd
pushd ..
cp -a glib-networking-2.76.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688408439
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dlibproxy=enabled \
-Dgnutls=enabled \
-Dinstalled_tests=true  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dlibproxy=enabled \
-Dgnutls=enabled \
-Dinstalled_tests=true  builddiravx2
ninja -v -C builddiravx2
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=plain -Dlibproxy=enabled \
-Dgnutls=enabled \
-Dinstalled_tests=true -Dlibproxy=disabled \
-Dopenssl=disabled \
-Dinstalled_tests=false builddir
ninja -v -C builddir
popd

%install
mkdir -p %{buildroot}/usr/share/package-licenses/glib-networking
cp %{_builddir}/glib-networking-%{version}/COPYING %{buildroot}/usr/share/package-licenses/glib-networking/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
pushd ../build32/
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang glib-networking
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/services/org.gtk.GLib.PACRunner.service

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/gio/modules/libgiognomeproxy.so
/V3/usr/lib64/gio/modules/libgiognutls.so
/V3/usr/lib64/gio/modules/libgiolibproxy.so
/usr/lib64/gio/modules/libgiognomeproxy.so
/usr/lib64/gio/modules/libgiognutls.so
/usr/lib64/gio/modules/libgiolibproxy.so

%files lib32
%defattr(-,root,root,-)
/usr/lib32/gio/modules/libgiognomeproxy.so
/usr/lib32/gio/modules/libgiognutls.so

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/glib-pacrunner
/usr/libexec/glib-pacrunner

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/glib-networking/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/glib-pacrunner.service

%files tests
%defattr(-,root,root,-)
/V3/usr/libexec/installed-tests/glib-networking/certificate-gnutls
/V3/usr/libexec/installed-tests/glib-networking/connection-gnutls
/V3/usr/libexec/installed-tests/glib-networking/environment-libproxy
/V3/usr/libexec/installed-tests/glib-networking/file-database-gnutls
/V3/usr/libexec/installed-tests/glib-networking/gnome
/V3/usr/libexec/installed-tests/glib-networking/mock-pkcs11.so
/usr/libexec/installed-tests/glib-networking/certificate-gnutls
/usr/libexec/installed-tests/glib-networking/connection-gnutls
/usr/libexec/installed-tests/glib-networking/environment-libproxy
/usr/libexec/installed-tests/glib-networking/file-database-gnutls
/usr/libexec/installed-tests/glib-networking/files/ca-alternative.pem
/usr/libexec/installed-tests/glib-networking/files/ca-key.pem
/usr/libexec/installed-tests/glib-networking/files/ca-ocsp.pem
/usr/libexec/installed-tests/glib-networking/files/ca-roots-bad.pem
/usr/libexec/installed-tests/glib-networking/files/ca-roots.pem
/usr/libexec/installed-tests/glib-networking/files/ca-verisign-sha1.pem
/usr/libexec/installed-tests/glib-networking/files/ca.pem
/usr/libexec/installed-tests/glib-networking/files/chain-with-verisign-md2.pem
/usr/libexec/installed-tests/glib-networking/files/chain.pem
/usr/libexec/installed-tests/glib-networking/files/client-and-key-fullchain.pem
/usr/libexec/installed-tests/glib-networking/files/client-and-key-password-enckey.p12
/usr/libexec/installed-tests/glib-networking/files/client-and-key-password.p12
/usr/libexec/installed-tests/glib-networking/files/client-and-key.p12
/usr/libexec/installed-tests/glib-networking/files/client-and-key.pem
/usr/libexec/installed-tests/glib-networking/files/client-csr.pem
/usr/libexec/installed-tests/glib-networking/files/client-future.pem
/usr/libexec/installed-tests/glib-networking/files/client-key.pem
/usr/libexec/installed-tests/glib-networking/files/client-past.pem
/usr/libexec/installed-tests/glib-networking/files/client.pem
/usr/libexec/installed-tests/glib-networking/files/client2-and-key.pem
/usr/libexec/installed-tests/glib-networking/files/client2-csr.pem
/usr/libexec/installed-tests/glib-networking/files/client2-key.pem
/usr/libexec/installed-tests/glib-networking/files/client2.pem
/usr/libexec/installed-tests/glib-networking/files/create-files.sh
/usr/libexec/installed-tests/glib-networking/files/garbage.pem
/usr/libexec/installed-tests/glib-networking/files/intermediate-ca-csr.pem
/usr/libexec/installed-tests/glib-networking/files/intermediate-ca-key.pem
/usr/libexec/installed-tests/glib-networking/files/intermediate-ca.pem
/usr/libexec/installed-tests/glib-networking/files/non-ca.pem
/usr/libexec/installed-tests/glib-networking/files/old-ca-key.pem
/usr/libexec/installed-tests/glib-networking/files/old-ca.pem
/usr/libexec/installed-tests/glib-networking/files/root-ca-csr.pem
/usr/libexec/installed-tests/glib-networking/files/server-and-key.pem
/usr/libexec/installed-tests/glib-networking/files/server-csr.pem
/usr/libexec/installed-tests/glib-networking/files/server-intermediate-csr.pem
/usr/libexec/installed-tests/glib-networking/files/server-intermediate-key.pem
/usr/libexec/installed-tests/glib-networking/files/server-intermediate.pem
/usr/libexec/installed-tests/glib-networking/files/server-key-pkcs8.der
/usr/libexec/installed-tests/glib-networking/files/server-key-pkcs8.pem
/usr/libexec/installed-tests/glib-networking/files/server-key.der
/usr/libexec/installed-tests/glib-networking/files/server-key.pem
/usr/libexec/installed-tests/glib-networking/files/server-ocsp-missing-and-key.pem
/usr/libexec/installed-tests/glib-networking/files/server-ocsp-missing-csr.pem
/usr/libexec/installed-tests/glib-networking/files/server-ocsp-missing.pem
/usr/libexec/installed-tests/glib-networking/files/server-ocsp-required-by-ca-and-key.pem
/usr/libexec/installed-tests/glib-networking/files/server-ocsp-required-by-ca-csr.pem
/usr/libexec/installed-tests/glib-networking/files/server-ocsp-required-by-ca.pem
/usr/libexec/installed-tests/glib-networking/files/server-ocsp-required-by-server-and-key.pem
/usr/libexec/installed-tests/glib-networking/files/server-ocsp-required-by-server-csr.pem
/usr/libexec/installed-tests/glib-networking/files/server-ocsp-required-by-server.pem
/usr/libexec/installed-tests/glib-networking/files/server-ocsp-required-csr.pem
/usr/libexec/installed-tests/glib-networking/files/server-oscp-req.der
/usr/libexec/installed-tests/glib-networking/files/server-self.pem
/usr/libexec/installed-tests/glib-networking/files/server.csr.pem
/usr/libexec/installed-tests/glib-networking/files/server.der
/usr/libexec/installed-tests/glib-networking/files/server.pem
/usr/libexec/installed-tests/glib-networking/files/ssl/ca.conf
/usr/libexec/installed-tests/glib-networking/files/ssl/client.conf
/usr/libexec/installed-tests/glib-networking/files/ssl/intermediate-ca.conf
/usr/libexec/installed-tests/glib-networking/files/ssl/old-ca.conf
/usr/libexec/installed-tests/glib-networking/files/ssl/server-intermediate.conf
/usr/libexec/installed-tests/glib-networking/files/ssl/server-muststaple.conf
/usr/libexec/installed-tests/glib-networking/files/ssl/server.conf
/usr/libexec/installed-tests/glib-networking/files/update-certificate-test.py
/usr/libexec/installed-tests/glib-networking/files/update-chain-with-new-root.py
/usr/libexec/installed-tests/glib-networking/files/update-test-database.py
/usr/libexec/installed-tests/glib-networking/gnome
/usr/libexec/installed-tests/glib-networking/mock-pkcs11.so
/usr/share/installed-tests/glib-networking/certificate-gnutls.test
/usr/share/installed-tests/glib-networking/connection-gnutls.test
/usr/share/installed-tests/glib-networking/environment-libproxy.test
/usr/share/installed-tests/glib-networking/file-database-gnutls.test
/usr/share/installed-tests/glib-networking/gnome.test

%files locales -f glib-networking.lang
%defattr(-,root,root,-)


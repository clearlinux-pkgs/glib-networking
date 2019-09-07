#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : glib-networking
Version  : 2.62.0
Release  : 23
URL      : https://download.gnome.org/sources/glib-networking/2.62/glib-networking-2.62.0.tar.xz
Source0  : https://download.gnome.org/sources/glib-networking/2.62/glib-networking-2.62.0.tar.xz
Summary  : Network extensions for GLib
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
BuildRequires : openssl-dev
BuildRequires : openssl-dev32
BuildRequires : pacrunner-dev
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libproxy-1.0)

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

%description services
services components for the glib-networking package.


%prep
%setup -q -n glib-networking-2.62.0
pushd ..
cp -a glib-networking-2.62.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567882466
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dlibproxy=enabled -Dgnutls=enabled  builddir
ninja -v -C builddir
pushd ../build32
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=plain -Dlibproxy=enabled -Dgnutls=enabled -Dlibproxy=disabled -Dopenssl=disabled builddir
ninja -v -C builddir
popd

%install
mkdir -p %{buildroot}/usr/share/package-licenses/glib-networking
cp COPYING %{buildroot}/usr/share/package-licenses/glib-networking/COPYING
pushd ../build32
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang glib-networking

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/services/org.gtk.GLib.PACRunner.service

%files lib
%defattr(-,root,root,-)
/usr/lib64/gio/modules/libgiognomeproxy.so
/usr/lib64/gio/modules/libgiognutls.so
/usr/lib64/gio/modules/libgiolibproxy.so

%files lib32
%defattr(-,root,root,-)
/usr/lib32/gio/modules/libgiognomeproxy.so
/usr/lib32/gio/modules/libgiognutls.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/glib-pacrunner

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/glib-networking/COPYING

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/glib-pacrunner.service

%files locales -f glib-networking.lang
%defattr(-,root,root,-)


#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : glib-networking
Version  : 2.50.0
Release  : 7
URL      : http://ftp.gnome.org/pub/gnome/sources/glib-networking/2.50/glib-networking-2.50.0.tar.xz
Source0  : http://ftp.gnome.org/pub/gnome/sources/glib-networking/2.50/glib-networking-2.50.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: glib-networking-lib
Requires: glib-networking-locales
BuildRequires : ca-certs
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(32gnutls)
BuildRequires : pkgconfig(32p11-kit-1)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(gsettings-desktop-schemas)
BuildRequires : pkgconfig(p11-kit-1)

%description
Network-related giomodules for glib.
File bugs against
http://bugzilla.gnome.org/enter_bug.cgi?product=glib&component=network

%package lib
Summary: lib components for the glib-networking package.
Group: Libraries

%description lib
lib components for the glib-networking package.


%package lib32
Summary: lib32 components for the glib-networking package.
Group: Default

%description lib32
lib32 components for the glib-networking package.


%package locales
Summary: locales components for the glib-networking package.
Group: Default

%description locales
locales components for the glib-networking package.


%prep
%setup -q -n glib-networking-2.50.0
pushd ..
cp -a glib-networking-2.50.0 build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1483234555
%configure --disable-static -with-ca-certificates=/var/cache/ca-certs/extracted/pem/tls-ca-bundle.pem
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static -with-ca-certificates=/var/cache/ca-certs/extracted/pem/tls-ca-bundle.pem   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%install
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
%find_lang glib-networking

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/gio/modules/libgiognomeproxy.so
/usr/lib64/gio/modules/libgiognutls.so

%files lib32
%defattr(-,root,root,-)
/usr/lib32/gio/modules/libgiognomeproxy.so
/usr/lib32/gio/modules/libgiognutls.so

%files locales -f glib-networking.lang
%defattr(-,root,root,-)


Name:       libxshmfence
Version:    1.3.2
Release:    1%{?dist}
Summary:    Shared memory 'SyncFence' synchronization primitive
License:    MIT
URL:        https://gitlab.freedesktop.org/xorg/lib/%{name}
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xorg-macros) >= 1.3
BuildRequires:  pkgconfig(xproto)

%description
This library offers a CPU-based synchronization primitive compatible
with the X SyncFence objects that can be shared between processes
using file descriptor passing.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%license COPYING
%{_includedir}/X11/xshmfence.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/xshmfence.pc

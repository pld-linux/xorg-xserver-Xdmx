# TODO
# - consider XSELINUX by default
#
# Conditional build:
%bcond_with	dbus		# D-BUS support for configuration (if no udev)
%bcond_with	hal		# HAL support for configuration (if no udev)
%bcond_without	udev		# UDEV support for configuration
%bcond_without	dri2		# DRI2 extension
%bcond_without	dri3		# DRI3 extension
%bcond_without	record		# RECORD extension
%bcond_with	xcsecurity	# XC-SECURITY extension (deprecated)
%bcond_with	xf86bigfont	# XF86BigFont extension
%bcond_with	xselinux	# SELinux extension
%bcond_without	systemtap	# systemtap/dtrace probes
%bcond_without	libunwind	# use libunwind for backtracing
#

%define	pixman_ver	0.30.0

%ifarch x32
%undefine	with_libunwind
%endif

Summary:	Xdmx - distributed multi-head X server
Summary(pl.UTF-8):	Xdmx - rozproszony, wielomonitorowy serwer X
Name:		xorg-xserver-Xdmx
Version:	1.20.13
Release:	1
License:	MIT
Group:		X11/Servers
Source0:	https://xorg.freedesktop.org/releases/individual/xserver/xorg-server-%{version}.tar.xz
# Source0-md5:	9acb2a51507e6056b09e3d3f19565419
Patch0:		xorg-xserver-server-builtin-SHA1.patch
Patch1:		110_nvidia_slowdow_fix.patch
Patch2:		%{name}-fix.patch
URL:		https://xorg.freedesktop.org/
BuildRequires:	Mesa-dri-devel >= 7.8.1
%{?with_dri2:BuildRequires:	Mesa-dri-devel >= 9.2.0}
BuildRequires:	OpenGL-devel >= 3.0
# for glx headers
BuildRequires:	OpenGL-GLX-devel >= 1.3
%{?with_xselinux:BuildRequires:	audit-libs-devel}
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	docbook-dtd43-xml
#BuildRequires:	doxygen >= 1.6.1
%if %{with hal} || %{with dbus}
BuildRequires:	dbus-devel >= 1.0
%endif
%{?with_hal:BuildRequires:	hal-devel}
BuildRequires:	libbsd-devel
BuildRequires:	libdrm-devel >= 2.4.89
%{?with_xselinux:BuildRequires:	libselinux-devel >= 2.0.86}
BuildRequires:	libtirpc-devel
BuildRequires:	libtool >= 2:2.2
%{?with_libunwind:BuildRequires:	libunwind-devel}
BuildRequires:	perl-base
BuildRequires:	pixman-devel >= %{pixman_ver}
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	pkgconfig(gl) >= 1.2
%{?with_systemtap:BuildRequires:	systemtap-sdt-devel}
BuildRequires:	systemd-devel >= 1:209
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-devel >= 1:143
BuildRequires:	xmlto >= 0.0.20
BuildRequires:	xorg-font-font-util >= 1.1
BuildRequires:	xorg-lib-libX11-devel >= 1.6
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXext-devel >= 1.0.99.4
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXfont2-devel >= 2.0.0
BuildRequires:	xorg-lib-libXi-devel >= 1.2.99.1
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXres-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-lib-libXtst-devel >= 1.0.99.2
BuildRequires:	xorg-lib-libdmx-devel >= 1.0.99.1
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.12.901
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-lib-libxshmfence-devel >= 1.1
BuildRequires:	xorg-lib-xtrans-devel >= 1.3.5
BuildRequires:	xorg-proto-bigreqsproto-devel >= 1.1.0
BuildRequires:	xorg-proto-compositeproto-devel >= 0.4
BuildRequires:	xorg-proto-damageproto-devel >= 1.1
BuildRequires:	xorg-proto-dmxproto-devel >= 2.2.99.1
%{?with_dri2:BuildRequires:	xorg-proto-dri2proto-devel >= 2.8}
BuildRequires:	xorg-proto-dri3proto-devel >= 1.2
BuildRequires:	xorg-proto-fixesproto-devel >= 5.0
BuildRequires:	xorg-proto-fontsproto-devel >= 2.1.3
BuildRequires:	xorg-proto-glproto-devel >= 1.4.17
BuildRequires:	xorg-proto-inputproto-devel >= 2.3
BuildRequires:	xorg-proto-kbproto-devel >= 1.0.3
BuildRequires:	xorg-proto-presentproto-devel >= 1.1
BuildRequires:	xorg-proto-randrproto-devel >= 1.6.0
%{?with_record:BuildRequires:	xorg-proto-recordproto-devel >= 1.13.99.1}
BuildRequires:	xorg-proto-renderproto-devel >= 0.11
BuildRequires:	xorg-proto-resourceproto-devel >= 1.2.0
BuildRequires:	xorg-proto-scrnsaverproto-devel >= 1.1
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xcmiscproto-devel >= 1.2.0
BuildRequires:	xorg-proto-xextproto-devel >= 1:7.3.0
%{?with_xf86bigfont:BuildRequires:	xorg-proto-xf86bigfontproto-devel >= 1.2.0}
BuildRequires:	xorg-proto-xf86dgaproto-devel >= 2.0.99.1
BuildRequires:	xorg-proto-xf86driproto-devel >= 2.1.0
BuildRequires:	xorg-proto-xf86vidmodeproto-devel >= 2.2.99.1
BuildRequires:	xorg-proto-xineramaproto-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.31
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.14
BuildRequires:	xz
Requires:	pixman >= %{pixman_ver}
Requires:	xorg-lib-libX11 >= 1.6
Requires:	xorg-lib-libXext >= 1.0.99.4
Requires:	xorg-lib-libXfont2 >= 2.0.0
Requires:	xorg-lib-libXi >= 1.2.99.1
Requires:	xorg-lib-libdmx >= 1.0.99.1
Requires:	xorg-xserver-common >= 1.20.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		tirpc_cflags	$(pkg-config --cflags libtirpc)
%define		tirpc_libs	$(pkg-config --libs libtirpc)

%description
Xdmx - distributed multi-head X server.

%description -l pl.UTF-8
Xdmx - rozproszony, wielomonitorowy serwer X.

%prep
%setup -q -n xorg-server-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

# xserver uses pixman-1 API/ABI so put that explictly here
sed -i -e 's#<pixman\.h#<pixman-1/pixman.h#g' ./fb/fb.h ./include/miscstruct.h ./render/picture.h

# support __filemansuffix__ with "x" suffix (per FHS 2.3)
%{__sed} -i -e 's,\.so man__filemansuffix__/,.so man5/,' hw/xfree86/man/*.man

%{__sed} -i -e '1s|#!/usr/bin/python$|#!%{__python}|' config/fdi2iclass.py

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CPPFLAGS="%{rpmcppflags} %{tirpc_cflags}" \
	LIBS="%{tirpc_libs}" \
	--libexecdir=%{_libdir}/xorg \
	--with-os-name="PLD/Linux" \
	--with-os-vendor="PLD/Team" \
	--with-default-font-path="%{_fontsdir}/misc,%{_fontsdir}/TTF,%{_fontsdir}/OTF,%{_fontsdir}/Type1,%{_fontsdir}/100dpi,%{_fontsdir}/75dpi" \
	--with-xkb-output=/var/lib/xkb \
	--disable-linux-acpi \
	--disable-linux-apm \
	%{?with_dbus:--enable-config-dbus} \
	--enable-config-hal%{!?with_hal:=no} \
	--enable-config-udev%{!?with_udev:=no} \
	--enable-dga \
	--enable-dmx \
	--enable-dri2%{!?with_dri2:=no} \
	--enable-dri3%{!?with_dri3:=no} \
	--disable-kdrive \
	%{?with_libunwind:--enable-libunwind} \
	%{?with_record:--enable-record} \
	--enable-secure-rpc \
	--enable-suid-wrapper \
	%{?with_xcsecurity:--enable-xcsecurity} \
	--disable-xephyr \
	%{?with_xf86bigfont:--enable-xf86bigfont} \
	--disable-xfree86-utils \
	--disable-xnest \
	--disable-xorg \
	%{?with_xselinux:--enable-xselinux} \
	--disable-xvfb \
	--disable-xwayland \
	%{!?with_systemtap:--without-dtrace} \
	--without-fop \
	--with-systemd-daemon

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with systemtap}
%{__rm} $RPM_BUILD_ROOT%{_docdir}/xorg-server/Xserver-DTrace.*
%endif

# packaged in xorg-xserver-common built from xorg-xserver-server.spec
%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/protocol.txt
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/Xserver.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/Xdmx
%attr(755,root,root) %{_bindir}/dmxaddinput
%attr(755,root,root) %{_bindir}/dmxaddscreen
%attr(755,root,root) %{_bindir}/dmxinfo
%attr(755,root,root) %{_bindir}/dmxreconfig
%attr(755,root,root) %{_bindir}/dmxresize
%attr(755,root,root) %{_bindir}/dmxrminput
%attr(755,root,root) %{_bindir}/dmxrmscreen
%attr(755,root,root) %{_bindir}/dmxtodmx
%attr(755,root,root) %{_bindir}/dmxwininfo
%attr(755,root,root) %{_bindir}/vdltodmx
%attr(755,root,root) %{_bindir}/xdmxconfig
%{_mandir}/man1/Xdmx.1*
%{_mandir}/man1/dmxtodmx.1*
%{_mandir}/man1/vdltodmx.1*
%{_mandir}/man1/xdmxconfig.1*

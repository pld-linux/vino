Summary:	A remote desktop system for GNOME
Summary(pl.UTF-8):	System zdalnego pulpitu dla GNOME
Name:		vino
Version:	3.22.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	http://ftp.gnome.org/pub/GNOME/sources/vino/3.22/%{name}-%{version}.tar.xz
# Source0-md5:	7305feaa5cc9acb788d7a13389922012
URL:		https://wiki.gnome.org/Projects/Vino
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	avahi-devel >= 0.6.18
BuildRequires:	avahi-glib-devel >= 0.6.18
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnutls-devel >= 2.2.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	libgcrypt-devel >= 1.2.0
BuildRequires:	libjpeg-devel
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libsecret-devel
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.16
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-glib-devel >= 0.18.0
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires(post,postun):	glib2 >= 1:2.32.0
Requires:	glib2 >= 1:2.32.0
Requires:	gnutls >= 2.2.0
Requires:	libgcrypt >= 1.2.0
Requires:	telepathy-glib >= 0.18.0
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
Vino is a VNC server for GNOME. It allows remote users to connect to a
running GNOME session using VNC.

%description -l pl.UTF-8
Vino to serwer VNC dla GNOME. Pozwala zdalnym użytkownikom na łączenie
się z działającą sesją GNOME przy użyciu VNC.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-ipv6 \
	--disable-schemas-compile \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README docs/TODO docs/remote-desktop.txt
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/vino-server
%{systemduserunitdir}/vino-server.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Vino.service
%{_datadir}/glib-2.0/schemas/org.gnome.Vino.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Vino.gschema.xml
%{_datadir}/telepathy/clients/Vino.client
%{_desktopdir}/vino-server.desktop

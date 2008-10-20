Summary:	A remote desktop system for GNOME
Summary(pl.UTF-8):	System zdalnego pulpitu dla GNOME
Name:		vino
Version:	2.24.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	http://ftp.gnome.org/pub/GNOME/sources/vino/2.24/%{name}-%{version}.tar.bz2
# Source0-md5:	b373292a7a5443d7fad1cce5eb07f37f
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avahi-glib-devel >= 0.6.18
BuildRequires:	dbus-devel >= 1.2.3
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-keyring-devel >= 2.24.0
BuildRequires:	gnutls-devel >= 1.0.0
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgcrypt-devel >= 1.2.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.24.0
BuildRequires:	libjpeg-devel
BuildRequires:	libnotify-devel >= 0.4.4
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	unique-devel >= 1.0.0
BuildRequires:	zlib-devel
Requires(post,postun):	gtk+2
Requires(post,preun):	GConf2
Requires:	libgnomeui >= 2.24.0
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
	--enable-avahi \
	--enable-ipv6 \
	--enable-gnome-keyring \
	--enable-libnotify \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install vino-server.schemas

%preun
%gconf_schema_uninstall vino-server.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README docs/TODO docs/remote-desktop.txt
%attr(755,root,root) %{_bindir}/vino-passwd
%attr(755,root,root) %{_bindir}/vino-preferences
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/vino-server
%dir %{_datadir}/vino
%{_datadir}/vino/*.glade
%{_datadir}/gnome/autostart/vino-server.desktop
%{_desktopdir}/vino-preferences.desktop
%{_sysconfdir}/gconf/schemas/vino-server.schemas

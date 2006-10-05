Summary:	A remote desktop system for GNOME
Summary(pl):	System zdalnego pulpitu dla GNOME
Name:		vino
Version:	2.16.0
Release:	1
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://ftp.gnome.org/pub/gnome/sources/vino/2.16/%{name}-%{version}.tar.bz2
# Source0-md5:	89937e6d6cd8f658d037da0a7cfd3f4e
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.16.0
BuildRequires:	ORBit2-devel >= 2.14.3
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnutls-devel >= 1.0.0
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgcrypt-devel >= 1.2.0
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.16.1
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	zlib-devel
Requires(post,preun):	GConf2 >= 2.16.0
Requires:	libgnomeui >= 2.16.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
Vino is a VNC server for GNOME. It allows remote users to connect to a
running GNOME session using VNC.

%description -l pl
Vino to serwer VNC dla GNOME. Pozwala zdalnym u¿ytkownikom na ³±czenie
siê z dzia³aj±c± sesj± GNOME przy u¿yciu VNC.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	LIBS="-lgnutls"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# stuff we don't want
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome/vino/vino-client.*

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/ug

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install vino-server.schemas

%preun
%gconf_schema_install vino-server.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README docs/TODO docs/remote-desktop.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/vino-server
%dir %{_datadir}/gnome/vino
%{_datadir}/gnome/vino/*.glade
%{_desktopdir}/*.desktop
%{_iconsdir}/*/*/apps/*.png
%{_libdir}/bonobo/servers/*.server
%{_sysconfdir}/gconf/schemas/vino-server.schemas

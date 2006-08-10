Summary:	A remote desktop system for GNOME
Summary(pl):	System zdalnego pulpitu dla GNOME
Name:		vino
Version:	2.13.5
Release:	4
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://ftp.gnome.org/pub/gnome/sources/vino/2.13/%{name}-%{version}.tar.bz2
# Source0-md5:	9bc8c3f0e639fdc7b9ed023501308359
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	ORBit2-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnutls-devel >= 1.0.0
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool
BuildRequires:	libgcrypt-devel >= 1.2.0
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui-devel >= 2.14.0
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	zlib-devel
Requires(post,preun):	GConf2 >= 2.14.0
Requires:	libgnomeui >= 2.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
Vino is a VNC server for GNOME. It allows remote users to connect to a
running GNOME session using VNC.

%description -l pl
Vino to serwer VNC dla GNOME. Pozwala zdalnym u�ytkownikom na ��czenie
si� z dzia�aj�c� sesj� GNOME przy u�yciu VNC.

%prep
%setup -q
%patch0 -p1

%build
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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

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

Summary:	A remote desktop system for GNOME
Summary(pl):	System zdalnego pulpitu dla GNOME
Name:		vino
Version:	2.7.91
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://ftp.gnome.org/pub/GNOME/sources/vino/2.7/%{name}-%{version}.tar.bz2
# Source0-md5:	667f5562d252e7a53f62f1cc6aa7db0d
Patch0:		%{name}-locale-names.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.6.0
BuildRequires:	ORBit2-devel
BuildRequires:	autoconf
BuildRequires:	automake
Buildrequires:	gnome-common >= 2.4.0
BuildRequires:	gnutls-devel >= 1.0.0
BuildRequires:	gtk+2-devel >= 2.4.0
BuildRequires:	libgcrypt-devel >= 1.1.90
BuildRequires:	libglade2-devel >= 2.3.6
BuildRequires:	libgnomeui-devel >= 2.6.0
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	zlib-devel
Requires(post):	GConf2 >= 2.6.0
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

mv po/{no,nb}.po

%build
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gnome/capplets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/control-center-2.0/capplets/*.desktop \
	$RPM_BUILD_ROOT%{_datadir}/gnome/capplets

# stuff we don't want
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome/vino/vino-client.*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README docs/TODO docs/remote-desktop.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/vino-server
%dir %{_datadir}/gnome/vino
%{_datadir}/gnome/vino/*.glade
%{_datadir}/gnome/capplets/*.desktop
%{_pixmapsdir}/*.png
%{_libdir}/bonobo/servers/*.server
%{_sysconfdir}/gconf/schemas/*.schemas

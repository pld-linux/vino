Summary:	A remote desktop system for GNOME
Summary(pl):	System zdalnego pulpitu dla GNOME
Name:		vino
Version:	2.7.4
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://ftp.gnome.org/pub/GNOME/sources/vino/2.7/%{name}-%{version}.tar.bz2
# Source0-md5:	359d5bc52be64bedb2d8af42bdff2f0c
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.6.0
BuildRequires:	gtk+2-devel >= 2.4.0
BuildRequires:	libgcrypt-devel
BuildRequires:	libglade2-devel >= 2.3.6
BuildRequires:	libgnomeui-devel >= 2.6.0
Requires(post):	GConf2 >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vino is a VNC server for GNOME. It allows remote users to connect to a
running GNOME session using VNC.

%description -l pl
Vino to serwer VNC dla GNOME. Pozwala zdalnym u¿ytkownikom na ³±czenie
siê z dzia³aj±c± sesj± GNOME przy u¿yciu VNC.

%prep
%setup -q

%build
%configure \
	--disable-gnutls
# --disable-session-support
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

desktop-file-install --vendor gnome --delete-original                   \
  --dir $RPM_BUILD_ROOT%{_datadir}/control-center-2.0/capplets          \
  --add-only-show-in GNOME                                              \
  --add-category X-Red-Hat-Base                                         \
  $RPM_BUILD_ROOT%{_datadir}/control-center-2.0/capplets/vino-preferences.desktop

# stuff we don't want
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome/vino/vino-client.*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README docs/TODO docs/remote-desktop.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/gnome/vino
%{_datadir}/gnome/vino/*.glade
%{_datadir}/control-center-2.0/capplets/*.desktop
%{_pixmapsdir}/*.png
%{_libdir}/bonobo/servers/*.server
%{_libexecdir}/*
%{_sysconfdir}/gconf/schemas/*.schemas

Name: girl
Version: 6.0.0      
Release: 1%{?dist}
Summary: GNOME Internet Radio Locator program       

License: GPLv2+       
URL: http://www.ping.uio.no/~oka/src/girl/ 
Source0: https://download.gnome.org/sources/girl/6.0/%{name}-%{version}.tar.xz        
Patch0: girl-incorrect-fsf-address.patch    

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: gnome-vfs2-devel
BuildRequires: libgnomeui-devel
BuildRequires: libgnome-devel
BuildRequires: libxml2-devel
BuildRequires: gtk2-devel
BuildRequires: intltool
BuildRequires: itstool

Requires: streamripper
Requires: totem 

%description
GIRL is a GNOME Internet Radio Locator program that allows the user
to easily find and record live radio programs on radio broadcasters
on the Internet.

GIRL is developed on the GNOME platform and it requires at least
one audio player such as Videos to be installed for playback and
streamripper for recording.

Enjoy Internet Radio.

%prep
%setup -q
%patch0 -p1

%build
%configure
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%post
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :

%files -f %{name}.lang
%doc AUTHORS LETTER NEWS README TODO VERSION YP-DIRS ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*
%{_datadir}/help/*/%{name}/*

%changelog
* Mon Aug  3 2015 Maxim Orlov <murmansksity@gmail.com> - 6.0.0-1
- Initial package.

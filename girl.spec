Name:          girl
Version:       7.0.0
Release:       1%{?dist}
Summary:       GNOME Internet Radio Locator

License:       GPLv2+
URL:           https://wiki.gnome.org/Apps/Girl
Source0:       https://download.gnome.org/sources/%{name}/7.0/%{name}-%{version}.tar.xz
# main dependencies
BuildRequires: gcc
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libgnomeui-2.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(gnome-vfs-2.0)
BuildRequires: pkgconfig(libgnome-2.0)
BuildRequires: intltool
BuildRequires: itstool
# check
BuildRequires: /usr/bin/desktop-file-validate
BuildRequires: /usr/bin/appstream-util

Recommends:    streamripper
Requires:      totem

%description
GIRL is a GNOME Internet Radio Locator program that allows the user
to easily find and record live radio programs on radio broadcasters
on the Internet.

GIRL is developed on the GNOME platform and it requires at least
one audio player such as Videos to be installed for playback and
streamripper for recording.

%prep
%autosetup

%build
%configure --with-recording
%make_build V=1

%install
%make_install

%find_lang %{name} --with-gnome

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :

%files -f %{name}.lang
%license COPYING
%doc AUTHORS LETTER NEWS README TODO VERSION YP-DIRS ChangeLog THANKS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Jan 07 2016 Maxim Orlov <murmansksity@gmail.com> - 7.0.0-1.R
- Update to 7.0.0

* Wed Nov 11 2015 Maxim Orlov <murmansksity@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Tue Aug 04 2015 Maxim Orlov <murmansksity@gmail.com> - 6.0.0-3
- Add BuildRequires: pkgconfig(libgnome-2.0)

* Mon Aug 03 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.0.0-2
- Fixes many issues and cleanups in spec

* Mon Aug 03 2015 Maxim Orlov <murmansksity@gmail.com> - 6.0.0-1
- Initial package.

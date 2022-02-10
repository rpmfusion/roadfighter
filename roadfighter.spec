Name:           roadfighter
Version:        1.0.1269
Release:        24%{?dist}
Summary:        Konami's Road Fighter remake

# http://www.braingames.getput.com/forum/forum_posts.asp?TID=678&PN=1
License:        Distributable
URL:            http://roadfighter.jorito.net/
Source0:        http://braingames.jorito.net/roadfighter/downloads/%{name}.src_%{version}.tgz
Source1:        %{name}.sh
Source2:        %{name}.appdata.xml
Patch0:         %{name}-1.0.1269-Makefile.patch
Patch1:         %{name}-1.0.1269-fix-string-format-bug.patch 
Patch2:         %{name}-1.0.1269-build-fix.patch

BuildRequires:  gcc-c++
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_sound-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme


%description
This is a remake of a car-based arcade game developed by Konami and released 
in 1984. The goal is to reach the finish line within the stages without 
running out of time, hitting other cars or running out of fuel.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# Fix char encondig
iconv --from=ISO-8859-1 --to=UTF-8 readme.txt > readme.txt.utf8
touch -r readme.txt readme.txt.utf8
mv readme.txt.utf8 readme.txt


%build
%set_build_flags
%make_build


%install
# Install wrapper script
install -d %{buildroot}%{_bindir}
install -m 755 -p %{SOURCE1} %{buildroot}%{_bindir}/%{name}

# Install game and data
install -d %{buildroot}%{_libexecdir}/%{name}
install -m 755 -p %{name} %{buildroot}%{_libexecdir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
cp -pr fonts graphics maps sound %{buildroot}%{_datadir}/%{name}

# Install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
convert -resize 48x48 \
  -extent 48x48 \
  -gravity center \
  -background none \
  build/linux/%{name}.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

# Install desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --set-icon=%{name} \
  --remove-category=Application \
  build/linux/%{name}.desktop

# Install AppData file
install -d %{buildroot}%{_metainfodir}
install -p -m 644 %{SOURCE2} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml


%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libexecdir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.appdata.xml
%doc readme.txt


%changelog
* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.0.1269-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.1269-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.1269-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.1269-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.1269-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Andrea Musuruane <musuruan@gmail.com> - 1.0.1269-19
- Added AppData file

* Sat Dec 14 2019 Andrea Musuruane <musuruan@gmail.com> - 1.0.1269-18
- Fixed icon directory

* Sat Dec 14 2019 Andrea Musuruane <musuruan@gmail.com> - 1.0.1269-17
- Spec file clean up

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.1269-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.1269-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.1269-14
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 1.0.1269-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.0.1269-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.0.1269-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.0.1269-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul  4 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 1.0.1269-9
- Fix FTBFS
- Rebuild for F24

* Tue Sep 30 2014 Andrea Musuruane <musuruan@gmail.com> - 1.0.1269-8
- Fix FTBFS
- Dropped obsolete Group, Buildroot, %%clean and %%defattr
- Dropped cleaning at the beginning of %%install
- Remove extension from Icon in Desktop file

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.0.1269-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.0.1269-6
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Apr 12 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.1269-5
- Rebuilt

* Thu Mar 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.1269-4
- Rebuilt for c++ ABI breakage

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.0.1269-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 07 2009 Andrea Musuruane <musuruan@gmail.com> 1.0.1269-2
- Preserved timestamps

* Thu Jul 23 2009 Andrea Musuruane <musuruan@gmail.com> 1.0.1269-1
- First release


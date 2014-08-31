Name:           roadfighter
Version:        1.0.1269
Release:        7%{?dist}
Summary:        Konami's Road Fighter remake

Group:          Amusements/Games
# http://www.braingames.getput.com/forum/forum_posts.asp?TID=678&PN=1
License:        Distributable
URL:            http://roadfighter.jorito.net/
Source0:        http://braingames.jorito.net/roadfighter/downloads/%{name}.src_%{version}.tgz
Source1:        roadfighter.sh
Patch0:         %{name}-1.0.1269-Makefile.patch 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_sound-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils 
Requires: hicolor-icon-theme


%description
This is a remake of a car-based arcade game developed by Konami and released 
in 1984. The goal is to reach the finish line within the stages without 
running out of time, hitting other cars or running out of fuel.


%prep
%setup -q
%patch0 -p1

# Fix char encondig
iconv --from=ISO-8859-1 --to=UTF-8 readme.txt > readme.txt.utf8
touch -r readme.txt readme.txt.utf8
mv readme.txt.utf8 readme.txt


%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}


%install
rm -rf %{buildroot}

# Install wrapper script
install -d %{buildroot}%{_bindir}
install -m 755 -p %{SOURCE1} %{buildroot}%{_bindir}/%{name}

# Install game and data
install -d %{buildroot}%{_libexecdir}/%{name}
install -m 755 -p %{name} %{buildroot}%{_libexecdir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
cp -pr fonts graphics maps sound %{buildroot}%{_datadir}/%{name}

# Install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
convert -resize 32x32 \
  -frame 0x3 \
  -mattecolor '#dfdfdf' \
  -transparent '#dfdfdf' \
  build/linux/roadfighter.png \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

# Install desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  build/linux/%{name}.desktop


%clean
rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libexecdir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%doc readme.txt


%changelog
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


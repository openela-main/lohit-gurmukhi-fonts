%global fontname lohit-gurmukhi
%global fontconf0 65-0-%{fontname}.conf
%global fontconf1 30-%{fontname}.conf
%global metainfo io.pagure.lohit.gurmukhi.font.metainfo


Name:           %{fontname}-fonts
Version:        2.91.2
Release:        3%{?dist}
Summary:        Free Gurmukhi truetype font for Punjabi language

License:        OFL
URL:            https://pagure.io/lohit
Source0:        https://releases.pagure.org/lohit/%{fontname}-%{version}.tar.gz
Source1:        %{name}.conf
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
BuildRequires: python3-devel
Requires:       fontpackages-filesystem
Provides:       lohit-punjabi-fonts = %{version}-%{release}
Obsoletes:      lohit-punjabi-fonts < 2.5.3-5


%description
This package provides a free Gurmukhi script truetype font for Punjabi language.


%prep
%setup -q -n %{fontname}-%{version}
# To make it default font for 'or' language.
mv 66-%{fontname}.conf 65-0-%{fontname}.conf

%build
make ttf %{?_smp_mflags}

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf0} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf0}
ln -s %{_fontconfig_templatedir}/%{fontconf0} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf0}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf1}
ln -s %{_fontconfig_templatedir}/%{fontconf1} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf1}

# Add AppStream metadata
install -Dm 0644 -p %{metainfo}.xml \
       %{buildroot}%{_datadir}/metainfo/%{metainfo}.xml

%_font_pkg -f *.conf  *.ttf

%doc ChangeLog COPYRIGHT OFL.txt AUTHORS README test-gurmukhi.txt
%{_datadir}/metainfo/%{metainfo}.xml

%changelog
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Pravin Satpute <psatpute@redhat.com> - 2.91.2-1
- Upstream new release 2.91.2
- Update metainfo file with latest specifications
- Changed location of metainfo to /usr/share/metainfo

* Tue Mar 14 2017 Pravin Satpute <psatpute@redhat.com> - 2.91.1-1
- Added  BuildRequires: python3-devel.
- Resolves: #1423904 - FTBFS in rawhide.
- Migrated from fedorahosted.org to pagure.io.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 27 2014 Pravin Satpute <psatpute@redhat.com> - 2.91.0-5
- Added metainfo for gnome-software

* Fri Sep 05 2014 Pravin Satpute <psatpute@redhat.com> - 2.91.0-4
- Updated obsolete version rhbz#1138266

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 11 2014 Pravin Satpute <psatpute@redhat.com> - 2.91.0-2
- Updated spec file as per review comments rhbz#1073376

* Thu Feb 27 2014 Pravin Satpute <psatpute@redhat.com> - 2.91.0-1
- Initial Upstream release with font name change
- Renamed Lohit Punjabi to Lohit Gurmukhi.
- First release of Gurmukhi after re-writing all rules.
Technical improvements
- Supports guru and gur2 open type script tags.
- Follows AGL specification syntax.
- Open type rules are available in .fea file for easy reusability
- Open type gsub lookups reduction from 10 to 8.
- Corrected glyph class of all glyphs.
- Renamed anchors to GRAnchor.
- Improved positioning of U+0A71.
Designing improvements
- Improved shape of aivowelguru, oovowelguru, auvowelguru,aivowelguru_tippiguru, oovowelguru_tippiguru, auvowelguru_tippiguru,aivowelguru_addakguru, oovowelguru_addakguru,auvowelguru_addakguru, oovowelguru_bindiguru, auvowelguru_bindiguru.
- "Copy Reference" feature implemented for better reusability of glyphs.
- Improved grid fitting(GASP) table.
Testing
- Tested with Harfbuzz NG and Uniscribe (W8)
- Test file available with release tarball
- Auto test integrated with Makefile ($make test)

* Fri Aug 30 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-3
- Resolved bug 1002380: Improved positioning of U0A71

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jan 31 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-1
- Upstream release 2.5.3

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-2
- Resolved bug #803259

* Mon Apr 23 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-1
- Upstream new release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Pravin Satpute <psatpute@redhat.com> - 2.5.0-2
- Upadated fontconf priority from 66 to 65-0, bug #683122

* Mon Oct 10 2011 Pravin Satpute <psatpute@redhat.com> - 2.5.0-1
- Upstream new release with relicensing to OFL

* Wed Apr 13 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.4-4
- Resolved bug 692366

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 08 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.4-2
- resolved bug 673418, added rupee sign

* Wed Mar 31 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.4-1
- upstream new release

* Sun Dec 13 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-3
- fixed bug 548686, license field

* Fri Sep 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-2
- updated specs

* Fri Sep 11 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-1
- first release after lohit-fonts split in new tarball

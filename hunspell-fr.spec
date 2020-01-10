Name: hunspell-fr
Summary: French hunspell dictionaries
Version: 4.6
Release: 4%{?dist}
Source: http://www.dicollecte.org/download/fr/hunspell-fr-classique+reforme1990-v%{version}.zip
Group: Applications/Text
URL: http://www.dicollecte.org/home.php?prj=fr
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: MPLv2.0
BuildArch: noarch

Requires: hunspell

%description
French (France, Belgium, etc.) hunspell dictionaries.

%prep
%setup -q -c -n hunspell-fr

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p fr-classique+reforme1990.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/fr_FR.dic
cp -p fr-classique+reforme1990.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/fr_FR.aff

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
fr_FR_aliases="fr_BE fr_CA fr_CH fr_LU fr_MC"
for lang in $fr_FR_aliases; do
	ln -s fr_FR.aff $lang.aff
	ln -s fr_FR.dic $lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_fr.txt
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 4.6-4
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 02 2012 Caolán McNamara <caolanm@redhat.com> - 4.6-2
- licences is mplv2.0 now

* Wed Sep 12 2012 Caolán McNamara <caolanm@redhat.com> - 4.6-1
- latest version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 14 2012 Caolán McNamara <caolanm@redhat.com> - 4.5-1
- latest version

* Fri Mar 09 2012 Caolán McNamara <caolanm@redhat.com> - 4.4.1-1
- latest version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Caolán McNamara <caolanm@redhat.com> - 4.3-1
- latest version

* Mon Apr 08 2011 Caolán McNamara <caolanm@redhat.com> - 4.2-1
- latest version

* Sat Apr 02 2011 Caolán McNamara <caolanm@redhat.com> - 4.1-1
- latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 20 2011 Caolán McNamara <caolanm@redhat.com> - 4.0.1-1
- latest version

* Sun Jan 09 2011 Caolán McNamara <caolanm@redhat.com> - 4.0-1
- latest version

* Mon Aug 09 2010 Caolán McNamara <caolanm@redhat.com> - 3.8-1
- latest version

* Wed May 05 2010 Caolán McNamara <caolanm@redhat.com> - 3.7-1
- latest version

* Tue Jan 26 2010 Caolán McNamara <caolanm@redhat.com> - 3.5-1
- latest version

* Thu Oct 01 2009 Caolán McNamara <caolanm@redhat.com> - 3.4.1-1
- latest version

* Fri Sep 11 2009 Caolán McNamara <caolanm@redhat.com> - 3.4-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Caolán McNamara <caolanm@redhat.com> - 3.2-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 02 2008 Caolán McNamara <caolanm@redhat.com> - 2.3.2-1
- latest version

* Tue Apr 22 2008 Caolán McNamara <caolanm@redhat.com> - 2.3.1-1
- latest version

* Mon Mar 10 2008 Caolán McNamara <caolanm@redhat.com> - 2.2.0-1
- latest version

* Thu Feb 07 2008 Caolán McNamara <caolanm@redhat.com> - 2.1.0-1
- latest version

* Fri Dec 21 2007 Caolán McNamara <caolanm@redhat.com> - 2.0.5-1
- project moved to http://dico.savant.free.fr and a new release

* Fri Aug 03 2007 Caolán McNamara <caolanm@redhat.com> - 0.20060915-2
- clarify license version

* Thu Dec 07 2006 Caolán McNamara <caolanm@redhat.com> - 0.20060915-1
- initial version

%{?scl:%scl_package jnr-enxio}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

Name:           %{?scl_prefix}jnr-enxio
Version:        0.9
Release:        3.2%{?dist}
Summary:        Unix sockets for Java
Group:          Development/Libraries
# src/main/java/jnr/enxio/channels/PollSelectionKey.java is LGPLv3
# rest of the source code is ASL 2.0
License:        ASL 2.0 and LGPLv3
URL:            http://github.com/jnr/%{pkg_name}/
Source0:        https://github.com/jnr/%{pkg_name}/archive/%{version}.tar.gz
Source1:	MANIFEST.MF
Patch0:		add-manifest.patch
BuildArch:      noarch


BuildRequires:  %{?scl_prefix_java_common}jpackage-utils
BuildRequires:  %{?scl_prefix}jnr-constants
BuildRequires:  %{?scl_prefix}jnr-ffi

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix_maven}maven-compiler-plugin
BuildRequires:  %{?scl_prefix_maven}maven-install-plugin
BuildRequires:  %{?scl_prefix_maven}maven-jar-plugin
BuildRequires:  %{?scl_prefix_maven}maven-javadoc-plugin
BuildRequires:  %{?scl_prefix_maven}maven-surefire-plugin
BuildRequires:  %{?scl_prefix_maven}maven-surefire-provider-junit

Requires:       %{?scl_prefix}jnr-constants
Requires:       %{?scl_prefix}jnr-ffi

%description
Unix sockets for Java.

%package javadoc
Summary:        Javadocs for %{pkg_name}
Group:          Documentation

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%setup -n %{pkg_name}-%{version} -q
cp %{SOURCE1} .
%patch0

find ./ -name '*.jar' -delete
find ./ -name '*.class' -delete
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc LICENSE
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Thu Aug 20 2015 Mat Booth <mat.booth@redhat.com> - 0.9-3.2
- Fix unowned directories

* Thu Aug 20 2015 Mat Booth <mat.booth@redhat.com> - 0.9-3.1
- Import latest from Fedora

* Wed Jun 17 2015 Jeff Johnston <jjohnstn@redhat.com> - 0.9-3
- Add proper MANIFEST.MF.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 5 2015 Alexander Kurtakov <akurtako@redhat.com> 0.9-1
- Update to upstream 0.9.

* Thu Apr 30 2015 Alexander Kurtakov <akurtako@redhat.com> 0.8-1
- Update to upstream 0.8.

* Fri Jun 27 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.3-7
- Fix FTBFS due to XMvn changes in F21 (#1106957)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 0.3-5
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 08 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3-3
- Document the multiple licensing scenario.

* Fri Feb 08 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3-2
- The license is in fact ASL 2.0 and LGPLv3.
- Properly use the dist tag.

* Wed Feb 06 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3-1
- Initial package.

#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Filter-NSNormalise
Summary:	XML::Filter::NSNormalise - SAX filter to normalise namespace prefixes
Summary(pl):	XML::Filter::NSNormalise - filtr SAX normalizuj±cy prefiksy przestrzeni nazw
Name:		perl-XML-Filter-NSNormalise
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6d42b4b4df10bce96a6a8a57bab99f4d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-NamespaceSupport >= 1.08
BuildRequires:	perl-XML-SAX >= 0.11
BuildRequires:	perl-XML-SAX-Writer >= 0.44
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This SAX (version 2) filter can be used to transform documents to
ensure the prefixes associated with namespaces are used consistently.

%description -l pl
Ten filtr SAX (w wersji 2) mo¿e byæ u¿ywany do przekszta³cania
dokumentów w celu upewnienia siê, ¿e prefiksy powi±zane z
przestrzeniami nazw s± u¿ywane spójnie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/XML/*/*.pm
%{_mandir}/man3/*

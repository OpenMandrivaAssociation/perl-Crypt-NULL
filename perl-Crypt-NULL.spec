%define real_name Crypt-NULL

Summary:	Crypt-NULL module for perl 
Name:		perl-%{real_name}
Version:	1.02
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch

%description
The NULL Encryption Algorithm is a symmetric block cipher described
in RFC 2410 by Rob Glenn and Stephen Kent.
This module implements NULL encryption. It supports the Crypt::CBC
interface, with several functions.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Crypt/NULL.pm
%{_mandir}/*/*



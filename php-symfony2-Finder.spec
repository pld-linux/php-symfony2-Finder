%define		pearname	Finder
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Finder Component
Name:		php-symfony2-Finder
Version:	2.4.8
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{pearname}/archive/v%{version}/%{pearname}-%{version}.tar.gz
# Source0-md5:	a3e79e931dc045af730c5b4ba4b2bf35
URL:		http://symfony.com/doc/2.4/components/finder.html
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-pear >= 1.3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Finder Component finds files and directories via an intuitive
fluent interface.

%prep
%setup -q -n %{pearname}-%{version}


%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_pear_dir}/Symfony/Component/Finder
%{php_pear_dir}/Symfony/Component/Finder/*.php
%{php_pear_dir}/Symfony/Component/Finder/Adapter
%{php_pear_dir}/Symfony/Component/Finder/Comparator
%{php_pear_dir}/Symfony/Component/Finder/Exception
%{php_pear_dir}/Symfony/Component/Finder/Expression
%{php_pear_dir}/Symfony/Component/Finder/Iterator
%{php_pear_dir}/Symfony/Component/Finder/Shell

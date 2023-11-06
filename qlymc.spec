Name:           qlymc
Version:        0.1.0
Release:        0
Summary:        Framework for gathering software quality metrics
License:        GPL-2.0
Group:          Development/Tools/Other
Url:            https://github.com/llansky3/qlymc
Source0:        _service
BuildRequires:  fdupes
BuildArch:      noarch

%description
Framework for gathering software quality metrics

%prep
%setup -q -n %_sourcedir/%name-%version -T -D

%build
%py3_build

%install
%py3_install
%fdupes %{buildroot}%{python3_sitelib}

%files
%license LICENSE
%doc README.md %{name}.changes
%{python3_sitelib}/%{name}/
%{_bindir}/%{name}

%changelog


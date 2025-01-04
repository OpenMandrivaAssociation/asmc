%undefine _debugsource_packages

Name:		asmc
Version:	2.36.16
Release:	1
Source0:	https://github.com/nidud/asmc/archive/refs/heads/master.tar.gz#/%{name}-%{version}.tar.gz
Summary:	MASM compatible x86 macro assembler
URL:		https://github.com/nidud/asmc
License:	GPL-2.0
Group:		Development/Tools
BuildRequires:	make
ExclusiveArch:	%{ix86} %{x86_64}

%patchlist
asmc-dont-force-pie.patch

%description
MASM compatible x86 macro assembler

%prep
%autosetup -p1 -n %{name}-master

%build
%make_build -j1 -C source/asmc

%install
mkdir -p %{buildroot}%{_bindir}
install -cD -m 755 source/asmc/asmc %{buildroot}%{_bindir}/
install -cD -m 755 source/asmc/asmc64 %{buildroot}%{_bindir}/

%files
%{_bindir}/asmc
%{_bindir}/asmc64

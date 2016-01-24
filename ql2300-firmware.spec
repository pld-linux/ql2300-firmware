#
%define		nameprog ql2300

Summary:	Firmware for the QLogic %{nameprog} HBA
Summary(pl.UTF-8):	Firmware dla HBA QLogic %{nameprog}
Name:		%{nameprog}-firmware
Version:	3.03.29
Release:	1
License:	distributable
Group:		Base/Kernel
Source0:	http://ldriver.qlogic.com/firmware/old/%{nameprog}_fw.bin.3.03.29
# Source0-md5:	c1fe1fa53583bc7520cf65a6b81af7e5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the firmware for the QLogic %{nameprog} driver.

%description -l pl.UTF-8
Ten pakiet zawiera firmware dla sterownika QLogic %{nameprog}.

%prep
%setup -q -c -T

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

install %{SOURCE0} $RPM_BUILD_ROOT/lib/firmware/ql2300_fw.bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/firmware/ql2300_fw.bin

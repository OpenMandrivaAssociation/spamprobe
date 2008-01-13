Summary:	A Bayesian probability spam analysis engine
Name:		spamprobe
Version:	1.4d
Release:	%mkrel 2
License:	QPL
Group:		Networking/Mail
URL:		http://www.sourceforge.net/projects/spamprobe
Source0:	http://prdownloads.sourceforge.net/spamprobe/%{name}-%{version}.tar.bz2
BuildRequires:	db4.6-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
SpamProbe is a spam detection program that uses a Bayesian
analysis of the frequencies of terms used in the email. Because it
filters email based on content rather than on general rules, it
easily adapts itself to the types of email that each individual
user normally receives. 

%prep

%setup -q

%build

%configure2_5x

%make

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc contrib ChangeLog README.txt
%doc src/scripts/*
%{_mandir}/man1/spam*
%{_bindir}/spamprobe 



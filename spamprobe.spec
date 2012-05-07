Summary:	A Bayesian probability spam analysis engine
Name:		spamprobe
Version:	1.4d
Release:	11
License:	QPL
Group:		Networking/Mail
URL:		http://www.sourceforge.net/projects/spamprobe
Source0:	http://prdownloads.sourceforge.net/spamprobe/%{name}-%{version}.tar.bz2
# http://sourceforge.net/tracker/index.php?func=detail&aid=1818489&group_id=61201&atid=496459
Patch0:		spamprobe-1.4d-with-gcc4.3.diff
BuildRequires:	db-devel
BuildRequires:	ungif-devel
BuildRequires:	jpeg-devel
BuildRequires:	png-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
SpamProbe is a spam detection program that uses a Bayesian analysis of the
frequencies of terms used in the email. Because it filters email based on
content rather than on general rules, it easily adapts itself to the types of
email that each individual user normally receives. 

%prep

%setup -q
%patch0 -p1

%build

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc contrib ChangeLog README.txt
%doc src/scripts/*
%{_mandir}/man1/spam*
%{_bindir}/spamprobe 

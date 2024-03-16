%global debug_package %{nil}

Name: cloak
Version: 2.8.0
Release: 1%{?dist}
Summary: A censorship circumvention tool to evade detection by authoritarian state adversaries
License: GPLv3
URL: https://github.com/cbeuw/Cloak
Source0: %{url}/archive/v%{version}.tar.gz
BuildRequires: gcc git golang make

%description
Cloak is a pluggable transport that enhances traditional proxy tools like
OpenVPN to evade sophisticated censorship and data discrimination.

Cloak is not a standalone proxy program. Rather, it works by masquerading
proxied traffic as normal web browsing activities. In contrast to traditional
tools which have very prominent traffic fingerprints and can be blocked by
simple filtering rules, it's very difficult to precisely target Cloak with
little false positives. This increases the collateral damage to censorship
actions as attempts to block Cloak could also damage services the censor
state relies on.

%prep
%autosetup -n Cloak-%{version}

%build
make version=v%{version}

%check
# nothing for now

%install
# bin
for BIN_NAME in ck-client ck-server; do
    install -Dpm 755 build/${BIN_NAME} %{buildroot}%{_bindir}/${BIN_NAME}
done

# example configs
for CFG_NAME in ckclient.json ckserver.json; do
    install -Dpm 644 example_config/${CFG_NAME} %{buildroot}%{_sysconfdir}/%{name}/${CFG_NAME}
done

%files
%license LICENSE
%doc README.md
%{_bindir}/ck-client
%{_bindir}/ck-server
%config %{_sysconfdir}/%{name}/*

%changelog
* Sun Mar 17 2024 spyophobia - 2.8.0-1
- Release 2.8.0

* Tue Apr 25 2023 spyophobia - 2.7.0-1
- Release 2.7.0

* Fri Mar 24 2023 spyophobia - 2.6.1-1
- Release 2.6.1

* Mon Dec 19 2022 spyophobia - 2.6.0-1
- Release 2.6.0

# **Configuração de DNS com o Bind**

# /etc/bind/named.conf.local

```c
// 
// Do any local configuration here
//

// Consider adding the 1918 zones here, if they are not used in your
// organization
// include "/etc/bind/zones.rfc1918";

// Zona de pesquisa direta
zone "empresa.net" {
    type master;
    file "/etc/bind/db.empresa.net";
};

// Zona de pesquisa reversa
zone "1.168.193.in-addr.arpa" {
    type master;
    file "/etc/bind/db.193";
};
```

# /etc/bind/named.conf.options

```c
options {
	directory "/var/cache/bind";

	// If there is a firewall between you and nameservers you want
	// to talk to, you may need to fix the firewall to allow multiple
	// ports to talk.  See http://www.kb.cert.org/vuls/id/800113

	// If your ISP provided one or more IP addresses for stable 
	// nameservers, you probably want to use them as forwarders.  
	// Uncomment the following block, and insert the addresses replacing 
	// the all-0's placeholder.

	forwarders {
		8.8.8.8;
	};

	//========================================================================
	// If BIND logs error messages about the root key being expired,
	// you will need to update your keys.  See https://www.isc.org/bind-keys
	//========================================================================
	dnssec-validation auto;

	auth-nxdomain no;    # conform to RFC1035
	listen-on-v6 { any; };
};
```

> sudo cp db.local db.empresa.net

> sudo cp db.127 db.193

# /etc/bind/db.empresa.net

```c
;
; BIND data file for local loopback interface
;
$TTL	604800
@	IN	SOA	dnspc.empresa.net. root.empresa.net. (
			      2		; Serial
			 604800		; Refresh
			  86400		; Retry
			2419200		; Expire
			 604800 )	; Negative Cache TTL
;
empresa.net.	IN	NS	dnspc.empresa.net.
empresa.net.	IN	A	193.136.1.4
;@	IN	A	127.0.0.1
;@	IN	AAAA	::1
dnspc	IN	A	193.136.1.4
router	IN	A	193.136.1.1
outer	IN	A	192.0.0.2
intra	IN	A	1.0.0.6
```

# /etc/bind/db.193

```c
;
; BIND reverse data file for local loopback interface
;
$TTL	604800
@	IN	SOA	localhost. root.localhost. (
			      1		; Serial
			 604800		; Refresh
			  86400		; Retry
			2419200		; Expire
			 604800 )	; Negative Cache TTL
;
@	IN	NS	localhost.
1.0.0	IN	PTR	localhost.

```

> sudo /etc/init.d/bind restart

> named-checkzone empresa.net /etc/bind/db.empresa.net

> named-checkzone empresa.net /etc/bind/db.192

> sudo reboot

> host -l empresa.net

> nslookup empresa.net

> dig empresa.net

> host (...)

> ping (...)
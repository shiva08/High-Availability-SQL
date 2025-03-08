import json

t = [
  {
    "offer": "SQL2008R2SP3-WS2008R2SP1",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2008R2SP3-WS2008R2SP1:Enterprise:10.72.200114",
    "version": "10.72.200114"
  },
  {
    "offer": "SQL2008R2SP3-WS2008R2SP1",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2008R2SP3-WS2008R2SP1:Enterprise:10.72.200310",
    "version": "10.72.200310"
  },
  {
    "offer": "SQL2008R2SP3-WS2008R2SP1",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2008R2SP3-WS2008R2SP1:Express:10.72.200310",
    "version": "10.72.200310"
  },
  {
    "offer": "SQL2008R2SP3-WS2008R2SP1",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2008R2SP3-WS2008R2SP1:Express:10.72.200324",
    "version": "10.72.200324"
  },
  {
    "offer": "SQL2008R2SP3-WS2008R2SP1",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2008R2SP3-WS2008R2SP1:Standard:10.72.200114",
    "version": "10.72.200114"
  },
  {
    "offer": "SQL2008R2SP3-WS2008R2SP1",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2008R2SP3-WS2008R2SP1:Standard:10.72.200310",
    "version": "10.72.200310"
  },
  {
    "offer": "SQL2008R2SP3-WS2008R2SP1",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2008R2SP3-WS2008R2SP1:Web:10.72.200114",
    "version": "10.72.200114"
  },
  {
    "offer": "SQL2008R2SP3-WS2008R2SP1",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2008R2SP3-WS2008R2SP1:Web:10.72.200310",
    "version": "10.72.200310"
  },
  {
    "offer": "sql2008r2sp3-ws2008r2sp1-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2008r2sp3-ws2008r2sp1-byol:enterprise:10.72.200114",
    "version": "10.72.200114"
  },
  {
    "offer": "sql2008r2sp3-ws2008r2sp1-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2008r2sp3-ws2008r2sp1-byol:enterprise:10.72.200324",
    "version": "10.72.200324"
  },
  {
    "offer": "sql2008r2sp3-ws2008r2sp1-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2008r2sp3-ws2008r2sp1-byol:standard:10.72.191210",
    "version": "10.72.191210"
  },
  {
    "offer": "sql2008r2sp3-ws2008r2sp1-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2008r2sp3-ws2008r2sp1-byol:standard:10.72.200114",
    "version": "10.72.200114"
  },
  {
    "offer": "sql2008r2sp3-ws2008r2sp1-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2008r2sp3-ws2008r2sp1-byol:standard:10.72.200324",
    "version": "10.72.200324"
  },
  {
    "offer": "SQL2012SP4-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2012SP4-WS2012R2:Enterprise:11.1.211012",
    "version": "11.1.211012"
  },
  {
    "offer": "SQL2012SP4-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2012SP4-WS2012R2:Enterprise:11.1.211109",
    "version": "11.1.211109"
  },
  {
    "offer": "SQL2012SP4-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2012SP4-WS2012R2:Enterprise:11.1.220111",
    "version": "11.1.220111"
  },
  {
    "offer": "SQL2012SP4-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2012SP4-WS2012R2:Express:11.1.211012",
    "version": "11.1.211012"
  },
  {
    "offer": "SQL2012SP4-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2012SP4-WS2012R2:Express:11.1.211109",
    "version": "11.1.211109"
  },
  {
    "offer": "SQL2012SP4-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2012SP4-WS2012R2:Express:11.1.220111",
    "version": "11.1.220111"
  },
  {
    "offer": "SQL2012SP4-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2012SP4-WS2012R2:Standard:11.1.211012",
    "version": "11.1.211012"
  },
  {
    "offer": "SQL2012SP4-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2012SP4-WS2012R2:Standard:11.1.211109",
    "version": "11.1.211109"
  },
  {
    "offer": "SQL2012SP4-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2012SP4-WS2012R2:Standard:11.1.220111",
    "version": "11.1.220111"
  },
  {
    "offer": "SQL2012SP4-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2012SP4-WS2012R2:Web:11.1.211012",
    "version": "11.1.211012"
  },
  {
    "offer": "SQL2012SP4-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2012SP4-WS2012R2:Web:11.1.211109",
    "version": "11.1.211109"
  },
  {
    "offer": "SQL2012SP4-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2012SP4-WS2012R2:Web:11.1.220111",
    "version": "11.1.220111"
  },
  {
    "offer": "SQL2012SP4-WS2012R2-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2012SP4-WS2012R2-BYOL:Enterprise:11.1.211012",
    "version": "11.1.211012"
  },
  {
    "offer": "SQL2012SP4-WS2012R2-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2012SP4-WS2012R2-BYOL:Enterprise:11.1.211109",
    "version": "11.1.211109"
  },
  {
    "offer": "SQL2012SP4-WS2012R2-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2012SP4-WS2012R2-BYOL:Enterprise:11.1.220111",
    "version": "11.1.220111"
  },
  {
    "offer": "SQL2012SP4-WS2012R2-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2012SP4-WS2012R2-BYOL:Standard:11.1.211012",
    "version": "11.1.211012"
  },
  {
    "offer": "SQL2012SP4-WS2012R2-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2012SP4-WS2012R2-BYOL:Standard:11.1.211109",
    "version": "11.1.211109"
  },
  {
    "offer": "SQL2012SP4-WS2012R2-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2012SP4-WS2012R2-BYOL:Standard:11.1.220111",
    "version": "11.1.220111"
  },
  {
    "offer": "SQL2014SP2-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2014SP2-WS2012R2:Enterprise:12.21.210713",
    "version": "12.21.210713"
  },
  {
    "offer": "SQL2014SP2-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2014SP2-WS2012R2:Enterprise:12.21.210810",
    "version": "12.21.210810"
  },
  {
    "offer": "SQL2014SP2-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2014SP2-WS2012R2:Enterprise:12.21.210914",
    "version": "12.21.210914"
  },
  {
    "offer": "SQL2014SP2-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2014SP2-WS2012R2:Express:12.21.210713",
    "version": "12.21.210713"
  },
  {
    "offer": "SQL2014SP2-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2014SP2-WS2012R2:Express:12.21.210810",
    "version": "12.21.210810"
  },
  {
    "offer": "SQL2014SP2-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2014SP2-WS2012R2:Express:12.21.210914",
    "version": "12.21.210914"
  },
  {
    "offer": "SQL2014SP2-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2014SP2-WS2012R2:Standard:12.21.210713",
    "version": "12.21.210713"
  },
  {
    "offer": "SQL2014SP2-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2014SP2-WS2012R2:Standard:12.21.210810",
    "version": "12.21.210810"
  },
  {
    "offer": "SQL2014SP2-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2014SP2-WS2012R2:Standard:12.21.210914",
    "version": "12.21.210914"
  },
  {
    "offer": "SQL2014SP2-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2014SP2-WS2012R2:Web:12.21.210713",
    "version": "12.21.210713"
  },
  {
    "offer": "SQL2014SP2-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2014SP2-WS2012R2:Web:12.21.210810",
    "version": "12.21.210810"
  },
  {
    "offer": "SQL2014SP2-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2014SP2-WS2012R2:Web:12.21.210914",
    "version": "12.21.210914"
  },
  {
    "offer": "SQL2014SP2-WS2012R2-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2014SP2-WS2012R2-BYOL:Enterprise:12.21.210312",
    "version": "12.21.210312"
  },
  {
    "offer": "SQL2014SP2-WS2012R2-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2014SP2-WS2012R2-BYOL:Enterprise:12.21.210713",
    "version": "12.21.210713"
  },
  {
    "offer": "SQL2014SP2-WS2012R2-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2014SP2-WS2012R2-BYOL:Enterprise:12.21.210810",
    "version": "12.21.210810"
  },
  {
    "offer": "SQL2014SP2-WS2012R2-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2014SP2-WS2012R2-BYOL:Enterprise:12.21.210914",
    "version": "12.21.210914"
  },
  {
    "offer": "SQL2014SP2-WS2012R2-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2014SP2-WS2012R2-BYOL:Standard:12.21.210312",
    "version": "12.21.210312"
  },
  {
    "offer": "SQL2014SP2-WS2012R2-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2014SP2-WS2012R2-BYOL:Standard:12.21.210713",
    "version": "12.21.210713"
  },
  {
    "offer": "SQL2014SP2-WS2012R2-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2014SP2-WS2012R2-BYOL:Standard:12.21.210810",
    "version": "12.21.210810"
  },
  {
    "offer": "SQL2014SP2-WS2012R2-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2014SP2-WS2012R2-BYOL:Standard:12.21.210914",
    "version": "12.21.210914"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:enterprise:12.21.200114",
    "version": "12.21.200114"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:enterprise:12.21.201013",
    "version": "12.21.201013"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:enterprise:12.21.201110",
    "version": "12.21.201110"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:enterprise:12.21.211109",
    "version": "12.21.211109"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:enterprise:12.21.220111",
    "version": "12.21.220111"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "express",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:express:12.21.200114",
    "version": "12.21.200114"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "express",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:express:12.21.201013",
    "version": "12.21.201013"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "express",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:express:12.21.201110",
    "version": "12.21.201110"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "express",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:express:12.21.211109",
    "version": "12.21.211109"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "express",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:express:12.21.220111",
    "version": "12.21.220111"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:sqldev:12.21.200114",
    "version": "12.21.200114"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:sqldev:12.21.201013",
    "version": "12.21.201013"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:sqldev:12.21.201110",
    "version": "12.21.201110"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:sqldev:12.21.211109",
    "version": "12.21.211109"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:sqldev:12.21.220111",
    "version": "12.21.220111"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:standard:12.21.200114",
    "version": "12.21.200114"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:standard:12.21.201013",
    "version": "12.21.201013"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:standard:12.21.201110",
    "version": "12.21.201110"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:standard:12.21.211109",
    "version": "12.21.211109"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:standard:12.21.220111",
    "version": "12.21.220111"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:web:12.21.200114",
    "version": "12.21.200114"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:web:12.21.201013",
    "version": "12.21.201013"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:web:12.21.201110",
    "version": "12.21.201110"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:web:12.21.211109",
    "version": "12.21.211109"
  },
  {
    "offer": "sql2014sp3-ws2012r2",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2:web:12.21.220111",
    "version": "12.21.220111"
  },
  {
    "offer": "sql2014sp3-ws2012r2-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2-byol:enterprise:12.21.200114",
    "version": "12.21.200114"
  },
  {
    "offer": "sql2014sp3-ws2012r2-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2-byol:enterprise:12.21.201013",
    "version": "12.21.201013"
  },
  {
    "offer": "sql2014sp3-ws2012r2-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2-byol:enterprise:12.21.201110",
    "version": "12.21.201110"
  },
  {
    "offer": "sql2014sp3-ws2012r2-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2-byol:enterprise:12.21.211109",
    "version": "12.21.211109"
  },
  {
    "offer": "sql2014sp3-ws2012r2-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2-byol:enterprise:12.21.220111",
    "version": "12.21.220111"
  },
  {
    "offer": "sql2014sp3-ws2012r2-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2-byol:standard:12.21.200114",
    "version": "12.21.200114"
  },
  {
    "offer": "sql2014sp3-ws2012r2-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2-byol:standard:12.21.200310",
    "version": "12.21.200310"
  },
  {
    "offer": "sql2014sp3-ws2012r2-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2-byol:standard:12.21.201013",
    "version": "12.21.201013"
  },
  {
    "offer": "sql2014sp3-ws2012r2-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2-byol:standard:12.21.201110",
    "version": "12.21.201110"
  },
  {
    "offer": "sql2014sp3-ws2012r2-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2-byol:standard:12.21.211109",
    "version": "12.21.211109"
  },
  {
    "offer": "sql2014sp3-ws2012r2-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2014sp3-ws2012r2-byol:standard:12.21.220111",
    "version": "12.21.220111"
  },
  {
    "offer": "SQL2016SP1-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016:Enterprise:13.2.210810",
    "version": "13.2.210810"
  },
  {
    "offer": "SQL2016SP1-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016:Enterprise:13.2.210914",
    "version": "13.2.210914"
  },
  {
    "offer": "SQL2016SP1-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016:Enterprise:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "SQL2016SP1-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprisedbengineonly",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016:enterprisedbengineonly:13.2.190910",
    "version": "13.2.190910"
  },
  {
    "offer": "SQL2016SP1-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016:Express:13.2.210810",
    "version": "13.2.210810"
  },
  {
    "offer": "SQL2016SP1-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016:Express:13.2.210914",
    "version": "13.2.210914"
  },
  {
    "offer": "SQL2016SP1-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016:Express:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "SQL2016SP1-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016:SQLDEV:13.2.210810",
    "version": "13.2.210810"
  },
  {
    "offer": "SQL2016SP1-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016:SQLDEV:13.2.210914",
    "version": "13.2.210914"
  },
  {
    "offer": "SQL2016SP1-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016:SQLDEV:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "SQL2016SP1-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016:Standard:13.2.210810",
    "version": "13.2.210810"
  },
  {
    "offer": "SQL2016SP1-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016:Standard:13.2.210914",
    "version": "13.2.210914"
  },
  {
    "offer": "SQL2016SP1-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016:Standard:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "SQL2016SP1-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "standarddbengineonly",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016:standarddbengineonly:13.2.190220",
    "version": "13.2.190220"
  },
  {
    "offer": "SQL2016SP1-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016:Web:13.2.210810",
    "version": "13.2.210810"
  },
  {
    "offer": "SQL2016SP1-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016:Web:13.2.210914",
    "version": "13.2.210914"
  },
  {
    "offer": "SQL2016SP1-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016:Web:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "SQL2016SP1-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016-BYOL:Enterprise:13.2.210810",
    "version": "13.2.210810"
  },
  {
    "offer": "SQL2016SP1-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016-BYOL:Enterprise:13.2.210914",
    "version": "13.2.210914"
  },
  {
    "offer": "SQL2016SP1-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016-BYOL:Enterprise:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "SQL2016SP1-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016-BYOL:Standard:13.2.210810",
    "version": "13.2.210810"
  },
  {
    "offer": "SQL2016SP1-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016-BYOL:Standard:13.2.210914",
    "version": "13.2.210914"
  },
  {
    "offer": "SQL2016SP1-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2016SP1-WS2016-BYOL:Standard:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "SQL2016SP2-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2012R2:Enterprise:13.2.190214",
    "version": "13.2.190214"
  },
  {
    "offer": "SQL2016SP2-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2012R2:Express:13.2.190214",
    "version": "13.2.190214"
  },
  {
    "offer": "SQL2016SP2-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2012R2:SQLDEV:13.2.190214",
    "version": "13.2.190214"
  },
  {
    "offer": "SQL2016SP2-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2012R2:Standard:13.2.190214",
    "version": "13.2.190214"
  },
  {
    "offer": "SQL2016SP2-WS2012R2",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2012R2:Web:13.2.190214",
    "version": "13.2.190214"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:Enterprise:13.2.201013",
    "version": "13.2.201013"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:Enterprise:13.2.201110",
    "version": "13.2.201110"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:Enterprise:13.2.210218",
    "version": "13.2.210218"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:Enterprise:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:Enterprise:13.2.220111",
    "version": "13.2.220111"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprisedbengineonly",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:enterprisedbengineonly:13.2.201013",
    "version": "13.2.201013"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprisedbengineonly",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:enterprisedbengineonly:13.2.201110",
    "version": "13.2.201110"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprisedbengineonly",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:enterprisedbengineonly:13.2.210218",
    "version": "13.2.210218"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprisedbengineonly",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:enterprisedbengineonly:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprisedbengineonly",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:enterprisedbengineonly:13.2.220111",
    "version": "13.2.220111"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:Express:13.2.201013",
    "version": "13.2.201013"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:Express:13.2.201110",
    "version": "13.2.201110"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:Express:13.2.210218",
    "version": "13.2.210218"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:Express:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:Express:13.2.220111",
    "version": "13.2.220111"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:SQLDEV:13.2.201013",
    "version": "13.2.201013"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:SQLDEV:13.2.201110",
    "version": "13.2.201110"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:SQLDEV:13.2.210218",
    "version": "13.2.210218"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:SQLDEV:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:SQLDEV:13.2.220111",
    "version": "13.2.220111"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:Standard:13.2.201013",
    "version": "13.2.201013"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:Standard:13.2.201110",
    "version": "13.2.201110"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:Standard:13.2.210218",
    "version": "13.2.210218"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:Standard:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:Standard:13.2.220111",
    "version": "13.2.220111"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "standarddbengineonly",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:standarddbengineonly:13.2.201013",
    "version": "13.2.201013"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "standarddbengineonly",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:standarddbengineonly:13.2.201110",
    "version": "13.2.201110"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "standarddbengineonly",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:standarddbengineonly:13.2.210218",
    "version": "13.2.210218"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "standarddbengineonly",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:standarddbengineonly:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "standarddbengineonly",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:standarddbengineonly:13.2.220111",
    "version": "13.2.220111"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:Web:13.2.201013",
    "version": "13.2.201013"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:Web:13.2.201110",
    "version": "13.2.201110"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:Web:13.2.210218",
    "version": "13.2.210218"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:Web:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "SQL2016SP2-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016:Web:13.2.220111",
    "version": "13.2.220111"
  },
  {
    "offer": "SQL2016SP2-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016-BYOL:Enterprise:13.2.201013",
    "version": "13.2.201013"
  },
  {
    "offer": "SQL2016SP2-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016-BYOL:Enterprise:13.2.201110",
    "version": "13.2.201110"
  },
  {
    "offer": "SQL2016SP2-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016-BYOL:Enterprise:13.2.210218",
    "version": "13.2.210218"
  },
  {
    "offer": "SQL2016SP2-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016-BYOL:Enterprise:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "SQL2016SP2-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016-BYOL:Enterprise:13.2.220111",
    "version": "13.2.220111"
  },
  {
    "offer": "SQL2016SP2-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016-BYOL:Standard:13.2.201013",
    "version": "13.2.201013"
  },
  {
    "offer": "SQL2016SP2-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016-BYOL:Standard:13.2.201110",
    "version": "13.2.201110"
  },
  {
    "offer": "SQL2016SP2-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016-BYOL:Standard:13.2.210218",
    "version": "13.2.210218"
  },
  {
    "offer": "SQL2016SP2-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016-BYOL:Standard:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "SQL2016SP2-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2016SP2-WS2016-BYOL:Standard:13.2.220111",
    "version": "13.2.220111"
  },
  {
    "offer": "sql2016sp2-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2016sp2-ws2019:enterprise:13.2.191028",
    "version": "13.2.191028"
  },
  {
    "offer": "sql2016sp2-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2016sp2-ws2019:enterprise:13.2.210218",
    "version": "13.2.210218"
  },
  {
    "offer": "sql2016sp2-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2016sp2-ws2019:enterprise:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "sql2016sp2-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "express",
    "urn": "MicrosoftSQLServer:sql2016sp2-ws2019:express:13.2.210218",
    "version": "13.2.210218"
  },
  {
    "offer": "sql2016sp2-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "express",
    "urn": "MicrosoftSQLServer:sql2016sp2-ws2019:express:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "sql2016sp2-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2016sp2-ws2019:sqldev:13.2.210218",
    "version": "13.2.210218"
  },
  {
    "offer": "sql2016sp2-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2016sp2-ws2019:sqldev:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "sql2016sp2-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2016sp2-ws2019:standard:13.2.191028",
    "version": "13.2.191028"
  },
  {
    "offer": "sql2016sp2-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2016sp2-ws2019:standard:13.2.210218",
    "version": "13.2.210218"
  },
  {
    "offer": "sql2016sp2-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2016sp2-ws2019:standard:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "sql2016sp2-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2016sp2-ws2019:web:13.2.191028",
    "version": "13.2.191028"
  },
  {
    "offer": "sql2016sp2-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2016sp2-ws2019:web:13.2.210218",
    "version": "13.2.210218"
  },
  {
    "offer": "sql2016sp2-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2016sp2-ws2019:web:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "sql2016sp2-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2016sp2-ws2019-byol:enterprise:13.2.191028",
    "version": "13.2.191028"
  },
  {
    "offer": "sql2016sp2-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2016sp2-ws2019-byol:enterprise:13.2.210218",
    "version": "13.2.210218"
  },
  {
    "offer": "sql2016sp2-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2016sp2-ws2019-byol:enterprise:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "sql2016sp2-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2016sp2-ws2019-byol:standard:13.2.191028",
    "version": "13.2.191028"
  },
  {
    "offer": "sql2016sp2-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2016sp2-ws2019-byol:standard:13.2.210218",
    "version": "13.2.210218"
  },
  {
    "offer": "sql2016sp2-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2016sp2-ws2019-byol:standard:13.2.211109",
    "version": "13.2.211109"
  },
  {
    "offer": "sql2016sp3-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2016sp3-ws2019:enterprise:13.0.211109",
    "version": "13.0.211109"
  },
  {
    "offer": "sql2016sp3-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2016sp3-ws2019:enterprise:13.2.220111",
    "version": "13.2.220111"
  },
  {
    "offer": "sql2016sp3-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2016sp3-ws2019:sqldev:13.0.211109",
    "version": "13.0.211109"
  },
  {
    "offer": "sql2016sp3-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2016sp3-ws2019:sqldev:13.2.220111",
    "version": "13.2.220111"
  },
  {
    "offer": "sql2016sp3-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2016sp3-ws2019:standard:13.0.211109",
    "version": "13.0.211109"
  },
  {
    "offer": "sql2016sp3-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2016sp3-ws2019:standard:13.2.220111",
    "version": "13.2.220111"
  },
  {
    "offer": "sql2016sp3-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2016sp3-ws2019:web:13.0.211109",
    "version": "13.0.211109"
  },
  {
    "offer": "sql2016sp3-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2016sp3-ws2019:web:13.2.220111",
    "version": "13.2.220111"
  },
  {
    "offer": "SQL2017-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2017-RHEL7:Enterprise:14.1.200811",
    "version": "14.1.200811"
  },
  {
    "offer": "SQL2017-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2017-RHEL7:Enterprise:14.1.200908",
    "version": "14.1.200908"
  },
  {
    "offer": "SQL2017-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2017-RHEL7:Enterprise:14.1.201013",
    "version": "14.1.201013"
  },
  {
    "offer": "SQL2017-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2017-RHEL7:Express:14.1.200811",
    "version": "14.1.200811"
  },
  {
    "offer": "SQL2017-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2017-RHEL7:Express:14.1.200908",
    "version": "14.1.200908"
  },
  {
    "offer": "SQL2017-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2017-RHEL7:Express:14.1.201013",
    "version": "14.1.201013"
  },
  {
    "offer": "SQL2017-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2017-RHEL7:SQLDEV:14.1.200811",
    "version": "14.1.200811"
  },
  {
    "offer": "SQL2017-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2017-RHEL7:SQLDEV:14.1.200908",
    "version": "14.1.200908"
  },
  {
    "offer": "SQL2017-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2017-RHEL7:SQLDEV:14.1.201013",
    "version": "14.1.201013"
  },
  {
    "offer": "SQL2017-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2017-RHEL7:Standard:14.1.200811",
    "version": "14.1.200811"
  },
  {
    "offer": "SQL2017-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2017-RHEL7:Standard:14.1.200908",
    "version": "14.1.200908"
  },
  {
    "offer": "SQL2017-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2017-RHEL7:Standard:14.1.201013",
    "version": "14.1.201013"
  },
  {
    "offer": "SQL2017-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2017-RHEL7:Web:14.1.200811",
    "version": "14.1.200811"
  },
  {
    "offer": "SQL2017-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2017-RHEL7:Web:14.1.200908",
    "version": "14.1.200908"
  },
  {
    "offer": "SQL2017-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2017-RHEL7:Web:14.1.201013",
    "version": "14.1.201013"
  },
  {
    "offer": "sql2017-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2017-rhel8:enterprise:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "sql2017-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2017-rhel8:enterprise:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "sql2017-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2017-rhel8:enterprise:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "sql2017-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2017-rhel8:sqldev:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "sql2017-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2017-rhel8:sqldev:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "sql2017-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2017-rhel8:sqldev:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "sql2017-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2017-rhel8:standard:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "sql2017-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2017-rhel8:standard:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "sql2017-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2017-rhel8:standard:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "sql2017-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2017-rhel8:web:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "sql2017-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2017-rhel8:web:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "sql2017-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2017-rhel8:web:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "SQL2017-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2017-Ubuntu1604:Enterprise:14.1.210511",
    "version": "14.1.210511"
  },
  {
    "offer": "SQL2017-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2017-Ubuntu1604:Enterprise:14.1.210608",
    "version": "14.1.210608"
  },
  {
    "offer": "SQL2017-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2017-Ubuntu1604:Enterprise:14.1.210713",
    "version": "14.1.210713"
  },
  {
    "offer": "SQL2017-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2017-Ubuntu1604:Enterprise:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "SQL2017-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2017-Ubuntu1604:Express:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "SQL2017-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2017-Ubuntu1604:SQLDEV:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "SQL2017-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2017-Ubuntu1604:Standard:14.1.210511",
    "version": "14.1.210511"
  },
  {
    "offer": "SQL2017-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2017-Ubuntu1604:Standard:14.1.210608",
    "version": "14.1.210608"
  },
  {
    "offer": "SQL2017-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2017-Ubuntu1604:Standard:14.1.210713",
    "version": "14.1.210713"
  },
  {
    "offer": "SQL2017-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2017-Ubuntu1604:Standard:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "SQL2017-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2017-Ubuntu1604:Web:14.1.210511",
    "version": "14.1.210511"
  },
  {
    "offer": "SQL2017-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2017-Ubuntu1604:Web:14.1.210608",
    "version": "14.1.210608"
  },
  {
    "offer": "SQL2017-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2017-Ubuntu1604:Web:14.1.210713",
    "version": "14.1.210713"
  },
  {
    "offer": "SQL2017-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2017-Ubuntu1604:Web:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "sql2017-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2017-ubuntu1804:enterprise:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "sql2017-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2017-ubuntu1804:enterprise:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "sql2017-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2017-ubuntu1804:enterprise:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "sql2017-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2017-ubuntu1804:sqldev:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "sql2017-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2017-ubuntu1804:sqldev:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "sql2017-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2017-ubuntu1804:sqldev:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "sql2017-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2017-ubuntu1804:standard:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "sql2017-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2017-ubuntu1804:standard:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "sql2017-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2017-ubuntu1804:standard:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "sql2017-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2017-ubuntu1804:web:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "sql2017-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2017-ubuntu1804:web:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "sql2017-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2017-ubuntu1804:web:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:Enterprise:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:Enterprise:14.1.210914",
    "version": "14.1.210914"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:Enterprise:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:Enterprise:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:Enterprise:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise-gen2",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:enterprise-gen2:14.1.200128",
    "version": "14.1.200128"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise-gen2",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:enterprise-gen2:14.1.210218",
    "version": "14.1.210218"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprisedbengineonly",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:enterprisedbengineonly:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprisedbengineonly",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:enterprisedbengineonly:14.1.210914",
    "version": "14.1.210914"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprisedbengineonly",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:enterprisedbengineonly:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprisedbengineonly",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:enterprisedbengineonly:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprisedbengineonly",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:enterprisedbengineonly:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:Express:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:Express:14.1.210914",
    "version": "14.1.210914"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:Express:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:Express:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Express",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:Express:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:SQLDEV:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:SQLDEV:14.1.210914",
    "version": "14.1.210914"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:SQLDEV:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:SQLDEV:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:SQLDEV:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev-gen2",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:sqldev-gen2:14.1.200128",
    "version": "14.1.200128"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev-gen2",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:sqldev-gen2:14.1.210218",
    "version": "14.1.210218"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:Standard:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:Standard:14.1.210914",
    "version": "14.1.210914"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:Standard:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:Standard:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:Standard:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard-gen2",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:standard-gen2:14.1.200128",
    "version": "14.1.200128"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard-gen2",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:standard-gen2:14.1.210218",
    "version": "14.1.210218"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "standarddbengineonly",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:standarddbengineonly:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "standarddbengineonly",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:standarddbengineonly:14.1.210914",
    "version": "14.1.210914"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "standarddbengineonly",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:standarddbengineonly:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "standarddbengineonly",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:standarddbengineonly:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "standarddbengineonly",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:standarddbengineonly:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:Web:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:Web:14.1.210914",
    "version": "14.1.210914"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:Web:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:Web:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "SQL2017-WS2016",
    "publisher": "MicrosoftSQLServer",
    "sku": "Web",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016:Web:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "SQL2017-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016-BYOL:Enterprise:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "SQL2017-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016-BYOL:Enterprise:14.1.210914",
    "version": "14.1.210914"
  },
  {
    "offer": "SQL2017-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016-BYOL:Enterprise:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "SQL2017-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016-BYOL:Enterprise:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "SQL2017-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Enterprise",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016-BYOL:Enterprise:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "SQL2017-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016-BYOL:Standard:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "SQL2017-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016-BYOL:Standard:14.1.210914",
    "version": "14.1.210914"
  },
  {
    "offer": "SQL2017-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016-BYOL:Standard:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "SQL2017-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016-BYOL:Standard:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "SQL2017-WS2016-BYOL",
    "publisher": "MicrosoftSQLServer",
    "sku": "Standard",
    "urn": "MicrosoftSQLServer:SQL2017-WS2016-BYOL:Standard:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:enterprise:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:enterprise:14.1.210914",
    "version": "14.1.210914"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:enterprise:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:enterprise:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:enterprise:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise-gen2",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:enterprise-gen2:14.1.200211",
    "version": "14.1.200211"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise-gen2",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:enterprise-gen2:14.1.210218",
    "version": "14.1.210218"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprisedbengineonly",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:enterprisedbengineonly:14.1.200512",
    "version": "14.1.200512"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprisedbengineonly",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:enterprisedbengineonly:14.1.210218",
    "version": "14.1.210218"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "express",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:express:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "express",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:express:14.1.210914",
    "version": "14.1.210914"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "express",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:express:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "express",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:express:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "express",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:express:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:sqldev:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:sqldev:14.1.210914",
    "version": "14.1.210914"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:sqldev:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:sqldev:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:sqldev:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:standard:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:standard:14.1.210914",
    "version": "14.1.210914"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:standard:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:standard:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:standard:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:web:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:web:14.1.210914",
    "version": "14.1.210914"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:web:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:web:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "sql2017-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2017-ws2019:web:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "sql2017-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2017-ws2019-byol:enterprise:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "sql2017-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2017-ws2019-byol:enterprise:14.1.210914",
    "version": "14.1.210914"
  },
  {
    "offer": "sql2017-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2017-ws2019-byol:enterprise:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "sql2017-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2017-ws2019-byol:enterprise:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "sql2017-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2017-ws2019-byol:enterprise:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "sql2017-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2017-ws2019-byol:standard:14.1.210810",
    "version": "14.1.210810"
  },
  {
    "offer": "sql2017-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2017-ws2019-byol:standard:14.1.210914",
    "version": "14.1.210914"
  },
  {
    "offer": "sql2017-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2017-ws2019-byol:standard:14.1.211012",
    "version": "14.1.211012"
  },
  {
    "offer": "sql2017-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2017-ws2019-byol:standard:14.1.211109",
    "version": "14.1.211109"
  },
  {
    "offer": "sql2017-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2017-ws2019-byol:standard:14.1.220111",
    "version": "14.1.220111"
  },
  {
    "offer": "SQL2019-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:SQL2019-RHEL7:enterprise:15.0.200114",
    "version": "15.0.200114"
  },
  {
    "offer": "SQL2019-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:SQL2019-RHEL7:enterprise:15.0.200211",
    "version": "15.0.200211"
  },
  {
    "offer": "SQL2019-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:SQL2019-RHEL7:enterprise:15.0.200310",
    "version": "15.0.200310"
  },
  {
    "offer": "SQL2019-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2019-RHEL7:SQLDEV:15.0.200114",
    "version": "15.0.200114"
  },
  {
    "offer": "SQL2019-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2019-RHEL7:SQLDEV:15.0.200211",
    "version": "15.0.200211"
  },
  {
    "offer": "SQL2019-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2019-RHEL7:SQLDEV:15.0.200310",
    "version": "15.0.200310"
  },
  {
    "offer": "SQL2019-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:SQL2019-RHEL7:standard:15.0.200114",
    "version": "15.0.200114"
  },
  {
    "offer": "SQL2019-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:SQL2019-RHEL7:standard:15.0.200211",
    "version": "15.0.200211"
  },
  {
    "offer": "SQL2019-RHEL7",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:SQL2019-RHEL7:standard:15.0.200310",
    "version": "15.0.200310"
  },
  {
    "offer": "sql2019-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-rhel8:enterprise:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-rhel8:enterprise:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-rhel8:enterprise:15.0.220111",
    "version": "15.0.220111"
  },
  {
    "offer": "sql2019-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2019-rhel8:sqldev:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2019-rhel8:sqldev:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2019-rhel8:sqldev:15.0.220111",
    "version": "15.0.220111"
  },
  {
    "offer": "sql2019-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-rhel8:standard:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-rhel8:standard:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-rhel8:standard:15.0.220111",
    "version": "15.0.220111"
  },
  {
    "offer": "sql2019-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2019-rhel8:web:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2019-rhel8:web:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-rhel8",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2019-rhel8:web:15.0.220111",
    "version": "15.0.220111"
  },
  {
    "offer": "sql2019-sles12sp5",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-sles12sp5:enterprise:15.0.210914",
    "version": "15.0.210914"
  },
  {
    "offer": "sql2019-sles12sp5",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-sles12sp5:enterprise:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-sles12sp5",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-sles12sp5:enterprise:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-sles12sp5",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2019-sles12sp5:sqldev:15.0.210914",
    "version": "15.0.210914"
  },
  {
    "offer": "sql2019-sles12sp5",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2019-sles12sp5:sqldev:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-sles12sp5",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2019-sles12sp5:sqldev:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-sles12sp5",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-sles12sp5:standard:15.0.210914",
    "version": "15.0.210914"
  },
  {
    "offer": "sql2019-sles12sp5",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-sles12sp5:standard:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-sles12sp5",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-sles12sp5:standard:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-sles12sp5",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2019-sles12sp5:web:15.0.210914",
    "version": "15.0.210914"
  },
  {
    "offer": "sql2019-sles12sp5",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2019-sles12sp5:web:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-sles12sp5",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2019-sles12sp5:web:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "SQL2019-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:SQL2019-Ubuntu1604:enterprise:15.0.200114",
    "version": "15.0.200114"
  },
  {
    "offer": "SQL2019-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:SQL2019-Ubuntu1604:enterprise:15.0.200211",
    "version": "15.0.200211"
  },
  {
    "offer": "SQL2019-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:SQL2019-Ubuntu1604:enterprise:15.0.200310",
    "version": "15.0.200310"
  },
  {
    "offer": "SQL2019-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2019-Ubuntu1604:SQLDEV:15.0.200114",
    "version": "15.0.200114"
  },
  {
    "offer": "SQL2019-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2019-Ubuntu1604:SQLDEV:15.0.200211",
    "version": "15.0.200211"
  },
  {
    "offer": "SQL2019-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "SQLDEV",
    "urn": "MicrosoftSQLServer:SQL2019-Ubuntu1604:SQLDEV:15.0.200310",
    "version": "15.0.200310"
  },
  {
    "offer": "SQL2019-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:SQL2019-Ubuntu1604:standard:15.0.200114",
    "version": "15.0.200114"
  },
  {
    "offer": "SQL2019-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:SQL2019-Ubuntu1604:standard:15.0.200211",
    "version": "15.0.200211"
  },
  {
    "offer": "SQL2019-Ubuntu1604",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:SQL2019-Ubuntu1604:standard:15.0.200310",
    "version": "15.0.200310"
  },
  {
    "offer": "sql2019-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu1804:enterprise:15.0.210810",
    "version": "15.0.210810"
  },
  {
    "offer": "sql2019-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu1804:enterprise:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu1804:enterprise:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu1804:sqldev:15.0.210810",
    "version": "15.0.210810"
  },
  {
    "offer": "sql2019-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu1804:sqldev:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu1804:sqldev:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu1804:standard:15.0.210810",
    "version": "15.0.210810"
  },
  {
    "offer": "sql2019-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu1804:standard:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu1804:standard:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu1804:web:15.0.210810",
    "version": "15.0.210810"
  },
  {
    "offer": "sql2019-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu1804:web:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-ubuntu1804",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu1804:web:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-ubuntu2004",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu2004:enterprise:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-ubuntu2004",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu2004:enterprise:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-ubuntu2004",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu2004:enterprise:15.0.220111",
    "version": "15.0.220111"
  },
  {
    "offer": "sql2019-ubuntu2004",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu2004:sqldev:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-ubuntu2004",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu2004:sqldev:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-ubuntu2004",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu2004:sqldev:15.0.220111",
    "version": "15.0.220111"
  },
  {
    "offer": "sql2019-ubuntu2004",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu2004:standard:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-ubuntu2004",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu2004:standard:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-ubuntu2004",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu2004:standard:15.0.220111",
    "version": "15.0.220111"
  },
  {
    "offer": "sql2019-ubuntu2004",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu2004:web:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-ubuntu2004",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu2004:web:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-ubuntu2004",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2019-ubuntu2004:web:15.0.220111",
    "version": "15.0.220111"
  },
  {
    "offer": "sql2019-ubuntupro2004",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise_upro",
    "urn": "MicrosoftSQLServer:sql2019-ubuntupro2004:enterprise_upro:15.0.211020",
    "version": "15.0.211020"
  },
  {
    "offer": "sql2019-ubuntupro2004",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev_upro",
    "urn": "MicrosoftSQLServer:sql2019-ubuntupro2004:sqldev_upro:15.0.211020",
    "version": "15.0.211020"
  },
  {
    "offer": "sql2019-ubuntupro2004",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard_upro",
    "urn": "MicrosoftSQLServer:sql2019-ubuntupro2004:standard_upro:15.0.211020",
    "version": "15.0.211020"
  },
  {
    "offer": "sql2019-ubuntupro2004",
    "publisher": "MicrosoftSQLServer",
    "sku": "web_upro",
    "urn": "MicrosoftSQLServer:sql2019-ubuntupro2004:web_upro:15.0.211020",
    "version": "15.0.211020"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:enterprise:15.0.210810",
    "version": "15.0.210810"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:enterprise:15.0.210914",
    "version": "15.0.210914"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:enterprise:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:enterprise:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:enterprise:15.0.220111",
    "version": "15.0.220111"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprisedbengineonly",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:enterprisedbengineonly:15.0.210810",
    "version": "15.0.210810"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprisedbengineonly",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:enterprisedbengineonly:15.0.210914",
    "version": "15.0.210914"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprisedbengineonly",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:enterprisedbengineonly:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprisedbengineonly",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:enterprisedbengineonly:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprisedbengineonly",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:enterprisedbengineonly:15.0.220111",
    "version": "15.0.220111"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprisedbengineonly-gen2",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:enterprisedbengineonly-gen2:15.0.200512",
    "version": "15.0.200512"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprisedbengineonly-gen2",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:enterprisedbengineonly-gen2:15.0.210218",
    "version": "15.0.210218"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:sqldev:15.0.210810",
    "version": "15.0.210810"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:sqldev:15.0.210914",
    "version": "15.0.210914"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:sqldev:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:sqldev:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:sqldev:15.0.220111",
    "version": "15.0.220111"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:standard:15.0.210810",
    "version": "15.0.210810"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:standard:15.0.210914",
    "version": "15.0.210914"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:standard:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:standard:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:standard:15.0.220111",
    "version": "15.0.220111"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "standarddbengineonly",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:standarddbengineonly:15.0.210810",
    "version": "15.0.210810"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "standarddbengineonly",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:standarddbengineonly:15.0.210914",
    "version": "15.0.210914"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "standarddbengineonly",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:standarddbengineonly:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "standarddbengineonly",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:standarddbengineonly:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "standarddbengineonly",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:standarddbengineonly:15.0.220111",
    "version": "15.0.220111"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:web:15.0.210810",
    "version": "15.0.210810"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:web:15.0.210914",
    "version": "15.0.210914"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:web:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:web:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-ws2019",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2019-ws2019:web:15.0.220111",
    "version": "15.0.220111"
  },
  {
    "offer": "sql2019-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-ws2019-byol:enterprise:15.0.210810",
    "version": "15.0.210810"
  },
  {
    "offer": "sql2019-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-ws2019-byol:enterprise:15.0.210914",
    "version": "15.0.210914"
  },
  {
    "offer": "sql2019-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-ws2019-byol:enterprise:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-ws2019-byol:enterprise:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-ws2019-byol:enterprise:15.0.220111",
    "version": "15.0.220111"
  },
  {
    "offer": "sql2019-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-ws2019-byol:standard:15.0.210810",
    "version": "15.0.210810"
  },
  {
    "offer": "sql2019-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-ws2019-byol:standard:15.0.210914",
    "version": "15.0.210914"
  },
  {
    "offer": "sql2019-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-ws2019-byol:standard:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-ws2019-byol:standard:15.0.211109",
    "version": "15.0.211109"
  },
  {
    "offer": "sql2019-ws2019-byol",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-ws2019-byol:standard:15.0.220111",
    "version": "15.0.220111"
  },
  {
    "offer": "sql2019-ws2022",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-ws2022:enterprise:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-ws2022",
    "publisher": "MicrosoftSQLServer",
    "sku": "enterprise",
    "urn": "MicrosoftSQLServer:sql2019-ws2022:enterprise:15.0.220111",
    "version": "15.0.220111"
  },
  {
    "offer": "sql2019-ws2022",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2019-ws2022:sqldev:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-ws2022",
    "publisher": "MicrosoftSQLServer",
    "sku": "sqldev",
    "urn": "MicrosoftSQLServer:sql2019-ws2022:sqldev:15.0.220111",
    "version": "15.0.220111"
  },
  {
    "offer": "sql2019-ws2022",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-ws2022:standard:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-ws2022",
    "publisher": "MicrosoftSQLServer",
    "sku": "standard",
    "urn": "MicrosoftSQLServer:sql2019-ws2022:standard:15.0.220111",
    "version": "15.0.220111"
  },
  {
    "offer": "sql2019-ws2022",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2019-ws2022:web:15.0.211012",
    "version": "15.0.211012"
  },
  {
    "offer": "sql2019-ws2022",
    "publisher": "MicrosoftSQLServer",
    "sku": "web",
    "urn": "MicrosoftSQLServer:sql2019-ws2022:web:15.0.220111",
    "version": "15.0.220111"
  }
]

# On azure cli , run az vm image list --all --publisher MicrosoftSQLServer >>p.txt
# Find images for windows server
# if SQL >= 2016, SKU should be in enterprise, standard, developer
# if SQL >= 2012, SKU should be in enterprise, developer

offers = []
for b in t:
    a = b["offer"]
    p = a.index('-')
    # AG works with WS>=2012
    if a[p+1:p+3].lower()=="ws" and int(a[3:7])>=2012:  
      # if int(a[3:7])>=2016:
      #   if b["sku"].lower() in ["enterprise","standard","developer"]:
      #     offers += [a.upper()]
      # elif int(a[3:7])>=2012:
      if b["sku"].lower() in ["enterprise","developer"]:
        offers += [a.upper()]

print(sorted(list(set(offers))))
    

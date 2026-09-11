#!/usr/bin/env python3
"""Samscaped static site generator. Outputs to ./public for Cloudflare Pages."""
import hashlib
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")
DOMAIN = "https://samscaped.com"  # TODO: confirm final domain
PHONE = "(330) 578-5085"
PHONE_TEL = "+13305785085"
EMAIL = "samscaped@outlook.com"
GBP = "https://maps.app.goo.gl/uvKDxwjGTd1u3Eym6"

CSS = """
:root{--green:#2C5E1A;--deep:#16300C;--green-lt:#5E9C3F;--tint:#F2F5EC;--yellow:#F2B722;--ink:#1E231A;--muted:#5C6355;--r:10px;--shadow:0 8px 24px rgba(22,48,12,.10);--shadow-lg:0 16px 40px rgba(22,48,12,.16)}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:'Barlow',Arial,sans-serif;color:var(--ink);line-height:1.65;background:#fff;-webkit-font-smoothing:antialiased}
h1,h2,h3{font-family:'Barlow Condensed',Arial,sans-serif;text-transform:uppercase;letter-spacing:.5px;line-height:1.05;color:var(--deep)}
h1{font-size:clamp(2.4rem,5.4vw,4rem);font-weight:800}
h2{font-size:clamp(1.7rem,3.6vw,2.5rem);font-weight:700;margin-bottom:.6rem}
h3{font-size:1.3rem;font-weight:700}
p{margin-bottom:1rem}
a{color:var(--green)}
img{max-width:100%;display:block}
:focus-visible{outline:3px solid var(--yellow);outline-offset:3px;border-radius:3px}
.wrap{max-width:1120px;margin:0 auto;padding:0 22px}
/* stripe accent */
.stripe-bar{height:7px;background:repeating-linear-gradient(115deg,var(--green) 0 14px,var(--green-lt) 14px 28px)}
h2 .rule,.rule{display:block;width:64px;height:5px;margin-bottom:18px;background:repeating-linear-gradient(115deg,var(--green) 0 8px,var(--green-lt) 8px 16px);border-radius:2px}
/* topbar */
.topbar{background:var(--deep);color:#DCE6D2;font-size:.88rem;padding:7px 0;letter-spacing:.2px}
.topbar .wrap{display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px}
.topbar a{color:#fff;text-decoration:none;font-weight:600}
.topbar a:hover{color:var(--yellow)}
/* header */
header{background:#fff;position:sticky;top:0;z-index:60;box-shadow:0 1px 0 rgba(22,48,12,.10);transition:box-shadow .25s}
header.shrunk{box-shadow:0 4px 18px rgba(22,48,12,.12)}
.nav{display:flex;align-items:center;justify-content:space-between;padding:16px 0;flex-wrap:wrap;gap:12px;transition:padding .25s}
header.shrunk .nav{padding:8px 0}
.logo{display:block;line-height:0}
.logo-svg{height:60px;width:auto;transition:height .25s}
header.shrunk .logo-svg{height:46px}
nav ul{display:flex;list-style:none;gap:2px;flex-wrap:wrap;align-items:center}
nav a{display:block;padding:11px 14px;text-decoration:none;color:var(--ink);font-weight:600;font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;font-size:1.08rem;letter-spacing:.6px;border-radius:6px}
nav a:hover{color:var(--green);background:var(--tint)}
/* mobile menu toggle (CSS-only, no JS) */
.nav-toggle{position:absolute;width:1px;height:1px;opacity:0;margin:0}
.burger{display:none;order:2;flex:none;width:46px;height:46px;border-radius:8px;cursor:pointer;align-items:center;justify-content:center}
.burger i{display:block;width:24px;height:2px;background:var(--deep);position:relative}
.burger i:before,.burger i:after{content:"";position:absolute;left:0;width:24px;height:2px;background:var(--deep);transition:transform .2s}
.burger i:before{top:-7px}
.burger i:after{top:7px}
.nav-toggle:focus-visible+.burger{outline:3px solid var(--yellow);outline-offset:3px}
/* buttons */
.btn{display:inline-block;background:var(--yellow);color:var(--deep)!important;font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;font-weight:800;font-size:1.12rem;letter-spacing:.6px;padding:15px 28px;text-decoration:none;border-radius:var(--r);border:none;cursor:pointer;box-shadow:0 4px 14px rgba(242,183,34,.28);transition:transform .15s,box-shadow .15s,filter .15s}
.btn:hover{filter:brightness(1.05);transform:translateY(-2px);box-shadow:0 8px 20px rgba(242,183,34,.34)}
.btn:active{transform:translateY(0);box-shadow:0 2px 8px rgba(242,183,34,.3)}
nav .btn{padding:12px 22px}
.btn-outline{background:transparent;border:2px solid rgba(255,255,255,.75);color:#fff!important;box-shadow:none}
.btn-outline:hover{background:rgba(255,255,255,.14);box-shadow:none}
/* HERO */
.hero{position:relative;overflow:hidden;background:linear-gradient(115deg,var(--deep) 0%,#245012 55%,var(--green) 100%);color:#fff;padding:104px 0 92px;isolation:isolate}
.hero-media{position:absolute;inset:0;z-index:-2;background-image:url('/assets/hero.jpg');background-size:cover;background-position:center;transform:scale(1.0)}
.hero-scrim{position:absolute;inset:0;z-index:-1;background:linear-gradient(105deg,rgba(22,48,12,.94) 0%,rgba(22,48,12,.72) 45%,rgba(44,94,26,.34) 100%)}
.hero h1{color:#fff;max-width:850px;text-shadow:0 2px 20px rgba(0,0,0,.28)}
.hero p{max-width:640px;font-size:1.18rem;margin:18px 0 28px;color:#E9F0E1}
.hero .eyebrow{font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;letter-spacing:3px;font-weight:700;font-size:1rem;color:var(--yellow);margin-bottom:12px}
.hero .cta-row{display:flex;gap:14px;flex-wrap:wrap}
.trust-row{display:flex;gap:28px;flex-wrap:wrap;margin-top:34px;padding-top:24px;border-top:1px solid rgba(255,255,255,.2)}
.trust-row span{display:flex;align-items:center;gap:9px;font-weight:600;font-size:.98rem;color:#E9F0E1}
.trust-row svg{flex:none;width:20px;height:20px;fill:var(--yellow)}
/* google strip */
.gstrip{background:var(--tint);padding:18px 0}
.gstrip .wrap{display:flex;align-items:center;justify-content:center;gap:14px;flex-wrap:wrap;text-align:center}
.gstrip a{text-decoration:none;color:var(--ink);font-weight:600;display:flex;align-items:center;gap:12px;flex-wrap:wrap;justify-content:center}
.gstrip a:hover{color:var(--green)}
.stars{display:inline-flex;gap:2px}
.stars svg{width:17px;height:17px;fill:var(--yellow)}
/* sections */
section{padding:88px 0}
.tint{background:var(--tint)}
.lead{font-size:1.14rem;color:var(--muted);max-width:730px}
.grid{display:grid;gap:26px;margin-top:34px}
.grid-3{grid-template-columns:repeat(auto-fit,minmax(min(280px,100%),1fr))}
.grid-2{grid-template-columns:repeat(auto-fit,minmax(min(320px,100%),1fr))}
.quotes{grid-template-columns:repeat(2,1fr)}
/* cards */
.card{background:#fff;border:none;border-radius:var(--r);box-shadow:var(--shadow);overflow:hidden;transition:transform .2s,box-shadow .2s;display:flex;flex-direction:column}
.card:hover{transform:translateY(-4px);box-shadow:var(--shadow-lg)}
.card-img{aspect-ratio:16/9;background:linear-gradient(120deg,var(--green) 0%,var(--green-lt) 100%);background-size:cover;background-position:center;position:relative}
.card-img:after{content:"";position:absolute;inset:auto 0 0 0;height:6px;background:repeating-linear-gradient(115deg,rgba(255,255,255,.35) 0 10px,transparent 10px 20px)}
.card-body{padding:24px;flex:1;display:flex;flex-direction:column}
.card h3{margin-bottom:8px}
.card h3 a{text-decoration:none;color:var(--deep)}
.card h3 a:hover{color:var(--green)}
.card p{color:var(--muted);margin-bottom:14px}
.card .more{margin-top:auto;font-weight:700;font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;text-decoration:none;letter-spacing:.6px;color:var(--green)}
.card .more:hover{color:var(--deep)}
.card-plain .card-body{padding:28px}
/* checklist */
.checks{list-style:none;margin:16px 0 24px}
.checks li{padding-left:32px;position:relative;margin-bottom:11px}
.checks li:before{content:"";position:absolute;left:0;top:7px;width:16px;height:16px;background:var(--green);clip-path:polygon(14% 44%,0 62%,40% 100%,100% 16%,84% 4%,38% 70%)}
/* chips */
.chips{display:flex;flex-wrap:wrap;gap:11px;margin-top:20px}
.chips a{background:#fff;border:1px solid #CBD9BC;color:var(--deep);text-decoration:none;font-weight:600;padding:11px 20px;border-radius:99px;box-shadow:0 2px 6px rgba(22,48,12,.06);transition:all .15s}
.chips a:hover{background:var(--green);color:#fff;border-color:var(--green)}
.chips span{background:transparent;border:1px dashed #B9C6A9;color:var(--muted);padding:11px 20px;border-radius:99px}
/* quote band */
.quote-band{position:relative;background:linear-gradient(115deg,var(--deep) 0%,#245012 100%);color:#fff;text-align:center;padding:82px 0;overflow:hidden}
.quote-band:before{content:"";position:absolute;inset:0;background:repeating-linear-gradient(115deg,rgba(255,255,255,.035) 0 60px,transparent 60px 120px)}
.quote-band .wrap{position:relative}
.quote-band h2{color:#fff}
.quote-band p{max-width:580px;margin:14px auto 22px;color:#DCE6D2}
.quote-band .phone-big{font-family:'Barlow Condensed',sans-serif;font-size:2.4rem;font-weight:800;color:var(--yellow);text-decoration:none;display:inline-block;margin-bottom:20px;letter-spacing:1px}
.quote-band .phone-big:hover{filter:brightness(1.1)}
/* testimonials */
.quote-card{background:#fff;border-radius:var(--r);padding:28px;box-shadow:var(--shadow)}
.quote-card .stars{margin-bottom:12px}
.quote-card p{font-size:1.05rem;color:var(--ink)}
.quote-card cite{font-style:normal;font-weight:700;color:var(--deep);font-size:.95rem}
/* faq */
details{background:transparent;border:none;border-bottom:1px solid #D9E2CD;border-radius:0;margin:0;padding:20px 0}
details summary{font-weight:700;cursor:pointer;font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;font-size:1.18rem;letter-spacing:.6px;color:var(--deep);list-style:none;display:flex;justify-content:space-between;align-items:center;gap:16px}
details summary::-webkit-details-marker{display:none}
details summary:after{content:"+";color:var(--green);font-size:1.7rem;font-weight:700;line-height:1;flex:none;transition:transform .2s}
details[open] summary:after{content:"3";transform:rotate(0)}
details summary:hover{color:var(--green)}
details p{margin:14px 0 0;color:var(--muted);max-width:760px}
/* pricing */
.callout{background:#fff;border-left:5px solid var(--yellow);border-radius:var(--r);padding:22px 26px;box-shadow:var(--shadow);margin:26px 0}
.callout p{margin:0;font-size:1.08rem;font-weight:600;color:var(--deep)}
.price-table{width:100%;border-collapse:collapse;margin:24px 0;background:#fff;border-radius:var(--r);overflow:hidden;box-shadow:var(--shadow)}
.price-table th{background:var(--deep);color:#fff;font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;letter-spacing:.7px;font-size:1.05rem;padding:15px 18px;text-align:left}
.price-table td{padding:17px 18px;border-bottom:1px solid #E5EBDC;vertical-align:top}
.price-table tr:last-child td{border-bottom:none}
.price-table td:first-child{font-weight:700;color:var(--deep)}
.price-table td:nth-child(2){font-weight:600;color:var(--green);white-space:nowrap}
.price-table td:nth-child(3){color:var(--muted)}

/* before / after gallery */
.ba-grid{display:grid;gap:28px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));margin-top:34px}
.ba-item{background:#fff;border-radius:var(--r);box-shadow:var(--shadow);overflow:hidden}
.ba-pair{display:grid;grid-template-columns:1fr 1fr;gap:2px;background:#fff}
.ba-shot{position:relative;aspect-ratio:3/4;overflow:hidden}
.ba-shot img{width:100%;height:100%;object-fit:cover}
.ba-shot span{position:absolute;top:10px;left:10px;font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;font-weight:800;font-size:.82rem;letter-spacing:1.2px;padding:5px 11px;border-radius:5px}
.ba-shot.before span{background:rgba(30,35,26,.86);color:#fff}
.ba-shot.after span{background:var(--yellow);color:var(--deep)}
.ba-cap{padding:16px 20px}
.ba-cap h3{font-size:1.1rem;margin-bottom:3px}
.ba-cap p{margin:0;color:var(--muted);font-size:.95rem}
.ba-single .ba-pair{grid-template-columns:1fr}
@media(max-width:520px){.ba-grid{gap:20px}}
/* form */
.form-shell{background:#fff;border-radius:var(--r);box-shadow:var(--shadow);padding:12px}

/* quote form */
.qform{display:grid;gap:16px}
.qf-row{display:grid;gap:16px;grid-template-columns:1fr 1fr}
.qf-field{display:flex;flex-direction:column;gap:6px}
.qf-field label{font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;font-weight:700;font-size:1rem;letter-spacing:.6px;color:var(--deep)}
.qf-field label .req{color:#B3401A}
.qform input,.qform select,.qform textarea{font-family:'Barlow',sans-serif;font-size:1rem;color:var(--ink);background:#fff;border:1.5px solid #CBD9BC;border-radius:8px;padding:13px 14px;width:100%;min-height:48px}
.qform textarea{min-height:100px;resize:vertical}
.qform input:focus,.qform select:focus,.qform textarea:focus{border-color:var(--green);outline:3px solid rgba(94,156,63,.25);outline-offset:0}
.qf-checks{display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));margin-top:2px}
.qf-check{display:flex;align-items:center;gap:10px;background:var(--tint);border:1.5px solid transparent;border-radius:8px;padding:12px 14px;cursor:pointer;font-weight:600;min-height:48px}
.qf-check:hover{border-color:#CBD9BC}
.qf-check input{width:20px;height:20px;min-height:0;accent-color:var(--green);flex:none;padding:0}
.qf-check.on{border-color:var(--green);background:#E8F0DF}
.qform .btn{width:100%;font-size:1.2rem}
.qf-note{font-size:.9rem;color:var(--muted);text-align:center;margin:0}
.qf-msg{border-radius:8px;padding:16px 18px;font-weight:600;display:none}
.qf-msg.ok{display:block;background:#E8F0DF;border-left:5px solid var(--green);color:var(--deep)}
.qf-msg.err{display:block;background:#FBEDE6;border-left:5px solid #B3401A;color:#7A2A10}
.qf-hp{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}
@media(max-width:600px){.qf-row{grid-template-columns:1fr}}
/* footer */
footer{background:var(--deep);color:#C6D3B9;padding:64px 0 26px;font-size:.96rem}
footer h3{color:#fff;margin-bottom:14px;font-size:1.15rem}
footer a{color:#E4EDDA;text-decoration:none}
footer a:hover{color:var(--yellow)}
footer ul{list-style:none}
footer li{margin-bottom:8px}
.foot-grid{display:grid;gap:38px;grid-template-columns:repeat(auto-fit,minmax(210px,1fr))}
.foot-bottom{border-top:1px solid #2C4A21;margin-top:42px;padding-top:20px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;color:#93A783;font-size:.85rem}
/* mobile action bar */
.mobile-bar{display:none;position:fixed;left:0;right:0;bottom:0;z-index:80;background:#fff;box-shadow:0 -4px 18px rgba(22,48,12,.16);padding:10px;gap:10px}
.mobile-bar a{flex:1;text-align:center;padding:15px 8px;border-radius:var(--r);text-decoration:none;font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;font-weight:800;font-size:1.1rem;letter-spacing:.6px;min-height:48px}
.mobile-bar .call{background:var(--green);color:#fff}
.mobile-bar .quote{background:var(--yellow);color:var(--deep)}
/* reveal */
.reveal{opacity:1}
@media(prefers-reduced-motion:no-preference){
 .reveal{opacity:0;transform:translateY(24px);transition:opacity .6s ease,transform .6s ease}
 .reveal.in{opacity:1;transform:none}
 .hero-media{animation:kb 20s ease-out forwards}
 @keyframes kb{from{transform:scale(1.02)}to{transform:scale(1.06)}}
 .hero .eyebrow,.hero h1,.hero p,.hero .cta-row,.hero .trust-row{opacity:0;animation:rise .55s ease-out forwards}
 .hero .eyebrow{animation-delay:.05s}
 .hero h1{animation-delay:.15s}
 .hero p{animation-delay:.3s}
 .hero .cta-row{animation-delay:.45s}
 .hero .trust-row{animation-delay:.6s}
 @keyframes rise{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}
}
@media(max-width:900px){nav ul{gap:0}nav a{padding:9px 10px;font-size:1rem}}
@media(max-width:768px){
 .hero-media{background-image:url('/assets/hero-mobile.jpg');background-position:center 32%;animation:none;transform:none}
 .hero-scrim{background:linear-gradient(178deg,rgba(22,48,12,.86) 0%,rgba(22,48,12,.74) 42%,rgba(22,48,12,.90) 100%)}
 body{padding-bottom:76px}
 .mobile-bar{display:flex}
 section{padding:56px 0}
 .hero{padding:64px 0 56px}
 .logo-svg{height:44px}
 header.shrunk .logo-svg{height:40px}
 /* collapse the nav behind a toggle so the sticky header stays ~70px */
 .topbar{font-size:.8rem;padding:6px 0}
 .topbar .wrap{justify-content:center;text-align:center;gap:2px 14px}
 .nav{padding:10px 0;gap:8px}
 header.shrunk .nav{padding:6px 0}
 .burger{display:flex}
 header nav{display:none;order:3;width:100%}
 .nav-toggle:checked~nav{display:block}
 .nav-toggle:checked+.burger i{background:transparent}
 .nav-toggle:checked+.burger i:before{transform:translateY(7px) rotate(45deg)}
 .nav-toggle:checked+.burger i:after{transform:translateY(-7px) rotate(-45deg)}
 header nav ul{flex-direction:column;align-items:stretch;gap:0;padding:4px 0 14px}
 header nav a{padding:14px 6px;font-size:1.14rem;border-radius:0;border-bottom:1px solid #E5EBDC}
 header nav li:last-child a{border-bottom:none}
 nav .btn{display:block;text-align:center;margin-top:14px;padding:15px 22px}
 .gstrip{padding:14px 0}
 .gstrip a{gap:8px;font-size:.95rem}
 .quotes{grid-template-columns:1fr}
 footer li{margin-bottom:0}
 footer ul a{display:block;padding:11px 0}
 .grid{gap:20px}
 .trust-row{gap:16px;margin-top:26px}
 .quote-band{padding:56px 0}
 .quote-band .phone-big{font-size:1.9rem}
 footer{padding-bottom:90px}
 .price-table,.price-table tbody,.price-table tr,.price-table td{display:block;width:100%}
 .price-table thead{display:none}
 .price-table tr{border-bottom:1px solid #E5EBDC;padding:14px 0}
 .price-table td{border:none;padding:3px 16px}
}
"""


# Content hash so a CSS change always busts the browser cache.
# Without this a stale stylesheet can render new markup broken for up to a day.
CSS_V = hashlib.md5(CSS.encode("utf-8")).hexdigest()[:8]


JS = """<script>
(function(){
 var h=document.querySelector('header');
 if(h){addEventListener('scroll',function(){h.classList.toggle('shrunk',scrollY>60)},{passive:true})}
 if(!matchMedia('(prefers-reduced-motion: no-preference)').matches)return;
 var els=document.querySelectorAll('.reveal');
 if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('in')});return}
 var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}})},{threshold:.15});
 els.forEach(function(e){io.observe(e)});
})();
</script>"""

MOBILE_BAR = """<div class="mobile-bar">
<a class="call" href="tel:%s">Call Now</a>
<a class="quote" href="/contact.html">Free Quote</a>
</div>""" % PHONE_TEL

NAV = """<div class="topbar"><div class="wrap"><span>Free quotes for Akron &amp; Canton area homeowners</span><a href="tel:%s">Call or text %s</a></div></div>
<header><div class="wrap nav">
<input type="checkbox" id="navt" class="nav-toggle" aria-label="Open navigation menu">
<label for="navt" class="burger" aria-hidden="true"><i></i></label>
<a class="logo" href="/" aria-label="Samscaped home">
<!-- TODO: swap for Sam's original vector logo file when he provides it -->
<svg class="logo-svg" viewBox="0 0 268 66" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Samscaped">
<rect x="6" y="30" width="40" height="15" rx="3" fill="#2C5E1A"/>
<path d="M44 32 L57 12 h9" fill="none" stroke="#2C5E1A" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="16" cy="49" r="8" fill="#16300C"/><circle cx="16" cy="49" r="3" fill="#F2F5EC"/>
<circle cx="41" cy="50" r="6" fill="#16300C"/><circle cx="41" cy="50" r="2.2" fill="#F2F5EC"/>
<path d="M2 60 q5 -9 10 0 q5 -9 10 0 q5 -9 10 0 q5 -9 10 0 q5 -9 10 0" fill="none" stroke="#5E9C3F" stroke-width="3.5" stroke-linecap="round"/>
<text x="76" y="36" font-family="'Barlow Condensed',sans-serif" font-weight="800" font-size="32" letter-spacing="1.6" fill="#2C5E1A">SAMSCAPED</text>
<text x="78" y="55" font-family="Barlow,sans-serif" font-weight="600" font-size="13" letter-spacing="3.4" fill="#5C6355">330-578-5085</text>
</svg></a>
<nav><ul>
<li><a href="/services.html">Services</a></li>
<li><a href="/service-areas.html">Service Areas</a></li>
<li><a href="/gallery.html">Gallery</a></li>
<li><a href="/pricing.html">Pricing</a></li>
<li><a href="/about.html">About</a></li>
<li><a href="/contact.html" class="btn">Get a Free Quote</a></li>
</ul></nav>
</div></header>
<div class="stripe-bar"></div>""" % (PHONE_TEL, PHONE)

GSTRIP = """<div class="gstrip"><div class="wrap">
<a href="%s" target="_blank" rel="noopener" aria-label="See Samscaped reviews on Google">
<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path fill="#4285F4" d="M23 12.3c0-.8-.1-1.6-.2-2.3H12v4.5h6.2a5.3 5.3 0 0 1-2.3 3.5v2.9h3.7c2.2-2 3.4-5 3.4-8.6z"/><path fill="#34A853" d="M12 24c3.1 0 5.7-1 7.6-2.8l-3.7-2.9c-1 .7-2.3 1.1-3.9 1.1-3 0-5.5-2-6.4-4.7H1.8v3C3.7 21.5 7.6 24 12 24z"/><path fill="#FBBC05" d="M5.6 14.7a7.2 7.2 0 0 1 0-4.6v-3H1.8a12 12 0 0 0 0 10.6z"/><path fill="#EA4335" d="M12 4.8c1.7 0 3.2.6 4.4 1.7l3.3-3.3C17.7 1.2 15.1 0 12 0 7.6 0 3.7 2.5 1.8 6.2l3.8 3a7.1 7.1 0 0 1 6.4-4.4z"/></svg>
<span class="stars"><svg viewBox="0 0 20 20"><path d="M10 1l2.6 5.6 6 .7-4.4 4.1 1.2 5.9L10 14.4 4.6 17.3l1.2-5.9L1.4 7.3l6-.7z"/></svg><svg viewBox="0 0 20 20"><path d="M10 1l2.6 5.6 6 .7-4.4 4.1 1.2 5.9L10 14.4 4.6 17.3l1.2-5.9L1.4 7.3l6-.7z"/></svg><svg viewBox="0 0 20 20"><path d="M10 1l2.6 5.6 6 .7-4.4 4.1 1.2 5.9L10 14.4 4.6 17.3l1.2-5.9L1.4 7.3l6-.7z"/></svg><svg viewBox="0 0 20 20"><path d="M10 1l2.6 5.6 6 .7-4.4 4.1 1.2 5.9L10 14.4 4.6 17.3l1.2-5.9L1.4 7.3l6-.7z"/></svg><svg viewBox="0 0 20 20"><path d="M10 1l2.6 5.6 6 .7-4.4 4.1 1.2 5.9L10 14.4 4.6 17.3l1.2-5.9L1.4 7.3l6-.7z"/></svg></span>
<span>5.0 on Google &middot; 8 reviews &middot; Akron &amp; Canton homeowners</span></a>
</div></div>""" % GBP

QUOTE_BAND = """<div class="quote-band"><div class="wrap">
<h2>Get Your Free Quote</h2>
<p>No pressure, no obligation. Tell us about your property and we'll get you a straight answer fast.</p>
<a class="phone-big" href="tel:%s">%s</a><br>
<a class="btn" href="/contact.html">Request a Free Quote Online</a>
</div></div>""" % (PHONE_TEL, PHONE)

FOOTER = """<footer><div class="wrap">
<div class="foot-grid">
<div><h3>Samscaped</h3>
<p>Lawn care and landscaping for homeowners across the Akron and Canton area. Free quotes on every job.</p>
<p><strong>Phone:</strong> <a href="tel:%s">%s</a><br>
<strong>Email:</strong> <a href="mailto:%s">%s</a><br>
<a href="%s" rel="noopener" target="_blank">Find us on Google</a></p></div>
<div><h3>Services</h3><ul>
<li><a href="/lawn-mowing.html">Lawn Mowing</a></li>
<li><a href="/landscaping.html">Landscaping</a></li>
<li><a href="/mulch-installation.html">Mulch Installation</a></li>
<li><a href="/spring-fall-cleanup.html">Spring &amp; Fall Cleanup</a></li>
<li><a href="/hedge-trimming.html">Bush &amp; Hedge Trimming</a></li>
<li><a href="/leaf-removal.html">Leaf Removal</a></li>
</ul></div>
<div><h3>Service Areas</h3><ul>
<li><a href="/lawn-care-akron.html">Akron, OH</a></li>
<li><a href="/lawn-care-canton.html">Canton, OH</a></li>
<li><a href="/lawn-care-north-canton.html">North Canton, OH</a></li>
<li><a href="/lawn-care-green.html">Green, OH</a></li>
<li>Also serving Uniontown, Jackson Township &amp; Massillon</li>
<li><!-- TODO: confirm hours with Sam -->Mon&ndash;Sat, seasonal hours</li>
</ul></div>
<div><h3>Company</h3><ul>
<li><a href="/about.html">About Samscaped</a></li>
<li><a href="/gallery.html">Before &amp; After</a></li>
<li><a href="/pricing.html">Pricing</a></li>
<li><a href="/contact.html">Free Quote</a></li>
</ul></div>
</div>
<div class="foot-bottom"><span>&copy; 2026 Samscaped. All rights reserved.</span><span>Serving the Akron / Canton, Ohio area</span></div>
</div></footer>""" % (PHONE_TEL, PHONE, EMAIL, EMAIL, GBP)

# GHL form embed placeholder. Swap YOUR_FORM_ID for the Samscaped form ID from GHL.
# Leads POST as JSON to a GoHighLevel Inbound Webhook.
# TODO: In GHL (Samscaped sub-account) create Automation > Workflow > Trigger "Inbound Webhook",
# copy the webhook URL, and paste it below. Until then the form shows the call-instead fallback.
FORM_WEBHOOK = "YOUR_GHL_WEBHOOK_URL"

GHL_FORM = """<div class="form-shell">
<form class="qform" id="quoteForm" novalidate>
<div class="qf-msg" id="qfMsg" role="status" aria-live="polite"></div>
<div class="qf-row">
<div class="qf-field"><label for="qf-name">Name <span class="req">*</span></label>
<input id="qf-name" name="name" type="text" autocomplete="name" required></div>
<div class="qf-field"><label for="qf-phone">Phone <span class="req">*</span></label>
<input id="qf-phone" name="phone" type="tel" autocomplete="tel" required></div>
</div>
<div class="qf-row">
<div class="qf-field"><label for="qf-email">Email</label>
<input id="qf-email" name="email" type="email" autocomplete="email"></div>
<div class="qf-field"><label for="qf-address">Property Address <span class="req">*</span></label>
<input id="qf-address" name="address" type="text" autocomplete="street-address" placeholder="Street, City" required></div>
</div>
<div class="qf-field"><label>What do you need?</label>
<div class="qf-checks">
<label class="qf-check"><input type="checkbox" name="service" value="Lawn Mowing">Lawn Mowing</label>
<label class="qf-check"><input type="checkbox" name="service" value="Landscaping">Landscaping</label>
<label class="qf-check"><input type="checkbox" name="service" value="Mulch">Mulch</label>
<label class="qf-check"><input type="checkbox" name="service" value="Cleanup">Spring/Fall Cleanup</label>
<label class="qf-check"><input type="checkbox" name="service" value="Trimming">Bush &amp; Hedge Trimming</label>
<label class="qf-check"><input type="checkbox" name="service" value="Leaf Removal">Leaf Removal</label>
</div></div>
<div class="qf-field"><label for="qf-timing">How soon?</label>
<select id="qf-timing" name="timing">
<option value="As soon as possible">As soon as possible</option>
<option value="Within a couple weeks">Within a couple weeks</option>
<option value="Just getting prices">Just getting prices</option>
</select></div>
<div class="qf-field"><label for="qf-notes">Anything we should know?</label>
<textarea id="qf-notes" name="notes" placeholder="Gates, slopes, dogs, HOA rules, or what you're hoping to get done"></textarea></div>
<div class="qf-hp"><label>Leave blank<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
<button type="submit" class="btn" id="qfBtn">Get My Free Quote</button>
<p class="qf-note">No obligation. We usually reply the same day. Prefer to talk? Call or text <a href="tel:%s">%s</a>.</p>
</form>
</div>
<script>
(function(){
 var f=document.getElementById('quoteForm');if(!f)return;
 var msg=document.getElementById('qfMsg'),btn=document.getElementById('qfBtn'),hook='%s';
 f.addEventListener('change',function(e){var w=e.target.closest('.qf-check');if(w)w.classList.toggle('on',e.target.checked)});
 function show(t,cls){msg.textContent=t;msg.className='qf-msg '+cls;msg.scrollIntoView({block:'nearest'})}
 f.addEventListener('submit',function(e){
  e.preventDefault();
  if(f.website.value)return;
  var d={};new FormData(f).forEach(function(v,k){d[k]=d[k]?d[k]+', '+v:v});
  if(!d.name||!d.phone||!d.address){show('Please add your name, phone, and property address so we can quote it.','err');return}
  d.source='Samscaped website';d.page=location.pathname;
  if(hook.indexOf('http')!==0){show('Thanks! The online form is not live yet. Please call or text (330) 578-5085 and we will get you a quote today.','err');return}
  btn.disabled=true;btn.textContent='Sending...';
  fetch(hook,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)})
   .then(function(r){if(!r.ok)throw 0;f.reset();
    Array.prototype.forEach.call(f.querySelectorAll('.qf-check.on'),function(w){w.classList.remove('on')});
    show('Got it. We will get back to you shortly, usually the same day.','ok')})
   .catch(function(){show('Something went wrong sending that. Please call or text (330) 578-5085 and we will take care of you.','err')})
   .then(function(){btn.disabled=false;btn.textContent='Get My Free Quote'});
 });
})();
</script>""" % (PHONE_TEL, PHONE, FORM_WEBHOOK)

def schema_block(page_name, page_url, extra_service=None):
    services = ["Lawn Mowing","Landscaping","Mulch Installation","Spring and Fall Cleanup","Bush and Hedge Trimming","Leaf Removal"]
    s = """<script type="application/ld+json">
{
 "@context":"https://schema.org",
 "@type":"LocalBusiness",
 "name":"Samscaped",
 "description":"Lawn care and landscaping company serving the Akron and Canton, Ohio area. Free quotes.",
 "url":"%s",
 "telephone":"%s",
 "email":"%s",
 "image":"%s/assets/samscaped-logo.png",
 "priceRange":"$$",
 "areaServed":[{"@type":"City","name":"Akron"},{"@type":"City","name":"Canton"},{"@type":"City","name":"North Canton"},{"@type":"City","name":"Green"},{"@type":"City","name":"Uniontown"},{"@type":"City","name":"Jackson Township"},{"@type":"City","name":"Massillon"}],
 "address":{"@type":"PostalAddress","addressRegion":"OH","addressCountry":"US"},
 "sameAs":["%s"],
 "hasOfferCatalog":{"@type":"OfferCatalog","name":"Lawn Care Services","itemListElement":[%s]}
}
</script>""" % (DOMAIN, PHONE_TEL, EMAIL, DOMAIN, GBP,
    ",".join(['{"@type":"Offer","itemOffered":{"@type":"Service","name":"%s"}}' % x for x in services]))
    return s

def page(filename, title, meta_desc, h1_block, body, breadcrumb=None):
    canonical = DOMAIN + "/" + (filename if filename != "index.html" else "")
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<!-- BUILD: v7-form -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">
<link rel="icon" href="/assets/samscaped-logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Barlow:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css?v=__CSSV__">
%s
</head>
<body>
%s
%s
%s
%s
%s
%s
%s
</body>
</html>""" % (title, meta_desc, canonical, schema_block(filename, canonical), NAV, h1_block, body, QUOTE_BAND, FOOTER, MOBILE_BAR, JS)
    html = html.replace("__CSSV__", CSS_V)
    with open(os.path.join(OUT, filename), "w") as f:
        f.write(html)

def hero(eyebrow, h1, sub):
    return """<div class="hero">
<!-- TODO: drop a real photo of Sam's work at /assets/hero.jpg (striped lawn, phone shot is fine). Deep-green gradient shows until then. -->
<div class="hero-media"></div><div class="hero-scrim"></div>
<div class="wrap">
<div class="eyebrow">%s</div>
<h1>%s</h1>
<p>%s</p>
<div class="cta-row"><a class="btn" href="/contact.html">Get a Free Quote</a><a class="btn btn-outline" href="tel:%s">Call %s</a></div>
<div class="trust-row">
<span><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M8 14.5 3.5 10l1.4-1.4L8 11.7l7.1-7.1L16.5 6z"/></svg>Free quotes, no obligation</span>
<span><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1 2 5v6c0 4.4 3.4 7.6 8 8 4.6-.4 8-3.6 8-8V5z"/></svg>Locally owned in Akron/Canton</span>
<!-- TODO: confirm licensed &amp; insured wording with Sam before launch -->
<span><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1 2 5v6c0 4.4 3.4 7.6 8 8 4.6-.4 8-3.6 8-8V5z"/></svg>Licensed &amp; insured</span>
</div>
</div></div>""" % (eyebrow, h1, sub, PHONE_TEL, PHONE)

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "styles.css"), "w") as f:
    f.write(CSS)

# ---------------- REVIEWS ----------------
# Verbatim excerpts from the Samscaped Google Business Profile (5.0, 8 reviews).
# Only edit these by copying text directly from the GBP. Never write a testimonial.
# City is shown only where the reviewer stated it themselves.
_STAR = '<svg viewBox="0 0 20 20"><path d="M10 1l2.6 5.6 6 .7-4.4 4.1 1.2 5.9L10 14.4 4.6 17.3l1.2-5.9L1.4 7.3l6-.7z"/></svg>'
STARS5 = '<span class="stars">' + _STAR * 5 + '</span>'

REVIEWS = [
 ("Samuel completely transformed our yard. He removed a large amount of overgrown weeds, cleaned and reshaped all of our landscape beds, and installed fresh mulch that made everything look brand new. The quality of work exceeded our expectations.",
  "Brooke E. &middot; Plain Township"),
 ("Sam was great! He was very responsive and professional. I think the before and after pictures speak for themselves regarding the quality of his work!",
  "Layla A. &middot; North Canton"),
 ("Great service! Sam always shows up on time, does a thorough job mowing the lawn, and leaves the yard looking neat and well-maintained. Reliable, professional, and easy to work with. Highly recommend!",
  "Melissa C. &middot; Google review"),
 ("Attention to detail, great pricing and great communication!",
  "Anthony D. &middot; Google review"),
]

REVIEW_CARDS = "\n".join(
 '<div class="quote-card">%s<p>"%s"</p><cite>%s</cite></div>' % (STARS5, q, c)
 for q, c in REVIEWS)


# Real Samscaped job photos. Pairings are my read of the shots, Christian to confirm.
BA_ITEMS = [
    ("bed-refresh", "Bed Refresh", "Overgrown side bed cleaned out, edged, and mulched."),
    ("front-shrubs", "Shrub Trim &amp; Mulch", "Front shrubs cut back to shape, beds re-edged and mulched."),
    ("ranch-front", "Front Bed Rebuild", "New shrubs installed with a fresh curved edge and mulch."),
    ("curved-bed", "Bed Reshape", "Weedy border reshaped into a clean curve, fully mulched."),
    ("entry-beds", "Entry Cleanup", "Overgrown entry beds cleared, trimmed, and finished."),
    ("deck-surround", "Deck Surround", "Debris cleared and beds mulched around the deck perimeter."),
    ("under-deck", "Under-Deck Gravel", "Bare, washed-out ground leveled and finished with gravel."),
]


def ba_block(limit=None):
    items = BA_ITEMS if limit is None else BA_ITEMS[:limit]
    out = ['<div class="ba-grid">']
    for slug, title, cap in items:
        out.append(
            '<div class="ba-item"><div class="ba-pair">'
            '<div class="ba-shot before"><img src="/assets/ba-%s-before.jpg" alt="%s before Samscaped" loading="lazy" width="700" height="933"><span>Before</span></div>'
            '<div class="ba-shot after"><img src="/assets/ba-%s-after.jpg" alt="%s after Samscaped" loading="lazy" width="700" height="933"><span>After</span></div>'
            '</div><div class="ba-cap"><h3>%s</h3><p>%s</p></div></div>'
            % (slug, title, slug, title, title, cap))
    out.append('</div>')
    return "".join(out)

# ---------------- HOMEPAGE ----------------
home_body = """
<section class="reveal"><div class="wrap">
<h2>Lawn Care Services</h2>
<p class="lead">One crew, one point of contact, and a lawn that looks cut every single week. Every service comes with a free quote.</p>
<div class="grid grid-3">
<div class="card"><div class="card-img" style="background-image:url('/assets/svc-mowing.jpg')"></div><div class="card-body"><h3><a href="/lawn-mowing.html">Lawn Mowing</a></h3><p>Weekly and biweekly mowing with edging, trimming, and cleanup on every visit.</p><a class="more" href="/lawn-mowing.html">Mowing details &rarr;</a></div></div>
<div class="card"><!-- TODO: real job photo at /assets/svc-landscaping.jpg --><div class="card-img" style="background-image:url('/assets/svc-landscaping.jpg')"></div><div class="card-body"><h3><a href="/landscaping.html">Landscaping</a></h3><p>Bed design, plant installs, and refreshes that lift curb appeal without a designer price tag.</p><a class="more" href="/landscaping.html">Landscaping details &rarr;</a></div></div>
<div class="card"><!-- TODO: real job photo at /assets/svc-mulch.jpg --><div class="card-img" style="background-image:url('/assets/svc-mulch.jpg')"></div><div class="card-body"><h3><a href="/mulch-installation.html">Mulch Installation</a></h3><p>Bed edging, weed prep, and fresh mulch installed clean and even.</p><a class="more" href="/mulch-installation.html">Mulch details &rarr;</a></div></div>
<div class="card"><div class="card-img" style="background-image:url('/assets/svc-cleanup.jpg')"></div><div class="card-body"><h3><a href="/spring-fall-cleanup.html">Spring &amp; Fall Cleanup</a></h3><p>Full seasonal cleanups that get beds and turf ready for the season ahead.</p><a class="more" href="/spring-fall-cleanup.html">Cleanup details &rarr;</a></div></div>
<div class="card"><!-- TODO: real job photo at /assets/svc-trimming.jpg --><div class="card-img" style="background-image:url('/assets/svc-trimming.jpg')"></div><div class="card-body"><h3><a href="/hedge-trimming.html">Bush &amp; Hedge Trimming</a></h3><p>Shaping and trimming for shrubs, hedges, and ornamentals, debris hauled away.</p><a class="more" href="/hedge-trimming.html">Trimming details &rarr;</a></div></div>
<div class="card"><div class="card-img" style="background-image:url('/assets/svc-leaf.jpg')"></div><div class="card-body"><h3><a href="/leaf-removal.html">Leaf Removal</a></h3><p>Fall leaf cleanup and hauling so your lawn goes into winter healthy.</p><a class="more" href="/leaf-removal.html">Leaf removal details &rarr;</a></div></div>
</div>
</div></section>

<section class="tint reveal"><div class="wrap">
<h2>Why Homeowners Choose Samscaped</h2>
<div class="grid grid-3">
<div class="card card-plain"><div class="card-body"><h3>Free Quotes, Fast</h3><p>Call, text, or send the form. You get a real number, not a runaround.</p></div></div>
<div class="card card-plain"><div class="card-body"><h3>Owner on the Job</h3><p>Samscaped is owned and run by Sam Emich. The person quoting your lawn is the person accountable for it.</p></div></div>
<div class="card card-plain"><div class="card-body"><h3>Local to Akron &amp; Canton</h3><p>We live and work here. Same crew, same standards, week after week.</p></div></div>
</div>
</div></section>

<section class="reveal"><div class="wrap">
<h2>Where We Work</h2>
<p class="lead">Samscaped serves homeowners across the greater Akron and Canton area.</p>
<div class="chips">
<a href="/lawn-care-akron.html">Akron</a>
<a href="/lawn-care-canton.html">Canton</a>
<a href="/lawn-care-north-canton.html">North Canton</a>
<a href="/lawn-care-green.html">Green</a>
<span>Uniontown</span><span>Jackson Township</span><span>Massillon</span>
</div>
</div></section>

<section class="tint reveal"><div class="wrap">
<h2>Recent Work</h2>
<p class="lead">Real properties in the Akron and Canton area, before and after. No stock photos.</p>
""" + ba_block(4) + """
<p style="margin-top:28px"><a class="btn" href="/gallery.html">See More Before &amp; After</a></p>
</div></section>

<section class="reveal"><div class="wrap">
<h2>What Customers Say</h2>
<div class="grid grid-2 quotes">
%s
</div>
<p style="margin-top:16px"><a href="%s" target="_blank" rel="noopener">Read our reviews on Google &rarr;</a></p>
</div></section>

<section class="reveal"><div class="wrap">
<h2>Request Your Free Quote</h2>
<p class="lead">Tell us your address and what you need. Most quotes go out the same day.</p>
%s
</div></section>
""" % (REVIEW_CARDS, GBP, GHL_FORM)

page("index.html",
 "Lawn Care Akron & Canton, OH | Free Quotes | Samscaped",
 "Samscaped provides lawn mowing, landscaping, mulch, cleanups, and leaf removal for homeowners in the Akron and Canton, Ohio area. Free quotes. Call (330) 578-5085.",
 hero("Akron &amp; Canton, Ohio", "Lawn Care in Akron &amp; Canton, OH", "Mowing, landscaping, mulch, cleanups, and leaf removal from a local crew that shows up. Free quotes on every job.") + GSTRIP,
 home_body)

# ---------------- SERVICES HUB ----------------
services_body = """
<section class="reveal"><div class="wrap">
<p class="lead">Every Samscaped service starts with a free quote and ends with a property that looks taken care of. Pick a service below for what's included and how pricing works.</p>
<div class="grid grid-3">
<div class="card"><div class="card-img" style="background-image:url('/assets/svc-mowing.jpg')"></div><div class="card-body"><h3><a href="/lawn-mowing.html">Lawn Mowing</a></h3><p>Weekly and biweekly cuts with edging and trimming included.</p><a class="more" href="/lawn-mowing.html">Learn more &rarr;</a></div></div>
<div class="card"><!-- TODO: real job photo at /assets/svc-landscaping.jpg --><div class="card-img" style="background-image:url('/assets/svc-landscaping.jpg')"></div><div class="card-body"><h3><a href="/landscaping.html">Landscaping</a></h3><p>Bed work, plantings, and refreshes for real curb appeal.</p><a class="more" href="/landscaping.html">Learn more &rarr;</a></div></div>
<div class="card"><!-- TODO: real job photo at /assets/svc-mulch.jpg --><div class="card-img" style="background-image:url('/assets/svc-mulch.jpg')"></div><div class="card-body"><h3><a href="/mulch-installation.html">Mulch Installation</a></h3><p>Prep, edge, and install. Clean lines, even depth.</p><a class="more" href="/mulch-installation.html">Learn more &rarr;</a></div></div>
<div class="card"><div class="card-img" style="background-image:url('/assets/svc-cleanup.jpg')"></div><div class="card-body"><h3><a href="/spring-fall-cleanup.html">Spring &amp; Fall Cleanup</a></h3><p>Seasonal resets for beds and turf.</p><a class="more" href="/spring-fall-cleanup.html">Learn more &rarr;</a></div></div>
<div class="card"><!-- TODO: real job photo at /assets/svc-trimming.jpg --><div class="card-img" style="background-image:url('/assets/svc-trimming.jpg')"></div><div class="card-body"><h3><a href="/hedge-trimming.html">Bush &amp; Hedge Trimming</a></h3><p>Shaping, trimming, and haul-away.</p><a class="more" href="/hedge-trimming.html">Learn more &rarr;</a></div></div>
<div class="card"><div class="card-img" style="background-image:url('/assets/svc-leaf.jpg')"></div><div class="card-body"><h3><a href="/leaf-removal.html">Leaf Removal</a></h3><p>Fall cleanup and hauling before winter sets in.</p><a class="more" href="/leaf-removal.html">Learn more &rarr;</a></div></div>
</div>
<p style="margin-top:24px">Not sure what your property needs? <a href="/contact.html">Send us the address</a> and we'll tell you straight, including what you don't need.</p>
</div></section>
"""
page("services.html",
 "Lawn Care Services in Akron & Canton, OH | Samscaped",
 "Full list of Samscaped lawn care services for the Akron and Canton area: mowing, landscaping, mulch, seasonal cleanups, hedge trimming, and leaf removal.",
 hero("Our Services", "Lawn Care Services", "Everything your lawn needs in one place, from weekly mowing to full seasonal cleanups."),
 services_body)

# ---------------- SERVICE PAGES ----------------
def service_page(fn, kw, title, desc, eyebrow, h1, sub, intro, includes, faqs, related):
    faq_html = "".join(["<details><summary>%s</summary><p>%s</p></details>" % (q, a) for q, a in faqs])
    rel_html = " &middot; ".join(['<a href="/%s">%s</a>' % (u, t) for u, t in related])
    body = """
<section class="reveal"><div class="wrap">
%s
<h2>What's Included</h2>
<ul class="checks">%s</ul>
</div></section>
<section class="tint reveal"><div class="wrap">
<h2>%s Questions</h2>
%s
</div></section>
<section class="reveal"><div class="wrap">
<h2>Serving the Akron &amp; Canton Area</h2>
<p>Samscaped provides %s throughout <a href="/lawn-care-akron.html">Akron</a>, <a href="/lawn-care-canton.html">Canton</a>, <a href="/lawn-care-north-canton.html">North Canton</a>, <a href="/lawn-care-green.html">Green</a>, and nearby communities including Uniontown, Jackson Township, and Massillon.</p>
<p><strong>Related services:</strong> %s</p>
</div></section>
""" % (intro, "".join(["<li>%s</li>" % i for i in includes]), kw, faq_html, kw.lower(), rel_html)
    page(fn, title, desc, hero(eyebrow, h1, sub), body)

service_page("lawn-mowing.html", "Lawn Mowing",
 "Lawn Mowing Akron & Canton, OH | Weekly Mowing Service | Samscaped",
 "Weekly and biweekly lawn mowing in Akron, Canton, and nearby Ohio communities. Edging and trimming included on every cut. Free quotes from Samscaped.",
 "Mowing Service", "Lawn Mowing in Akron &amp; Canton, OH",
 "Weekly and biweekly mowing with edging, trimming, and blow-off included on every visit.",
 """<p>A good mowing service is boring in the best way: the crew shows up on the same day, cuts at the right height for the season, and leaves the property cleaner than they found it. That's the whole Samscaped mowing pitch. No skipped weeks, no scalped turf, no clippings all over your driveway.</p>
<p>Northeast Ohio grass grows fast from April through June, slows in the summer heat, then surges again in fall. We adjust cut height and frequency to match instead of running the same routine all season, which is how lawns stay green instead of getting stressed and thin.</p>""",
 ["Weekly or biweekly mowing on a consistent schedule",
  "String trimming around beds, trees, fences, and hard edges",
  "Crisp edging along driveways and walkways",
  "Blowing off clippings from drives, walks, and patios",
  "Seasonal cut-height adjustments for healthier turf"],
 [("How much does lawn mowing cost?", "Most standard city lots in the Akron and Canton area fall in a predictable range depending on lot size and trimming complexity. See our <a href='/pricing.html'>pricing page</a> for typical ranges, or send your address for an exact free quote."),
  ("Weekly or biweekly, which should I pick?", "Weekly is right for most lawns from April through June when growth is heavy. Biweekly can work in mid-summer. We'll recommend a schedule based on your lawn, and you're never locked in."),
  ("Do I need to be home?", "No. As long as the crew can access the lawn and gates are unlocked, you don't need to be there. You'll know we came because the lines will tell you.")],
 [("spring-fall-cleanup.html", "Spring &amp; Fall Cleanup"), ("hedge-trimming.html", "Hedge Trimming"), ("leaf-removal.html", "Leaf Removal")])

service_page("landscaping.html", "Landscaping",
 "Landscaping Akron & Canton, OH | Bed Design & Plant Installation | Samscaped",
 "Landscaping services in the Akron and Canton area: bed design, plant installation, bed refreshes, and curb appeal projects. Free quotes from Samscaped.",
 "Landscaping", "Landscaping in Akron &amp; Canton, OH",
 "Bed design, plant installs, and full refreshes that make the front of your house the best one on the street.",
 """<p>Most landscaping around Akron and Canton doesn't need a landscape architect. It needs overgrown beds cleaned out, tired shrubs replaced with plants that actually survive Ohio winters, and clean edges that make everything look intentional. That's the work Samscaped does every week.</p>
<p>We plan around zone 6 plants that handle our freeze-thaw cycles and clay-heavy soil, so what we install in May still looks good in two years, not just two weeks.</p>""",
 ["Bed cleanouts, reshaping, and fresh edging",
  "Shrub and perennial selection and installation",
  "Removal and replacement of overgrown or dead plantings",
  "Decorative stone and mulch finishing",
  "Small-project focus: fast quotes, fast turnaround"],
 [("Do you do full landscape design?", "We handle design for typical residential front and back beds. If you want a plan for the whole property, we'll walk it with you and quote it in phases so you can spread out the cost."),
  ("What does landscaping cost?", "It depends on plant count, bed size, and removals. Every project gets a free itemized quote so you can see exactly where the money goes."),
  ("When is the best time to plant in Northeast Ohio?", "Spring and early fall are ideal. Fall planting is underrated here: roots establish before winter and plants take off in spring.")],
 [("mulch-installation.html", "Mulch Installation"), ("hedge-trimming.html", "Hedge Trimming"), ("spring-fall-cleanup.html", "Seasonal Cleanup")])

service_page("mulch-installation.html", "Mulch Installation",
 "Mulch Installation Akron & Canton, OH | Delivery & Install | Samscaped",
 "Professional mulch installation in Akron, Canton, and surrounding Ohio areas. Bed prep, edging, weed control, and clean installation. Free quotes.",
 "Mulch", "Mulch Installation in Akron &amp; Canton, OH",
 "Prep, edge, and install. Fresh mulch laid clean and even, with the bed work done right first.",
 """<p>Mulch is the cheapest upgrade a property can get, but only if the prep happens first. Dumping fresh mulch on weedy, unedged beds looks good for about two weeks. Samscaped does it in the right order: clean out the beds, cut a fresh edge, deal with the weeds, then install mulch at a proper depth.</p>
<p>We install hardwood, dyed brown, and black mulch depending on the look you want, and we'll tell you honestly how many yards your beds actually need so you're not paying for material that ends up piled around your trees.</p>""",
 ["Bed cleanout and weed removal before installation",
  "Fresh spade or machine edge on every bed",
  "Pre-emergent weed treatment available",
  "Hardwood, dyed brown, or black mulch options",
  "Installed at proper 2-3 inch depth, kept off trunks and siding"],
 [("How much mulch do I need?", "A yard of mulch covers roughly 100 square feet at 3 inches deep. Send us photos or an address and we'll calculate it for you as part of the free quote."),
  ("What does mulch installation cost?", "Pricing is per yard installed and includes prep and edging. See <a href='/pricing.html'>our pricing page</a> for typical ranges."),
  ("Should I mulch every year?", "Most beds in Northeast Ohio need a refresh every spring. Color fades and depth compresses over a season, especially after our winters.")],
 [("landscaping.html", "Landscaping"), ("spring-fall-cleanup.html", "Spring Cleanup"), ("lawn-mowing.html", "Lawn Mowing")])

service_page("spring-fall-cleanup.html", "Spring & Fall Cleanup",
 "Spring & Fall Cleanup Akron & Canton, OH | Yard Cleanup Service | Samscaped",
 "Seasonal yard cleanups in the Akron and Canton area. Spring bed prep and fall cleanups that protect your lawn through Ohio winters. Free quotes.",
 "Seasonal Cleanups", "Spring &amp; Fall Cleanup in Akron &amp; Canton, OH",
 "A full seasonal reset for your beds and turf, done in one visit instead of five of your weekends.",
 """<p>Ohio hands every homeowner two big cleanup jobs a year. Spring means matted leaves, winter debris, dead growth, and beds that need to be cut back and re-edged before anything can grow. Fall means leaves, perennial cutbacks, and getting turf clean before snow sits on it for three months.</p>
<p>A Samscaped cleanup is one scheduled visit that resets the whole property, so the mowing season starts clean and winter doesn't smother your lawn.</p>""",
 ["Leaf and debris removal from turf and beds",
  "Perennial and ornamental grass cutbacks",
  "Bed edging and reshaping",
  "First or final mow of the season",
  "Haul-away of all debris"],
 [("When should I schedule a spring cleanup?", "March through early May in Northeast Ohio, ideally before the first mow. Spots fill fast once the weather turns, so book early."),
  ("Is fall cleanup really necessary?", "Yes. Leaves left under snow smother turf and invite snow mold. A clean lawn going into winter is the single best thing you can do for how it looks in April."),
  ("What does a cleanup cost?", "It depends on property size and how much debris there is. Every cleanup gets a free quote, and bundling cleanup with a mowing plan usually saves money.")],
 [("leaf-removal.html", "Leaf Removal"), ("mulch-installation.html", "Mulch Installation"), ("lawn-mowing.html", "Lawn Mowing")])

service_page("hedge-trimming.html", "Bush & Hedge Trimming",
 "Bush & Hedge Trimming Akron & Canton, OH | Shrub Shaping | Samscaped",
 "Bush and hedge trimming in Akron, Canton, and nearby Ohio communities. Clean shaping, healthy cuts, full debris haul-away. Free quotes from Samscaped.",
 "Trimming &amp; Shaping", "Bush &amp; Hedge Trimming in Akron &amp; Canton, OH",
 "Sharp, healthy shaping for shrubs, hedges, and ornamentals, with every clipping hauled away.",
 """<p>Overgrown shrubs age a house faster than almost anything else. The fix is quick when it's done by someone who knows where to cut: trimming at the right time of year, shaping so plants stay full instead of going woody, and cleaning up every clipping.</p>
<p>We trim boxwoods, yews, arborvitae, burning bush, and the rest of the usual Northeast Ohio lineup, and we'll flag anything that's beyond trimming and should just be replaced.</p>""",
 ["Shaping and trimming for shrubs, hedges, and ornamentals",
  "Timing-aware cuts so flowering shrubs still bloom",
  "Height reduction for overgrown plantings",
  "Removal recommendations when a plant is past saving",
  "Complete debris cleanup and haul-away"],
 [("How often should hedges be trimmed?", "Most shrubs in our area need one or two trims per season. Fast growers like arborvitae and privet may need more to hold a clean shape."),
  ("When is the wrong time to trim?", "Spring-flowering shrubs like lilac and forsythia should be trimmed right after they bloom, not before. Trim at the wrong time and you lose a year of flowers."),
  ("Do you haul away the branches?", "Always. Cleanup and haul-away are included in every trimming quote.")],
 [("landscaping.html", "Landscaping"), ("spring-fall-cleanup.html", "Seasonal Cleanup"), ("lawn-mowing.html", "Lawn Mowing")])

service_page("leaf-removal.html", "Leaf Removal",
 "Leaf Removal Akron & Canton, OH | Fall Leaf Cleanup | Samscaped",
 "Fall leaf removal in the Akron and Canton area. Full cleanup and haul-away so your lawn goes into winter healthy. Free quotes from Samscaped.",
 "Leaf Removal", "Leaf Removal in Akron &amp; Canton, OH",
 "Complete fall leaf cleanup and haul-away, before the snow buries the job until April.",
 """<p>Akron and Canton neighborhoods are full of mature maples and oaks, which is great in July and a burial in October. Leaves left on turf through winter smother grass, breed snow mold, and turn spring cleanup into a much bigger bill.</p>
<p>Samscaped runs leaf cleanups from October through early December. One or two scheduled visits and your lawn goes into winter clean.</p>""",
 ["Full leaf removal from turf, beds, and hard surfaces",
  "Single-visit or multi-visit plans depending on your trees",
  "Curb-line cleanup where city pickup applies",
  "Haul-away included",
  "Combine with fall cleanup for the full seasonal reset"],
 [("One big cleanup or multiple visits?", "If you have heavy tree cover, two visits (mid-fall and after final drop) keeps the lawn healthier and usually costs about the same as one massive cleanup."),
  ("What does leaf removal cost?", "It scales with lot size and tree cover. Send your address for a free quote, and check <a href='/pricing.html'>pricing</a> for typical ranges."),
  ("Can you mulch the leaves instead?", "On lighter cover, mulching leaves into the turf is healthy and cheaper. We'll recommend it when it makes sense for your lawn.")],
 [("spring-fall-cleanup.html", "Fall Cleanup"), ("lawn-mowing.html", "Lawn Mowing"), ("hedge-trimming.html", "Hedge Trimming")])

# ---------------- SERVICE AREAS HUB ----------------
areas_body = """
<section class="reveal"><div class="wrap">
<p class="lead">Samscaped is a local, owner-run crew serving homeowners across the greater Akron and Canton area. Pick your city for details, or just call. If you're close, we'll come.</p>
<div class="grid grid-2">
<div class="card"><!-- TODO: real job photo at /assets/city-akron.jpg --><div class="card-img" style="background-image:url('/assets/city-akron.jpg')"></div><div class="card-body"><h3><a href="/lawn-care-akron.html">Lawn Care in Akron, OH</a></h3><p>From Highland Square to Ellet, mowing and full-service lawn care across Akron's neighborhoods.</p><a class="more" href="/lawn-care-akron.html">Akron details &rarr;</a></div></div>
<div class="card"><!-- TODO: real job photo at /assets/city-canton.jpg --><div class="card-img" style="background-image:url('/assets/city-canton.jpg')"></div><div class="card-body"><h3><a href="/lawn-care-canton.html">Lawn Care in Canton, OH</a></h3><p>Serving Canton homeowners from Ridgewood to Avondale and out into Plain Township.</p><a class="more" href="/lawn-care-canton.html">Canton details &rarr;</a></div></div>
<div class="card"><!-- TODO: real job photo at /assets/city-north-canton.jpg --><div class="card-img" style="background-image:url('/assets/city-north-canton.jpg')"></div><div class="card-body"><h3><a href="/lawn-care-north-canton.html">Lawn Care in North Canton, OH</a></h3><p>Weekly mowing and landscaping for North Canton's tidy, tree-lined streets.</p><a class="more" href="/lawn-care-north-canton.html">North Canton details &rarr;</a></div></div>
<div class="card"><!-- TODO: real job photo at /assets/city-green.jpg --><div class="card-img" style="background-image:url('/assets/city-green.jpg')"></div><div class="card-body"><h3><a href="/lawn-care-green.html">Lawn Care in Green, OH</a></h3><p>Larger lots and newer developments across Green, kept sharp all season.</p><a class="more" href="/lawn-care-green.html">Green details &rarr;</a></div></div>
</div>
<p style="margin-top:24px">We also serve <strong>Uniontown, Jackson Township, and Massillon</strong>. Outside these areas? <a href="/contact.html">Ask anyway.</a></p>
</div></section>
"""
page("service-areas.html",
 "Service Areas | Lawn Care in the Akron & Canton, OH Area | Samscaped",
 "Samscaped provides lawn care throughout the Akron and Canton, Ohio area including North Canton, Green, Uniontown, Jackson Township, and Massillon.",
 hero("Where We Work", "Our Service Areas", "Local lawn care for the greater Akron and Canton area."),
 areas_body)

# ---------------- CITY PAGES ----------------
def city_page(fn, city, title, desc, sub, paras, hoods, faq):
    faq_html = "".join(["<details><summary>%s</summary><p>%s</p></details>" % (q, a) for q, a in faq])
    body = """
<section class="reveal"><div class="wrap">
%s
<h2>Neighborhoods We Serve in %s</h2>
<p>%s</p>
</div></section>
<section class="tint reveal"><div class="wrap">
<h2>Lawn Care Services in %s</h2>
<div class="grid grid-3">
<div class="card"><div class="card-img" style="background-image:url('/assets/svc-mowing.jpg')"></div><div class="card-body"><h3><a href="/lawn-mowing.html">Lawn Mowing</a></h3><p>Weekly and biweekly cuts, edging included.</p></div></div>
<div class="card"><!-- TODO: real job photo at /assets/svc-landscaping.jpg --><div class="card-img" style="background-image:url('/assets/svc-landscaping.jpg')"></div><div class="card-body"><h3><a href="/landscaping.html">Landscaping &amp; Mulch</a></h3><p>Bed work, plantings, and <a href="/mulch-installation.html">mulch installation</a>.</p></div></div>
<div class="card"><div class="card-img" style="background-image:url('/assets/svc-cleanup.jpg')"></div><div class="card-body"><h3><a href="/spring-fall-cleanup.html">Cleanups &amp; Leaf Removal</a></h3><p>Seasonal cleanups and <a href="/leaf-removal.html">fall leaf removal</a>.</p></div></div>
</div>
</div></section>
<section class="reveal"><div class="wrap">
<h2>%s Lawn Care Questions</h2>
%s
</div></section>
""" % ("".join("<p>%s</p>" % p for p in paras), city, hoods, city, city, faq_html)
    page(fn, title, desc, hero("Serving " + city, "Lawn Care in " + city + ", OH", sub), body)

city_page("lawn-care-akron.html", "Akron",
 "Lawn Care Akron, OH | Mowing & Landscaping | Samscaped",
 "Lawn mowing, landscaping, and yard cleanups for Akron, Ohio homeowners. Local crew, free quotes. Call Samscaped at (330) 578-5085.",
 "Mowing, landscaping, and cleanups for Akron homeowners, from a crew that actually works your neighborhood.",
 ["Akron lawns come with Akron problems: mature tree canopy that dumps serious leaf volume every fall, clay-heavy soil that compacts hard, and older neighborhoods where tight lot lines mean trimming matters as much as mowing. Samscaped works these streets every week and quotes them accurately the first time.",
  "Whether it's a compact lot near Highland Square or a bigger yard out toward Ellet, you get the same deal: a consistent weekly schedule, edging and trimming on every cut, and a free quote before any work starts."],
 "We serve homeowners across Akron including Highland Square, Wallhaven, Firestone Park, Goodyear Heights, Ellet, Kenmore, and the Merriman Valley, plus surrounding communities.",
 [("Do you service my part of Akron?", "Almost certainly. We cover Akron city neighborhoods and the immediate suburbs. Send your address through the quote form and we'll confirm same day."),
  ("How fast can you start?", "During the season we can usually add new weekly customers within a week of the quote."),
  ("Do you handle leaf season in Akron?", "Yes, and Akron's tree cover makes fall our busiest stretch here. See our <a href='/leaf-removal.html'>leaf removal service</a> and book early.")])

city_page("lawn-care-canton.html", "Canton",
 "Lawn Care Canton, OH | Mowing & Landscaping | Samscaped",
 "Lawn mowing, landscaping, and seasonal cleanups for Canton, Ohio homeowners. Free quotes from a local crew. Call Samscaped at (330) 578-5085.",
 "Weekly mowing, bed work, and seasonal cleanups for Canton homeowners. Free quotes, straight answers.",
 ["Canton is home turf for Samscaped. From established streets in Ridgewood and Market Heights to newer builds on the Plain Township side, we keep Canton lawns cut, edged, and cleaned up on a schedule you can set your watch to.",
  "Canton properties range from compact city lots to bigger suburban yards, and pricing should reflect that instead of a one-size-fits-all number. Send us your address and we'll quote your actual property, free."],
 "We serve homeowners throughout Canton including Ridgewood, Avondale, Market Heights, the Hall of Fame Village area, and out into Plain Township and Meyers Lake.",
 [("Are you actually local to Canton?", "Yes. Samscaped is based right here in the Akron/Canton area and owned by Sam Emich. When you call the number on this page, that's who answers for the work."),
  ("What's the most popular service in Canton?", "Weekly mowing with spring and fall cleanups added on. It keeps the property handled all season for one predictable cost."),
  ("Do you offer free quotes in Canton?", "Every job, every time. Call <a href='tel:+13305785085'>(330) 578-5085</a> or use the form.")])

city_page("lawn-care-north-canton.html", "North Canton",
 "Lawn Care North Canton, OH | Mowing & Landscaping | Samscaped",
 "Lawn mowing, landscaping, mulch, and cleanups for North Canton, Ohio homeowners. Local, owner-run crew. Free quotes: (330) 578-5085.",
 "Sharp, consistent lawn care for North Canton's tree-lined streets. Free quotes on every job.",
 ["North Canton homeowners keep their properties tight, and the standard on most streets is high. That's a good fit for how Samscaped works: consistent weekly cuts, real edging, and beds that stay clean instead of slowly going wild between big cleanups.",
  "We handle everything from weekly mowing near the Hoover District to full bed refreshes and mulch installs in the neighborhoods around Dogwood Park and Walsh University."],
 "We serve homeowners across North Canton including the Hoover District area, neighborhoods around Dogwood Park, Walsh University, and Washington Square, plus adjacent Jackson Township and Plain Township streets.",
 [("Do you do mulch and bed work in North Canton?", "Yes, spring mulch installs are one of our biggest services here. See <a href='/mulch-installation.html'>mulch installation</a> for what's included."),
  ("Can I bundle mowing with cleanups?", "That's the setup most North Canton customers choose: weekly mowing plus spring and fall cleanups, quoted together."),
  ("How do quotes work?", "Send your address. We size the lot, factor the trimming, and send a number, usually the same day. Free, no obligation.")])

city_page("lawn-care-green.html", "Green",
 "Lawn Care Green, OH | Mowing & Landscaping | Samscaped",
 "Lawn mowing, landscaping, and cleanups for Green, Ohio homeowners. Larger lots welcome. Free quotes from Samscaped: (330) 578-5085.",
 "Bigger lots, newer neighborhoods, same standard. Lawn care built for Green properties.",
 ["Green sits right between Akron and Canton, which makes it dead center in Samscaped's service area. Lots here run larger than the city neighborhoods, and plenty of Green developments have HOA standards to keep up with. We quote by the actual property, so a half-acre in Green gets a half-acre price and a half-acre level of attention.",
  "From established neighborhoods near Boettler Park to the newer builds off Massillon Road, we keep Green lawns cut, edged, and cleaned up all season."],
 "We serve homeowners throughout Green including neighborhoods around Boettler Park, Raintree, the Massillon Road corridor, and nearby Uniontown and Lake Township streets.",
 [("Do you handle larger properties in Green?", "Yes. Bigger lots are common here and we're set up for them. The quote reflects actual lot size, not a flat guess."),
  ("My HOA has standards. Can you keep up with them?", "That's the job. Consistent scheduling and clean edging are exactly what HOA streets need. We can work to your HOA's requirements."),
  ("Do you serve Uniontown too?", "Yes, Uniontown and Lake Township are inside our regular routes.")])

# ---------------- PRICING ----------------
# TODO: All prices below are typical NE Ohio market ranges. Confirm real numbers with Sam before launch.
pricing_body = """
<section class="reveal"><div class="wrap">
<p class="lead">Most lawn care companies make you call just to find out you can't afford them, or that you were overpaying. Here's how Samscaped pricing actually works, with real ranges. Your exact quote is always free.</p>
<!-- TODO: confirm all ranges with Sam before launch. These are typical Akron/Canton market ranges. -->
<div class="callout"><p>Every quote is free. These ranges just mean no surprises.</p></div>
<h2>Typical Pricing Ranges</h2>
<table class="price-table">
<tr><th>Service</th><th>Typical Range</th><th>What Drives the Price</th></tr>
<tr><td>Weekly Lawn Mowing (standard city lot)</td><td>$45 - $65 per cut</td><td>Lot size, trimming complexity, gates and slopes</td></tr>
<tr><td>Weekly Lawn Mowing (up to 1/2 acre)</td><td>$65 - $100 per cut</td><td>Turf area, obstacles, edging footage</td></tr>
<tr><td>Mulch Installation</td><td>$75 - $95 per yard installed</td><td>Yards needed, bed prep, edging, weed treatment</td></tr>
<tr><td>Spring or Fall Cleanup</td><td>$150 - $400</td><td>Debris volume, bed count, property size</td></tr>
<tr><td>Bush &amp; Hedge Trimming</td><td>$75 - $250</td><td>Number and size of shrubs, haul-away volume</td></tr>
<tr><td>Leaf Removal</td><td>$150 - $450</td><td>Tree cover, lot size, single vs multi-visit</td></tr>
</table>
<p><em>Ranges cover most residential properties in the Akron/Canton area. Unusual properties get unusual quotes, still free.</em></p>
</div></section>
<section class="tint reveal"><div class="wrap">
<h2>How Quotes Work</h2>
<ul class="checks">
<li>Send your address by phone, text, or the form below</li>
<li>We size the property and factor real conditions: trimming, slopes, gates, debris</li>
<li>You get a clear number, usually the same day</li>
<li>No contracts required. If we're not doing a good job, fire us.</li>
</ul>
<h2>Pricing Questions</h2>
<details><summary>Why do prices vary between neighbors?</summary><p>Two lawns on the same street can take very different time. Fence lines, play sets, slopes, and edging footage all change the work, so they change the price.</p></details>
<details><summary>Is there a discount for bundling services?</summary><p>Yes. Weekly mowing customers get preferred pricing on cleanups, mulch, and trimming because we're already on the property.</p></details>
<details><summary>Do you require a season-long contract?</summary><p>No. We keep customers by doing good work, not by locking them in.</p></details>
</div></section>
<section class="reveal"><div class="wrap">
<h2>Get Your Exact Price</h2>
%s
</div></section>
""" % GHL_FORM
page("pricing.html",
 "Lawn Care Pricing Akron & Canton, OH | Mowing Cost | Samscaped",
 "How much does lawn care cost in Akron and Canton? Real pricing ranges for mowing, mulch, cleanups, and leaf removal from Samscaped. Free exact quotes.",
 hero("Straight Answers", "Lawn Care Pricing in Akron &amp; Canton", "Real ranges up front, exact quotes free. No mystery pricing."),
 pricing_body)

# ---------------- ABOUT ----------------
about_body = """
<section class="reveal"><div class="wrap">
<div class="grid grid-2">
<div>
<h2>Owned and Run by Sam Emich</h2>
<p>Samscaped is a local lawn care company serving the Akron and Canton area, owned and operated by Sam Emich. No call centers, no franchise playbook. The person who quotes your property is the person responsible for how it looks.</p>
<p>The business is built on a simple idea: show up when you say you will, do the work like it's your own yard, and quote honestly enough that customers stop shopping around.</p>
<p><img src="/assets/about-crew.jpg" alt="Samscaped crew working on a property in the Akron area" loading="lazy" width="900" height="675" style="border-radius:var(--r);box-shadow:var(--shadow)"></p>
<!-- TODO: add Sam's story (how he started, years in business, crew size) and a portrait of Sam -->
<p><a class="btn" href="/contact.html">Get a Free Quote</a></p>
</div>
<div>
<h3>What You Can Expect</h3>
<ul class="checks">
<li>Free quotes on every job, usually same day</li>
<li>Consistent scheduling, same crew each visit</li>
<li>Straight answers, including "you don't need that"</li>
<li>Local ownership, Akron/Canton based</li>
<li>Every job cleaned up before we leave</li>
</ul>
</div>
</div>
</div></section>
<section class="tint reveal"><div class="wrap">
<h2>Find Samscaped on Google</h2>
<p>See our reviews, photos, and updates on our <a href="%s" target="_blank" rel="noopener">Google Business Profile</a>. If we've done work for you, a review there means more to a small local business than you'd guess.</p>
</div></section>
""" % GBP
page("about.html",
 "About Samscaped | Local Lawn Care, Akron & Canton, OH",
 "Samscaped is a locally owned lawn care company run by Sam Emich, serving homeowners across the Akron and Canton, Ohio area with free quotes on every job.",
 hero("About Us", "About Samscaped", "A local, owner-run lawn care company built on showing up."),
 about_body)

# ---------------- CONTACT ----------------
contact_body = """
<section class="reveal"><div class="wrap">
<div class="grid grid-2">
<div>
<h2>Request a Free Quote</h2>
<p>Fill out the form and we'll get back to you fast, usually the same day. Or skip the form entirely and call or text.</p>
<p><strong>Phone:</strong> <a href="tel:%s">%s</a><br>
<strong>Email:</strong> <a href="mailto:%s">%s</a><br>
<strong>Service Area:</strong> Akron, Canton, North Canton, Green, Uniontown, Jackson Township, Massillon</p>
<p><a href="%s" target="_blank" rel="noopener">Find us on Google Maps</a></p>
<h3>What to Include</h3>
<ul class="checks">
<li>Your address (so we can size the property)</li>
<li>What you need: mowing, mulch, cleanup, trimming</li>
<li>Any details: gates, slopes, dogs, HOA requirements</li>
</ul>
</div>
<div>
%s
</div>
</div>
</div></section>
""" % (PHONE_TEL, PHONE, EMAIL, EMAIL, GBP, GHL_FORM)
page("contact.html",
 "Free Lawn Care Quote | Contact Samscaped | Akron & Canton, OH",
 "Get a free lawn care quote from Samscaped. Call or text (330) 578-5085 or send the form. Serving the Akron and Canton, Ohio area.",
 hero("Free Quotes", "Get a Free Quote", "Call, text, or send the form. Most quotes go out the same day."),
 contact_body)

# ---------------- GALLERY ----------------
gallery_body = """
<section class="reveal"><div class="wrap">
<p class="lead">Every photo below is a real Samscaped job in the Akron and Canton area. Same crew, same standard, whether it is a bed refresh or a full front rebuild.</p>
""" + ba_block() + """
<div class="ba-grid" style="margin-top:28px">
<div class="ba-item ba-single"><div class="ba-pair">
<div class="ba-shot after"><img src="/assets/ba-brick-front-after.jpg" alt="Finished mulch bed with landscape lighting by Samscaped" loading="lazy" width="700" height="933"><span>Finished</span></div>
</div><div class="ba-cap"><h3>Mulch &amp; Lighting</h3><p>Black mulch, new plantings, and path lighting along a full front walk.</p></div></div>
</div>
</div></section>

<section class="tint reveal"><div class="wrap">
<h2>What Customers Say</h2>
<div class="grid grid-2 quotes">
""" + REVIEW_CARDS + """
</div>
<p style="margin-top:16px"><a href="%s" target="_blank" rel="noopener">Read our reviews on Google &rarr;</a></p>
</div></section>
""" % GBP

page("gallery.html",
 "Before & After Gallery | Lawn Care Akron & Canton, OH | Samscaped",
 "See real before and after photos of Samscaped lawn care and landscaping jobs across the Akron and Canton, Ohio area. Free quotes on every project.",
 hero("Our Work", "Before &amp; After Gallery", "Real properties, real results. Every photo below is an actual Samscaped job."),
 gallery_body)

# ---------------- SITEMAP + ROBOTS ----------------
pages = ["", "services.html", "lawn-mowing.html", "landscaping.html", "mulch-installation.html",
 "spring-fall-cleanup.html", "hedge-trimming.html", "leaf-removal.html", "service-areas.html",
 "lawn-care-akron.html", "lawn-care-canton.html", "lawn-care-north-canton.html", "lawn-care-green.html",
 "gallery.html", "pricing.html", "about.html", "contact.html"]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for p in pages:
    sm += "  <url><loc>%s/%s</loc></url>\n" % (DOMAIN, p)
sm += "</urlset>\n"
with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    f.write(sm)
with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % DOMAIN)

print("Built %d pages" % len([x for x in os.listdir(OUT) if x.endswith('.html')]))

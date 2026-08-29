# Gmail Signature

## APPROVED DESIGN — SOURCE OF TRUTH

This file is the authoritative specification for Alexander Ferrari Miller's approved Gmail signature.

**DO NOT redesign, reinterpret, restyle, or regenerate this signature.**

For outgoing Gmail drafts, use normal Gmail rich/HTML-capable formatting with the plain-text alternative below unless Alexander explicitly instructs otherwise.

The approved signature has exactly three cells:

1. Upper left: Alexander's actual optimized Professional-page headshot.
2. Upper right: identity and contact information.
3. Lower full width: social links, arranged 5 entries on the first row and 5 on the second row for mobile Gmail.

The upper section is frozen except for explicitly approved changes. The upper-right contact block uses very tiny 9×9 px monochrome icons for address, phone, and both email lines. Do not change its sizing, typography, line breaks, or spacing unless Alexander explicitly requests a change.

The portrait must be Alexander's actual optimized Professional-page headshot:

`https://AlexanderFerrariMiller.com/images/Alexander-Ferrari-Miller-web.png`

The address must remain on exactly these two lines:

`3549 North D Street`  
`San Bernardino, CA 92405-2103`

`(Legacy)` must appear immediately before the legacy email address and must not be italicized.

For WhatsApp, the displayed phone number is plain text and must not be intentionally turned into a telephone link. The wa.me URL is the clickable WhatsApp link.

All visible social URLs must retain their full leading `https://`. Preserve the approved display line breaks below so long identifiers remain within their columns on mobile Gmail. The long identifier lines use 6.5px text where specified. TikTok remains lowercase. YouTube uses the verified capitalization shown below. LinkedIn, Snapchat, and X use the verified capitalization shown below.

Pearlsom is approved and is social/contact entry #1. Its visible layout is exactly five lines: `Pearlsom`, `(Beta)`, `https://`, `pearlsom.com/`, `Alexander.Ferrari.Miller`.

## Approved Gmail HTML implementation

```html
<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%;max-width:600px;font-family:Arial,Helvetica,sans-serif;color:#10244a;border-collapse:collapse;table-layout:fixed;">
  <tr>
    <td width="90" valign="top" style="width:90px;padding:8px 12px 14px 0;text-align:center;">
      <img src="https://AlexanderFerrariMiller.com/images/Alexander-Ferrari-Miller-web.png" alt="Alexander Ferrari Miller" width="76" style="display:block;width:76px;height:auto;border:0;margin:0 auto;">
    </td>
    <td valign="top" style="border-left:2px solid #10244a;padding:0 0 14px 14px;">
      <div style="font-size:20px;font-weight:700;line-height:1.15;white-space:nowrap;margin:0 0 6px 0;">Alexander Ferrari Miller</div>
      <div style="font-size:11px;font-weight:700;line-height:1.35;margin:0 0 10px 0;">Professional of Many Hats • Scientist • Artist • Author • Problem Solver</div>
      <div style="font-size:11px;line-height:1.5;">
        <img src="https://AlexanderFerrariMiller.com/images/signature-icons/address.svg" alt="Address" width="9" height="9" style="display:inline-block;width:9px;height:9px;border:0;vertical-align:-1px;margin-right:4px;">3549 North D Street<br>
        <span style="display:inline-block;width:13px;"></span>San Bernardino, CA 92405-2103<br>
        <img src="https://AlexanderFerrariMiller.com/images/signature-icons/phone.svg" alt="Phone" width="9" height="9" style="display:inline-block;width:9px;height:9px;border:0;vertical-align:-1px;margin-right:4px;">+1 (323) 681-7588<br>
        <a href="https://AlexanderFerrariMiller.com" style="color:#10244a;text-decoration:none;">AlexanderFerrariMiller.com</a><br>
        <img src="https://AlexanderFerrariMiller.com/images/signature-icons/email.svg" alt="Email" width="9" height="9" style="display:inline-block;width:9px;height:9px;border:0;vertical-align:-1px;margin-right:4px;"><a href="mailto:Alexander.Ferrari.Miller@gmail.com" style="color:#10244a;text-decoration:none;">Alexander.Ferrari.Miller@gmail.com</a><br>
        <img src="https://AlexanderFerrariMiller.com/images/signature-icons/email.svg" alt="Email" width="9" height="9" style="display:inline-block;width:9px;height:9px;border:0;vertical-align:-1px;margin-right:4px;"><span style="font-style:normal;">(Legacy)</span> <a href="mailto:alex.miller.boston@gmail.com" style="color:#10244a;text-decoration:none;font-style:normal;">alex.miller.boston@gmail.com</a>
      </div>
    </td>
  </tr>
  <tr>
    <td colspan="2" style="border-top:2px solid #10244a;padding-top:10px;">
      <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%;font-family:Arial,Helvetica,sans-serif;color:#10244a;font-size:7px;text-align:center;border-collapse:collapse;table-layout:fixed;">
        <tr>
          <td width="20%" valign="top" style="padding:4px 1px;"><b style="font-size:8px;">Pearlsom</b><br><b style="font-size:7px;">(Beta)</b><br><a href="https://pearlsom.com/Alexander.Ferrari.Miller" style="color:#10244a;text-decoration:none;"><span style="white-space:nowrap;">https://</span><br><span style="white-space:nowrap;">pearlsom.com/</span><br><span style="white-space:nowrap;font-size:6.5px;">Alexander.Ferrari.Miller</span></a></td>
          <td width="20%" valign="top" style="padding:4px 1px;"><b style="font-size:8px;">Facebook</b><br><a href="https://www.facebook.com/Alexander.Ferrari.Miller" style="color:#10244a;text-decoration:none;"><span style="white-space:nowrap;">https://www.</span><br><span style="white-space:nowrap;">facebook.com/</span><br><span style="white-space:nowrap;font-size:6.5px;">Alexander.Ferrari.Miller</span></a></td>
          <td width="20%" valign="top" style="padding:4px 1px;"><b style="font-size:8px;">Instagram</b><br><a href="https://www.instagram.com/Alexander.Ferrari.Miller/" style="color:#10244a;text-decoration:none;"><span style="white-space:nowrap;">https://www.</span><br><span style="white-space:nowrap;">instagram.com/</span><br><span style="white-space:nowrap;font-size:6.5px;">Alexander.Ferrari.Miller/</span></a></td>
          <td width="20%" valign="top" style="padding:4px 1px;"><b style="font-size:8px;">TikTok</b><br><a href="https://www.tiktok.com/@alexander.ferrari.miller" style="color:#10244a;text-decoration:none;"><span style="white-space:nowrap;">https://www.</span><br><span style="white-space:nowrap;">tiktok.com/</span><br><span style="white-space:nowrap;font-size:6.5px;">@alexander.ferrari.miller</span></a></td>
          <td width="20%" valign="top" style="padding:4px 1px;"><b style="font-size:8px;">YouTube</b><br><a href="https://www.youtube.com/@Alexander.Ferrari.Miller" style="color:#10244a;text-decoration:none;"><span style="white-space:nowrap;">https://www.</span><br><span style="white-space:nowrap;">youtube.com/</span><br><span style="white-space:nowrap;font-size:6.5px;">@Alexander.Ferrari.Miller</span></a></td>
        </tr>
      </table>
      <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%;font-family:Arial,Helvetica,sans-serif;color:#10244a;font-size:7px;text-align:center;border-collapse:collapse;table-layout:fixed;">
        <tr>
          <td width="20%" valign="top" style="padding:9px 1px 4px 1px;"><b style="font-size:8px;">LinkedIn</b><br><a href="https://www.linkedin.com/in/Alexander-Ferrari-Miller/" style="color:#10244a;text-decoration:none;"><span style="white-space:nowrap;">https://www.</span><br><span style="white-space:nowrap;">linkedin.com/in/</span><br><span style="white-space:nowrap;font-size:6.5px;">Alexander-Ferrari-Miller/</span></a></td>
          <td width="20%" valign="top" style="padding:9px 1px 4px 1px;"><b style="font-size:8px;">Snapchat</b><br><a href="https://www.snapchat.com/add/AFMSanBern" style="color:#10244a;text-decoration:none;"><span style="white-space:nowrap;">https://www.</span><br><span style="white-space:nowrap;">snapchat.com/add/</span><br><span style="white-space:nowrap;">AFMSanBern</span></a></td>
          <td width="20%" valign="top" style="padding:9px 1px 4px 1px;"><b style="font-size:8px;">X</b><br><span style="white-space:nowrap;">@AFMSanBern</span><br><a href="https://x.com/AFMSanBern" style="color:#10244a;text-decoration:none;"><span style="white-space:nowrap;">https://x.com/</span><br><span style="white-space:nowrap;">AFMSanBern</span></a></td>
          <td width="20%" valign="top" style="padding:9px 1px 4px 1px;"><b style="font-size:8px;">WhatsApp</b><br><span style="white-space:nowrap;">+1 (323) 681-7588</span><br><a href="https://wa.me/13236817588" style="color:#10244a;text-decoration:none;"><span style="white-space:nowrap;">https://wa.me/</span><br><span style="white-space:nowrap;">13236817588</span></a></td>
          <td width="20%" valign="top" style="padding:9px 1px 4px 1px;"><b style="font-size:8px;">Zello</b><br><span style="white-space:nowrap;">SantaAlex63</span><br><a href="https://zello.com/" style="color:#10244a;text-decoration:none;white-space:nowrap;">https://zello.com/</a></td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

## Plain-text alternative

```text
Regards,

Alexander Ferrari Miller
Professional of Many Hats • Scientist • Artist • Author • Problem Solver
3549 North D Street
San Bernardino, CA 92405-2103
+1 (323) 681-7588
https://AlexanderFerrariMiller.com
Alexander.Ferrari.Miller@gmail.com
(Legacy) alex.miller.boston@gmail.com

Pearlsom (Beta): https://pearlsom.com/Alexander.Ferrari.Miller
Facebook: https://www.facebook.com/Alexander.Ferrari.Miller
Instagram: https://www.instagram.com/Alexander.Ferrari.Miller/
TikTok: https://www.tiktok.com/@alexander.ferrari.miller
YouTube: https://www.youtube.com/@Alexander.Ferrari.Miller
LinkedIn: https://www.linkedin.com/in/Alexander-Ferrari-Miller/
Snapchat: https://www.snapchat.com/add/AFMSanBern
X: @AFMSanBern
X: https://x.com/AFMSanBern
WhatsApp: +1 (323) 681-7588
WhatsApp: https://wa.me/13236817588
Zello: SantaAlex63
Zello: https://zello.com/
```

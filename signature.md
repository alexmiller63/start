# Gmail Signature

## APPROVED DESIGN — SOURCE OF TRUTH

This file is the authoritative specification for Alexander Ferrari Miller's approved Gmail signature.

**DO NOT redesign, reinterpret, restyle, or regenerate this signature.**

For outgoing Gmail drafts, use normal Gmail rich/HTML-capable formatting with the plain-text alternative below unless Alexander explicitly instructs otherwise.

The approved signature has exactly three cells:

1. Upper left: Alexander's actual optimized Professional-page headshot.
2. Upper right: identity and contact information.
3. Lower full width: social links, arranged 5 entries on the first row and 4 on the second row for mobile Gmail.

The upper section is frozen. Do not change its sizing, typography, line breaks, or spacing unless Alexander explicitly requests a change.

The portrait must be Alexander's actual optimized Professional-page headshot:

`https://AlexanderFerrariMiller.com/images/Alexander-Ferrari-Miller-web.png`

The address must remain on exactly these two lines:

`3549 North D Street`  
`San Bernardino, CA 92405-2103`

`(Legacy)` must appear immediately before the legacy email address and must not be italicized.

For WhatsApp, the displayed phone number is plain text and must not be intentionally turned into a telephone link. The wa.me URL is the clickable WhatsApp link.

All visible social URLs must retain their full leading `https://`. Long identifiers such as `alexander.ferrari.miller` and `alexander-ferrari-miller` must not be broken inside a word; line breaks should occur before the identifier instead.

Pearlsom is not yet included. Do not add `pearlsom.com` until Alexander explicitly says it is ready.

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
        3549 North D Street<br>
        San Bernardino, CA 92405-2103<br>
        +1 (323) 681-7588<br>
        <a href="https://AlexanderFerrariMiller.com" style="color:#10244a;text-decoration:none;">AlexanderFerrariMiller.com</a><br>
        <a href="mailto:Alexander.Ferrari.Miller@gmail.com" style="color:#10244a;text-decoration:none;">Alexander.Ferrari.Miller@gmail.com</a><br>
        <span style="font-style:normal;">(Legacy)</span> <a href="mailto:alex.miller.boston@gmail.com" style="color:#10244a;text-decoration:none;font-style:normal;">alex.miller.boston@gmail.com</a>
      </div>
    </td>
  </tr>
  <tr>
    <td colspan="2" style="border-top:2px solid #10244a;padding-top:10px;">
      <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%;font-family:Arial,Helvetica,sans-serif;color:#10244a;font-size:7px;text-align:center;border-collapse:collapse;table-layout:fixed;">
        <tr>
          <td width="20%" valign="top" style="padding:4px 1px;"><b style="font-size:8px;">Facebook</b><br><a href="https://www.facebook.com/alexander.ferrari.miller" style="color:#10244a;text-decoration:none;"><span style="white-space:nowrap;">https://www.facebook.com/</span><br><span style="white-space:nowrap;">alexander.ferrari.miller</span></a></td>
          <td width="20%" valign="top" style="padding:4px 1px;"><b style="font-size:8px;">Instagram</b><br><a href="https://www.instagram.com/alexander.ferrari.miller/" style="color:#10244a;text-decoration:none;"><span style="white-space:nowrap;">https://www.instagram.com/</span><br><span style="white-space:nowrap;">alexander.ferrari.miller/</span></a></td>
          <td width="20%" valign="top" style="padding:4px 1px;"><b style="font-size:8px;">TikTok</b><br><a href="https://www.tiktok.com/@alexander.ferrari.miller" style="color:#10244a;text-decoration:none;"><span style="white-space:nowrap;">https://www.tiktok.com/</span><br><span style="white-space:nowrap;">@alexander.ferrari.miller</span></a></td>
          <td width="20%" valign="top" style="padding:4px 1px;"><b style="font-size:8px;">YouTube</b><br><a href="https://www.youtube.com/@alexander-ferrari-miller" style="color:#10244a;text-decoration:none;"><span style="white-space:nowrap;">https://www.youtube.com/</span><br><span style="white-space:nowrap;">@alexander-ferrari-miller</span></a></td>
          <td width="20%" valign="top" style="padding:4px 1px;"><b style="font-size:8px;">LinkedIn</b><br><a href="https://www.linkedin.com/in/alexander-ferrari-miller/" style="color:#10244a;text-decoration:none;"><span style="white-space:nowrap;">https://www.linkedin.com/in/</span><br><span style="white-space:nowrap;">alexander-ferrari-miller/</span></a></td>
        </tr>
      </table>
      <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%;font-family:Arial,Helvetica,sans-serif;color:#10244a;font-size:7px;text-align:center;border-collapse:collapse;table-layout:fixed;">
        <tr>
          <td width="25%" valign="top" style="padding:9px 1px 4px 1px;"><b style="font-size:8px;">Snapchat</b><br><a href="https://www.snapchat.com/add/afmsanbern" style="color:#10244a;text-decoration:none;"><span style="white-space:nowrap;">https://www.snapchat.com/add/</span><br><span style="white-space:nowrap;">afmsanbern</span></a></td>
          <td width="25%" valign="top" style="padding:9px 1px 4px 1px;"><b style="font-size:8px;">X</b><br><span style="white-space:nowrap;">@AFMSanBern</span><br><a href="https://x.com/afmsanbern" style="color:#10244a;text-decoration:none;white-space:nowrap;">https://x.com/afmsanbern</a></td>
          <td width="25%" valign="top" style="padding:9px 1px 4px 1px;"><b style="font-size:8px;">WhatsApp</b><br><span style="white-space:nowrap;">+1 (323) 681-7588</span><br><a href="https://wa.me/13236817588" style="color:#10244a;text-decoration:none;white-space:nowrap;">https://wa.me/13236817588</a></td>
          <td width="25%" valign="top" style="padding:9px 1px 4px 1px;"><b style="font-size:8px;">Zello</b><br><span style="white-space:nowrap;">SantaAlex63</span><br><a href="https://zello.com/" style="color:#10244a;text-decoration:none;white-space:nowrap;">https://zello.com/</a></td>
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

Facebook: https://www.facebook.com/alexander.ferrari.miller
Instagram: https://www.instagram.com/alexander.ferrari.miller/
TikTok: https://www.tiktok.com/@alexander.ferrari.miller
YouTube: https://www.youtube.com/@alexander-ferrari-miller
LinkedIn: https://www.linkedin.com/in/alexander-ferrari-miller/
Snapchat: https://www.snapchat.com/add/afmsanbern
X: @AFMSanBern
X: https://x.com/afmsanbern
WhatsApp: +1 (323) 681-7588
WhatsApp: https://wa.me/13236817588
Zello: SantaAlex63
Zello: https://zello.com/
```

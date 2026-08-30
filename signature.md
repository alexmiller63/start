# Gmail Signature

## VALIDATED KNOWN-GOOD BASELINE — AK — August 29, 2026

This is the authoritative Gmail signature for Alexander Ferrari Miller.

AK is the current production baseline. It was validated in Gmail with all 15 intended links functioning, including the Google Maps address link. Do not reintroduce HTML from `signature.bad`.

## Required Gmail construction rules

1. Build the complete Gmail HTML body in one pass. Do not append this signature as an isolated HTML fragment.
2. Preserve the transition: ordinary message body → blank spacing → `Regards,` → blank spacing → `Alex Miller` → blank spacing → graphical signature table.
3. When creating Gmail drafts programmatically, provide explicit raw HTML as `html_body` and also provide a plain-text fallback in `body`.
4. The upper contact block uses `font-size:11px;line-height:16.5px;`. Do not replace the fixed `16.5px` line height with unitless `1.5`.
5. The 5-column social tables use `table-layout:fixed`, but the individual social `<td>` elements must NOT have `width="20%"` attributes.
6. Use explicit `font-size:11px` on upper contact anchors and `font-size:7px` on social anchors.
7. Preserve visible underlining with `text-decoration:underline` on all anchors.
8. Preserve the full 2-line postal address as one Google Maps hyperlink.
9. Treat any change to this HTML as experimental until it passes an isolation test in Gmail.

## Approved closing

```text
Regards,

Alex Miller
```

The graphical signature follows the closing.

## Validated graphical signature HTML — AK

```html
<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%;max-width:600px;font-family:Arial,Helvetica,sans-serif;color:#10244a;border-collapse:collapse;table-layout:fixed;">
  <tr>
    <td width="90" valign="top" style="width:90px;padding:8px 12px 14px 0;text-align:center;">
      <img src="https://AlexanderFerrariMiller.com/images/Alexander-Ferrari-Miller-web.png" alt="Alexander Ferrari Miller" width="76" style="display:block;width:76px;height:auto;border:0;margin:0 auto;">
    </td>
    <td valign="top" style="border-left:2px solid #10244a;padding:0 0 14px 14px;">
      <div style="font-size:20px;font-weight:700;line-height:1.15;white-space:nowrap;margin:0 0 6px 0;">Alexander Ferrari Miller</div>
      <div style="font-size:11px;font-weight:700;line-height:1.35;margin:0 0 10px 0;">Professional of Many Hats • Scientist • Artist • Author • Problem Solver</div>
      <div style="font-size:11px;line-height:16.5px;">
        <img src="https://raw.githubusercontent.com/alexmiller63/start/main/images/address-email.png" alt="Address" width="13" height="13" style="display:inline-block;width:13px;height:13px;border:0;vertical-align:-2px;margin-right:4px;"><a href="https://www.google.com/maps/search/?api=1&amp;query=3549+North+D+Street%2C+San+Bernardino%2C+CA+92405-2103" style="color:#10244a;text-decoration:underline;font-size:11px;">3549 North D Street<br><span style="display:inline-block;width:17px;"></span>San Bernardino, CA 92405-2103</a><br>
        <img src="https://raw.githubusercontent.com/alexmiller63/start/main/images/phone-email.png" alt="Phone" width="13" height="13" style="display:inline-block;width:13px;height:13px;border:0;vertical-align:-2px;margin-right:4px;"><a href="tel:+13236817588" style="color:#10244a;text-decoration:underline;font-size:11px;">+1 (323) 681-7588</a><br>
        <img src="https://raw.githubusercontent.com/alexmiller63/start/main/images/website-email.png" alt="Website" width="13" height="13" style="display:inline-block;width:13px;height:13px;border:0;vertical-align:-2px;margin-right:4px;"><a href="https://AlexanderFerrariMiller.com" style="color:#10244a;text-decoration:underline;font-size:11px;">AlexanderFerrariMiller.com</a><br>
        <img src="https://raw.githubusercontent.com/alexmiller63/start/main/images/email-email.png" alt="Email" width="13" height="13" style="display:inline-block;width:13px;height:13px;border:0;vertical-align:-2px;margin-right:4px;"><a href="mailto:Alexander.Ferrari.Miller@gmail.com" style="color:#10244a;text-decoration:underline;font-size:11px;">Alexander.Ferrari.Miller@gmail.com</a><br>
        <img src="https://raw.githubusercontent.com/alexmiller63/start/main/images/email-email.png" alt="Email" width="13" height="13" style="display:inline-block;width:13px;height:13px;border:0;vertical-align:-2px;margin-right:4px;"><span style="font-style:normal;">(Legacy)</span> <a href="mailto:alex.miller.boston@gmail.com" style="color:#10244a;text-decoration:underline;font-style:normal;font-size:11px;">alex.miller.boston@gmail.com</a>
      </div>
    </td>
  </tr>
  <tr>
    <td colspan="2" style="border-top:2px solid #10244a;padding-top:10px;">
      <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%;font-family:Arial,Helvetica,sans-serif;color:#10244a;font-size:7px;text-align:center;border-collapse:collapse;table-layout:fixed;">
        <tr>
          <td valign="top" style="padding:4px 1px;"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/alexmiller63/start/main/images/pearlsom-email.png" alt="Pearlsom" width="20" height="20" style="display:inline-block;width:20px;height:20px;border:0;vertical-align:middle;margin-right:3px;"><b style="font-size:8px;vertical-align:middle;">Pearlsom</b></span><br><b style="font-size:7px;">(Beta)</b><br><a href="https://pearlsom.com/Alexander.Ferrari.Miller" style="color:#10244a;text-decoration:underline;font-size:7px;"><span style="white-space:nowrap;">https://</span><br><span style="white-space:nowrap;">pearlsom.com/</span><br><span style="white-space:nowrap;font-size:6.5px;">Alexander.Ferrari.Miller</span></a></td>
          <td valign="top" style="padding:4px 1px;"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/alexmiller63/start/main/images/Facebook-email.png" alt="Facebook" width="20" height="20" style="display:inline-block;width:20px;height:20px;border:0;vertical-align:middle;margin-right:3px;"><b style="font-size:8px;vertical-align:middle;">Facebook</b></span><br><a href="https://www.facebook.com/Alexander.Ferrari.Miller" style="color:#10244a;text-decoration:underline;font-size:7px;"><span style="white-space:nowrap;">https://www.</span><br><span style="white-space:nowrap;">facebook.com/</span><br><span style="white-space:nowrap;font-size:6.5px;">Alexander.Ferrari.Miller</span></a></td>
          <td valign="top" style="padding:4px 1px;"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/alexmiller63/start/main/images/Instagram-email.png" alt="Instagram" width="20" height="20" style="display:inline-block;width:20px;height:20px;border:0;vertical-align:middle;margin-right:3px;"><b style="font-size:8px;vertical-align:middle;">Instagram</b></span><br><a href="https://www.instagram.com/Alexander.Ferrari.Miller/" style="color:#10244a;text-decoration:underline;font-size:7px;"><span style="white-space:nowrap;">https://www.</span><br><span style="white-space:nowrap;">instagram.com/</span><br><span style="white-space:nowrap;font-size:6.5px;">Alexander.Ferrari.Miller/</span></a></td>
          <td valign="top" style="padding:4px 1px;"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/alexmiller63/start/main/images/TikTok-email.png" alt="TikTok" width="20" height="20" style="display:inline-block;width:20px;height:20px;border:0;vertical-align:middle;margin-right:3px;"><b style="font-size:8px;vertical-align:middle;">TikTok</b></span><br><a href="https://www.tiktok.com/@alexander.ferrari.miller" style="color:#10244a;text-decoration:underline;font-size:7px;"><span style="white-space:nowrap;">https://www.</span><br><span style="white-space:nowrap;">tiktok.com/</span><br><span style="white-space:nowrap;font-size:6.5px;">@alexander.ferrari.miller</span></a></td>
          <td valign="top" style="padding:4px 1px;"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/alexmiller63/start/main/images/YouTube-email.png" alt="YouTube" width="20" height="20" style="display:inline-block;width:20px;height:20px;border:0;vertical-align:middle;margin-right:3px;"><b style="font-size:8px;vertical-align:middle;">YouTube</b></span><br><a href="https://www.youtube.com/@Alexander.Ferrari.Miller" style="color:#10244a;text-decoration:underline;font-size:7px;"><span style="white-space:nowrap;">https://www.</span><br><span style="white-space:nowrap;">youtube.com/</span><br><span style="white-space:nowrap;font-size:6.5px;">@Alexander.Ferrari.Miller</span></a></td>
        </tr>
      </table>
      <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%;font-family:Arial,Helvetica,sans-serif;color:#10244a;font-size:7px;text-align:center;border-collapse:collapse;table-layout:fixed;">
        <tr>
          <td valign="top" style="padding:9px 1px 4px 1px;"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/alexmiller63/start/main/images/LinkedIn-email.png" alt="LinkedIn" width="20" height="20" style="display:inline-block;width:20px;height:20px;border:0;vertical-align:middle;margin-right:3px;"><b style="font-size:8px;vertical-align:middle;">LinkedIn</b></span><br><a href="https://www.linkedin.com/in/Alexander-Ferrari-Miller/" style="color:#10244a;text-decoration:underline;font-size:7px;"><span style="white-space:nowrap;">https://www.</span><br><span style="white-space:nowrap;">linkedin.com/in/</span><br><span style="white-space:nowrap;font-size:6.5px;">Alexander-Ferrari-Miller/</span></a></td>
          <td valign="top" style="padding:9px 1px 4px 1px;"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/alexmiller63/start/main/images/Snapchat-email.png" alt="Snapchat" width="20" height="20" style="display:inline-block;width:20px;height:20px;border:0;vertical-align:middle;margin-right:3px;"><b style="font-size:8px;vertical-align:middle;">Snapchat</b></span><br><a href="https://www.snapchat.com/add/AFMSanBern" style="color:#10244a;text-decoration:underline;font-size:7px;"><span style="white-space:nowrap;">https://www.</span><br><span style="white-space:nowrap;">snapchat.com/add/</span><br><span style="white-space:nowrap;">AFMSanBern</span></a></td>
          <td valign="top" style="padding:9px 1px 4px 1px;"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/alexmiller63/start/main/images/X-email.png" alt="X" width="20" height="20" style="display:inline-block;width:20px;height:20px;border:0;vertical-align:middle;margin-right:3px;"><b style="font-size:8px;vertical-align:middle;">X</b></span><br><span style="white-space:nowrap;">@AFMSanBern</span><br><a href="https://x.com/AFMSanBern" style="color:#10244a;text-decoration:underline;font-size:7px;"><span style="white-space:nowrap;">https://x.com/</span><br><span style="white-space:nowrap;">AFMSanBern</span></a></td>
          <td valign="top" style="padding:9px 1px 4px 1px;"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/alexmiller63/start/main/images/WhatsApp-email.png" alt="WhatsApp" width="20" height="20" style="display:inline-block;width:20px;height:20px;border:0;vertical-align:middle;margin-right:3px;"><b style="font-size:8px;vertical-align:middle;">WhatsApp</b></span><br><span style="white-space:nowrap;">+1 (323) 681-7588</span><br><a href="https://wa.me/13236817588" style="color:#10244a;text-decoration:underline;font-size:7px;"><span style="white-space:nowrap;">https://wa.me/</span><br><span style="white-space:nowrap;">13236817588</span></a></td>
          <td valign="top" style="padding:9px 1px 4px 1px;"><span style="white-space:nowrap;"><img src="https://raw.githubusercontent.com/alexmiller63/start/main/images/Zello-email.png" alt="Zello" width="20" height="20" style="display:inline-block;width:20px;height:20px;border:0;vertical-align:middle;margin-right:3px;"><b style="font-size:8px;vertical-align:middle;">Zello</b></span><br><span style="white-space:nowrap;">SantaAlex63</span><br><a href="https://zello.com/" style="color:#10244a;text-decoration:underline;white-space:nowrap;font-size:7px;">https://zello.com/</a></td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

## Validation record

Validated in Gmail on August 29, 2026. AK passed with the complete approved graphical presentation and all 15 intended links functioning: postal address, phone, website, 2 email addresses, and 10 social/service links.

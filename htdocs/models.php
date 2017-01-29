<!DOCTYPE html>
<html>
<?php
include "bin/basics.php";
include "config.php";
$pif = GetPageInfo("models");
DoHead($pif);
DoPageHeader($pif);
?>


<table>
<tr>
<th class="chead lsm">Larger Scale Models</th>
<th class="chead ssm">Smaller Scale Models</th>
</tr>

<tr>
<td class="ccell early">
<a href="cgi-bin/sets.cgi?page=early"><img src="<?php echo $IMG_DIR_ART; ?>/early.gif" alt="Early Lesney Toys"></a>
</td>
<td class="ccell rw"><a href="/database.php#year"><img src="<?php echo $IMG_DIR_ART; ?>/mb60s.gif"><br>Regular Wheels<br>1947-1969</a></td>
</tr>

<tr>
<td class="ccell ks">
<a href="cgi-bin/sets.cgi?page=kings">
<img src="<?php echo $IMG_DIR_ART; ?>/kingsize.gif" alt="King Size">
<img src="<?php echo $IMG_DIR_ART; ?>/superkings-s.gif" alt="Super Kings"></a>
</td>
<td class="ccell sf"><a href="/database.php#year">
<img src="<?php echo $IMG_DIR_ART; ?>/75.gif"><br>1970-</a></td>
</tr>

<tr>
<td class="ccell yy"><a href="cgi-bin/sets.cgi?page=yy"><img src="<?php echo $IMG_DIR_ART; ?>/moy2.gif" alt="Models of Yesteryear"></a></td>
<td class="ccell series"><a href="cgi-bin/matrix.cgi"><font color="#FFFFFF">Some Special<br><img src="<?php echo $IMG_DIR_ART; ?>/matchbox.gif" alt="Matchbox"><br>Series</font></a></td>
</tr>

<tr>
<td class="ccell dinky"><a href="cgi-bin/sets.cgi?page=dinky"><img src="<?php echo $IMG_DIR_ART; ?>/dinky-s.gif" alt="Dinky Collection"></a></td>
<td class="ccell prem"><a href="cgi-bin/matrix.cgi?page=premiere"><img src="<?php echo $IMG_DIR_ART; ?>/premiere.gif" alt="Premiere Collection"></a></td>
</tr>

<tr>
<td class="ccell coll43"><a href="cgi-bin/sets.cgi?page=coll43"><img src="<?php echo $IMG_DIR_ART; ?>/collectibles.gif" alt="Matchbox Collectibles"></a></td>
<td class="ccell coll64"><a href="cgi-bin/matrix.cgi?page=coll64"><img src="<?php echo $IMG_DIR_ART; ?>/collectibles.gif" alt="Matchbox Collectibles"></a></td>
</tr>

<tr>
<td class="ccell coll72"><a href="cgi-bin/sets.cgi?page=coll72"><img src="<?php echo $IMG_DIR_ART; ?>/collectibles.gif" alt="Matchbox Collectibles"><img src="pic/gfx/coll72.gif"><br>Aircraft</a></td>
<td class="ccell skb"><a href="cgi-bin/sets.cgi?page=skb"><img src="<?php echo $IMG_DIR_ART; ?>/skybusters-s.gif" alt="Skybusters"></a></td>
</tr>

<tr><td colspan=2>&nbsp;</td></tr>

<tr>
<td class="back"><a href="."><div class="textbutton">BACK</div> to the main index.</a></td>
<td class="other"><a href="pages/other.php">Other Matchbox Products</a>
</td>
</tr>

</table>


<?php DoPageFooter($pif); ?>
</body>
</html>

import gmpy2
from gmpy2 import mpz


enc_flag =mpz('323632295564281159207345320711830086103981503695434315924393443973399482299874562360968500862876287023632748254787351738941585712095344019983198177945565400654536629637732351282380565009100902713082583050762147607191082109760553937383829348683296530066579753265359049223441756105519813532004174546850749474535173601525531811058478333730459603102537773934534248732658092236016740005418735628483060593269345442915008678976337794825475933783907794757274849704179731791440193240092427321596419559936323103598474657702547718767018417373486155768468558920105705913105404921856190362626614133596252692797930055841715044842426152656793340609614116561202186808166877866486025300349202528114311261727834707278761103514852806668213087488808660378212720213592356366132347504025812953413000154933003086840160732050264205691363629262503947972573616341201458165592288968871612869577653691394250516090042434155471744011357674967574011121907911034874898132303571238825929633695908091663809591335136145714537026370618316640898377497145769532280625123916256336778149273702315260333746322657868027143573221191572795621019888586794804135187158192688795016226227583932029882304019029365106352804332378688041015064696688776113409348786763786832765229764932')
leak=mpz(' 15075602855517923347863863253278930015846398339020081334646696099433836878577903768449203099026659986014876988658735897159372955691850765262254268661556151109792711387773616314876736240733233501818549739730195176402670816059701724651985834090122043152459714236832899621467504551940245324055255179406268873788462126744194376060119875354364722019997007737207134053455135021564444128027189338375042306699448907992408795507146124594012562949786562732202724074452260276665755779965909578813543668444085838148459974799498051693205119093517535541996621556081892284535363147039211933865212854032111239633582905388635109082373271673205707852769230474982450594435936996742688064239436936899903930905558770916249877319980392613598680340172746884222805017973143462897163656582275519641698207420243895126720527386507453335974504484008946288146412473244858045434501456906886761924412792053513907257466936953247332596445037657901927531829261761261813861562161126805801696985321819451752317963987140319643001132210396198138484896847249509624452946838731847360372384314988231964775344502905157228817050461414914564713339246727442839494442233898863855844203994901349366199365484379224652147923366882024096784267744775166831986565083038147004069228093')
n =mpz(' 831263642654418652091548394401765323910418765037717323148233269045801513578255419193021663895461573631914752687183420081180978296520838240666910250069803524914853414549730928025618751637395473628996254589435969599194922147193606480827954797733826570454519522481445234748629985683944574101405428806838560699393069275868598855839830515381289209431995786817509352748850205975872701746823289215353161865747032265288078527510528596539534739040061668737283516820861317692275587588783161683736664646522998281007168183900327066647572102109174763287279050410998866099737853013279916558671066134071773719338294046183557764557074103953899743371630421953773513819180087891998451975377770321988305301139378990916012908886598034486255391869797802060322650581426516022324761566431238215959751263669319523149142731894622772759785528451226120621701282149509524847341403745956988055525299874281640704238994146166008717217791140106091665905802366109484623642677006594202878124716900101129564012727662880868264515805882211770947605014323952213348233321179847281456503538426771724647461734897537750326022596814191062152252057429468509948378159900516783955126764113782900825196245693473595958396001181214043062293076950519939066234106200422038531883314033')

for i in range(99999999):
    if gmpy2.powmod(gmpy2.isqrt(leak + (i*n)), 2, n) == leak:
        phi = n-(gmpy2.isqrt(leak + (i*n)))
        print(f"phi = {n-(gmpy2.isqrt(leak + (i*n)))}")
        break



e = 0x10001

d = gmpy2.powmod(e, -1, phi)
print(f"d = {d}")

flag_int = gmpy2.powmod(enc_flag, d, n)
print(f'flag_int = {flag_int}')
flag_hex = flag_int.digits(16)
print(f'flag_hex = {flag_hex}')

#FLAG = bytes.fromhex(flag_hex)
#print(FLAG)

# -*- coding: utf-8 -*-

import re
import urllib.parse
from flask import Flask, request, render_template
from bs4 import BeautifulSoup
from versionsDB import versions_search


lists = []
lists.append('I-#Idim-IIm7-#IIdim-IIIm7')
lists.append('I-#Idim-IIm7-V7')
lists.append('I-I+-IV-#IVdim')
lists.append('I-I7-IV-#IVdim')
lists.append('I-I7-IV-IVm')
lists.append('I-IIm7-IIIm7-IIm7')
lists.append('I-IIm7-IIIm7-bIIIdim')
lists.append('I-III7-IImin')
lists.append('I-III7-IV-II7-V7')
lists.append('I-III7-IV')
lists.append('I-III7-VI7-II7-V7')
lists.append('I-III7-VI7-II7-IIm')
lists.append('I-III7-VI7-II7-IVm')
lists.append('I-III7-VIm-II7')
lists.append('I-IIIm7b5-VI7')
lists.append('I-IV7')
lists.append('I-IVm')
lists.append('I-VI7-II7-V7')
lists.append('I-VI7-IIm7-V7')
lists.append('I-VI7-IV-IVm')
lists.append('I-VI7-VIIm7b5-III7')
lists.append('I-VIm7-IIm7-V7')
lists.append('I-VII7-I')
lists.append('I-VII7-III7-VI7-II7-V7')
lists.append('I-bVII7-VI7')
lists.append('I-bVII7-VI7-II7-V7')
lists.append('I-IV')
lists.append('I-Im7')
lists.append('I-Im')
lists.append('I-II7b5')
lists.append('I-VIm7-IIIm7')
lists.append('Im')
lists.append('I7-IV')
lists.append('I7-IV-III7-VIm-II7')
lists.append('I7-IV-VI7-IIm')
lists.append('I7-IV7-bVII7-bIII7-V7')
lists.append('I7-IVm')
lists.append('I7-VII7-bVII7-VI7')
lists.append('I7+')
lists.append('II')
lists.append('IIm')
lists.append('IIm-VIm')
lists.append('IIm7-V7-downinwholesteps')
lists.append('IIm7-Vm7')
lists.append('IIm7b5-V7')
lists.append('II7')
lists.append('II7-V7')
lists.append('II7-bII7-I')
lists.append('III')
lists.append('IIIm')
lists.append('IIIm7-VI7-II7-IIm7-V7')
lists.append('IIIm7-VI7-IIm7-V7')
lists.append('IIIm7-bIII7-IIm7-bII7-I')
lists.append('IIIm7-bIIIm7-IIm7-V7')
lists.append('IIIm7b5-VI7')
lists.append('IIIm7b5-VI7-IIm7b5-V7')
lists.append('IIIm7b5-VI7-IIm-IIm7-V7')
lists.append('IIIm7b5-VI7-IV-IVm')
lists.append('III7-IV-IVm')
lists.append('III7-VI7-II7-V7')
lists.append('IV')
lists.append('IV-#IVdim-I')
lists.append('IV-IVm')
lists.append('IV-bVI')
lists.append('IVm')
lists.append('IVm6')
lists.append('IV7')
lists.append('IV7-III7-VI7-II7')
lists.append('V')
lists.append('V-VI')
lists.append('Vm')
lists.append('Vm7')
lists.append('V7+')
lists.append('V7sus')
lists.append('VI')
lists.append('VI-V')
lists.append('VIm')
lists.append('VIm-IIm')
lists.append('VIm-II7')
lists.append('VIm-III')
lists.append('VIm-IIIm')
lists.append('VI7-IIm')
lists.append('VI7-II7-V7-I')
lists.append('VI7-IV-IVm')
lists.append('VI7-IV')
lists.append('VII')
lists.append('VII-I')
lists.append('VIIm')
lists.append('VIIm7b5-III7-VIm7-II7I')
lists.append('VII7')
lists.append('VII7-III7-VI7-II7-V7')
lists.append('bII')
lists.append('bIIm')
lists.append('bII7')
lists.append('bII7-bVI7-V7')
lists.append('bIII')
lists.append('bIII-bVI-bII')
lists.append('bIIIm')
lists.append('bIII7')
lists.append('bIIIdim')
lists.append('bV')
lists.append('bVI')
lists.append('bVI-bV')
lists.append('bVI7')
lists.append('bVI7-V7')
lists.append('bVII')
lists.append('bVIIm')
lists.append('bVII7-VI7')
lists.append('bVII7-VI7-II7')
lists.append('bVII7-VI7-II7-V7')
lists.append('bVII7-VI7-IIm')
lists.append('bVII7-VI7-bVI7-V7')
lists.append('start_IV')
lists.append('start_IV-IVm')
lists.append('start_II7')
lists.append('start_bVI7-V7')
lists.append('start_VIm-VIm/maj7-VIm7-VIm6')
lists.append('start_VIm7')
lists.append('IIm7-V7_down_in_half_steps')
lists.append('A_section_IIm7-V7')
lists.append('I')
lists.append('Im')
lists.append('I7-VII7-bVII7-VI7')
lists.append('II')
lists.append('IIm')
lists.append('III')
lists.append('IIIm')
lists.append('III7-VI7-II7-V7')
lists.append('IV')
lists.append('IV-I')
lists.append('IV-IIm')
lists.append('IV-III7-VI7-II7-V7')
lists.append('IV-III')
lists.append('IV-IVm')
lists.append('IV-V_or_IV-II7-V7')
lists.append('IV-bIII')
lists.append('IV-bVI')
lists.append('IV-#IVdim-I')
lists.append('IVm')
lists.append('IV7')
lists.append('V')
lists.append('V-VI')
lists.append('Vm')
lists.append('VI7-II7-V7')
lists.append('VI')
lists.append('VIm')
lists.append('VIm-IIm')
lists.append('VII')
lists.append('VIIm')
lists.append('bII')
lists.append('bII7')
lists.append('bIII')
lists.append('bIII7')
lists.append('bV')
lists.append('bVI')
lists.append('bVI-bV')
lists.append('bVI7')
lists.append('bVII')
lists.append('bVII-bV')
lists.append('5th_cycle')
lists.append('V7_down_chroma')
lists.append('IIm7-V7_down_whole_steps')
lists.append('IIm7b5-V7_down_whole_steps')

list_titles = []
list_titles.append('A PORTRAIT OF JENNIE')
list_titles.append('A FOGGY DAY')
list_titles.append('AFTER YOU\'VE GONE')
list_titles.append('AIN\'T MISBEHAVIN')
list_titles.append('AIREGIN')
list_titles.append('AIR MAIL SPECIAL')
list_titles.append('ALEXANDER\'S RAGTIME BAND')
list_titles.append('ALL BLUES')
list_titles.append('ALL GOD\'S CHILDREN GOT RHYTHM')
list_titles.append('ALL OF ME')
list_titles.append('ALL OF YOU')
list_titles.append('ALL THE THINGS YOU ARE')
list_titles.append('ALMOST LIKE BEING IN LOVE')
list_titles.append('ALONE TOGETHER')
list_titles.append('ALONG CAME BETTY')
list_titles.append('ALWAYS')
list_titles.append('AMAZING GRACE')
list_titles.append('AM I BLUE')
list_titles.append('ANGEL EYES')
list_titles.append('ANYTHING GOES')
list_titles.append('APRIL IN PARIS')
list_titles.append('AREN\'T YOU GLAD YOU\'RE YOU')
list_titles.append('AS LONG AS I LIVE')
list_titles.append('AS TIME GOES BY')
list_titles.append('AT SUNDOWN')
list_titles.append('AUTUMN IN NEW YORK')
list_titles.append('AUTUMN LEAVES')
list_titles.append('AVALON')
list_titles.append('AZURE')
list_titles.append('BASIN STREET BLUES')
list_titles.append('BAUBLES BANGLES AND BEADS')
list_titles.append('BEAUTIFUL LOVE')
list_titles.append('BERNIE\'S TUNE')
list_titles.append('BETWEEN THE DEVIL AND THE DEEP BLUE SEA')
list_titles.append('BEWITCHED BOTHERED AND BEWILDERED')
list_titles.append('BIDIN MY TIME')
list_titles.append('BILL BAILEY')
list_titles.append('BIRTH OF THE BLUES')
list_titles.append('BLACK AND BLUE')
list_titles.append('BLACK COFFEE')
list_titles.append('BLUE BOSSA')
list_titles.append('BLUE LOU')
list_titles.append('BLUE MONK ')
list_titles.append('BLUE MOON')
list_titles.append('BLUE ROOM (THE)')
list_titles.append('BLUESETTE')
list_titles.append('BLUE SKIES')
list_titles.append('BODY AND SOUL')
list_titles.append('BORN TO BE BLUE')
list_titles.append('BROADWAY')
list_titles.append('BUT BEAUTIFUL')
list_titles.append('BUT NOT FOR ME')
list_titles.append('BYE BYE BLACKBIRD')
list_titles.append('BYE BYE BLUES')
list_titles.append('BY MYSELF')
list_titles.append('CABIN IN THE SKY')
list_titles.append('CAN\'T GET OUT OF THIS MOOD')
list_titles.append('CAN\'T HELP LOVIN DAT MAN')
list_titles.append('CAN\'T WE BE FRIENDS')
list_titles.append('CARAVAN')
list_titles.append('CARNIVAL (BLACK ORPHEUS)')
list_titles.append('CHEEK TO CHEEK')
list_titles.append('CHELSEA BRIDGE')
list_titles.append('CHEROKEE')
list_titles.append('CHICAGO')
list_titles.append('CHRISTMAS SONG')
list_titles.append('COME RAIN OR COME SHINE')
list_titles.append('COMES LOVE')
list_titles.append('CONFIRMATION')
list_titles.append('CORCOVADO')
list_titles.append('COTTAGE FOR SALE')
list_titles.append('COTTON TAIL')
list_titles.append('CRAZY RHYTHM')
list_titles.append('CRY ME A RIVER')
list_titles.append('CUTE')
list_titles.append('DANCING IN THE DARK')
list_titles.append('DANCING ON THE CEILING')
list_titles.append('DANNY BOY')
list_titles.append('DARN THAT DREAM')
list_titles.append('DAY BY DAY')
list_titles.append('DAY IN  DAY OUT')
list_titles.append('DAYS OF WINE AND ROSES')
list_titles.append('DEARLY BELOVED')
list_titles.append('DEED I DO')
list_titles.append('DEEP PURPLE')
list_titles.append('DESAFINADA')
list_titles.append('DJANGO')
list_titles.append('DO NOTHIN TILL YOU HEAR FROM ME')
list_titles.append('DON\'T BLAME ME')
list_titles.append('DON\'T GET AROUND MUCH ANY MORE')
list_titles.append('DON\'T TAKE YOUR LOVE FROM ME')
list_titles.append('DOXY')
list_titles.append('EAST OF THE SUN')
list_titles.append('EASY LIVIN')
list_titles.append('EASY TO LOVE')
list_titles.append('EMBRACEABLE YOU')
list_titles.append('EPISTROPHY')
list_titles.append('EVERYTHING HAPPENS TO ME')
list_titles.append('EVERYTHING I\'VE GOT BELONGS TO YOU')
list_titles.append('EVERY TIME WE SAY GOODBYE')
list_titles.append('EXACTLY LIKE YOU')
list_titles.append('FALLING IN LOVE WITH LOVE')
list_titles.append('FASCINATING RHYTHM')
list_titles.append('FINE AND DANDY')
list_titles.append('FINE ROMANCE (A)')
list_titles.append('FLY ME TO THE MOON')
list_titles.append('FOLKS WHO LIVE ON THE HILL')
list_titles.append('FOOLS RUSH IN')
list_titles.append('FOR ALL WE KNOW')
list_titles.append('FOUR')
list_titles.append('FREDDIE THE FREELOADER')
list_titles.append('FROM THIS MOMENT ON')
list_titles.append('GAL IN CALICO')
list_titles.append('GEE BABY AIN\'T I GOOD TO YOU')
list_titles.append('GEORGIA ON MY MIND')
list_titles.append('GET HAPPY')
list_titles.append('GET OUT OF TOWN')
list_titles.append('GHOST OF A CHANCE WITH YOU')
list_titles.append('GIANT STEPS')
list_titles.append('GIRL FROM IPANEMA')
list_titles.append('GIVE ME THE SIMPLE LIFE')
list_titles.append('GLAD TO BE UNHAPPY')
list_titles.append('GOD BLESS THE CHILD')
list_titles.append('GONE WITH THE WIND')
list_titles.append('GREEN DOLPHIN STREET')
list_titles.append('GROOVIN HIGH')
list_titles.append('HALLELUJAH')
list_titles.append('HAVE YOU MET MISS JONES')
list_titles.append('HEAT WAVE')
list_titles.append('HERE\'S THAT RAINY DAY')
list_titles.append('HONEYSUCKLE ROSE')
list_titles.append('HOW ABOUT YOU')
list_titles.append('HOW DEEP IS THE OCEAN')
list_titles.append('HOW HIGH THE MOON')
list_titles.append('HOW INSENSITIVE')
list_titles.append('HOW LONG HAS THIS BEEN GOING ON')
list_titles.append('I CAN\'T BELIEVE THAT YOUR IN LOVE')
list_titles.append('I CAN\'T GET STARTED WITH YOU')
list_titles.append('I CAN\'T GIVE YOU ANYTHING BUT LOVE')
list_titles.append('I CONCENTRATE ON YOU')
list_titles.append('I COULD WRITE A BOOK')
list_titles.append('I COVER THE WATERFRONT')
list_titles.append('IDAHO')
list_titles.append('I DIDN\'T KNOW WHAT TIME IT WAS')
list_titles.append('I DON\'T KNOW WHY')
list_titles.append('I FALL IN LOVE TOO EASILY')
list_titles.append('IF I HAD YOU')
list_titles.append('IF I LOVE AGAIN')
list_titles.append('IF I SHOULD LOSE YOU')
list_titles.append('IF I WERE A BELL')
list_titles.append('I FOUND A NEW BABY')
list_titles.append('IF THERE IS SOMEONE LOVELIER')
list_titles.append('IF YOU COULD SEE ME NOW')
list_titles.append('I GET A KICK OUT OF YOU')
list_titles.append('I GOT IT BAD')
list_titles.append('I GOT RHYTHM')
list_titles.append('I HADN\'T ANYONE \'TIL YOU')
list_titles.append('I HEAR A RHAPSODY')
list_titles.append('I HEAR MUSIC')
list_titles.append('I LEFT MY HEART IN SAN FRANCISCO')
list_titles.append('I LET A SONG GO OUT  OF MY HEART')
list_titles.append('I\'LL BE AROUND')
list_titles.append('I\'LL BE SEEING YOU')
list_titles.append('I\'LL GET BY')
list_titles.append('I\'LL NEVER BE THE SAME')
list_titles.append('I\'LL REMEMBER APRIL')
list_titles.append('I\'LL STRING ALONG WITH YOU')
list_titles.append('I\'LL TAKE MANHATTAN')
list_titles.append('I\'LL TAKE ROMANCE')
list_titles.append('ILL WIND')
list_titles.append('I LOVE PARIS')
list_titles.append('I LOVE YOU')
list_titles.append('IMAGINATION')
list_titles.append('I MAY BE WRONG')
list_titles.append('I\'M BEGINNING TO SEE THE LIGHT')
list_titles.append('I\'M CONFESSIN')
list_titles.append('I\'M GETTIN SENTIMENTAL OVER YOU')
list_titles.append('I\'M GLAD THERE IS YOU')
list_titles.append('I\'M IN THE MOOD FOR LOVE')
list_titles.append('I\'M OLD FASHIONED')
list_titles.append('IN A MELLOW TONE')
list_titles.append('IN A SENTIMENTAL MOOD')
list_titles.append('INDIANA')
list_titles.append('INDIAN SUMMER')
list_titles.append('I NEVER KNEW')
list_titles.append('IN MY SOLITUDE')
list_titles.append('INVITATION')
list_titles.append('IN YOUR OWN SWEET WAY')
list_titles.append('I REMEMBER YOU')
list_titles.append('I SHOULD CARE')
list_titles.append('ISN\'T IT ROMANTIC')
list_titles.append('I SURRENDER DEAR')
list_titles.append('IT COULD HAPPEN TO YOU')
list_titles.append('IT DON\'T MEAN A THING')
list_titles.append('IT HAD TO BE YOU')
list_titles.append('I THOUGHT ABOUT YOU')
list_titles.append('IT MIGHT AS WELL BE SPRING')
list_titles.append('IT NEVER ENTERED MY MIND')
list_titles.append('IT\'S ALL RIGHT WITH ME')
list_titles.append('IT\'S ONLY A PAPER MOON')
list_titles.append('IT\'S THE TALK OF THE TOWN')
list_titles.append('IT\'S YOU OR NO ONE')
list_titles.append('IT WAS JUST ONE OF THOSE THINGS')
list_titles.append('I\'VE GOT A CRUSH ON YOU')
list_titles.append('I\'VE GOT MY LOVE TO KEEP ME WARM')
list_titles.append('I\'VE GOT THE WORLD ON A STRING')
list_titles.append('I\'VE GOT YOU UNDER MY SKIN')
list_titles.append('I\'VE GROWN ACCUSTOMED TO YOUR FACE')
list_titles.append('I WANT TO BE HAPPY')
list_titles.append('I WISH I WERE IN LOVE AGAIN')
list_titles.append('I WON\'T DANCE')
list_titles.append('JEEPERS  CREEPERS')
list_titles.append('JORDU')
list_titles.append('JOY SPRING')
list_titles.append('JUST FRIENDS')
list_titles.append('JUST IN TIME')
list_titles.append('JUST SQUEEZE ME')
list_titles.append('JUST YOU JUST ME')
list_titles.append('LADY BE GOOD')
list_titles.append('LADY BIRD')
list_titles.append('LADY IN RED')
list_titles.append('LADY IS A TRAMP')
list_titles.append('LAST TIME I SAW PARIS')
list_titles.append('LAURA')
list_titles.append('LAZYBIRD')
list_titles.append('LET\'S FACE THE MUSIC AND DANCE')
list_titles.append('LIKE SOMEONE IN LOVE')
list_titles.append('LIL DARLIN')
list_titles.append('LIMEHOUSE BLUES')
list_titles.append('LITTLE WHITE LIES')
list_titles.append('LIZA')
list_titles.append('LONG AGO AND FAR AWAY')
list_titles.append('LOOK FOR THE SILVER LINING')
list_titles.append('LOOKING FOR A BOY')
list_titles.append('LOVE FOR SALE')
list_titles.append('LOVE ME OR LEAVE ME')
list_titles.append('LOVE NEST (THE)')
list_titles.append('LOVER COME BACK TO ME')
list_titles.append('LOVER')
list_titles.append('LOVER MAN')
list_titles.append('LOVE WALKED IN')
list_titles.append('LULLABY IN RHYTHM')
list_titles.append('LULLABY OF BIRDLAND')
list_titles.append('LULLABY OF BROADWAY')
list_titles.append('LULLABY OF THE LEAVES')
list_titles.append('MAKIN WHOOPEE')
list_titles.append('MEAN TO ME')
list_titles.append('MEDITATION')
list_titles.append('MEMORIES OF YOU')
list_titles.append('MISTY')
list_titles.append('MOOD  INDIGO')
list_titles.append('MOONGLOW')
list_titles.append('MOONLIGHT IN VERMONT')
list_titles.append('MORE THAN YOU KNOW')
list_titles.append('MOUNTAIN GREENERY')
list_titles.append('MY BLUE HEAVEN')
list_titles.append('MY FAVORITE THINGS')
list_titles.append('MY FOOLISH HEART')
list_titles.append('MY FUNNY VALENTINE')
list_titles.append('MY HEART BELONGS TO DADDY')
list_titles.append('MY HEART STOOD STILL')
list_titles.append('MY IDEAL')
list_titles.append('MY MELANCHOLY BABY')
list_titles.append('MY OLD FLAME')
list_titles.append('MY ONE AND ONLY LOVE')
list_titles.append('MY ROMANCE')
list_titles.append('MY SHINING HOUR')
list_titles.append('MY SHIP')
list_titles.append('MY SILENT LOVE')
list_titles.append('NEARNESS OF YOU (THE)')
list_titles.append('NICE WORK IF YOU CAN GET IT')
list_titles.append('NIGHT AND DAY')
list_titles.append('NIGHT IN TUNISIA')
list_titles.append('NOBODY ELSE BUT ME')
list_titles.append('NO MOON AT ALL')
list_titles.append('OLD DEVIL MOON')
list_titles.append('ON A CLEAR DAY')
list_titles.append('ON A SLOW BOAT TO CHINA')
list_titles.append('ONCE IN A WHILE')
list_titles.append('ONE I LOVE BELONGS TO SOMEBODY')
list_titles.append('ONE NOTE SAMBA')
list_titles.append('ON THE STREET WHERE YOU LIVE')
list_titles.append('ON THE SUNNY SIDE OF THE STREET')
list_titles.append('OUR DAY WILL COME')
list_titles.append('OUR LOVE IS HERE TO STAY')
list_titles.append('OUT OF NOWHERE')
list_titles.append('OUT OF THIS WORLD')
list_titles.append('OVER THE RAINBOW')
list_titles.append('PENNIES FROM HEAVEN')
list_titles.append('PEOPLE WILL SAY WE\'RE IN LOVE')
list_titles.append('PERDIDO')
list_titles.append('PICK YOURSELF UP')
list_titles.append('POLKA DOTS AND MOONBEAMS')
list_titles.append('POOR BUTTERFLY')
list_titles.append('PRELUDE TO A KISS')
list_titles.append('QUIET NIGHTS OF QUIET STARS')
list_titles.append('RECORDAME')
list_titles.append('ROSE ROOM')
list_titles.append('ROSETTA')
list_titles.append('ROUND MIDNIGHT')
list_titles.append('RUBY MY DEAR')
list_titles.append('SAMBA DE ORFEU')
list_titles.append('SATIN DOLL')
list_titles.append('SAVOY BLUES')
list_titles.append('SCRAPPLE FROM THE APPLE')
list_titles.append('SECRET LOVE')
list_titles.append('SEPTEMBER IN THE RAIN')
list_titles.append('SEPTEMBER SONG')
list_titles.append('SEVEN COME ELEVEN')
list_titles.append('SHADOW OF YOUR SMILE')
list_titles.append('SHE\'S FUNNY THAT WAY')
list_titles.append('SHINY STOCKINGS')
list_titles.append('SKYLARK')
list_titles.append('SMOKE GETS IN YOUR EYES')
list_titles.append('SOFTLY AS IN A MORNING SUNRISE')
list_titles.append('SO IN LOVE')
list_titles.append('SOLAR')
list_titles.append('SOMEBODY LOVES ME')
list_titles.append('SOMEDAY MY PRINCE WILL COME')
list_titles.append('SOMEONE TO WATCH OVER ME')
list_titles.append('SOMETIMES I\'M HAPPY')
list_titles.append('THE SONG IS YOU')
list_titles.append('SOON')
list_titles.append('SOPHISTICATED LADY')
list_titles.append('SO WHAT')
list_titles.append('SPEAK LOW')
list_titles.append('S\'POSIN')
list_titles.append('SPRING IS HERE')
list_titles.append('STARDUST')
list_titles.append('STAR EYES')
list_titles.append('STARS FELL ON ALABAMA')
list_titles.append('STELLA BY STARLIGHT')
list_titles.append('ST JAMES INFIRMARY BLUES')
list_titles.append('ST LOUIS BLUES')
list_titles.append('STOMPIN AT THE SAVOY')
list_titles.append('STORMY WEATHER')
list_titles.append('STREET OF DREAMS')
list_titles.append('STRIKE UP THE BAND')
list_titles.append('ST THOMAS')
list_titles.append('SUGAR')
list_titles.append('SUMMERTIME')
list_titles.append('SWEET AND LOVELY')
list_titles.append('SWEET GEORGIA BROWN')
list_titles.append('SWEETHEARTS ON PARADE')
list_titles.append('SWEET LORRAINE')
list_titles.append('SWINGING ON A STAR')
list_titles.append('S\'WONDERFUL')
list_titles.append('TAKE FIVE')
list_titles.append('TAKE THE A TRAIN')
list_titles.append('TAKING A CHANCE ON LOVE')
list_titles.append('TANGERINE')
list_titles.append('TEA FOR TWO')
list_titles.append('TENDERLY')
list_titles.append('THAT OLD FEELING')
list_titles.append('THE END OF A LOVE AFFAIR')
list_titles.append('THE MAN I LOVE')
list_titles.append('THE MORE I SEE YOU')
list_titles.append('THE WAY YOU LOOK TONIGHT')
list_titles.append('THERE IS NO GREATER LOVE')
list_titles.append('THERE\'S A SMALL HOTEL')
list_titles.append('THERE WILL NEVER BE ANOTHER YOU')
list_titles.append('THESE FOOLISH THINGS')
list_titles.append('THEY ALL LAUGHED')
list_titles.append('THEY CAN\'T TAKE THAT AWAY')
list_titles.append('THINGS AIN\'T WHAT THEY USED TO BE')
list_titles.append('THIS CAN\'T BE LOVE')
list_titles.append('THIS YEARS KISSES')
list_titles.append('THOU SWELL')
list_titles.append('THREE LITTLE WORDS')
list_titles.append('TIME AFTER TIME')
list_titles.append('TOO MARVELOUS FOR WORDS')
list_titles.append('TOUCH OF YOUR LIPS (THE)')
list_titles.append('TRY A LITTLE TENDERNESS')
list_titles.append('TUNE UP')
list_titles.append('TWO SLEEPY PEOPLE')
list_titles.append('UNDECIDED')
list_titles.append('UNTIL THE REAL THING COMES ALONG')
list_titles.append('UP A LAZY RIVER')
list_titles.append('VERY THOUGHT OF YOUTHE')
list_titles.append('WAIT TILL YOU SEE HER')
list_titles.append('WAVE')
list_titles.append('WELL YOU NEEDN\'T')
list_titles.append('WHAT A DIFFERENCE A DAY MADE')
list_titles.append('WHAT A LITTLE MOONLIGHT CAN DO')
list_titles.append('WHAT IS THERE TO SAY')
list_titles.append('WHAT IS THIS THING CALLED LOVE')
list_titles.append('WHAT\'LL I DO')
list_titles.append('WHAT\'S NEW')
list_titles.append('WHEN I FALL IN LOVE')
list_titles.append('WHEN SUNNY GETS BLUE')
list_titles.append('WHEN THE SAINTS GO MARCHING IN')
list_titles.append('WHEN YOUR LOVER HAS GONE')
list_titles.append('WHEN YOU WISH UPON A STAR')
list_titles.append('WHERE OR WHEN')
list_titles.append('WHIFFENPOOF SONG')
list_titles.append('WHISPERING')
list_titles.append('WHITE CHRISTMAS')
list_titles.append('WHO CARES')
list_titles.append('WHY SHOULDN\'T I')
list_titles.append('WILLOW WEEP FOR ME')
list_titles.append('WITH THE WIND AND THE RAIN')
list_titles.append('WORLD IS WAITING FOR THE SUNRISE')
list_titles.append('WRAP YOUR TROUBLES IN DREAMS')
list_titles.append('YARDBIRD SUITE')
list_titles.append('YESTERDAY')
list_titles.append('YESTERDAYS')
list_titles.append('YOU AND THE NIGHT AND THE MUSIC')
list_titles.append('YOU BROUGHT A NEW KIND OF LOVE')
list_titles.append('YOU\'D BE SO NICE TO COME HOME TO')
list_titles.append('YOU DON\'T KNOW WHAT LOVE IS')
list_titles.append('YOU DO SOMETHING TO ME')
list_titles.append('YOU GO TO MY HEAD')
list_titles.append('YOURS IS MY HEART ALONE')
list_titles.append('YOU SAY YOU CARE')
list_titles.append('YOU STEPPED OUT OF A DREAM')
list_titles.append('YOU TOOK ADVANTAGE OF ME')
list_titles.append('ZING WENT THE STRINGS')

list_cadence = []
list_cadence.append('I-#Idim-IIm7-#IIdim-IIIm7')
list_cadence.append('I-#Idim-IIm7-V7')
list_cadence.append('I-I+-IV-#IVdim')
list_cadence.append('I-I7-IV-#IVdim')
list_cadence.append('I-I7-IV-IVm')
list_cadence.append('I-IIm7-IIIm7-IIm7')
list_cadence.append('I-IIm7-IIIm7-bIIIdim')
list_cadence.append('I-III7-IImin')
list_cadence.append('I-III7-IV-II7-V7')
list_cadence.append('I-III7-IV')
list_cadence.append('I-III7-VI7-II7-V7')
list_cadence.append('I-III7-VI7-II7-IIm')
list_cadence.append('I-III7-VI7-II7-IVm')
list_cadence.append('I-III7-VIm-II7')
list_cadence.append('I-IIIm7b5-VI7')
list_cadence.append('I-IV7')
list_cadence.append('I-IVm')
list_cadence.append('I-VI7-II7-V7')
list_cadence.append('I-VI7-IIm7-V7')
list_cadence.append('I-VI7-IV-IVm')
list_cadence.append('I-VI7-VIIm7b5-III7')
list_cadence.append('I-VIm7-IIm7-V7')
list_cadence.append('I-VII7-I')
list_cadence.append('I-VII7-III7-VI7-II7-V7')
list_cadence.append('I-bVII7-VI7')
list_cadence.append('I-bVII7-VI7-II7-V7')
list_cadence.append('I-IV')
list_cadence.append('I-Im7')
list_cadence.append('I-Im')
list_cadence.append('I-II7b5')
list_cadence.append('I-VIm7-IIIm7')
list_cadence.append('Im')
list_cadence.append('I7-IV')
list_cadence.append('I7-IV-III7-VIm-II7')
list_cadence.append('I7-IV-VI7-IIm')
list_cadence.append('I7-IV7-bVII7-bIII7-V7')
list_cadence.append('I7-IVm')
list_cadence.append('I7-VII7-bVII7-VI7')
list_cadence.append('I7+')
list_cadence.append('II')
list_cadence.append('IIm')
list_cadence.append('IIm-VIm')
list_cadence.append('IIm7-V7-downinwholesteps')
list_cadence.append('IIm7-Vm7')
list_cadence.append('IIm7b5-V7')
list_cadence.append('II7')
list_cadence.append('II7-V7')
list_cadence.append('II7-bII7-I')
list_cadence.append('III')
list_cadence.append('IIIm')
list_cadence.append('IIIm7-VI7-II7-IIm7-V7')
list_cadence.append('IIIm7-VI7-IIm7-V7')
list_cadence.append('IIIm7-bIII7-IIm7-bII7-I')
list_cadence.append('IIIm7-bIIIm7-IIm7-V7')
list_cadence.append('IIIm7b5-VI7')
list_cadence.append('IIIm7b5-VI7-IIm7b5-V7')
list_cadence.append('IIIm7b5-VI7-IIm-IIm7-V7')
list_cadence.append('IIIm7b5-VI7-IV-IVm')
list_cadence.append('III7-IV-IVm')
list_cadence.append('III7-VI7-II7-V7')
list_cadence.append('IV')
list_cadence.append('IV-#IVdim-I')
list_cadence.append('IV-IVm')
list_cadence.append('IV-bVI')
list_cadence.append('IVm')
list_cadence.append('IVm6')
list_cadence.append('IV7')
list_cadence.append('IV7-III7-VI7-II7')
list_cadence.append('V')
list_cadence.append('V-VI')
list_cadence.append('Vm')
list_cadence.append('Vm7')
list_cadence.append('V7+')
list_cadence.append('V7sus')
list_cadence.append('VI')
list_cadence.append('VI-V')
list_cadence.append('VIm')
list_cadence.append('VIm-IIm')
list_cadence.append('VIm-II7')
list_cadence.append('VIm-III')
list_cadence.append('VIm-IIIm')
list_cadence.append('VI7-IIm')
list_cadence.append('VI7-II7-V7-I')
list_cadence.append('VI7-IV-IVm')
list_cadence.append('VI7-IV')
list_cadence.append('VII')
list_cadence.append('VII-I')
list_cadence.append('VIIm')
list_cadence.append('VIIm7b5-III7-VIm7-II7I')
list_cadence.append('VII7')
list_cadence.append('VII7-III7-VI7-II7-V7')
list_cadence.append('bII')
list_cadence.append('bIIm')
list_cadence.append('bII7')
list_cadence.append('bII7-bVI7-V7')
list_cadence.append('bIII')
list_cadence.append('bIII-bVI-bII')
list_cadence.append('bIIIm')
list_cadence.append('bIII7')
list_cadence.append('bIIIdim')
list_cadence.append('bV')
list_cadence.append('bVI')
list_cadence.append('bVI-bV')
list_cadence.append('bVI7')
list_cadence.append('bVI7-V7')
list_cadence.append('bVII')
list_cadence.append('bVIIm')
list_cadence.append('bVII7-VI7')
list_cadence.append('bVII7-VI7-II7')
list_cadence.append('bVII7-VI7-II7-V7')
list_cadence.append('bVII7-VI7-IIm')
list_cadence.append('bVII7-VI7-bVI7-V7')
list_cadence.append('start_IV')
list_cadence.append('start_IV-IVm')
list_cadence.append('start_II7')
list_cadence.append('start_bVI7-V7')
list_cadence.append('start_VIm-VIm/maj7-VIm7-VIm6')
list_cadence.append('start_VIm7')
list_cadence.append('IIm7-V7_down_in_half_steps')
list_cadence.append('A_section_IIm7-V7')


list_bridge = []
list_bridge.append('I')
list_bridge.append('Im')
list_bridge.append('I7-VII7-bVII7-VI7')
list_bridge.append('II')
list_bridge.append('IIm')
list_bridge.append('III')
list_bridge.append('IIIm')
list_bridge.append('III7-VI7-II7-V7')
list_bridge.append('IV')
list_bridge.append('IV-I')
list_bridge.append('IV-IIm')
list_bridge.append('IV-III7-VI7-II7-V7')
list_bridge.append('IV-III')
list_bridge.append('IV-IVm')
list_bridge.append('IV-V_or_IV-II7-V7')
list_bridge.append('IV-bIII')
list_bridge.append('IV-bVI')
list_bridge.append('IV-#IVdim-I')
list_bridge.append('IVm')
list_bridge.append('IV7')
list_bridge.append('V')
list_bridge.append('V-VI')
list_bridge.append('Vm')
list_bridge.append('VI7-II7-V7')
list_bridge.append('VI')
list_bridge.append('VIm')
list_bridge.append('VIm-IIm')
list_bridge.append('VII')
list_bridge.append('VIIm')
list_bridge.append('bII')
list_bridge.append('bII7')
list_bridge.append('bIII')
list_bridge.append('bIII7')
list_bridge.append('bV')
list_bridge.append('bVI')
list_bridge.append('bVI-bV')
list_bridge.append('bVI7')
list_bridge.append('bVII')
list_bridge.append('bVII-bV')
list_bridge.append('5th_cycle')
list_bridge.append('V7_down_chroma')
list_bridge.append('IIm7-V7_down_whole_steps')
list_bridge.append('IIm7b5-V7_down_whole_steps')

###########################################

app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template('home_page.html')

@app.route('/search')
def search():
#rechercher un standard
	search_title = request.args.get('title','')
	if search_title:
		regex = re.compile(r'.*'+search_title+'.*',re.IGNORECASE)
		results_title = []
		selectobj = filter(regex.search, list_titles)
		for val in selectobj:
			results_title.append(val)
	else: 
		results_title = []
		
#rechercher les versions d\'un standard
	search_versions = request.args.get('versions','')
	s = versions_search()
	s.init_versionsDB()
	if search_versions:
		results_versions = []
		regex = re.compile(r'.*'+search_versions+'.*',re.IGNORECASE)
		selectobj = filter(regex.search, s.DB.keys())
		for val in selectobj:
			results_versions.append(val)
	else: 
		results_versions = []

#rechercher une cadence
	search_cadence = request.args.get('cadence','')
	if search_cadence:
		results_cadence = []
		for x in list_cadence:
			y = re.findall('\\b'+search_cadence, x)
			if y != []:
				results_cadence += [(x,list_cadence.index(x)+1)]
				list_name = lists[list_cadence.index(x)+1]
	else:
		results_cadence = []
	
#rechercher un pont
	search_bridge = request.args.get('bridge','')
	if search_bridge:
		results_bridge = []
		for x in list_bridge:
			y = re.findall('\\b'+search_bridge, x)
			if y != []:
				results_bridge += [(x,list_bridge.index(x)+121)]
	else:
		results_bridge = []

	return render_template('query_results.html', results_title=results_title, results_cadence=results_cadence, results_bridge=results_bridge, results_versions=results_versions)

@app.route('/list')
def view_list():
	list_number = request.args.get('')
	f = open('static/lists/list'+list_number+'.html', encoding='ISO 8859-1')
	content = f.read()
	s = BeautifulSoup(content,'html.parser')
	title_list = []
	for y in s.findAll('a', href=True):
		g = open('static/corpus-list/'+y['href'], encoding='ISO 8859-1')
		content2 = g.read()
		t = BeautifulSoup(content2, 'html.parser')
		title = t.find('h4')
		if title:
			title_list += [(title.text,y['href'])]
			
	list_name=lists[int(re.findall(r'(\d+)',list_number)[0])-1]
	
	return render_template('list_results.html', title_list=title_list, list_name=list_name)
				
@app.route('/view/')
def view_theme():
	
#afficher la grille
	view_word = request.args.get('')
	f = open('static/corpus-html/'+view_word+'.html')
	plain = f.read()
	s = BeautifulSoup(plain, 'html.parser')
	title = s.find('h4').text
	title_encoded = urllib.parse.quote(title)
	results = []
	for corpus in s.findAll('pre'):
		results.append(corpus.text)

	return render_template('view_theme.html', results=results, title=title, title_encoded=title_encoded)
	
@app.route('/view_list/')
def list_display():
	view_link = request.args.get('')
	f = open('static/corpus-list/'+view_link)
	plain = f.read()
	s = BeautifulSoup(plain, 'html.parser')
	title = s.find('h4').text
	title_encoded = urllib.parse.quote(title)
	results = []
	span_chords = []
	
	for corpus in s.findAll('pre'):
		results.append(corpus.text)
		
	span_chords = s.findAll('span')[0]
	
	list_name=lists[int(re.findall(r'(\d+)',view_link)[0])-1]
	
	return render_template('view_theme.html', results=results, title=title, title_encoded=title_encoded, span_chords=span_chords, list_name=list_name)

@app.route('/versions')
def versions():
	versions_query = str(request.args.get(''))
	s = versions_search()
	s.init_versionsDB()
	results_versions = s.DB.get(versions_query)
	
	return render_template('view_versions.html',results_versions=results_versions)
	
@app.route('/transpose')
def transpose_theme():
	
	results = []
	
	tune_coded = request.args.get('tune','')
	tune = urllib.parse.unquote(tune_coded)
	tone = request.args.get('tone','')
	
	
	pitch_flat = ('A','Bb','Cb','C','Db','D','Eb','E','F','Gb','G','Ab')
	pitch_sharp = ('A','A#','B','C','C#','D','D#','E','F','F#','G','G#')
	
	tone_flat = ('C','F','Bb','Eb','Ab','Db','Gb','Cb')
	tone_sharp = ('A#','D#','G#','C#','F#','B','E','A','D','G')
	
	f = open('static/corpus-html/'+tune+'.html')
	plain = f.read()
	occ = plain.find('Key of ')
	key = plain[occ+7:occ+9].strip()
	
	init_pitch = key
	final_pitch = tone

	#enharmonic choice
	if init_pitch in tone_flat:
		if final_pitch in tone_flat:
			index_init = pitch_flat.index(init_pitch)
			index_final = pitch_flat.index(final_pitch)
			diff = index_final - index_init
		elif final_pitch in tone_sharp:
			index_init = pitch_flat.index(init_pitch)
			index_final = pitch_sharp.index(final_pitch)
			diff = index_final - index_init
	elif init_pitch in tone_sharp:
		if final_pitch in tone_flat:
			index_init = pitch_sharp.index(init_pitch)
			index_final = pitch_flat.index(final_pitch)
			diff = index_final - index_init
		elif final_pitch in tone_sharp:
			index_init = pitch_sharp.index(init_pitch)
			index_final = pitch_sharp.index(final_pitch)
			diff = index_final - index_init
	
	corpus_list = []
	view_word = request.args.get('')
	f = open('static/corpus-html/'+tune+'.html')
	plain = f.read()
	s = BeautifulSoup(plain, 'html.parser')
	title = s.find('h4').text
	title_encoded = urllib.parse.quote(title)
	for corpus in s.findAll('pre'):
		corpus_list.append(corpus.text)

	chord_flat = set(re.findall(r'[ABCDEFG]b+', str(corpus_list)))
	chord_sharp = set(re.findall(r'[ABCDEFG]#+', str(corpus_list)))
	chord_none = set(re.findall(r'[ABCDEFG](?!b|#)+', str(corpus_list)))
	
	if chord_flat:
		for x in chord_flat:
			corpus_list = [y.replace(x,'*'+x) for y in corpus_list]
	if chord_sharp:
		for x in chord_sharp:
			corpus_list = [y.replace(x,'*'+x) for y in corpus_list]
	if chord_none:
		for x in chord_none:
			corpus_list = [y.replace(x,'*'+x) for y in corpus_list]

#transposition			
	if chord_flat:
		for x in chord_flat:
			if final_pitch in tone_flat:
				z = pitch_flat.index(x)
				q = z + diff
				pattern = re.compile(r'(\*\*|\*)'+ re.escape(x))
				if q <= 11:
					corpus_list = [re.sub(pattern,pitch_flat[q],y) for y in corpus_list]
				else:
					corpus_list = [re.sub(pattern,pitch_flat[q-12],y) for y in corpus_list]
			elif final_pitch in tone_sharp:
				for x in chord_flat:
					z = pitch_flat.index(x)
					q = z + diff
					pattern = re.compile(r'(\*\*|\*)'+ re.escape(x))
					if q <= 11:
						corpus_list = [re.sub(pattern,pitch_sharp[q],y) for y in corpus_list]
					else:
						corpus_list = [re.sub(pattern,pitch_sharp[q-12],y) for y in corpus_list]

	if chord_sharp:
		for x in chord_sharp:
			if final_pitch in tone_flat:
				z = pitch_sharp.index(x)
				q = z + diff
				pattern = re.compile(r'(\*\*|\*)'+ re.escape(x))
				if q <= 11:
					corpus_list = [re.sub(pattern,pitch_flat[q],y) for y in corpus_list]
				else:
					corpus_list = [re.sub(pattern,pitch_flat[q-12],y) for y in corpus_list]
			elif final_pitch in tone_sharp:
				z = pitch_sharp.index(x)
				q = z + diff
				pattern = re.compile(r'(\*\*|\*)'+ re.escape(x))
				if q <= 11:
					corpus_list = [re.sub(pattern,pitch_sharp[q],y) for y in corpus_list]
				else:
					corpus_list = [re.sub(pattern,pitch_sharp[q-12],y) for y in corpus_list]
				
	if chord_none:
		for x in chord_none:
			if final_pitch in tone_flat:
				z = pitch_flat.index(x)
				q = z + diff
				pattern_none = re.compile(r'\*'+re.escape(x)+'(?!b|#)+')
				if q <= 11:
					corpus_list = [re.sub(pattern_none,pitch_flat[q],y) for y in corpus_list]
				else:
					corpus_list = [re.sub(pattern_none,pitch_flat[q-12],y) for y in corpus_list]
			elif final_pitch in tone_sharp:
				z = pitch_sharp.index(x)
				q = z + diff
				pattern_none = re.compile(r'\*'+re.escape(x)+'(?!b|#)+')
				if q <= 11:
					corpus_list = [re.sub(pattern_none,pitch_sharp[q],y) for y in corpus_list]
				else:
					corpus_list = [re.sub(pattern_none,pitch_sharp[q-12],y) for y in corpus_list]

	for text_in_corpus in corpus_list:
		results.append(text_in_corpus)
	
	return render_template('view_theme.html', results=results, title=title, title_encoded=title_encoded)


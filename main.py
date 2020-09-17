# -*- coding: utf-8 -*-

import re
import os
import tempfile
import random
import string
import itertools
import urllib.parse
from flask import Flask, request, render_template
from flask_mail import Mail, Message
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

from midiutil import MIDIFile
from collections import defaultdict
from mido import MidiFile
from pydub import AudioSegment
from pydub.generators import Sine

from jazzreal.versionsDB import versions_search
from jazzreal.albumDB import album
from jazzreal.biographyDB import biography
from jazzreal.groupsDB import groups
from jazzreal.tracksDB import tracks
from jazzreal.membersDB import members
from jazzreal.nbenies_articlesDB import articles
from jazzreal.creditsDB import credits_db

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
list_titles.append('26-2')
list_titles.append('500 MILES HIGH')
list_titles.append('502 BLUES')
list_titles.append('52ND STREET THEME')
list_titles.append('920 SPECIAL')
list_titles.append('ACCENT TCHUATE THE POSITIVE')
list_titles.append('ACROSS THE VALLEY FROM THE ALAMO')
list_titles.append('ADAM\'S APPLE')
list_titles.append('A FELICIDADE')
list_titles.append('AFRO BLUE')
list_titles.append('AFRO CENTRIC')
list_titles.append('AFTERNOON IN PARIS')
list_titles.append('AFTER YOU')
list_titles.append('AFTER YOU\'VE GONE')
list_titles.append('AGAIN')
list_titles.append('AGUA DE BEBER')
list_titles.append('AIN\'T MISBEHAVIN\'')
list_titles.append('AIN\'T SHE SWEET')
list_titles.append('AIREGIN')
list_titles.append('AIRMAIL SPECIAL')
list_titles.append('AISHA')
list_titles.append('ALEXANDER\'S RAGTIME BAND')
list_titles.append('ALFIE')
list_titles.append('ALFIE\'S THEME')
list_titles.append('ALICE IN WONDERLAND')
list_titles.append('ALL ABOUT RONNIE')
list_titles.append('ALL ALONE')
list_titles.append('ALL BLUES')
list_titles.append('ALL GODS CHILLUN GOT RHYTHM')
list_titles.append('ALL MY TOMORROWS')
list_titles.append('ALL OF A SUDDEN MY HEART SINGS')
list_titles.append('ALL OF ME')
list_titles.append('ALL OF YOU')
list_titles.append('ALL OR NOTHING AT ALL')
list_titles.append('ALL THE THINGS YOU ARE')
list_titles.append('ALL THE WAY')
list_titles.append('ALL THROUGH THE DAY')
list_titles.append('ALL THROUGH THE NIGHT')
list_titles.append('ALL TOO SOON')
list_titles.append('ALMOST LIKE BEING IN LOVE')
list_titles.append('ALONE TOGETHER')
list_titles.append('ALONE TOO LONG')
list_titles.append('ALONG CAME BETTY')
list_titles.append('ALWAYS')
list_titles.append('AM I BLUE')
list_titles.append('AMONG MY SOUVENIRS')
list_titles.append('AMOR')
list_titles.append('ANA MARIA')
list_titles.append('AND ON THE THIRD DAY')
list_titles.append('AND THE ANGELS SING')
list_titles.append('ANGELEYES')
list_titles.append('ANTHROPOLOGY')
list_titles.append('ANYTHING GOES')
list_titles.append('APRIL IN PARIS')
list_titles.append('APRIL JOY')
list_titles.append('AREN\'T YOU GLAD YOU\'RE YOU')
list_titles.append('ARMANDO\'S RHUMBA')
list_titles.append('ASK ME NOW')
list_titles.append('AS LONG AS I LIVE')
list_titles.append('AS TIME GOES BY')
list_titles.append('AT LAST')
list_titles.append('AT LONG LAST LOVE')
list_titles.append('AUTUMN IN NEW YORK')
list_titles.append('AUTUMN LEAVES')
list_titles.append('AVALON')
list_titles.append('BACKSTAGE SALLY')
list_titles.append('BAG\'S GROOVE')
list_titles.append('BALLAD')
list_titles.append('BALLADE')
list_titles.append('BALTIMORE ORIOLE')
list_titles.append('BA-LUE BOLIVAR BA-LUES-ARE')
list_titles.append('BARBADOS')
list_titles.append('BARK FOR BARKSDALE')
list_titles.append('BASINSTREETBLUES')
list_titles.append('BAUBLES')
list_titles.append('BEATRICE')
list_titles.append('BEAUTIFUL FRIENDSHIP')
list_titles.append('BEAUTIFUL LOVE')
list_titles.append('BEAUTY AND THE BEAST')
list_titles.append('BE-BOP')
list_titles.append('BECAREFUL IT\'S MY HEART')
list_titles.append('BEGIN THE BEGUINE')
list_titles.append('BE IN GREEN')
list_titles.append('BEMSHA SWING')
list_titles.append('BE MY LOVE')
list_titles.append('BENNY\'S TUNE')
list_titles.append('BERNIE\'S TUNE')
list_titles.append('BESAME MUCHO')
list_titles.append('BESSIE\'S BLUES')
list_titles.append('BESS YOU IS MY WOMAN')
list_titles.append('BEST IS YET TO COME')
list_titles.append('BEST THING FOR YOU IS ME')
list_titles.append('BEST THINGS IN LIFE ARE FREE')
list_titles.append('BETTER THAN ANY THING')
list_titles.append('BETWEEN THE DEVIL AND THE DEEP BLUE SEA')
list_titles.append('BEWITCHED')
list_titles.append('BEYOND THE BLUE HORIZON')
list_titles.append('BEYOND THE SEA')
list_titles.append('BID IN MY TIME')
list_titles.append('BILL BAILEY')
list_titles.append('BILLIE\'S BOUNCE')
list_titles.append('BILLY BOY')
list_titles.append('BIRKS WORKS')
list_titles.append('BIRTH OF THE BLUES')
list_titles.append('BLACK AND BLUE')
list_titles.append('BLACKBERRY WINTER')
list_titles.append('BLACK COFFEE')
list_titles.append('BLACK NARCISSUS')
list_titles.append('BLACK NILE')
list_titles.append('BLAME IT ON MY YOUTH')
list_titles.append('BLOOM')
list_titles.append('BLOOMDIDO')
list_titles.append('BLOSSOM FELL')
list_titles.append('BLUE')
list_titles.append('BLUE AND SENTIMENTAL')
list_titles.append('BLUEBERRY HILL')
list_titles.append('BLUE BOSSA')
list_titles.append('BLUE CHAMPAGNE')
list_titles.append('BLUE DANIEL')
list_titles.append('BLUE IN GREEN')
list_titles.append('BLUE LOU')
list_titles.append('BLUE MOON')
list_titles.append('BLUE ROOM')
list_titles.append('BLUESETTE')
list_titles.append('BLUES FIVE SPOT')
list_titles.append('BLUES FOR ALICE')
list_titles.append('BLUES FOR WOOD')
list_titles.append('BLUES IN THE CLOSET')
list_titles.append('BLUES IN THE NIGHT')
list_titles.append('BLUESKIES')
list_titles.append('BLUES MARCH')
list_titles.append('BLUE SPHERE')
list_titles.append('BLUE TURNING GREY OVER YOU')
list_titles.append('BODY AND SOUL')
list_titles.append('BOHEMIA AFTER DARK')
list_titles.append('BOLIVIA')
list_titles.append('BOO BOO\'S BIRTHDAY')
list_titles.append('BOOKER\'S WALTZ')
list_titles.append('BOPLICITY')
list_titles.append('BORN TO BE BLUE')
list_titles.append('BOSSA ANTIGUA')
list_titles.append('BOUNCIN\' WITH BUD')
list_titles.append('BOURBON STREET PARADE')
list_titles.append('BOY NEXT DOOR')
list_titles.append('BRAZIL')
list_titles.append('BRAZILIAN LIKE')
list_titles.append('BRAZILIAN SUITE')
list_titles.append('BREEZE AND I')
list_titles.append('BRIGHT BOY')
list_titles.append('BRIGHT MISSISSIPPI')
list_titles.append('BRIGHT SIZE LIFE')
list_titles.append('BRILLIANT CORNERS')
list_titles.append('BROADWAY')
list_titles.append('BROTHERHOODOFMAN')
list_titles.append('BUDO')
list_titles.append('BUD POWELL')
list_titles.append('BUNKO')
list_titles.append('BUT BEAUTIFUL')
list_titles.append('BUTCH AND BUTCH')
list_titles.append('BUT NOT FOR ME')
list_titles.append('BUTTERFLY')
list_titles.append('BUTTERFLY DREAMS')
list_titles.append('BYE BYE BABY')
list_titles.append('BYE BYE BLACKBIRD')
list_titles.append('BYE BYE BLUES')
list_titles.append('BYE-YA')
list_titles.append('BY MYSELF')
list_titles.append('CALL ME')
list_titles.append('CALL ME IRRESPONSIBLE')
list_titles.append('CANDY')
list_titles.append('CANTALOUPE ISLAND')
list_titles.append('CAN\'T HELP LOVIN\' DAT MAN')
list_titles.append('CAPTAIN MARVEL')
list_titles.append('CARAVAN')
list_titles.append('CELIA')
list_titles.append('CENTRAL PARK WEST')
list_titles.append('CEORA')
list_titles.append('CERTAIN SMILE')
list_titles.append('C\'EST SI BON')
list_titles.append('CHANGE PARTNERS')
list_titles.append('CHARLESTON')
list_titles.append('CHASIN\' THE TRANE')
list_titles.append('CHEEK TO CHEEK')
list_titles.append('CHEESE CAKE')
list_titles.append('CHEETAH')
list_titles.append('CHEGA DE SAUDADE')
list_titles.append('CHELSEA BRIDGE')
list_titles.append('CHEROKEE')
list_titles.append('CHERYL')
list_titles.append('CHICAGO')
list_titles.append('CHICKEN')
list_titles.append('CHILD IS BORN')
list_titles.append('CJAMBLUES')
list_titles.append('CLOSE ENOUGH FOR LOVE')
list_titles.append('COME FLY WITH ME')
list_titles.append('COME RAIN OR COME SHINE')
list_titles.append('COMES LOVE')
list_titles.append('COME SUNDAY')
list_titles.append('CON ALMA')
list_titles.append('CONCEPTION')
list_titles.append('CONFERENCE OF THE BIRDS')
list_titles.append('CONFESSIN\'')
list_titles.append('CONFIRMATION')
list_titles.append('CONTEMPLATION')
list_titles.append('CONTINUUM')
list_titles.append('COOL ONE')
list_titles.append('COPENHAGEN')
list_titles.append('CORAL')
list_titles.append('CORCOVADO')
list_titles.append('COTTAGE FOR SALE')
list_titles.append('COTTONTAIL')
list_titles.append('COULD IT BE YOU')
list_titles.append('COUNTDOWN')
list_titles.append('COUNTRY')
list_titles.append('COUSIN MARY')
list_titles.append('CRAZY HE CALLS ME')
list_titles.append('CRAZY RHYTHM')
list_titles.append('CREOLELOVECALL')
list_titles.append('CREPUSCULE WITH NELLIE')
list_titles.append('CRISIS')
list_titles.append('CRISS CROSS')
list_titles.append('CROSS CURRENT')
list_titles.append('CRY ME A RIVER')
list_titles.append('CRYSTALSILENCE')
list_titles.append('CTA')
list_titles.append('CUTE')
list_titles.append('CYCLIC EPISODE')
list_titles.append('DAAHOUD')
list_titles.append('DANCE OF THE INFIDELS')
list_titles.append('DANCINGI N THE DARK')
list_titles.append('DANCING ON THE CEILING')
list_titles.append('DARN THAT DREAM')
list_titles.append('DAT DERE')
list_titles.append('DAY BREAK')
list_titles.append('DAY BY DAY')
list_titles.append('DAY DREAM')
list_titles.append('DAY DREAMING')
list_titles.append('DAY IN')
list_titles.append('DAYS AND NIGHTS WAITING')
list_titles.append('DAYS OF WINE AND ROSES')
list_titles.append('DEAR LORD')
list_titles.append('DEARLY BE LOVED')
list_titles.append('DEAR OLD STOCKHOLM')
list_titles.append('DEDICATED TO YOU')
list_titles.append('DEED\' I DO')
list_titles.append('DEEP PURPLE')
list_titles.append('DELSASSER')
list_titles.append('DELUGE')
list_titles.append('DESAFINADO')
list_titles.append('DETOUR AHEAD')
list_titles.append('DEVIL MAY CARE')
list_titles.append('DEWEY SQUARE')
list_titles.append('DEXTERITY')
list_titles.append('DIENDA')
list_titles.append('DIG')
list_titles.append('DINAH')
list_titles.append('DINDI')
list_titles.append('DJANGO')
list_titles.append('DOLORES')
list_titles.append('DOLPHIN')
list_titles.append('DOLPHIN DANCE')
list_titles.append('DONNA LEE')
list_titles.append('DO NOTHING TIL YOU HEAR FROM ME')
list_titles.append('DON\'T BE THAT WAY')
list_titles.append('DON\'T BLAME ME')
list_titles.append('DON\'T EXPLAIN')
list_titles.append('DON\'T GET AROUND MUCH ANY MORE')
list_titles.append('DON\'T GO TO STRANGERS')
list_titles.append('DON\'T KNOW WHY')
list_titles.append('DON\'T MISUNDERSTAND')
list_titles.append('DON\'T TAKE YOUR LOVE FROM ME')
list_titles.append('DON\'T WORRY \'BOUT ME')
list_titles.append('DOWN BY THE RIVERSIDE')
list_titles.append('DOWN IN THE DEPTHS')
list_titles.append('DOXY')
list_titles.append('DO YOU KNOW WHAT IT MEANS')
list_titles.append('DREAM A LITTLE DREAM OF ME')
list_titles.append('DREAM DANCING')
list_titles.append('DREAMSVILLE')
list_titles.append('DRIFTIN\'')
list_titles.append('EARLY AUTUMN')
list_titles.append('EAST OF THE SUN')
list_titles.append('EASY LIVING')
list_titles.append('EASY STREET')
list_titles.append('EASY TO LOVE')
list_titles.append('EIDER DOWN')
list_titles.append('EIGHTY ONE')
list_titles.append('ELCAJON')
list_titles.append('EL GAUCHO')
list_titles.append('ELORA')
list_titles.append('EMBRACEABLE YOU')
list_titles.append('EMILY')
list_titles.append('END OF A LOVE AFFAIR')
list_titles.append('EPISTROPHY')
list_titles.append('EQUINOX')
list_titles.append('ERONEL')
list_titles.append('ESP')
list_titles.append('ESTATE')
list_titles.append('ETERNAL TRIANGLE')
list_titles.append('EVERYBODY\'S SONG BUT MY OWN')
list_titles.append('EVERYTHING HAPPENS TO ME')
list_titles.append('EVERYTHING I HAVE IS YOURS')
list_titles.append('EVERYTHING I LOVE')
list_titles.append('EVERYTHING I\'VE GOT BELONGS TO YOU')
list_titles.append('EVIDENCE')
list_titles.append('EVERYTIME WE SAY GOODBYE')
list_titles.append('EXACTLY LIKE YOU')
list_titles.append('FALL')
list_titles.append('FALLING GRACE')
list_titles.append('FALLING IN LOVE AGAIN')
list_titles.append('FALLING IN LOVE WITH LOVE')
list_titles.append('FANTASYIND')
list_titles.append('FASCINATING RHYTHM')
list_titles.append('FASCINATION')
list_titles.append('FAVELA')
list_titles.append('FEE-FI-FO-FUM')
list_titles.append('FEEL LIKE MAKIN\' LOVE')
list_titles.append('FEELS SO GOOD')
list_titles.append('FEVER')
list_titles.append('FINE AND DANDY')
list_titles.append('FINE AND MELLOW')
list_titles.append('FINE ROMANCE')
list_titles.append('FIVE BROTHERS')
list_titles.append('FLAMINGO')
list_titles.append('FLINTSTONES')
list_titles.append('FLOWER IS A LOVE SOMETHING')
list_titles.append('FLYING HOME')
list_titles.append('FLY ME TO THE MOON')
list_titles.append('FOGGY DAY')
list_titles.append('FOLKS WHO LIVE ON THE HILL')
list_titles.append('FOOTPRINTS')
list_titles.append('FOR ALL WE KNOW')
list_titles.append('FOREST FLOWER')
list_titles.append('FOREVER SONNY')
list_titles.append('FOR HEAVEN\'S SAKE')
list_titles.append('FOR JAN')
list_titles.append('FOR ONCE IN MY LIFE')
list_titles.append('FOR SENTIMENTAL REASONS')
list_titles.append('FOR YOU')
list_titles.append('FOUR')
list_titles.append('FOUR BROTHERS')
list_titles.append('FOUR IN ONE')
list_titles.append('FOUR ON SIX')
list_titles.append('FRECKLE FACE')
list_titles.append('FREDDIE THE FREELOADER')
list_titles.append('FREIGHT TRAIN')
list_titles.append('FRENESI')
list_titles.append('FRIDAY THE 13TH')
list_titles.append('FRIM FRAM SAUCE')
list_titles.append('FROM THIS MOMENT ON')
list_titles.append('FULL HOUSE')
list_titles.append('FUNKALLERO')
list_titles.append('FUNK IN DEEP FREEZE')
list_titles.append('GARY\'S NOTEBOOK')
list_titles.append('GEE BABY')
list_titles.append('GENTLE RAIN')
list_titles.append('GEORGIA ON MY MIND')
list_titles.append('GET HAPPY')
list_titles.append('GET ME TO THE CHURCH ON TIME')
list_titles.append('GET OUT OF TOWN')
list_titles.append('GHOST OF A CHANCE')
list_titles.append('GIANT STEPS')
list_titles.append('GIRL FROM IPANEMA')
list_titles.append('GIRL TALK')
list_titles.append('GIVE ME THE SIMPLE LIFE')
list_titles.append('GLAD TO BE UNHAPPY')
list_titles.append('GLORIA\'S STEP')
list_titles.append('GLORY OF LOVE')
list_titles.append('GOD BLESS THE CHILD')
list_titles.append('GOD CHILD')
list_titles.append('GOLDEN EARRING')
list_titles.append('GONEWITHTHEWIND')
list_titles.append('GOOD BAIT')
list_titles.append('GOODBYE')
list_titles.append('GOODBYE PORKPIE HAT')
list_titles.append('GOOD LIFE')
list_titles.append('GOOD MORNING HEARTACHE')
list_titles.append('GOT A MATCH')
list_titles.append('GRAND CENTRAL')
list_titles.append('GRAVY WALTZ')
list_titles.append('GREEN CHIMNEYS')
list_titles.append('GREGORY IS HERE')
list_titles.append('GROOVIN\' HIGH')
list_titles.append('HACKENSACK')
list_titles.append('HALF NELSON')
list_titles.append('HALLUCINATIONS')
list_titles.append('HAPPY LITTLE SUNBEAM')
list_titles.append('HAUNTEDHEART')
list_titles.append('HAVE YOU MET MISS JONES')
list_titles.append('HEART AND SOUL')
list_titles.append('HEAT WAVE')
list_titles.append('HELLO DOLLY')
list_titles.append('HELLO YOUNG LOVERS')
list_titles.append('HERE\'S THAT RAINY DAY')
list_titles.append('HERE\'S TO LIFE')
list_titles.append('HE\'S A TRAMP')
list_titles.append('HEYOKE')
list_titles.append('HIGH FLY')
list_titles.append('HIGH HOPES')
list_titles.append('HOME COMING')
list_titles.append('HOME COOKIN\'')
list_titles.append('HONEYSUCKLE ROSE')
list_titles.append('HOT HOUSE')
list_titles.append('HOUSE OF JADE')
list_titles.append('HOW ABOUT YOU')
list_titles.append('HOW ARE THINGS IN GLOCCAMORRA')
list_titles.append('HOW DEEP IS THE OCEAN')
list_titles.append('HOW HIGH THE MOON')
list_titles.append('HOW INSENSITIVE')
list_titles.append('HOW LONG HAS THIS BEEN GOING ON')
list_titles.append('HOW MY HEART SINGS')
list_titles.append('HUMPTY DUMPTY')
list_titles.append('HUNGARIA')
list_titles.append('I AIN\'T GOT NOBODY')
list_titles.append('I BELIEVE IN YOU')
list_titles.append('I CAN\'T BELIEVE YOU\'RE IN LOVE')
list_titles.append('I CAN\'T GET STARTED')
list_titles.append('I CAN\'T GIVE YOU ANYTHING BUT LOVE')
list_titles.append('I CONCENTRATE ON YOU')
list_titles.append('I COULD HAVE DANCED ALL NIGHT')
list_titles.append('I COULD WRITE A BOOK')
list_titles.append('I COVER THE WATERFRONT')
list_titles.append('I CRIED FOR YOU')
list_titles.append('I DID\'NT KNOW ABOUT YOU')
list_titles.append('I DID\'NT KNOW WHAT TIME IT WAS')
list_titles.append('IDLE MOMENTS')
list_titles.append('I DON\'T KNOW ENOUGH ABOUT YOU')
list_titles.append('I DON\'T STAND A GHOST OF A CHANCE')
list_titles.append('I DON\'T WANT TO MISS MISSISSIPPI')
list_titles.append('I FALL IN LOVE TOO EASILY')
list_titles.append('I FEVER I WOULD LEAVE YOU')
list_titles.append('IF I COULD BE WITH YOU')
list_titles.append('IF I DIDN\'T CARE')
list_titles.append('IF I HAD YOU')
list_titles.append('IF I LOVED YOU')
list_titles.append('IF I SHOULD LOSE YOU')
list_titles.append('IF I WERE A BELL')
list_titles.append('IF THERE IS SOMEONE LOVELIER')
list_titles.append('IF YOU COULD SEE ME NOW')
list_titles.append('IF YOU EVER SHOULD LEAVE')
list_titles.append('IF YOU NEVER COME TOME')
list_titles.append('I GET A KICKOUT OF YOU')
list_titles.append('I GET ALONG WITHOUT YOU')
list_titles.append('I GOT IT BAD')
list_titles.append('I GOT RHYTHM')
list_titles.append('I GOTTA RIGHT TO SING THE BLUES')
list_titles.append('I GOT THE SUN IN THE MORNING')
list_titles.append('I GUESS I\'LL HANG MY TEARS OUT TO DRY')
list_titles.append('I HAD\'NT ANYONE TILL YOU')
list_titles.append('I HEAR A RHAPSODY')
list_titles.append('I HEAR MUSIC')
list_titles.append('I LEFT MY HEART IN SAN FRANCISCO')
list_titles.append('I LET A SONG GO OUT OF MY HEART')
list_titles.append('I LIKE THE LIKES OF YOU')
list_titles.append('I\'LL BE AROUND')
list_titles.append('I\'LL BE SEEING YOU')
list_titles.append('I\'LL CLOSE MY EYES')
list_titles.append('I\'LL GET BY')
list_titles.append('I\'LL NEVER BE THE SAME')
list_titles.append('I\'LL REMEMBER APRIL')
list_titles.append('I\'LL SEE YOU IN MY DREAMS')
list_titles.append('I\'LL TAKE ROMANCE')
list_titles.append('I\'LL WIND')
list_titles.append('I LOVE PARIS')
list_titles.append('I LOVES YOU PORGY')
list_titles.append('I LOVE YOU')
list_titles.append('I\'M A FOOL TO WANT YOU')
list_titles.append('IMAGINATION')
list_titles.append('I\'M ALL SMILES')
list_titles.append('I\'M ALWAYS CHASIN\' GRAIN BOWS')
list_titles.append('I MAYBE WRONG')
list_titles.append('I\'M BEGINNING TO SEE THE LIGHT')
list_titles.append('I MEAN YOU')
list_titles.append('I\'M GETTING SENTIMENTAL OVER YOU')
list_titles.append('I\'M GLAD THERE IS YOU')
list_titles.append('I\'M GONNA SIT RIGHT DOWN AND WRITE MY SELF A LETTER')
list_titles.append('I\'M IN THE MOOD FOR LOVE')
list_titles.append('I\'M JUST A LUCKY SO-AND-SO')
list_titles.append('I\'M OLD FASHIONED')
list_titles.append('IMPRESSIONS')
list_titles.append('I\'M PUTTING ALL MY EGGS IN ONE BASKET')
list_titles.append('I\'M SITTING ON TOP OF THE WORLD')
list_titles.append('I\'M THROUGH WITH LOVE')
list_titles.append('IN A LITTLE SPANISH TOWN')
list_titles.append('IN A MELLOW TONE')
list_titles.append('IN A SENTIMENTAL MOOD')
list_titles.append('IN A SHANTY IN OLD SHANTY TOWN')
list_titles.append('INDIANA')
list_titles.append('INDIAN SUMMER')
list_titles.append('INFANT EYES')
list_titles.append('IN LOVE IN VAIN')
list_titles.append('INNER URGE')
list_titles.append('INTERPLAY')
list_titles.append('IN THE COOL')
list_titles.append('IN THE STILL OF THE NIGHT')
list_titles.append('IN THE WEE SMALL HOURS OF THE MORNING')
list_titles.append('INVITATION')
list_titles.append('IN WALKED BUD')
list_titles.append('I ONLY HAVE EYES FOR YOU')
list_titles.append('I REMEMBER CLIFFORD')
list_titles.append('I REMEMBER YOU')
list_titles.append('IRIS')
list_titles.append('IRRESISTABLE YOU')
list_titles.append('I SAY A LITTLE PRAYER FOR YOU')
list_titles.append('I SEE YOUR FACE BEFORE ME')
list_titles.append('ISFAHAN')
list_titles.append('I SHOULD CARE')
list_titles.append('I\'SNT IT A PITY')
list_titles.append('ISN\'T IT ROMANTIC')
list_titles.append('ISN\'T THIS A LOVELY DAY')
list_titles.append('ISOTOPE')
list_titles.append('ISRAEL')
list_titles.append('I SURRENDER DEAR')
list_titles.append('IS YOU IS OR IS YOU AIN\'T')
list_titles.append('IT AIN\'T NECESSARILY SO')
list_titles.append('IT COULD HAPPEN TO YOU')
list_titles.append('IT DON\'T MEAN A THING')
list_titles.append('IT HAD TO BE YOU')
list_titles.append('I THOUGHT ABOUT YOU')
list_titles.append('IT MIGHT AS WELL BE SPRING')
list_titles.append('IT NEVER ENTERED MY MIND')
list_titles.append('IT ONLY HAPPENS WHEN I DANCE WITH YOU')
list_titles.append('IT\'S A BIG WIDE WONDERFUL WORLD')
list_titles.append('IT\'S A BLUE WORLD')
list_titles.append('IT\'S A DANCE')
list_titles.append('IT\'S A GOOD DAY')
list_titles.append('IT\'S ALL RIGHT WITH ME')
list_titles.append('IT\'S A LOVELY DAY TO DAY')
list_titles.append('IT\'S BEEN A LONG LONG TIME')
list_titles.append('IT\'S DE-LOVELY')
list_titles.append('IT\'S EASY TO REMEMBER')
list_titles.append('IT\'S IMPOSSIBLE')
list_titles.append('IT\'S MAGIC')
list_titles.append('IT\'S ONLY A PAPER MOON')
list_titles.append('IT\'S THE TALK OF THE TOWN')
list_titles.append('IT\'S YOU OR NO ONE')
list_titles.append('I USED TO BE COLOR BLIND')
list_titles.append('I\'VE FOUND A NEW BABY')
list_titles.append('I\'VE FOUND A NEW BABY (2)')
list_titles.append('I\'VE GOT A CRUSH ON YOU')
list_titles.append('I\'VE GOT MY LOVE TO KEEP ME WARM')
list_titles.append('I\'VE GOT THE WORLD ON A STRING')
list_titles.append('I\'VE GOT YOU UNDER MY SKIN')
list_titles.append('I\'VE GROWN ACCUSTOMED TO HER FACE')
list_titles.append('I\'VE HEARD THAT SONG BEFORE')
list_titles.append('I\'VE NEVER BEEN IN LOVE BEFORE')
list_titles.append('I\'VE TOLD EVERY LITTLE STAR')
list_titles.append('I WANT TO BE HAPPY')
list_titles.append('I WANT TO TALK ABOUT YOU')
list_titles.append('I WAS DOING ALL RIGHT')
list_titles.append('I WILL WAIT FOR YOU')
list_titles.append('I WISH I KNEW')
list_titles.append('I WISH I KNEW HOW IT WOULD FEEL TO BE FREE')
list_titles.append('I WISH I WERE IN LOVE AGAIN')
list_titles.append('I WISH YOU LOVE')
list_titles.append('I WON\'T DANCE')
list_titles.append('JACKIE-ING')
list_titles.append('JACO')
list_titles.append('JAMES')
list_titles.append('JEANNIE\'S SONG')
list_titles.append('JEANNINE')
list_titles.append('JEEPERS CREEPERS')
list_titles.append('JERSEY BOUNCE')
list_titles.append('JINRIKISHA')
list_titles.append('JITTERBUG WALTZ')
list_titles.append('JODY GRIND')
list_titles.append('JOKER')
list_titles.append('JORDU')
list_titles.append('JOSHUA')
list_titles.append('JOY SPRING')
list_titles.append('JUJU')
list_titles.append('JUMPIN WITH SYMPHONY SID')
list_titles.append('JUST A GIGOLO')
list_titles.append('JUST FRIENDS')
list_titles.append('JUST IN TIME')
list_titles.append('JUST IN TUNE')
list_titles.append('JUST ONE MORE CHANCE')
list_titles.append('JUST ONE OF THOSE THINGS')
list_titles.append('JUST SQUEEZE ME')
list_titles.append('JUST YOU')
list_titles.append('KEEP IN MYSELF FOR YOU')
list_titles.append('KICKER')
list_titles.append('KIDS ARE PRETTY PEOPLE')
list_titles.append('KILLER JOE')
list_titles.append('KISS TO BUILD A DREAM ON')
list_titles.append('KOKO')
list_titles.append('LADIES IN MERCEDES')
list_titles.append('LADY BIRD')
list_titles.append('LADY IS A TRAMP')
list_titles.append('LADY\'S IN LOVE WITHY OU')
list_titles.append('LAMENT')
list_titles.append('LAMP IS LOW')
list_titles.append('LAST NIGHT WHEN WE WE\'RE YOUNG')
list_titles.append('LAURA')
list_titles.append('LAURIE')
list_titles.append('LAZY AFTERNOON')
list_titles.append('LAZY BIRD')
list_titles.append('LAZY BONES')
list_titles.append('LAZY RIVER')
list_titles.append('LEAVING')
list_titles.append('LEILA')
list_titles.append('LENNIE\'S PENNIES')
list_titles.append('LET\'S CALL THE WHOLE THING OFF')
list_titles.append('LET\'S CALL THIS')
list_titles.append('LET\'S COOL ONE')
list_titles.append('LET\'S DO IT')
list_titles.append('LET\'S FACE THE MUSIC AND DANCE')
list_titles.append('LET\'S FALL IN LOVE')
list_titles.append('LET\'S GET AWAY FROM IT ALL')
list_titles.append('LET\'S GET LOST')
list_titles.append('LET THERE BE LOVE')
list_titles.append('LET THERE BE YOU')
list_titles.append('LIGHT BLUE')
list_titles.append('LIGIA')
list_titles.append('LIKE A LOVER')
list_titles.append('LIKE SOMEONE IN LOVE')
list_titles.append('LIKE SONNY')
list_titles.append('LIL\' DARLING')
list_titles.append('LIMEHOUSE BLUES')
list_titles.append('LINE FOR LYONS')
list_titles.append('LINGER A WHILE')
list_titles.append('LITHA')
list_titles.append('LITTLE BOAT')
list_titles.append('LITTLE B\'S POEM')
list_titles.append('LITTLE DANCER')
list_titles.append('LITTLE GIRL BLUE')
list_titles.append('LITTLE NILES')
list_titles.append('LITTLE PEACE IN C FOR YOU')
list_titles.append('LITTLE ROOTIE TOOTIE')
list_titles.append('LITTLE SUN FLOWER')
list_titles.append('LITTLE TEAR')
list_titles.append('LITTLE WALTZ')
list_titles.append('LITTLE WILLIE LEAPS')
list_titles.append('LIZA')
list_titles.append('LONE JACK')
list_titles.append('LONELY DREAMS')
list_titles.append('LONESOME ROAD')
list_titles.append('LONG AGO AND FAR AWAY')
list_titles.append('LONNIE\'S LAMENT')
list_titles.append('LOOK FOR THE SILVER LINING')
list_titles.append('LOOKING UP')
list_titles.append('LOOK OF LOVE')
list_titles.append('LOOK TO THE RAINBOW')
list_titles.append('LOOK TO THE SKY')
list_titles.append('LOOP')
list_titles.append('LOTUS BLOSSOM')
list_titles.append('LOVE FOR SALE')
list_titles.append('LOVE IS JUST AROUND THE CORNER')
list_titles.append('LOVELY WAY TO SPEND AN EVENING')
list_titles.append('LOVE ME OR LEAVE ME')
list_titles.append('LOVE NEST')
list_titles.append('LOVER')
list_titles.append('LOVER COME BACK TO ME')
list_titles.append('LOVER MAN')
list_titles.append('LOVE WALKED IN')
list_titles.append('LUCKY SOUTHERN')
list_titles.append('LULLABY IN RHYTHM')
list_titles.append('LULLABY OF BIRDLAND')
list_titles.append('LULLABY OF THE LEAVES')
list_titles.append('LUSH LIFE')
list_titles.append('LYRESTO')
list_titles.append('MAC THE KNIFE')
list_titles.append('MAHJONG')
list_titles.append('MAIDEN VOYAGE')
list_titles.append('MAKE SOMEONE HAPPY')
list_titles.append('MAKING WHOOPEE')
list_titles.append('MAMBO INN')
list_titles.append('MANHA DE CARNAVAL')
list_titles.append('MANHATTAN')
list_titles.append('MAN I LOVE')
list_titles.append('MANOIR DE MES REVES')
list_titles.append('MANTECA')
list_titles.append('MAN THAT GOT AWAY')
list_titles.append('MAS QUE NADA')
list_titles.append('MASQUERADE IS OVER')
list_titles.append('MAYBE I SHOULD CHANGE MY WAYS')
list_titles.append('MAZE')
list_titles.append('MC JOLT')
list_titles.append('MEANING OF THE BLUES')
list_titles.append('MEAN TO ME')
list_titles.append('MEDITATION')
list_titles.append('MEMORIES OF TOMORROW')
list_titles.append('MEMORIES OF YOU')
list_titles.append('MERCY MERCY MERCY')
list_titles.append('MIDNIGHT AT THE OASIS')
list_titles.append('MIDNIGHT MOOD')
list_titles.append('MIDNIGHT SUN')
list_titles.append('MILANO')
list_titles.append('MILES AHEAD')
list_titles.append('MILESTONES (NEW)')
list_titles.append('MILESTONES (OLD)')
list_titles.append('MIMI')
list_titles.append('MINOR MISHAP')
list_titles.append('MINOR MOOD')
list_titles.append('MINOR STRAIN')
list_titles.append('MIRROR')
list_titles.append('MISTERIOSO')
list_titles.append('MISTY')
list_titles.append('MIYAKO')
list_titles.append('MOANIN')
list_titles.append('MOMENT\'S NOTICE')
list_titles.append('MOMENTS TO REMEMBER')
list_titles.append('MONA LISA')
list_titles.append('MONK\'S DREAM')
list_titles.append('MONK\'S MOOD')
list_titles.append('MOOD INDIGO')
list_titles.append('MOON ALLEY')
list_titles.append('MOON AND SAND')
list_titles.append('MOONCHILD')
list_titles.append('MOONDANCE')
list_titles.append('MOONGLOW')
list_titles.append('MOONLIGHT BECOMES YOU')
list_titles.append('MOONLIGHT IN VERMONT')
list_titles.append('MOONLIGHT SAVING TIME')
list_titles.append('MOONLIGHT SERENADE')
list_titles.append('MOON RIVER')
list_titles.append('MOON TRANE')
list_titles.append('MORE I SEE YOU')
list_titles.append('MORE THAN YOU KNOW')
list_titles.append('MORGAN THE PIRATE')
list_titles.append('MORNING')
list_titles.append('MOTEN SWING')
list_titles.append('MOUNTAIN GREENERY')
list_titles.append('MOVE')
list_titles.append('MR PC')
list_titles.append('MY FAVORITE THINGS')
list_titles.append('MY FOOLISH HEART')
list_titles.append('MY FUNNY VALENTINE')
list_titles.append('MY HEART BELONGS TO DADDY')
list_titles.append('MY HEART STOOD STILL')
list_titles.append('MY IDEAL')
list_titles.append('MY LITTLE BROWN BOOK')
list_titles.append('MY LITTLE SUEDE SHOES')
list_titles.append('MY LUCKY STAR')
list_titles.append('MY MAN\'S GONE NOW')
list_titles.append('MY MELANCHOLY BABY')
list_titles.append('MY OLD FLAME')
list_titles.append('MY ONE AND ONLY LOVE')
list_titles.append('MY ROMANCE')
list_titles.append('MY SECRET LOVE')
list_titles.append('MY SHINING HOUR')
list_titles.append('MY SHIP')
list_titles.append('MY SONG')
list_titles.append('MY WAY')
list_titles.append('NAIMA')
list_titles.append('NANCY')
list_titles.append('NANDIS')
list_titles.append('NATURE BOY')
list_titles.append('NEARNESS OF YOU')
list_titles.append('NEFERTITI')
list_titles.append('NEVER LET ME GO')
list_titles.append('NEVERTHELESS')
list_titles.append('NEVER WILL I MARRY')
list_titles.append('NEW PICTURE')
list_titles.append('NEW YORK')
list_titles.append('NICA\'S DREAM')
list_titles.append('NICE \'N EASY')
list_titles.append('NICE WORK IF YOU CAN GET IT')
list_titles.append('NIGHT AND DAY')
list_titles.append('NIGHT DREAMER')
list_titles.append('NIGHT HAS A THOUSAND EYES')
list_titles.append('NIGHTINGALE SANG IN BERKELEYS QUARE')
list_titles.append('NIGHT IN TUNISIA')
list_titles.append('NIGHT WE CALLED IT A DAY')
list_titles.append('NOBODY ELSE BUT ME')
list_titles.append('NO MOON AT ALL')
list_titles.append('NO SPLICE')
list_titles.append('NOSTALGIA IN TIMES SQUARE')
list_titles.append('NOTHING PERSONAL')
list_titles.append('NOW\'S THE TIME')
list_titles.append('NUAGES')
list_titles.append('NUTTY')
list_titles.append('NUTVILLE')
list_titles.append('ODD COUPLE')
list_titles.append('OFF MINOR')
list_titles.append('O GRANDE AMOR')
list_titles.append('OH LADY BE GOOD')
list_titles.append('OH LOOK AT ME NOW')
list_titles.append('OH WHAT A BEAUTIFUL MORNIN\'')
list_titles.append('OLD CAPE COD')
list_titles.append('OLD COUNTRY')
list_titles.append('OLD DEVIL MOON')
list_titles.append('OLD FOLKS')
list_titles.append('OLILOQUI VALLEY')
list_titles.append('OL\' MAN RIVER')
list_titles.append('ON A CLEAR DAY')
list_titles.append('ON A SLOW BOAT TO CHINA')
list_titles.append('ON BROADWAY')
list_titles.append('ONCE I LOVED')
list_titles.append('ONCE IN A WHILE')
list_titles.append('ONE BY ONE')
list_titles.append('ONE FINGER SNAP')
list_titles.append('ONE FOOT IN THE GUTTER')
list_titles.append('ONE FOR MY BABY')
list_titles.append('ONE I LOVE')
list_titles.append('ONE MORNING IN MAY')
list_titles.append('ONE NOTE SAMBA')
list_titles.append('ON GREEN DOLPHIN STREET')
list_titles.append('ONLY TRUST YOUR HEART')
list_titles.append('ON THE STREET WHERE YOU LIVE')
list_titles.append('ON THE SUNNY SIDE OF THE STREET')
list_titles.append('ON THE TRAIL')
list_titles.append('OPENER')
list_titles.append('ORNITHOLOGY')
list_titles.append('OUR LOVE IS HERE TO STAY')
list_titles.append('OUT OF NOWHERE')
list_titles.append('OUT OF THIS WORLD')
list_titles.append('OVER THE RAINBOW')
list_titles.append('PANNONICA')
list_titles.append('PAPER DOLL')
list_titles.append('PARISIAN THOROUGHFARE')
list_titles.append('PARKER\'S MOOD')
list_titles.append('PARTY\'S OVER')
list_titles.append('PASSION DANCE')
list_titles.append('PASSION FLOWER')
list_titles.append('PASSPORT')
list_titles.append('PEACE')
list_titles.append('PEEL ME A GRAPE')
list_titles.append('PEE WEE')
list_titles.append('PENNIE\'S FROM HEAVEN')
list_titles.append('PENSATIVA')
list_titles.append('PENTHOUSE SERENADE')
list_titles.append('PENTUP HOUSE')
list_titles.append('PEOPLE')
list_titles.append('PEOPLE WILL SAY WERE IN LOVE')
list_titles.append('PERDIDO')
list_titles.append('PERHAPS')
list_titles.append('PERHAPS PERHAPS PERHAPS')
list_titles.append('PERI\'S SCOPE')
list_titles.append('PETITE FLEUR')
list_titles.append('PHASE DANCE')
list_titles.append('PICK YOURSELF UP')
list_titles.append('PING PONG')
list_titles.append('PINOCCHIO')
list_titles.append('PLAYED TWICE')
list_titles.append('POINCIANA')
list_titles.append('POLKADOTS AND MOONBEAMS')
list_titles.append('POOR BUTTERFLY')
list_titles.append('POPSICLE TOES')
list_titles.append('PORTRAIT OF JENNIE')
list_titles.append('PREACHER')
list_titles.append('PRELUDE TO A KISS')
list_titles.append('PRETEND')
list_titles.append('PRETTY GIRL IS LIKE A MELODY')
list_titles.append('PRISM')
list_titles.append('PS I LOVE YOU')
list_titles.append('PUT ON A HAPPY FACE')
list_titles.append('QUASIMODO BLOWING CHANGES')
list_titles.append('QUASIMODO THEME')
list_titles.append('QUESTAR')
list_titles.append('QUESTION AND ANSWER')
list_titles.append('QUIET NOW')
list_titles.append('RADIO')
list_titles.append('RAINBOW CONNECTION')
list_titles.append('RAINCHECK')
list_titles.append('RECADO BOSSA NOVA')
list_titles.append('RECORDAME')
list_titles.append('RED CLAY')
list_titles.append('RED TOP')
list_titles.append('REFLECTIONS')
list_titles.append('RELAXIN\' AT CAMARILLO')
list_titles.append('REMEMBER')
list_titles.append('RE: PERSON I KNEW')
list_titles.append('RHYTHM-A-NING')
list_titles.append('ROAD SONG')
list_titles.append('ROBBIN\'S NEST')
list_titles.append('ROCKIN\' CHAIR')
list_titles.append('ROSE ROOM')
list_titles.append('ROSETTA')
list_titles.append('ROUND MIDNIGHT')
list_titles.append('ROUTE 66')
list_titles.append('RUBY MY DEAR')
list_titles.append('SAGA OF HARRISON CRABFEATHERS')
list_titles.append('SAIL AWAY')
list_titles.append('SAMBA DE ORFEU')
list_titles.append('SANDU')
list_titles.append('SAN FRANCISCO HOLIDAY')
list_titles.append('SATELLITE')
list_titles.append('SATIN DOLL')
list_titles.append('SAVE YOUR LOVE FOR ME')
list_titles.append('SAY IT')
list_titles.append('SCENE')
list_titles.append('SCOTCH AND SODA')
list_titles.append('SCRAPPLE FROM THE APPLE')
list_titles.append('SEA JOURNEY')
list_titles.append('SECOND STAR TO THE RIGHT')
list_titles.append('SECOND TIME AROUND')
list_titles.append('SECRET LOVE')
list_titles.append('SEGMENT')
list_titles.append('SENTIMENTAL JOURNEY')
list_titles.append('SEPTEMBER IN THE RAIN')
list_titles.append('SEPTEMBER SONG')
list_titles.append('SERENADE TO A CUCKOO')
list_titles.append('SERENE')
list_titles.append('SERENITY')
list_titles.append('SEVEN COME ELEVEN')
list_titles.append('SEVEN STEPS TO HEAVEN')
list_titles.append('SHADOW OF YOUR SMILE')
list_titles.append('SHE\'S FUNNY THAT WAY')
list_titles.append('SHINE')
list_titles.append('SHINY STOCKINGS')
list_titles.append('SID\'S DELIGHT')
list_titles.append('SILVER\'S SERENADE')
list_titles.append('SIMONE')
list_titles.append('SINCE I FELL FOR YOU')
list_titles.append('SIPPIN\' AT BELLS')
list_titles.append('SISI')
list_titles.append('SISTER SADIE')
list_titles.append('SKATING IN CENTRAL PARK')
list_titles.append('SKIPPY')
list_titles.append('SKYLARK')
list_titles.append('SKYLINER')
list_titles.append('SLEEPIN\' BEE')
list_titles.append('SLIPPED DISC')
list_titles.append('SLOW HOT WIND')
list_titles.append('SMILE')
list_titles.append('SMOKE GETS IN YOUR EYES')
list_titles.append('SMOKE RINGS')
list_titles.append('SMOOTH ONE')
list_titles.append('SNO\' PEAS')
list_titles.append('SO DANCO SAMBA')
list_titles.append('SOFTLY AS IN A MORNING SUNRISE')
list_titles.append('SO IN LOVE')
list_titles.append('SOLAR')
list_titles.append('SOLITUDE')
list_titles.append('SO MANY STARS')
list_titles.append('SOMEBODY LOVES ME')
list_titles.append('SOMEDAY MY PRINCE WILL COME')
list_titles.append('SOMEDAY YOU\'LL BE SORRY')
list_titles.append('SOME ENCHANTED EVENING')
list_titles.append('SOMEONE TO WATCH OVER ME')
list_titles.append('SOME OTHER BLUES')
list_titles.append('SOME OTHER SPRING')
list_titles.append('SOME OTHER TIME')
list_titles.append('SOMETIME AGO')
list_titles.append('SOMETIMES I\'M HAPPY')
list_titles.append('SOMEWHERE')
list_titles.append('SONG FOR MY FATHER')
list_titles.append('SO NICE')
list_titles.append('SONNY MOON FOR TWO')
list_titles.append('SOON')
list_titles.append('SOPHISTICATED LADY')
list_titles.append('SORCERER')
list_titles.append('SOS')
list_titles.append('SO TENDER')
list_titles.append('SOUL EYES')
list_titles.append('SOUL TRANE')
list_titles.append('SOUND FOR SORE EARS')
list_titles.append('SOUVENIR')
list_titles.append('SO WHAT')
list_titles.append('SPAIN')
list_titles.append('SPEAK LIKE A CHILD')
list_titles.append('SPEAK LOW')
list_titles.append('SPEAK NO EVIL')
list_titles.append('S\'POSIN\'')
list_titles.append('SPRING CAN REALLY HANG YOU UP THE MOST')
list_titles.append('SPRING IS HERE')
list_titles.append('STABLEMATES')
list_titles.append('STAIRWAY TO THE STARS')
list_titles.append('STAR-CROSSED LOVERS')
list_titles.append('STARDUST')
list_titles.append('STAR EYES')
list_titles.append('STARS FELL ON ALABAMA')
list_titles.append('STELLA BY STARLIGHT')
list_titles.append('ST LOUIS BLUES')
list_titles.append('STOLEN MOMENTS')
list_titles.append('STOMPIN\' AT THE SAVOY')
list_titles.append('STORMY WEATHER')
list_titles.append('STRAIGHTEN UP AND FLY RIGHT')
list_titles.append('STRAIGHT NO CHASER')
list_titles.append('STRAIGHT STREET')
list_titles.append('STRANGERS IN THE NIGHT')
list_titles.append('STRAYHORN 2')
list_titles.append('STREETOFDREAMS')
list_titles.append('STRIKEUPTHEBAND')
list_titles.append('STRODERODE')
list_titles.append('STROLLIN')
list_titles.append('STRUTTIN\' WITH SOME BARBECUE')
list_titles.append('ST THOMAS')
list_titles.append('SUBCONSCIOUS LEE')
list_titles.append('SUDDENLY IT\'S SPRING')
list_titles.append('SUGAR')
list_titles.append('SUMMER BAND CAMP')
list_titles.append('SUMMER KNOWS')
list_titles.append('SUMMER SERENADE')
list_titles.append('SUMMERTIME')
list_titles.append('SUNDAY KIND OF LOVE')
list_titles.append('SUNDOWN')
list_titles.append('SUNNY')
list_titles.append('SURREY WITH THE FRINGE ON THE TOP')
list_titles.append('SWAY')
list_titles.append('SWEEPIN GUP')
list_titles.append('SWEET AND LOVELY')
list_titles.append('SWEETEST SOUNDS')
list_titles.append('SWEET GEORGIA BRIGHT')
list_titles.append('SWEET GEORGIA BROWN')
list_titles.append('SWEET LORRAINE')
list_titles.append('SWEET SUE')
list_titles.append('SWINGING SHEPHERD BLUES')
list_titles.append('S\'WONDERFUL')
list_titles.append('TAKE FIVE')
list_titles.append('TAKE THE A TRAIN')
list_titles.append('TAKING A CHANCE ON LOVE')
list_titles.append('TANGERINE')
list_titles.append('TASTE OF HONEY')
list_titles.append('TEACH ME TONIGHT')
list_titles.append('TEA FOR TWO')
list_titles.append('TELL ME A BEDTIME STORY')
list_titles.append('TEMPUS FUGIT')
list_titles.append('TENDERLY')
list_titles.append('TENOR MADNESS')
list_titles.append('THANKS FOR THE MEMORY')
list_titles.append('THAT OLD BLACK MAGIC')
list_titles.append('THAT OLD FEELING')
list_titles.append('THAT\'S ALL')
list_titles.append('THE BALANCE')
list_titles.append('THE DUKE')
list_titles.append('THELONIOUS')
list_titles.append('THEME')
list_titles.append('THEM THERE EYES')
list_titles.append('THE PEACOCKS')
list_titles.append('THERE IS NO GREATER LOVE')
list_titles.append('THERE\'LL BE SOME CHANGES MADE')
list_titles.append('THERE\'S A LULL IN MY LIFE')
list_titles.append('THERE\'S A SMALL HOTEL')
list_titles.append('THERE\'S NO YOU')
list_titles.append('THERE WILL NEVER BE ANOTHER YOU')
list_titles.append('THESE FOOLISH THINGS')
list_titles.append('THE SONG IS YOU')
list_titles.append('THE WAY YOU LOOK TONIGHT')
list_titles.append('THEY ALL LAUGHED')
list_titles.append('THEY CAN\'T TAKE THAT AWAY FROM ME')
list_titles.append('THEY DIDN\'T BELIEVE ME')
list_titles.append('THEY SAY')
list_titles.append('THEY SAY IT\'S WONDERFUL')
list_titles.append('THINGS AIN\'T WHAT THEY USED TO BE')
list_titles.append('THINGS WE DID LAST SUMMER')
list_titles.append('THINK OF ONE')
list_titles.append('THIS CAN\'T BE LOVE')
list_titles.append('THIS COULD BE THE START OF SOMETHING')
list_titles.append('THIS I DIG OF YOU')
list_titles.append('THIS IS ALL I ASK')
list_titles.append('THIS IS NEW')
list_titles.append('THIS MASQUERADE')
list_titles.append('THIS YEARS KISSES')
list_titles.append('THOU SWELL')
list_titles.append('THREE LITTLE WORDS')
list_titles.append('THRILL IS GONE')
list_titles.append('THRIVING FROM A RIFF')
list_titles.append('TILL THERE WAS YOU')
list_titles.append('TIME AFTER TIME')
list_titles.append('TIME FOR LOVE')
list_titles.append('TIME ON MY HANDS')
list_titles.append('TIME REMEMBERED')
list_titles.append('TIN TIN DEO')
list_titles.append('TINY CAPERS')
list_titles.append('TIS AUTUMN')
list_titles.append('TISKET A TASKET')
list_titles.append('TONES FOR JOAN\'S BONES')
list_titles.append('TONIGHT')
list_titles.append('TONIGHT YOU BELONG TO ME')
list_titles.append('TOO CLOSE FOR COMFORT')
list_titles.append('TOO MARVELOUS FOR WORDS')
list_titles.append('TOO YOUNG')
list_titles.append('TOO YOUNG TO GO STEADY')
list_titles.append('TOUCH OF YOUR LIPS')
list_titles.append('TOYS')
list_titles.append('TOY TUNE')
list_titles.append('TRAINING')
list_titles.append('TRICOTISM')
list_titles.append('TRINKLE TINKLE')
list_titles.append('TRISTE')
list_titles.append('TROUBLED WATERS')
list_titles.append('TRY A LITTLE TENDERNESS')
list_titles.append('TUNE UP')
list_titles.append('TURN AROUND')
list_titles.append('TURN OUT THE STARS')
list_titles.append('TWISTED BLUES')
list_titles.append('TWO FOR THE ROAD')
list_titles.append('UGLY BEAUTY')
list_titles.append('UNDECIDED')
list_titles.append('UNDER A BLANKET OF BLUE')
list_titles.append('UNFORGETTABLE')
list_titles.append('UNITED')
list_titles.append('UNIT SEVEN')
list_titles.append('UNREQUITED')
list_titles.append('UP JUMPED SPRING')
list_titles.append('UPPER MANHATTAN MEDICAL GROUP')
list_titles.append('VALSE HOT')
list_titles.append('VCHUCHO')
list_titles.append('VERY EARLY')
list_titles.append('VERY THOUGHT OF YOU')
list_titles.append('VIOLETS FOR YOUR FURS')
list_titles.append('VIRGO')
list_titles.append('VOYAGE')
list_titles.append('WALKIN')
list_titles.append('WALKIN MY BABY BACK HOME')
list_titles.append('WALKIN SHOES')
list_titles.append('WALKIN UP')
list_titles.append('WALK TALL')
list_titles.append('WALTZ FOR DEBBY')
list_titles.append('WARM VALLEY')
list_titles.append('WATCH WHAT HAPPENS')
list_titles.append('WATERMELON MAN')
list_titles.append('WAVE')
list_titles.append('WAYNE\'S THANG')
list_titles.append('WEAVER OF DREAMS')
list_titles.append('WEBB CITY')
list_titles.append('WELL BE TOGETHER AGAIN')
list_titles.append('WELL YOU NEEDN\'T')
list_titles.append('WENDY')
list_titles.append('WE SEE')
list_titles.append('WEST COAST BLUES')
list_titles.append('WE WILL MEET AGAIN')
list_titles.append('WHAT A DIFFERENCE A DAY MADE')
list_titles.append('WHAT A LITTLE MOONLIGHT CAN DO')
list_titles.append('WHAT ARE YOU DOING NEW YEARS')
list_titles.append('WHAT ARE YOU DOING THE REST OF YOUR LIFE')
list_titles.append('WHAT A WONDERFUL WORLD')
list_titles.append('WHAT IS THIS THING CALLED LOVE')
list_titles.append('WHAT\'LL I DO')
list_titles.append('WHAT\'S NEW')
list_titles.append('WHEN IT RAINS')
list_titles.append('WHEN IT\'S SLEEPY TIME DOWN SOUTH')
list_titles.append('WHEN LIGHTS ARE LOW')
list_titles.append('WHEN SUNNY GETS BLUE')
list_titles.append('WHEN THE SAINTS GO MARCHING IN')
list_titles.append('WHEN YOU\'RE SMILIN\'')
list_titles.append('WHEN YOU WISH UPON A STAR')
list_titles.append('WHERE OR WHEN')
list_titles.append('WHILE WE\'RE YOUNG')
list_titles.append('WHISPER NOT')
list_titles.append('WHO CAN I TURN TO')
list_titles.append('WHO\'S SORRY NOW')
list_titles.append('WHY DO I LOVE YOU')
list_titles.append('WHY DO\'NT YOU DO RIGHT')
list_titles.append('WILD FLOWER')
list_titles.append('WILLOW WEEP FOR ME')
list_titles.append('WILL YOU STILL BE MINE')
list_titles.append('WINDOWS')
list_titles.append('WITCH CRAFT')
list_titles.append('WITCH HUNT')
list_titles.append('WITH A SONG IN MY HEART')
list_titles.append('WITHOUT A SONG')
list_titles.append('WITH THE WIND AND THE RAIN IN HAIR')
list_titles.append('WIVES AND LOVERS')
list_titles.append('WONDERFUL DA YLIKE TO DAY')
list_titles.append('WOODY \'N YOU')
list_titles.append('WORK SONG')
list_titles.append('WOULDN\'T IT BE LOVERLY')
list_titles.append('WOW')
list_titles.append('WRAP YOUR TROUBLES IN DREAMS')
list_titles.append('YARDBIRD SUITE')
list_titles.append('YES AND NO')
list_titles.append('YESTERDAYS')
list_titles.append('YOU AND THE NIGHT AND THE MUSIC')
list_titles.append('YOU ARE TOO BEAUTIFUL')
list_titles.append('YOU BETTER GO NOW')
list_titles.append('YOU BROUGHT A NEW KIND OF LOVE')
list_titles.append('YOU CAN DEPEND ON ME')
list_titles.append('YOU\'D BE SO NICE TO COME HOME TO')
list_titles.append('YOU DON\'T KNOW WHAT LOVE IS')
list_titles.append('YOU DO SOMETHING TO ME')
list_titles.append('YOU GO TO MY HEAD')
list_titles.append('YOU KEEP COMING BACK LIKE A SONG')
list_titles.append('YOU MAKE ME FEEL SO YOUNG')
list_titles.append('YOU MUST BELIEVE IN SPRING')
list_titles.append('YOUNG AND FOOLISH')
list_titles.append('YOUNG AT HEART')
list_titles.append('YOU\'RE EVERYTHING')
list_titles.append('YOU\'RE LAUGHING AT ME')
list_titles.append('YOU\'RE MY EVERYTHING')
list_titles.append('YOU\'RE MY THRILL')
list_titles.append('YOU\'RE NOBODY TILL SOMEBODY LOVES YOU')
list_titles.append('YOU\'RE THE TOP')
list_titles.append('YOU STEPPED OUT OF A DREAM')
list_titles.append('YOU TOOK ADVANTAGE OF ME')
list_titles.append('YOU TURNED THE TABLES ON ME')
list_titles.append('YOU\'VE CHANGED')
list_titles.append('YOU WON\'T FORGET ME')
list_titles.append('ZINGARO')
list_titles.append('ZING WENT THE STRINGS OF MY HEART')
list_titles.append('ZOLTAN')

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

artist_list = [
'Aage Tanggaard',
'Aaron Bell',
'Aaron Goldberg (2)',
'Aaron J. Johnson',
'Aaron Juvelier',
'Aaron Kimmel',
'Aaron Parks',
'Aaron Sachs',
'Aaron Scott',
'Abby Hoffer',
'Abdou M\'Boup',
'Abdul Salaam',
'Abe Aaron',
'Abe Bolar',
'Abe Lincoln',
'Abe Luboff',
'Abe Nole',
'Abe Rosen',
'Abraham \'Boomie\' Richman',
'Abraham Burton',
'Abraham Hochstein',
'Abraham Laboriel',
'Ace Tesone',
'Ack Van Rooyen',
'Adalberto Santiago',
'Adam Brenner',
'Adam Makowicz',
'Adam Nussbaum',
'Adam Rogers (2)',
'Adam Rudolph',
'Addison Collins',
'Addison Farmer',
'Adele Girard',
'Adelhard Roidinger',
'Ado Broodboom',
'Adrian Acea',
'Adrian Guillery',
'Adrian Rollini',
'Afrika Bambaataa',
'A. G. Godley',
'A. Grace Lee Mims',
'Ahmad Jamal',
'Ahmed Abdullahi Gallab',
'Ahmed Abdul-Malik',
'Aimé Barelli',
'Airto Moreira',
'Åke Hasselgård',
'Åke Persson',
'Akira Daiyoshi',
'Akira Tana',
'Akua Dixon',
'Al Aarons',
'Aladár Pege',
'Alain Jean-Marie',
'Alain Romans',
'Alan Braufman',
'Alan Broadbent',
'Alan Dawson',
'Alan Estes',
'Alan Gauvin',
'Alan Hare',
'Alan Hawkshaw',
'Alan Jeffreys',
'Alan Jones (2)',
'Alan Kaplan',
'Alan Metcalfe',
'Alan Morrissey',
'Alan Raph',
'Alan Read (3)',
'Alan Reuss',
'Alan Robinson',
'Alan Rubin',
'Alan Shulman',
'Alan Simon (2)',
'Alan Skidmore',
'Al Anthony',
'Al Antonucci',
'Alan Vitouš',
'Alan Ware',
'Alan Weighall',
'Alan Weight',
'Alan Yankee',
'Al Avola',
'Al Bartee',
'Al Beldini',
'Al Belletto',
'Albert Ammons',
'Albert Ayler',
'Albert Dailey',
'Albert Hall (2)',
'Albert Harris',
'Albert Heath',
'Albert \'June\' Gardner',
'Albert King (2)',
'Albert Mangelsdorff',
'Albert Nicholas',
'Alberto Corvini',
'Alberto Mandarini',
'Alberto Socarras',
'Albert Pollan',
'Albert Richmond',
'Albert Sanz',
'Albert Saparoff',
'Albert Smith (8)',
'Albert Stinson',
'Albert Washington (2)',
'Albert Wynn',
'Al Block',
'Al Bryant',
'Al Burke',
'Alby Cullaz',
'Al Caiola',
'Al Casey',
'Al Cobbs',
'Al Cohn',
'Al Cooper',
'Al Costi',
'Al Craig',
'Al Davis (2)',
'Al Del Simone',
'Al De Risi',
'Al Di Meola',
'Al Donahue',
'Aldo Romano',
'Aldo Vigorito',
'Al Dreares',
'Alec Fila',
'Alejo Poveda',
'Al Epstein',
'Al Esposito (2)',
'Alessandro Tedesco',
'Alex Acuña',
'Alexander Courage',
'Alexander Koltun',
'Alexander Neiman',
'Alex Beller',
'Alex Blake (2)',
'Alex Caturegli',
'Alex Cirin	Jr.',
'Alex Cuozzo',
'Alex Deutsch',
'Alex Dmochowski',
'Alex Domschot',
'Alex Domschott',
'Alex Elin',
'Alex Foster',
'Alex Iles',
'Alexis Taylor',
'Alex Kallao',
'Alex Law',
'Alex Ligertwood',
'Alex Malempré',
'Alex Mitchell (4)',
'Alex Norris',
'Alex Pevsner',
'Alex Renard',
'Alex Riel',
'Alex Rodriguez',
'Alex Sipiagin',
'Alfa Šmíd',
'Al \'Fats\' Edwards',
'Alf Bamford',
'Alf Clausen',
'Alfie Evans',
'Alfons Kühn',
'Al Forte',
'Al Foster',
'Alfred Breuning',
'Alfred \'Chippy\' Outcalt',
'Alfred Harth',
'Alfred Hause',
'Alfred Moore',
'Alfred Patterson',
'Alfred Richter',
'Alf Reece',
'Al Gafa',
'Al George (2)',
'Al George (3)',
'Al Gibbons',
'Al Gibson',
'Al Goering',
'Al Grey',
'Al Haig',
'Al Hall',
'Al Harewood',
'Al Hayes',
'Al Hendrickson',
'Al Hicks',
'Alice Herald',
'Alice Leon',
'Alice McLeod',
'Alice Stuart',
'Ali Haurand',
'Ali Jackson',
'Ali-Ollie Woodson',
'Alix Combelle',
'Al Jarreau',
'Al Jennings',
'Al Jordan',
'Al Kiger',
'Al Killian',
'Al Klink',
'Alla Goldberg',
'Allan Beutler',
'Allan Botschinsky',
'Allan Harshman',
'Allan Hodgkiss',
'Allan Jones (5)',
'Allan Langstaff',
'Allan Reuss',
'Allan Seltzer',
'Allan Thompson (2)',
'Allan Yeager',
'Allaudin Mathieu',
'Allen Blairman',
'Allen Durham',
'Allen Eager',
'Allen Fields',
'Allen Hanlon',
'Allen Harris (2)',
'Allen Smith',
'Allen Vizzutti',
'Al Lerner (2)',
'Al Levitt',
'Al Lorraine',
'Al Lucas',
'Al MacDowell',
'Al Maiorca',
'Al Mastren',
'Al Mattaliano',
'Al McKibbon',
'Al Morgan',
'Alonzo \'Pookie\' Johnson',
'Al Patacca',
'Al Pellegrini',
'Al Philburn',
'Alphonse Masselier',
'Alphonse Mouzon',
'Alphonso Cotton',
'Alphonso Johnson',
'Alphonso Trent',
'Al Plank',
'Al Porcino',
'Al Puccin',
'Al Ramsey',
'Al Richmond',
'Al Sears',
'Al Spieldock',
'Al Stearns',
'Al Stewart (3)',
'Alton Moore',
'Al Torre (2)',
'Alvester Garnett',
'Alvin Alcorn',
'Alvin Atkinson',
'Alvin Burroughs',
'Alvin Fielder',
'Alvin Jackson',
'Alvino Rey',
'Alvin Queen',
'Alvin Stoller',
'Al Viola',
'Al White (3)',
'Al Wichard',
'Alyrio Lima',
'Amédée Charles',
'Amedeo Tommasi',
'Ameen Saleem',
'Americo Bellotto',
'Amina Claudine Myers',
'Amir Ziv',
'Amos Gordon',
'Amos Trice',
'Amy Roslyn',
'Anatol Kaminsky',
'Anders Burman',
'Anders Christensen',
'Anders Lindskog',
'Anderson Lacy',
'Anders Svanoe',
'Anders Ullberg',
'Anders Wiborg',
'Andrea Formenti',
'Andrea Pozza',
'André Cornille',
'Andre Dabonneville',
'André Ekyan',
'Andre Hayward',
'Andrei Kondakov',
'Andrei Strobert',
'André Jourdan',
'Andre Lewis',
'André Paquinet',
'André Persiany',
'André Previn',
'Andres Meringuito',
'André Spang',
'Andrew Brown (5)',
'Andrew Clark (3)',
'Andrew Cyrille',
'Andrew Dickeson',
'Andrew Ford (3)',
'Andrew \'Goon\' Gardner',
'Andrew Hill',
'Andrew McGhee',
'Andrew Simpkins',
'Andrew White',
'Andrzej Cudzich',
'Andy Bey',
'Andy Duryea',
'Andy Ferretti',
'Andy Fitzgerald',
'Andy Fusco',
'Andy Gibson',
'Andy Gonzalez',
'Andy Jackson (6)',
'Andy Kirk',
'Andy Laverne',
'Andy Marsala',
'Andy Martin',
'Andy McCloud',
'Andy McDevitt',
'Andy McGovin',
'Andy McKee',
'Andy Middleton',
'Andy Peele',
'Andy Picard',
'Andy Pino',
'Andy Russo',
'Andy Scherrer',
'Andy Secrest',
'Andy Sheppard',
'Andy Snitzer',
'Andy Vargas',
'Andy White',
'Angie Callea',
'Angus MacLise',
'Angus Thomas',
'Anita Boyer',
'Anita Evans',
'Anita O\'Day',
'Anita Pointer',
'Ann Baker',
'Anne Drummond',
'Ann E. Sutton',
'Annette Peacock',
'Ann Graham (4)',
'Annie Fratellini',
'Annisteen Allen',
'Ann Patterson',
'Ann Winley',
'Anselm Kluge',
'Anthony Bisazza',
'Anthony Braxton',
'Anthony Cole (3)',
'Anthony Corbett',
'Anthony Cox',
'Anthony Davis (2)',
'Anthony Doria',
'Anthony Jackson',
'Anthony Maratea',
'Anthony Ortega',
'Anthony Pinciotti',
'Anthony Sciacca',
'Anthony Sophos',
'Anthony Williams',
'Anthony Wonsey',
'Antje Busch',
'Anton Fig',
'Antonín Julina',
'Antonín Viktora',
'Antonio Adame',
'Antonio Ciacca',
'Antonio Faraò',
'Antonio Hart',
'Antonio Sanchez (2)',
'Antonio \'Tony\' Rovira',
'Antonis Anissegos',
'April Ames',
'Aram Schefrin',
'Archie Alleyne',
'Archie Bell',
'Archie Johnson',
'Archie LeCoque',
'Archie Martin',
'Archie Shepp',
'Ares Tavolazzi',
'Ari Ambrose',
'Arie Volinez',
'Ari Hoenig',
'Arild Andersen',
'Arjen Gorter',
'Armand Cavallaro',
'Armand Molinetti',
'Armando Peraza',
'Armin Rusch',
'Arne Domnérus',
'Arnett Cobb',
'Arnett Sparrow',
'Arney Farterd',
'Arnie Lawrence',
'Arno Gullberg',
'Arnold Adams',
'Arnold Belnick',
'Arnold Brilhart',
'Arnold Covey',
'Arnold Fishkin',
'Arnold Jarvis (2)',
'Arnold Koblentz',
'Arnold Ross',
'Arnold Teich',
'Arno Marsh',
'Art Baron',
'Art Beck',
'Art Blakey',
'Art Capehart',
'Art Davis',
'Art Depew',
'Art Farmer',
'Art Frank',
'Art House',
'Arthur Adams',
'Arthur \'Babe\' Campbell',
'Arthur Barrow',
'Arthur Bitker',
'Arthur Blythe',
'Arthur Briegleb',
'Arthur Briggs',
'Arthur Clarke',
'Arthur Dennis',
'Arthur Edgehill',
'Arthur Gleghorn',
'Arthur Greenslade',
'Arthur Harper',
'Arthur Herbert',
'Arthur Hoyle',
'Arthur Knight',
'Arthur Motta',
'Arthur Rando',
'Arthur Rollini',
'Arthur Sammons',
'Arthur Schutt',
'Arthur Smith (16)',
'Arthur Theus',
'Arthur Watts',
'Arthur Whetsol',
'Arthur Wright',
'Artie Anton',
'Artie Baker',
'Artie Bernstein',
'Artie Foster',
'Artie Kane',
'Artie Kaplan',
'Artie Seelig',
'Artie Shapiro',
'Artie Shaw',
'Artie Starks',
'Art Johnson',
'Art Karle',
'Art Koenig',
'Art Linsner',
'Art Lund',
'Art Maebe',
'Art Mardigan',
'Art Masters',
'Art Miller',
'Art Moore (2)',
'Arto Tuncboyaciyan',
'Art Pepper',
'Art Phipps',
'Art Pirie',
'Art Raboy',
'Art Ralston',
'Art Robey',
'Art Ryerson',
'Art Simmons',
'Art St. John',
'Art Tancredi',
'Art Tatum',
'Art Taylor',
'Art Tripp',
'Arturo O\'Farrill',
'Arturo Sandoval',
'Artur Pavlíček',
'Art Van Damme',
'Arvell Shaw',
'Arville Harris',
'Arvin Garrison',
'Ashley Alexander (2)',
'Ashley Fannell',
'Ashley Fennell',
'Ashley Slater',
'Atle Hammer',
'Attila Zoller',
'Attilio Zanchi',
'Augusto Mancinelli',
'Aura Dione',
'Austin Roberts (2)',
'Austin Young',
'Avery Sharpe',
'Axel Hennies',
'Aye Guy',
'Aynsley Dunbar',
'Azar Lawrence',
'Azzedin Weston',
'Babe Bowman',
'Babe Clark',
'Babe Russin',
'Babe Wagner',
'Babs Gonzales',
'Baby Cox',
'Baby Dodds',
'Baby Lovett',
'Badi Assad',
'Baikida Carroll',
'Bänz Oester',
'Barbara Carroll',
'Barbara Long',
'Barney Bigard',
'Barney Kessel',
'Barney McAll',
'Barney Spieler',
'Barney Wilen',
'Barney Zudecoff',
'Barre Phillips',
'Barrett Deems',
'Barrie Lee Hall Jr.',
'Barry Altschul',
'Barry Finnerty',
'Barry Galbraith',
'Barry Guy',
'Barry Harris (2)',
'Barry Keiner',
'Barry Maur',
'Barry Morgan',
'Barry Reeves (2)',
'Barry Ries',
'Barry Rogers',
'Barry Ross',
'Barry Smith (5)',
'Barry Ulman',
'Bart Caldarelli',
'Bart Hall',
'Bart Van Lier',
'Bart Varsalona',
'Bart Walsaliona',
'Battista Lena',
'Bayardo Velarde',
'Bea Booze',
'Beat Hofstetter',
'Beat Kappeler',
'Beatrice Byers',
'Beaver Harris',
'Bebo Valdès'
'Belton Evans',
'Ben Allison',
'Ben Aronov',
'Ben Besiakov',
'Ben Brown (2)',
'Bendik Hofseth',
'Ben Dixon',
'Ben Ginsberg',
'Bengt Hallberg',
'Bengt Stark',
'Ben Hall (4)',
'Ben Heller',
'Ben Henderson (2)',
'Benjamin Brown (2)',
'Benjamin Henocq',
'Benjamin Jacobs-El',
'Benjamin Lundy',
'Benjamin Orzechowski',
'Ben Johnson (15)',
'Ben Monder',
'Bennie Bailey',
'Bennie Green',
'Bennie Maupin',
'Bennie Payne',
'Bennie Wallace',
'Benny Bailey',
'Benny Baker',
'Benny Barth',
'Benny Bendorff',
'Benny Bennet',
'Benny Bonaccio',
'Benny Booker',
'Benny Carter',
'Benny Feman',
'Benny Fonville',
'Benny Golson',
'Benny Goodman',
'Benny Green',
'Benny Harris',
'Benny Jackson',
'Benny Lagasse',
'Benny Morton',
'Benny Moten',
'Benny Powell',
'Benny Rietveld',
'Benny Stabler',
'Benny Vasseur',
'Benny Waters',
'Benny Weeks',
'Benoit Quersin',
'Ben Pickering',
'Ben Pollack',
'Ben Riley',
'Ben Seaman',
'Ben Smith (9)',
'Ben Street',
'Ben Surman',
'Bent Axen',
'Ben Thigpen',
'Bent Nielsen',
'Ben Tucker',
'Ben Vaughn',
'Ben Webster',
'Ben Wittman',
'Ben Wolfe',
'Ben Zimberoff',
'Beppe Calamosca',
'Bernard Addison',
'Bernard Anderson',
'Bernard Flood',
'Bernard Greenhouse',
'Bernard Hulin',
'Bernard Kundell',
'Bernard Lubat',
'Bernard McKinney',
'Bernard Peiffer',
'Bernard Purdie',
'Bernard Tinterow',
'Bernard Vitet',
'Bernard Wright',
'Bernd Konrad',
'Bernd Moschner',
'Bernd Reiter',
'Bernd Steffanowski',
'Bernd Wippich',
'Bernie Billings',
'Bernie Cavaliere',
'Bernie Glow',
'Bernie Greenhouse',
'Bernie Leighton',
'Bernie Mackey',
'Bernie Peacock',
'Bernie Privin',
'Bernie Senensky',
'Bernie Worrell',
'Bernt Rosengren',
'Bert Curry',
'Bert Ezard',
'Bertha Hope',
'Bert Howard',
'Bertil Lövgren',
'Bert Joris',
'Bert Van Duynhoven',
'Beryl Booker',
'Beryl Bryden',
'Bessie Smith',
'Bette Midler',
'Betty Bleigh',
'Betty Carter',
'Betty Glamann',
'Beverly Moran',
'Beverly Peer',
'Biddy Bastien',
'Big Chief\' Russell Moore',
'Big Jim Sullivan',
'Big John Greer',
'Bill Abel (4)',
'Bill Adams (10)',
'Bill Atkinson (2)',
'Bill Barber',
'Bill Barron',
'Bill Beason',
'Bill Berry',
'Bill Bethel',
'Bill Bickford',
'Bill Boyole',
'Bill Bradley (3)',
'Bill Britto',
'Bill Bufkin',
'Bill Bushey',
'Bill Byrne',
'Bill Byrne (3)',
'Bill Calkins',
'Bill Castagnino',
'Bill Castell',
'Bill Catalano (2)',
'Bill Challis',
'Bill Charlap',
'Bill Chase',
'Bill Cherones',
'Bill Clark',
'Bill Coleman (2)',
'Bill Connors',
'Bill Conrad (2)',
'Bill Cronk',
'Bill Crow',
'Bill Danzien',
'Bill De Arango',
'Bill Decker',
'Bill Depew',
'Bill Dillard',
'Bill Dixon',
'Bill Dobbins',
'Bill Doggett',
'Bill Dolney',
'Bill Douglass (2)',
'Bill Easley',
'Bill Ehrenkranz',
'Bill Elgart',
'Bill Ellington',
'Bill Elton',
'Bill English',
'Bill Evans',
'Bill Evans (3)',
'Bill Eyden',
'Bill Fitch',
'Bill Frazier',
'Bill Frisell',
'Bill Fritz',
'Bill Gibson',
'Bill Goodall',
'Bill Goodwin',
'Bill Grah',
'Bill Graham',
'Bill Hardman',
'Bill Harris',
'Bill Hartman',
'Bill Hicks (2)',
'Bill Hitz',
'Bill Holman',
'Bill Hood',
'Bill Horan',
'Bill Hughes (2)',
'Billie Holiday',
'Billie Rogers (2)',
'Bill Johnson',
'Bill King (5)',
'Bill Lee (2)',
'Bill Legan',
'Bill Leslie',
'Bill Liston',
'Bill Luther',
'Bill Massey',
'Bill Mattison',
'Bill Mays',
'Bill McHenry',
'Bill McLemore (2)',
'Bill McMahon',
'Bill Miller (2)',
'Bill Mobley',
'Bill Moody',
'Bill Mulraney',
'Bill Nadel',
'Bill Oldham',
'Bill Ortiz',
'Bill Palmer (3)',
'Bill Paynter',
'Bill Pemberton',
'Bill Perkins',
'Bill Perkins (2)',
'Bill Phillips',
'Bill Pitman',
'Bill Plavan',
'Bill Plummer',
'Bill Porter (4)',
'Bill Potts',
'Bill Pursell',
'Bill Pusey',
'Bill Ramsey (3)',
'Bill Rank',
'Bill Reichenbach',
'Bill Reichenbach (2)',
'Bill Richmond',
'Bill Robertson',
'Bill Robinson (4)',
'Bill Rogers (9)',
'Bill Ross (2)',
'Bill Russo',
'Bill Saxton',
'Bill Scaffe',
'Bill Schaeffer',
'Bill Schumann',
'Bill Sears',
'Bill Shine',
'Bill Skeat',
'Bill Smiley',
'Bill Smith (20)',
'Bill Spears',
'Bill Stapleton',
'Bill Stewart',
'Bill Suyker',
'Bill Swindell',
'Bill Takas',
'Bill Tamper',
'Bill Thiele',
'Bill Thomas (3)',
'Bill Thompson (9)',
'Bill Triglia',
'Bill Trujillo',
'Bill Vaccaro',
'Bill Vitale (2)',
'Bill Washer',
'Bill Watrous',
'Bill White (2)',
'Bill Wimberly',
'Billy Bauer',
'Billy Bean',
'Billy Bowen',
'Billy Brooks',
'Billy Butler',
'Billy Butler (3)',
'Billy Butterfield',
'Billy Byers',
'Billy Campbell',
'Billy Childs',
'Billy Cobham',
'Billy Drewes',
'Billy Drummond',
'Billy Eckstine',
'Billy Exiner',
'Billy Fowler',
'Billy Gardner',
'Billy Gault',
'Billy Gussak',
'Billy Hadnott',
'Billy Harper',
'Billy Hart',
'Billy Hicks',
'Billy Higgins',
'Billy Hodges',
'Billy Hunt (2)',
'Billy Joel',
'Billy Kent',
'Billy Kyle',
'Billy Mackel',
'Billy Mark',
'Billy Martin',
'Billy Massey',
'Billy May',
'Billy Mintz',
'Billy Mitchell',
'Billy Moore (5)',
'Billy Mundi',
'Billy Munn',
'Billy Mure',
'Billy Osborne',
'Billy Paul',
'Billy Pierce',
'Billy Preston',
'Billy \'Red\' Love',
'Billy Robbins (2)',
'Billy Rogers (2)',
'Billy Root',
'Billy Ross',
'Billy Rowland',
'Billy Schneider',
'Billy Smith',
'Billy Strayhorn',
'Billy Stuart',
'Billy Taylor Jr.',
'Billy Taylor',
'Billy Taylor Sr.',
'Billy Usselton',
'Billy Wallace',
'Billy Williams (14)',
'Bill Zickenfoose',
'Bingie Madison',
'Birch Johnson',
'Biréli Lagrène',
'Bitsy Mullins',
'Bix Beiderbecke',
'Bjørn Kjellemyr',
'Blake Hines',
'Blake Reynolds',
'Blanche Calloway',
'Blossom Dearie',
'\'Blue\' Gene Tyranny',
'Blue Mitchell',
'Bob Achilles',
'Bob Acri',
'Bob Ahern (2)',
'Bob Alexy',
'Bob Ascher',
'Bob Bain',
'Bob Bates',
'Bob Behrendt',
'Bob Bein',
'Bob Belden',
'Bob Berg',
'Bob Bertaux',
'Bob Blumenhoven',
'Bob Bodley',
'Bob Boswell',
'Bob Bowly',
'Bob Bowman (3)',
'Bob Braye',
'Bob Brookmeyer',
'Bob Bunch',
'Bob Burgess',
'Bob Butta',
'Bobby Bandiera',
'Bobby Bennett',
'Bobby Bradford',
'Bobby Broom',
'Bobby Bryant',
'Bobby Burnet',
'Bobby Byrne',
'Bobby Clark (2)',
'Bobby Crowe (3)',
'Bobby Cruz',
'Bobby Davis (4)',
'Bobby Donaldson',
'Bobby Donaldson (3)',
'Bobby Durham',
'Bobby Enriquez',
'Bobby Fever',
'Bobby Gibbons',
'Bobby Graham (3)',
'Bobby Guyer',
'Bobby Hackett',
'Bobby Haynes',
'Bobby Hutcherson',
'Bobby Jaspar',
'Bobby Johnson',
'Bobby Jones (2)',
'Bobby Kimball',
'Bobby Knight',
'Bobby Lamb',
'Bobby Lyle',
'Bobby Martin (2)',
'Bobby Militello',
'Bobby Mitchell',
'Bobby Moore (3)',
'Bobby Naughton',
'Bobby Plater',
'Bobby Previte',
'Bobby Rodriguez',
'Bobby Rosengarden',
'Bobby Scott',
'Bobby Sherwood',
'Bobby Shew',
'Bobby Stark',
'Bobby Styles',
'Bobby Thomas (2)',
'Bobby Timmons',
'Bobby Troup',
'Bobby Tucker',
'Bobby Valentin',
'Bobby Watson (2)',
'Bobby White',
'Bobby Williams (6)',
'Bobby Womack',
'Bobby Woodlen',
'Bobby Zankel',
'Bob Carr',
'Bob Carr (4)',
'Bob Carter (15)',
'Bob Carter (2)',
'Bob Carter (4)',
'Bob Casey',
'Bob Coassin',
'Bob Collins (2)',
'Bob Cooper',
'Bob Corwin',
'Bob Cranshaw',
'Bob Crull',
'Bob Cunningham',
'Bob Curnow',
'Bob Curtis (2)',
'Bob Daugherty',
'Bob Dawes',
'Bob Decker',
'Bob Devos',
'Bob Dockstader',
'Bob \'Doc\' Livingston',
'Bob Dorough',
'Bob Dylan',
'Bob Edmondson',
'Bob Efford',
'Bob Enevoldsen',
'Bob Fitzpatrick',
'Bob Fleming',
'Bob Florence',
'Bob Fuller',
'Bob Garcia',
'Bob Geldof',
'Bob Gioga',
'Bob Gordon (2)',
'Bob Graettinger',
'Bob Graf',
'Bob Haggart',
'Bob Hammerstone',
'Bob Harmon',
'Bob Harrington (2)',
'Bob Harris (5)',
'Bob Hicks',
'Bob Higgins (3)',
'Bob Horton',
'Bob James',
'Bob Jenkins (4)',
'Bob Jenney',
'Bob Jung',
'Bob \'Junior\' Williams',
'Bob Karch',
'Bob Kaye',
'Bob Keene',
'Bob Kesterson',
'Bob Kindred',
'Bob Kitsis',
'Bob Lanese',
'Bob Lark',
'Bob Lawson',
'Bob Leininger',
'Bob Lesher',
'Bob Lessey',
'Bob Lively',
'Bob Lord (2)',
'Bob Lymperis',
'Bob Mabane',
'Bob Magnusson',
'Bob Maize',
'Bob Malach',
'Bob Mann',
'Bob Manners (2)',
'Bob Marlo',
'Bob Martin (6)',
'Bob McChesney',
'Bob McCracken',
'Bob Merrill (2)',
'Bob Mintzer',
'Bob Moore',
'Bob Morgan (6)',
'Bob Morrow',
'Bob Moses',
'Bob Mosley (2)',
'Bob Mover',
'Bob Munoz',
'Bob Neal (3)',
'Bob Neel',
'Bob Newman (3)',
'Bob Nieske',
'Bob Ojeda',
'Bob Olson',
'Bobo Stenson',
'Bo Boyd',
'Bob Paige',
'Bob Peck (2)',
'Bob Pelander',
'Bob Peterson (3)',
'Bob Peterson (8)',
'Bob Pierson',
'Bob Poland',
'Bob Price',
'Bob Prince',
'Bob Quibel',
'Bob Rockwell',
'Bob Rolfe',
'Bob Rudolph',
'Bob Sanchez',
'Bob Sheppard',
'Bob Simpson',
'Bob Smith',
'Bob Smith (43)',
'Bob Snyder',
'Bob Sprentall',
'Bob Stewart',
'Bob Stone (2)',
'Bob Strahl',
'Bob Strahl (2)',
'Bob Stroup',
'Bob Summers',
'Bob Summers (3)',
'Bob Swift',
'Bob Thiele',
'Bob Thomas',
'Bob Tricarico',
'Bob Varney',
'Bob Walters (5)',
'Bob West',
'Bob Whitlock',
'Bob Wilber',
'Bob Winiker',
'Bob Wyatt (2)',
'Bob Zimmitti',
'Bob Zottola',
'Bob Zurke',
'Boncana Maïga',
'Bonnie Pottle',
'Bonnie Raitt',
'Booker Collins',
'Booker Ervin',
'Booker Little',
'Booker Pittman',
'Boots Mussulli',
'Booty Wood',
'Bora Roković',
'Boris Kozlov',
'Boris Midney',
'Boris Petrov (2)',
'Boško Petrović',
'Bo Söderberg',
'Bo Stief',
'Boyce Cullen',
'Boyd Raeburn',
'Boy Edgar',
'Brace Phillips',
'Brad Gowans',
'Brad Hatfield',
'Brad Jones',
'Bradley Spinney',
'Brad Mehldau',
'Brad Miller',
'Brad Shepik',
'Brad Warnaar',
'Brad Williams (2)',
'Brandon Fields',
'Branford Marsalis',
'Branislav Kovačev',
'Branko Pejykovic',
'Brett Stamps',
'Brew Moore',
'Brian A. Grivna',
'Brian Blade',
'Brian Brake',
'Brian Dee',
'Brian Dickinson',
'Brian Horton (2)',
'Brian Landrus',
'Brian Lynch',
'Brian Melvin',
'Brian O\'Flaherty',
'Brian O\'Rourke',
'Brian Scanlon',
'Brian Smith (9)',
'Brian Surina',
'Brian Trentham',
'Brian Williams (12)',
'Brick Fleagle',
'Bridget O\'Flynn',
'Brigitte Duncklau',
'Britt Savage',
'Britt Woodman',
'Briz',
'Brock Answer',
'Bronislav Horák',
'Brooks Tillotson',
'Brother Jack McDuff',
'Bruce Barth',
'Bruce Branson',
'Bruce Ditmas',
'Bruce Forman',
'Bruce Fowler (3)',
'Bruce Gertz',
'Bruce Johnson (4)',
'Bruce Johnstone',
'Bruce Lawrence (2)',
'Bruce MacDonald',
'Bruce Paulson',
'Bruce Snyder',
'Bruce Springsteen',
'Bruce Squires',
'Bruce Wilkins',
'Bruno Biriaco',
'Bruno Carr',
'Bruno Rondelli',
'Bruno Tommaso',
'Bryan Kent',
'Bubber Miley',
'Buck Clayton',
'Buck Hill',
'Buck Scott',
'Buck Washington',
'Bucky Calabrese',
'Bucky Calla',
'Bucky Pizzarelli',
'Bud Billings',
'Bud Brisbois',
'Bud Burridge',
'Bud Carleton',
'Budd Johnson',
'Buddy Banks (2)',
'Buddy Bregman',
'Buddy Calker',
'Buddy Catlett',
'Buddy Childers',
'Buddy Christian (2)',
'Buddy Clark',
'Buddy Collette',
'Buddy Combine',
'Buddy DeFranco',
'Buddy DiVito',
'Buddy FeatherStonaugh',
'Buddy Harper',
'Buddy Hartford',
'Buddy Hayes',
'Buddy Hughes',
'Buddy Lucas',
'Buddy Montgomery',
'Buddy Moreno',
'Buddy Morrow',
'Buddy Motsinger',
'Buddy Neal',
'Buddy Poor',
'Buddy Powers',
'Buddy Rich',
'Buddy Savitt',
'Buddy Schutz',
'Buddy Shepard',
'Buddy Tate',
'Buddy Weed',
'Buddy Williams',
'Buddy Wise',
'Buddy Woodson',
'Bud Freeman',
'Bud Gould',
'Bud Parker',
'Bud Powell',
'Bud Scott',
'Bud Shank',
'Bud Smith (2)',
'Buell Neidlinger',
'Buff Estes',
'Buford Oliver',
'Bull Moose Jackson',
'Bumps Myers',
'Bunk Gardner',
'Bunky Green',
'Bunny Berigan',
'Bunny Briggs',
'Burgher Jones',
'Burt Collins',
'Bus Bassey',
'Bus Etri',
'Buster Bailey',
'Buster Cooper',
'Buster Johnson',
'Buster Moten',
'Buster Williams',
'Buster Wilson',
'Butch Ballard',
'Butch Lacy',
'Butch Miles',
'Butch Morris',
'Butch Warren',
'Buzz Freeman',
'Buzz King (2)',
'Buzzy Brauner',
'Buzzy Drootin',
'Byron Miller',
'Byron Stripling',
'Cab Calloway',
'Caesar Giovannini',
'Cal Collins',
'Cali Aleman',
'Call Cobbs',
'Calo Scott',
'Cal Tjader',
'Calvin Banks',
'Calvin Brown',
'Calvin Hill',
'Calvin Jackson',
'Calvin Newborn',
'Calvin Strickland',
'Camelia Ben Naceur',
'Cameron Brown',
'Cameron Undy',
'Candido',
'Cannonball Adderley',
'Cappy Lewis',
'Caris Visentin',
'Carla Bley',
'Carl Allen',
'Carl Berg',
'Carl Biesacker',
'Carl Burnett',
'Carl Carter (3)',
'Carl Elmer',
'Carl Fontana',
'Carl Fortina',
'Carl Frye',
'Carl Groen',
'Carl-Henrik Norin',
'Carlinhos Brown',
'Carl Kress',
'Carl Leach',
'Carl Lott',
'Carl Maus',
'Carlo Gonzi',
'Carlo Mombelli',
'Carl Orrje',
'Carlos Barretto',
'Carlos Diernhammer',
'Carlos Duchesne',
'Carlos Duran (2)',
'Carlos Henriquez',
'Carlos McKinney',
'Carlos \'Patato\' Valdes',
'Carlos Rosario',
'Carlos Santana',
'Carlos Vidal',
'Carlos Ward',
'Carl Ottobrino',
'Carl Perkins (4)',
'Carl Poole',
'Carl Pruitt',
'Carl Saunders',
'Carl Smith',
'Carlton McBeath',
'Carlton McBeth',
'Carl Warwick',
'Carl Zeigler',
'Carmell Jones',
'Carmen Bradford',
'Carmen Leggio',
'Carmen Mastren',
'Carol Buck',
'Carol Kaye',
'Carol Lee (8)',
'Carolyne Mas',
'Carolyn Grey',
'Carrington Visor Jr.'
'Carroll Dickerson',
'Carson Smith',
'Carsten Dahl',
'Carter Jefferson',
'Castor McCord',
'Cat Anderson',
'Caughey Roberts',
'Cecelia Hobbs',
'Cecil Bridgewater',
'Cecil Irwin',
'Cecil McBee',
'Cecil Payne',
'Cecil Scott',
'Cecil Taylor',
'Cedar Walton',
'Cedric Wallace',
'Ceele Burke',
'Cees See',
'Cees Slinger',
'Cees Smal',
'Celia Cruz',
'Chach Gonzales',
'Chad Wackerman',
'Chaka Khan',
'Chano Domínguez',
'Chano O\'Ferral',
'Chano Pozo',
'Charlene Bartley',
'Charles Ables',
'Charles Bateman',
'Charles Bell',
'Charles Brackeen',
'Charles Butterfield',
'Charles Coolidge',
'Charles Crosby',
'Charles Davis',
'Charles Davis (2)',
'Charles Eubanks',
'Charles Fambrough',
'Charles Frank (3)',
'Charles Frankhauser',
'Charles Frazier',
'Charles Gelruth',
'Charles Greenlee',
'Charles Griffin',
'Charles Harris (2)',
'Charles Hary',
'Charles Huffine',
'Charles Johnson (17)',
'Charles Johnson (9)',
'Charles Kynard',
'Charles La Rue',
'Charles Lawson (3)',
'Charles Lisée',
'Charles Lloyd',
'Charles Loper',
'Charles Matson',
'Charles McCamish',
'Charles McCracken',
'Charles McGhee',
'Charles McPherson',
'Charles Mingus',
'Charles Moffett',
'Charles O\'Kane',
'Charles Orieux',
'Charles Owens',
'Charles Pillars',
'Charles Pillow',
'Charles Price',
'Charles Saudrais',
'Charles Stephens',
'Charles Strickfaden',
'Charles Sullivan',
'Charles Taggart',
'Charles Tolliver',
'Charles Turner (3)',
'Charles Veal Jr.',
'Charles Warwick',
'Charlie Alexander',
'Charlie Allen (3)',
'Charlie Barnet',
'Charlie Bechler',
'Charlie Byrd',
'Charlie Calzaretta',
'Charlie Castaldo',
'Charlie Christian',
'Charlie DiMaggio',
'Charlie Dixon',
'Charlie Drayton',
'Charlie Fowlkes',
'Charlie Gaines',
'Charlie Green',
'Charlie Grifford',
'Charlie Haden',
'Charlie Henry (3)',
'Charlie Holmes',
'Charlie Howard',
'Charlie Irvis',
'Charlie Johnson (4)',
'Charlie Jones (2)',
'Charlie Kamey',
'Charlie Kegley',
'Charlie Kennedy',
'Charlie Lamphere',
'Charlie Lewis',
'Charlie Lodice',
'Charlie Margulis',
'Charlie Mariano',
'Charlie McLean (2)',
'Charlie McLean (3)',
'Charlie Morillas',
'Charlie Musselwhite',
'Charlie Parker',
'Charlie Perry',
'Charlie Persip',
'Charlie Prebble',
'Charlie Queener',
'Charlie Rouse',
'Charlie Shavers',
'Charlie Shoemake',
'Charlie Short',
'Charlie Small',
'Charlie Smith (2)',
'Charlie Spivak',
'Charlie Teagarden',
'Charlie Ventura',
'Charlie Walp',
'Charly Antolini',
'Charnett Moffett',
'Chase Dean',
'Chase Morrison',
'Chauncey Haughton',
'Chauncey Morehouse',
'Chauncey Welsch',
'Chelsea Quealey',
'Cheo Feliciano',
'Cheryl Hardwick',
'Chester Clark (2)',
'Chester Hazlett',
'Chester Thompson',
'Chester Thompson (2)',
'Chet Amsterdam',
'Chet Baker',
'Chet Ferretti',
'Chet Kruley',
'Chet Pardee',
'Cheyney Thomas',
'Chicas',
'Chick Bullock',
'Chick Carter',
'Chick Corea',
'Chick Keeney',
'Chick Reeves',
'Chick Webb',
'Chico Alvarez',
'Chico Freeman',
'Chico Guerrero',
'Chico Hamilton',
'Chico Marx',
'Chico Pinheiro',
'Chief Bey',
'Chink Johnson',
'Chino Pozo',
'Chino Valdes',
'Chip Hoehler',
'Chip Jackson',
'Chip White',
'Chris Albert (3)',
'Chris Anderson (5)',
'Chris Bacas',
'Chris Brubeck',
'Chris Cheek',
'Chris Dahlgren',
'Chris Dean',
'Chris Flory',
'Chris Galuman',
'Chris Griffin (3)',
'Chris Gulhaugen',
'Chris Hayes',
'Chris Higgins (2)',
'Chris Hills',
'Chris Hunter',
'Chris Mancini',
'Chris McCann',
'Chris Palmaro',
'Chris Parker (2)',
'Chris Potter (2)',
'Chris Pyne',
'Chris Solberg',
'Chris Spedding',
'Chris Swansen',
'Chris Thompson',
'Christian Bellest',
'Christiane Legrand',
'Christian Garros',
'Christian Guizien',
'Christian Jacob',
'Christian Kellens',
'Christian Lembrecht',
'Christian Martinez',
'Christian McBride',
'Christian Muthspiel',
'Christian Sands',
'Christian Spering',
'Christian Wagner (2)',
'Christina von Bülow',
'Christine Wiltshire',
'Christoph Brandt - Lindbaum',
'Christophe Cravero',
'Christophe Panzani',
'Christopher Thomas',
'Christophe Schweizer',
'Chris White (3)',
'Chris Witherspoon',
'Chris Woods',
'Chubby Jackson',
'Chuck Anderson',
'Chuck Andrus',
'Chuck Berghofer',
'Chuck Carter',
'Chuck Carter (2)',
'Chuck Connors',
'Chuck Deardorf',
'Chuck Domanico',
'Chuck Findley',
'Chuck Flores',
'Chuck Gentry',
'Chuck Harris (5)',
'Chuck Israels',
'Chuck Lampkin',
'Chuck Lawson',
'Chuck Loeb',
'Chuck Mangione',
'Chuck Manning',
'Chuck Morrison',
'Chuck Peterson',
'Chuck Rainey',
'Chuck Riggs',
'Chuck Robinson',
'Chuck Schmidt',
'Chuck Stentz',
'Chuck Thomas (4)',
'Chuck Thompson',
'Chuck Wayne',
'Chuck Williams',
'Chunky (3)',
'Churchill Jolobe',
'Cindy Blackman',
'Claes Björnberg',
'Clare Fischer',
'Clarence Anderson',
'Clarence Banks',
'Clarence Becton',
'Clarence Clemons',
'Clarence \'Gatemouth\' Brown',
'Clarence Holiday',
'Clarence Johnston',
'Clarence Jones (2)',
'Clarence Penn',
'Clarence Ross',
'Clarence Shaw',
'Clarence \'Skip\' Stine',
'Clarence Smith',
'Clarence Terry',
'Clarence Trice',
'Clarence Watson',
'Clarence Wheeler (2)',
'Clarence Willard',
'Clarence Williams',
'Clarence Wright',
'Clark Gayton',
'Clark Terry',
'Clark Tracey',
'Clark Yocum',
'Claude Bolling',
'Claude Bowen',
'Claude Delcloo',
'Claude Deppa',
'Claude Dunson',
'Claude Egéa',
'Claude Evelyne',
'Claude Gilroy',
'Claude Hopkins',
'Claude Jones',
'Claude Lakey',
'Claude Noel',
'Claude Scheiner',
'Claude Thornhill',
'Claude Williams',
'Claude Williamson',
'Claudia Bombardella',
'Claudine Meunier',
'Claudio De Queiroz',
'Claudio Puntin',
'Claudio Roditi',
'Claudio Szenkar',
'Claudius Alzner',
'Claus Bühler (3)',
'Claus-Robert Kruse',
'Clay Hervey',
'Clay Jenkins',
'Clem Clempson',
'Clem De Rosa',
'Cliff Almond',
'Cliff Barton',
'Cliff Heather',
'Cliff Hill (2)',
'Cliff Jackson',
'Cliff Jackson (3)',
'Cliff Leeman',
'Clifford Adams',
'Clifford Barbaro',
'Clifford Brown',
'Clifford Carter',
'Clifford Jarvis',
'Clifford Jordan',
'Clifford Scott',
'Clifford Solomon',
'Cliff Smalls',
'Cliff Strickland',
'Cliff Weston',
'Cliff Woodbridge',
'Clif Lee',
'Clifton Best',
'Clint Davis',
'Clint Garvin',
'Clint Houston',
'Clint Neagley',
'Clint Sharman',
'Clint Weaver',
'Clive Acker',
'Clive Powell (2)',
'Clyde Bernhardt',
'Clyde Hart',
'Clyde Hurley',
'Clyde Lombardi',
'Clyde Newcomb',
'Clyde Reasinger',
'Clyde Rounds',
'Clyde Singleton',
'Coke Escovedo',
'Coleman Hawkins',
'Coleridge Goode',
'Coleridge-Taylor Perkinson',
'Colin Bailey',
'Colin Green (2)',
'Colin Satterwhite',
'Collin Walcott',
'Columbus Baker',
'Conn Humphreys',
'Connie Boswell',
'Connie Haines',
'Connie Harvey',
'Connie Kay',
'Connie Wainwright',
'Conrad Bauer',
'Conrad Gozzo',
'Conrad Herwig',
'Conrad Lanoue',
'Consuela Lee Moorehead',
'Conte Candoli',
'Cootie Williams',
'Corey Wilkes',
'Corky Corcoran',
'Cornelius Thomas',
'Cornell Dupree',
'Cornell Smelser',
'Count Basie',
'Cozy Cole',
'Craig Gosnell',
'Craig Handy',
'Craig Harris (3)',
'Craig Kastelnik',
'Craig Taborn',
'Crawford Wethington',
'Creed Taylor',
'\'Crusher\' Bennett',
'Curley Hamner',
'Curly Chalker',
'Curly Russell',
'Curt Berg (2)',
'Curt Bley',
'Curtis Counce',
'Curtis Fowlkes',
'Curtis Fuller',
'Curtis Lowe',
'Curtis Lundy',
'Curtis Mosby',
'Curtis Murphy',
'Curtis Ousley',
'Curtis Peagler',
'Curtis Porter',
'Cutty Cutshall',
'Cy Baker',
'Cy Bernard',
'Cyndi Lauper',
'Cyril Haynes',
'Cyril Towbin',
'Cyrus Chestnut',
'Cyrus Faryar',
'Cyrus St. Clair',
'Cy Sulak',
'Cy Touff',
'Czesław Bartkowski',
'Dado Moroni',
'Dae Boon',
'Dag Arnesen',
'Dalbert Bright',
'Dale Barlow',
'Dale Brown',
'Dale Carley',
'Dale Devoe',
'Dale Frank',
'Dale Jones',
'Dale Kirkland',
'Dale McMickle',
'Dale Pearce',
'Dale Pierce',
'Dalila Khatir',
'Dalton Rizzotto',
'Dalton Smith',
'Damir Dičić',
'Dana Hughes',
'Dana Teboe',
'Dan Aykroyd',
'Dan Brubeck',
'Dan D\'Imperio',
'Dan Faulk',
'Dan Fornero',
'Daniel Collette',
'Daniele Mazzucchelli',
'Daniel Humair',
'Daniel Sadownick',
'Danilo Perez',
'Danilo Terenzi',
'Dan Lube',
'Dan Martin (19)',
'Dan Minor',
'Dannie Richmond',
'Danny Alvin',
'Danny Bank',
'Danny Barber (2)',
'Danny Barcelona',
'Danny Barker',
'Danny Cahn',
'Danny Coleman',
'Danny Cowan',
'Danny Gottlieb',
'Danny Hayes',
'Danny Megna',
'Danny Mixon',
'Danny Moore',
'Danny Negri',
'Danny Nolan',
'Danny Perri',
'Danny Polo',
'Danny Quebec West',
'Danny Small (3)',
'Danny Stiles',
'Danny Thompson',
'Danny Trifan',
'Danny Turner',
'Danny Vannelli',
'Danny Weiss',
'Dan Palladino',
'Dan Rieser',
'Dan Salmasian',
'Dan Terry',
'Dan Wall',
'Dardanelle',
'Daren Reinsch',
'Darlene Love',
'Darnell Howard',
'Darrel Gardner',
'Darryl Jones',
'Daryl \'Flea\' Campbell',
'Daryl Hall',
'Daunik Lazro',
'Dave Bailey',
'Dave Barbour',
'Dave Bargeron',
'Dave Black',
'Dave Bowman',
'Dave Boyle (2)',
'Dave Bristow',
'Dave Brubeck',
'Dave Burns',
'Dave Burrell',
'Dave Carpenter',
'Dave Chapman (4)',
'Dave Coleman',
'Dave Coone',
'Dave Culp',
'Dave Dana',
'Dave Dipietro',
'Dave Dyson',
'Dave Ellis (2)',
'Dave Figg',
'Dave Frishberg',
'Dave Fullerton',
'Dave Gale',
'Dave Gonsalves',
'Dave Gonzales',
'Dave Grusin',
'Dave Harris (2)',
'Dave Holland',
'Dave Hubbard',
'Dave Jackson (15)',
'Dave Jacobs',
'Dave Johnson (52)',
'Dave Keim',
'Dave Kennedy (3)',
'Dave King',
'Dave Klein (3)',
'Dave Koonse',
'Dave LaLama',
'Dave Larocca',
'Dave Mackay',
'Dave MacRae',
'Dave Madden',
'Dave Matthews (2)',
'Dave Matthews (3)',
'Dave Mayten',
'Dave McKenna',
'Dave McRae',
'Dave Miller (20)',
'Dave Moore (21)',
'Dave Moser',
'Dave Page',
'Dave Parlato',
'Dave Peck (3)',
'Dave Pell',
'Dave Pike',
'Dave Posmontier',
'Dave Ratajczak',
'Dave Riekenberg',
'Dave Rivera',
'Dave Robbins (4)',
'Dave Robinson (7)',
'Dave Schackne',
'Dave Schultze',
'Dave Schumacher',
'Dave Shapiro',
'Dave Sova',
'Dave Stahl',
'Dave Stewart (2)',
'Dave Stone (2)',
'Dave Stryker',
'Dave Tofani',
'Dave Tough',
'Dave Uchitel',
'Dave Valentin',
'Dave Van Kriedt',
'Dave Weckl',
'Dave Wells',
'Dave Wheeler',
'Dave Wickins',
'Dave Wilborn',
'Dave Williams (54)',
'Dave Young (10)',
'Dave Young (3)',
'Davey Schildkraut',
'Dave Zeagler',
'David Allyn',
'David Amram',
'David Amsterdam',
'David Baker (3)',
'David Benoit',
'David Berger (2)',
'David Berkman',
'David Brown (5)',
'David Cavanaugh',
'David Chapman',
'David Clowney',
'David Duke',
'David Earle Johnson',
'David Enos',
'David Ephross',
'David Eubanks (2)',
'David Eyges',
'David Finck',
'David Fiuczynski',
'David Friesen',
'David Frisina',
'David Garrett (4)',
'David Gates',
'David Glasser (2)',
'David Goldblatt',
'David Hazeltine',
'David Horowitz',
'David Izenzon',
'David James (15)',
'David Johansen',
'David Johnson (2)',
'David Jones (41)',
'David Kikoski',
'David K. Mathews',
'David Kurtzer',
'David Lahm',
'David Liebman',
'David Livolsi',
'David Mann',
'David Margen',
'David Martin (10)',
'David Martin (8)',
'David Murray',
'David Patrois',
'David Piltch',
'David Prater (2)',
'David Pritchard (2)',
'David Rosenboom',
'David Ruffin Jr',
'David Sanborn',
'David Sanchez (4)',
'David Sancious',
'David Schnitter',
'David Schwartz',
'David Sherr',
'David Shostac',
'David Simmons (4)',
'David Spinozza',
'David Sterkin',
'David S. Ware',
'David Taylor',
'David T. Walker',
'David Weiss (9)',
'David Williams (2)',
'David Williams (34)',
'David Wong',
'David Young (4)',
'DD Jackson',
'Deane Kincaide',
'Dean Johnson (3)',
'Dean Palanzo',
'Dean Pratt',
'Deborah Holland',
'Dee Barton',
'Dee Dee Sharp Gamble',
'Dee Keating',
'Deena Shoshkes',
'Delfeayo Marsalis',
'Delmar Brown',
'Dempsey Wright',
'Denis Charles',
'Denise Varene',
'Denis Leloup',
'Dennis Anderson',
'Dennis Budimir',
'Dennis Chambers',
'Dennis Davis',
'Dennis Dotson',
'Dennis Farias',
'Dennis Irwin',
'Dennis Luxion',
'Dennis Mackrel',
'Dennis Moorman',
'Dennis Noday',
'Dennis Wilson',
'Denny Walley',
'Denny Zeitlin',
'Denzil Best',
'DePriest Wheeler',
'Derek Humble',
'Derek Smith',
'Derek Watkins',
'Deron Johnson',
'Detlef Surmann',
'Dewey Johnson',
'Dewey Redman',
'Dexter Gordon',
'Dexter Hall',
'Diana Moreira Booker',
'Diana Ross',
'Diane Monroe',
'Dick Abel',
'Dick Berk',
'Dick Bienenfeld',
'Dick Carter (2)',
'Dick Cary',
'Dick Clark',
'Dick Cole',
'Dick Collins',
'Dick Forest',
'Dick Garcia',
'Dick Gould',
'Dick Griffin',
'Dick Hafer',
'Dick Haymes',
'Dick Heckstall-Smith',
'Dick Horvath',
'Dick Houlgate',
'Dick Hyde',
'Dick Hyman',
'Dickie Wells',
'Dick Johnson (8)',
'Dick Jones (3)',
'Dick Kane',
'Dick Katz',
'Dick Kenney',
'Dick Kniss',
'Dick Lieb',
'Dick McDonough',
'Dick McQuarry',
'Dick Meldonian',
'Dick Mitchell',
'Dick Morgan (2)',
'Dick Morse',
'Dick Munson',
'Dick Murphy',
'Dick Nash',
'Dick Niveson',
'Dick Noel (2)',
'Dick Oakley',
'Dick Oatts',
'Dick Paladino',
'Dick Robilotto',
'Dick Ruedebusch',
'Dick Shanahan',
'Dick Shearer',
'Dick Sherman',
'Dick Slevin',
'Dick Spencer',
'Dick Stanton',
'Dick Taylor',
'Dick Twardzik',
'Dick Vance',
'Dick Vennik',
'Dick Vennink',
'Dick Wellstood',
'Dick Wetmore',
'Dick Wharton',
'Dick Whitsell',
'Dick Wilkie',
'Dick Wilson',
'Dick Wright',
'Dick Zabach',
'Diego Iborra',
'Dieter Ilg',
'Dieter Kock',
'Dieter Reith',
'Dieter Scherf',
'Dillagene',
'Dillon Ober',
'Dinah Washington',
'Dinky Bingham',
'Dino Crocetti',
'Dino Saluzzi',
'Dionne Warwick',
'Dizzy Gillespie',
'Dizzy Reece',
'Django Bates',
'Django Reinhardt',
'DJ Cheese',
'Doc Cheatham',
'Doc Goldberg',
'Doc Ryker',
'Doc Severinsen',
'Dodge Terlemezian',
'Dodo Marmarosa',
'Doles Dickens',
'Dolly Houston',
'Dolo Coker',
'Domenic Troiano',
'Dominic Duval',
'Dominique Di Piazza',
'Dom Moio',
'Dom Um Romao',
'Don Abney',
'Donald Bailey',
'Donald Brown',
'Donald Byrd',
'Donald Cole',
'Donald Corrado',
'Donald Doane',
'Donald Edwards',
'Donald Garrett',
'Donald Harrison',
'Donald McDonald',
'Donald McKyre',
'Donald Smith',
'Donald T. Carson',
'Don Alias',
'Don Aliquo',
'Don Arnone',
'Don Ashworth',
'Don Bagley',
'Don Baldwin',
'Don Boyd',
'Don Braden',
'Don Brassfield',
'Don Burns',
'Don Butterfield',
'Don Byas',
'Don Byron',
'Don Carone',
'Don Carter',
'Don Cherry',
'Don Christlieb',
'Don Clark (5)',
'Don Darcy',
'Don Davidson',
'Don Dennis',
'Don Donaldson',
'Don Elliott',
'Don Ellis',
'Don Englert',
'Don Ewell',
'Don Fagerquist',
'Don Ferrara',
'Don Friedman',
'Don Frye',
'Don Gardner',
'Don Gardner (2)',
'Don Gilliand',
'Don Goldie',
'Don Grolnick',
'Don Hill (5)',
'Don Honeywill',
'Don Jacoby',
'Don Kelly',
'Don Kirkpatrick (2)',
'Don Lamond',
'Don Lanphere',
'Don Littleton',
'Don Lodice',
'Don Lusher',
'Don McCook',
'Don McGinnis',
'Don Melka',
'Don Menza',
'Don Michaels',
'Don Mikkelsen',
'Don Mohr',
'Don Moore',
'Don Murray (2)',
'Donn Trenner',
'Donny Hathaway',
'Donny McCaslin',
'Donovan Mixon',
'Don Owens',
'Don Paladino',
'Don Pate',
'Don Payne',
'Don Prell',
'Don Preston',
'Don Pullen',
'Don Rader',
'Don Raffell',
'Don Redman',
'Don Reed (2)',
'Don Rendell',
'Don Ruppersberg',
'Don Sebesky',
'Don Seidel',
'Don Shelton (2)',
'Don Sickler',
'Don Slaughter',
'Don Smith (6)',
'Don Stewart (3)',
'Don Stratton',
'Don \'Sugarcane\' Harris',
'Don Switzer',
'Don Thompson (2)',
'Don Van Vliet',
'Don Waldrop',
'Don Watt',
'Don Young (3)',
'Dorothy Reid',
'Dottie Grae',
'Doubraire',
'Doug Allen',
'Doug Hammond',
'Doug Harris',
'Doug Inman',
'Doug Kirkham',
'Douglas Ewart',
'Doug Macdonald',
'Doug Mathews (2)',
'Doug Mettome',
'Doug Miller',
'Doug Norwine',
'Doug Parker',
'Doug Purviance',
'Doug Raney',
'Doug Rauch',
'Doug Sides',
'Doug Watkins',
'Doug Weiss',
'Drew Gress',
'Drew Page',
'Drew Salperto',
'D. Sharpe',
'Dud Harvey',
'Dudley Brooks',
'Dudley Moore',
'Duduka Da Fonseca',
'Dudu Pukwana',
'Duffy Jackson',
'Duke Ellington',
'Duke Garrette',
'Duke Jordan',
'Duke Levine',
'Duke Pearson',
'Duncan Whyte',
'Durval Ferreira',
'Dusko Goykovich',
'Dwayne Burno',
'Dwight Adams',
'Dwight Andrews',
'Dwight Carver',
'Earl Bostic',
'Earl Chapin',
'Earl Collier',
'Earl Cornwell',
'Earl Dumler',
'Earle Hagen',
'Earle Warren',
'Earl Gardner',
'Earl Griffith',
'Earl Griffiths',
'Earl Hardy',
'Earl Hines',
'Earl Klugh',
'Earl Mason',
'Earl May',
'Earl McIntyre',
'Earl Miller',
'Earl Palmer',
'Earl Sauls',
'Earl Swope',
'Earl Thompson',
'Earl Walker',
'Earl Watkins',
'Earl Williams',
'Eberhard Weber',
'Ed Allen',
'Ed Anderson',
'Ed Armour',
'Ed Badgley',
'Ed Bennett (5)',
'Ed Bergman',
'Ed Bickert',
'Ed Blackwell',
'Ed Burke (3)',
'Ed Calle',
'Ed Cherry',
'Ed Cuffee',
'Ed Cunningham',
'Ed Diamond',
'Eddie Allen',
'Eddie Aulino',
'Eddie Barefield',
'Eddie Bernard',
'Eddie Bert',
'Eddie \'Bongo\' Brown',
'Eddie Bourne (2)',
'Eddie Busnello',
'Eddie Caine',
'Eddie Cano',
'Eddie Chamblee',
'Eddie \'Cleanhead\' Vinson',
'Eddie Coleman (4)',
'Eddie Condon',
'Eddie Costa',
'Eddie Daniels',
'Eddie De Haas',
'Eddie Dell',
'Eddie de Verteuil',
'Eddie Dougherty',
'Eddie Duran',
'Eddie Durham',
'Eddie Engels',
'Eddie Gibbs',
'Eddie Gladden',
'Eddie Gomez',
'Eddie Harris',
'Eddie Henderson',
'Eddie Heywood',
'Eddie Higgins',
'Eddie Jefferson',
'Eddie Jenkins (2)',
'Eddie Johnson',
'Eddie Jones',
'Eddie Kendricks',
'Eddie Khan',
'Eddie Lang',
'Eddie Locke',
'Eddie \'Lockjaw\' Davis',
'Eddie Mack',
'Eddie Marshall (2)',
'Eddie Mathias',
'Eddie McFadden',
'Eddie Meyers (2)',
'Eddie Miller (2)',
'Eddie Moore',
'Eddie Morgan',
'Eddie Nicholson',
'Eddie Palmieri',
'Eddie Pazant',
'Eddie Preston',
'Eddie Robinson (4)',
'Eddie Safranski',
'Eddie Sauter',
'Eddie Scalzi',
'Eddie Shomer',
'Eddie Shu',
'Eddie South',
'Eddie \'Tan Tan\' Thornton',
'Eddie Walters',
'Eddie Williams',
'Eddie Yance',
'Eddy Louiss',
'Eddy Manson',
'Eddy Martinez',
'Eddy McKimmey',
'Ede Brumund-Rüther',
'Ed Epstein (2)',
'Ed Fletcher',
'Ed Fromm',
'Edgar Bateman',
'Edgar Battle',
'Edgar Campbell (3)',
'Edgardo Sodero',
'Edgar Hayes',
'Ed Garland',
'Edgar Lustgarten (2)',
'Edgar Rosales',
'Edgar Sampson',
'Edgar Willis',
'Ed Hayes (2)',
'Ed Howard',
'Ed Iglewski',
'Edi Vitouch',
'Ed Jackson',
'Ed Kelly (3)',
'Ed Kiefer',
'Ed Kneling',
'Ed Koeling',
'Ed Kusby',
'Ed Leddy',
'Ed Lewis',
'Ed Manion',
'Ed Mann',
'Ed McKinney',
'Ed McNeil',
'Ed Mihelich',
'Edmond Hall',
'Edmond Harnie',
'Ed Mullens',
'Edmund Costanza',
'Edmund McConney',
'Ed Neumeister',
'Ed Petersen',
'Ed Powell',
'Ed Price',
'Ed Rosa',
'Ed Schuller',
'Ed Shaughnessy',
'Ed Soph',
'Ed Stang',
'Ed Testa',
'Ed Thigpen',
'Ed Timbs (2)',
'Edward Cornelius',
'Edward Inge',
'Edward Johnson (9)',
'Edward McNeil',
'Edward Moran',
'Edward Morant',
'Edward Morris',
'Edward Saldanha (Dizzy Sal)',
'Edward Warren',
'Ed Wasserman',
'Edwin Birdsong',
'Edwin Ross',
'Edwin Swayzee',
'Ed Xiques',
'Ed Zandy',
'Eef Albers',
'Efraim Logreira',
'Egil Johansen',
'Egil Kapstad',
'Egon Christmann',
'Eileen Folson',
'Eje Thelin',
'Elaine Leighton',
'Eldon Shamblin',
'Eliane Elias',
'Elias Friede',
'Eli Degibri',
'Eliot Zigmund',
'Eli Robinson',
'Elisse Cooper',
'Ellade Bandini',
'Ella Fitzgerald',
'Ellas McDaniel',
'Elliot Ingber',
'Elliot Lawrence',
'Elliott Jacoby',
'Elliott Washington',
'Ellis Bartee',
'Ellis Larkins',
'Ellis Marsalis',
'Ellis Tollin',
'Elmer Bernstein',
'Elmer Brown',
'Elmer Byers',
'Elmer Chambers',
'Elmer James',
'Elmer Smithers',
'Elmer Snowden',
'Elmer Warner',
'Elmer Whitlock',
'Elmer Williams',
'Elmo Hope',
'Elmon Wright',
'Elton Dean',
'Elvin Jones',
'Elwyn Fraser',
'Emanuel Boyd',
'Emanuel Moss',
'Embra Daylie',
'Emil Briano',
'Emil Mangelsdorff',
'Emil Mazaneo',
'Emil Richards',
'Emil Stern',
'Emil Terry',
'Emil Viklický',
'Emil Wurster',
'Emily Mitchell',
'Emmanuel Abdul-Rahim',
'Emmanuel Soudieux',
'Emmerich Weninger',
'Emmett Berry',
'Emmett Carls',
'Enrico Morello (2)',
'Enrico Pieranunzi',
'Enrico Rava',
'Enzo Pietropaoli',
'Eric Alexander',
'Eric Allen',
'Eric Burdon',
'Eric Clapton',
'Eric Dixon',
'Eric Dolphy',
'Eric Gale',
'Eric Gravatt',
'Eric Harland',
'Erich Bachträgel',
'Erich Kleinschuster',
'Erich Lederer',
'Eric Ineke',
'Eric Kloss',
'Eric Lewis',
'Eric Marienthal',
'Eric McPherson',
'Eric Miller (8)',
'Eric Miyashiro',
'Eric Reed',
'Eric Revis',
'Eric Sosinski',
'Erik Friedlander',
'Erik Moseholm',
'Erik Nordström (2)',
'Erik Van Lier',
'Erlend Krauser',
'Ermet Perry',
'Ernest Ashley',
'Ernest Booker',
'Ernest Carter',
'Ernest Elliott',
'Ernest Hill (2)',
'Ernestine Anderson',
'Ernest Karpati',
'Ernest Purce',
'Ernest Thompson (2)',
'Ernest Tozier',
'Ernest Williamson (2)',
'Ernie Caceres',
'Ernie Englund',
'Ernie Farrow',
'Ernie Felice',
'Ernie Fields',
'Ernie Furtado',
'Ernie Hayes',
'Ernie Henry',
'Ernie Hood (2)',
'Ernie Hughes',
'Ernie Marrero',
'Ernie Mauro',
'Ernie Powell',
'Ernie Royal',
'Ernie Shepard',
'Ernie Small',
'Ernie Tack',
'Ernie Watts',
'Ernie Wilkins',
'Erno Neufeld',
'Ernst Kugler',
'Ernst-Ludwig Petrowsky',
'Errol Burke',
'Errol Knowles',
'Erroll Garner',
'Erwin Böss',
'Erwin Halletz',
'Espen Rud',
'Essiet Essiet',
'Esther Phillips',
'Ethan Ardelli',
'Ethan Iverson',
'Ethel Ennis',
'Ethmer Roten',
'Etienne Mbappe',
'Etienne \'Sarane\' Ferret',
'Ettore Fioravanti',
'Eugen Cicero',
'Eugene Cook',
'Eugène d\'Hellemmes',
'Eugène Vées',
'Eugene Wright',
'Eugene Young',
'Eugenio Colombo',
'Eugen Jegorov',
'Eugen Landwehr',
'Eumir Deodato',
'Eustis Moore',
'Evan Diner',
'Evan Parker',
'Evan Vail',
'Eva Svobodová',
'Evelyn Künneke',
'Everett Barksdale',
'Everett Brown Jr.',
'Everett Levy',
'Everett Longstreth',
'Everett McDonald',
'Everett Robbins',
'Fabio Grandi',
'Fabio Morgera',
'Fabrizio Sferra',
'Falkner Evans',
'Famoudou Don Moye',
'Fat Boys',
'Fats Navarro',
'Fats Waller',
'Fatty George',
'Fausto Beccalossi',
'Fayyaz Virji',
'Felix Hanusik',
'Felix Pappalardi',
'Felix Slatkin',
'Ferdinand Nitsch',
'Ferdinand Povel',
'Ferenc Aszodi',
'Fernando Arbello',
'Fernando Saunders',
'Fernand Verstraete',
'Fern Caron',
'Fiete Wacker',
'Filippo Faguttin',
'Flavio Ambrosetti',
'Fletcher Henderson',
'Fletcher Hereford',
'Flip Phillips',
'Flip Ricard',
'Flora Purim',
'Florian Bramböck',
'Florian Esch',
'Florian Weber (2)',
'Floyd Blanton',
'Floyd Casey',
'Floyd Johnson (3)',
'Floyd Smith (2)',
'Floyd Standifer',
'Floyd Turnham',
'Foday Musa Suso',
'Ford Leary',
'Forrest Buchtel',
'Forrest Crawford',
'Francesco Cafiso',
'Francesco Cagnasso',
'Francesco Diodati',
'Frances Faye',
'Frances Wayne',
'Frances Whitby',
'Francine Aubret',
'Francine Claudel',
'Francis \'Butch\' Axsmith',
'Francisco Aguabella',
'Francisco Pozp',
'Francis Fitzpatrick',
'Francis Haynes',
'Francis Howard',
'Francis Luca',
'Francis Palmer (2)',
'Francis Polifroni',
'Francis Williams',
'Franck Gariepy',
'Franck Tortiller',
'Franco Ambrosetti',
'Franco Cerri',
'Franco D\'Andrea',
'François Guin',
'François Jeanneau',
'François Laizeau',
'François Théberge',
'Franco Manzecchi',
'Franco Tonani',
'Francy Boland',
'Frands Rifbjerg',
'Fran Heines',
'Frank Anderson (2)',
'Frank Assunto',
'Frank Basile (2)',
'Frank Beach',
'Frank Beecher',
'Frank \'Big Boy\' Goodie',
'Frank \'Big Boy\' Goudie',
'Frank Bode',
'Frank Bradley (2)',
'Frank Brieff',
'Frank Butler',
'Frank Capp',
'Frank Carlson',
'Frank Clark (4)',
'Frank Clayton',
'Frank \'Coco\' Darling',
'Frank D\'Annolfo',
'Frank Davilla',
'Frank De La Rosa',
'Frank Devito',
'Frank Elmo',
'Frank Foster',
'Frank Froeba',
'Frank Galbraith',
'Frank Gallagher (2)',
'Frank Gambale',
'Frank Gant',
'Frank Greene (2)',
'Frank Guerrero',
'Frank Haynes',
'Frank Hittner',
'Frank Hooks',
'Frank Huggins',
'Frank Humphries',
'Frankie Dunlop',
'Frankie Malabe',
'Frankie Trumbauer',
'Frankie Valli',
'Frank Ippolito',
'Frank Isola',
'Frank Jakobsen',
'Frank \'Josh\' Billings',
'Frank Kimbrough',
'Frank Lacy',
'Frank Langone',
'Frank Lee (8)',
'Franklin Skeete',
'Frank Lo Pinto',
'Frank Luther',
'Frank Mantooth',
'Frank Marshall (2)',
'Frank Mazzoli',
'Frank Minear',
'Frank Mitchell',
'Frank Morgan',
'Frank Newton',
'Frank Oberpichler',
'Frank Owens',
'Frank Paparelli',
'Frank Pasley',
'Frank Patchen',
'Frank Pinero',
'Frank Posa',
'Frank Rehak',
'Frank Ricotti',
'Frank Rosolino',
'Frank Ryerson',
'Frank Severino',
'Frank Siegfield',
'Frank Signorelli',
'Frank Sinatra',
'Frank Sinatra Jr.',
'Frank Siravo',
'Frank Socolow',
'Frank Strazzeri',
'Frank Strong',
'Frank Strozier',
'Frank Szabo',
'Frank Teschemacher',
'Frank Tesinsky',
'Frank Tiberi',
'Frank Traficante',
'Frank Tusa',
'Frank Vaccaro',
'Frank Vicari',
'Frank Victor',
'Frank Webb',
'Frank Wess',
'Frank Worrell',
'Frank Wright',
'Frank Wunsch',
'Franky Douglas',
'Frank Zappa',
'Frans Elsen',
'Frans van Luin',
'Frans Wieringa',
'František Kryka',
'František Uhlíř',
'Franz Cadek',
'Franz David',
'Franz Jackson',
'Franz Mikuliska',
'Franz Plichta',
'Franz Reinisch',
'Franz Reitter',
'Franz Simons',
'Franz Trepesch',
'Freda Payne',
'Fred Atwood',
'Fred Beckett',
'Fred Braceful',
'Fred Carter',
'Freddie Assunto',
'Freddie Bryant',
'Freddie Gambrell',
'Freddie Green',
'Freddie Hall',
'Freddie Hendrix',
'Freddie Hill',
'Freddie Hubbard',
'Freddie Martell Singers',
'Freddie Redd',
'Freddie Robinson',
'Freddie Rundquist',
'Freddie Schreiber',
'Freddie Waits',
'Freddie Webster',
'Fred Dutton',
'Freddy Culliver',
'Freddy Jenkins',
'Freddy Johnson (5)',
'Freddy Lewis',
'Freddy Wood',
'Freddy Zito',
'Frederick Buldrini',
'Frederick Schmitt',
'Frederic Rabold',
'Frederic Rzewski',
'Fred Fallensby',
'Fred Gérard',
'Fred Glickstein',
'Fred Goerner',
'Fred Greenleaf',
'Fred Griffin',
'Fred Guy',
'Fred Haller',
'Fred Hersch',
'Fred Hopkins',
'Fred Jackson',
'Fred Jackson (2)',
'Fred J. Bauer',
'Fred Katz',
'Fred Keller',
'Fred Koyen',
'Fred Leeflang',
'Fred Lenner',
'Fred Mandel',
'Fred Ohms',
'Fred Otis',
'Fred Petry (2)',
'Fred Pirtle',
'Fred Radcliffe',
'Fredrik Lundin',
'Fredrik Norén',
'Fred Robinson',
'Fred Rodriguez',
'Fred Simmons',
'Fred Simon (2)',
'Fred Simon (3)',
'Fred Stoll',
'Fred Stulce',
'Fred Van Ingen',
'Fred Waldron',
'Fred Wallisch',
'Fred Woods',
'Fredy Studer',
'Freeman Lee',
'Freya Wippich',
'Friedrich Gulda',
'Friedrich Hollaender',
'Fritz Gallosch',
'Fritz Meisinger',
'Fritz Ozmec',
'Fritz Pauer',
'Fritz Renold',
'Frode Thingnæs',
'Froebel Brigham',
'Fud Livingston',
'Fulton McGrath',
'Fumio Karashima',
'Furio Di Castri',
'Fuzzy Ferrar',
'Gabe Baltazar',
'Gabor Szabo',
'Gabriele Evangelista',
'Gabriel Gelinas',
'Gabriel Vilain',
'Gaetano Delfini',
'Gail Brockman',
'Gail Laughton',
'Gail Martin',
'Gait Preddy',
'Gale Curtis',
'Gale Robinson (2)',
'Garcia Morales',
'Gareth Nuttycombe',
'Garnett Brown',
'Garrett List',
'Garrison Fewell',
'Garry Dial',
'Garry McAdams',
'Garry Tallent',
'Garvin Bushell',
'Garvin Masseaux',
'Gary Anderson',
'Gary Anderson (4)',
'Gary Barone',
'Gary Bartz',
'Gary Brooker',
'Gary Burton',
'Gary Campbell',
'Gary Chaffee',
'Gary Chester (2)',
'Gary Coleman',
'Gary Foote',
'Gary Foster',
'Gary Freyman',
'Gary Frommer',
'Gary Grant',
'Gary Herbig',
'Gary Hobbs',
'Gary Husband',
'Gary Hypes',
'Gary Keller',
'Gary Klein (2)',
'Gary Krand',
'Gary Mapp',
'Gary Mazzaroppi',
'Gary McFarland',
'Gary Novak',
'Gary Pack',
'Gary Peacock',
'Gary Potter (2)',
'Gary Pribek',
'Gary Shaffer',
'Gary Slavo',
'Gary Smulyan',
'Gary Todd (2)',
'Gary Tole (2)',
'Gary Valente',
'Gary Versace',
'Gary Williamson (2)',
'Gary Willis',
'Gary Windo',
'Gaston Etienne',
'Gaston Léonard',
'Gaston Moat',
'Gato Barbieri',
'Gayle Dixon',
'Gayle Moran',
'Gaylord Birch',
'Geechie Smith',
'Gene Allen',
'Gene Ammons',
'Gene Anderson (2)',
'Gene Bertoncini',
'Gene Bianco',
'Gene Burkert',
'Gene Byrd',
'Gene Calderazzo',
'Gene Cherico',
'Gene Cipriano',
'Gene DiNovi',
'Gene Englund',
'Gene Esposito',
'Gene Estes',
'Gene Fields',
'Gene Gammage',
'Gene Garf',
'Gene Goe',
'Gene Harris',
'Gene Jackson',
'Gene Kinsey',
'Gene Komer',
'Gene Krupa',
'Gene Lamas',
'Gene Leman',
'Gene Norton',
'Gene Orloff',
'Gene Perla',
'Gene Phillips',
'Gene Phipps',
'Gene Porter',
'Gene Powers',
'Gene Prince',
'Gene Quill',
'Gene Ramey',
'Gene Redd',
'Gene Rodgers',
'Gene Roland',
'Gene Sargent',
'Gene Schroeder',
'Gene Sedric',
'Gene Simon',
'Gene Smith (3)',
'Gene Smookler',
'Gene Taylor',
'Gene Tettamanti',
'Gene Traxler',
'Gene Victory',
'Gene Zanoni',
'Genya Ravan',
'Geoff Goodman',
'Geoff Keezer',
'Geoff Perkins',
'Geoff Sharp',
'George Adams',
'George Arus',
'George Baker (4)',
'George Bardon',
'George Barnes',
'George Barrow',
'George Bell (2)',
'George Benson',
'George Berg',
'George Bledsoe',
'George Boehm',
'George Bohanon',
'George Bohn',
'George Bone',
'George Booker (2)',
'George Brown (4)',
'George Brunies',
'George Bujie',
'George Butcher',
'George Cables',
'George Chandler',
'George Clark (3)',
'George Clinton',
'George Coleman',
'George Colligan',
'George Davis (2)',
'George Davis (9)',
'George Defenbaugh',
'George Devens',
'George Dixon',
'George Dorsey',
'George Duke',
'George Durkin',
'George Duvivier',
'George Elrick',
'George Esposito',
'George Faye',
'George F. Hirst',
'George Freeman (2)',
'George Garzone',
'George Gibbs',
'George Goldsmith',
'George Green (21)',
'George Grossman',
'George Gruntz',
'George Handy',
'George Hanna (3)',
'George Hudson',
'George Hunt',
'George Irish',
'George Jacquemont',
'George James (2)',
'George Jeffers',
'George Jenkins',
'George Jenkins (6)',
'George Johnston',
'George Jones (5)',
'George Joyner',
'George Kast',
'George Kelly (4)',
'George Koch',
'George Koenig',
'George Koutzen',
'George Lewis',
'George Marge',
'George Marsh',
'George Masso',
'George Matthews (2)',
'George McCurn',
'George McFetridge',
'George Meyer',
'George Monte',
'George Moran',
'George Morrow',
'George Mraz',
'George Myers',
'George Nicholas (3)',
'George Ohtsuka',
'George Oldham',
'George Orendorff',
'George Parker (4)',
'George Paulson',
'George Perry (2)',
'George Probert',
'George Rabbai',
'George Ricci',
'George Robert',
'George Roberts',
'George Roumanis',
'George Russell',
'George Schwartz',
'Georges Cloud',
'Georges Delagaye',
'George Seaberg',
'George Semper',
'Georges Hadjo',
'George Shearing',
'George Signore (2)',
'George Siravo',
'Georges Paquay',
'George Stafford',
'George Stevenson',
'George Syran',
'George Taitt',
'George Theiss',
'George Thomas',
'George Thow',
'George Tucker',
'George Van Eps',
'George Wallington',
'George Walters (2)',
'George Washington',
'George Weidler',
'George Wein',
'George Wendt',
'George Wettling',
'George Williams (2)',
'George Young (2)',
'George Zonce',
'Georgie Auld',
'Georgie Fame',
'Georg Riedel',
'Georg Wadenius',
'Gerald Chamberlain',
'Gerald Cleaver',
'Gerald Fried',
'Gerald Goff',
'Gerald Hayes',
'Gerald Joyce',
'Gerald Levert',
'Gerald Sanfino',
'Gerald Valentine (2)',
'Gerald Veasley',
'Gerald Vinci',
'Gerald Wiggins',
'Gerald Wilson',
'Gérard Gustin',
'Gérard Lévêque',
'Gérard Pochonet',
'Gerd Breuer',
'Gerd Dudek',
'Gerd Lachmann',
'Gerhard König (2)',
'Geri Allen',
'Germaine Sablon',
'Gerrie Van Der Klei',
'Gerry Brown',
'Gerryck King',
'Gerry Eastman',
'Gerry Geiger',
'Gerry Gibbs',
'Gerry Hemingway',
'Gerry Jochim',
'Gerry LaFurn',
'Gerry Lamy',
'Gerry Moore',
'Gerry Mulligan',
'Gerry Niewood',
'Gerson Oberstein',
'Gert Rostock',
'G.E. Smith',
'Giampaolo Casati',
'Giampiero Prina',
'Giancarlo Schiaffini',
'Giani Lincan',
'Gianluca Petrella',
'Gianludovico Carmenati',
'Gianmarco Lanza',
'Gianni Basso',
'Gianni Bedori',
'Gianni Cazzola',
'Gib Wallace',
'Gideon Honore',
'Gigi Grata',
'Gigi Gryce',
'Gijs Hendriks',
'Gil Barrios',
'Gilbert Rovère',
'Gil Bowers',
'Gil Coggins',
'Gil Cuppini',
'Gilda Macon',
'Gilda Maiken',
'Gildo Mahones',
'Gil Evans',
'Gil Falco',
'Gil Fuller',
'Gil Goldstein',
'Gilles Naturel',
'Gil Mellé',
'Gil Rathel',
'Gil Rodin',
'Gil Scott-Heron',
'Ginette Garcin',
'Ginger Baker',
'Ginnie Powell',
'Ginny Simms',
'Gino Bozzacco',
'Gino Sambuco',
'Giorgio Gaslini',
'Giovanni Tommaso',
'Gish Gilbertson',
'Giuseppi Logan',
'Gladys Madden',
'Glauco Masetti',
'Glen Burtnick',
'Glen Campbell',
'Glenn Davis',
'Glenn Drewes',
'Glenn Hardman',
'Glenn Herzer',
'Glenn Miller',
'Glenn S. Jeffrey',
'Glenn Stuart',
'Glenn Zottola',
'Gloria Agostini',
'Gloria Coleman',
'Goldie Zelkowitz',
'Gonzalo Rubalcaba',
'Gordon Barrentine',
'Gordon Beck',
'Gordon Boswell',
'Gordon Brisker',
'Gordon Edwards',
'Gordon Goodwin',
'Gordon Jenkins',
'Gordon Johnson',
'Gordon Polk',
'Gordon Schoneberg',
'Gordon Thomas',
'Gosady McGee',
'Gösta Theselius',
'Grachan Moncur',
'Grachan Moncur III',
'Grady Tate',
'Graham Bond',
'Graham Ellis',
'Graham Haynes',
'Graham Lear',
'Graham Young',
'Grant Green',
'Granville T. Hogan',
'Grassella Oliphant',
'Gray Sargent',
'Greely Walton',
'Greg Abate',
'Greg Bandy',
'Greg Bowen',
'Greg Errico',
'Gregg Field',
'Greg Gilbert (6)',
'Greg Gisbert',
'Gregg Rolie',
'Greg Hopkins',
'Greg Lake',
'Greg Leisz',
'Greg Maker',
'Greg Marciel',
'Greg Marvin',
'Greg Metcalf',
'Greg Millar',
'Gregor Josephs',
'Gregory Bemko',
'Gregory Herbert',
'Gregory Hutchinson',
'Greg Osby',
'Greg Phillips',
'Greg Smith (3)',
'Greg Tardy',
'Greg Walker',
'Greig McRitchie',
'Grover Mitchell',
'Grover Washington Jr.',
'Guido Mozzato',
'Guilherme Franco',
'Guillaume Naturel',
'Gunnar Johnson',
'Gunnar Plümer',
'Günter Christmann',
'Gunter Hampel',
'Günter Lenz',
'Günter Meier',
'Günter Platzek',
'Gunther Schuller',
'Gus Aiken',
'Gus Arnheim',
'Gus Bivona',
'Gus Chappell',
'Gus Deloof',
'Gus Dixon',
'Gus Evans',
'Gus Gustafson',
'Gus Johnson',
'Gus Mancuso',
'Gus Mas',
'Gus McReynolds',
'Gus Nemeth',
'Gustav Brom Jr.',
'Gustavo Maas',
'Gust William Tsilis',
'Gusztáv Csík',
'Guttorm Guttormsen',
'Guy Barker',
'Guy Erlandsen',
'Guy Hayat',
'Guy Kelly',
'Guy Paquinet',
'Guy Pedersen',
'Guy Scalise',
'Gwilym Simcock',
'Hadley Caliman',
'Haig Eshow',
'Haig Stephens',
'Hajo Lange',
'Håkan Nyqvist',
'Hal Blaine',
'Hal Crook',
'Haleem Rasheed',
'Hale Rood (2)',
'Hal Espinosa',
'Hal Galper',
'Hal Gordon',
'Hal Korn',
'Hall Overton',
'Hal McKusick',
'Hal Mitchell',
'Hal Posey',
'Hal Roberts',
'Hal Schaefer',
'Hal Smith (4)',
'Hal Stein',
'Hamid Drake',
'Hamiet Bluiett',
'Hammond Russum',
'Hampton Hawes',
'Hank Crawford',
'Hank D\'Amico',
'Hank Freeman',
'Hank Garland',
'Hank Jones',
'Hank Kmen',
'Hank Mobley',
'Hank Wayland',
'Hannibal Marvin Peterson',
'Hans Backenroth',
'Hans Ehrlinger',
'Hans Fiala',
'Hans Hammerschmid',
'Hans Koller',
'Hans Kresse',
'Hans Last',
'Hans Löw (2)',
'Hans Mertl',
'Hans Rettenbacher',
'Hans Salomon',
'Hans Thomas',
'Hans Ulrik',
'Hans Van Oosterhout',
'Happy Caldwell',
'Harald Ende',
'Harold Ashby',
'Harold Ayres',
'Harold Baker',
'Harold Bemko',
'Harold Bruce',
'Harold Clark (3)',
'Harold Cooper',
'Harold Danko',
'Harold \'Doc\' West',
'Harold Feldman',
'Harold Garrett',
'Harold Gaylor',
'Harold Granowsky',
'Harold Hahn',
'Harold Herzon',
'Harold Johnson (2)',
'Harold Jones',
'Harold Land Jr.',
'Harold Land',
'Harold Lawson',
'Harold Lewis',
'Harold Lieberman (2)',
'Harold Mabern',
'Harold McDonald',
'Harold Melvin And The Blue Notes',
'Harold Minerve',
'Harold Moe',
'Harold Ousley',
'Harold Scott',
'Harold Sorin',
'Harold Sturr',
'Harold Vick',
'Harold Wegbreit',
'Harold White',
'Harper Cosby',
'Harri Sjöström',
'Harrison Bankhead',
'Harris Simon',
'Harry Allen (2)',
'Harry Anderson',
'Harry Babasin',
'Harry Barris',
'Harry Barth',
'Harry Beckett',
'Harry Belafonte',
'Harry Betts',
'Harry Biss',
'Harry Blostein',
'Harry Bluestone',
'Harry Brainard',
'Harry Brainerd',
'Harry Brooks (7)',
'Harry Carney',
'Harry DiVito',
'Harry Edison',
'Harry Emmery',
'Harry Feldman',
'Harry Ferguson (2)',
'Harry Filkin',
'Harry Forbes (2)',
'Harry Geller',
'Harry Goldfield',
'Harry Goodman',
'Harry Grey',
'Harry Grube',
'Harry Hall',
'Harry Hull',
'Harry Hyams',
'Harry Jaeger',
'Harry James (2)',
'Harry Jaworski',
'Harry Johnson (6)',
'Harry Katzman',
'Harry Klee',
'Harry Kleintank',
'Harry Lawson',
'Harry Leahey',
'Harry Lookofsky',
'Harry Melnikoff',
'Harry Palsinger',
'Harry \'Pee Wee\' Jackson',
'Harry Polk',
'Harry Rodgers',
'Harry Samp',
'Harry Schuchman',
'Harry Schuman',
'Harry Sheppard',
'Harry Sloan',
'Harry Sokal',
'Harry Sosnik',
'Harry Struble',
'Harry Terrill',
'Harry Van Oven',
'Harry Verbeke',
'Harry Whitaker',
'Harry White',
'Hart Smith',
'Harvey Boone',
'Harvey Brooks (2)',
'Harvey Cell',
'Harvey Coonin',
'Harvey Leonard',
'Harvey Mason',
'Harvey Newmark',
'Harvey Phillips',
'Harvey Sarch',
'Harvey Shapiro',
'Harvey Wainapel',
'Harvie Swartz',
'Hasaan',
'Hassan Shakur',
'Hayden Causey',
'Hayes Alvis',
'Hayes Pillars',
'Haywood Henry',
'Hazel Scott',
'Hector Lavoe',
'Hector Zarzuela',
'Heiner Wiberny',
'Heinie Beau',
'Heinrich Alfing',
'Hein Van de Geyn',
'Heinz Bigler',
'Heinz Grah',
'Heinz Habermann',
'Heinz Hruza',
'Heinz Kitschenberg',
'Heinz Kretzschmar',
'Heinz Neubrand',
'Heinz Niemeyer',
'Heinz Pohle',
'Heinz Sauer',
'Heinz Schultze',
'Heinz von Hermann',
'Heiri Känzig',
'Helen Forrest',
'Helen Humes',
'Helen Ward',
'Helmut Brandt',
'Helmuth Franke',
'Henderson Chambers',
'Henk Haverhoek',
'Henri Renaud',
'Henri Tallourd',
'Henri Texier',
'Henry Adler',
'Henry Boozier',
'Henry Bridges',
'Henry Busse',
'Henry Coker',
'Henry Glover',
'Henry Goodwin',
'Henry Greenwald',
'Henry Grimes',
'Henry Hicks',
'Henry Jones',
'Henry Lange',
'Henry Levine',
'Henry Lowther',
'Henry Mancini',
'Henry Prince',
'Henry \'Red\' Allen',
'Henry R. Hines',
'Henry Rowland',
'Henry Salgado',
'Henry Saltman',
'Henry Sigismonti',
'Henry Southall',
'Henry Stern',
'Henry Threadgill',
'Henry Tucker Green',
'Henry Vestine',
'Henry Wells',
'Herb Barman',
'Herb Bass',
'Herb Besson',
'Herb Bushler',
'Herb Ellis',
'Herbert Bornhold',
'Herbert Brown',
'Herbert Cowans',
'Herbert Fiala',
'Herbert Joos',
'Herbert Offner',
'Herbert Reisinger',
'Herbert Solomon',
'Herbert Witz',
'Herb Fleming',
'Herb Geller',
'Herb Gordy (2)',
'Herb Hall',
'Herb Harper',
'Herbie Fields',
'Herbie Flowers',
'Herbie Goins',
'Herbie Hancock',
'Herbie Haymer',
'Herbie Jones',
'Herbie Lewis',
'Herbie Lovelle',
'Herbie Nichols',
'Herbie Philips',
'Herb Jeffries',
'Herb Lorden',
'Herb Mickman',
'Herb Pomeroy',
'Herb Quigley',
'Herb Randel',
'Herb Robertson',
'Herb Steed',
'Herb Steward',
'Herb Tompkins',
'Herb Winfield',
'Heribert Thusek',
'Herlin Riley',
'Herman Bell',
'Herman Clebanoff',
'Herman Foster',
'Herman Green',
'Herman Gunkler',
'Herman Lebow',
'Herman Mitchell',
'Hermann Mutschler',
'Herman Schoonderwalt',
'Herman Wright',
'Hernifan Majeed',
'Herschel Brassfield',
'Herschel Burke Gilbert',
'Herschel Evans',
'Hersh Hamel',
'Hervé Meschinet',
'Heshima Mark Williams',
'Hilton Jefferson',
'Hilton Ruiz',
'Hiromi Uehara',
'Hiroshi Fukumura',
'Hiroshi Kagawa',
'Hiroshi Munekiyo',
'Hiroshi Murakami',
'Hoagy Carmichael',
'Hobart Dotson',
'Hod O\'Brien',
'Hollis Bridwell',
'Holly Oas',
'Homer Hobson',
'Horace Diaz',
'Horacee Arnold',
'Horace Henderson',
'Horace Parlan',
'Horace Rollins',
'Horace Silver',
'Horace Tapscott',
'Horacio Fumero',
'Horst Mühlbradt',
'Hotep Idris Galeta',
'Hot Lips Page',
'Houghton Peterson',
'Houston Person',
'Howard Collins',
'Howard Davies (2)',
'Howard Davis (8)',
'Howard Etherton',
'Howard Johnson (3)',
'Howard Johnson (6)',
'Howard Jones',
'Howard Kaylan',
'Howard King',
'Howard McGhee',
'Howard McRae',
'Howard Rego',
'Howard Roberts',
'Howard Rumsey',
'Howard Scott (2)',
'Howard Scott (5)',
'Howard Shore',
'Howard Smith (4)',
'Howard Terry',
'Howard Williams (4)',
'Howdy Quicksell',
'Howie Mann',
'Howie Smith',
'Hoyt Bohannon',
'Hubert Eaves III',
'Hubert Fol',
'Hubert Laws',
'Hubert Rostaing',
'Huey Lewis',
'Huey Long',
'Hugh Hopper',
'Hugh Lawson',
'Hugh McCracken',
'Hugh Ragin',
'Hugh Steinmetz',
'Hugh Walker',
'Hugo Lowenstern',
'Hugo Montenegro',
'Hugo Rasmussen',
'Humberto Canto',
'Humberto Morales',
'Hy Mandel',
'Hymie Schertzer',
'Hymie Wolfson',
'Hy White',
'Iain Ballamy',
'Iain Dixon',
'Ian Anderson',
'Ian Carr',
'Iancsy Körössy',
'Ian McDougall',
'Ian Underwood',
'Idrees Sulieman',
'Idris Muhammad',
'Iggy Shevak',
'Ignacio Berroa',
'Igor Berukshtis',
'Ike Carpenter',
'Ike Covington',
'Ike Isaacs (2)',
'Ike Perkins (2)',
'Ike Quebec',
'Ike Turner',
'Ike Willis',
'Ikuo Sakurai',
'Ildefonso Sanchez',
'Illinois Jacquet',
'Imogene Lynn',
'Ingfried Hoffmann',
'Ingo Lahme',
'Ira Coleman',
'Ira Nepus',
'Ira Pettiford',
'Ira Schulman',
'Ira Sullivan',
'Ira Westley',
'Irene Aebi',
'Irene Chanter',
'Irene Daye',
'Irv Cottler',
'Irv Gordon',
'Irving Ashby',
'Irving Brodsky',
'Irving Brown (2)',
'Irving Fazola',
'Irving Garner',
'Irving Geller',
'Irving Goodman',
'Irving Joseph',
'Irving Mills',
'Irving Randolph',
'Irv Kluger',
'Irv Lang',
'Irv Lewis',
'Irv Roth',
'Irv Stokes',
'Irwin Abrams',
'Irwin Berken',
'Isaac Hayes',
'Isaac Livingstone',
'Isaac Smith',
'Isadore Myers',
'Isao Suzuki',
'Isham Jones',
'Ish Montgomery',
'Isidore Bassard',
'Isla Eckinger',
'Ismael Miranda',
'Isoo Fukui',
'Israel Crosby',
'Israel Dorn',
'Issa Pointer',
'Itzie Riskin',
'Ivan Gambini',
'Ivan Lopez (4)',
'Ivan Smažík',
'Ivar Jaminez',
'Ivie Anderson',
'Izzy Friedman',
'Izzy Sanabria',
'Jabbo Smith',
'Jac Assunto',
'Jack Aiken',
'Jack Arnold',
'Jack Berg',
'Jack Bland',
'Jack Bohannon',
'Jack Bruce',
'Jack Burger',
'Jack Carmen',
'Jack Cathcart',
'Jack Caudill',
'Jack Cave',
'Jack Chapman',
'Jack Cooley',
'Jack Costanzo',
'Jack DeJohnette',
'Jack Del Rio',
'Jack Diéval',
'Jack Dulong',
'Jack Dumont',
'Jack Fallon',
'Jack Feierman',
'Jack Ferrier',
'Jack Franklin',
'Jack Fulton',
'Jack Furlong (2)',
'Jack Gale',
'Jack Gardner',
'Jack Goldie',
'Jack Gootkin',
'Jack Green (4)',
'Jack Hansen',
'Jack Henderson',
'Jack H. Laubach',
'Jack Holliday',
'Jackie Brenston',
'Jackie Cain',
'Jackie Davis',
'Jackie Dougan',
'Jackie Fields',
'Jackie Jackson',
'Jackie Kelso',
'Jackie McLean',
'Jackie Mills',
'Jack Jarvis',
'Jack Jeffers',
'Jack Jenney',
'Jack Kelleher',
'Jack Lacey',
'Jack Layton',
'Jack Lee (3)',
'Jack LeMaire',
'Jack Lesberg',
'Jack Llewelyn',
'Jack Marshall',
'Jack Mayhew',
'Jack McVea',
'Jack Millman',
'Jack Mills (2)',
'Jack Montrose',
'Jack Mootz',
'Jack Nimitz',
'Jack Noren',
'Jack O\'Keefe',
'Jack Ordean',
'Jack Palmer',
'Jack Parker',
'Jack Perciful',
'Jack Pettis',
'Jack Platt',
'Jack Poster',
'Jack Purvis',
'Jack Raines',
'Jack Ranelli',
'Jack Russin',
'Jack Ryan',
'Jack Satterfield',
'Jack Scarda',
'Jack Schaeffer',
'Jack Schwartz',
'Jack Sewing',
'Jack Sheldon',
'Jack Six',
'Jackson Browne',
'Jackson Krall',
'Jackson Wiley',
'Jack Sperling',
'Jack Spurlock',
'Jack Stacey',
'Jack Stevens (4)',
'Jack Stuckey',
'Jack Teagarden',
'Jack Thirwell',
'Jack Thompson (10)',
'Jack Walrath',
'Jack Washington',
'Jack Watson (6)',
'Jack Weeks',
'Jack Wertheimer',
'Jack Wilkins',
'Jack Wilson',
'Jack Wulfe',
'Jacky Bambou',
'Jacky Terrasson',
'Jack Zimmerman (2)',
'Jacob Garchik',
'Jacob Karlzon',
'Jacob Krachmalnick',
'Jaco Pastorius',
'Jacques Bolognesi',
'Jacques Gasselin',
'Jacques Hélian',
'Jacques Hendrix',
'Jacques Hess',
'Jacques Martinon',
'Jacques Pelzer',
'Jacques Schols',
'Jacques Thollot',
'Jaime Austria',
'Jake Hanna',
'Jake Koven',
'Jaki Byard',
'Jakob Bro',
'Jakob Dinesen',
'James Black',
'James Bossert',
'James Cammack',
'James Cannady',
'James Carroll (4)',
'James Carter (3)',
'James Chambers (2)',
'James Chirillo',
'James Clay',
'James Craig',
'James Dahl',
'James Decker',
'James D. King',
'James Fei',
'James Forman Jr.',
'James Gannon',
'James Gemus',
'James Genus',
'James Getzoff',
'James Grimes (2)',
'James Haughton',
'James Henderson (4)',
'James Imberman',
'James Ingram',
'James Jetter',
'James \'Jiggs\' Noble',
'James Kartchner',
'James Lamare',
'James Martin (13)',
'James McAllister',
'James Moody',
'James Moore (17)',
'James Morrison',
'James Mtume',
'James Newton (2)',
'James Ola Folami',
'James Politis',
'James Price Johnson',
'James Putnam',
'James Robinson (16)',
'James Rupp',
'James Sands',
'James Schenck',
'James Scott (2)',
'James Simmons',
'James Singleton',
'James Spaulding',
'James Stinnett',
'James Tolliver',
'James Towsey',
'James Troutman',
'James Vincent',
'James Whitney',
'James William Guercio',
'James Williams (2)',
'James Zito',
'James Zollar',
'Jamey Haddad',
'Jamie Lidderdale',
'Jamil Nasser',
'Jan Allan',
'Jan Arnet',
'Jane Bunnett',
'Jane Getter',
'Jane Getz',
'Janet Ferguson',
'Janet Putnam',
'Janet Wright',
'Jan Garbarek',
'Jan Hammer',
'Janice Robinson (2)',
'Jan Johansson',
'Jan Kohlin',
'Jan Konopásek',
'Jan Oosthof',
'Janot Morales',
'Janse H. Vincent',
'Jan Stewart (3)',
'Jarmo Hoogendijk',
'Jaromír Helešic',
'Jaromír Hnilička',
'Jaromír Honzák',
'Jason Brown (16)',
'Jason Carder',
'Jason Jackson (2)',
'Jason Marsalis',
'Jason Moran',
'Jason Palmer (2)',
'Jason Trammell',
'Jasper Van\'t Hof',
'Javier Colina',
'Javon Jackson',
'Jay Anderson',
'Jay Ashby',
'Jay Cameron',
'Jay Corre',
'Jay Dennis',
'Jay Hoggard',
'Jay Kelliher',
'Jay Leonhart',
'Jay McAllister',
'Jay McShann',
'Jay Migliori',
'Jay Peters',
'Jay Rosen (2)',
'Jay Saunders',
'Jay Shanman',
'Jay Silva',
'Jay Sollenberger',
'Jay Thomas (3)',
'Jay Watson (2)',
'J. Billy VerPlanck',
'J.C. Heard',
'J.C. Higginbotham',
'J.C. Moses',
'J.C. Williams',
'J.D. Allen',
'Jean Baissat',
'Jean-Baptiste \'Mac Kac\' Reilles',
'Jean Bonal',
'Jean-Claude Briodin',
'Jean-Claude Fohrenbach',
'Jean-Claude Pelletier',
'Jean-Claude Petit',
'Jean-Claude Verstraete',
'Jean Gambini',
'Jean Goldkette',
'Jean Hawker',
'Jean-Jacques Avenel',
'Jean-Louis Chautemps',
'Jean-Louis Rassinfosse',
'Jean-Louis Tristan',
'Jean-Louis Viale',
'Jean-Luc Ponty',
'Jean Magnien',
'Jean Marco',
'Jean-Marie Ecay',
'Jean-Marie Ingrand',
'Jean \'Matlo\' Ferret',
'Jean-Michel Pilc',
'Jean-My Truong',
'Jeanne Lee',
'Jean-Paul Bourelly',
'Jean-Paul Mengeon',
'Jean-Philippe Viret',
'Jean-Pierre Arnaud (3)',
'Jean-Pierre Solves',
'Jean Storne',
'Jean Toussaint',
'Jean Turner',
'Jean Warland',
'Jeb Patton',
'Jed Levy',
'Jeff Andrews',
'Jeff Ballard',
'Jeff Baxter',
'Jeff Brillinger',
'Jeff Carney (2)',
'Jeff Carswell',
'Jeff Castleman',
'Jeff Chambers (3)',
'Jeff Clayton (3)',
'Jeff Clyne',
'Jeff Cressman',
'Jeff Daniel (2)',
'Jeff Davis (3)',
'Jeff Denson',
'Jeff Fuller',
'Jeff Gardner (3)',
'Jeff Hamilton',
'Jeff Hirshfield',
'Jeff Johnson (8)',
'Jeff Lane',
'Jeff Mironov',
'Jeff Morton',
'Jeff Pevar',
'Jeffrey Hyman',
'Jeffrey Osborne',
'Jeff Simmons',
'Jeff Sipe',
'Jeff Stockham',
'Jeff Stout',
'Jeff \'Tain\' Watts',
'Jeff Uusitalo',
'Jeff Williams',
'Jef Gilson',
'Jemeel Moondoc',
'Jennifer Hall (2)',
'Jennifer Lee (11)',
'Jens Winther',
'Jeremy Pelt',
'Jeremy Steig',
'Jeremy Udden',
'Jérôme Bourdellon',
'Jerome Darr',
'Jerome Harris',
'Jerome Jennings',
'Jerome Kessler',
'Jerome Pasquall',
'Jerome Reisler',
'Jerome Richardson',
'Jerry Bergonzi',
'Jerry Blake',
'Jerry Coker',
'Jerry Collins (2)',
'Jerry Colonna',
'Jerry Cox (4)',
'Jerry DiMuzio',
'Jerry Dodgion',
'Jerry Elliott',
'Jerry Friedman',
'Jerry Fuller (2)',
'Jerry Fuller (3)',
'Jerry Gonzalez',
'Jerry Goodman',
'Jerry Gray',
'Jerry Hahn',
'Jerry Hurwitz',
'Jerry Jerome',
'Jerry Johnson (3)',
'Jerry Kail',
'Jerry Keys (2)',
'Jerry Lloyd (2)',
'Jerry McKenzie',
'Jerry Mengo',
'Jerry Neary',
'Jerry Peel',
'Jerry Pinter',
'Jerry Potter',
'Jerry Rosa',
'Jerry Segal',
'Jerry Smith (2)',
'Jerry Stephan',
'Jerry Therkeld',
'Jerry Thirkeld',
'Jerry Tyree',
'Jerry Underwood',
'Jerry Van Rooyen',
'Jerry Weldon',
'Jerry Williams',
'Jerry Winner',
'Jesper Lundgaard',
'Jesper Thilo',
'Jesse Davis (3)',
'Jesse Drakes',
'Jesse Ehrlich',
'Jesse Heath',
'Jesse Kilpatrick',
'Jesse Miller',
'Jesse Powell (2)',
'Jesse Price',
'Jesse Ralph',
'Jesse Whitaker',
'Jess Stacy',
'Jethro Burns',
'Jewell Brown',
'Jewell Grant',
'J.-F. Jenny-Clark',
'Jie-Bing Chen',
'Jiggs Whigham',
'Jilla Webb',
'Jim Amlotte',
'Jim Amos',
'Jim Atlas',
'Jim Beard',
'Jim Bonebrake',
'Jim Bossy',
'Jim Buck',
'Jim Buck Jr',
'Jim Buffington',
'Jim Burtch',
'Jim Castaldi',
'Jim Cathcart (2)',
'Jim Chapin',
'Jim Cox',
'Jim \'Daddy\' Walker',
'Jim Daniels',
'Jim Falzone (2)',
'Jim Fielder',
'Jim Foy',
'Jim Gailloreto',
'Jim Galloway',
'Jim Hacker',
'Jim Hall',
'Jim Hayes',
'Jim Haynes (2)',
'Jim Hewitt (3)',
'Jim Holmes (2)',
'Jim Hughart',
'Jim Huntzinger',
'Jimi Jamison',
'Jim Massoth',
'Jim McGhee',
'Jim McNeely',
'Jimmie Nicol',
'Jimmie Noone',
'Jimmie Smith',
'Jimmie Vaughan',
'Jim Monaghan (3)',
'Jimmy Abato',
'Jimmy Allen (2)',
'Jimmy Anderson (13)',
'Jimmy Archey',
'Jimmy Bennett (5)',
'Jimmy Blake',
'Jimmy Blanton',
'Jimmy Bond',
'Jimmy Boyd (2)',
'Jimmy Bunn',
'Jimmy Butts',
'Jimmy Campbell',
'Jimmy Campbell (6)',
'Jimmy Carl Black',
'Jimmy Cathcart',
'Jimmy Cleveland',
'Jimmy Cobb',
'Jimmy Coe',
'Jimmy Cook',
'Jimmy Crawford',
'Jimmy Delgado',
'Jimmy Deuchar',
'Jimmy Dorsey',
'Jimmy Ford (6)',
'Jimmy Forrest',
'Jimmy Garrison',
'Jimmy Gemus',
'Jimmy Giuffre',
'Jimmy Gloomy',
'Jimmy Golden',
'Jimmy Gourley',
'Jimmy Grissom',
'Jimmy Guinn',
'Jimmy Halperin',
'Jimmy Hamilton',
'Jimmy Hamilton (5)',
'Jimmy Harrison',
'Jimmy Haslip',
'Jimmy Heath',
'Jimmy Helms',
'Jimmy Henderson',
'Jimmy Herring',
'Jimmy Hopps',
'Jimmy Horvath',
'Jimmy Hoskins',
'Jimmy Johnson (2)',
'Jimmy Johnson (7)',
'Jimmy Jones (3)',
'Jimmy Knepper',
'Jimmy Lewis (2)',
'Jimmy Lovelace',
'Jimmy Lyon (2)',
'Jimmy Lyons (2)',
'Jimmy Madison',
'Jimmy Maxwell',
'Jimmy McGriff',
'Jimmy McLin',
'Jimmy McPartland',
'Jimmy Millazzo',
'Jimmy Miller (5)',
'Jimmy Molneiri',
'Jimmy Mosher',
'Jimmy Mundy',
'Jimmy Nottingham',
'Jimmy Oliver (3)',
'Jimmy Owens',
'Jimmy Padget',
'Jimmy Page',
'Jimmy Powell',
'Jimmy Pratt',
'Jimmy Priddy',
'Jimmy Prince',
'Jimmy Pupa',
'Jimmy Raney',
'Jimmy Robinson (8)',
'Jimmy Rowles',
'Jimmy Rowser',
'Jimmy Rushing',
'Jimmy Salko',
'Jimmy Saunders',
'Jimmy Saunders (5)',
'Jimmy Scott',
'Jimmy Sedler',
'Jimmy Sherman',
'Jimmy Shirley',
'Jimmy Simms',
'Jimmy Skidmore',
'Jimmy Skiles',
'Jimmy Smith',
'Jimmy Smith (5)',
'Jimmy Strong',
'Jimmy Wallace (2)',
'Jimmy Welch (2)',
'Jimmy Welch (4)',
'Jimmy Wilkins',
'Jimmy Wisner',
'Jimmy Woode',
'Jimmy Woods',
'Jimmy Wormick',
'Jimmy Wyble',
'Jim Oatts',
'Jim Odgren',
'Jim Pepper',
'Jim Plank',
'Jim Pons',
'Jim Powell',
'Jim Pryor',
'Jim Pugh',
'Jim Rattigan',
'Jim Richardson (3)',
'Jim Rotondi',
'Jim Seeley',
'Jim Snidero',
'Jim Stutz',
'Jim Thomas (11)',
'Jim Timmens',
'Jim Trimble',
'Jim Tyler',
'Jim Weaver (3)',
'Jim White (2)',
'Jiří Stivín',
'Jiří Tomek',
'J.J. Johnson',
'J.J. Stelmach',
'Joachim Kühn',
'Joakim Milder',
'Joan Elardo',
'Joan Logue',
'Joanne Brackeen',
'Joanne Caldwell McNabb',
'Joanne Stone',
'Jo Charrier',
'Jock Ellis',
'Jodie Christian',
'Joe Aglora',
'Joe Aguanno',
'Joe Ascione',
'Joe Bailey',
'Joe Barati',
'Joe Barbary',
'Joe Bauer (2)',
'Joe Beck',
'Joe Benjamin',
'Joe Bishop',
'Joe Bonner',
'Joe Borghetti',
'Joe Britton',
'Joe Burnett',
'Joe Bushkin',
'Joe Cadena',
'Joe Caiani',
'Joe Calloway',
'Joe Calo',
'Joe Carroll',
'Joe Casano',
'Joe Castro',
'Joe Chambers',
'Joe Ciavardone',
'Joe Cinderella',
'Joe Clarvadone',
'Joe Comfort',
'Joe Cornell',
'Joe Dale',
'Joe Daley',
'Joe Darensbourg',
'Joe Denton',
'Joe Dixon',
'Joe Dodge',
'Joe Dolny',
'Joe Dukes',
'Joe Durham',
'Joe Eldridge',
'Joe Ellis',
'Joe Epps',
'Joe Estren',
'Joe Evans (3)',
'Joe Farnsworth',
'Joe Farrell',
'Joe Ferdinando',
'Joe Ferrall',
'Joe Ferrante',
'Joe Fine (2)',
'Joe Ford',
'Joe Gallardo',
'Joe Gallivan',
'Joe Gardner',
'Joe Garland',
'Joe Gayles',
'Joe Giuffreda',
'Joe Gordon',
'Joe Grauso',
'Joe Guy',
'Joe Hambrick',
'Joe Harris (2)',
'Joe Harris (3)',
'Joe Henderson',
'Joe Hinton (2)',
'Joe Hostetter',
'Joe Howard',
'Joe Hunt',
'Joe Johnson (8)',
'Joe Kennedy',
'Joe Keyes',
'Joe Knight (4)',
'Joe Koch',
'Joe Kretchner',
'Joe LaBarbera',
'Joe Laconi',
'Joe Lano',
'Joel DiBartolo',
'Joel Forbes',
'Joel Hamilton (5)',
'Joe Lipman',
'Joel Kaye',
'Joel Krauss',
'Joe Locke',
'Joe Lopes (2)',
'Joe Lovano',
'Joel Peskin',
'Joel Weiskopf',
'Joe MacDonald (2)',
'Joe Magnarelli',
'Joe Maini',
'Joe Maneri',
'Joe Manning (2)',
'Joe Marcinkiewicz',
'Joe Marsala',
'Joe Marshall',
'Joe McDonald (6)',
'Joe McLewis',
'Joe Megro',
'Joe Meisner',
'Joe Messina',
'Joe Mondragon',
'Joe Morello',
'Joe Morris (2)',
'Joe Mosello',
'Joe Moser',
'Joe Muranyi',
'Joe Nanton',
'Joe Newman',
'Joe Pamelia',
'Joe Parks',
'Joe Parnello',
'Joe Pass',
'Joe Pulice',
'Joe Puma',
'Joe Quartell',
'Joe Randazzo',
'Joe Raymond',
'Joe Reisman',
'Joe Riggs',
'Joe Roccisano',
'Joe Rodriguez (3)',
'Joe Roland',
'Joe Romano (2)',
'Joe Sample',
'Joe Shepley',
'Joe Shulman',
'Joe Sinacore',
'Joe Smith (3)',
'Joe Soldo',
'Joe Sudler',
'Joe Sullivan',
'Joe Sweeney (2)',
'Joe Sydow',
'Joe Tarto',
'Joe Tekula',
'Joe Temperley',
'Joe Texidor',
'Joe Thomas (3)',
'Joe Thomas (4)',
'Joe Triscari',
'Joe Turner',
'Joe Venuti',
'Joe Venuto',
'Joe Vernon',
'Joe Weidman',
'Joe Wilder',
'Joe Williams',
'Joe Williams (5)',
'Joey Baron',
'Joey Bishop',
'Joey Calderazzo',
'Joey Norosavage',
'Joe Zawinul',
'Johann Anton Rettenbacher',
'Johannes Bockholt',
'Johannes Enders',
'Johannes Fehring',
'Johannes Strasser',
'Johannes Weidenmueller',
'John Abercrombie',
'John Abraham',
'John Adams (22)',
'John Altwerger',
'John Amoroso',
'John Anderson (2)',
'Johnathan Blake',
'John Audino',
'John Bacon',
'John Baldwin',
'John Balkin',
'John Barber',
'John Barclay',
'John B. Arnold',
'John Barrows',
'John Basile',
'John Beal',
'John Bello',
'John Benson Brooks',
'John Bergamo',
'John Berisi',
'John Best',
'John Betsch',
'John Birks Gillespie',
'John Bishop (3)',
'John Blake',
'John Bock',
'John Boice',
'John Brown (3)',
'John Brown (9)',
'John Brunious',
'John Bunch',
'John Cale',
'John Campbell (18)',
'John Carisi',
'John Carroll (5)',
'John Cave',
'John Chance',
'John Clark (2)',
'John Clayton',
'John Cobbs',
'John Cochran',
'John Cochrane',
'John Colianni',
'John Collins (2)',
'John Coltraine',
'John Coltrane',
'John Cook',
'John Coppola',
'John Cordaro',
'John Crescini',
'John Crews',
'John Dailey (2)',
'John D\'Earth',
'John Dee (12)',
'John De Flon',
'John Dengler',
'John Dentz',
'John De Voogdt',
'John Dillard (2)',
'John Di Martino',
'John Doling',
'John Duke',
'John Eckert',
'John Engels',
'John Ewing',
'John Fallstitch',
'John Fedchock',
'John Foster (16)',
'John Frigo',
'John Frosk',
'John Gatchell',
'John Gerber',
'John Gilmore',
'John Giordano (3)',
'John Giuffrida',
'John Glasel',
'John Gordon',
'John Graas',
'John Gray (2)',
'John Guerin',
'John Guerriere',
'John Halliburton',
'John Handy',
'John Hardee',
'John Harner',
'John Harrington',
'John Harris Jr.',
'John Hart',
'John Haughton',
'John Heard',
'John Hebert',
'John Helliwell',
'John Hening',
'John Hicks',
'John Hoffman',
'John Houston',
'John Howell',
'John Hunt',
'John Ingliss',
'John Jackson (7)',
'John Jenkins (2)',
'John \'J.T.\' Bowen',
'John Kirby',
'John Kirkpatrick (2)',
'John Klemmer',
'John Kricker',
'John La Barbera',
'John Lamb',
'John Laporta',
'John Laws',
'John Lee (3)',
'John Leitham',
'John Levy',
'John Lewis (2)',
'John Leys',
'John Lindsay',
'John Lockwood',
'John Longo',
'John Lowe',
'John Lucas (3)',
'John Lynch (4)',
'John Lyon (2)',
'John Macombe',
'John \'Mad Hatter\' Spruill',
'John Madrid',
'John Magruder',
'John Malachi',
'John Marabuto',
'John Markham',
'John Marshall',
'John Marshall (7)',
'John McComb',
'John McConnell',
'John McCormick (9)',
'John McLaughlin',
'John McLevy',
'John McNeil',
'John Mehegan',
'John Messner',
'John Mosca',
'John Mosley',
'John Murtaugh',
'John Nelson (7)',
'John Nesbitt',
'John Newell (2)',
'Johnnie Edwards',
'John Nugent',
'Johnny Acea',
'Johnny Amoroso',
'Johnny Andersen (2)',
'Johnny Austin',
'Johnny Barbera',
'Johnny Blowers',
'Johnny Board',
'Johnny Bothwell',
'Johnny Chance',
'Johnny Coles',
'Johnny Colla',
'Johnny Cresci',
'Johnny Dodds',
'Johnny Dunn',
'Johnny Dyani',
'Johnny Fischer',
'Johnny Fresco',
'Johnny Griffin',
'Johnny Guarnieri',
'Johnny Hammond',
'Johnny Hodges',
'Johnny Knapp',
'Johnny Lathem',
'Johnny Lytle',
'Johnny Mandel',
'Johnny Martel',
'Johnny McAfee',
'Johnny McGee',
'Johnny Mendell',
'Johnny Mezey',
'Johnny Miller (2)',
'Johnny Mince',
'Johnny Morris (4)',
'Johnny Morris (8)',
'Johnny Napton',
'Johnny Otis',
'Johnny Pacheco',
'Johnny Potoker',
'Johnny Powell',
'Johnny Rae',
'Johnny Richards',
'Johnny Rodgers (7)',
'Johnny Russell',
'Johnny Smith',
'Johnny Van Derrick',
'Johnny Van Eps',
'Johnny Walker (4)',
'Johnny Williams',
'John Oates',
'John Oddo',
'John Ore',
'John Oslawski',
'John Owens',
'John Pål Inderberg',
'John Park',
'John Parricelli',
'John Patitucci',
'John Patton',
'John Pendenza',
'John Perry (7)',
'John Pierce (4)',
'John Pisano',
'John Poole (3)',
'John Purcell',
'John Rains',
'John Rangecroft',
'John Riley (2)',
'John Robinson (2)',
'John Rooke',
'John Rotella',
'John Ryan (18)',
'John Sanders',
'John Santulis',
'John Schröder',
'John Scofield',
'John Scottile',
'John Scott Trotter',
'John Sewell (3)',
'John \'Shifty\' Henry',
'John Simmons',
'John Smith (35)',
'John Smith (6)',
'John Sparrow (3)',
'John Stephens (2)',
'John Stetch',
'John Stevens (3)',
'John Stroffe',
'John Stubblefield',
'John Surman',
'John Swana',
'John Taylor (2)',
'John Taylor (41)',
'John Tchicai',
'John Thomas (2)',
'John Thomas (3)',
'John Trueheart',
'John Tumino',
'John Voigt',
'John Von Ohlen',
'John Wasson (2)',
'John Watson (2)',
'John Webber (2)',
'John Williams (14)',
'John Williams (4)',
'John Williams (5)',
'John Williams (8)',
'John Williams (9)',
'John Winter (4)',
'John Wittenberg',
'John Woehrmann',
'John Worster',
'Jo Hrasko',
'Jo Jones',
'Joki Freund',
'Jo Ment',
'Jonah Jones',
'Jon Anderson',
'Jonas Gwangwa',
'Jonas Hellborg',
'Jonas Johansen',
'Jonathan Kreisberg',
'Jon Burr',
'Jon Christensen',
'Jon Davis (2)',
'Jon Dryden',
'Jon Eardley',
'Jon English',
'Jon Faddis',
'Jon Gibson (2)',
'Jon Gordon (3)',
'Jon Hall (11)',
'Jon Hassell',
'Jon Haupers',
'Jon Hiseman',
'Jon Jang',
'Jon Langford',
'Jon Lord',
'Jon Pierson',
'Jon Rogers (5)',
'Jon Walton',
'Jordan Fordin',
'Jordan McLean',
'Jorge Bezerra',
'Jorge Rossy',
'Jörg Fries',
'Jörg Gebhardt',
'Joris Teepe',
'Jørn Elniff',
'Joschi Wimmer',
'José \'Chepito\' Areas',
'Josef Audes',
'Josef Blaha',
'Josef Fischer',
'Josef Pavelka',
'Josef Pelc',
'Josef Skruzny',
'Josef Vejvoda',
'Jose Gutierrez',
'Jose Mangual',
'José Mangual Jr.',
'José Oliveira (3)',
'José Paula',
'Jose \'Pepe\' Jimenez',
'Joseph Bennett',
'Joseph Bowie',
'Joseph Cardinale',
'Joseph Dejean',
'Joseph Difiore',
'Joseph Eger',
'Joseph Grimaldi',
'Joseph Jarman',
'Joseph Park',
'Joseph Reinhardt',
'Joseph Saxon',
'Joseph Scianni',
'Joseph Techner',
'Jose Rossy',
'Josh Jackson',
'Joshua Breakstone',
'Joshua Redman',
'Joshua Rich',
'Joshua Roseman',
'Josie James',
'Josse Breyere',
'Jost Hecker',
'Joszi Klimek',
'Joyce Collins',
'Joyce Hammann',
'J.R. Monterose',
'J.R. Taylor',
'J.T. Lewis',
'Jual Curtis',
'Juan Amalbert',
'Juancito Torres',
'Juan Tizol',
'Jud Denaut',
'Judi Silvano',
'Judy Ellington',
'Jug Taylor',
'Juini Booth',
'Jukkis Uotila',
'Jules Broussard',
'Jules Cassard',
'Jules Chaikin',
'Jules Jacob',
'Jules Kinsler',
'Jules Pouzalgues',
'Julia Lee',
'Julian Adderley',
'Julian Argüelles',
'Julian Coryell',
'Julian Davidson',
'Julian Euell',
'Julian Hess',
'Julian Joseph',
'Julian Lage',
'Julian Priester',
'Julie Jacobs',
'Julien Barber',
'Julio Ayala',
'Julio Barreto',
'Julius Baker',
'Julius Ehrenworth',
'Julius Schacter',
'Julius Tannenbaum',
'Julius Watkins',
'June Christy',
'June Cole',
'June Richmond',
'June Rotenberg',
'Junior Collins',
'Junior Cook',
'Junior Gill',
'Junior Mance',
'Junior Marvin',
'Junior Raglin',
'Junior Weerasinghe',
'Junius Paul',
'Jupp Kreuser',
'Jürgen Ehlers',
'Jürgen Karg',
'Jürgen Schmidt-Oehm',
'Jürgen Schröder',
'Justin Gordon',
'Justo Almario',
'Justo Betancourt',
'Jutta Hipp',
'Juvenal De Holanda Vasconcelos',
'J. W. Alexander',
'Jymie Merritt',
'Jym Young',
'Kahil El Zabar',
'Kahlil Henry',
'Kahn Keene',
'Kai Eckhardt',
'Kaiser Marshall',
'Kai Winding',
'Kali Fasteau',
'Kálmán Oláh',
'Kamasi Washington',
'Kamau Adilifu',
'Kansas Fields',
'Karel Krautgartner',
'Karel Roberti',
'Karel Růžička',
'Karel Vejvoda',
'Karel Velebný',
'Karen Briggs',
'Karen Jones (2)',
'Karen Mantler',
'Karim Ziad',
'Karin Krog',
'Karl Barthelmes',
'Karl Berger',
'Karl De Karske',
'Karl Dobnik',
'Karl Drewo',
'Karl Frey',
'Karl George',
'Karlheinz Kästel',
'Karl-Hermann Lüer',
'Karl Kiffe',
'Karl Kowarik',
'Karl Leaf',
'Karl Loubé',
'Karlo Takač',
'Karl Perazzo',
'Karl Prosenik',
'Karl Ratzer',
'Karl Sanner',
'Karriem Riggins',
'Kasper Tranberg',
'Kass Malone',
'Katie Kissoon',
'Katie Melua',
'Kay Davis',
'Kay Garner',
'Kay Penton',
'Kazumi Watanabe',
'Kazuyoshi Okayama',
'Keg Johnson',
'Keg Purnell',
'Kei Akagi',
'Keiji Kishida',
'Keith Barber',
'Keith Bird',
'Keith Bishop (3)',
'Keith Christie',
'Keith Copeland',
'Keith Davy',
'Keith Jarrett',
'Keith Jones (3)',
'Keith LaMotte',
'Keith Loving',
'Keith Marks',
'Keith Mitchell (6)',
'Keith Moon (2)',
'Keith O\'Quinn',
'Kelly Roberty',
'Ken Ascher',
'Ken Broadhurst',
'Ken Faulk',
'Ken Filiano',
'Kengo Nakamura',
'Ken Hanna',
'Ken Harkins',
'Ken Harpster',
'Ken Hitchcock',
'Ken Lowther',
'Ken Mamayek',
'Ken McIntyre',
'Kenneth Hollon',
'Kenneth Nash',
'Kenneth Stuart',
'Kenny Barron',
'Kenny Berger',
'Kenny Burrell',
'Kenny Clare',
'Kenny Clarke',
'Kenny Davern',
'Kenny Davis',
'Kenny DeLange',
'Kenny Dennis',
'Kenny Dorham',
'Kenny Drew',
'Kenny Garrett',
'Kenny Hagood',
'Kenny Hing',
'Kenny John',
'Kenny Kersey',
'Kenny Kirkland',
'Kenny Loggins',
'Kenny Martlock',
'Kenny Napper',
'Kenny O\'Brien (4)',
'Kenny Pinson',
'Kenny Rampton',
'Kenny Rogers',
'Kenny Rupp',
'Kenny Salmon',
'Kenny Shroyer',
'Kenny Tiffany',
'Kenny Vance',
'Kenny Washington',
'Kenny Werner',
'Kenny Wheeler',
'Keno Duke',
'Ken Peplowski',
'Ken Soderblom',
'Kent Brinkley',
'Kent Carter',
'Kent Larsen',
'Kent McGarity',
'Kenton Morrow',
'Ken Watson',
'Ken Wenzel',
'Kenwood Dennard',
'Kermit Moore',
'Kermit Scott',
'Kermit Simmons',
'Keter Betts',
'Kevin Cline',
'Kevin Donovan',
'Kevin Eubanks',
'Kevin Gray',
'Kevin Hays',
'Kevin Jordan',
'Kevin Kanner',
'Kevin Kavanaugh',
'Kevin O\'Connell (4)',
'Kevin Richardson (3)',
'Khalil Balakrishna',
'Kid Ory',
'Kieran Overs',
'Kim Carnes',
'Kim Clarke',
'Kim Frizell',
'Kim Kimberly',
'Kim Park',
'Kim Thompson (2)',
'King Errisson',
'King Guion',
'King Kolax',
'King Oliver',
'Kirby Stewart',
'Kirk Lightsey',
'Kirk Whalum',
'Kirsten Ibarra',
'Kitt Reid',
'Kitty Kallen',
'Kiyoshi Kitagawa',
'Kiyoshi Tokunaga',
'Klaus Koch',
'Klaus Nagurski',
'Klaus Suonsaari',
'Klaus Weiss',
'Knut Riisnæs',
'Kohsuke Mine',
'Koko Taylor',
'Konrad Alfing',
'Konrad Bogdan',
'Kresten Osgood',
'Krzysztof Zawadzki',
'Kunimitsu Inaba',
'Kurt Bloom',
'Kurt Bong',
'Kurt \'Bubi\' Aderhold',
'Kurt Dieterle',
'Kurtis Walker',
'Kurt McGettrick',
'Kurt Rosenwinkel',
'Kurt Wald',
'Kylo Turner',
'Laco Deczi',
'Laco Tropp',
'Ladislas Czabanick',
'Ladislav Fidri',
'Ladjl Camara',
'Lafayette Harris',
'Lalo Schifrin',
'Lamar Wright (2)',
'Lammar Wright',
'La Monte Young',
'LaMont Johnson (2)',
'Lance Larson',
'Lanfranco Malaguti',
'Langston Curl',
'Lanny Morgan',
'Larry Abbott',
'Larry Adler',
'Larry Binyon',
'Larry Breen',
'Larry Bunker',
'Larry Carlton',
'Larry Charles (2)',
'Larry Coryell',
'Larry Covelli',
'Larry Cramer',
'Larry Farrell',
'Larry Ford',
'Larry Frazier',
'Larry Fuller (2)',
'Larry Gales',
'Larry Goldings',
'Larry Grenadier',
'Larry Hall',
'Larry Hall (2)',
'Larry Harlow',
'Larry Kinnamon',
'Larry Knechtel',
'Larry Kurkdjie',
'Larry Lunetta',
'Larry Mann',
'Larry McGuire',
'Larry McKenna',
'Larry Morton',
'Larry Mosher',
'Larry Novak',
'Larry O\'Brien (2)',
'Larry Patton (2)',
'Larry Pyatt',
'Larry Ridley',
'Larry Ritchie',
'Larry Rockwell',
'Larry Rosen',
'Larry Schneider',
'Larry Shunk',
'Larry Sonn',
'Larry Stoffel',
'Larry Taylor (4)',
'Larry Townsend',
'Larry Vuckovich',
'Larry Walsh (2)',
'Larry Wilcox',
'Larry Willis',
'Larry Wilson (3)',
'Larry Wright',
'Larry Young',
'Lars Andersson (6)',
'Lars Black',
'Lars Danielsson (3)',
'Lars Eklund',
'Lars Erstrand',
'Lars Gullin',
'Lars Jansson',
'Lars Møller',
'Lars Sjösten',
'La Toya Jackson',
'Laurdine Patrick',
'Laurence Cook',
'Laurence Cottle',
'Laurence Elam',
'Laurence Ridley',
'Laurie Frink',
'Laurie Johnson (2)',
'Laurindo Almeida',
'Lauro Rossi',
'Lawrence Brown',
'Lawrence Burgan',
'Lawrence Dixon',
'Lawrence Feldman',
'Lawrence Freeman',
'Lawrence \'Frog\' Anderson',
'Lawrence Killian',
'Lawrence Lucie',
'Lawrence Marable',
'Lawrence Stearns',
'Leah Matthews',
'Leata Galloway',
'Lee Abrams',
'LeeAnn Ledgerwood',
'Lee Blair',
'Lee Callet',
'Lee Castaldo',
'Lee Castle',
'Lee Fortier',
'Lee Hazlewood',
'Lee Hilliard (2)',
'Lee Katzman',
'Lee Konitz',
'Lee Morgan',
'Lee O\'Connor',
'Lee Pearson (2)',
'Lee Ritenour',
'Lee Robertson (4)',
'Lee Romano',
'Lee Young (2)',
'Leif Uvemark',
'Leif Wennerström',
'Leith Stevens',
'Lem Davis',
'Lem Johnson',
'Len Goldstein',
'Lennart Axelsson',
'Lennie Hayton',
'Lennie Johnson',
'Lennie Mitchell',
'Lennie Niehaus',
'Lennie Tristano',
'Lenny Corris',
'Lenny Mayes',
'Lenny McBrowne',
'Lenny Pickett',
'Lenny White',
'Len Skeat',
'Leo Acosta',
'Leo Blevins',
'Léo Chauliac',
'Leo Connors',
'Leo Cuypers',
'Leo Eggenberger',
'Leo Goudriaan',
'Leo Kahn',
'Leo Kruczek',
'Léo Leobons',
'Leo McConville',
'Leonard Atkins',
'Leonard Cerris',
'Leonard Davis',
'Leonard \'Doc\' Gibbs Jr.',
'Leonard Enois',
'Leonard Feather',
'Leonard Gaskin',
'Leonard Hartman',
'Leonard Hawkins',
'Leonard Johnson (3)',
'Leonard Jones',
'Leonard Kaye',
'Leonard Lowry',
'Leonard Malarsky',
'Leonard Posner',
'Leonard Selic',
'Leonard Swain',
'Leon \'Chu\' Berry',
'Leon Comegys',
'Leon Cox',
'Leon Dorsey',
'Leon Dubrow',
'Leon Ferreri',
'Leon Maleson',
'Leon Merian',
'Leon Ndugu Chancler',
'Leon Patillo',
'Leon Pendarvis',
'Leon Pettis',
'Leon Rix',
'Leon Roy (2)',
'Leon Russell',
'Leon Spann',
'Leon Thomas',
'Leon Trommel',
'Leo Parker',
'Leopoldo Pineda',
'Leo Shepherd',
'Leo \'Snub\' Mosley',
'Leo White',
'Leo Wright',
'Leo Zorn',
'Leppe Sundevall',
'Leroy Hardy',
'Leroy Harris',
'Leroy Harris (2)',
'Leroy Jackson (3)',
'Leroy Jenkins',
'Leroy Lovett',
'Leroy Maxey',
'Leroy Parker',
'Leroy Vinnegar',
'Leroy Williams',
'Lesa Terry',
'Les Benedict',
'Les Burness',
'Les Clarke (2)',
'Les Cooper (4)',
'Les Crumbacher',
'Les DeMerle',
'Les Grinage',
'Les Hite',
'Les Jenkins',
'Les Lieber',
'Leslie Johnakins',
'Leslie Mandoki',
'Les Lovitt',
'Les Robinson',
'Les Rout',
'Les Spann',
'Lester Boone',
'Lester Bowie',
'Lester Clarke',
'Lester Lashley',
'Lester Robertson',
'Lester Robinson',
'Lester Santiago',
'Lester Young',
'Lew Davis',
'Lew Elias',
'Lewis Kahn',
'Lewis Nash',
'Lewis Worrell',
'Lew McCreary',
'Lew Soloff',
'Lew Tabackin',
'Lex Humphries',
'Lex Mond',
'Linc Chamberland',
'Linc Milliman',
'Lincoln Goines',
'Lincoln Mayorga',
'Lincoln Mills',
'Linda \'Tequila\' Logan',
'Linda Wenger',
'Lindsey Buckingham',
'Linley Marthe',
'Linton Garner',
'Linton Kwesi Johnson',
'Lionel Belmondo',
'Lionel Hampton',
'Lionel Reason',
'Lionel Richie',
'Lisa Salzer',
'Lisle Atkinson',
'Livio Fresk',
'Lixbot',
'LJ Reynolds',
'L. Lee',
'Lloyd Anderson (5)',
'Lloyd Buchanon',
'Lloyd Davis (2)',
'Lloyd Ellis',
'Lloyd Glenn',
'Lloyd Lunham',
'Lloyd Martin',
'Lloyd Mayers',
'Lloyd Michels',
'Lloyd Oldham',
'Lloyd Otto',
'Lloyd Spoon',
'Lloyd Trotman (2)',
'Lloyd Turner (4)',
'Lloyd Ulyate',
'Loinel Sesma',
'Lois Colin',
'Lois Martin',
'Lonesome Bob',
'Lonnie Braun',
'Lonnie Hewitt',
'Lonnie Hillyer',
'Lonnie Plaxico',
'Lonnie Shaw',
'Lonnie Simmons (2)',
'Lonnie Smith',
'Lonnie Wilfong',
'Lonzo Westphal',
'Loren Little',
'Loren Stillman',
'Lorraine Geller',
'Lorraine Ragon',
'Lotten Taylor',
'Lotty Rank',
'Lou Anne Neill',
'Lou Bennett (2)',
'Lou Blackburn',
'Lou Bring',
'Lou Busch',
'Lou Darley',
'Lou Donaldson',
'Lou Fromm',
'Lou Gasca',
'Lou Gramm',
'Lou Grassi',
'Lou Hackney',
'Lou Horvath',
'Louie Hoff',
'Louis Armstrong',
'Louis Bacon',
'Louis Banks',
'Louis Bauzo',
'Louis Bellson',
'Louis Carrington',
'Louis Ciccone',
'Louis Ciotti',
'Louis Colombo',
'Louis Garcia (6)',
'Louis Giamo',
'Louis Harmin',
'Louis Hayes',
'Louis Hjulmand',
'Louis Hunt',
'Louis Jordan',
'Louis Kabok',
'Louis Kievman',
'Louis Martin (3)',
'Louis Melon',
'Louis Metcalf',
'Louis Pressman',
'Louis Prima',
'Louis Richardet',
'Louis R. Mucci',
'Louis Smith (2)',
'Louis Stewart',
'Louis Taylor',
'Louis Taylor (3)',
'Louis Taylor Jr.',
'Louis Valizan',
'Louis Vola',
'Louis Zito (2)',
'Lou Levy',
'Lou Marini',
'Lou McGarity',
'Lou Mecca',
'Lou Obergh Jr.',
'Lou Oles',
'Lou Orenstein',
'Lou Prisby',
'Lou Raderman',
'Lou Rawls',
'Lou Reed',
'Lou Singer',
'Lou Skalinder',
'Lou Stein',
'Lowell \'Count\' Hastings',
'Lowell George',
'Lowell Martin',
'Luca Del Maestro',
'Lucas Costa',
'Lucas Lindholm',
'Luciano Biondini',
'Luciano Fabris (2)',
'Lucien Gallopain',
'Lucien Jeunesse',
'Lucien Schmit',
'Lucien Simoens',
'Lucille Dixon',
'Lucio Ferrara',
'Lucky Millinder',
'Lucky Thompson',
'Luděk Švábenský',
'Luigi Trussardi',
'Luis Bonilla',
'Luis Gasca',
'Luis Kant',
'Luis \'Perico\' Ortiz',
'Luis Russell',
'Lukasz Gottwald',
'Luke Jenner',
'Luther Hughes',
'Luther \'Sonny\' Craven',
'Lyle Mars',
'Lyle Mays',
'Lyle Murphy',
'Lyle Ritz',
'Lyman Vunk',
'Lyn Biviano',
'Lyn Christie',
'Lynn Blessing',
'Lynn Cornell',
'Lynn Davis',
'Lynne Stevens',
'Lynn Franklin',
'Lynn Nicholson',
'Lynn Richards',
'Lynn Seaton',
'Lyn White',
'Mac Cheikes',
'Mac Gallehon',
'Mack Goldsbury',
'Mack Sterling',
'Mack Walker',
'Mac MacQuordale',
'Mac Rebennack',
'Madeline Bell',
'Mads Vinding',
'Maffy Falay',
'Mahlon Clark',
'Major Holley',
'Makaya Ntshoko',
'Makoto Ozone',
'Malachi Favors',
'Malcolm Crain',
'Malcolm Griffiths',
'Malcolm McNab',
'Malcolm Taylor',
'Malopoets',
'Malta (3)',
'Mal Waldron',
'Mamie Smith',
'Mancy Carr',
'Manfred Gätjens',
'Manfred Grossmann',
'Manfred Moch',
'Manfred Schoof',
'Manfred Zeh',
'Mani Neumeier',
'Manley Buchanan',
'Mannie Gershman',
'Manny Albam',
'Manny Berger',
'Manny Klein',
'Manolo Badrena',
'Manuel Duran',
'Manuel Zegler',
'Manzie Johnson',
'Marc Copland',
'Marcel Bianchi',
'Marcel Dumont',
'Marcel Fuchs',
'Marcello Di Leonardo',
'Marcello Melis',
'Marcello Pellitteri (2)',
'Marc Fosset',
'Marc Hellman',
'Marcia Van Dyke',
'Marcio Mattos',
'Marc Johnson (2)',
'Marc Levin',
'Marc-Michel Le Bévillon',
'Marco Fagioli',
'Marco Panascia',
'Marco Ratti',
'Marco Ricci',
'Marco Valeri',
'Marco Zurzolo',
'Marc Shaiman',
'Marc Silverman',
'Marcus Belgrave',
'Marcus Fiorillo',
'Marcus Malone',
'Marcus McLaurine',
'Marcus Miller',
'Marcus Printup',
'Marcus Roberts',
'Marcy Levy',
'Margot Newman',
'Marian McPartland',
'Marianne Gazzani',
'Marian Zazeela',
'Maria Teresa Tecchi',
'Marijan Domić',
'Marika Falk',
'Marilyn Crispell',
'Mario Babidillo',
'Mario Bauzá',
'Mario Cipollina',
'Mario Cruz',
'Mario Daone',
'Mario Gonzi',
'Mario Mavrin',
'Marion \'Boonie\' Hazel',
'Marion Brown',
'Marion Childers',
'Marion DeVeta',
'Marion Morgan',
'Mario Ochoa (2)',
'Mario Rivera (2)',
'Mario Rollo',
'Mario Serritello',
'Mario Toscarelli',
'Marius Beets',
'Marjorie Hyams',
'Mark Barnett (3)',
'Mark Belair',
'Mark Bennett (3)',
'Mark Bettcher',
'Mark Dresser',
'Mark Egan',
'Mark Feldman',
'Mark Griffith (2)',
'Mark Gross',
'Mark Helias',
'Mark Levinson',
'Mark Lewis (18)',
'Mark Lusk',
'Mark McIntyre',
'Mark Mondesir',
'Mark Pasco',
'Mark Stevens',
'Mark Stevens (2)',
'Mark Taylor (10)',
'Mark Tornillo',
'Mark Turner (2)',
'Mark Vinci',
'Mark Volman',
'Mark Walker (2)',
'Mark Whitecage',
'Mark \'Wilkie\' Wilkinson',
'Marky Markowitz',
'Marlon Jackson',
'Marlowe Morris',
'Marquis Foster',
'Marshall Allen',
'Marshall Brown',
'Marshall Cram',
'Marshall Hawkins',
'Marshall Mendell',
'Marshall Royal',
'Marshall Sosson',
'Marshall Thompson (2)',
'Martial Solal',
'Martin Bues',
'Martin Drew',
'Martin Drover',
'Martin Gjakonovski',
'Martin Jacobsen',
'Martin Joseph',
'Martin Lubenov',
'Martin Mayes',
'Martin Rivera',
'Martin Slavin',
'Martin Van Duynhoven',
'Martin Williams (6)',
'Martin Wind',
'Martin Zenker',
'Marty Ashby',
'Marty Berman',
'Marty Blitz',
'Marty Clausen',
'Marty Ehrlich',
'Marty Flax',
'Marty Grosz',
'Marty Harris',
'Marty Marsala',
'Marty Morell',
'Marty Napoleon',
'Marty Paich',
'Marty Richards',
'Marty Ruderman',
'Marty Wilson',
'Marvin George',
'Marvin Halladay',
'Marvin Holladay',
'Marvin Jenkins',
'Marvin Johnson',
'Marvin Pattillo',
'Marvin Shore',
'Marvin \'Smitty\' Smith',
'Marvin Stamm',
'Mary Ann McCall',
'Mary Lou Williams',
'Mary Martin',
'Mary Osborne',
'Masabumi Kikuchi',
'Masahiro Yoshida',
'Masayuki Takayanagi',
'Masha Elstner',
'Massimo Faraò',
'Massimo Manzi',
'Massimo Moriconi',
'Massimo Urbani',
'Mat Clasen',
'Mat Maneri',
'Mat Mathews',
'Mats Hägglöf',
'Matt Finders',
'Matt Harris (7)',
'Matthew Fisher',
'Matthew Garrison',
'Matthew Gee',
'Matthew McKay',
'Matthew Shipp',
'Matthias Schriefl',
'Matthias Thurow',
'Matthieu Michel',
'Matt Penman',
'Matt Wilson',
'Matty Golizio',
'Matty Malneck',
'Matty Matlock',
'Matyi Csányi',
'Maurice Brown',
'Maurice Cevrero',
'Maurice Chaillou',
'Maurice Cizeron',
'Maurice Gladieu',
'Maurice Harris',
'Maurice James Simon',
'Maurice Kogan',
'Maurice Mark',
'Maurice Marks',
'Maurice McIntyre',
'Maurice Meunier',
'Maurice Miller',
'Maurice Moufflard',
'Maurice Mouflard',
'Maurice Perlmutter',
'Maurice Purtill',
'Maurice Spears',
'Maurice Stein',
'Maurice Thomas',
'Maurice Van Cleef',
'Maurice Vander',
'Maurizio Giammarco',
'Mauro Beggio',
'Mauro Turso',
'Maury Beeson',
'Max Bennett',
'Max Blanc',
'Max Boeree',
'Max Elloy',
'Max Farley',
'Max Garduno',
'Max Goldberg',
'Max Herman (2)',
'Max Hollander',
'Max Hugot',
'Maxine Roach',
'Max Kaminsky',
'Max Mariash',
'Max Pollikoff',
'Max Roach',
'Max Seigel',
'Max Wayne',
'Max Weinberg',
'Maxwell Davis',
'May Hogan Cambern',
'Maynard Ferguson',
'McChenry Ellis',
'McCoy Tyner',
'McGrégor',
'McHouston Baker',
'Meade \'Lux\' Lewis',
'Med Flory',
'Meg Okura',
'Melba Liston',
'Mel Davis',
'Mel Ellison',
'Mel Graves',
'Mel Green (2)',
'Mel Kunkle',
'Mel Lee',
'Mel Lewis',
'Mel Powell',
'Mel Rhyne',
'Mel Tormé',
'Melvin Glover',
'Melvin Jackson',
'Melvin Lastie',
'Melvin Moore (2)',
'Melvin Sparks',
'Mel Wanzo',
'Mel Zelnick',
'Mercer Ellington',
'Merle Bredwell',
'Merrill Kline',
'Mert Goodspeed',
'Mert Oliver',
'Merv Harding',
'Meyer Hirsch',
'Mezz Mezzrow',
'Michael Abene',
'Michael Adkins',
'Michael Asch',
'Michael Bahner',
'Michael Bocchiccio',
'Michael Brecker',
'Michael Brooks (2)',
'Michael Cain',
'Michael Carabello',
'Michael Carvin',
'Michael Cochrane',
'Michael Colgrass',
'Michael Davis',
'Michael Dease',
'Michael DiPasqua',
'Michael Formanek',
'Michael Gibbs',
'Michael Goldberg (2)',
'Michael Grey (4)',
'Michael Jackson',
'Michael Jones (4)',
'Michael Leonhart',
'Michael Longo',
'Michael Mantler',
'Michael Mattos',
'Michael Monroe',
'Michael Moore (2)',
'Michael Philip Mossman',
'Michael Reinecke',
'Michael Rodriguez',
'Michael Sabol',
'Michael Sell',
'Michael Shrieve',
'Michael Silva',
'Michael Smith (14)',
'Michael Stanley Gee',
'Michael Thielepape',
'Michael Weiss (2)',
'Michael White (2)',
'Michael Young (4)',
'Michael Zager',
'Michał Urbaniak',
'Michel Camilo',
'Michel Cassez',
'Michel de Villers',
'Michele Donati',
'Michel Emer',
'Michele Rabbia',
'Michele Rosewoman',
'Michel Gaudry',
'Michel Godard',
'Michel Goldberg',
'Michel Graillier',
'Michel Hausser',
'Micheline Day',
'Michel Legrand',
'Michel Marre',
'Michel Petrucciani',
'Michel Poli',
'Michel Portal',
'Michel Roger',
'Michel Rosciglione',
'Michel Sardaby',
'Michel Warlop',
'Mick Eve',
'Mickey Bloom',
'Mickey Crane',
'Mickey Folus',
'Mickey Mangano',
'Mickey Rich',
'Mickey Roker',
'Mickey Scrima',
'Mickey Sheen',
'Mickey Tucker',
'Mick Goodrick',
'Mick Hucknall',
'Mick Waller',
'Micky Crane',
'Midge Ure',
'Miff Mole',
'Miff Sines',
'Miguel Zenon',
'Mike Alterman',
'Mike Altschul',
'Mike Baker (2)',
'Mike Barone',
'Mike Barrowman',
'Mike Bloomfield',
'Mike Brignola',
'Mike Bryan',
'Mike Butera',
'Mike Citron',
'Mike Conn',
'Mike Datz',
'Mike Datzenko',
'Mike Deasy',
'Mike Doty',
'Mike Egan (4)',
'Mike Finnigan',
'Mike Gerber',
'Mike Glass (3)',
'Mike Hall (11)',
'Mike Hedley',
'Mike Hyman',
'Mike Jamieson',
'Mike Karn',
'Mike Lang',
'Mike Lawrence',
'Mike LeDonne',
'Mike Levine (7)',
'Mike Love',
'Mike Mainieri',
'Mike Mandel',
'Mike McKendrick',
'Mike Melillo',
'Mike Melvoin',
'Mike Moole',
'Mike Nock',
'Mike Pacheco',
'Mike Pingitore',
'Mike Ponella',
'Mike Price',
'Mike Reznikoff',
'Mike Richmond',
'Mike Rodriguez (9)',
'Mike Ross (4)',
'Mike Rubino',
'Mike Shapiro (2)',
'Mike Snustead',
'Mike Spengler',
'Mike Steinel',
'Mike Stern',
'Mike Suter',
'Mike Tinnes',
'Mike Tomaro',
'Mike Trafficante',
'Mike Triscari',
'Mike Vax',
'Mike Walker',
'Mike Wallace',
'Mike Williams (6)',
'Mike Wofford',
'Mike Zwerin',
'Mike Zydowsky',
'Milan Máder',
'Milan Pilar',
'Milan Ulrich',
'Milan Vitoch',
'Milcho Leviev',
'Mildred Bailey',
'Miles Davis',
'Miles Evans',
'Milford Graves',
'Millard Vinson',
'Milo Pavlovic',
'Milt Bernhart',
'Milt Buckner',
'Milt Gold',
'Milt Grayson',
'Milt Harris',
'Milt Hinton',
'Milt Holland',
'Milt Jackson',
'Milt Lomask',
'Milton Fletcher (2)',
'Milton Kabak',
'Milton Mezzrow',
'Milton Robinson',
'Milton Rogers',
'Milton Senior',
'Milton S. Garred',
'Milton Suggs',
'Milt Raskin',
'Milt Turner',
'Milt Yaner',
'Mingo Lewis',
'Min Leibrook',
'Mino Cinelu',
'Minor Hall',
'Miroslav Krýsl',
'Miroslav Vitous',
'Mischa Russell',
'Missak Baghboudarian',
'Mitchel Forman',
'Mitchell Lurie',
'Mitchell Wood',
'Mitch Melnick',
'Mitch Miller',
'Mitch Mitchell',
'Modesto Briseno (2)',
'Modesto Duran',
'Moe Schneider',
'Moe Wechsler',
'Mojmír Bártek',
'Money Johnson',
'Money Mark',
'Mongo Santamaria',
'Monguito Santamaria',
'Monk Montgomery',
'Montego Joe',
'Montez Coleman',
'Monty Alexander',
'Monty Budwig',
'Monty Stark',
'Moon Zappa',
'Morey Feld',
'Morey Field',
'Morey Samuel',
'Morris Bercov',
'Morris Jennings',
'Morris Kohn',
'Morris Lane',
'Morris Rayman',
'Morris Secon',
'Morris Stonzek',
'Morris White',
'Mort Herbert',
'Morton Friedman',
'Mort Stuhlmaker',
'Morty Corb',
'Morty Lewis (2)',
'Mose Allison',
'Motohiko Hino',
'Motorhead Sherwood',
'Mousey Alexander',
'Muggsy Spanier',
'Muhal Richard Abrams',
'Muhammad Ali',
'Mulgrew Miller',
'Mundell Lowe',
'Muneer B. Fennell',
'Munyungo Jackson',
'Murali Coryell',
'Muriel Lane',
'Murray Kellner',
'Murray McEachern',
'Murray Shipinsky',
'Murray Williams',
'Musky Ruffo',
'Mustapha Daleel',
'Mutt Carey',
'Myron Dove',
'Myron Folies',
'Myron Shapler',
'Nabil Totah',
'Nadine Young',
'Nadi Qamar',
'Najee',
'Nancy Sinatra',
'Nancy Stahl',
'Napoleon M. Brock',
'Nappy Lamare',
'Narada Michael Walden',
'Nasheet Waits',
'Nat Adderley',
'Nat Bettis',
'Nate Kazebier',
'Nate Nelson (2)',
'Nathan Davis',
'Nathan Gershman',
'Nathan Goldstein',
'Nathaniel Allen',
'Nathaniel Benson',
'Nathaniel Meeks',
'Nathaniel Townsley III',
'Nathan Page',
'Nathen Page',
'Nat Hentoff',
'Nat Jaffe',
'Nat King Cole',
'Nat Lobovsky',
'Nat Morris Jr.',
'Nat Natoli',
'Nat Pavone',
'Nat Peck',
'Nat Perrilliat',
'Nat Pierce',
'Nat Polen',
'Nat Ray',
'Nat Reeves',
'Nat Story',
'Neal Hefti',
'Neal Schon',
'Neely Plumb',
'Neemoi Acquaye',
'Neil Clark',
'Neil Friel',
'Neil Lancaster',
'Neil Marshall (3)',
'Neil Metcalfe',
'Neil Reid (2)',
'Neil Swainson',
'Nels Bultmann',
'Nelson Boyd',
'Nelson Bryant',
'Nelson Hatt',
'Nelson Hinds',
'Nelson Rangell',
'Nelson Riddle',
'Nelson Shelladay',
'Nelson Shellady',
'Nelson Williams',
'Nestor Amaral',
'Nestor Sanchez',
'Newell Parker',
'Nicholas (5)',
'Nicholas Pisani',
'Nick Bonney',
'Nick Brignola',
'Nick Buono',
'Nick Caiazza',
'Nick Capezuto',
'Nick Ceroli',
'Nick DiMaio',
'Nick Esposito (2)',
'Nick Fatool',
'Nick Fenton',
'Nick Gaglio',
'Nick Hauck',
'Nick Hauk',
'Nick Holmes (4)',
'Nick Hupfer',
'Nick Martinis',
'Nick Sands (2)',
'Nick Stabulas',
'Nick Travis',
'Nick Van Eede',
'Nicky Marrero',
'Nico Bunink',
'Nicola Borrelli',
'Nicolae Ochi Albi',
'Nicola Raffone',
'Nicolas Fiszman',
'Nicolas Simion',
'Nicola Stilo',
'Nicoletta Manzini',
'Niels-Henning Ørsted Pedersen',
'Niels Lan Doky',
'Nik Kershaw',
'Nikki Iles',
'Niklas Munter',
'Nils-Bertil Dahlander',
'Nils Bultmann',
'Nils Lofgren',
'Ninapinta',
'Nini Rosso (2)',
'Nitta Rette',
'Noah Brandmark',
'Noel Chiboust',
'Noel Jewkes',
'Noel McGhie',
'Noel Smith',
'Nolan Smith',
'Nona Hendryx',
'Noni Bernardi',
'Norbert Scholly',
'Noriko Ueda',
'Norma Jean Bell',
'Norman Baltazar',
'Norman Bates (2)',
'Norman Brown (3)',
'Norman Buster',
'Norman Connors',
'Norman Faye',
'Norman Fearrington',
'Norman Greene',
'Norman Keenan',
'Norman McPherson',
'Norman Murphy',
'Norman Parker',
'Norman Pockrandt',
'Norman Seelig',
'Norman Simmons',
'Norman Smith (2)',
'Norma Teagarden',
'Norris Jones',
'Norris Turney',
'Obie Massingill',
'Odd Ulleberg',
'Odean Pope',
'Ohad Talmor',
'Olaf Gustavson',
'Olav Gustafsson',
'Olcott Vail',
'Ole Jacob Hansen',
'Ole Kock Hansen',
'Ole Ousen',
'Ole Rømer',
'Oliver Jackson',
'Oliver Johnson',
'Oliver Mathewson',
'Oliver Nelson',
'Oliver Richardson',
'Olivier Antunes',
'Olivier Gatto',
'Olivier Hutman',
'Olle Holmqvist',
'Ollie Mitchell',
'Ollie Wilson',
'Olodum',
'Olu Dara',
'Omar Hakim',
'Omer Simeon',
'Onaje Allan Gumbs',
'O\'Neil Spencer',
'Oren Marshall',
'Orestes Vilato',
'Ornette Coleman',
'Orrin Evans',
'Orville \'Piggy\' Minor',
'Oscar Aleman',
'Oscar Brashear',
'Oscar Dennard',
'Oscar Estell',
'Oscar Klein',
'Oscar Lee Bradley Sr.',
'Oscar Moore',
'Oscar Peterson',
'Oscar Pettiford',
'Oscar Slembroek',
'Osie Johnson',
'Othello Molineaux',
'Othmar Šerhák',
'Otis \'Bu Bu\' Turner',
'Otis Finch',
'Otis Johnson',
'Otmaro Ruiz',
'Otto Bredl',
'Otto Hardwick',
'Otto Tucker',
'Ozren Depolo',
'Ozzie Bailey',
'Pablo Calogero',
'Pablo Escayola',
'Pablo Tellez',
'Pablo Today',
'Paco Sery',
'Palle Danielsson',
'Palle Mikkelborg',
'Pamela Goldsmith',
'Pam Windo',
'Panama Francis',
'Paoli Mejias',
'Paolo Benedettini',
'Paolo Cardoso',
'Paolo Fresu',
'Paolo Ghetti',
'Papa Charlie Jackson',
'Papo Lucca',
'Pat Benatar',
'Pat Chartrand',
'Pat Coil',
'Pat Dodd',
'Pat Flaherty (5)',
'Patience Higgins',
'Pat Illingworth',
'Pat Jenkins (2)',
'Pat LaBarbera',
'Pat Longo',
'Pat Martino',
'Pat McNaughton',
'Pat Metheny',
'Pat Moran (2)',
'Pat O\'Leary',
'Patoum',
'Pat Patrick',
'Pat Pratta',
'Pat Rebillot',
'Patrice Caratini',
'Patrice Rushen',
'Patrick Mahoney',
'Patrick Rickman',
'Patrizia Scascitelli',
'Patti Bown',
'Patti Maloney',
'Patty Price',
'Pat Virgadamo',
'Paul Adamson',
'Paula Gilbert',
'Paula Kelly',
'Paul Barbarin',
'Paul Bley',
'Paul Campbell (5)',
'Paul Carr',
'Paul Carrack',
'Paul Chambers',
'Paul Chambers (3)',
'Paul Chapman (3)',
'Paul Cohen',
'Paul Cohen (8)',
'Paul Collins (6)',
'Paul Cordonnier',
'Paul Coscino',
'Paul Desmond',
'Paul Fauerso',
'Paul Faulise',
'Paul Ferrara',
'Paul Fontaine',
'Paul Gansalves',
'Paul Geil',
'Paul Gill',
'Paul Gonsalves',
'Paul Guerrero',
'Paul Gusman',
'Paul Harris (2)',
'Paul Hewson',
'Paul Heydorff',
'Paul Horn',
'Paul Humphrey',
'Paul Ingraham',
'Paulinho Da Costa',
'Paul Jackson (2)',
'Paul Janes',
'Paul Jeffery',
'Paul Jeffrey',
'Paul Kelly (29)',
'Paul King (4)',
'Paul Kondziela',
'Paul Kreibich',
'Paul Lee (5)',
'Paul Lowenkron',
'Paul Lytton',
'Paul Madeira Mertz',
'Paul Mason',
'Paul Mazzio',
'Paul McCandless',
'Paul McCoy (2)',
'Paul McGinley',
'Paul McKee',
'Paul McLeod',
'Paul Mertens (4)',
'Paul Metzke',
'Paul Meyers',
'Paul Moen',
'Paul Moer',
'Paul Morsey',
'Paul Motian',
'Paulo Cardoso',
'Paul Picard',
'Paul Piguillem',
'Paul Plummer',
'Paul Polansky',
'Paul Powell (5)',
'Paul Prince (3)',
'Paul Quinichette',
'Paul Renzi',
'Paul Ricci',
'Paul Robyn',
'Paul Rovère',
'Paul Rutherford (2)',
'Paul Salvo (2)',
'Paul Sarmento',
'Paul Selden',
'Paul Seldon',
'Paul Serrano',
'Paul Severson',
'Paul Shaffer',
'Paul Shure',
'Paul Simon',
'Paul Smith (5)',
'Paul Villepigue',
'Paul Webster',
'Paul Weigand',
'Paul Wertico',
'Paul West',
'Paul Weston (2)',
'Paul Whiteman',
'Paul Winter',
'Paul Winter (2)',
'Pavel Staněk',
'Peanuts Holland',
'Peanuts Hucko',
'Pearl Kaufman',
'Peck Morrison',
'Pedro Chao',
'Pedro \'puchi\' Boulong',
'Peer Wyboris',
'Pee Wee Erwin',
'Pee Wee Hunt',
'Pee Wee Moore',
'Pee Wee Russell',
'Peggy King',
'Peggy Lee',
'Peggy Stern',
'Pekka Sarmanto',
'Pepe Leon',
'Pepito Pignatelli',
'Pepito Riestra',
'Pepper Adams',
'Per-Arne Croona',
'Percival Payne',
'Percy Brice',
'Percy Heath',
'Per Goldschmidt',
'Per Hultén',
'Per Husby',
'Per-Ola Gadd',
'Perry Botkin',
'Perry Lopez',
'Perry Robinson',
'Petar Spasov',
'Pete Beachill',
'Pete Briggs',
'Pete Brown (2)',
'Pete Candoli',
'Pete Carpenter',
'Pete Chilver',
'Pete Christlieb',
'Pete Clark (2)',
'Pete Dalbis',
'Pete De Siena',
'Pete Escovedo',
'Pete Fountain',
'Pete Hurt',
'Pete Johns',
'Pete Jolly',
'Pete Levin',
'Pete Minger',
'Pete Mondello',
'Pete Peterson',
'Peter Appleyard',
'Peter Badie',
'Peter Barshay',
'Peter Baumeister',
'Peter Bellomo',
'Peter Bernstein',
'Peter Brötzmann',
'Peter Chivily',
'Peter Coe',
'Peter Dominguez',
'Peter Donald',
'Peter Erskine',
'Peter Frampton',
'Peter Franken',
'Peter Gabriel',
'Peter Garrett',
'Peter Gordon (8)',
'Peter Graves',
'Peter Hecht',
'Peter Herbolzheimer',
'Peter Hesslein',
'Peter Hyde (2)',
'Peter Ind',
'Peter John Barnfather',
'Peter Johnson (27)',
'Peter Kowald',
'Peter Lawford',
'Peter Littman',
'Peter Ludes',
'Peter Madsen',
'Peter Maffay',
'Peter Martin (6)',
'Peter Maurer (4)',
'Pete Rodriguez',
'Peter Perfido',
'Peter Schaper',
'Peter Sims (2)',
'Peter Sprague',
'Peter Stock',
'Peter Trunk',
'Pete Rugolo',
'Peter Washington',
'Peter Weihe',
'Peter Witte',
'Peter Wolf',
'Peter Wolf (3)',
'Peter Yellin',
'Peter Ypma',
'Peter Zak',
'Pete Townshend',
'Pete Vibona',
'Petr Kořínek',
'Petter Kateraas',
'Pharoah Sanders',
'Pha Terrell',
'Pheeroan Aklaff',
'Phil Bodner',
'Phil Bowler',
'Phil Brito',
'Phil Brown (23)',
'Phil Cook (4)',
'Phil Davidson (5)',
'Phil Feather',
'Phil Flanagan',
'Phil Flanigan',
'Phil Giacobbi',
'Phil Giardina',
'Phil Gilbert',
'Phil Grossman',
'Phil Herring',
'Philip Catherine',
'Philip Goldberg',
'Philip Harper',
'Philippe Brun',
'Philippe Caillat',
'Philippe Chayeb',
'Philippe Slominski',
'Philippe Soirat',
'Philipp Schaufelberger',
'Philipp Wachsmann',
'Philip West',
'Philip Woo',
'Phil Kraus',
'Phil Leshin',
'Phillip Guilbeau',
'Phillip Wilson',
'\'Philly\' Joe Jones',
'Phil Markowitz',
'Phil Moore III',
'Phil Napoleon',
'Phil Nemoli',
'Phil Olivella',
'Phil Palmer (2)',
'Phil Seamen',
'Phil Stephens',
'Phil Sunkel',
'Phil Upchurch',
'Phil Urso',
'Phil Viscuglia',
'Phil Wilson',
'Phil Woods',
'Phil Worde',
'Phil Wright',
'Phineas Newborn Jr.',
'Phyllis Pinkerton',
'Piero Leveratto',
'Pierre Allier',
'Pierre Bergeret',
'Pierre Boussaguet',
'Pierre Brun (2)',
'Pierre Cavalli',
'Pierre Dørge',
'Pierre Favre',
'Pierre Ferret',
'Pierre Fouad',
'Pierre Josephs',
'Pierre Lemarchand',
'Pierre Michelot',
'Pierre Pagliaiso',
'Pierre Pagliano',
'Pierre Spiers',
'Pierre Thibaud',
'Pierre Zepilli',
'Piet Noordijk',
'Pietro Tonolo',
'Pinky Savitt',
'Pinky Williams',
'Pino Minafra',
'Pino Palladino',
'Piotr Wojtasik',
'Plas Johnson',
'Pokey Carriere',
'Pola Roberts',
'Pops Foster',
'Porky Cohen',
'Porter Grainger',
'Porter Kilbert',
'Portinho',
'Preston Jackson',
'Preston Love',
'Prince Lasha',
'Prince Robinson',
'Pritchard Cheesman',
'Pud Brown',
'Punch Miller',
'Purnell Rice',
'Putney Dandridge',
'Putte Wickman',
'Quentin Jackson',
'Quentin Warren',
'Quincy Davis',
'Quincy Jones',
'Quin Davis',
'Quinn Davis',
'Quinn Wilson',
'Rachael Steuermann',
'Rachel Z',
'Rae Pearl',
'Rafael \'Felo\' Barrio',
'Rafael \'Tata\' Palau',
'Rafik Abdullah',
'Rainer Brüninghaus',
'Rainer Grimm',
'Rajko Milosavljević',
'Rale Oberpichler',
'Ralf Hübner',
'Ralf Isakson',
'Ralph Aldridge',
'Ralph Blaze',
'Ralph Bledsoe',
'Ralph Bowen',
'Ralph Burns',
'Ralph Collier',
'Ralph Copsey',
'Ralphe Armstrong',
'Ralph Escudero',
'Ralph Grierson',
'Ralph Hamilton (2)',
'Ralph Hamperian',
'Ralph Hansell',
'Ralph Hawkins',
'Ralph Humphrey',
'Ralph Lalama',
'Ralph Lane (2)',
'Ralph Lee (2)',
'Ralph Martin',
'Ralph Martin (3)',
'Ralph Moore (2)',
'Ralph Muzillo',
'Ralph Olson',
'Ralph Osborne',
'Ralph Peña',
'Ralph Penland',
'Ralph Peterson',
'Ralph Pfeffner',
'Ralph Rayner',
'Ralph Schaeffer',
'Ralph Schécroun',
'Ralph Sharon',
'Ralph Sutton (2)',
'Ralph Towner',
'Ramesh Shotham',
'Ramon Banda',
'Ramon Lopez',
'Ramsey Ameen',
'Ramsey Lewis',
'Randall Connors',
'Randall Hawes',
'Randall Miller',
'Randy Aldcroft',
'Randy Bellerjean',
'Randy Bernsen',
'Randy Brecker',
'Randy Brooks (3)',
'Randy Drake',
'Randy Emerick',
'Randy Jackson',
'Randy Jones (3)',
'Randy Kaye',
'Randy Peterson',
'Randy Russell',
'Randy Sabien',
'Randy Tomasello',
'Randy Weston',
'Raoul Poliakin',
'Raoul Romero',
'Raphael Kramer',
'Raphael Taylor',
'Raphe Malik',
'Rashied Ali',
'Rasul Siddik',
'Ratzo B. Harris',
'Raul Rekow',
'Ravi Coltrane',
'Ray Abrams',
'Ray Alexander',
'Ray Alonge',
'Ray Anderson',
'Ray Anthony',
'Ray Armando',
'Ray Barretto',
'Ray Bauduc',
'Ray Beckenstein',
'Ray Beller',
'Ray Biondi',
'Ray Bojorquez',
'Ray Borden',
'Ray Brown',
'Ray Brown (12)',
'Ray Brown (2)',
'Ray Bryant',
'Ray Charles',
'Ray Chew',
'Ray Collins',
'Ray Conniff',
'Ray Connor',
'Ray Copeland',
'Ray Crawford',
'Ray Davies (3)',
'Ray Draper',
'Ray Drummond',
'Ray Ellis',
'Ray Florian',
'Rayford Griffin',
'Ray Greene (2)',
'Ray Hagan',
'Ray Hagen',
'Ray Hopfner',
'Ray Kelley',
'Ray Klein',
'Ray Leatherwood',
'Ray Linn',
'Ray Maldonado',
'Ray Mantella',
'Ray Mantilla',
'Ray Martinez (3)',
'Ray McKinley',
'Ray McKinney',
'Ray Menhennick',
'Ray Michaels',
'Raymond Cohen',
'Raymond Crisara',
'Raymond Droz',
'Raymond Fal',
'Raymond Fol',
'Raymond Fonsèque',
'Raymond Guiot',
'Raymond Hill',
'Raymond Katarzynsky',
'Raymond Le Sénéchal',
'Raymond Orr',
'Raymond Pounds',
'Raymond Scott',
'Raymond Shiner',
'Raymond Tunia',
'Ray Mosca',
'Ray Nance',
'Ray Neapolitan',
'Ray Norman',
'Ray Perry',
'Ray Pitts',
'Ray Pizzi',
'Ray Pohlman',
'Ray Premru',
'Ray Price (3)',
'Ray Reed',
'Ray Rossi (2)',
'Ray Sherman',
'Ray Siegel',
'Ray Sikora',
'Ray Sims',
'Ray Starling',
'Ray Toland',
'Ray Triscari',
'Ray Turner',
'Ray Turner (7)',
'Ray Warleigh',
'Ray Wetzel',
'Ray White (2)',
'Ray Winslow',
'Rebecca Borchert',
'Red Ballard',
'Red Battistelli',
'Red Bone (2)',
'Red Burns',
'Red Callender',
'Red Dorris',
'Red Garland',
'Red Gingler',
'Red Holloway',
'Red Lacky',
'Red Loring',
'Red Mayer',
'Red McKenzie',
'Red Mitchell',
'Red Nichols',
'Red Norvo',
'Red Prysock',
'Red Richards',
'Red Rodney',
'Red Saunders',
'Red Scheps',
'Red Wootten',
'Reggie Johnson',
'Reggie Washington',
'Reggie Workman',
'Reginald Veal',
'Reid Anderson',
'Rein De Graaff',
'Reiner Winterschladen',
'Reinhard Schwartz',
'Reinhold Hirth',
'Remo Biondi',
'Remo Palmieri',
'Rémy Francis',
'Renaldo Jackson',
'Renato Sellani',
'Rene Bloch',
'René \'Challain\' Ferret',
'René Duchossoir',
'Renee Rosnes',
'Rene Hall',
'Rene McLean',
'René Mosele',
'René Thomas',
'René Urtreger',
'Reuben Brown (2)',
'Reuben Cole',
'Reuben Phillips',
'Reuben Rogers',
'Reunald Jones',
'Rex Morris',
'Rex Peer',
'Rex Stewart',
'Reynaldo Jorge',
'Ricardo Ray',
'Ricardo Strobert',
'Riccardo Del Fra',
'Richard Allen',
'Richard Baker',
'Richard Beirach',
'Richard Berg (3)',
'Richard Bona',
'Richard Boone',
'Richard Bullock',
'Richard Clarke (5)',
'Richard Cooper (2)',
'Richard Davis (2)',
'Richard \'Dick\' Fullbright',
'Richard Dollarhide',
'Richard Edwards (2)',
'Richard Eliot',
'Richard Ellington',
'Richard Evans (2)',
'Richard Galliano',
'Richard Harris (26)',
'Richard Henry',
'Richard Hixson',
'Richard Hurwitz',
'Richard Iles',
'Richard Kermode',
'Richard Leith',
'Richard Meisterman',
'Richard Murphy (3)',
'Richard Perissi',
'Richard Perry (2)',
'Richard Powell',
'Richard Pratt (2)',
'Richard Resnicoff',
'Richard Simon (4)',
'Richard Smith (31)',
'Richard Starkey',
'Richard Steacker',
'Richard Sussman',
'Richard Tee',
'Richard Thompson (3)',
'Richard Torres',
'Richard Williams',
'Richard Winter (3)',
'Richard Wyands',
'Rich Daniels',
'Rich DeRosa',
'Richie Cole',
'Richie Crabtree',
'Richie Frost',
'Richie Goods',
'Richie Kamuca',
'Richie Kotzen',
'Richie La Bamba',
'Richie Powell',
'Rich Perry',
'Rich Rajewski',
'Rick Canoff',
'Rick Centalonza',
'Rick Condit',
'Rick Culver',
'Rick Davis',
'Rick Henderson',
'Rick Hollander',
'Rick Kiefer',
'Rick Laird',
'Rick Mann',
'Rick Margitza',
'Rick Rozie',
'Rick Stepton',
'Rick Torcaso',
'Rick Visone',
'Ricky Brauer',
'Ricky Brown (2)',
'Ricky Collins',
'Ricky Ford',
'Ricky Lawson',
'Rico Reyes',
'Rigby Powell',
'Riley B. King',
'Riley Mullins',
'Riley Weston',
'Ringo Hirth',
'Rita Castel',
'Rob Adam',
'Rob Agerbeek',
'Rob Bargad',
'Robben Ford',
'Rob Crowder',
'Robert Ashton',
'Robert Berrenson',
'Robert Bockholt',
'Robert Brookins',
'Robert Collier',
'Robert \'Cookie\' Mason',
'Robert Crowder',
'Robert Crowder (2)',
'Robert Cummings',
'Robert Cusumano',
'Robert Demmer',
'Robert DiDomenica',
'Robert Drasnin',
'Robert Dubow',
'Robert Edward Pring',
'Robert \'Eppie\' Jackson',
'Robert \'Frog\' Camarena',
'Robert Gil',
'Robert Hardaway',
'Robert Haynes (2)',
'Robert Henderson (3)',
'Robert Hurst',
'Robert Irving III',
'Robert Johnson (56)',
'Robert Jordan',
'Robert Keller',
'Robert Leslie Hurst III',
'Robert Mason (6)',
'Robert Maxwell',
'Robert Millikan',
'Robert Moore',
'Robert Northern',
'Roberto Bellatalla',
'Roberto Casanova (2)',
'Roberto Della Grotta',
'Roberto Gatto',
'Roberto Miranda',
'Roberto Monti (2)',
'Roberto Rodriguez (2)',
'Roberto Roena',
'Robert Payne',
'Robert Politzer',
'Robert Popwell',
'Robert Robinson (4)',
'Robert Scott (4)',
'Robert Seastrom',
'Robert Swisshelm',
'Robert Thomas Jr.'
'Robert Trowers',
'Robert Yance',
'Rob Franken',
'Rob Howard',
'Robin Eubanks',
'Robin Gibb',
'Robin Gould',
'Robin Kenyatta',
'Rob Langereis',
'Rob Madna',
'Rob McConnell',
'Rob Middleton (3)',
'Rob Mounsey',
'Rob Pronk',
'Rob Turk',
'Rob van den Broeck',
'Rob Williams (15)',
'Rocky Boyd',
'Rocky Coluccio',
'Rocky Lombardo',
'Rod Adam',
'Rod Levitt',
'Rod Morgenstein',
'Rodney Cajka',
'Rodney Franklin',
'Rodney Holmes',
'Rodney Jones',
'Rodney Levitt',
'Rodney Ogle',
'Rodney Richardson',
'Rodney Whitaker',
'Rod Rodriguez',
'Rod Williams',
'Roger Blank',
'Roger Boyd (2)',
'Roger Chapman',
'Roger Chaput',
'Roger Courcel',
'Roger Dale',
'Roger DeLillo',
'Roger Ellick',
'Roger Grasset',
'Roger Guérin',
'Roger Hodgson',
'Roger Holmes',
'Roger Humphries',
'Roger Hurd',
'Roger Ingram',
'Roger Jannotta',
'Roger Johnston',
'Roger Jones',
'Roger Kellaway',
'Roger Neumann',
'Roger Newman',
'Roger Paraboschi',
'Roger Pemberton',
'Roger Ramirez',
'Roger Rampton',
'Roger Rosenberg',
'Roger Wolfe Kahn',
'Roland Hanna',
'Roland Kirk',
'Roland Kovac',
'Roland Prince',
'Roland Verdon',
'Roland Wittich',
'Rolf Ahrens',
'Rolf Berg',
'Rolf Ericson',
'Rolf Goldstein',
'Rolf Kästel',
'Rolf Kühn',
'Rolf Tragauer',
'Rollice Dale',
'Rollo Garberg',
'Rolly Bundock',
'Romeo Penque',
'Romero Lubambo',
'Ronald Clyne',
'Ronald Cooper',
'Ronald Westray',
'Ron Altbach',
'Ron Banks',
'Ron Barrows',
'Ron Blake',
'Ron Bridgewater',
'Ron Burton',
'Ron Carter',
'Ron Crotty',
'Ron Davis',
'Ron Escheté',
'Ron Feuer',
'Ron Goodwin',
'Ron Hannah (2)',
'Ron Howerton',
'Ron Jackson (9)',
'Ron Karpman',
'Ron Keller',
'Ron King',
'Ron Lankone',
'Ron Lawrence',
'Ron Loofbourrow',
'Ron Lundberg',
'Ron Mathewson',
'Ron McClure',
'Ron Meyers',
'Ron Miller',
'Ron Myers',
'Ronnell Bright',
'Ronnie Ball',
'Ronnie Bedford',
'Ronnie Boykins',
'Ronnie Burrage',
'Ronnie Cuber',
'Ronnie Foster',
'Ronnie Free',
'Ronnie Greb',
'Ronnie Gubertini',
'Ronnie Jones',
'Ronnie Mathews',
'Ronnie Ossa',
'Ronnie Perry',
'Ronnie Rochat',
'Ronnie Ross',
'Ronnie Rubin',
'Ronnie Scott',
'Ronnie Stephenson',
'Ronnie Verrell',
'Ronnie Zito',
'Ronny Lang',
'Ron Odrich',
'Ron Paley',
'Ron Perry (3)',
'Ron Rooley',
'Ron Simmonds',
'Ron Starr',
'Ron Stout',
'Ron Tooley',
'Ron Tutt',
'Ron Vincent',
'Roosevelt Wardell',
'Rosario Bonaccorso',
'Roscoe Mitchell',
'Rossano Sportiello',
'Ross Konikoff',
'Ross Tompkins',
'Roswell Rudd',
'Roy Ayers',
'Roy Babbington',
'Roy Bargy',
'Roy Brooks',
'Roy Burns',
'Roy Burrowes',
'Roy Caton',
'Roy Eldridge',
'Roy Estrada',
'Roy Frazee',
'Roy Freeze',
'Roy Hargrove',
'Roy Harte',
'Roy Haynes',
'Roy Hobson',
'Roy Johnson (3)',
'Roy Kral',
'Roy Main',
'Roy McCoy',
'Roy McCurdy',
'Roy Nathan',
'Roy Poper',
'Roy Porter',
'Roy Reynolds',
'Roy Wiegand',
'Roy Willox',
'R.Q. Dickerson',
'Rube Crozier',
'Ruben Blades',
'Ruben Ladron De Guevara',
'Ruben Leon',
'Ruben McFall',
'Ruby Braff',
'Ruby James',
'Ruby Weinstein',
'Rude De Luca',
'Rudi Füsers',
'Rudi Kregcyck',
'Rudi Reindl',
'Rudi Sehring',
'Rudi Wilfer',
'Rudolf Dašek',
'Rudolf Hansen',
'Rudolf Josel',
'Rudolf Ticháček',
'Rudolph Tanza',
'Rudy Bosch',
'Rudy Collins',
'Rudy Jackson',
'Rudy Novak',
'Rudy Powell',
'Rudy Rutherford',
'Rudy Taylor (2)',
'Rudy Williams',
'Rufus Jones',
'Rufus Reid',
'Rufus Wagner',
'Run-DMC',
'Rune Carlsson',
'Runo Ericksson',
'Rupert Cole',
'Russ Andrews',
'Russ Burgher',
'Russ Cantor',
'Russ Cheever',
'Russ Dufort',
'Russell Brown',
'Russell Campbell',
'Russell Ferrante',
'Russell Garcia',
'Russell George',
'Russell Gunn',
'Russell Jacquet',
'Russell Malone',
'Russell Procope',
'Russell Smith',
'Russell Stone',
'Russ Freeman',
'Russ Iverson',
'Russ Johnson',
'Russ Lossing',
'Russ Phillips',
'Russ Saunders',
'Russ Wagner',
'Rusty Dedrick',
'Rusty Holloway',
'Rusty Jones',
'Ruth Hill (2)',
'Ruth Pointer',
'Ruth Price',
'Ruth Underwood',
'Ruud Brink',
'Ryan Carniaux',
'Ryan Kisor',
'Ryo Kawasaki',
'Sabu Martinez',
'Sacha Distel',
'Sadao Watanabe',
'Sa Davis',
'Sadi',
'Saheb Sarbib',
'Sahib Shihab',
'Sal Amico',
'Sal Cuevas',
'Sal Dettore',
'Sal Franzella',
'Sal Giorgianni',
'Salih Sadiković',
'Sal Lozano',
'Sal Marquez',
'Sal Mosca',
'Sal Nistico',
'Sal Salvador',
'Sal Spicola',
'Salvatore Bonafede',
'Sam Allen',
'Sam Blank',
'Sam Brown (2)',
'Sam Burtis',
'Sam Caplan',
'Sam Cassano',
'Sam Conte (2)',
'Sam Dasberg',
'Sam Dockery',
'Sam Donahue',
'Sam Fedi',
'Sam Firmature',
'Sam Freed',
'Sam Gill',
'Sam Herman',
'Sam Hopkins',
'Sam Hurt',
'Sam Hyster',
'Sam Jones',
'Sam Krupit',
'Sam Listengart',
'Sam Margolis',
'Sam Marowitz',
'Sam Massenberg',
'Sam Middleman',
'Sam Most',
'Sam Musiker',
'Sammy Armato',
'Sammy Davis Jr.',
'Sammy Figueroa',
'Sammy Price',
'Sammy Shapiro',
'Sammy Spumberg',
'Sammy Taylor',
'Sam Noto',
'Sam Persoff',
'Sam Rice',
'Sam Rivers',
'Sam Rosen (2)',
'Sam Rosenblum',
'Sam Ross',
'Sam Rubinowitch',
'Sam Sachelle',
'Sam Scavone',
'Sam Shapiro (2)',
'Sam Simmons',
'Sam Singer (2)',
'Sam Skolnick',
'Sam Skolnik',
'Sam Speed (2)',
'Sam Staff',
'Sam Taylor (2)',
'Sam Taylor (4)',
'Sam Turner (2)',
'Samuel Blaser',
'Samuel Cytron',
'Samuele Garofoli',
'Sam Weiss',
'Sam Woodyard',
'Sam Yahel',
'Sandro Satta',
'Sandy Block',
'Sandy Mosse',
'Sandy Siegelstein',
'Sandy Williams',
'Sanford Gold',
'Sangoma Everett',
'Santi Debriano',
'Santo Russo',
'Santo Savino',
'Santos Colón',
'Sarah Vaughan',
'Sascha Armbruster',
'Sascha Gotowtschikow',
'Sasha Sims',
'Saxie Mansfield',
'Scoops Carey',
'Scott Bentall',
'Scott Colley',
'Scott Edwards (2)',
'Scott Hamilton',
'Scott Jurek',
'Scott LaFaro',
'Scott Lee (5)',
'Scott Morris',
'Scott Robinson (2)',
'Scott Wagstaff',
'Scott Wendholt',
'Scotty Holt',
'Scotville Brown',
'Scoville Brown',
'Seamus Blake',
'Sean Hopper',
'Sean Jones (2)',
'Sebastian Giacco',
'Sébastien Boisseau',
'Seb Mercurio',
'Seldon Powell',
'Seneca Black',
'Seppo Paakkunainen',
'Seretta Wright',
'Serge Chaloff',
'Sérgio Mendes',
'Seymour Barab',
'Seymour Goldfinger',
'Shad Collins',
'Shadow Wilson',
'Shake Keane',
'Shankar',
'Sharel Cassity',
'Sharon Freeman',
'Sheila Escovedo',
'Sheila Jordan',
'Shelley Carrol',
'Shelley Denny',
'Shelly Berg',
'Shelly Gold',
'Shelly Manne',
'Shelton Heath',
'Shelton Hemphill',
'Shep Shepherd',
'Sheridon Stokes',
'Sherman Darby',
'Sherman Ferguson',
'Sheryl Easly',
'Shinji Mori',
'Shirley Clay',
'Shirley Horn',
'Shirley Scott',
'Shirley Thompson (2)',
'Shorty Allen',
'Shorty McConnell',
'Shorty Roeder',
'Shorty Rogers',
'Shorty Sherock',
'Shunzo Ohno',
'Sid Brokaw',
'Sid Brown',
'Sid Bulkin',
'Sid Cooper',
'Sid Feller',
'Sid Harris (3)',
'Sid Horowitz',
'Sid Jacobs',
'Sid Jekowsky',
'Sidney Arodin',
'Sidney Bechet',
'Sidney Brecher',
'Sidney Catlett',
'Sidney De Paris',
'Sidney Edwards',
'Sidney Gross',
'Sidney Perlmutter',
'Sid Stoneburn',
'Sid Weiss',
'Siegfried Kessler',
'Siegfried Schmidt (3)',
'Siegfried Schwab',
'Sigfreid Trager',
'Simona Caucia',
'Simon Bell',
'Simon Brehm',
'Simone Haggiag',
'Sindel Kopp',
'Singleton Palmer',
'Siobhain',
'Sir Charles Thompson',
'Si Zentner',
'Skeeter Best',
'Skeets Herfurt',
'Skip Beckwith',
'Skip Hall',
'Skip Layton',
'Skip Martin',
'Skip Nelson',
'Skippy Desair',
'Skippy Galluccio',
'Slam Stewart',
'Slick Jones',
'Slide Hampton',
'Slim Gaillard',
'Smith Ballew',
'Snooky Young',
'Sol Geskin',
'Sol Gubin',
'Sol Kane',
'Sol Kindler',
'Sol Moore',
'Solomon G. Ilori',
'Sol Schlinger',
'Sonelius Smith',
'Sonny Berman',
'Sonny Brown',
'Sonny Clark',
'Sonny Cohn',
'Sonny Costanzo',
'Sonny Criss',
'Sonny Dallas',
'Sonny Dunham',
'Sonny Fortune',
'Sonny Greer',
'Sonny Igoe',
'Sonny Johnson',
'Sonny Kenn',
'Sonny Lee',
'Sonny Mann (3)',
'Sonny Okosun',
'Sonny Parker',
'Sonny Payne',
'Sonny Red',
'Sonny Rich (2)',
'Sonny Rollins',
'Sonny Russo',
'Sonny Sharrock',
'Sonny Simmons',
'Sonny Stitt',
'Sonny Truitt',
'Sonny White',
'Sorin Romanescu',
'Spanky Davis',
'Spanky DeBrest',
'Spaulding Givens',
'Specs Powell',
'Specs Wright',
'Spencer Barefield',
'Spencer Clark (2)',
'Spencer Odom',
'Spider Webb (2)',
'Spiegle Willcox',
'Spike Hughes',
'Spike Jones',
'Spud Murphy',
'Stacy Dillard',
'Stacy Dillars',
'Stafford James',
'Stafford Simon',
'Stan Doughty',
'Stan Fishelson',
'Stan Fletcher',
'Stan Foster (2)',
'Stan Freeman',
'Stan Getz',
'Stan Harris (2)',
'Stan Hasselgard',
'Stanislav Sulkovský',
'Stan Kenton',
'Stan king',
'Stan Levey',
'Stanley Chaloupka',
'Stanley Clarke',
'Stanley Cowell',
'Stanley Dance',
'Stanley Jordan',
'Stanley Kay',
'Stanley Mendelson',
'Stanley Payne',
'Stanley Plummer',
'Stanley Spiegelman',
'Stanley Turrentine',
'Stanley Webb',
'Stanley Wilson',
'Stan Palmer (2)',
'Stan Popper',
'Stan Puls',
'Stan Robinson',
'Stan Roderick',
'Stan Slotter',
'Stan Stanchfield',
'Stan Steckler',
'Stan Sulzmann',
'Stanton Davis',
'Stan Tracey',
'Stan Wrightsman',
'Stash O\'Laughlin'
'Steady Nelson',
'Stefan Hansson',
'Stefan Karlsson',
'Stefano Battaglia',
'Stefano Bollani',
'Stefan Pintev',
'Stefan Von Dobrzynski',
'Steffen Schorn',
'Stefon Harris',
'Stein Erik Tafjord',
'Stéphane Belmondo',
'Stephan Eggert',
'Stéphane Grappelli',
'Stephen Furtado',
'Stephen McCraven',
'Stephen Scott (5)',
'Stephen Wick',
'Sterling Bose',
'Sterling Magee',
'Sterling Marlow',
'Sterling Marlowe',
'Sterling McGee',
'Steve Allen (3)',
'Steve Backer',
'Steve Berrios',
'Steve Bohannon',
'Steve Brown (2)',
'Steve Brown (3)',
'Steve Brown (6)',
'Steve Campos',
'Steve Cardenas',
'Steve Carr (10)',
'Steve Cobb',
'Steve Coleman',
'Steve Davis',
'Steve Davis (7)',
'Steve Devich',
'Steve Ellington',
'Steve Erquiaga',
'Steve Ferrone',
'Steve Gadd',
'Steve Galloway',
'Steve Gilmore',
'Steve Giordano',
'Steve Grossman',
'Steve Harrow',
'Steve Hass',
'Steve Hawk (4)',
'Steve Hester',
'Steve Houghton',
'Steve Huffsteter',
'Steve Johns',
'Steve Jordan (3)',
'Steve Khan',
'Steve Kohlbacher',
'Steve Kravitz',
'Steve Kroon',
'Steve Kuhn',
'Steve Lacy',
'Steve LaSpina',
'Steve Lederer',
'Steve Lipkins',
'Steve Little',
'Steve Lukather',
'Steve Mann (7)',
'Steve Marcus',
'Steve McCall',
'Steven Bernstein',
'Steve Nelson',
'Steve Novosel',
'Steve Peregrin Took',
'Steve Perlow',
'Steve Perry',
'Steve Porter (6)',
'Steve Potts',
'Steve Rodby',
'Steve Schaeffer',
'Steve Sidwell',
'Steve Slagle',
'Steve Smith (5)',
'Steve Swallow',
'Steve Swell',
'Steve Thornton',
'Steve Turre',
'Steve Van Zandt',
'Steve Vasconcellos',
'Steve Wallace',
'Steve Waterman',
'Steve Watts (2)',
'Steve White (22)',
'Steve White (3)',
'Steve Wiest',
'Steve Williams (5)',
'Steve Wilson (2)',
'Steve Winwood',
'Steve Zenz',
'Stevie Wonder',
'Stewart Anderson (2)',
'Stewart Bruner',
'Stewart Copeland',
'Stewart Undem',
'Stew Pletcher',
'Sticks Evans',
'Stiv Bators',
'Stix\' Hooper',
'Stomu Takeishi',
'Stuart Anderson (4)',
'Stuart Blumberg',
'Stuart Brooks',
'Stuart Olsen (2)',
'Stubby Sebastian',
'Stuff Combe',
'Stuff Smith',
'Stu Goldberg',
'Stu Haimer',
'Stu Martin',
'Sture Nordin',
'Stu Williamson',
'Sue Evans',
'Sue Glover',
'Sue Manchester',
'Sue Raney',
'Sue & Sunny',
'Sumi Tonooka',
'Sune Spångberg',
'Sunil Garg',
'Sunnie Paxson',
'Sunny Kim',
'Sunny Leslie',
'Sunny Murray',
'Sunny Skylar',
'Sun Ra',
'Susan Tallman (2)',
'Suzette Moriarty',
'Suzy Creamcheese',
'Sven Bollhem',
'Svend-Erik Nørregaard',
'Sy Baker',
'Sy Berger',
'Syd Pearlmutter',
'Sylvester \'Vess\' Payne',
'Sylvia Cuenca',
'Sylvia Ruderman',
'Sylvio Gualda',
'Sy Miroff',
'Sy Oliver',
'Sy Salzberg',
'Tab Smith',
'Tadashi Namba',
'Tadd Dameron',
'Taft Jordan',
'Takeshi Inomata',
'Tak Takvorian',
'Tal Farlow',
'Talib Daawud',
'Tani Tabbal',
'Tank Butterball',
'Tanya Darby',
'Tarteboulle',
'Tarus Mateen',
'Tasso Harris',
'Taswell Baird',
'Tate Houston',
'Tatsuya Nakamura (2)',
'Tatum Greenblatt',
'T-Bone Walker',
'T-Bone Wolk',
'Tchangodei',
'Ted Barnett',
'Ted Blume',
'Ted Brinson (2)',
'Ted Brown',
'Ted Casher',
'Ted Currie',
'Ted Curson',
'Teddi King',
'Ted Donnelly',
'Ted Dunbar',
'Teddy Brannon',
'Teddy Buckner',
'Teddy Charles',
'Teddy Cole',
'Teddy Cypron',
'Teddy Edwards',
'Teddy Hill',
'Teddy Kotick',
'Teddy Lee (2)',
'Teddy McRae',
'Teddy Napoleon',
'Teddy Nixon',
'Teddy Pendergrass',
'Teddy Saunders',
'Teddy Smith',
'Teddy Sommer',
'Teddy Stewart',
'Teddy Walters',
'Teddy Wilson',
'Teddy Windholz',
'Ted Efantis',
'Ted Fields',
'Ted Goddard',
'Ted Gompers',
'Ted Heath',
'Ted Kelly',
'Ted Klages',
'Ted Lewis',
'Ted Lo',
'Ted McCord',
'Ted Nash',
'Ted Nash (2)',
'Ted Richardson',
'Ted Robinson (2)',
'Ted Romersa',
'Ted Rosen',
'Ted Rosenthal',
'Ted Sajdyk',
'Ted Seibs',
'Ted Sturgis',
'Ted Vesely',
'Teo Macero',
'Terell Stafford',
'Terence Blanchard',
'Terje Rypdal',
'Terje Venaas',
'Terri Lyne Carrington',
'Terry Adams (2)',
'Terry Allen (6)',
'Terry Clarke',
'Terry Connell',
'Terry Gibbs',
'Terry Jenkins',
'Terry Jennings',
'Terry Layne',
'Terry Pollard',
'Terry Riley',
'Terry Rosen',
'Terry Ross (5)',
'Terry Shand',
'Terry Snyder',
'Terry Swope',
'Terry Trotter',
'Terry Woodson',
'Terumasa Hino',
'Tete Montoliu',
'Tetsujiro Obara',
'Tex Beneke',
'Tex Hurst',
'Tex Satterwhite',
'Thad Jones',
'The 450 Voice J.A.M. \'86 Choir',
'The Blue Flames',
'The Caballiers',
'The Herdmen',
'The Intruders',
'Thelonious Monk',
'The Mills Brothers',
'Theodore Cohen',
'Theo Ferstl',
'The Skylarks',
'The Sturcz String Quartet',
'The Terrytones',
'Thilo Von Westernhagen',
'Thomas Bettermann',
'Thomas Bramerie',
'Thomas Buckner',
'Thomas Chapin',
'Thomas Clausen',
'Thomas Crump',
'Thomas Garling',
'Thomas Grider',
'Thomas Heberer',
'Thomas Kelly (2)',
'Thomas Mitchell',
'Thomas Morgan (4)',
'Thomas Moultrie',
'Thomas Parshley',
'Thomas Porrello',
'Thomas Shepard',
'Thomas Talbert',
'Thomas Von Zurmühlen',
'Thomas Zoller',
'Thore Jederby',
'Thore Swanerud',
'Thornel Schwartz',
'Thorsten Klentze',
'Thurman Barker',
'Thurman Green',
'Thurman Teague',
'Tia Fuller',
'Tibor Elekes',
'Tibor Zelig',
'Tiger Okoshi',
'Till Brönner',
'Tim Berne',
'Tim Burke (4)',
'Tim Hagans',
'Tim Hauff',
'Tim Hopkins',
'Tim Horner',
'Tim Kennedy',
'Timme Rosenkrantz',
'Tim Newman',
'Tim Ray (2)',
'Tim Ries',
'Tim Ryan',
'Tim Williams (4)',
'Tina B',
'Tina Brooks',
'Tina Sinatra',
'Tina Turner',
'Tino Isgrow',
'Tinus Bruyn',
'Tiny \'Bam\' Brown',
'Tiny Grimes',
'Tiny Kahn',
'Tiny Parham',
'Tiny Timbrell',
'Tito Puente',
'Titos Sompa',
'T. Lavitz',
'Tobias Weidinger',
'Toby Guynn',
'Toby Turner',
'Toby Tyler',
'Todd Bashore',
'Todd Canedy',
'Todd Cochran',
'Todd Coolman',
'Todd Gustafson',
'Todd Miller',
'Todd Rhodes',
'Todd Williams',
'Todt Carlton',
'Tom Anastas',
'Tomas Ulrich',
'Tomasz Stańko',
'Tom Azzarello',
'Tom Baken',
'Tom Barney',
'Tom Boras',
'Tom Brechtlein',
'Tom Bridges',
'Tom Child (2)',
'Tom Coster',
'Tom DiCarlo',
'Tom Ehlan',
'Tomeka Reid',
'Tom Fowler',
'Tom Garling',
'Tom Hall (3)',
'Tom Harrell',
'Tom Holden',
'Tom Jones (28)',
'Tom Kennedy (2)',
'Tom Kirkpatrick',
'Tom Kozic',
'Tom Mace',
'Tom Malone',
'Tommaso Vittorini',
'Tom McClung',
'Tom McIntosh',
'Tom Morgan (5)',
'Tommy Allison',
'Tommy Anthony',
'Tommy Benford',
'Tommy Bradascio',
'Tommy Brookins',
'Tommy Bryant',
'Tommy Check',
'Tommy De Rose',
'Tommy Derrick',
'Tommy Dobeck',
'Tommy Dorsey',
'Tommy Douglas',
'Tommy Farr',
'Tommy Flanagan',
'Tommy Fulford',
'Tommy Gonsoulin',
'Tommy Gott',
'Tommy Greco',
'Tommy Gumina',
'Tommy Gwaltney',
'Tommy Hodges',
'Tommy Johnson (2)',
'Tommy LaBella',
'Tommy Ladnier',
'Tommy Lindsay',
'Tommy Linehan',
'Tommy Lopez',
'Tommy Lucas (3)',
'Tommy Mariano',
'Tommy McQuarter',
'Tommy McQuater',
'Tommy Moore (6)',
'Tommy Morgan',
'Tommy Newsom',
'Tommy O\'Neil (2)',
'Tommy Pederson',
'Tommy Peltier',
'Tommy Potter',
'Tommy Romersa',
'Tommy Sheppard',
'Tommy Smith',
'Tommy Stevenson',
'Tommy Thunen',
'Tommy Todd',
'Tommy Turk',
'Tommy Turrentine',
'Tommy Vig',
'Tommy Williams (3)',
'Tom Nygaard',
'Tom Padveen',
'Tom Pastorek',
'Tom Pierson',
'Tom Rainey',
'Tom Ranier',
'Tom Reeves (2)',
'Tom Ringo',
'Tom Satterfield',
'Tom Scott',
'Tom Scully (4)',
'Tom Skinner',
'Tom Slaney',
'Tom Suthers',
'Tom Taylor (10)',
'Tom Timko',
'Tom Varner',
'Tom Warrington',
'Tom Webb',
'Tom Whittaker',
'Tom Williams (7)',
'Tom Wirtel',
'Toni Stricker',
'Tony Aless',
'Tony Anelli',
'Tony Antonelli',
'Tony Barrero',
'Tony Bazley',
'Tony Burrows',
'Tony Campise',
'Tony Carey',
'Tony Coe',
'Tony Colucci',
'Tony Conrad',
'Tony Dagradi',
'Tony D\'Amore',
'Tony Denicola',
'Tony DiMaggio',
'Tony DiMiscio',
'Tony Di Nardi',
'Tony Dumas',
'Tony Duran',
'Tony Faso',
'Tony Felisi',
'Tony Ferina',
'Tony Fisher (2)',
'Tony Gerhardi',
'Tony Gottuso',
'Tony Inzalaco',
'Tony Jefferson',
'Tony Kadleck',
'Tony Klatka',
'Tony Lakatos',
'Tony Lee (5)',
'Tony Leonardi',
'Tony Levin',
'Tony Levin (2)',
'Tony Lindsay',
'Tony Lujan',
'Tony Malaby',
'Tony Marino',
'Tony Miranda',
'Tony Monte (2)',
'Tony Mottola',
'Tony Nichols (2)',
'Tony Osiecki',
'Tony Overwater',
'Tony Oxley',
'Tony Pastor',
'Tony Phillatoni',
'Tony Prentice',
'Tony Price (2)',
'Tony Purrone',
'Tony Reedus',
'Tony Reyes (3)',
'Tony Rizzi',
'Tony Roberts',
'Tony Rodriguez (6)',
'Tony Russo (2)',
'Tony Salvatori',
'Tony Sbarbaro',
'Tony Scodwell',
'Tony Scott (2)',
'Tony Smith (2)',
'Tony Studd',
'Tony Visconti',
'Tony Walls',
'Tony Zimmers',
'Toon van Vliet',
'Toots Mondello',
'Toots Thielemans',
'Torbjörn Hultcrantz',
'Torg Halten',
'Toru Tenda',
'Toshifumi Kawabata',
'Toshiko Akiyoshi',
'Toshiko Mariano',
'Toshio Osumi',
'Tracy Allen',
'Travis Tritt',
'Trevor Bacon',
'Trevor Feldman',
'Trevor Koehler',
'Trey Henry',
'Tricky Sam Nanton',
'Trilok Gurtu',
'Tristan Honsinger',
'Tristan Hyronimus Celander',
'Truck Parham',
'Truett Jones',
'Truman Boardman',
'Truman Quigley',
'Trummy Young',
'Tsutomu Okada',
'Tsuyoshi Yamamoto',
'Tubby Hall',
'Tubby Hayes',
'Turk Van Lake',
'Tutti Camarata',
'Twennynine',
'Tyree Glenn',
'Tyrone Brown',
'Tyrone Washington',
'Uan Rasey',
'Udo Dahmen',
'Udo Lindenberg',
'Uffe Karskov',
'Ugonna Okegwo',
'Ulf Linde',
'Ulf Wakenius',
'Ulysses Livingston',
'Ulysses Owens',
'Umberto Pagnini',
'Unni Duncklau',
'Urbie Green',
'Uri Caine',
'Urszula Dudziak',
'Uschi Brüning',
'Václav Hoza',
'Valerio Perla',
'Valery Ponomarev',
'Varner Barlow',
'Vaughn Wiester',
'Velma Middleton',
'Verne Guertin',
'Vernell Fournier',
'Vern Friley',
'Vernon Alley',
'Vernon Biddle',
'Vernon Brown',
'Vernon King',
'Vernon Martin',
'Vernon Polk',
'Vernon Slater',
'Vernon Smith (2)',
'Vernon Yocum',
'Vern Rowe',
'Vetese Guérino',
'Vic Berton',
'Vic Breidis',
'Vic Briedis',
'Vic Coulson',
'Vic Dickenson',
'Vicente Archer',
'Vic Flick',
'Vic Hamann',
'Vic Harris (2)',
'Vic Juris',
'Vic Lewis',
'Vic McMillan',
'Vic Minichelli',
'Vic Minichiello',
'Victor Bailey',
'Victor Comer',
'Victor Feldman',
'Victor Ford',
'Victor Gaskin',
'Victor Goines',
'Victor Jones (2)',
'Victor Lewis',
'Victor Morosco',
'Victor Pantoja',
'Victor Paz',
'Victor Piemonte',
'Victor Sproles',
'Victor Stern',
'Victor Venegas',
'Victor Wooten',
'Victor Young',
'Vidal Bolado',
'Vidar Johansen',
'Vido Musso',
'Vijay Iyer',
'Viktor Plasil',
'Vince Badale',
'Vince Benedetti',
'Vince Cutro',
'Vince Diaz',
'Vince Forrest',
'Vince Guaraldi',
'Vince Hughes',
'Vince Lateano',
'Vince Maffei',
'Vincenc Kummer',
'Vincent Casino',
'Vincent Chancey',
'Vincent Daniele',
'Vincent Davis (3)',
'Vincent DeRosa',
'Vincent Gardner',
'Vincent Herring',
'Vincent Pirro',
'Vincent Terri',
'Vincent Wilburn',
'Vince Prudente',
'Vinni De Campo',
'Vinnie Burke',
'Vinnie Dean',
'Vinnie Johnson',
'Vinnie Ruggiero',
'Vinnie Talerico',
'Vinnie Tanno',
'Vinnie Thomas',
'Vinny Golia',
'Virgil Gonsalves',
'Virgil Jones',
'Vivien Garry',
'Vladimir Shafranov',
'Vladimír Tymich',
'Volker Kriegel',
'Wadada Leo Smith',
'Waddet Williams',
'Wade Legge',
'Wade Marcus',
'Waldemar Erbe',
'Walfredo De Los Reyes Jr.'
'Wallace Bishop',
'Wallace Davenport',
'Wallace Jones',
'Wallace McMillan',
'Wallace Roney',
'Wallace Snow',
'Wally Barron',
'Wally Kane',
'Wally Morris',
'Wally Wells',
'Walt Benson',
'Walter Bates',
'Walter Benson',
'Walter Benton',
'Walter Bishop Jr.',
'Walter Blanding',
'Walter Bolden',
'Walter Booker',
'Walter Brown',
'Walter Davis Jr.',
'Walter Edelstein',
'Walter Fuller',
'Walter J. Blanton',
'Walter Johnson',
'Walter Knox',
'Walter Mercurio',
'Walter Namuth',
'Walter Nimms',
'Walter Norris',
'Walter Page',
'Walter Perkins',
'Walter Pfyl',
'Walter \'Phatz\' Morris',
'Walter Robinson (4)',
'Walter Schmocker',
'Walter Thomas',
'Walter Williams (3)',
'Walter Yost',
'Walt Levinsky',
'Walt Weiskopf',
'Walt Welscher',
'Walt Yoder',
'Wardell Gray',
'Wardell Thomas',
'Ward Lay',
'Ward Silloway',
'Warne Marsh',
'Warren Barker',
'Warren Bernhardt',
'Warren Bracken',
'Warren Chiasson',
'Warren Covington',
'Warren Fitzgerald (2)',
'Warren Jefferson',
'Warren Luckey',
'Warren Smith',
'Warren Vaché',
'Warren Weidler',
'Waylon Jennings',
'Wayman Carver',
'Waymon Reed',
'Wayne Andre',
'Wayne Bergeron',
'Wayne Darling',
'Wayne DeSilva',
'Wayne Dockery',
'Wayne Dunstan',
'Wayne Goodman',
'Wayne Henderson',
'Wayne Horvitz',
'Wayne Naus',
'Wayne Nichols',
'Wayne Oliver',
'Wayne Shorter',
'Webster Lewis',
'Webster Young',
'Wellman Braud',
'Welton Gite',
'Wendell Culley',
'Wendell Kelly',
'Wendell Marshall',
'Wendy Haas',
'Werner Feldgrill',
'Werner Giertz',
'Werner Rönfeldt',
'Wes Brown',
'Wes Hein',
'Wes Hensel',
'Wes Landers',
'Wesley Dean',
'Wesley Jones',
'Wesley Prince',
'Wes Montgomery',
'Wessell Anderson',
'Wes Vaughan',
'Whitey Mitchell',
'Whitey Thomas',
'Wilber Morris',
'Wilbert Baranco',
'Wilbert Hogan',
'Wilbur Bascomb',
'Wilbur Campbell',
'Wilbur De Paris',
'Wilbur Hall',
'Wilbur Harden',
'Wilbur Hogan',
'Wilbur Little',
'Wilburn Stewart',
'Wilbur Schwartz',
'Wilbur Ware',
'Wilbur Wynne',
'Wilby Fletcher',
'Wild Bill Davis',
'Wild Bill Davison',
'Wilfred Middlebrooks',
'Willard Brown',
'Willard Culley',
'Will Bradley',
'Will Downing',
'Willem Breuker',
'William Allen',
'William Austin',
'William Bennett (2)',
'William Bloom (2)',
'William Blue',
'William Boucaya',
'William Brown (38)',
'William \'Cat\' Johnson',
'William Cato',
'William Cepeda',
'William Dirvin',
'William Doty',
'William Franklin (2)',
'William Granzos',
'William Green',
'William Gross',
'William H. Bailey',
'William Henderson',
'William Herndon',
'William Hinshaw',
'William J. Scott',
'William Kurasch',
'William Massingill',
'William Mendenhall',
'William Oscar Smith',
'William O. Smith',
'William Parker',
'William Parker (5)',
'William \'Peppy\' Hinnant',
'William Robinson Jr.',
'William Schaffer',
'William Schiöpffe',
'William Shepherd',
'William Slapin',
'Williams Scott',
'William Winant',
'William Wirges',
'Willie Barton',
'Willie Bobo',
'Willie Colón',
'Willie Cook',
'Willie Dennis',
'Willie Ford',
'Willie Humphrey',
'Willie Jones',
'Willie Jones III',
'Willie Kelley',
'Willie Kizart',
'Willie Lynch',
'Willie Maiden',
'Willie Michael',
'Willie Nelson',
'Willie Pickens',
'Willie Randall',
'Willie Rodriguez',
'Willie Ruff',
'Willie Smith (2)',
'Willie Stump Junior',
'Willie \'The Lion\' Smith',
'Willie Thomas',
'Willie Weeks',
'Willi Marton',
'Willi Meerwald',
'Willi Sanner',
'Willis Jackson',
'Will Johnson (2)',
'Will Lee',
'Willy Lockwood',
'Wilmus Reeves',
'Wilson Myers',
'Wilton Felder',
'Wim Brieffies',
'Wim Ter Bruggen',
'Winard Harper',
'Wingy Manone',
'Winston Welch',
'Władysław Sendecki',
'Wolfgang Ahlers',
'Wolfgang Dauner',
'Wolfgang Engstfeld',
'Wolfgang Köhler',
'Wolfgang Muthspiel',
'Wolfgang Puschnig',
'Wolfgang Schalk',
'Wolfgang Schlüter',
'Wolfgang Zwiauer',
'Woodrow Key (2)',
'Woody Herman',
'Woody James',
'Woody Shaw',
'Woody Theus',
'Wyatt Ruther',
'Wycliffe Gordon',
'Wynonie Harris',
'Wynton Kelly',
'Wynton Marsalis',
'Xavier Davis',
'Yank Lawson',
'Yank Porter',
'Yasuo Arakawa',
'Yngve Åkerberg',
'Yomo Toro',
'Yoron Israel',
'Yoshiaki Masuo',
'Yoshio Suzuki',
'Yoshitaka Uematsu',
'Yoshito Murakami',
'Yoshiyuki Nakamura',
'Yosuke Yamashita',
'Yusef Lateef',
'Zachary Bock',
'Zak Starkey',
'Zane Massey',
'Zappy Max',
'Zdeněk Novák',
'Zdeněk Pulec',
'Zeb Julian',
'Zeke Zarchy',
'Zela Terry',
'Ziggy Elman',
'Ziggy Harrell',
'Ziggy Lane',
'Ziggy Vines',
'Zilner Randolph',
'Ziv Ravitz',
'Zlatko Dvoržak',
'Zoltán Lantos',
'Zoot Sims',
'Zutty Singleton',
]

list_transcript = []
list_transcript.append('Art Pepper_Anthropology')
list_transcript.append('Art Pepper_Blues For Blanche')
list_transcript.append('Art Pepper_Desafinado')
list_transcript.append('Art Pepper_In A Mellow Tone')
list_transcript.append('Art Pepper_Stardust-1')
list_transcript.append('Art Pepper_Stardust-2')
list_transcript.append('Benny Carter_I Got It Bad')
list_transcript.append('Benny Carter_It\'s A Wonderful World-1')
list_transcript.append('Benny Carter_It\'s A Wonderful World-2')
list_transcript.append('Benny Carter_Just Friends')
list_transcript.append('Benny Carter_Long Ago And Far Away-1')
list_transcript.append('Benny Carter_Long Ago And Far Away-2')
list_transcript.append('Benny Carter_Sweet Lorraine')
list_transcript.append('Benny Goodman_Avalon')
list_transcript.append('Benny Goodman_Handful Of Keys')
list_transcript.append('Benny Goodman_Nobody\'s Sweetheart')
list_transcript.append('Benny Goodman_Runnin\' Wild')
list_transcript.append('Benny Goodman_Tiger Rag-1')
list_transcript.append('Benny Goodman_Tiger Rag-2')
list_transcript.append('Benny Goodman_Whispering')
list_transcript.append('Ben Webster_Bye Bye Blackbird')
list_transcript.append('Ben Webster_Did You Call Her Today')
list_transcript.append('Ben Webster_My Ideal')
list_transcript.append('Ben Webster_Night And Day')
list_transcript.append('Ben Webster_Where Or When')
list_transcript.append('Bix Beiderbecke_I\'m Coming Virginia')
list_transcript.append('Bix Beiderbecke_Margie')
list_transcript.append('Bix Beiderbecke_Riverboat Shuffle')
list_transcript.append('Bix Beiderbecke_Royal Garden Blues')
list_transcript.append('Bix Beiderbecke_Singin The Blues')
list_transcript.append('Bob Berg_Angles')
list_transcript.append('Bob Berg_Blues For Bela')
list_transcript.append('Bob Berg_I Didn\'t Know What Time It Was')
list_transcript.append('Bob Berg_Nature Of The Beast')
list_transcript.append('Bob Berg_No Moe')
list_transcript.append('Bob Berg_Second Sight')
list_transcript.append('Bob Berg_You And The Night And The Music')
list_transcript.append('Brandford Marsalis_Gutbucket Steepy')
list_transcript.append('Brandford Marsalis_Housed From Edward-1')
list_transcript.append('Brandford Marsalis_Housed From Edward-2')
list_transcript.append('Brandford Marsalis_The Nearness Of You')
list_transcript.append('Brandford Marsalis_Three Little Words')
list_transcript.append('Brandford Marsalis_U.M.M.G')
list_transcript.append('Buck Clayton_After Theatre Jump')
list_transcript.append('Buck Clayton_Destination K.C')
list_transcript.append('Buck Clayton_Dickie\'s Dream')
list_transcript.append('Cannonball Adderley_High Fly')
list_transcript.append('Cannonball Adderley_So What')
list_transcript.append('Cannonball Adderley_Star Eyes')
list_transcript.append('Cannonball Adderley_This Here')
list_transcript.append('Cannonball Adderley_Work Song')
list_transcript.append('Charlie Parker_Billie\'s Bounce')
list_transcript.append('Charlie Parker_Blues For Alice')
list_transcript.append('Charlie Parker_Don\'t Blame Me')
list_transcript.append('Charlie Parker_Donna Lee')
list_transcript.append('Charlie Parker_Embraceable You')
list_transcript.append('Charlie Parker_How Deep Is The Ocean')
list_transcript.append('Charlie Parker_K.C. Blues')
list_transcript.append('Charlie Parker_Ko-Ko')
list_transcript.append('Charlie Parker_My Little Suede Shoes')
list_transcript.append('Charlie Parker_Ornithology')
list_transcript.append('Charlie Parker_Out Of Nowhere')
list_transcript.append('Charlie Parker_Scrapple From The Apple')
list_transcript.append('Charlie Parker_Segment')
list_transcript.append('Charlie Parker_Star Eyes')
list_transcript.append('Charlie Parker_Steeplechase')
list_transcript.append('Charlie Parker_Thriving On A Riff')
list_transcript.append('Charlie Parker_Yardbird Suite')
list_transcript.append('Charlie Shavers_Limehouse Blues')
list_transcript.append('Chet Baker_I Fall In Love Too Easily')
list_transcript.append('Chet Baker_Just Friends')
list_transcript.append('Chet Baker_Let\'s Get Lost')
list_transcript.append('Chet Baker_Long Ago And Far Away')
list_transcript.append('Chet Baker_There Will Never Be Another You-1')
list_transcript.append('Chet Baker_There Will Never Be Another You-2')
list_transcript.append('Chet Baker_Two\'s Blues')
list_transcript.append('Chet Baker_You\'d Be So Nice To Come Home To')
list_transcript.append('Chris Potter_Anthropology')
list_transcript.append('Chris Potter_Arjuna')
list_transcript.append('Chris Potter_In A Sentimental Mood')
list_transcript.append('Chris Potter_Item1 D.I.T')
list_transcript.append('Chris Potter_Pop Tune#1')
list_transcript.append('Chris Potter_Rumples')
list_transcript.append('Chris Potter_Togo')
list_transcript.append('Chu Berry_Body And Soul-1')
list_transcript.append('Chu Berry_Body And Soul-2')
list_transcript.append('Clifford Brown_A Night In Tunisia')
list_transcript.append('Clifford Brown_Daahoud')
list_transcript.append('Clifford Brown_George\'s Dilemma')
list_transcript.append('Clifford Brown_I\'ll Remember April_AlternateTake2')
list_transcript.append('Clifford Brown_I\'ll Remember April')
list_transcript.append('Clifford Brown_Jordu')
list_transcript.append('Clifford Brown_Joy Spring')
list_transcript.append('Clifford Brown_Sandu')
list_transcript.append('Clifford Brown_Stompin\' At The Savoy')
list_transcript.append('Coleman Hawkins_Body And Soul')
list_transcript.append('Coleman Hawkins_It\'s Only A Papermoon')
list_transcript.append('Coleman Hawkins_My Blue Heaven')
list_transcript.append('Coleman Hawkins_Perdido')
list_transcript.append('Coleman Hawkins_Sophisticated Lady')
list_transcript.append('Coleman Hawkins_Stompin\' At The Savoy')
list_transcript.append('Curtis Fuller_Blue Train')
list_transcript.append('Curtis Fuller_Down Under')
list_transcript.append('David Liebman_Begin The Beguine')
list_transcript.append('David Liebman_Day & Nite')
list_transcript.append('David Liebman_I\'ve Got You Under My Skin')
list_transcript.append('David Liebman_Milestones')
list_transcript.append('David Liebman_Nica\'s Dream')
list_transcript.append('David Liebman_No Greater Love')
list_transcript.append('David Liebman_Pablo\'s Story')
list_transcript.append('David Liebman_Pendulum')
list_transcript.append('David Liebman_Secret Love')
list_transcript.append('David Liebman_Softly As In A Morning Sunrise')
list_transcript.append('David Liebman_There Will Never Be Another You')
list_transcript.append('David Murray_Ask Me Now')
list_transcript.append('David Murray_Blues For Two-1')
list_transcript.append('David Murray_Blues For Two-2')
list_transcript.append('David Murray_Body And Soul-1')
list_transcript.append('David Murray_Body And Soul-2')
list_transcript.append('David Murray_Chelsea Bridge')
list_transcript.append('Dexter Gordon_Cheesecake')
list_transcript.append('Dexter Gordon_Dextivity')
list_transcript.append('Dexter Gordon_Montmartre')
list_transcript.append('Dexter Gordon_Society Red')
list_transcript.append('Dexter Gordon_Stanley The Steamer')
list_transcript.append('Dexter Gordon_The Rainbow People')
list_transcript.append('Dickie Wells_After Theatre Jump')
list_transcript.append('Dickie Wells_Destination K.C')
list_transcript.append('Dickie Wells_Dickie\'s Dream')
list_transcript.append('Dickie Wells_I Got Rhythm')
list_transcript.append('Dickie Wells_Jo-Jo')
list_transcript.append('Dickie Wells_Six Cats And A Prince')
list_transcript.append('Dizzy Gillespie_Anthropology')
list_transcript.append('Dizzy Gillespie_Be-Bop')
list_transcript.append('Dizzy Gillespie_Blue \'n Boogie')
list_transcript.append('Dizzy Gillespie_Cognac Blues')
list_transcript.append('Dizzy Gillespie_Groovin\' High')
list_transcript.append('Dizzy Gillespie_Hot House')
list_transcript.append('Don Byas_Be-Bop')
list_transcript.append('Don Byas_Body And Soul')
list_transcript.append('Don Byas_Cognac Blues')
list_transcript.append('Don Byas_Harvard Blues-1')
list_transcript.append('Don Byas_Harvard Blues-2')
list_transcript.append('Don Byas_Infidele (Cry)')
list_transcript.append('Don Byas_Out Of Nowhere')
list_transcript.append('Don Byas_Un Amour Pleurait')
list_transcript.append('Don Ellis_I Love You')
list_transcript.append('Don Ellis_Johnny Come Lately')
list_transcript.append('Don Ellis_Out Of Nowhere')
list_transcript.append('Don Ellis_Sweet And Lovely')
list_transcript.append('Don Ellis_You Stepped Out Of A Dream-1')
list_transcript.append('Don Ellis_You Stepped Out Of A Dream-2')
list_transcript.append('Eric Dolphy_245')
list_transcript.append('Eric Dolphy_Aisha')
list_transcript.append('Eric Dolphy_Dahomey Dance')
list_transcript.append('Eric Dolphy_Les')
list_transcript.append('Eric Dolphy_Serene')
list_transcript.append('Fats Navarro_Anthropology_No1')
list_transcript.append('Fats Navarro_Double Talk')
list_transcript.append('Fats Navarro_Good Bait_AlternateTake')
list_transcript.append('Fats Navarro_Good Bait')
list_transcript.append('Fats Navarro_Our Delight')
list_transcript.append('Fats Navarro_The Skunk')
list_transcript.append('Freddie Hubbard_245')
list_transcript.append('Freddie Hubbard_Dolphin Dance')
list_transcript.append('Freddie Hubbard_Down Under')
list_transcript.append('Freddie Hubbard_Maiden Voyage')
list_transcript.append('Freddie Hubbard_Society Red')
list_transcript.append('Freddie Hubbard_Speak No Evil')
list_transcript.append('George Coleman_Maiden Voyage')
list_transcript.append('Gerry Mulligan_Bunny')
list_transcript.append('Gerry Mulligan_Line For Lyons')
list_transcript.append('Gerry Mulligan_Scrapple From The Apple')
list_transcript.append('Gerry Mulligan_The Red Door')
list_transcript.append('Gerry Mulligan_This Can\'t Be Love')
list_transcript.append('Gerry Mulligan_Walking Shoes')
list_transcript.append('Hank Jones_Autumn Leaves')
list_transcript.append('Hank Mobley_Doodlin\'')
list_transcript.append('Hank Mobley_Lady Bird')
list_transcript.append('Hank Mobley_Remember')
list_transcript.append('Hank Mobley_Soul Station')
list_transcript.append('Harry Edison_Did You Call Her Today')
list_transcript.append('Henry Allen_Baby Won\'t You Please Come Home')
list_transcript.append('Herbie Hancock_Agitation')
list_transcript.append('Herbie Hancock_Dolores')
list_transcript.append('Herbie Hancock_Gingerbread Boy')
list_transcript.append('Herbie Hancock_HandJive')
list_transcript.append('Herbie Hancock_Orbits')
list_transcript.append('JC Higginbotham_Baby Won\'t You Please Come Home')
list_transcript.append('JJ Johnson_Blue Mode')
list_transcript.append('JJ Johnson_Blues In The Closet')
list_transcript.append('JJ Johnson_Crazy Rhythm')
list_transcript.append('JJ Johnson_Elora')
list_transcript.append('JJ Johnson_My Funny Valentine')
list_transcript.append('JJ Johnson_Teapot')
list_transcript.append('JJ Johnson_Walkin\'')
list_transcript.append('JJ Johnson_Yesterdays')
list_transcript.append('Joe Henderson_In \'N Out-1')
list_transcript.append('Joe Henderson_In \'N Out-2')
list_transcript.append('Joe Henderson_Johnny Come Lately')
list_transcript.append('Joe Henderson_Punjab')
list_transcript.append('Joe Henderson_Serenity')
list_transcript.append('Joe Henderson_The Sidewinder')
list_transcript.append('Joe Henderson_Totem Pole')
list_transcript.append('Joe Henderson_U.M.M.G')
list_transcript.append('Joe Lovano_Body And Soul-1')
list_transcript.append('Joe Lovano_Body And Soul-2')
list_transcript.append('Joe Lovano_Central Park West')
list_transcript.append('Joe Lovano_Con Alma')
list_transcript.append('Joe Lovano_I Can\'t Get Started')
list_transcript.append('Joe Lovano_Little Willie Leaps In')
list_transcript.append('Joe Lovano_Lonnie\'s Lament-1')
list_transcript.append('Joe Lovano_Work')
list_transcript.append('John Abercrombie_Ralph\'s Piano Waltz')
list_transcript.append('John Coltrane_26-2')
list_transcript.append('John Coltrane_Bessie\'s Blues')
list_transcript.append('John Coltrane_Blues By Five')
list_transcript.append('John Coltrane_Blue Train')
list_transcript.append('John Coltrane_Body And Soul_AlternateTake')
list_transcript.append('John Coltrane_Body And Soul')
list_transcript.append('John Coltrane_Countdown')
list_transcript.append('John Coltrane_Giant Steps-1')
list_transcript.append('John Coltrane_Giant Steps-2')
list_transcript.append('John Coltrane_Impressions_1961')
list_transcript.append('John Coltrane_Impressions_1963')
list_transcript.append('John Coltrane_Mr.P.C')
list_transcript.append('John Coltrane_My Favorite Things-1')
list_transcript.append('John Coltrane_My Favorite Things-2')
list_transcript.append('John Coltrane_Nature Boy')
list_transcript.append('John Coltrane_Nutty')
list_transcript.append('John Coltrane_Oleo')
list_transcript.append('John Coltrane_Soultrane')
list_transcript.append('John Coltrane_So What')
list_transcript.append('John Coltrane_Trane\'s Blues')
list_transcript.append('Johnny Dodds_Got No Blues')
list_transcript.append('Johnny Dodds_Heebie Jeebies')
list_transcript.append('Johnny Dodds_Hotter Than That')
list_transcript.append('Johnny Dodds_Muskrat Ramble')
list_transcript.append('Johnny Dodds_My Heart')
list_transcript.append('Johnny Dodds_Once In A While')
list_transcript.append('Johnny Hodges_Bunny')
list_transcript.append('Johnny Hodges_Early Morning Rock')
list_transcript.append('Joshua Redman_Blues On Sunday')
list_transcript.append('Joshua Redman_Home Fries')
list_transcript.append('Joshua Redman_I Got You')
list_transcript.append('Joshua Redman_Sweet Sorrow')
list_transcript.append('Joshua Redman_Tears In Heaven')
list_transcript.append('Kai Winding_Tiny\'s Blues')
list_transcript.append('Kenny Dorham_Blues In Be-Bop')
list_transcript.append('Kenny Dorham_Doodlin\'')
list_transcript.append('Kenny Dorham_In \'N Out')
list_transcript.append('Kenny Dorham_Lady Bird')
list_transcript.append('Kenny Dorham_Prince Albert')
list_transcript.append('Kenny Dorham_Punjab')
list_transcript.append('Kenny Dorham_Serenity')
list_transcript.append('Kenny Garrett_Brother Hubbard-1')
list_transcript.append('Kenny Garrett_Brother Hubbard-2')
list_transcript.append('Kenny Wheeler_Double Vision')
list_transcript.append('Kenny Wheeler_Pass It On')
list_transcript.append('Kenny Wheeler_Slipped Again')
list_transcript.append('Kid Ory_Got No Blues')
list_transcript.append('Kid Ory_Gut Bucket Blues')
list_transcript.append('Kid Ory_Muskrat Ramble')
list_transcript.append('Kid Ory_Savoy Blues')
list_transcript.append('Kid Ory_Who\'s It')
list_transcript.append('Lee Konitz_All The Things You Are')
list_transcript.append('Lee Konitz_Bop Goes To Leesel')
list_transcript.append('Lee Konitz_Crosscurrent')
list_transcript.append('Lee Konitz_I\'ll Remember April')
list_transcript.append('Lee Konitz_Marshmallow')
list_transcript.append('Lee Konitz_Mean To Me')
list_transcript.append('Lee Konitz_Tautology')
list_transcript.append('Lee Konitz_Wow')
list_transcript.append('Lee Morgan_Blue Train')
list_transcript.append('Lee Morgan_Just One Of Those Things')
list_transcript.append('Lee Morgan_The Sidewinder')
list_transcript.append('Lee Morgan_Totem Pole')
list_transcript.append('Lester Young_After Theatre Jump')
list_transcript.append('Lester Young_Body And Soul')
list_transcript.append('Lester Young_D.B. Blues')
list_transcript.append('Lester Young_Destination K.C')
list_transcript.append('Lester Young_Dickie\'s Dream')
list_transcript.append('Lester Young_Lester Leaps In')
list_transcript.append('Lester Young_Six Cats And A Prince')
list_transcript.append('Lionel Hampton_Avalon')
list_transcript.append('Lionel Hampton_Dinah')
list_transcript.append('Lionel Hampton_High Society')
list_transcript.append('Lionel Hampton_Memories Of You')
list_transcript.append('Lionel Hampton_Runnin\' Wild')
list_transcript.append('Lionel Hampton_Whispering')
list_transcript.append('Louis Armstrong_Basin Street Blues')
list_transcript.append('Louis Armstrong_Big Butter And Egg Man')
list_transcript.append('Louis Armstrong_Cornet Chop Suey')
list_transcript.append('Louis Armstrong_Got No Blues')
list_transcript.append('Louis Armstrong_Gut Bucket Blues')
list_transcript.append('Louis Armstrong_Muskrat Ramble')
list_transcript.append('Louis Armstrong_Once In A While')
list_transcript.append('Louis Armstrong_Savoy Blues')
list_transcript.append('Michael Brecker_Cabin Fever')
list_transcript.append('Michael Brecker_Confirmation')
list_transcript.append('Michael Brecker_Delta City Blues')
list_transcript.append('Michael Brecker_I Mean You')
list_transcript.append('Michael Brecker_Midnight Voyage')
list_transcript.append('Michael Brecker_Naked Soul')
list_transcript.append('Michael Brecker_Never Alone')
list_transcript.append('Michael Brecker_Nothing Personal')
list_transcript.append('Michael Brecker_Peep')
list_transcript.append('Michael Brecker_Song For Bilbao')
list_transcript.append('Miles Davis_Agitation')
list_transcript.append('Miles Davis_Airegin')
list_transcript.append('Miles Davis_Bitches Brew-1')
list_transcript.append('Miles Davis_Bitches Brew-2')
list_transcript.append('Miles Davis_Blues By Five')
list_transcript.append('Miles Davis_Dolores')
list_transcript.append('Miles Davis_E.S.P')
list_transcript.append('Miles Davis_Eighty-One')
list_transcript.append('Miles Davis_K.C. Blues')
list_transcript.append('Miles Davis_Miles Runs The Voodoo Down-1')
list_transcript.append('Miles Davis_Miles Runs The Voodoo Down-2')
list_transcript.append('Miles Davis_Oleo-1')
list_transcript.append('Miles Davis_Oleo-2')
list_transcript.append('Miles Davis_Orbits')
list_transcript.append('Miles Davis_So What')
list_transcript.append('Miles Davis_Trane\'s Blues')
list_transcript.append('Miles Davis_Tune Up')
list_transcript.append('Miles Davis_Vierd Blues')
list_transcript.append('Miles Davis_Walkin\'')
list_transcript.append('Milt Jackson_All The Things You Are')
list_transcript.append('Milt Jackson_Bag\'s Groove')
list_transcript.append('Milt Jackson_Bemsha Swing')
list_transcript.append('Milt Jackson_Don\'t Get Around Much Anymore')
list_transcript.append('Milt Jackson_Softly As In A Morning Sunrise')
list_transcript.append('Milt Jackson_What\'s New')
list_transcript.append('Nat Adderley_Bohemia After Dark')
list_transcript.append('Nat Adderley_Work Song')
list_transcript.append('Ornette Coleman_Bird Food')
list_transcript.append('Ornette Coleman_Chronology')
list_transcript.append('Ornette Coleman_Congeniality')
list_transcript.append('Ornette Coleman_Peace')
list_transcript.append('Ornette Coleman_Ramblin\'')
list_transcript.append('Pat Martino_Along Came Betty')
list_transcript.append('Pat Metheny_All The Things You Are')
list_transcript.append('Pat Metheny_Cabin Fever')
list_transcript.append('Pat Metheny_Midnight Voyage')
list_transcript.append('Pat Metheny_Nothing Personal')
list_transcript.append('Paul Desmond_Alianca-1')
list_transcript.append('Paul Desmond_Alianca-2')
list_transcript.append('Paul Desmond_Alone Together')
list_transcript.append('Paul Desmond_Blue Rondo A La Turk')
list_transcript.append('Paul Desmond_Bossa Antigua')
list_transcript.append('Paul Desmond_Samba Cantina-1')
list_transcript.append('Paul Desmond_Samba Cantina-2')
list_transcript.append('Paul Desmond_The Girl From East 9th Street')
list_transcript.append('Pepper Adams_A Night In Tunisia')
list_transcript.append('Pepper Adams_Early Morning Mood')
list_transcript.append('Pepper Adams_How High The Moon')
list_transcript.append('Pepper Adams_Just One Of Those Things')
list_transcript.append('Pepper Adams_You\'d Be So Nice To Come Home To')
list_transcript.append('Phil Woods_Be My Love')
list_transcript.append('Phil Woods_Cotton Tail')
list_transcript.append('Phil Woods_Crazy Rhythm')
list_transcript.append('Phil Woods_Honeysuckle Rose')
list_transcript.append('Phil Woods_On A Slow Boat To China')
list_transcript.append('Phil Woods_Strollin\' With Pam')
list_transcript.append('Ray Nance_Take The A Train')
list_transcript.append('Red Garland_Oleo')
list_transcript.append('Rex Stewart_Perdido')
list_transcript.append('Roy Eldridge_Body And Soul')
list_transcript.append('Roy Eldridge_King David')
list_transcript.append('Roy Eldridge_St. Louis Blues')
list_transcript.append('Roy Eldridge_The Gasser-1')
list_transcript.append('Roy Eldridge_The Gasser-2')
list_transcript.append('Roy Eldridge_Undecided')
list_transcript.append('Sidney Bechet_Baby Won\'t You Please Come Home')
list_transcript.append('Sidney Bechet_I\'m Coming Virginia')
list_transcript.append('Sidney Bechet_Limehouse Blues')
list_transcript.append('Sidney Bechet_Really The Blues')
list_transcript.append('Sidney Bechet_Summertime')
list_transcript.append('Sonny Rollins_Airegin')
list_transcript.append('Sonny Rollins_Blue Seven-1')
list_transcript.append('Sonny Rollins_Blue Seven-2')
list_transcript.append('Sonny Rollins_Blue Seven-3')
list_transcript.append('Sonny Rollins_I\'ll Remember April_AlternateTake2')
list_transcript.append('Sonny Rollins_Playin\' In The Yard-1')
list_transcript.append('Sonny Rollins_Playin\' In The Yard-2')
list_transcript.append('Sonny Rollins_St. Thomas-1')
list_transcript.append('Sonny Rollins_St. Thomas-2')
list_transcript.append('Sonny Rollins_Tenor Madness')
list_transcript.append('Sonny Rollins_The Everywhere Calypso-1')
list_transcript.append('Sonny Rollins_The Everywhere Calypso-2')
list_transcript.append('Sonny Rollins_Vierd Blues')
list_transcript.append('Sonny Stitt_Blue Mode')
list_transcript.append('Sonny Stitt_Blues In Be-Bop')
list_transcript.append('Sonny Stitt_Body And Soul')
list_transcript.append('Sonny Stitt_Elora')
list_transcript.append('Sonny Stitt_Good Kick')
list_transcript.append('Sonny Stitt_Teapot')
list_transcript.append('Stan Getz_Blues In The Closet')
list_transcript.append('Stan Getz_Body And Soul')
list_transcript.append('Stan Getz_Crazy Rhythm')
list_transcript.append('Stan Getz_I\'m Glad There Is You')
list_transcript.append('Stan Getz_Insensatez')
list_transcript.append('Stan Getz_My Funny Valentine')
list_transcript.append('Steve Coleman_Cross-Fade-1')
list_transcript.append('Steve Coleman_Cross-Fade-2')
list_transcript.append('Steve Coleman_Double Vision')
list_transcript.append('Steve Coleman_Pass It On')
list_transcript.append('Steve Coleman_Processional')
list_transcript.append('Steve Coleman_Segment')
list_transcript.append('Steve Coleman_Slipped Again')
list_transcript.append('Steve Coleman_Take The Coltrane')
list_transcript.append('Steve Coleman_The Oracle-1')
list_transcript.append('Steve Coleman_The Oracle-2')
list_transcript.append('Steve Lacy_Alone Together')
list_transcript.append('Steve Lacy_Ask Me Now')
list_transcript.append('Steve Lacy_Easy To Love')
list_transcript.append('Steve Lacy_Let\'s Cool One')
list_transcript.append('Steve Lacy_Skippy')
list_transcript.append('Steve Lacy_Work')
list_transcript.append('Steve Turre_Dat Dere')
list_transcript.append('Steve Turre_If I Were A Bell')
list_transcript.append('Steve Turre_Steve\'s Blues')
list_transcript.append('Von Freeman_Pass It On')
list_transcript.append('Wayne Marsh_Crosscurrent')
list_transcript.append('Wayne Marsh_Tautology')
list_transcript.append('Wayne Marsh_Wow')
list_transcript.append('Wayne Shorter_Adam\'s Apple')
list_transcript.append('Wayne Shorter_Dolores')
list_transcript.append('Wayne Shorter_Down Under')
list_transcript.append('Wayne Shorter_E.S.P')
list_transcript.append('Wayne Shorter_Eighty-One')
list_transcript.append('Wayne Shorter_Footprints')
list_transcript.append('Wayne Shorter_Infant Eyes')
list_transcript.append('Wayne Shorter_Juju')
list_transcript.append('Wayne Shorter_Orbits')
list_transcript.append('Wayne Shorter_Speak No Evil')
list_transcript.append('Woody Shaw_Dat Dere')
list_transcript.append('Woody Shaw_If I Were A Bell')
list_transcript.append('Woody Shaw_Imagination')
list_transcript.append('Woody Shaw_In A Capricornian Way')
list_transcript.append('Woody Shaw_Rahsaan\'s Run')
list_transcript.append('Woody Shaw_Rosewood')
list_transcript.append('Woody Shaw_Stepping Stone')
list_transcript.append('Woody Shaw_Steve\'s Blues')
list_transcript.append('Wynton Kelly_Freddie The Freeloader')
list_transcript.append('Wynton Marsalis_April In Paris')
list_transcript.append('Wynton Marsalis_Caravan')
list_transcript.append('Wynton Marsalis_Cherokee')
list_transcript.append('Wynton Marsalis_Cherokee II')
list_transcript.append('Wynton Marsalis_Johnny Come Lately')
list_transcript.append('Wynton Marsalis_U.M.M.G')
list_transcript.append('Wynton Marsalis_You\'re My Everything')
list_transcript.append('Zoot Sims_All The Things You Are')
list_transcript.append('Zoot Sims_Dancing In The Dark-1')
list_transcript.append('Zoot Sims_Dancing In The Dark-2')
list_transcript.append('Zoot Sims_King David')
list_transcript.append('Zoot Sims_Night And Day-1')
list_transcript.append('Zoot Sims_Night And Day-2')

###########################################

app = Flask(__name__)

app.config['MAIL_SERVER']='ns0.ovh.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'feedback@jazzreal.org'
app.config['MAIL_PASSWORD'] = 'mIrlaPixQ1fp2h0iCrpH'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

###########################################

@app.route('/')
def home_page():
	return render_template('home_page.html')

@app.route('/contribute/', methods=['POST'])
def contribute():
	#sending email
	msg = Message('[Jazz Real] : '+request.form.get('Subject'), sender = 'feedback@jazzreal.org', recipients = ['feedback@jazzreal.org'])
	#msg.body = 'Last Name : '+request.form.get('FirstName')+'\n'
	#msg.body += 'First Name : '+request.form.get('LastName')+'\n'
	#msg.body += 'Email : '+request.form.get('Email')+'\n'
	#msg.body += 'Subject : '+request.form.get('Subject')+'\n'
	msg.body = 'Message : '+request.form.get('Message')+'\n'
	fp = request.files.get('file_upload')
	if fp:
		msg.attach(fp.filename,'application/octect-stream',fp.read())
		mail.send(msg)
	else:
		mail.send(msg)
	return render_template('contribute.html')

@app.route('/search')
def search():
#rechercher la grille d'un standard
	search_title = request.args.get('title','')
	if search_title:
		regex = re.compile(r'.*'+search_title+'.*',re.IGNORECASE)
		results_title = []
		selectobj = filter(regex.search, list_titles)
		for val in selectobj:
			results_title.append(val)
	else:
		results_title = []

#rechercher un artiste
	search_artist = request.args.get('artist','')
	if search_artist:
		results_artist = []
		regex = re.compile(r'.*'+search_artist+'.*',re.IGNORECASE)
		selectobj = filter(regex.search, artist_list)
		for val in selectobj:
			results_artist.append(val)
	else:
		results_artist = []

#rechercher un relevé
	search_transcript = request.args.get('transcript','')
	if search_transcript:
		results_transcript = []
		regex = re.compile(r'.*'+search_transcript+'.*',re.IGNORECASE)
		selectobj = filter(regex.search, list_transcript)
		for val in selectobj:
			results_transcript.append(val)
	else:
		results_transcript = []

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
			regex = re.compile(r'\b'+search_cadence,re.IGNORECASE)
			y = re.findall(regex, x)
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
			regex = re.compile(r'\b'+search_bridge,re.IGNORECASE)
			y = re.findall(regex, x)
			if y != []:
				results_bridge += [(x,list_bridge.index(x)+121)]
	else:
		results_bridge = []

#rechercher un article
	search_article = request.args.get('article','')
	if search_article:
		art = articles()
		art.init_articlesDB()
		results_article = []
		input_file = open('jazzreal/static/nbeniesDB.dict','r')
		read_file = input_file.read()
		regex = re.compile(r'{[^}]*'+search_article+'[^}]+}', re.IGNORECASE)
		result = re.findall(regex,read_file)
		regex2 = re.compile(r'\'titre\':([^\]]+\])')
		for i in result:
			result2 = re.findall(regex2,str(i))
		for i in result2:
			results_article += [(i,art.DB[i])]
		input_file.close()
	else:
		results_article = []
	return render_template('query_results.html', results_article=results_article, results_transcript=results_transcript, results_artist=results_artist, results_title=results_title, results_cadence=results_cadence, results_bridge=results_bridge, results_versions=results_versions)

@app.route('/artist')
def artist_search():
	search_artist = request.args.get('')

	alb = album()
	bio = biography()
	grp = groups()
	trk = tracks()
	mb = members()
	cred = credits_db()

	alb.init_albumDB()
	bio.init_biographyDB()
	grp.init_groupsDB()
	trk.init_tracksDB()
	mb.init_membersDB()
	cred.init_credits_db()

	if bio.DB.get(search_artist):
		bio_val = bio.DB.get(search_artist)
	else:
		bio_val = []

	if grp.DB.get(search_artist):
		grp_val = sorted(grp.DB.get(search_artist))
	else:
		grp_val = []

	if alb.DB.get(search_artist):
		alb_val = sorted(alb.DB.get(search_artist))
	else:
		alb_val = []

	#tree:root
	script = 'var data = [{"id": 1,"name": "Artist","description": "'+search_artist+'"},'

	#tree:level1 (biography + groups(root) + discography(root)
	script += '{"id": 2,"parentId": 1,"name": "Biographie", "type": "link_biography","description": "'+str(bio_val)+'"},'
	script += '{"id": 3,"parentId": 1,"name": "Groupes","description": "--ouvrir--"},'
	script += '{"id": 4,"parentId": 1,"name": "Discographie","description": "--ouvrir--"},'

	#counter
	i = 4
	j = 4

	#tree:level2->Groups
	for val in grp_val:
		i = j
		i += 1
		j = i+1

		script += '{"id": '+str(i)+',"parentId": 3,"name":"Groupe", "type":"link_group","description": "'+val+'"},'

	#counter
	j = i

	#tree:level2->Discography
	for val in alb_val:
		i = j
		i += 1
		script += '{"id": '+str(i)+',"parentId": 4,"name":"Album","description": "'+val+'"},'
		script += '{"id": '+str(i+1)+',"parentId": '+str(i)+',"name":"Pistes","description": "--ouvrir--"},'
		script += '{"id": '+str(i+2)+',"parentId": '+str(i)+',"name":"Crédits","description": "--ouvrir--"},'
		j = i + 3
		#tree:level3->Tracks
		try:
			for val2 in trk.DB[val]:
				script += '{"id": '+str(j)+',"parentId": '+str(i+1)+',"name":"Pistes","description": "'+val2+'"},'
				j += 1
		except KeyError:
			pass

		#tree:level3->Credits
		try:
			for val3 in cred.DB[val]:
				script += '{"id": '+str(j)+',"parentId": '+str(i+2)+',"name":"Crédits","description": "'+val3+'"},'
				j += 1
		except KeyError:
			pass

	script += '];'

	#script:end
	script += """
				var treePlugin = new d3.mitchTree.boxedTree()
				.getNodeSettings().setSizingMode('nodeSize').back()
				.setIsFlatData(true)
				.setData(data)
				.setMinScale(0.5)
				.setMaxScale(1)
				.setHeightWithoutMargin(900)
				.setElement(document.getElementById("visualisation"))
				.setIdAccessor(function(data) {
					return data.id;
				})
				.setParentIdAccessor(function(data) {
					return data.parentId;
				})
				.setBodyDisplayTextAccessor(function(data) {
					return data.description;
				})
				.setTitleDisplayTextAccessor(function(data) {
					return data.name;
				})

				.on("nodeClick", function(event) {
					console.log(event);
					if (event.data.type == "link_group")
						window.location = "/group?="+event.data.description
					if (event.data.type == "link_biography")
						window.location = "/bio?="+event.data.description
				})
				.initialize();
			"""


	return render_template('artist_results.html', script=script)


@app.route('/list')
def view_list():
	list_number = request.args.get('')
	f = open('jazzreal/static/lists/list'+list_number+'.html', encoding='ISO 8859-1')
	content = f.read()
	s = BeautifulSoup(content,'html.parser')
	title_list = []
	for y in s.findAll('a', href=True):
		g = open('jazzreal/static/corpus-list/'+y['href'], encoding='ISO 8859-1')
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
	f = open('jazzreal/static/corpus-html/'+view_word+'.html')
	plain = f.read()
	s = BeautifulSoup(plain, 'html.parser')
	title = s.find('h4').text
	title_encoded = urllib.parse.quote(title)
	results = []
	for corpus in s.findAll('pre'):
		results.append(corpus.text)
	for humeurs in s.findAll('humeurs'):
		results.append(humeurs.text)

	return render_template('view_theme.html', results=results, title=title, title_encoded=title_encoded)

@app.route('/view_list/')
def list_display():
	view_link = request.args.get('')
	f = open('jazzreal/static/corpus-list/'+view_link)
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
	versions_query = request.args.get('')
	s = versions_search()
	s.init_versionsDB()
	rvtmp1 = s.DB.get(versions_query)
	rvtmp2 = [x.replace('•','+') for x in rvtmp1]
	results_versions = zip(rvtmp1,rvtmp2)
	return render_template('view_versions.html',results_versions=results_versions)

@app.route('/gaia')
def gaia_app():
	return render_template('gaia.html')

@app.route('/bio')
def view_bio():
	bio_query = request.args.get('')

	return render_template('view_bio.html', bio_query=bio_query)

@app.route('/group')
def group_members():
	group_query = request.args.get('')
	mb = members()
	mb.init_membersDB()
	try:
		results_group_members = sorted(mb.DB.get(group_query))
	except TypeError:
		results_group_members = ['No results']
	return render_template('view_group_members.html', results_group_members = results_group_members)

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

	f = open('jazzreal/static/corpus-html/'+tune+'.html')

	f = open('jazzreal/static/corpus-html/'+tune+'.html')
	plain = f.read()

	key = re.search('<key>(.*)</key>', plain).group(1)
	key = str(key)
	key = key.replace(' ','')
	key = key.replace('m','')

	#key = plain[occ+7:occ+9].strip()
	#key = key.strip('m')

	init_pitch = key
	final_pitch = tone

	global diff

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
	f = open('jazzreal/static/corpus-html/'+tune+'.html')
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
			z = pitch_flat.index(x)
			q = z + diff
			pattern = re.compile(r'(\*\*|\*)'+ re.escape(x))
			if q <= 11:
				corpus_list = [re.sub(pattern,pitch_flat[q],y) for y in corpus_list]
			else:
				corpus_list = [re.sub(pattern,pitch_flat[q-12],y) for y in corpus_list]

	if chord_sharp:
		for x in chord_sharp:
			z = pitch_sharp.index(x)
			q = z + diff
			pattern = re.compile(r'(\*\*|\*)'+ re.escape(x))
			if q <= 11:
				corpus_list = [re.sub(pattern,pitch_flat[q],y) for y in corpus_list]
			else:
				corpus_list = [re.sub(pattern,pitch_flat[q-12],y) for y in corpus_list]

	if chord_none:
		for x in chord_none:
			if final_pitch in tone_flat:
				try:
					z = pitch_flat.index(x)
				except ValueError:
					z = pitch_sharp.index(x)
				q = z + diff
				pattern_none = re.compile(r'\*'+re.escape(x)+'(?!b|#)+')
				if q <= 11:
					corpus_list = [re.sub(pattern_none,pitch_flat[q],y) for y in corpus_list]
				else:
					corpus_list = [re.sub(pattern_none,pitch_flat[q-12],y) for y in corpus_list]
			elif final_pitch in tone_sharp:
				try:
					z = pitch_sharp.index(x)
				except ValueError:
					z = pitch_flat.index(x)
				q = z + diff
				pattern_none = re.compile(r'\*'+re.escape(x)+'(?!b|#)+')
				if q <= 11:
					corpus_list = [re.sub(pattern_none,pitch_sharp[q],y) for y in corpus_list]
				else:
					corpus_list = [re.sub(pattern_none,pitch_sharp[q-12],y) for y in corpus_list]

	for text_in_corpus in corpus_list:
		results.append(text_in_corpus)

	return render_template('view_theme.html', results=results, title=title, title_encoded=title_encoded)

#voiceGen#

#building chord base
tone_flat = ['C','F','Bb','Eb','Ab','Db','Gb','Cb']
tone_sharp = ['G','D','A','E','B','F_','C_']
pitch_flat = ['Ab','A','Bb','Cb','C','Db','D','Eb','E','F','Gb','G']
pitch_sharp = ['G_','A','A_','B','C','C_','D','D_','E','F','F_','G']
chord_type = ['6','7','M7','dim7','m6','m7','m7b5','mM7']

C = {}
F = {}
Bb = {}
Eb = {}
Ab = {}
Db = {}
Gb = {}
Cb = {}
G = {}
D = {}
A = {}
E = {}
B = {}
F_ = {}
C_ = {}


C['M7'] = [
	['C3','B3','E4','G4'],
	['C3','G3','B3','E4'],
	['C3','G3','E4','B4'],
	['C3','E3','B3','G4'],
	['E3','B3','C4','G4'],
	['E3','C4','G4','B4'],
	['E3','G3','C4','B4'],
	['G3','C4','E4','B4'],
	['G3','B3','C4','E4'],
	['C4','E4','G4','B4'],
]

C['6'] = [
	['C3','A3','E4','G4'],
	['C3','G3','A3','E4'],
	['C3','G3','E4','A4'],
	['C3','E3','A3','E4'],
	['E3','A3','C4','G4'],
	['E3','G3','C4','A4'],
	['G3','A3','C4','E4'],
	['E3','G3','A3','C4'],
	['C4','E4','G4','A4'],
]

C['m7b5'] = [
	['C3','Bb3','Eb4','Gb4'],
	['C3','Eb3','Bb3','Gb4'],
	['C3','Gb3','Bb3','Eb4'],
	['C3','Gb3','Eb4','Bb4'],
	['C3','Eb4','Gb4','Bb4'],
	['Eb3','Bb3','Gb4','C4'],
	['Eb3','Bb3','C4','Gb4'],
	['Eb3','Gb3','C4','Bb4'],
	['Eb3','C4','Gb4','Bb4'],
	['Gb3','C4','Eb4','Bb4'],
	['Bb2','Gb3','Eb4','C5'],
	['C4','Eb4','Gb4','Bb4'],
	['Bb3','C4','Eb4','Gb4'],
	['Gb3','Bb3','C4','Eb4'],
	['Eb3','Gb3','Bb3','C4'],
]

C['dim7'] = [
	['C3','A3','Eb4','Gb4'],
	['C3','Gb3','Eb4','A4'],
	['C3','Gb3','A3','Eb4'],
	['C3','Eb3','A4','Gb4'],
	['Eb3','C4','Gb4','A4'],
	['Eb3','A4','C4','Gb4'],
	['Eb3','A4','Gb4','C5'],
	['Eb3','A4','C4','Gb4'],
	['Gb3','C4','Eb4','A4'],
	['Gb3','Eb4','A4','C5'],
	['A2','Eb3','C4','Gb4'],
	['A2','Eb3','Gb3','C4'],
	['A4','Gb3','Eb4','C5'],
	['A4','Gb3','C4','Eb4'],
	['C4','Eb4','Gb4','A4'],
	['A4','C4','Eb4','Gb4'],
	['Gb3','A4','C4','Eb4'],
	['Eb3','Gb3','A4','C4'],
]

C['mM7'] = [
	['C3','B3','Eb4','G4'],
	['C3','G3','B3','Eb4'],
	['C3','G3','Eb4','B4'],
	['Eb3','B3','C4','G4'],
	['Eb3','G3','C4','B4'],
	['Eb3','C4','G4','B4'],
	['G3','C4','Eb4','B4'],
	['C4','Eb4','G4','B4'],
	['B3','C4','Eb4','G4'],
	['G3','B3','C4','Eb4'],
]

C['m7'] = [
	['C3','Bb3','Eb4','G4'],
	['C3','G3','Bb3','Eb4'],
	['C3','G3','Eb4','Bb4'],
	['C3','Eb3','Bb3','G4'],
	['Eb3','Bb3','G4','C5'],
	['Eb3','Bb3','C4','Bb3'],
	['Eb3','G3','C4','Bb4'],
	['Eb3','C4','G4','Bb4'],
	['G3','C4','Eb4','Bb4'],
	['Bb3','Eb4','G4','C5'],
	['Bb2','G3','Eb4','C5'],
	['C4','Eb4','G4','Bb4'],
	['Bb3','C4','Eb4','G4'],
	['G3','Bb3','C4','Eb4'],
	['Eb3','G3','Bb3','C4'],
]

C['m6'] = [
	['C3','A3','Eb4','G4'],
	['C3','G3','A3','Eb4'],
	['C3','G3','Eb4','A4'],
	['C3','Eb3','A3','G4'],
	['Eb3','C4','G4','A4'],
	['G3','C4','Eb4','A4'],
	['A2','G3','C4','Eb4'],
	['C4','Eb4','G4','A4'],
	['A3','C4','Eb4','G4'],
	['G3','A3','C4','Eb4'],
	['Eb3','G3','A3','C4'],
]

C['7'] = [
	['C3','Bb3','E4','G4'],
	['C3','G3','Bb3','E4'],
	['C3','G3','E4','Bb4'],
	['C3','E3','Bb3','G4'],
	['E3','Bb3','G4','C5'],
	['E3','Bb3','C4','G4'],
	['E3','G3','C4','Bb4'],
	['E3','C4','G4','Bb4'],
	['G3','C4','E4','Bb4'],
	['Bb3','C4','E4','C5'],
	['Bb2','G3','E4','C5'],
]

def transpose(chord,initkey,finalkey):

	note_to_midi_flat = {
	'A0':'21','Bb0':'22','B0':'23','C1':'24','Db1':'25','D1':'26','Eb1':'27','E1':'28','F1':'29','Gb1':'30','G1':'31','Ab1':'32','A1':'33','Bb1':'34','B1':'35','C2':'36','Db2':'37','D2':'38','Eb2':'39','E2':'40','F2':'41','Gb2':'42','G2':'43','Ab2':'44','A2':'45','Bb2':'46','B2':'47','C3':'48','Db3':'49','D3':'50','Eb3':'51','E3':'52','F3':'53','Gb3':'54','G3':'55','Ab3':'56','A3':'57','Bb3':'58','B3':'59','C4':'60','Db4':'61','D4':'62','Eb4':'63','E4':'64','F4':'65','Gb4':'66','G4':'67','Ab4':'68','A4':'69','Bb4':'70','B4':'71','C5':'72','Db5':'73','D5':'74','Eb5':'75','E5':'76','F5':'77','Gb5':'78','G5':'79','Ab5':'80','A5':'81','Bb5':'82','B5':'83','C6':'84','Db6':'85','D6':'86','Eb6':'87','E6':'88','F6':'89','Gb6':'90','G6':'91','Ab6':'92','A6':'93','Bb6':'94','B6':'95','C7':'96','Db7':'97','D7':'98','Eb7':'99','E7':'100','F7':'101','Gb7':'102','G7':'103','Ab7':'104','A7':'105','Bb7':'106','B7':'107','C8':'108',
	}
	midi_to_note_flat = {v:k for k,v in note_to_midi_flat.items()}

	note_to_midi_sharp = {
	'A0':'21','A#0':'22','B0':'23','C1':'24','C#1':'25','D1':'26','D#1':'27','E1':'28','F1':'29','F#1':'30','G1':'31','G#1':'32','A1':'33','A#1':'34','B1':'35','C2':'36','C#2':'37','D2':'38','D#2':'39','E2':'40','F2':'41','F#2':'42','G2':'43','G#2':'44','A2':'45','A#2':'46','B2':'47','C3':'48','C#3':'49','D3':'50','D#3':'51','E3':'52','F3':'53','F#3':'54','G3':'55','G#3':'56','A3':'57','A#3':'58','B3':'59','C4':'60','C#4':'61','D4':'62','D#4':'63','E4':'64','F4':'65','F#4':'66','G4':'67','G#4':'68','A4':'69','A#4':'70','B4':'71','C5':'72','C#5':'73','D5':'74','D#5':'75','E5':'76','F5':'77','F#5':'78','G5':'79','G#5':'80','A5':'81','A#5':'82','B5':'83','C6':'84','C#6':'85','D6':'86','D#6':'87','E6':'88','F6':'89','F#6':'90','G6':'91','G#6':'92','A6':'93','A#6':'94','B6':'95','C7':'96','C#7':'97','D7':'98','D#7':'99','E7':'100','F7':'101','F#7':'102','G7':'103','G#7':'104','A7':'105','A#7':'106','B7':'107','C8':'108',
	}
	midi_to_note_sharp = {v:k for k,v in note_to_midi_sharp.items()}

	if initkey in tone_flat:
		init = pitch_flat.index(initkey)
	else:
		init = pitch_sharp.index(initkey)

	if finalkey in tone_flat:
		final = pitch_flat.index(finalkey)
	else:
		final = pitch_sharp.index(finalkey)

	diff = final - init

	try:
		if finalkey in tone_flat:
			chord_index = note_to_midi_flat[chord]
		else:
			chord_index = note_to_midi_sharp[chord]
	except KeyError:
		chord_index = note_to_midi_flat[chord]

	chord_transposed_index = int(chord_index) + diff

	if finalkey in tone_flat:
		chord_transposed = midi_to_note_flat[str(chord_transposed_index)]
	else:
		chord_transposed = midi_to_note_sharp[str(chord_transposed_index)]

	return chord_transposed

#generate all voiceGen chords
k = ''
for i,j in itertools.product(tone_flat,chord_type):
	k = i
	i = {j:''}
	i[j] = [[transpose(x,'C',k) for x in chord] for chord in C[j]]
	exec(k+'[\''+j+'\']'+'='+str(i[j]))

for i,j in itertools.product(tone_sharp,chord_type):
	k = i
	i = {j:''}
	i[j] = [[transpose(x,'C',k) for x in chord] for chord in C[j]]
	exec(k+'[\''+j+'\']'+'='+str(i[j]))

####################
#voiceGen / audioGen
####################

#convert note to freq for wav gen
def note_to_freq(note, concert_A=440.0):
	'''
	from wikipedia: http://en.wikipedia.org/wiki/MIDI_Tuning_Standard#Frequency_values
	'''
	return (2.0 ** ((note - 69) / 12.0)) * concert_A

#convert midi ticks to ms for wav gen
def ticks_to_ms(ticks,mid_file):
	tick_ms = (60000.0 / tempo) / mid_file.ticks_per_beat
	return ticks * tick_ms

#corresponsdance table note/midi
note_to_midi = {'A0': '21', 'Bb0': '22', 'B0': '23', 'C1': '24', 'Db1': '25', 'D1': '26', 'Eb1': '27', 'E1': '28', 'F1': '29', 'Gb1': '30', 'G1': '31', 'Ab1': '32', 'A1': '33', 'Bb1': '34', 'B1': '35', 'C2': '36', 'Db2': '37', 'D2': '38', 'Eb2': '39', 'E2': '40', 'F2': '41', 'Gb2': '42', 'G2': '43', 'Ab2': '44', 'A2': '45', 'Bb2': '46', 'B2': '47', 'C3': '48', 'Db3': '49', 'D3': '50', 'Eb3': '51', 'E3': '52', 'F3': '53', 'Gb3': '54', 'G3': '55', 'Ab3': '56', 'A3': '57', 'Bb3': '58', 'B3': '59', 'C4': '60', 'Db4': '61', 'D4': '62', 'Eb4': '63', 'E4': '64', 'F4': '65', 'Gb4': '66', 'G4': '67', 'Ab4': '68', 'A4': '69', 'Bb4': '70', 'B4': '71', 'C5': '72', 'Db5': '73', 'D5': '74', 'Eb5': '75', 'E5': '76', 'F5': '77', 'Gb5': '78', 'G5': '79', 'Ab5': '80', 'A5': '81', 'Bb5': '82', 'B5': '83', 'C6': '84', 'Db6': '85', 'D6': '86', 'Eb6': '87', 'E6': '88', 'F6': '89', 'Gb6': '90', 'G6': '91', 'Ab6': '92', 'A6': '93', 'Bb6': '94', 'B6': '95', 'C7': '96', 'Db7': '97', 'D7': '98', 'Eb7': '99', 'E7': '100', 'F7': '101', 'Gb7': '102', 'G7': '103', 'Ab7': '104', 'A7': '105', 'Bb7': '106', 'B7': '107', 'C8': '108', 'A#0': '22', 'C#1': '25', 'D#1': '27', 'F#1': '30', 'G#1': '32', 'A#1': '34', 'C#2': '37', 'D#2': '39', 'F#2': '42', 'G#2': '44', 'A#2': '46', 'C#3': '49', 'D#3': '51', 'F#3': '54', 'G#3': '56', 'A#3': '58', 'C#4': '61', 'D#4': '63', 'F#4': '66', 'G#4': '68', 'A#4': '70', 'C#5': '73', 'D#5': '75', 'F#5': '78', 'G#5': '80', 'A#5': '82', 'C#6': '85', 'D#6': '87', 'F#6': '90', 'G#6': '92', 'A#6': '94', 'C#7': '97', 'D#7': '99', 'F#7': '102', 'G#7': '104', 'A#7': '106'}

#midi constant declaration
track001 = 0
channel  = 0
time = 0    # In beats
duration001 = 4    # In beats
tempo = 100   # In BPM
volume = 100  # 0-127, as per the MIDI standard


@app.route('/voiceGen')
def voiceGen():

	#########
	#voiceGen
	#########

	voiceGen_results = ''

	chord_i = []
	chords = []
	chord_progressions = []
	chord_progressions_display = []


	query = request.args.get('query','')

	#build reusults
	voiceGen_results += '<h4>'
	voiceGen_results += '<pre>'

	query = re.sub('#','_',query)
	query = re.findall(r'(C|F|Bb|Eb|Ab|Db|Gb|Cb|G|D|A|E|B|F_|C_)(6|7|M7|dim7|m6|m7\b|m7b5|mM7)',query)

	voiceGen_results += 'Nb d\'accords = ('+str(len(query))+'):'
	voiceGen_results += '<br>'

	for i in range(len(query)):
		chords.append(eval(query[i][0]+'[\''+query[i][1]+'\']'))

	if len(query) <= 4:

		#make cartesian product of list(chords)
		chord_progressions = list(itertools.product(*chords))

		voiceGen_results += 'Nb de progressions = ('+str(len(chord_progressions))+')'
		voiceGen_results += '<br>'
		voiceGen_results += 'Affichage  = (4/'+str(len(chord_progressions))+')'
		voiceGen_results += '<br>'
		voiceGen_results += 'Rafraîchir la page afin de "générer" d\'autres résultats aléatoirement'
		voiceGen_results += '<br>'
		voiceGen_results += '<br>'

		#random choice and constitution of progressions list
		for i in range(0,2):
			chord_progressions_display += random.choice(chord_progressions) , random.choice(chord_progressions)

		#build results for html display AND vexflow display AND audioGen
		for j in chord_progressions_display:

			for i in range(len(query)):
				voiceGen_results += query[i][0]+'[\''+query[i][1]+'\'] '


			voiceGen_results += '<details><summary>'
			voiceGen_results += str(j)
			voiceGen_results += '</summary>'

			k = str(j)
			k = k.replace(' ','')
			k = k.replace('(','')
			k = k.replace(')','')
			k = k.replace('[','')
			k = k.replace(']','')
			k = k.replace(',','')
			k = k.replace('\'','')
			k = k.replace('#','_')

			voiceGen_results += '<div id=\"'+k+'\"></div>'

			voiceGen_results += '<audio controls loop><source src=\"https://www.jazzreal.org/static/audioGen/_'+k+'.wav\" type=\"audio/wav\"></audio>'
			voiceGen_results += '</details>'
			voiceGen_results += '<br>'
			voiceGen_results += '<script>'
			voiceGen_results += """const VF_"""+k+""" = Vex.Flow;
					var vf = new VF_"""+k+""".Factory({renderer: {elementId: '"""+k+"""', height: 300}});
					var score = vf.EasyScore();
					score.set({ time: '5/4' });
					var system = vf.System();
					system.addStave({
					voices: [score.voice(score.notes('"""
			for z in range(len(j)):
				voiceGen_results += '('+str(j[z][2])+' '+str(j[z][3])+')/q ,'
			voiceGen_results += """')).setStrict(false)]
					}).addClef('treble').addTimeSignature('4/4');
					system.addStave({
					voices: [score.voice(score.notes('"""
			for z in range(len(j)):
				voiceGen_results += '('+str(j[z][0])+' '+str(j[z][1])+')/q ,'
			voiceGen_results += """',{clef: 'bass'})).setStrict(false)]
					}).addClef('bass').addTimeSignature('4/4');
				system.addConnector()
				vf.draw();"""
			voiceGen_results += '</script>'

	else:
		voiceGen_results += 'nombre de possibilités de progressions trop élevé'
		voiceGen_results += '<br>'
		voiceGen_results += 'maximum par requête = 4 accords'
		pass
	voiceGen_results += '</pre></h4>'

	#########
	#audioGen
	#########

	#
	# midi gen
	#
	for j in chord_progressions_display:

		#create midi objects
		MyMIDI = MIDIFile(1)
		MyMIDI.addTempo(track001, time, tempo)

		k = str(j)
		k = k.replace(' ','')
		k = k.replace('(','')
		k = k.replace(')','')
		k = k.replace('[','')
		k = k.replace(']','')
		k = k.replace(',','')
		k = k.replace('\'','')
		k = k.replace('#','_')
		#counter for separating chords in list
		x = 0

		for z in range(len(j)):
			for i in range(0,4):
				MyMIDI.addNote(track001,channel,int(note_to_midi[j[z][i]]),time+x,duration001,volume)
			x += 4

		#write midi file
		output_file = open('jazzreal/static/audioGen/_'+k+'.mid', 'wb')
		MyMIDI.writeFile(output_file)
		output_file.close()

		#
		# wav gen
		#

		mid = MidiFile('jazzreal/static/audioGen/_'+k+'.mid')

		output = AudioSegment.silent(mid.length * 1000.0)

		for track in mid.tracks:
			# position of rendering in ms
			current_pos = 0.0

			current_notes = defaultdict(dict)
			# current_notes = {
			#   channel: {
			#     note: (start_time, message)
			#   }
			# }

			for msg in track:
				current_pos += ticks_to_ms(msg.time,mid)

				if msg.type == 'note_on':
				  current_notes[msg.channel][msg.note] = (current_pos, msg)

				if msg.type == 'note_off':
					start_pos, start_msg = current_notes[msg.channel].pop(msg.note)

					duration = current_pos - start_pos

					signal_generator = Sine(note_to_freq(msg.note))
					rendered = signal_generator.to_audio_segment(duration=duration-50, volume=-20).fade_out(100).fade_in(30)

					output = output.overlay(rendered, start_pos)

		output.export('jazzreal/static/audioGen/_'+k+'.wav', format="wav")

		os.remove('jazzreal/static/audioGen/_'+k+'.mid')
		del output_file
		del mid
		del MyMIDI

	return render_template('view_voiceGen.html', voiceGen_results=voiceGen_results)

#bluesGen : blues Database in 16 keys
blues_db = {
	'C':[
	'C7 C7 C7 C7 Bb7 Bb7 C7 C7 G7 G7 C7 C7 ',
	'C7 C7 C7 C7 Bb7 Bb7 C7 C7 G7 Bb7 C7 G7 ',
	'C7 Bb7 C7 C7 Bb7 Bb7 C7 C7 D7 G7 C7 G7 ',
	'C7 Bb7 C7 C7 Bb7 Bb7 C7 A7 D7 G7 C7 G7 ',
	'C7 Bb7 C7 C7 Bb7 Bb7 C7 A7 Dm7 G7 C7 Dm7/G7 ',
	'C7 Bb7 C7 C7 Bb7 Eb7 C7 A7 Ab7 G7 C7 Ab7/G7 ',
	'C7 Bb7 C7 Gm7/C7 Bb7 Eb7 C7/Em7 A7 Dm7 G7 Em7/A7 Dm7/G7 ',
	'C7 Bb7 C7 Gm7/C7 Bb7 Eb7 Em7 A7 Dm7 G7 Em7/A7 Dm7/G7 ',
	'C7 F7 C7 Gm7/C7 F7 Gbm7/Cb7 C7/A7 Bb7/A7 Dm7 G7/F7 Em7/A7 Dm7/G7 ',
	'CM7 Cbm7/E7 Am7/D7 Gm7/C7 F7 Gbdim7 Em7/A7 EbM7/Ab7 Dm7 Abm7/Db7 C7/A7 Dm7/G7 ',
	'CM7 CbM7/Bbm7 Am7/Abm7 Gm7/Gb7 BbM7 Bbm7 Em7 Ebm7 Dm7 G7 Em7/Edim7 Dm7/Db6 ',
	'CM7 BbM7 Em7/Dm7 Dbm7/Cb7 BbM7 Bbm7 Em7 Ebm7 Dm7 Db7 CM7/Ebm7 Dm7/Db6 ',
	'CM7 BbM7 Em7/Dm7 Dbm7/Gb7 BbM7 BbM7/Eb7 EbM7 EbM7/Ab7 DbM7 Dm7/G7 Em7/A7 Dm7/G7 ',
	'CM7 Cbm7/E7 Am7/D7 DbM7/Gb7 BbM7 BbM7/Bb7 Em7 Ebm7/Ab7 Dm7 G7 Em7/A7 Dm7/G7 ',
	'CM7 Cbm7/E7 Am7/D7 DbM7/Gb7 FM7 Gbm7/Cb7 Em7 Ebm7/Ab7 Dm7 G7/F7 Em7/A7 Dm7/G7 ',
	'Dbm7/Gb7 Cbm7/E7 Am7/D7 Gm7/C7 FM7 Fm7/Bb7 EbM7 Ebm7/Ab7 DbM7 Dm7/G7 Em7/A7 Dm7/G7 ',
	'CM7 Dbm7/Gb7 CbM7 BbM7/AbM7 FM7 Gbm7/Cb7 EM7 Em7/A7 DM7 DbM7 CM7/EbM7 DM7/Db6 '
	],

	'C#':[
	'C#7 C#7 C#7 C#7 Bb7 Bb7 C#7 C#7 G#7 G#7 C#7 C#7 ',
	'C#7 C#7 C#7 C#7 Bb7 Bb7 C#7 C#7 G#7 Bb7 C#7 G#7 ',
	'C#7 Bb7 C#7 C#7 Bb7 Bb7 C#7 C#7 D#7 G#7 C#7 G#7 ',
	'C#7 Bb7 C#7 C#7 Bb7 Bb7 C#7 A#7 D#7 G#7 C#7 G#7 ',
	'C#7 Bb7 C#7 C#7 Bb7 Bb7 C#7 A#7 D#m7 G#7 C#7 D#m7/G#7 ',
	'C#7 Bb7 C#7 C#7 Bb7 Eb7 C#7 A#7 A7 G#7 C#7 A7/G#7 ',
	'C#7 Bb7 C#7 G#m7/C#7 Bb7 Eb7 C#7/Fm7 A#7 D#m7 G#7 Fm7/A#7 D#m7/G#7 ',
	'C#7 Bb7 C#7 G#m7/C#7 Bb7 Eb7 Fm7 A#7 D#m7 G#7 Fm7/A#7 D#m7/G#7 ',
	'C#7 Gb7 C#7 G#m7/C#7 Gb7 Gm7/C7 C#7/A#7 Cb7/A#7 D#m7 G#7/Gb7 Fm7/A#7 D#m7/G#7 ',
	'C#M7 Cm7/F7 A#m7/D#7 G#m7/C#7 Gb7 Gdim7 Fm7/A#7 FbM7/A7 D#m7 Am7/D7 C#7/A#7 D#m7/G#7 ',
	'C#M7 CM7/Cbm7 A#m7/Am7 G#m7/G7 BbM7 Bbm7 Fm7 Fbm7 D#m7 G#7 Fm7/Fdim7 D#m7/D6 ',
	'C#M7 BbM7 Fm7/D#m7 Dm7/Cb7 BbM7 Bbm7 Fm7 Fbm7 D#m7 D7 C#M7/Fbm7 D#m7/D6 ',
	'C#M7 BbM7 Fm7/D#m7 Dm7/G7 BbM7 BbM7/Eb7 FbM7 FbM7/A7 DM7 D#m7/G#7 Fm7/A#7 D#m7/G#7 ',
	'C#M7 Cm7/F7 A#m7/D#7 DM7/G7 BbM7 BbM7/Cb7 Fm7 Fbm7/A7 D#m7 G#7 Fm7/A#7 D#m7/G#7 ',
	'C#M7 Cm7/F7 A#m7/D#7 DM7/G7 GbM7 Gm7/C7 Fm7 Fbm7/A7 D#m7 G#7/Gb7 Fm7/A#7 D#m7/G#7 ',
	'Dm7/G7 Cm7/F7 A#m7/D#7 G#m7/C#7 GbM7 Gbm7/Cb7 FbM7 Fbm7/A7 DM7 D#m7/G#7 Fm7/A#7 D#m7/G#7 ',
	'C#M7 Dm7/G7 CM7 CbM7/AM7 GbM7 Gm7/C7 FM7 Fm7/A#7 D#M7 DM7 C#M7/FbM7 D#M7/D6 '
	],

	'Db':[
	'Db7 Db7 Db7 Db7 Bb7 Bb7 Db7 Db7 Ab7 Ab7 Db7 Db7 ',
	'Db7 Db7 Db7 Db7 Bb7 Bb7 Db7 Db7 Ab7 Bb7 Db7 Ab7 ',
	'Db7 Bb7 Db7 Db7 Bb7 Bb7 Db7 Db7 Eb7 Ab7 Db7 Ab7 ',
	'Db7 Bb7 Db7 Db7 Bb7 Bb7 Db7 Bb7 Eb7 Ab7 Db7 Ab7 ',
	'Db7 Bb7 Db7 Db7 Bb7 Bb7 Db7 Bb7 Ebm7 Ab7 Db7 Ebm7/Ab7 ',
	'Db7 Bb7 Db7 Db7 Bb7 Eb7 Db7 Bb7 A7 Ab7 Db7 A7/Ab7 ',
	'Db7 Bb7 Db7 Abm7/Db7 Bb7 Eb7 Db7/Fm7 Bb7 Ebm7 Ab7 Fm7/Bb7 Ebm7/Ab7 ',
	'Db7 Bb7 Db7 Abm7/Db7 Bb7 Eb7 Fm7 Bb7 Ebm7 Ab7 Fm7/Bb7 Ebm7/Ab7 ',
	'Db7 Gb7 Db7 Abm7/Db7 Gb7 Gm7/C7 Db7/Bb7 Cb7/Bb7 Ebm7 Ab7/Gb7 Fm7/Bb7 Ebm7/Ab7 ',
	'DbM7 Cm7/F7 Bbm7/Eb7 Abm7/Db7 Gb7 Gdim7 Fm7/Bb7 FbM7/A7 Ebm7 Am7/D7 Db7/Bb7 Ebm7/Ab7 ',
	'DbM7 CM7/Cbm7 Bbm7/Am7 Abm7/G7 BbM7 Bbm7 Fm7 Fbm7 Ebm7 Ab7 Fm7/Fdim7 Ebm7/D6 ',
	'DbM7 BbM7 Fm7/Ebm7 Dm7/Cb7 BbM7 Bbm7 Fm7 Fbm7 Ebm7 D7 DbM7/Fbm7 Ebm7/D6 ',
	'DbM7 BbM7 Fm7/Ebm7 Dm7/G7 BbM7 BbM7/Eb7 FbM7 FbM7/A7 DM7 Ebm7/Ab7 Fm7/Bb7 Ebm7/Ab7 ',
	'DbM7 Cm7/F7 Bbm7/Eb7 DM7/G7 BbM7 BbM7/Cb7 Fm7 Fbm7/A7 Ebm7 Ab7 Fm7/Bb7 Ebm7/Ab7 ',
	'DbM7 Cm7/F7 Bbm7/Eb7 DM7/G7 GbM7 Gm7/C7 Fm7 Fbm7/A7 Ebm7 Ab7/Gb7 Fm7/Bb7 Ebm7/Ab7 ',
	'Dm7/G7 Cm7/F7 Bbm7/Eb7 Abm7/Db7 GbM7 Gbm7/Cb7 FbM7 Fbm7/A7 DM7 Ebm7/Ab7 Fm7/Bb7 Ebm7/Ab7 ',
	'DbM7 Dm7/G7 CM7 CbM7/AM7 GbM7 Gm7/C7 FM7 Fm7/Bb7 EbM7 DM7 DbM7/FbM7 EbM7/D6 '
	],

	'D':[
	'D7 D7 D7 D7 Bb7 Bb7 D7 D7 A7 A7 D7 D7 ',
	'D7 D7 D7 D7 Bb7 Bb7 D7 D7 A7 Bb7 D7 A7 ',
	'D7 Bb7 D7 D7 Bb7 Bb7 D7 D7 E7 A7 D7 A7 ',
	'D7 Bb7 D7 D7 Bb7 Bb7 D7 B7 E7 A7 D7 A7 ',
	'D7 Bb7 D7 D7 Bb7 Bb7 D7 B7 Em7 A7 D7 Em7/A7 ',
	'D7 Bb7 D7 D7 Bb7 Eb7 D7 B7 Bb7 A7 D7 Bb7/A7 ',
	'D7 Bb7 D7 Am7/D7 Bb7 Eb7 D7/F#m7 B7 Em7 A7 F#m7/B7 Em7/A7 ',
	'D7 Bb7 D7 Am7/D7 Bb7 Eb7 F#m7 B7 Em7 A7 F#m7/B7 Em7/A7 ',
	'D7 G7 D7 Am7/D7 G7 G#m7/C#7 D7/B7 C7/B7 Em7 A7/G7 F#m7/B7 Em7/A7 ',
	'DM7 C#m7/F#7 Bm7/E7 Am7/D7 G7 G#dim7 F#m7/B7 FM7/Bb7 Em7 Bbm7/Eb7 D7/B7 Em7/A7 ',
	'DM7 C#M7/Cm7 Bm7/Bbm7 Am7/Ab7 BbM7 Bbm7 F#m7 Fm7 Em7 A7 F#m7/F#dim7 Em7/Eb6 ',
	'DM7 BbM7 F#m7/Em7 Ebm7/Cb7 BbM7 Bbm7 F#m7 Fm7 Em7 Eb7 DM7/Fm7 Em7/Eb6 ',
	'DM7 BbM7 F#m7/Em7 Ebm7/Ab7 BbM7 BbM7/Eb7 FM7 FM7/Bb7 EbM7 Em7/A7 F#m7/B7 Em7/A7 ',
	'DM7 C#m7/F#7 Bm7/E7 EbM7/Ab7 BbM7 BbM7/C7 F#m7 Fm7/Bb7 Em7 A7 F#m7/B7 Em7/A7 ',
	'DM7 C#m7/F#7 Bm7/E7 EbM7/Ab7 GM7 G#m7/C#7 F#m7 Fm7/Bb7 Em7 A7/G7 F#m7/B7 Em7/A7 ',
	'D#m7/G#7 C#m7/F#7 Bm7/E7 Am7/D7 GM7 Gm7/C7 FM7 Fm7/Bb7 EbM7 Em7/A7 F#m7/B7 Em7/A7 ',
	'DM7 D#m7/G#7 C#M7 CM7/BbM7 GM7 G#m7/C#7 F#M7 F#m7/B7 EM7 EbM7 DM7/FM7 EM7/Eb6 '
	],

	'D#':[
	'D#7 D#7 D#7 D#7 Bb7 Bb7 D#7 D#7 A#7 A#7 D#7 D#7 ',
	'D#7 D#7 D#7 D#7 Bb7 Bb7 D#7 D#7 A#7 Bb7 D#7 A#7 ',
	'D#7 Bb7 D#7 D#7 Bb7 Bb7 D#7 D#7 F7 A#7 D#7 A#7 ',
	'D#7 Bb7 D#7 D#7 Bb7 Bb7 D#7 C7 F7 A#7 D#7 A#7 ',
	'D#7 Bb7 D#7 D#7 Bb7 Bb7 D#7 C7 Fm7 A#7 D#7 Fm7/A#7 ',
	'D#7 Bb7 D#7 D#7 Bb7 Eb7 D#7 C7 Cb7 A#7 D#7 Cb7/A#7 ',
	'D#7 Bb7 D#7 A#m7/D#7 Bb7 Eb7 D#7/Gm7 C7 Fm7 A#7 Gm7/C7 Fm7/A#7 ',
	'D#7 Bb7 D#7 A#m7/D#7 Bb7 Eb7 Gm7 C7 Fm7 A#7 Gm7/C7 Fm7/A#7 ',
	'D#7 Ab7 D#7 A#m7/D#7 Ab7 Am7/D7 D#7/C7 Db7/C7 Fm7 A#7/Ab7 Gm7/C7 Fm7/A#7 ',
	'D#M7 Dm7/G7 Cm7/F7 A#m7/D#7 Ab7 Adim7 Gm7/C7 GbM7/Cb7 Fm7 Cbm7/Fb7 D#7/C7 Fm7/A#7 ',
	'D#M7 DM7/Dbm7 Cm7/Cbm7 A#m7/A7 BbM7 Bbm7 Gm7 Gbm7 Fm7 A#7 Gm7/Gdim7 Fm7/E6 ',
	'D#M7 BbM7 Gm7/Fm7 Fbm7/Cb7 BbM7 Bbm7 Gm7 Gbm7 Fm7 Fb7 D#M7/Gbm7 Fm7/E6 ',
	'D#M7 BbM7 Gm7/Fm7 Fbm7/A7 BbM7 BbM7/Eb7 GbM7 GbM7/Cb7 FbM7 Fm7/A#7 Gm7/C7 Fm7/A#7 ',
	'D#M7 Dm7/G7 Cm7/F7 FbM7/A7 BbM7 BbM7/Db7 Gm7 Gbm7/Cb7 Fm7 A#7 Gm7/C7 Fm7/A#7 ',
	'D#M7 Dm7/G7 Cm7/F7 FbM7/A7 AbM7 Am7/D7 Gm7 Gbm7/Cb7 Fm7 A#7/Ab7 Gm7/C7 Fm7/A#7 ',
	'Em7/A7 Dm7/G7 Cm7/F7 A#m7/D#7 AbM7 Abm7/Db7 GbM7 Gbm7/Cb7 FbM7 Fm7/A#7 Gm7/C7 Fm7/A#7 ',
	'D#M7 Em7/A7 DM7 DbM7/CbM7 AbM7 Am7/D7 GM7 Gm7/C7 FM7 FbM7 D#M7/GbM7 FM7/E6 '
	],

	'Eb':[
	'Eb7 Eb7 Eb7 Eb7 Bb7 Bb7 Eb7 Eb7 Bb7 Bb7 Eb7 Eb7 ',
	'Eb7 Eb7 Eb7 Eb7 Bb7 Bb7 Eb7 Eb7 Bb7 Bb7 Eb7 Bb7 ',
	'Eb7 Bb7 Eb7 Eb7 Bb7 Bb7 Eb7 Eb7 F7 Bb7 Eb7 Bb7 ',
	'Eb7 Bb7 Eb7 Eb7 Bb7 Bb7 Eb7 C7 F7 Bb7 Eb7 Bb7 ',
	'Eb7 Bb7 Eb7 Eb7 Bb7 Bb7 Eb7 C7 Fm7 Bb7 Eb7 Fm7/Bb7 ',
	'Eb7 Bb7 Eb7 Eb7 Bb7 Eb7 Eb7 C7 Cb7 Bb7 Eb7 Cb7/Bb7 ',
	'Eb7 Bb7 Eb7 Bbm7/Eb7 Bb7 Eb7 Eb7/Gm7 C7 Fm7 Bb7 Gm7/C7 Fm7/Bb7 ',
	'Eb7 Bb7 Eb7 Bbm7/Eb7 Bb7 Eb7 Gm7 C7 Fm7 Bb7 Gm7/C7 Fm7/Bb7 ',
	'Eb7 Ab7 Eb7 Bbm7/Eb7 Ab7 Am7/D7 Eb7/C7 Db7/C7 Fm7 Bb7/Ab7 Gm7/C7 Fm7/Bb7 ',
	'EbM7 Dm7/G7 Cm7/F7 Bbm7/Eb7 Ab7 Adim7 Gm7/C7 GbM7/Cb7 Fm7 Cbm7/Fb7 Eb7/C7 Fm7/Bb7 ',
	'EbM7 DM7/Dbm7 Cm7/Cbm7 Bbm7/A7 BbM7 Bbm7 Gm7 Gbm7 Fm7 Bb7 Gm7/Gdim7 Fm7/E6 ',
	'EbM7 BbM7 Gm7/Fm7 Fbm7/Cb7 BbM7 Bbm7 Gm7 Gbm7 Fm7 Fb7 EbM7/Gbm7 Fm7/E6 ',
	'EbM7 BbM7 Gm7/Fm7 Fbm7/A7 BbM7 BbM7/Eb7 GbM7 GbM7/Cb7 FbM7 Fm7/Bb7 Gm7/C7 Fm7/Bb7 ',
	'EbM7 Dm7/G7 Cm7/F7 FbM7/A7 BbM7 BbM7/Db7 Gm7 Gbm7/Cb7 Fm7 Bb7 Gm7/C7 Fm7/Bb7 ',
	'EbM7 Dm7/G7 Cm7/F7 FbM7/A7 AbM7 Am7/D7 Gm7 Gbm7/Cb7 Fm7 Bb7/Ab7 Gm7/C7 Fm7/Bb7 ',
	'Em7/A7 Dm7/G7 Cm7/F7 Bbm7/Eb7 AbM7 Abm7/Db7 GbM7 Gbm7/Cb7 FbM7 Fm7/Bb7 Gm7/C7 Fm7/Bb7 ',
	'EbM7 Em7/A7 DM7 DbM7/CbM7 AbM7 Am7/D7 GM7 Gm7/C7 FM7 FbM7 EbM7/GbM7 FM7/E6 '
	],

	'E':[
	'E7 E7 E7 E7 Bb7 Bb7 E7 E7 B7 B7 E7 E7 ',
	'E7 E7 E7 E7 Bb7 Bb7 E7 E7 B7 Bb7 E7 B7 ',
	'E7 Bb7 E7 E7 Bb7 Bb7 E7 E7 F#7 B7 E7 B7 ',
	'E7 Bb7 E7 E7 Bb7 Bb7 E7 C#7 F#7 B7 E7 B7 ',
	'E7 Bb7 E7 E7 Bb7 Bb7 E7 C#7 F#m7 B7 E7 F#m7/B7 ',
	'E7 Bb7 E7 E7 Bb7 Eb7 E7 C#7 C7 B7 E7 C7/B7 ',
	'E7 Bb7 E7 Bm7/E7 Bb7 Eb7 E7/G#m7 C#7 F#m7 B7 G#m7/C#7 F#m7/B7 ',
	'E7 Bb7 E7 Bm7/E7 Bb7 Eb7 G#m7 C#7 F#m7 B7 G#m7/C#7 F#m7/B7 ',
	'E7 A7 E7 Bm7/E7 A7 A#m7/D#7 E7/C#7 D7/C#7 F#m7 B7/A7 G#m7/C#7 F#m7/B7 ',
	'EM7 D#m7/G#7 C#m7/F#7 Bm7/E7 A7 A#dim7 G#m7/C#7 GM7/C7 F#m7 Cm7/F7 E7/C#7 F#m7/B7 ',
	'EM7 D#M7/Dm7 C#m7/Cm7 Bm7/Bb7 BbM7 Bbm7 G#m7 Gm7 F#m7 B7 G#m7/G#dim7 F#m7/F6 ',
	'EM7 BbM7 G#m7/F#m7 Fm7/Cb7 BbM7 Bbm7 G#m7 Gm7 F#m7 F7 EM7/Gm7 F#m7/F6 ',
	'EM7 BbM7 G#m7/F#m7 Fm7/Bb7 BbM7 BbM7/Eb7 GM7 GM7/C7 FM7 F#m7/B7 G#m7/C#7 F#m7/B7 ',
	'EM7 D#m7/G#7 C#m7/F#7 FM7/Bb7 BbM7 BbM7/D7 G#m7 Gm7/C7 F#m7 B7 G#m7/C#7 F#m7/B7 ',
	'EM7 D#m7/G#7 C#m7/F#7 FM7/Bb7 AM7 A#m7/D#7 G#m7 Gm7/C7 F#m7 B7/A7 G#m7/C#7 F#m7/B7 ',
	'E#m7/A#7 D#m7/G#7 C#m7/F#7 Bm7/E7 AM7 Am7/D7 GM7 Gm7/C7 FM7 F#m7/B7 G#m7/C#7 F#m7/B7 ',
	'EM7 E#m7/A#7 D#M7 DM7/CM7 AM7 A#m7/D#7 G#M7 G#m7/C#7 F#M7 FM7 EM7/GM7 F#M7/F6 '
	],

	'F':[
	'F7 F7 F7 F7 Bb7 Bb7 F7 F7 C7 C7 F7 F7 ',
	'F7 F7 F7 F7 Bb7 Bb7 F7 F7 C7 Bb7 F7 C7 ',
	'F7 Bb7 F7 F7 Bb7 Bb7 F7 F7 G7 C7 F7 C7 ',
	'F7 Bb7 F7 F7 Bb7 Bb7 F7 D7 G7 C7 F7 C7 ',
	'F7 Bb7 F7 F7 Bb7 Bb7 F7 D7 Gm7 C7 F7 Gm7/C7 ',
	'F7 Bb7 F7 F7 Bb7 Eb7 F7 D7 Db7 C7 F7 Db7/C7 ',
	'F7 Bb7 F7 Cm7/F7 Bb7 Eb7 F7/Am7 D7 Gm7 C7 Am7/D7 Gm7/C7 ',
	'F7 Bb7 F7 Cm7/F7 Bb7 Eb7 Am7 D7 Gm7 C7 Am7/D7 Gm7/C7 ',
	'F7 Bb7 F7 Cm7/F7 Bb7 Cbm7/E7 F7/D7 Eb7/D7 Gm7 C7/Bb7 Am7/D7 Gm7/C7 ',
	'FM7 Em7/A7 Dm7/G7 Cm7/F7 Bb7 Cbdim7 Am7/D7 AbM7/Db7 Gm7 Dbm7/Gb7 F7/D7 Gm7/C7 ',
	'FM7 EM7/Ebm7 Dm7/Dbm7 Cm7/Cb7 BbM7 Bbm7 Am7 Abm7 Gm7 C7 Am7/Adim7 Gm7/Gb6 ',
	'FM7 BbM7 Am7/Gm7 Gbm7/Cb7 BbM7 Bbm7 Am7 Abm7 Gm7 Gb7 FM7/Abm7 Gm7/Gb6 ',
	'FM7 BbM7 Am7/Gm7 Gbm7/Cb7 BbM7 BbM7/Eb7 AbM7 AbM7/Db7 GbM7 Gm7/C7 Am7/D7 Gm7/C7 ',
	'FM7 Em7/A7 Dm7/G7 GbM7/Cb7 BbM7 BbM7/Eb7 Am7 Abm7/Db7 Gm7 C7 Am7/D7 Gm7/C7 ',
	'FM7 Em7/A7 Dm7/G7 GbM7/Cb7 BbM7 Cbm7/E7 Am7 Abm7/Db7 Gm7 C7/Bb7 Am7/D7 Gm7/C7 ',
	'F#m7/Cb7 Em7/A7 Dm7/G7 Cm7/F7 BbM7 Bbm7/Eb7 AbM7 Abm7/Db7 GbM7 Gm7/C7 Am7/D7 Gm7/C7 ',
	'FM7 F#m7/Cb7 EM7 EbM7/DbM7 BbM7 Cbm7/E7 AM7 Am7/D7 GM7 GbM7 FM7/AbM7 GM7/Gb6 '
	],

	'F#':[
	'F#7 F#7 F#7 F#7 Bb7 Bb7 F#7 F#7 C#7 C#7 F#7 F#7 ',
	'F#7 F#7 F#7 F#7 Bb7 Bb7 F#7 F#7 C#7 Bb7 F#7 C#7 ',
	'F#7 Bb7 F#7 F#7 Bb7 Bb7 F#7 F#7 G#7 C#7 F#7 C#7 ',
	'F#7 Bb7 F#7 F#7 Bb7 Bb7 F#7 D#7 G#7 C#7 F#7 C#7 ',
	'F#7 Bb7 F#7 F#7 Bb7 Bb7 F#7 D#7 G#m7 C#7 F#7 G#m7/C#7 ',
	'F#7 Bb7 F#7 F#7 Bb7 Eb7 F#7 D#7 D7 C#7 F#7 D7/C#7 ',
	'F#7 Bb7 F#7 C#m7/F#7 Bb7 Eb7 F#7/A#m7 D#7 G#m7 C#7 A#m7/D#7 G#m7/C#7 ',
	'F#7 Bb7 F#7 C#m7/F#7 Bb7 Eb7 A#m7 D#7 G#m7 C#7 A#m7/D#7 G#m7/C#7 ',
	'F#7 Cb7 F#7 C#m7/F#7 Cb7 Cm7/F7 F#7/D#7 Fb7/D#7 G#m7 C#7/Cb7 A#m7/D#7 G#m7/C#7 ',
	'F#M7 Fm7/A#7 D#m7/G#7 C#m7/F#7 Cb7 Cdim7 A#m7/D#7 AM7/D7 G#m7 Dm7/G7 F#7/D#7 G#m7/C#7 ',
	'F#M7 FM7/Fbm7 D#m7/Dm7 C#m7/C7 BbM7 Bbm7 A#m7 Am7 G#m7 C#7 A#m7/A#dim7 G#m7/G6 ',
	'F#M7 BbM7 A#m7/G#m7 Gm7/Cb7 BbM7 Bbm7 A#m7 Am7 G#m7 G7 F#M7/Am7 G#m7/G6 ',
	'F#M7 BbM7 A#m7/G#m7 Gm7/C7 BbM7 BbM7/Eb7 AM7 AM7/D7 GM7 G#m7/C#7 A#m7/D#7 G#m7/C#7 ',
	'F#M7 Fm7/A#7 D#m7/G#7 GM7/C7 BbM7 BbM7/Fb7 A#m7 Am7/D7 G#m7 C#7 A#m7/D#7 G#m7/C#7 ',
	'F#M7 Fm7/A#7 D#m7/G#7 GM7/C7 CbM7 Cm7/F7 A#m7 Am7/D7 G#m7 C#7/Cb7 A#m7/D#7 G#m7/C#7 ',
	'Gm7/C7 Fm7/A#7 D#m7/G#7 C#m7/F#7 CbM7 Cbm7/Fb7 AM7 Am7/D7 GM7 G#m7/C#7 A#m7/D#7 G#m7/C#7 ',
	'F#M7 Gm7/C7 FM7 FbM7/DM7 CbM7 Cm7/F7 A#M7 A#m7/D#7 G#M7 GM7 F#M7/AM7 G#M7/G6 '
	],

	'Gb':[
	'Gb7 Gb7 Gb7 Gb7 Bb7 Bb7 Gb7 Gb7 Db7 Db7 Gb7 Gb7 ',
	'Gb7 Gb7 Gb7 Gb7 Bb7 Bb7 Gb7 Gb7 Db7 Bb7 Gb7 Db7 ',
	'Gb7 Bb7 Gb7 Gb7 Bb7 Bb7 Gb7 Gb7 Ab7 Db7 Gb7 Db7 ',
	'Gb7 Bb7 Gb7 Gb7 Bb7 Bb7 Gb7 Eb7 Ab7 Db7 Gb7 Db7 ',
	'Gb7 Bb7 Gb7 Gb7 Bb7 Bb7 Gb7 Eb7 Abm7 Db7 Gb7 Abm7/Db7 ',
	'Gb7 Bb7 Gb7 Gb7 Bb7 Eb7 Gb7 Eb7 D7 Db7 Gb7 D7/Db7 ',
	'Gb7 Bb7 Gb7 Dbm7/Gb7 Bb7 Eb7 Gb7/Bbm7 Eb7 Abm7 Db7 Bbm7/Eb7 Abm7/Db7 ',
	'Gb7 Bb7 Gb7 Dbm7/Gb7 Bb7 Eb7 Bbm7 Eb7 Abm7 Db7 Bbm7/Eb7 Abm7/Db7 ',
	'Gb7 Cb7 Gb7 Dbm7/Gb7 Cb7 Cm7/F7 Gb7/Eb7 Fb7/Eb7 Abm7 Db7/Cb7 Bbm7/Eb7 Abm7/Db7 ',
	'GbM7 Fm7/Bb7 Ebm7/Ab7 Dbm7/Gb7 Cb7 Cdim7 Bbm7/Eb7 AM7/D7 Abm7 Dm7/G7 Gb7/Eb7 Abm7/Db7 ',
	'GbM7 FM7/Fbm7 Ebm7/Dm7 Dbm7/C7 BbM7 Bbm7 Bbm7 Am7 Abm7 Db7 Bbm7/Bbdim7 Abm7/G6 ',
	'GbM7 BbM7 Bbm7/Abm7 Gm7/Cb7 BbM7 Bbm7 Bbm7 Am7 Abm7 G7 GbM7/Am7 Abm7/G6 ',
	'GbM7 BbM7 Bbm7/Abm7 Gm7/C7 BbM7 BbM7/Eb7 AM7 AM7/D7 GM7 Abm7/Db7 Bbm7/Eb7 Abm7/Db7 ',
	'GbM7 Fm7/Bb7 Ebm7/Ab7 GM7/C7 BbM7 BbM7/Fb7 Bbm7 Am7/D7 Abm7 Db7 Bbm7/Eb7 Abm7/Db7 ',
	'GbM7 Fm7/Bb7 Ebm7/Ab7 GM7/C7 CbM7 Cm7/F7 Bbm7 Am7/D7 Abm7 Db7/Cb7 Bbm7/Eb7 Abm7/Db7 ',
	'Gm7/C7 Fm7/Bb7 Ebm7/Ab7 Dbm7/Gb7 CbM7 Cbm7/Fb7 AM7 Am7/D7 GM7 Abm7/Db7 Bbm7/Eb7 Abm7/Db7 ',
	'GbM7 Gm7/C7 FM7 FbM7/DM7 CbM7 Cm7/F7 BbM7 Bbm7/Eb7 AbM7 GM7 GbM7/AM7 AbM7/G6 '
	],

	'G':[
	'G7 G7 G7 G7 Bb7 Bb7 G7 G7 D7 D7 G7 G7 ',
	'G7 G7 G7 G7 Bb7 Bb7 G7 G7 D7 Bb7 G7 D7 ',
	'G7 Bb7 G7 G7 Bb7 Bb7 G7 G7 A7 D7 G7 D7 ',
	'G7 Bb7 G7 G7 Bb7 Bb7 G7 E7 A7 D7 G7 D7 ',
	'G7 Bb7 G7 G7 Bb7 Bb7 G7 E7 Am7 D7 G7 Am7/D7 ',
	'G7 Bb7 G7 G7 Bb7 Eb7 G7 E7 Eb7 D7 G7 Eb7/D7 ',
	'G7 Bb7 G7 Dm7/G7 Bb7 Eb7 G7/Bm7 E7 Am7 D7 Bm7/E7 Am7/D7 ',
	'G7 Bb7 G7 Dm7/G7 Bb7 Eb7 Bm7 E7 Am7 D7 Bm7/E7 Am7/D7 ',
	'G7 C7 G7 Dm7/G7 C7 C#m7/F#7 G7/E7 F7/E7 Am7 D7/C7 Bm7/E7 Am7/D7 ',
	'GM7 F#m7/B7 Em7/A7 Dm7/G7 C7 C#dim7 Bm7/E7 BbM7/Eb7 Am7 Ebm7/Ab7 G7/E7 Am7/D7 ',
	'GM7 F#M7/Fm7 Em7/Ebm7 Dm7/Db7 BbM7 Bbm7 Bm7 Bbm7 Am7 D7 Bm7/Bdim7 Am7/Ab6 ',
	'GM7 BbM7 Bm7/Am7 Abm7/Cb7 BbM7 Bbm7 Bm7 Bbm7 Am7 Ab7 GM7/Bbm7 Am7/Ab6 ',
	'GM7 BbM7 Bm7/Am7 Abm7/Db7 BbM7 BbM7/Eb7 BbM7 BbM7/Eb7 AbM7 Am7/D7 Bm7/E7 Am7/D7 ',
	'GM7 F#m7/B7 Em7/A7 AbM7/Db7 BbM7 BbM7/F7 Bm7 Bbm7/Eb7 Am7 D7 Bm7/E7 Am7/D7 ',
	'GM7 F#m7/B7 Em7/A7 AbM7/Db7 CM7 C#m7/F#7 Bm7 Bbm7/Eb7 Am7 D7/C7 Bm7/E7 Am7/D7 ',
	'G#m7/C#7 F#m7/B7 Em7/A7 Dm7/G7 CM7 Cm7/F7 BbM7 Bbm7/Eb7 AbM7 Am7/D7 Bm7/E7 Am7/D7 ',
	'GM7 G#m7/C#7 F#M7 FM7/EbM7 CM7 C#m7/F#7 BM7 Bm7/E7 AM7 AbM7 GM7/BbM7 AM7/Ab6 '
	],

	'G#':[
	'G#7 G#7 G#7 G#7 Bb7 Bb7 G#7 G#7 D#7 D#7 G#7 G#7 ',
	'G#7 G#7 G#7 G#7 Bb7 Bb7 G#7 G#7 D#7 Bb7 G#7 D#7 ',
	'G#7 Bb7 G#7 G#7 Bb7 Bb7 G#7 G#7 A#7 D#7 G#7 D#7 ',
	'G#7 Bb7 G#7 G#7 Bb7 Bb7 G#7 F7 A#7 D#7 G#7 D#7 ',
	'G#7 Bb7 G#7 G#7 Bb7 Bb7 G#7 F7 A#m7 D#7 G#7 A#m7/D#7 ',
	'G#7 Bb7 G#7 G#7 Bb7 Eb7 G#7 F7 Fb7 D#7 G#7 Fb7/D#7 ',
	'G#7 Bb7 G#7 D#m7/G#7 Bb7 Eb7 G#7/Cm7 F7 A#m7 D#7 Cm7/F7 A#m7/D#7 ',
	'G#7 Bb7 G#7 D#m7/G#7 Bb7 Eb7 Cm7 F7 A#m7 D#7 Cm7/F7 A#m7/D#7 ',
	'G#7 Db7 G#7 D#m7/G#7 Db7 Dm7/G7 G#7/F7 Gb7/F7 A#m7 D#7/Db7 Cm7/F7 A#m7/D#7 ',
	'G#M7 Gm7/C7 Fm7/A#7 D#m7/G#7 Db7 Ddim7 Cm7/F7 CbM7/Fb7 A#m7 Fbm7/A7 G#7/F7 A#m7/D#7 ',
	'G#M7 GM7/Gbm7 Fm7/Fbm7 D#m7/D7 BbM7 Bbm7 Cm7 Cbm7 A#m7 D#7 Cm7/Cdim7 A#m7/A6 ',
	'G#M7 BbM7 Cm7/A#m7 Am7/Cb7 BbM7 Bbm7 Cm7 Cbm7 A#m7 A7 G#M7/Cbm7 A#m7/A6 ',
	'G#M7 BbM7 Cm7/A#m7 Am7/D7 BbM7 BbM7/Eb7 CbM7 CbM7/Fb7 AM7 A#m7/D#7 Cm7/F7 A#m7/D#7 ',
	'G#M7 Gm7/C7 Fm7/A#7 AM7/D7 BbM7 BbM7/Gb7 Cm7 Cbm7/Fb7 A#m7 D#7 Cm7/F7 A#m7/D#7 ',
	'G#M7 Gm7/C7 Fm7/A#7 AM7/D7 DbM7 Dm7/G7 Cm7 Cbm7/Fb7 A#m7 D#7/Db7 Cm7/F7 A#m7/D#7 ',
	'Am7/D7 Gm7/C7 Fm7/A#7 D#m7/G#7 DbM7 Dbm7/Gb7 CbM7 Cbm7/Fb7 AM7 A#m7/D#7 Cm7/F7 A#m7/D#7 ',
	'G#M7 Am7/D7 GM7 GbM7/FbM7 DbM7 Dm7/G7 CM7 Cm7/F7 A#M7 AM7 G#M7/CbM7 A#M7/A6 '
	],

	'A':[
	'A7 A7 A7 A7 Bb7 Bb7 A7 A7 E7 E7 A7 A7 ',
	'A7 A7 A7 A7 Bb7 Bb7 A7 A7 E7 Bb7 A7 E7 ',
	'A7 Bb7 A7 A7 Bb7 Bb7 A7 A7 B7 E7 A7 E7 ',
	'A7 Bb7 A7 A7 Bb7 Bb7 A7 F#7 B7 E7 A7 E7 ',
	'A7 Bb7 A7 A7 Bb7 Bb7 A7 F#7 Bm7 E7 A7 Bm7/E7 ',
	'A7 Bb7 A7 A7 Bb7 Eb7 A7 F#7 F7 E7 A7 F7/E7 ',
	'A7 Bb7 A7 Em7/A7 Bb7 Eb7 A7/C#m7 F#7 Bm7 E7 C#m7/F#7 Bm7/E7 ',
	'A7 Bb7 A7 Em7/A7 Bb7 Eb7 C#m7 F#7 Bm7 E7 C#m7/F#7 Bm7/E7 ',
	'A7 D7 A7 Em7/A7 D7 D#m7/G#7 A7/F#7 G7/F#7 Bm7 E7/D7 C#m7/F#7 Bm7/E7 ',
	'AM7 G#m7/C#7 F#m7/B7 Em7/A7 D7 D#dim7 C#m7/F#7 CM7/F7 Bm7 Fm7/Bb7 A7/F#7 Bm7/E7 ',
	'AM7 G#M7/Gm7 F#m7/Fm7 Em7/Eb7 BbM7 Bbm7 C#m7 Cm7 Bm7 E7 C#m7/C#dim7 Bm7/Bb6 ',
	'AM7 BbM7 C#m7/Bm7 Bbm7/Cb7 BbM7 Bbm7 C#m7 Cm7 Bm7 Bb7 AM7/Cm7 Bm7/Bb6 ',
	'AM7 BbM7 C#m7/Bm7 Bbm7/Eb7 BbM7 BbM7/Eb7 CM7 CM7/F7 BbM7 Bm7/E7 C#m7/F#7 Bm7/E7 ',
	'AM7 G#m7/C#7 F#m7/B7 BbM7/Eb7 BbM7 BbM7/G7 C#m7 Cm7/F7 Bm7 E7 C#m7/F#7 Bm7/E7 ',
	'AM7 G#m7/C#7 F#m7/B7 BbM7/Eb7 DM7 D#m7/G#7 C#m7 Cm7/F7 Bm7 E7/D7 C#m7/F#7 Bm7/E7 ',
	'A#m7/D#7 G#m7/C#7 F#m7/B7 Em7/A7 DM7 Dm7/G7 CM7 Cm7/F7 BbM7 Bm7/E7 C#m7/F#7 Bm7/E7 ',
	'AM7 A#m7/D#7 G#M7 GM7/FM7 DM7 D#m7/G#7 C#M7 C#m7/F#7 BM7 BbM7 AM7/CM7 BM7/Bb6 '
	],

	'A#':[
	'A#7 A#7 A#7 A#7 Bb7 Bb7 A#7 A#7 F7 F7 A#7 A#7 ',
	'A#7 A#7 A#7 A#7 Bb7 Bb7 A#7 A#7 F7 Bb7 A#7 F7 ',
	'A#7 Bb7 A#7 A#7 Bb7 Bb7 A#7 A#7 C7 F7 A#7 F7 ',
	'A#7 Bb7 A#7 A#7 Bb7 Bb7 A#7 G7 C7 F7 A#7 F7 ',
	'A#7 Bb7 A#7 A#7 Bb7 Bb7 A#7 G7 Cm7 F7 A#7 Cm7/F7 ',
	'A#7 Bb7 A#7 A#7 Bb7 Eb7 A#7 G7 Gb7 F7 A#7 Gb7/F7 ',
	'A#7 Bb7 A#7 Fm7/A#7 Bb7 Eb7 A#7/Dm7 G7 Cm7 F7 Dm7/G7 Cm7/F7 ',
	'A#7 Bb7 A#7 Fm7/A#7 Bb7 Eb7 Dm7 G7 Cm7 F7 Dm7/G7 Cm7/F7 ',
	'A#7 Eb7 A#7 Fm7/A#7 Eb7 Em7/A7 A#7/G7 Ab7/G7 Cm7 F7/Eb7 Dm7/G7 Cm7/F7 ',
	'A#M7 Am7/D7 Gm7/C7 Fm7/A#7 Eb7 Edim7 Dm7/G7 DbM7/Gb7 Cm7 Gbm7/Cb7 A#7/G7 Cm7/F7 ',
	'A#M7 AM7/Abm7 Gm7/Gbm7 Fm7/Fb7 BbM7 Bbm7 Dm7 Dbm7 Cm7 F7 Dm7/Ddim7 Cm7/B6 ',
	'A#M7 BbM7 Dm7/Cm7 Cbm7/Cb7 BbM7 Bbm7 Dm7 Dbm7 Cm7 Cb7 A#M7/Dbm7 Cm7/B6 ',
	'A#M7 BbM7 Dm7/Cm7 Cbm7/Fb7 BbM7 BbM7/Eb7 DbM7 DbM7/Gb7 CbM7 Cm7/F7 Dm7/G7 Cm7/F7 ',
	'A#M7 Am7/D7 Gm7/C7 CbM7/Fb7 BbM7 BbM7/Ab7 Dm7 Dbm7/Gb7 Cm7 F7 Dm7/G7 Cm7/F7 ',
	'A#M7 Am7/D7 Gm7/C7 CbM7/Fb7 EbM7 Em7/A7 Dm7 Dbm7/Gb7 Cm7 F7/Eb7 Dm7/G7 Cm7/F7 ',
	'Bm7/E7 Am7/D7 Gm7/C7 Fm7/A#7 EbM7 Ebm7/Ab7 DbM7 Dbm7/Gb7 CbM7 Cm7/F7 Dm7/G7 Cm7/F7 ',
	'A#M7 Bm7/E7 AM7 AbM7/GbM7 EbM7 Em7/A7 DM7 Dm7/G7 CM7 CbM7 A#M7/DbM7 CM7/B6 '
	],

	'Bb':[
	'Bb7 Bb7 Bb7 Bb7 Bb7 Bb7 Bb7 Bb7 F7 F7 Bb7 Bb7 ',
	'Bb7 Bb7 Bb7 Bb7 Bb7 Bb7 Bb7 Bb7 F7 Bb7 Bb7 F7 ',
	'Bb7 Bb7 Bb7 Bb7 Bb7 Bb7 Bb7 Bb7 C7 F7 Bb7 F7 ',
	'Bb7 Bb7 Bb7 Bb7 Bb7 Bb7 Bb7 G7 C7 F7 Bb7 F7 ',
	'Bb7 Bb7 Bb7 Bb7 Bb7 Bb7 Bb7 G7 Cm7 F7 Bb7 Cm7/F7 ',
	'Bb7 Bb7 Bb7 Bb7 Bb7 Eb7 Bb7 G7 Gb7 F7 Bb7 Gb7/F7 ',
	'Bb7 Bb7 Bb7 Fm7/Bb7 Bb7 Eb7 Bb7/Dm7 G7 Cm7 F7 Dm7/G7 Cm7/F7 ',
	'Bb7 Bb7 Bb7 Fm7/Bb7 Bb7 Eb7 Dm7 G7 Cm7 F7 Dm7/G7 Cm7/F7 ',
	'Bb7 Eb7 Bb7 Fm7/Bb7 Eb7 Em7/A7 Bb7/G7 Ab7/G7 Cm7 F7/Eb7 Dm7/G7 Cm7/F7 ',
	'BbM7 Am7/D7 Gm7/C7 Fm7/Bb7 Eb7 Edim7 Dm7/G7 DbM7/Gb7 Cm7 Gbm7/Cb7 Bb7/G7 Cm7/F7 ',
	'BbM7 AM7/Abm7 Gm7/Gbm7 Fm7/Fb7 BbM7 Bbm7 Dm7 Dbm7 Cm7 F7 Dm7/Ddim7 Cm7/Cb6 ',
	'BbM7 BbM7 Dm7/Cm7 Cbm7/Cb7 BbM7 Bbm7 Dm7 Dbm7 Cm7 Cb7 BbM7/Dbm7 Cm7/Cb6 ',
	'BbM7 BbM7 Dm7/Cm7 Cbm7/Fb7 BbM7 BbM7/Eb7 DbM7 DbM7/Gb7 CbM7 Cm7/F7 Dm7/G7 Cm7/F7 ',
	'BbM7 Am7/D7 Gm7/C7 CbM7/Fb7 BbM7 BbM7/Ab7 Dm7 Dbm7/Gb7 Cm7 F7 Dm7/G7 Cm7/F7 ',
	'BbM7 Am7/D7 Gm7/C7 CbM7/Fb7 EbM7 Em7/A7 Dm7 Dbm7/Gb7 Cm7 F7/Eb7 Dm7/G7 Cm7/F7 ',
	'Bm7/E7 Am7/D7 Gm7/C7 Fm7/Bb7 EbM7 Ebm7/Ab7 DbM7 Dbm7/Gb7 CbM7 Cm7/F7 Dm7/G7 Cm7/F7 ',
	'BbM7 Bm7/E7 AM7 AbM7/GbM7 EbM7 Em7/A7 DM7 Dm7/G7 CM7 CbM7 BbM7/DbM7 CM7/Cb6 '
	],

	'B':[
	'B7 B7 B7 B7 Bb7 Bb7 B7 B7 F#7 F#7 B7 B7 ',
	'B7 B7 B7 B7 Bb7 Bb7 B7 B7 F#7 Bb7 B7 F#7 ',
	'B7 Bb7 B7 B7 Bb7 Bb7 B7 B7 C#7 F#7 B7 F#7 ',
	'B7 Bb7 B7 B7 Bb7 Bb7 B7 G#7 C#7 F#7 B7 F#7 ',
	'B7 Bb7 B7 B7 Bb7 Bb7 B7 G#7 C#m7 F#7 B7 C#m7/F#7 ',
	'B7 Bb7 B7 B7 Bb7 Eb7 B7 G#7 G7 F#7 B7 G7/F#7 ',
	'B7 Bb7 B7 F#m7/B7 Bb7 Eb7 B7/D#m7 G#7 C#m7 F#7 D#m7/G#7 C#m7/F#7 ',
	'B7 Bb7 B7 F#m7/B7 Bb7 Eb7 D#m7 G#7 C#m7 F#7 D#m7/G#7 C#m7/F#7 ',
	'B7 Fb7 B7 F#m7/B7 Fb7 Fm7/A#7 B7/G#7 A7/G#7 C#m7 F#7/Fb7 D#m7/G#7 C#m7/F#7 ',
	'BM7 A#m7/D#7 G#m7/C#7 F#m7/B7 Fb7 Fdim7 D#m7/G#7 DM7/G7 C#m7 Gm7/C7 B7/G#7 C#m7/F#7 ',
	'BM7 A#M7/Am7 G#m7/Gm7 F#m7/F7 BbM7 Bbm7 D#m7 Dm7 C#m7 F#7 D#m7/D#dim7 C#m7/C6 ',
	'BM7 BbM7 D#m7/C#m7 Cm7/Cb7 BbM7 Bbm7 D#m7 Dm7 C#m7 C7 BM7/Dm7 C#m7/C6 ',
	'BM7 BbM7 D#m7/C#m7 Cm7/F7 BbM7 BbM7/Eb7 DM7 DM7/G7 CM7 C#m7/F#7 D#m7/G#7 C#m7/F#7 ',
	'BM7 A#m7/D#7 G#m7/C#7 CM7/F7 BbM7 BbM7/A7 D#m7 Dm7/G7 C#m7 F#7 D#m7/G#7 C#m7/F#7 ',
	'BM7 A#m7/D#7 G#m7/C#7 CM7/F7 FbM7 Fm7/A#7 D#m7 Dm7/G7 C#m7 F#7/Fb7 D#m7/G#7 C#m7/F#7 ',
	'Cm7/F7 A#m7/D#7 G#m7/C#7 F#m7/B7 FbM7 Fbm7/A7 DM7 Dm7/G7 CM7 C#m7/F#7 D#m7/G#7 C#m7/F#7 ',
	'BM7 m7/F7 A#M7 AM7/GM7 FbM7 Fm7/A#7 D#M7 D#m7/G#7 C#M7 CM7 BM7/DM7 C#M7/C6 '
	]
}

@app.route('/bluesGen')
def BluesGenerator():

	tone = request.args.get('tone','')

	try:
		if tone:
			blues_grid = random.choice([blues_db[tone][0],blues_db[tone][1],blues_db[tone][2],blues_db[tone][3],blues_db[tone][4],blues_db[tone][5],blues_db[tone][6],blues_db[tone][7],blues_db[tone][8],blues_db[tone][9],blues_db[tone][10],blues_db[tone][11],blues_db[tone][12],blues_db[tone][13],blues_db[tone][14],blues_db[tone][15],blues_db[tone][16]])
			pattern = re.compile(r'(\S+\s\S+\s\S+\s\S+\s)')
			bluesGen_results = re.sub(pattern,r'\1'+'<br><br>',blues_grid)
			bluesGen_results = re.sub(' ','  |',bluesGen_results)
			bluesGen_results = re.sub(r'((([A-G]#)|([A-G]b)|([A-G]))?(\b|7|6|dim7|M7|m7))','<a href="https://www.jazzreal.org/voiceGen?query='+r'\1'+'\" onclick=\"window.open(this.href, \'Popup\', \'scrollbars=1,resizable=1,height=600,width=400\'); return false;\">'+r'\1'+'</a>',bluesGen_results)
			bluesGen_results = '<h2><pre>'+bluesGen_results+'</pre></h2>'
			bluesGen_results = re.sub('<a href=\"https://www\.jazzreal\.org/voiceGen\?query=\" onclick=\"window.open\(this\.href, \'Popup\', \'scrollbars=1,resizable=1,height=600,width=400\'\); return false;\"></a>','',bluesGen_results)
		else:
			blues_grid = random.choice([blues_db['C'][0],blues_db['C'][1],blues_db['C'][2],blues_db['C'][3],blues_db['C'][4],blues_db['C'][5],blues_db['C'][6],blues_db['C'][7],blues_db['C'][8],blues_db['C'][9],blues_db['C'][10],blues_db['C'][11],blues_db['C'][12],blues_db['C'][13],blues_db['C'][14],blues_db['C'][15],blues_db['C'][16]])
			pattern = re.compile(r'(\S+\s\S+\s\S+\s\S+\s)')
			bluesGen_results = re.sub(pattern,r'\1'+'<br><br>',blues_grid)
			bluesGen_results = re.sub(' ','  |',bluesGen_results)
			bluesGen_results = re.sub(r'((([A-G]#)|([A-G]b)|([A-G]))?(\b|7|6|dim7|M7|m7))','<a href="https://www.jazzreal.org/voiceGen?query='+r'\1'+'\" onclick=\"window.open(this.href, \'Popup\', \'scrollbars=1,resizable=1,height=600,width=400\'); return false;\">'+r'\1'+'</a>',bluesGen_results)
			bluesGen_results = '<h2><pre>'+bluesGen_results+'</pre></h2>'
			bluesGen_results = re.sub('<a href=\"https://www\.jazzreal\.org/voiceGen\?query=\" onclick=\"window.open\(this\.href, \'Popup\', \'scrollbars=1,resizable=1,height=600,width=400\'\); return false;\"></a>','',bluesGen_results)

	except KeyError:
		blues_grid = random.choice([blues_db['C'][0],blues_db['C'][1],blues_db['C'][2],blues_db['C'][3],blues_db['C'][4],blues_db['C'][5],blues_db['C'][6],blues_db['C'][7],blues_db['C'][8],blues_db['C'][9],blues_db['C'][10],blues_db['C'][11],blues_db['C'][12],blues_db['C'][13],blues_db['C'][14],blues_db['C'][15],blues_db['C'][16]])
		pattern = re.compile(r'(\S+\s\S+\s\S+\s\S+\s)')
		bluesGen_results = re.sub(pattern,r'\1'+'<br><br>',blues_grid)
		bluesGen_results = re.sub(' ','  |',bluesGen_results)
		bluesGen_results = re.sub(r'((([A-G]#)|([A-G]b)|([A-G]))?(\b|7|6|dim7|M7|m7))','<a href="https://www.jazzreal.org/voiceGen?query='+r'\1'+'\" onclick=\"window.open(this.href, \'Popup\', \'scrollbars=1,resizable=1,height=600,width=400\'); return false;\">'+r'\1'+'</a>',bluesGen_results)
		bluesGen_results = '<h2><pre>'+bluesGen_results+'</pre></h2>'
		bluesGen_results = re.sub('<a href=\"https://www\.jazzreal\.org/voiceGen\?query=\" onclick=\"window.open\(this\.href, \'Popup\', \'scrollbars=1,resizable=1,height=600,width=400\'\); return false;\"></a>','',bluesGen_results)

	return render_template('view_bluesGen.html', bluesGen_results=bluesGen_results)

###
### Hum : app looking up tunes for moods
###

##BUILD DICT OF SYNONYMS
# This method adds all given synonyms into the correct dictionary entry.
def extendDictEntry(dict_syn, key, xmlSynonyms):
	for child in xmlSynonyms:

		childText = child.text

		if (childText not in dict_syn[key]):
			dict_syn[key].extend([childText])
	return dict_syn

# This method buils the synonyms dictionary from the WoNeF file.
tree = ET.parse('jazzreal/static/wonef-coverage-0.1.xml')

root = tree.getroot()
dict_syn = {}

# fill synonyms dictionary
for synset in root:
	for child in synset:
		if child.tag == "SYNONYM":
			for literal in child:
				currLiteralText = literal.text

				if currLiteralText in dict_syn:
					# add all SYNONYM tags text into the correct entry of the map
					extendDictEntry(dict_syn, currLiteralText, child)
				else:
					# create a new entry in the map
					dict_syn[currLiteralText] = [currLiteralText]
					extendDictEntry(dict_syn, currLiteralText, child)

corpus = {}

for title in list_titles:
	try:
		f = open('jazzreal/static/corpus-html/'+title+'.html', 'r')
		TEXT = f.read()
		title = re.search('<TITLE>(.*)</TITLE>', TEXT).group(1)
		grille = re.findall('>(.*):\n-([\w\W][^>]*)', TEXT)

		humeurs_extended = []
		humeurs = re.search('<humeurs>Humeurs=(.*)</humeurs>', TEXT).group(1)
		humeurs = re.findall('[a-zA-Z0-9_êâéèÉ]+',humeurs)
		humeurs = list(set(humeurs))

		for x in humeurs:
			try:
				humeurs_extended += dict_syn[x.lower()]
			except KeyError:
				pass

		corpus[title] = {'humeurs':''}
		corpus[title]['humeurs'] = list(humeurs_extended)
		for i in range(len(grille)):
			corpus[title][grille[i][0]]=grille[i][1]
	except AttributeError:
		pass

def pattern_build(words_query):
	moods_list = []
	words_tokenize = re.findall('[a-zA-Z0-9_êâéèÉ]+', words_query)
	words_length = len(words_tokenize)
	for i in range(words_length):
		moods_list.append(words_tokenize[i])
	return moods_list


@app.route('/Hume')
def Hume_search():

	viewHume_results = ''

	mood_query = request.args.get('texte','')

	if mood_query:
		viewHume_results = '<h4>recherche:"'+str(mood_query)+'"</h4>'
		viewHume_results += '<br>'
		viewHume_results += '<br>'
		rank = {}
		for i in list_titles:
			rank[i] = 0
		moods_list = pattern_build(mood_query)
		for word in moods_list:
			regex = re.compile(word,re.IGNORECASE)
			for i in list_titles:
				selectobj = filter(regex.search, corpus[i]['humeurs'])
				for val in selectobj:
					rank[i] += 1

		###ranking method with scores (1st and 2nd)
		x = max(rank.values())
		for i in list_titles:
			if rank[i] == x:
				#print(i+':'+str(x))
				viewHume_results += i+':'+str(x)
				viewHume_results += '<br>'

				try:
					if corpus[i]['a']:
						#print('>a:')
						viewHume_results += '>a:'
						viewHume_results += '<br>'
						#print(corpus[i]['a'])
						viewHume_results += str(corpus[i]['a'])
						viewHume_results += '<br>'
				except KeyError:
					pass
				rank.pop(i)

		y = max(rank.values())
		for j in list_titles:
			try:
				if rank[j] == y:
					#print(j+':'+str(y))
					viewHume_results += j+':'+str(y)
					viewHume_results += '<br>'
					try:
						if corpus[j]['a']:
							#print('>a:')
							viewHume_results += '>a:'
							viewHume_results += '<br>'
							#print(corpus[j]['a'])
							viewHume_results += str(corpus[j]['a'])
							viewHume_results += '<br>'
					except KeyError:
						pass
					rank.pop(j)
			except KeyError:
				pass
	else:

		viewHume_results = 'pas de résultats'


	return render_template('view_hume.html', viewHume_results=viewHume_results)

corpus_sequence = {}

for title in list_titles:
	corpus_sequence[title] = {}
	try:
		f = open('jazzreal/static/corpus-html/'+title+'.html', 'r')
		TEXT = f.read()
		metric = re.search('<metric>(.*)</metric>', TEXT).group(1)
		key = re.search('<key>(.*)</key>', TEXT).group(1)
		grille = re.findall('>(.*):\n-([\w\W][^>]*)', TEXT)
		for i in range(len(grille)):
			corpus_sequence[title][grille[i][0]]=grille[i][1]
		corpus_sequence[title]['key'] = key
		corpus_sequence[title]['metric'] = metric
	except AttributeError:
		pass

#this method search by sequence of chords in all song's sections and rank the results
@app.route('/Sequence')
def Sequence_search():
	
	viewSequence_results = ''
	query = request.args.get('chords','')
	
	if query:
		rank = {}
		chord_query = re.findall(r'(?:[A-G]#|[A-G]b|[A-G])(?:6|7|maj7|Maj7|M7|m7\b|m7b5|mM7|mMaj7)', query)
		chord_query = ' '.join(list(chord_query))
		section = re.search('section:(.+)', query).group(1)
		
		for i in list_titles:
			rank[i] = 0
			try:
				to_search = ' '.join(re.findall('[A-G].[^\s]*\)',corpus_sequence[i][section]))
				to_search = re.sub('\(\d\)','',to_search)
				res = re.findall(chord_query, to_search)
				rank[i] += len(res)
			except KeyError:
				pass
		
		#print('recherche:['+query+']\n')
		viewSequence_results += '<b>recherche:['+query+']</b><br>'
		
		###ranking method by max score
		x = max(rank.values())
		if x != 0:
			for i in list_titles:
				try:
					if rank[i] == x:
						#print(i+':'+str(x))
						viewSequence_results = i+':'+str(x)
						#print('('+corpus_sequence[i]['key']+corpus_sequence[i]['metric']+')')
						viewSequence_results += '('+corpus_sequence[i]['key']+corpus_sequence[i]['metric']+')'
						#print('>'+section+':')
						viewSequence_results += '>'+section+':'
						#print(corpus_sequence[i][section])
						viewSequence_results += corpus_sequence[i][section]
				except KeyError:
					pass
				rank.pop(i)
		else:
			#print('pas de résultats')
			viewSequence_results += 'pas de résultats'
	else: 
		viewSequence_results += 'pas de résultats'

	return render_template('view_sequence.html', viewSequence_results=viewsequence_results)
	
if __name__ == "__main__":
    app.run()

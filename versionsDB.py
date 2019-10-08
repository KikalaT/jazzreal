# -*- coding: utf-8 -*-','\

import re
import sys

versions_dict = {'\
26-2\
':('\
Quartet Base•Allo ?•Circum-Disc•2009','\
John Coltrane•The Coltrane Legacy•Atlantic•1970','\
Ximo Tebar•Steps•Omix Records•2008','\
Quentin Collins•If Not Now Then When?•Sunlightsquare Records•2007','\
John Nugent Quintet•Live At The Blue Note (N.Y.C.)•DSM (2)•2000','\
Steve Heckman•Legacy: A Coltrane Tribute•Jazzed Media•2016','\
Joe Lovano•Quartets: Live At The Village Vanguard Volume 2•Blue Note•2015'),'\
\
34 Skidoo\
':('\
Bill Evans•The Paris Concert (Edition Two)•Elektra Musician•1984','\
Bill Evans•Montreux II•CTI Records•1970','\
Paul Motian•Bill Evans•JMT•1990','\
Bill Evans•In His Own Way•West Wind•1989','\
Bill Evans•Re: Person I Knew•Fantasy•1981'),'\
\
502 Blues\
':('\
Wayne Shorter•Adam\'s Apple•Blue Note•1966','\
Gebhard Ullmann•Per-Dee-Doo•NABEL•1990','\
Bill Holman / Mel Lewis Quintet•Jive For Five•Andex•1959','\
Jimmy Rowles•Sometime I\'m Happy Sometimes I\'m Blue•Orange Blue•1988','\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014'),'\
\
52nd Street Theme\
':('\
Dizzy Gillespie Septet•52nd Street Theme / Night In Tunisia•no label•0','\
Charlie Parker•One Night In Birdland•Columbia•1977','\
Miles Davis•The Last Bebop Session•Jazz Music Yesterday•1995','\
Sonny Rollins Quartet•Stuttgart 1963 Concert•Jazz Connoisseur•0','\
no artist•Dance Of The Infidels / 52nd Street Theme•Jazz Selection•1949','\
Sonny Rollins Quartet•In Europe 1963 - Vol. II•Jazz Up•1989','\
Charlie Parker•Volume 6: Young Bird Sep.-Nov. 1947•Média 7•1998','\
Sonny Rollins•Alternatives•Bluebird (3)•1992','\
Junko Onishi•Baroque•Verve Records•2010','\
Various•The Bebop Revolution•Bluebird (3)•1990','\
Bud Powell•Parisian Thoroughfares•Pablo Records•2003','\
Charlie Parker•At Their Rare Of All Rarest Performances Vol. 1•Kings Of Jazz•1975','\
no artist•Bouncing With Bud•Vogue Productions•1955','\
Bud Powell•I Remember Bud Powell•Records (3)•1982','\
The Quintet•Jazz At Massey Hall Volume One•Debut Records•1953'),'\
\
A Ballad For Doll\
':('\
Jackie McLean•Jackie\'s Bag•Blue Note•1960','\
Jackie McLean•Street Singer•Blue Note•1980','\
James Carter (3)•The Real Quietstorm•Atlantic Jazz•1995','\
Carmen McRae•The Great American Songbook•Atlantic•1972','\
Ella Fitzgerald•The Concert Years•Pablo Records•1994','\
Nina Simone•MP3 Collection•Digital Records (6)•0'),'\
\
A Beautiful Friendship\
':('\
Nat King Cole•Answer Me / A Beautiful Friendship•Capitol Records•1962','\
Ahmad Jamal•A Beautiful Friendship / Minor Moods•Cadet•1967','\
Ella Fitzgerald•A Beautiful Friendship / Stay There•Verve Records•1956','\
Mark Murphy•Mark Murphy - A Beautiful Friendship : Remembering Shirley Horn•Gearbox Records•2013','\
Ella Fitzgerald•I\'ll Always Be In Love With You•Verve Records•1962','\
Milt Jackson•Montreux \'77•Pablo Live•1977','\
Geri Allen•Some Aspects Of Water•Storyville•1997','\
Kenny Burrell•Togethering•Blue Note•1985','\
George Shearing•Light Airy & Swinging•MPS Records•1973'),'\
\
A Child is Born\
':('\
Terumasa Hino Sextet•Fuji•Victor•1972','\
Kenny Burrell•God Bless The Child•CTI Records•1971','\
Pepper Adams•Twelfth & Pingree•Enja Records•1975','\
Art Farmer•Big Blues•CTI Records•1979','\
Eddie Daniels•Brief Encounter•Muse Records•1980','\
Bill Evans•Quintessence•Fantasy•1977','\
Bobby Shew Quintet•Class Reunion•Sutra Records•1980','\
Jimmy Smith Trio•The Master II•Blue Note Records•1994','\
Joe B And Friends•Jazz At Blackie\'s•no label•0'),'\
\
A Family Joy\
':('\
Gary Burton Quartet•Country Roads & Other Places•RCA Victor•1969','\
Greg Koch•Radio Free Gristle•no label•2003','\
Danny Elfman•Music For A Darkened Theatre - Film & Television Music - Volume Two•MCA Soundtracks•1996','\
Prince•One Nite Alone... Live!•NPG Records•2002','\
Various•Warm And Happy•Columbia House•1977'),'\
\
A Felicidade\
':('\
Bola Sete•Bola Sete At The Monterey Jazz Festival•Verve Records•1967','\
Niels-Henning Ørsted Pedersen•Jaywalkin\'•SteepleChase•1975','\
Lee Konitz & The Brazilian Band•Brazilian Rhapsody•Venus Records (5)•1995','\
Camila Benson•Memories•One Voice (4)•1995','\
Lew Soloff•Hanalei Bay•Electric Bird•1985','\
Lyn Acton & Bossa Loco•O Amor Em Paz/A Six And Two Threes•Hear No Evil•2006','\
Joe Henderson•The Definitive Joe Henderson•Verve','\
 Records•2002','\
Beleza•Tribute To Antonio Carlos Jobim•Alfa•1995','\
Irio De Paula•Saudade Do Brasil•Folkstudio•1981'),'\
\
A Fine Romance\
':('\
Benny Goodman Sextet•Goodbye / A Fine Romance•Columbia•1956','\
Sammy Davis Jr.•I Go For You / A Fine Romance•Decca•1955','\
Yehudi Menuhin•Jealousy•EMI•1973','\
Dave Brubeck•Jazz Gallery•Philips•1954','\
Les Brown And His Orchestra•A Fine Romance / 1400 Dream Street•Columbia•1949','\
Fred Astaire•A Fine Romance (A Sarcastic Love Song) / The Waltz In Swingtime•Brunswick•1936','\
Oscar Peterson•Oscar Peterson Plays Jerome Kern•no label•1960','\
Joe Derise•Joe Derise Sings•Bethlehem Records•1955','\
Guy Lombardo And His Royal Canadians•Boo-Hoo•RCA Camden•1954','\
Billie Holiday•Jazz Masters (100 Ans De Jazz)•e.f.s.a. collection•1997','\
Dave Brubeck•Dave Brubeck Collection•CBS Records Australia Limited•1980','\
Martin Denny•Romantica•Liberty•1961','\
Benny Goodman Sextet•Date With The King•Columbia•1956','\
Martin Denny•Sayonara•Sunset Records•1967'),'\
\
A House Is Not A Home\
':('\
Sonny Rollins•The Cutting Edge•Milestone (4)•1974','\
Sarah Vaughan•Sarah Vaughan & The Jimmy Rowles Quintet•Mainstream Records•1974','\
Gene Ammons•My Way•Prestige•1971','\
Willis Jackson•West Africa•Muse Records•1974','\
Nelson Rangell•To Begin Again•Gaia Records•1988','\
Fay Claassen•Specially Arranged For Fay•no label•2003','\
Ramsey Lewis•Les Fleurs•Columbia•1983','\
The Bill Evans Trio•I Will Say Goodbye•Fantasy•1980','\
Joe Sample•Invitation•Warner Bros. Records•1993','\
Reggae Disco Rockers•I Saw The Light•Flower Records•2002'),'\
\
A Little Tear\
':('\
Toshiyuki Honda•The Super Quartet•Eastworld•1986','\
Hank Crawford•We Got A Good Thing Going•Kudu•1972','\
Sarah Vaughan•I Love Brazil!•Pablo today•1979','\
Willie Bobo•Tomorrow Is Here•Blue Note•1977','\
Catalyst (4)•The Complete Recordings Vol.2•Porter Records•2010','\
Ricky Peterson•A Tear Can Tell•Go Jazz•1995','\
Sonny Grey•En Directo •Sayton•1968','\
Willie Bobo•Lost And Found•Concord Records•2006','\
Perry Como•The Scene Changes•RCA Victor•1965','\
Sarah Vaughan•O Som Brasileiro De Sarah Vaughan•RCA Victor•1978','\
Marjorie Barnes•Once You’ve Been In Love•Jazz Between The Dikes•1993','\
Various•Wonderful World - 16 Original World Hits•MCA Records•1989','\
Danny Davis & The Nashville Brass•You Ain\'t Heard Nothin\' Yet•RCA Victor•1970','\
The Lennon Sisters•Can\'t Help Falling In Love•Dot Records•1962'),'\
\
A Lot Of Living To Do\
':('\
Frank Foster•Basie Is Our Boss•Argo (6)•1963','\
Gigi Cichellero Big Band•Stereo Hi-Fi Experience•IRT Imperial•1974','\
The John Young Trio•A Touch Of Pepper•Argo (6)•1963','\
Erroll Garner•Up In Erroll\'s Room•MPS Records•1968','\
Johnny Adams•The Verdict•Rounder Records•1995','\
Mel Davis Sextet•"Shoot" The Trumpet Player•Time Records (3)•1963','\
Mariska Veres•Shocking You•Red Bullet•1993','\
Johnny Adams•There Is Always One More Time•Rounder Records•2000','\
Sydney Thompson And His Orchestra•Modern In Tempo•Sydney Thompson Dance Records•1967','\
Shirley Bassey•In Person•United Artists Records•1965','\
Shirley Bassey•Shirley Bassey At The Pigalle•Columbia•1965','\
Frank Sinatra•The Very Best Of The Rat Pack•Reprise Records•2010'),'\
\
A Nightingale Sang in Berkeley Square\
':('\
Glenn Miller And His Orchestra•A Nightingale Sang In Berkeley Square / My Prayer•no label•1944','\
Harry Connick Jr.•Recipe For Love•CBS•1990','\
Glenn Miller And His Orchestra•A Nightingale Sang In Berkeley Square / Goodbye Little Darlin\' Goodbye•Bluebird (3)•1940','\
The Roland Kirk Quartet•Meets The Benny Golson Orchestra•Mercury•1963','\
Dexter Gordon•Gotham City•Columbia•1981','\
Marian McPartland•The Magnificent Marian McPartland - Volume 1•Savoy Records•0','\
Tete Montoliu•Body & Soul•Enja Records•1983','\
Sonny Rollins•This Is What I Do•Milestone (4)•2000','\
Tete Montoliu Trio•Catalonian Fire•SteepleChase•1974','\
Yoshiaki Masuo•A Subtle One•Jazz City•1991','\
Bud Shank Quartet•At Jazz Alley•Contemporary Records•1987','\
Stan Getz•Recorded Fall 1961•Verve Records•1961'),'\
\
A Quiet Place\
':('\
no artist•Collage•Soul Note•1984','\
Claude Williamson•La Fiesta•Interplay Records•1979','\
Randy Petersen•The Sounds Of Yosemite•Orange Tree Productions•1995','\
Ron Carter•A Song For You•Milestone (4)•1978','\
Michael Dowdle•Touch•Airus•1990','\
Various•Atlantic Jazz: Best Of The \'70s•Rhino Records (2)•1994','\
Marc Johnson (2)•The Sound Of Summer Running•Verve Records•1998','\
Ron Carter•Songs For You•Milestone (4)•2003','\
Katia Et Marielle Labèque•Love Of Colours•Sony Classical•1991','\
Max Roach•To The Max!•Enja Records•1992','\
Dave Boyer (2)•Come On Home•Word•1978','\
Alexandre Saada•Continuation To The End•Bee Jazz•2013'),'\
\
A Sleepin\' Bee\
':('\
Laura Swankey Quartet•Laura Swankey Quartet•Not On Label (Laura Swankey Self-released)•2013','\
Quincy Jones•This Is How I Feel About Jazz•ABC-Paramount•1957','\
The Bill Evans Trio•Quiet Now•Affinity•1981','\
The Bill Evans Trio•Camp Fortune 1974•Radio Canada International•1976','\
Sadayasu Fujii Trio•Like A Child•Victor•1977','\
James Torme•Comin\' Home•Rogalan Records•2005','\
Kenny Burrell•Soul Call•Prestige•1964','\
Kim Parker•"Havin\' Myself A Time"•Soul Note•1982','\
Marian McPartland Trio•Personal Choice•Concord Jazz•1983','\
Al Jarreau•1965•Ducale•1983','\
Various•Jazz-Club • Alto Sax•Verve Records•1989'),'\
\
A Song For You\
':('\
Buddy Greco•It\'s My Life•Pye Records•1972','\
Ben Sidran•Song For A Sucker Like You / One Way Grave•Arista Records•1977','\
Andy Williams•A Song For You / You\'ve Got A Friend•Columbia•1971','\
Kosei Uchida Trio•3 From Boston•Polydor•1982','\
Mike Garson•The Oxnard Sessions Volume Two•Reference Recordings•1993','\
Jaye P. Morgan•A Song For You / Do You Really Have A Heart•Beverly Hills•1971','\
Nancy Wilson•Forbidden Lover•Epic•1987','\
Billy Cobham•Life & Times•Atlantic•1976','\
The Ron Carter Nonet•Eight Plus•Seoul Records Inc.•1990','\
Eddy Palermo Ensemble•Jazz Fusion Mood•Penta Flowers•1985','\
Telly Savalas•Sweet Surprise•Papagayo•1980','\
Tutu Puoane•Song•Saphrane•2007','\
Django Reinhardt•Pêche à La Mouche•Verve Records•1991','\
John Serry Jr.•Jazziz•Chrysalis•1980','\
Christian McBride•A Family Affair•Verve Records•1998','\
Bruno Angelini•Open Land•La Buissonne•2018','\
Mike Campbell (2)•Secret Fantasy•Palo Alto Records•1982','\
David Benoit•Heroes•Peak Records (5)•2008','\
Dave Brubeck•1954 - 1972•CBS•1983','\
Various•The Stars In Stereo•Capitol Records•1957','\
Dave Holland•Music From Two Basses•ECM Records•1971'),'\
\
A Time For Love\
':('\
Bud Shank•Sidewinder•Pacific Jazz•1966','\
John Wagner•Blue In The Face/A Time For Love•Look Records (2)•0','\
Dick Griffin•A Dream For Rahsaan•Ruby Records (15)•1985','\
Sonny Red•Sonny Red•Mainstream Records•1971','\
Térez Montcalm•Songs for Shirley Horn•Universal Music•2011','\
Stan Getz Quartet•The Dolphin•Concord Jazz•1981','\
Percy Faith And His Orchestra And Chorus•For Those In Love / There Was A Time•Columbia•1968','\
Cal Tjader•Puttin\' It Together•Fantasy•1974','\
Monty Alexander•Overseas Special•Concord Jazz•1984','\
Hank Mobley Sextet•Hank•Blue Note•1957','\
John Coltrane•John Coltrane Plays For Lovers•Prestige•1966','\
Tony Bennett•I Left My Heart In San Francisco•CBS•1964','\
Ahmad Jamal•Digital Works•Atlantic•1985','\
Zoot Sims•Plays Johnny Mandel Quietly There•Pablo Records•1984','\
Gabe Baltazar•Stan Kenton Presents Gabe Baltazar•Creative World•1979','\
Jack Wilson•Easterly Winds•Blue Note•1967','\
Harry Connick Jr.•Come By Me•Columbia•1999'),'\
\
Ablution\
':('\
Lee Konitz•At Storyville•Black Lion Records•1988','\
Lee Konitz•Lee Konitz•Swingtime•1989','\
Lars Gullin Quartet•New Sounds From Europe - Vol. 3 Sweden•Vogue Records•1953','\
Lars Gullin•The Liquid Moves Of Lars Gullin Lost Jazz Files 1959 - 1963•Sonorama•2016','\
Dave Mihaly And Shimmering Leaves•Light In The Ring: The Ali Suite•Calar Music•2018','\
Lee Konitz•Sax Of A Kind - Lee Konitz In Sweden 1951/53•Dragon (8)•1979','\
Jef Gilson•The Archives•Jazzman•2013','\
Anthony Braxton•Quintet (Tristano) 1997•New Braxton House•2012'),'\
\
Actual Proof\
':('\
Herbie Hancock•Spank-A-Lee / Actual Proof•Columbia•1974','\
Herbie Hancock•Thrust•Columbia•1974','\
Herbie Hancock•Herbie Hancock•Columbia•1998','\
MVP (5)•Centrifugal Funk•Heading West•1991','\
Ximo Tebar•Steps•Omix Records•2008','\
Herbie Hancock•Flood•CBS/Sony•1975','\
Marcin Wasilewski Trio•Live•ECM Records•2018','\
Herbie Hancock•Ken Burns Jazz•Columbia•2000','\
Scott Henderson (2)•H B C•Tone Center•2012'),'\
\
Affirmation\
':('\
Dr. Tree•Dr. Tree•EMI•1976','\
Keiko Matsui•The Road...•Shanachie•2011','\
George Benson•Breezin\'•Warner Bros. Records•1976','\
The Al Gafa Quinteto•Leblon Beach•Pablo Records•1976'),'\
\
African Flower\
':('\
James Newton (2)•The African Flower (The Music Of Duke Ellington & Billy Strayhorn)•Blue Note•1985','\
Count Basie Orchestra•Afrique•Flying Dutchman•1971','\
Dollar Brand•African Dawn•Enja Records•1983','\
Count Basie Orchestra•Afrique•RCA International•1979','\
Gary Burton Quartet•Live In Tokyo•Atlantic•2013','\
Gary Burton Quartet•Live In Tokyo•Atlantic•1971','\
Count Basie Orchestra•Afrique•Doctor Jazz•1984','\
Duke Ellington•Money Jungle•United Artists Jazz•1962','\
Charlotte Halberg Trio•Summertime•Olufsen Records•1988','\
Orquesta Libre (2)•Plays Duke•Glamorous (2)•2014'),'\
\
Afro Blue\
':('\
John Coltrane•Coltrane In Tokyo Vol.2•MCA Records•1980','\
John Coltrane•Live In Paris Part 1•BYG Records•1972','\
Cal Tjader Sextet•Black Orchid / Afro Blue•Fantasy•0','\
Mongo Santamaria•"Summertime" - Digital At Montreux 1980•Pablo Live•1981','\
John Coltrane•Live In Paris Volume Two•Affinity•1980','\
John Coltrane•Africa & India•Jazz Masterworks•1985','\
John Coltrane•Live In Paris•BYG Records•0','\
Candido•In Indigo•ABC-Paramount•1958','\
Takao Uematsu•Straight Ahead •Trio Records•1977','\
The John Coltrane Quartet•The Complete 1963 Copenhagen Concert  •Gambit Records•2006'),'\
\
Afro-centric\
':('\
Joe Henderson•Power To The People•Milestone (4)•1969','\
Joe Henderson•The Milestone Years•Milestone (4)•1994'),'\
\
After the Rain\
':('\
Sting•After The Rain Has Fallen•A&M Records•2000','\
John Hicks•Power Trio •Novus•1991','\
John Coltrane•Dear Old Stockholm•GRP•1993','\
John Coltrane•Impressions•Impulse!•1963','\
Keisuke Doi•Across The Mountain•Oasis Productions•1995','\
Joe Chambers•Double Exposure•Muse Records•1978','\
Steve Narahara•Odyssey•Pausa Records•1985','\
Wayne Shorter•Tribute To John Coltrane - Live Under The Sky•Columbia•1987'),'\
\
After You\
':('\
Jimmy Lyons (2)•Push Pull•Hat Hut Records•1979','\
Les Brown And His Orchestra•Dardanella / After You•Columbia•1947','\
Eddie Lang-Joe Venuti And Their All Star Orchestra•After You’ve Gone / Farewell Blues•Decca•1931','\
Isham Jones Orchestra•It Had To Be You / After The Storm•Brunswick•1924','\
Jazz At The Philharmonic•After You\'re Gone•Disc Records•1948','\
Stan Kenton And His Orchestra•After You / Across The Alley From The Alamo•Capitol Records•0','\
Jimmy Ponder•Mean Streets - No Bridges•Muse Records•1987','\
Wayman Tisdale•Power Forward•MoJazz•1995','\
Joy Layne•You Gave Me Wings To Fly / After School•Mercury•1957','\
Anthony Davis (2)•I\'ve Known Rivers•Gramavision•1982','\
Jennie Smith•Jennie•Dot Records•1964','\
Mari Nakamoto•Unforgettable!•Three Blind Mice•1973','\
John Coltrane•The Mastery Of John Coltrane / Vol. II To The Beat Of A Different Drum•ABC Impulse!•1978','\
Vince Jones•One Day Spent•EMI•1990','\
The Tony Scott Quartet•Tony Scott In Hi-Fi•Brunswick•1955','\
no artist•My Way•DIW•1990'),'\
\
After You\'ve Gone\
':('\
Eddie Lang-Joe Venuti And Their All Star Orchestra•After You’ve Gone / Farewell Blues•Decca•1931','\
Jazz At The Philharmonic•After You\'re Gone•Disc Records•1948','\
Stéphane Grappelli•Live In San Francisco•Storyville•1998','\
Adrian Rollini And His Orchestra•Battle Of Jazz Volume 3•Brunswick•1953','\
Bill Holman•In A Jazz Orbit•Andex•1958','\
Noriko Miyamoto•Flashdance - Best Of Noriko•Casablanca•1983','\
Guy Lombardo And His Royal Canadians•Lombardoland - A Collection Of Guy Lombardo’s Favorites•DECCA•0','\
Cal Tjader•Vibist•Quality Records Limited•1954','\
The Dice Of Dixie Crew •1st Throw•in-akustik•0','\
Sol Yaged•It Might As Well Be Swing•Pine Hill Records•2018','\
Various•Trombone•Verve Records•1991','\
Kazuo Yashiro•Side By Side Vol.3. Kazuo Yashiro Plays Bosendorfer & Steinway ‎•Audio Lab. Record•0','\
Art Tatum Trio•The Complete Trio Sessions With Tiny Grimes & Slam Stewart Vol. 1•Official (3)•1988','\
The Chris Barber Jazz And Blues Band•Stardust•Timeless Records (3)•1988'),'\
\
Afternoon In Paris\
':('\
Kenny Baker And His Band•Round About Midnight / Afternoon In Paris•Parlophone•1953','\
J.J. Johnson•Afternoon In Paris•Sonet•0','\
John Lewis (2)•Midnight In Paris•Emarcy•1989','\
Andrew Hill•Verona Rag•Soul Note•1987','\
Curtis Fuller•Curtis Fuller Meets Roma Jazz Trio•Timeless Records (3)•1987','\
Xanadu•Xanadu At Montreux Volume One•Xanadu Records•1979','\
Scott Hamilton•I Could Write A Book •Fonè•2013','\
Steve Grossman•Katonah•DIW•1986','\
Benny Golson And The Philadelphians•Benny Golson & The Philadelphians•United Artists Records•1959','\
Kenny Burrell•Jazzmen: Detroit•Savoy Records•1956','\
Milt Jackson•Bags\' Opus•United Artists Records•1959','\
The Master Trio•Blues In The Closet•Baybridge Records•1984','\
John Lewis (2)•Duo•Eastworld•1981','\
Horace Parlan Quintet•Glad I Found You•SteepleChase•1984'),'\
\
Again\
':('\
Cuong Vu•Come Play With Me•Knitting Factory Records•2001','\
Tommy Wills•Sweet Soul•Juke•0','\
Nat King Cole•I\'ll Never Say "Never Again" Again / A Little Bit Independent•Capitol Records•1950','\
Giuseppe Emmanuele Quintet•A Waltz For Debby•Splasc(h) Records•1990','\
Benny Goodman And His Orchestra•What A Little Moonlight Can Do / I\'ll Never Say "Never Again" Again•Columbia•1953','\
Judith Durham•Again And Again / Memories•Columbia•1967','\
Kiki Ebsen•接吻～Kiss Me Again•InsideOut•1993','\
Oliver Lake•Again And Again•Gramavision•1991','\
Chick Corea•Again And Again (The Joburg Sessions)•Elektra Musician•1983','\
Dave Koz•Together Again•Capitol Records•1999','\
Jackie McLean•New Wine In Old Bottles•East Wind•1978','\
Isham Jones Orchestra•Never Again / Unfortunate Blues•Brunswick•1924','\
Woody Herman And His Orchestra•Skinned / Skinned Again•Capitol Records•0','\
Duke Ellington•Blues / Plucked Again•Columbia•1939','\
no artist•However•MPS Records•1978'),'\
\
Agua De Beber\
':('\
Astrud Gilberto•Agua De Beber / And Roses And Roses•Verve Records•1965','\
Erik Escobar•New Samba Jazz•Altrisuoni•2006','\
Various•Heirs To Jobim: A Musical Tribute•BMG Victor Inc.•1995','\
Messias (4)•O Melhor De Antonio Carlos Jobim•RCA Victor•1968','\
Ana Caram•Sunflower Time•Mercury•1996','\
Made In Brasil (2)•Numero Um (Number One)•Nucleus Records (2)•0','\
Tania Maria•Intimidade•Blue Note•2005','\
Gabriela Anders•Bossa Beleza•Victor•2008','\
Antonio Carlos Jobim•I Concerti Live @ Rtsi - 18 Ottobre 1978•RTSI•2002'),'\
\
Ain\'t Misbehavin\'\
':('\
Coleman Hawkins Quartet•Cheek To Cheek•Jazztone (2)•1956','\
Bob James•Espresso•Evosound•2018','\
Various•Le 18 Gemme Del Jazz•Giants Of Jazz•1991','\
Various•Yes Sir That\'s My Baby (The Golden Years Of Tin Pan Alley 1920-1929)•New World Records•1977','\
Various•Une Histoire Des Maitres Du Jazz / A Story Of Jazz Masters•CBS•1975','\
Various•Great Jazz Pianists•RCA Camden•1956','\
Lou Stein•Honky Tonk Piano And A "Hot Band"•Mercury•1960','\
Ben Light And His Lightning Fingers•Spotlight On Ben Light•Vik•0','\
Dizzy Gillespie•Dizzy In Paris / 1952-1953•Barclay•1980','\
Marty Grosz Quartet•Just For Fun!•Nagel Heyer Records•1997','\
Fats Waller•The Best Of Fats Waller•Joker (2)•1971'),'\
\
Ain\'t No Sunshine\
':('\
Patricia Kaas•Café Noir•Columbia•1996','\
José James•Lean On Me•Blue Note•2018','\
Various•Chips & Cheers (Blue Note Mix Tape Vol. 1) •Blue Note•2000','\
Jacqui Naylor•You Don´t Know Jacq•Wavemusic•2009','\
Georgie Fame•The Whole World’s Shaking (Complete Recordings 1963-1966)•Polydor•2015','\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014'),'\
\
Ain\'t That Peculiar\
':('\
George Benson•Summertime•CBS•1977'),'\
\
Airegin\
':('\
The Miles Davis Quintet•Airegin / Oleo•Metronome•1959','\
The Wes Montgomery Quartet•Airegin•Riverside Records•1960','\
Tubby Hayes•Jazz Of Modern Times 4. Folge•Fontana•1962','\
Miles Davis•Miles Davis With Sonny Rollins•Prestige•1954','\
Tete Montoliu Trio•Secret Love•Timeless Records (3)•1978','\
Manhattan Jazz Quintet•Manhattan Jazz Quintet•Paddle Wheel•1984','\
Chet Baker•In Concert•India Navigation•1982','\
Phil Woods•Bird Feathers•Prestige•1957','\
Hubert Laws•Then There Was Light (Volume 1)•CTI Records•1976','\
Bernt Rosengren Quartet•Surprise Party•SteepleChase•1983','\
Hubert Laws•Then There Was Light (Volume 1)•CTI Records•1976','\
Stan Getz•Line For Lyons•Sonet•1983','\
Dexter Gordon•Ca\' Purange•Prestige•1973','\
Tubby Hayes•Tubbs In N.Y.•Fontana•1962'),'\
\
Airmail Special\
':('\
Lionel Hampton And His Orchestra•Midnight Sun / Airmail Special•Clef Records•1955','\
Buddy Rich•Transition•Groove Merchant•1974','\
Ella Fitzgerald•At The Hollywood Bowl•Verve Records•0','\
Tiny Grimes•Callin\' The Blues•Prestige•1958','\
Gene Krupa•Gene Krupa - Lionel Hampton - Teddy Wilson•Verve Records•0','\
Gene Krupa•Playing Some Of The Selections They Played In The Benny Goodman Movie•Clef Records•1956','\
The Buddy Tate Celebrity Club Orchestra•Unbroken•MPS Records•1970','\
Lionel Hampton•The Best Of Lionel Hampton•Polydor•1975','\
Lionel Hampton All Stars•Air Mail Special•Clef Records•0'),'\
\
Aja\'s Theme\
':('\
Various•The Very Best Of Smooth Jazz•Universal Classics & Jazz•2002'),'\
\
Alfie\
':('\
Burt Bacharach•Alfie / Bond Street•A&M Records•1967','\
Sonny Rollins•Sonny Rollins In Japan•Victor•1973','\
Rumer•Sings Bacharach At Christmas•Atlantic•2010','\
no artist•Coco d\'Or 3•Sonic Groove (2)•2011','\
Billy Vaughn•Somewhere My Love / Alfie•Dot Records•1966','\
Machito And His Orchestra•Baby I Love You / Alfie•RCA Victor•1967','\
Eddie Higgins•Alfie / You Don\'t Have To Say You Love Me•Atlantic•1966','\
Hiroshi Suzuki Masahiko Togashi Quintet•Variation•Takt Jazz Series•1969','\
Georges-Edouard Nouel•Chodo•Le Chant Du Monde•1975','\
Alison Moyet•Almost Blue / Alfie•Sanctuary Records•2004','\
no artist•Extra! Volume II•Project 3 Total Sound•1974','\
Art Farmer•The Summer Knows•East Wind•1977','\
Bill Evans•Montreux II•CTI Records•1970'),'\
\
Alfie\'s Theme\
':('\
Katsunori Ishida•Body Talk•JVC•1977','\
Santo & Johnny•Famosi Temi Da Films•Produttori Associati•1972','\
Frank Chacksfield & His Orchestra•Foreign Film Festival•London Records•1967','\
Enoch Light And The Light Brigade•Film On Film • Great Movie Themes•Project 3 Total Sound•1966','\
Hugo Montenegro•Scenes & Themes•RCA•1973','\
Johnny Hammond•Soul Flowers•Prestige•1968','\
The Starlight Woodwinds•The Love Album•Columbia•0','\
Sarah Vaughan•Embraceable You•LaserLight Digital•1996','\
Eric Robertson•Born Free•Arc Records (4)•0','\
Chuck Kirkland•Yesterday And Today•Diplomat Records•0','\
Eddie Miller (2)•With A Little Help From My Friend•Coral•0','\
Charlie Byrd•The Look Of Love•Harmony (4)•1970'),'\
\
Alice In Wonderland\
':('\
The Dave Brubeck Quartet•Dave Digs Disney•Fontana•1957','\
Artie Butler•Feelin\' Alright / Alice In Wonderland•Verve Records•1971','\
The Dave Brubeck Quartet•All The Things You Are / Alice In Wonderland•Fantasy•0','\
John Abercrombie•Current Events•ECM Records•1986','\
Putte Wickman•Wickman In Wonderland•EMI•1988','\
The Bill Evans Trio•Sunday At The Village Vanguard•Riverside Records•1961'),'\
\
All About Ronnie\
':('\
Stan Kenton And His Orchestra•Baia / All About Ronnie•Capitol Records•1953','\
Chris Connor•Lullaby of Birdland / All About Ronnie•Bethlehem Records•1954','\
Chris Connor•Sings Lullabys Of Birdland•Bethlehem Records•1954','\
Stan Kenton•Kenton With Voices•Capitol Records•1957','\
Various•Atlantic Jazz•Best Of The \'50s•Rhino Records (2)•1993','\
Stan Kenton•Some Women I\'ve Known•Creative World•0','\
Chris Connor•Chris In Person•Atlantic•1959','\
Chris Connor•Chris•Bethlehem Records•1956','\
Ruth Cameron•Roadhouse•Emarcy•2000','\
Charles Lloyd•Hagar\'s Song•ECM Records•2013','\
Ran Blake•Breakthru•Improvising Artists Inc.•1976','\
Miles Davis•At Newport 1955-1975 (The Bootleg Series Vol. 4)•Columbia•2015'),'\
\
All Alone\
':('\
Mal Waldron Quintet•Live At The Village Vanguard•Pioneer Electronic Corporation•1985','\
Lee Morse•All Alone / Lee\'s Lullaby•Perfect (3)•1925','\
Mal Waldron•Left Alone \'86•Pioneer (3)•1986','\
Tremaine Brothers•All Alone/ Blue Eyed Sally•Gennett•1925','\
Mal Waldron•Left Alone \'86•Paddle Wheel•1987','\
Les Elgart•Recado Bossa Nova / All Alone Am I•Columbia•1962','\
Jimmy Dorsey And His Orchestra•Blue Champagne / All Alone And Lonely•Decca•1941','\
Mal Waldron•Meditations•Victor•1972','\
The Mills Brothers•I Don\'t Mind Being All Alone (When I\'m All Alone With You) / (I Get A) Funny Feelin\'•Decca•1950','\
Cliff Edwards•All Alone / It\'s All The Same To Me•Perfect (3)•1925','\
Yusef Lateef•Other Sounds•New Jazz•1959','\
Gloria De Haven•Who\'s Sorry Now? /  All Alone Monday•MGM Records•1958','\
Jimmy Sacca•Alone / You\'re All That I Need•Dot Records•0','\
Gloria Lynne•Watermelon Man / All Alone•Fontana•1965','\
Illinois Jacquet And His Orchestra•Jivin\' With Jack The Bellboy / You Left Me All Alone•Aladdin (6)•1947','\
The Boswell Sisters•Trav\'lin\' All Alone / St. Louis Blues•Brunswick•1935'),'\
\
All Blues\
':('\
Jimmy Ponder•Ponder\'n•51 West•1981','\
Clarke-Boland Big Band•Two Originals: All Blues/Sax No End•MPS Records•1994','\
Herbie Mann•All Blues / Forest Rain•Herbie Mann Music•1981','\
g.org•A New Kind Of Blue•A Nest Of Eggs•2004','\
Jim Hall•Youkali•CTI Records•1992','\
Jam Session N• 2•Jammin\' The Blues / All Together•Swing (3)•1947','\
Peter Erskine•From Kenton To Now•Fuzzy Music•1995','\
Roy Ayers Quartet•All Blues•Columbia•1969','\
New York Jazz Quartet•Blues For Sarka•Enja Records•1978','\
Russell Gunn•Plays Miles•HighNote Records Inc.•2007','\
The Tubby Hayes Quintet•A Tribute - Tubbs•Spotlite Records•1981','\
Lee Konitz•Creative Music Studio - Woodstock Jazz Festival 2•Douglas Music•1997','\
Eric Kloss•All Blues•Prestige•1966','\
Chet Baker•Studio Trieste•CTI Records•1982','\
Count Basie Orchestra•All Of Me / Rusty Dusty Blues•Columbia•1943','\
Miles Davis•All Blues / It Ain\'t Necessarily So•Columbia•1961','\
The Miles Davis Quintet•Live In Milan 1964•RLR Records•2007','\
Jimmy McGriff•All About My Girl / M.G. Blues•Sue Records Inc.•1962'),'\
\
All God\'s Chillun Got Rhythm\
':('\
Joe Williams•The Overwhelming Joe Williams•Bluebird (3)•1988','\
Various•Hollywood Swing & Jazz: Hot Numbers From Classic M-G-M Warner Bros. & RKO Films•Sony Classical•2000'),'\
\
All In Love Is Fair\
':('\
Cleo Laine•All In Love Is Fair / Skip-A-Long Sam•RCA•1974','\
Hank Crawford•Don\'t You Worry \'Bout A Thing•Kudu•1974','\
Yoshio Otomo Quartet•As A Child•Seven Seas•1978','\
The SOS All-Stars (2)•New York Rendezvous•Chase Music Group•1987','\
Tsuyoshi Yamamoto Trio•Blues To East•Philips•1978','\
The Great Jazz Trio•Chapter II•East Wind•1980','\
Brother Jack McDuff•The Fourth Dimension•Cadet•1974','\
Kimiko Itoh•For Lovers Only•Columbia•1987','\
Bubbha Thomas & The Lightmen Plus One•Country Fried Chicken•no label•1975','\
Houston Person•Houston Person \'75•20th Century Records•1975','\
Slide Hampton And The World Of Trombones•Spirit Of The Horn•MCG Jazz•2002','\
Michel Graillier•Fairly•Quantum (3)•1992','\
Cal Tjader•Heat Wave•Concord Jazz•1982','\
Morgana King•Stretchin\' Out•Muse Records•1978'),'\
\
All My Tomorrows\
':('\
The Four Coins•Cherry Lips / All My Tomorrows•Epic•1956','\
Frank Sinatra•High Hopes / All My Tomorrows•Capitol Records•1959','\
Frank Sinatra•High Hopes•Capitol Records•1959','\
Kirsti Ola & Erik•Rags & Silks•Name Music•2015','\
Julie Kelly•We\'re On Our Way•Pausa Records•1984','\
David Friesen•Other Mansions•Inner City Records•1980','\
The Concord All Stars•Concord All-Stars On Cape Cod•Concord Jazz•1992','\
Frank Sinatra•All The Way•Capitol Records•1961','\
Grant Geissman•All My Tomorrows•TBA Records•1988','\
Scott Hamilton•Midnight At Nola\'s Penthouse•Arbors Records•2010'),'\
\
All Of Me\
':('\
Ella Fitzgerald•Sings The Cole Porter Song Book•Artone•0','\
The Main (2)•All Of Me•Satellite Records (7)•1987','\
Illinois Jacquet And His Orchestra•Pastel / All Of Me•Mercury•1951','\
Tony Crombie And His Orchestra•All Of Me / Perdido•London Records•1954','\
Billy May And His Orchestra•Lean Baby / All Of Me•Capitol Records•1951','\
Benny Carter And His Orchestra•The Very Thought Of You / All Of Me•Bluebird (3)•1940','\
Count Basie Orchestra•All Of Me / Rusty Dusty Blues•Columbia•1943','\
Louis Armstrong And His Orchestra•All Of Me / New Tiger Rag•Odeon•0','\
Erroll Garner•All Of Me / I Don\'t Stand A Ghost Of A Chance•Savoy Records•1949','\
Count Basie•On The Road To Mandalay•Verve Records•1963','\
Lars Gullin•Baritone Sax•Atlantic•1956','\
Dinah Washington•Make Me A Present Of You / All Of Me•Mercury•1959','\
Louis Armstrong And His Orchestra•Blueberry Hill•Philips•1957','\
Thomas Pelzer Limited•TPL (Thomas Pelzer Limited)•Vogel•1974','\
The Gus Merzi Quintette•Cocktail Melodies (volume 2)•Manhattan (14)•0','\
The Charlie Shavers Quartet•Here Comes Charlie•Everest•1960','\
The Page Cavanaugh Trio•The Three Bears / All Of Me•RCA Victor•1946','\
Teddy Wilson•Cheek To Cheek•MGM Records•1958','\
Mildred Bailey•Mildred Bailey Sings•Royale•1951'),'\
\
All Of You\
':('\
Ella Fitzgerald•Sings The Cole Porter Song Book•Artone•0','\
Richie Beirach Trio•Summer Night•Venus Records (5)•2008','\
Miles Davis•My Funny Valentine - Miles Davis In Concert•Columbia•1965','\
Ahmad Jamal•All Of You / You\'re Blase•Argo (6)•1962','\
Miles Davis•\'Round About Midnight•Columbia•1957','\
Benny Carter And His Orchestra•The Very Thought Of You / All Of Me•Bluebird (3)•1940','\
The Miles Davis Quintet•Live In Milan 1964•RLR Records•2007','\
The Miles Davis Quintet•New York City Philharmonic Hall At Lincoln Center February 12 1964•Giants Of Jazz•1998','\
Louis Armstrong And His Orchestra•Papa Dip•Philips•0'),'\
\
All Or Nothing At All\
':('\
Al Jarreau•All Or Nothing At All•WEA•1988','\
Frank Sinatra•All Or Nothing At All / Ciribiribin•Columbia•0','\
Harry James And His Orchestra•All Or Nothing At All•Columbia•1940','\
Bob Cooper•Shifting Winds No. 3•Capitol Records•1955','\
Ric Marlow•A Taste Of Honey•Marc Records (2)•1962','\
Thomas Pelzer Limited•TPL (Thomas Pelzer Limited)•Vogel•1974','\
Freddie Hubbard•Open Sesame•Blue Note•1960','\
John Coltrane•Impressions•Impulse!•0','\
Dupree (4)•Nuestro Camino•Public Hi-Fi•2013','\
Freddie Hubbard•Jazz Profile: Freddie Hubbard•Blue Note•1997','\
Pharoah Sanders•Moon Child•Timeless Records (3)•1990','\
Hendrika Entzian Quartet•Turnus•Traumton Records•2014'),'\
\
All The Things You Are\
':('\
Tommy Dorsey And His Orchestra•All The Things You Are •Victor•1939','\
Clifford Brown Sextet•Conception E.P.•Vogue•1955','\
Johnny Griffin/Art Taylor Quartet•The Jamfs Are Coming!•Timeless Records (3)•1978','\
Bob Cooper•The Travelling Mr. Bob Cooper•no label•0','\
Artie Shaw And His Orchestra•All In Fun / All The Things You Are•Bluebird (3)•1939','\
The Zoot Sims Quintet•All The Things You Are / Tickle Toe•Gazell•0','\
David Rose & His Orchestra•Vanessa•MGM Records Division•1952','\
Dizzy Gillespie•Jazz At Massey Hall Volume 2•Debut Records (3)•0','\
The Oscar Pettiford Quartet•All The Things You Are / Vienna Blues•Bertelsmann Schallplattenring•1959','\
The Milt Jackson Quartet•All The Things You Are / La Ronde•Metronome•1953','\
Charlie Barnet And His Orchestra•All The Things You Are / Ill Wind•Capitol Records•0','\
Theo Schumann Combo•Erikson / Belgier / All The Things You Are / Karawane•AMIGA•1964','\
Lee Konitz•Sax Of A Kind - Lee Konitz In Sweden 1951/53•Dragon (8)•1979','\
Clark Dennis•Tenderly / All The Things You Are•Capitol Records•1950','\
Theo Schumann Combo•Erikson / Belgier / All The Things You Are / Karawane•AMIGA•1964','\
The Dave Brubeck Quartet•Dave Brubeck Concert•Brunswick•1956','\
The Dave Brubeck Quartet•All The Things You Are / Alice In Wonderland•Fantasy•0','\
Erroll Garner•Lady Be Good / All The Things You Are•Disc Records•1946','\
Paul Weston And His Orchestra•All The Things You Are / East Of The Sun•Capitol Records•0','\
Johnny Griffin•Live In Tokyo•Philips•1976','\
Ella Fitzgerald•Why Was I Born? •Verve Records•1964','\
George Benson•Oleo•Music Mirror•1993','\
Various•Jazz At The Philharmonic In Europe•Verve Records•1963','\
Frank Sinatra•All The Things You Are / Over The Rainbow•Columbia•1948'),'\
\
All The Way\
':('\
Frank Sinatra•High Hopes / All The Way•Capitol Records•0','\
Frank Sinatra•High Hopes / All The Way•Capitol Records•0','\
Frank Sinatra•Mr. Success•Capitol Records•0','\
Ramsey Lewis•All The Way Live•Columbia•1978','\
Frank Sinatra•All The Way•Capitol Records•1957','\
Sarah Vaughan•Just A Moment More / I Ran All The Way Home•Columbia•1951','\
Oliver Nelson•Taking Care Of Business•New Jazz•1960','\
Buddy Greco•I Ran All The Way Home•Coral•1951','\
Dean Martin•Solitaire / I Ran All The Way Home•Capitol Records•1951','\
Robert Farnon And His Orchestra•Robert Farnon And His Orchestra Play The Hits Of Sinatra•Fontana•1965','\
Connie Crothers•Perception•SteepleChase Records•1975'),'\
\
All Through The Night\
':('\
The Tal Farlow Quartet•Tal Farlow Quartet•Blue Note•1954','\
Percy Faith & His Orchestra•All Through The Night•Royale•0','\
101 Strings•In The Quiet Hours•Alshire•0','\
Julian Lage•Sounding Point•EmArcy•2009','\
The Scott Hamilton Quintet•The Right Time•Concord Jazz•1987','\
Tal Farlow•Early Tal•Blue Note•1983','\
Jimmy Knepper Quintet•Dream Dancing•Criss Cross Jazz•1986','\
The Phil Woods Quartet•At The Vanguard•Antilles•1983','\
Ella Fitzgerald•Ella Fitzgerald Sings The Cole Porter Song Book•Verve Records•1956','\
Percy Faith & His Orchestra•All Time Popular Dance Hits•Royale•1954','\
Deborah Henson-Conant•On The Rise•GRP•1989','\
André Kostelanetz And His Orchestra•Music Of Cole Porter•Columbia•0','\
The Johnny Griffin Quartet•Dance Of Passion•Antilles•1993','\
The Percy Faith Strings•Exotic Strings•Columbia•1962','\
Johnny Griffin•Woe Is Me•Movieplay•1993','\
The Dave Brubeck Quartet•Anything Goes! The Dave Brubeck Quartet Plays Cole Porter•Columbia•1967','\
Roswell Rudd•Roswell Rudd\'s MALIcool•Sunnyside•2002','\
Bobby Hackett•In A Mellow Mood•Capitol Records•1955','\
Stéphane Grappelli•Anything Goes•CBS•1989','\
Earl Klugh•The Journey•Warner Bros. Records•1997'),'\
\
Almost Like Being In Love\
':('\
The Pia Beck Trio•C\'est Mon Gigolo / Almost Like Being In Love•Philips•1954','\
J.J. Johnson•Misterioso - "Poll Winners Jazz"•Fontana•1960','\
Lester Young Quintet•There\'ll Never Be Another You / Almost Like Being In Love•Mercury•1953','\
Charlie Parker And His Orchestra•Almost Like Being In Love / What Is This Thing Called Love•Clef Records•0','\
Sonny Rollins•Sonny Rollins With Modern Jazz Quartet•Prestige•1954','\
Mary Martin•Come To The Mardi Gras / Almost Like Being In Love•Decca•1947','\
Lee Konitz•Lee Konitz Plays With The Gerry Mulligan Quartet•Pacific Jazz•1954','\
Chet Baker•Time After Time•IRD Records (2)•1989','\
Nat King Cole•Nat King Cole Sings For Two In Love Part 1•Capitol Records•0','\
Maynard Ferguson•Trumpet Rhapsody•MPS Records•1968','\
Nicole Croisille•Dieu merci il m’aime aussi•Fontana•1961','\
Lester Young•Lester Young With The Oscar Peterson Trio #1•Norgran Records•1954','\
Brad Mehldau Trio•Seymour Reads The Constitution!•Nonesuch•2018','\
Hank Jones•Quartet-Quintet•Savoy Records•1956','\
Buddy Banks (2)•Jazz De Chambre•Le Club Français Du Disque•0','\
Greetje Kauffeld•Young Girl Sunday Jazz•Sonorama•2015','\
Eydie Gormé•Blame It On The Bossa Nova•CBS•1963'),'\
\
Along Came Betty\
':('\
Art Blakey & The Jazz Messengers•Blues March / Along Came Betty•Blue Note•1958','\
Archie Shepp•Montreux Two•Arista•1976','\
Art Blakey & The Jazz Messengers•Drums Ablaze•Alto Records•0','\
The Phil Woods Quartet•Live Volume One•Clean Cuts•1980','\
Quincy Jones•If I Ever Lose This Heaven / Along Came Betty•A&M Records•1974','\
Siegfried Kessler Trio•Invitation•Impro•1979','\
The Jazztet•The Jazztet - Real Time•Contemporary Records•1988','\
Art Blakey & The Jazz Messengers•Live In Moers 1976•Jazzline•2016','\
Art Blakey & The Jazz Messengers•Live in Holland 1958•Bandstand•1991','\
Rufus Reid Trio•Seven Minds•Sunnyside•1985','\
Benny Golson•Are You Real•CBS/Sony•1977','\
Archie Shepp•Montreux•Freedom•1988','\
Benny Golson Quartet•Live•Dreyfus Jazz•1991','\
Art Blakey & The Jazz Messengers•Buhaina•Prestige•1973','\
The Jazztet•Moment To Moment•Soul Note•1983','\
Paul Robertson (14)•Old Friends New Friends•Palo Alto Records•1982'),'\
\
Alone Together\
':('\
Lee Konitz•Duets•Milestone (4)•1968','\
Lloyd Mayers•Desafinado / Alone Together•United Artists Records•1962','\
Pete Fountain•Alone Together / Forbidden Love•Coral•0','\
Artie Shaw And His Orchestra•Alone Together / Rose Room•Bluebird (3)•1939','\
Miles Davis•Blue Moods Vol. 1•Debut Records (3)•0','\
Terumasa Hino•Alone Together•Takt Jazz Series•1970','\
Buck Hill Quartet•Impressions•SteepleChase•1983','\
Terumasa Hino•Alone Together•Takt Jazz Series•1970','\
Eric Dolphy•Conversations•FM (6)•1963','\
Eric Dolphy•Conversations•Celluloid•1999'),'\
\
Altoitis\
':('\
Oliver Nelson•Images•Prestige•1976'),'\
\
Always There\
':('\
Willie Bobo•Always There•Columbia•1978','\
Percy Faith And His Orchestra And Chorus•Always Always / There She Goes•Columbia•0','\
Billy May And His Orchestra•There Is No Greater Love / Always•Capitol Records•1952','\
Billy May And His Orchestra•There Is No Greater Love / Always•Capitol Records•0','\
Ralph Flanagan And His Orchestra•Rag Mop / You\'re Always There•RCA Victor•1950','\
Ray Noble And His Orchestra•You\'re Always There / Melissa•Columbia•1949','\
Ronnie Laws•Always There•Blue Note•1976','\
Ronnie Laws•Always There•Blue Note•1976','\
Side Effect•Always There•Fantasy•1976','\
Ronnie Laws•Always There•United Artists Records•1978','\
Ronnie Laws•There\'s A Way•Liberty•1981','\
Yosaku•The Bottle•BSTRD Boots•2010','\
Peter Kater•Two Hearts•PDK Music•1986','\
Mal Waldron Trio•Set Me Free•Affinity•1984','\
The Toon Roos Quartet•Attitudes•Timeless Records (3)•1988'),'\
\
Am I Blue?\
':('\
Al Hall Quintet•Am I Blue / Emaline•Wax (12)•1946','\
Buddy Johnson And His Orchestra•Am I Blue / My Reverie•Decca•1951','\
Billie Holiday And Her Orchestra•Long Gone Blues / Am I Blue•Columbia•1947','\
Dinah Washington•Am I Blue / I Want To Be Loved•Mercury•1962','\
Elaine Delmar•A Swinging Chick•Columbia•1961','\
Harry Bluestone•Am I Blue / Kiddin\' On The Strings•Decca•1938','\
Ethel Waters•Birmingham Bertha / Am I Blue?•Columbia•1929','\
Noro Morales & His Orchestra•Istanbul / Am I Blue?•RCA Victor•1954','\
Erroll Garner•Am I Blue? / I Never Knew (I Could Love Anybody Like I\'m Loving You)•Columbia•1952','\
Neva Raphaello•With The Dutch Swing College Band•Philips•1958','\
Libby Holman•Am I Blue? / Moanin\' Low•Brunswick•1929','\
Fire! Orchestra•Arrival•Rune Grammofon•2019','\
Claudine Longet•Am I Blue / A Flea In Her Ear•A&M Records•1968','\
Clyde McCoy•Blue Prelude•Mercury•1962'),'\
\
American Gothic\
':('\
Bob Berg•Back Roads•Denon•1991','\
Maher Shalal Hash Baz•From A Summer To Another Summer (An Egypt To Another Egypt)•Geographic•2000'),'\
\
Ana Maria\
':('\
MVP (5)•Truth In Shredding•Tone Center•1990','\
Frank Morgan•Lament•Contemporary Records•1986','\
Act Big Band•Act Big Band And Guests - Extremes•Amplitude (2)•1988','\
Toolbox•Toolbox•Vital Records (11)•1992','\
Kirk Lightsey•Shorter By Two - The Music Of Wayne Shorter Played On Two Pianos•Sunnyside•1989','\
Kenny Kirkland•Kenny Kirkland•GRP•1991','\
Wayne Shorter•Native Dancer•Columbia•1975'),'\
\
And It All Goes Round\
':('\
Bernard Ighner•Little Dreamer•Alfa•1978','\
Kimiko Kasai•Round And Round•CBS/Sony•1978','\
Jon Lucien•Premonition•Columbia•1976','\
Andrea Pozza Trio•Drop This Thing•Dejavu•2008','\
Nicolas Bearde•Crossing The Line•Expansion•1998','\
Mike Campbell (2)•Secret Fantasy•Palo Alto Records•1982','\
Connie Boswell•Sand In My Shoes•MCA Records•1982','\
Boom Boom Satellites•19972007•gr8! records•2010','\
Hal Kemp And His Orchestra•Remember Me?•Jasmine Records•2001','\
Louis Prima•Capitol Collectors Series•Capitol Records•0','\
Various•The Great Band Era (1936-1945)•no label•1964','\
Count Basie Orchestra•Good Morning Blues•MCA Records•1977'),'\
\
And Now the Queen\
':('\
Paul Bley Quintet•Barrage•ESP Disk•1965','\
Paul Bley•Alone Again•Improvising Artists Inc.•1975','\
Paul Bley Trio•Closer•ESP Disk•1966','\
Paul Bley•Homage To Carla•Owl Records (4)•1993','\
The Carla Bley Band•European Tour 1977•WATT Works•1978','\
Joe McPhee•Creole Gardens (A New Orleans Suite)•NoBusiness Records•2011','\
The Nels Cline Singers•Initiate•Cryptogramophone•2010','\
S. Mos•Hip Hop And Jazz Mixed Up Volume 2•Musicast•2011','\
Paul Bley•Solo Piano•SteepleChase•1988','\
Various•Miss Juvena Presents 12 Teen Hits•CBS Special Products•1974','\
Molly Camp•Molly Camp Sings...•RCA Victor•0','\
The Grateful Dead•Dick\'s Picks Volume Nine 9/16/90•Grateful Dead Records•1997','\
Enoch Light And The Light Brigade•Big Hits Of The Seventies (Vol.3)•Project 3 Total Sound•1977'),'\
\
And On the Third Day\
':('\
Cuong Vu 4-tet•Ballet - The Music Of Michael Gibbs•RareNoise Records•2017','\
Richard Souther•Heirborne•Meadowlark Records•1985','\
Michael Gibbs•Michael Gibbs•Deram•1970','\
Gary Burton Quartet•Country Roads & Other Places•RCA Victor•1969','\
Gary Burton•Artist\'s Choice•Bluebird (3)•1987','\
The Three Suns•Let\'s Dance With The Three Suns•RCA Victor•1958','\
Guy Lombardo And His Royal Canadians•The Best Of•no label•1975','\
Various•Golden Guitar Magic•no label•1969','\
Various•Golden Guitar Magic•no label•1969','\
Duke Ellington•The Reprise Studio Recordings•Mosaic Records (2)•1999','\
George Gershwin•The Essential George Gershwin•Sony Classical•2003','\
Count Basie Orchestra•The Complete Roulette Studio Recordings Of Count Basie And His Orchestra•Mosaic Records (2)•1993','\
Arthur Fiedler•Pops Varieties•no label•1969','\
Guy Lombardo And His Royal Canadians•The Sweetest Music This Side Of Heaven•Longines Symphonette Society•0'),'\
\
And The Angels Sing\
':('\
Ziggy Elman & His Orchestra•Bublitchki / And The Angels Sing•Bluebird (3)•1939','\
Ziggy Elman & His Orchestra•Bublitchki / And The Angels Sing•RCA Victor•0','\
Benny Goodman And His Orchestra•The Benny Goodman Story Part 3•Decca•1956','\
Benny Goodman And His Orchestra•Bumble Bee Stomp / And The Angels Sing•RCA Victor•0','\
Ziggy Elman & His Orchestra•1947•Circle•1984','\
The Benny Goodman Quartet•The Benny Goodman Story Volume 2 Part 2•Brunswick•1956','\
Johnny Nash•Baby Baby Baby•ABC-Paramount•1959','\
Benny Goodman And His Orchestra•And The Angels Sing / Rose Of Washington Square•Disque Gramophone•1939','\
Count Basie Orchestra•And The Angels Sing / If I Didn\'t Care •Vocalion (2)•0','\
Ziggy Elman & His Orchestra•And The Angels Sing / Three Little Words•MGM Records•1948','\
Ella Fitzgerald•A Hard Day\'s Night/And The Angels Sing•Verve Records•1965','\
Herb Alpert & The Tijuana Brass•Spanish Flea!•Festival Records•1966','\
The Modernaires•The Benny Goodman Story•Coral•0','\
Ella Fitzgerald•A Hard Day\'s Night/And The Angels Sing•Verve Records•1965','\
Benny Goodman And His Orchestra•And The Angels Sing / Sent For You Yesterday And Here You Come Today•Victor•1943','\
Red Prysock•Riffin’ With Red / And The Angels Sing•Mercury•1959','\
Benny Goodman And His Orchestra•And The Angels Sing•RCA Victor•1958','\
Ted Heath•Ted Heath London Palladium Highlights No.2•Decca•1956','\
Benny Goodman•Plays Selections Featured In The Benny Goodman Story Part 2 •Capitol Records•1956','\
The Mills Brothers•And The Angels Sing / South Of The Border•Brunswick•1939','\
The Modernaires•A Tribute To The Benny Goodman •Coral•0'),'\
\
Angel Eyes\
':('\
Gene Ammons•Angel Eyes•Prestige•0','\
Bob Cooper•Cappuccino Time•Music•1956','\
David Newton (3)•Eye Witness•Linn Records•1991','\
The Modern Jazz Quartet•Versailles / Angel Eyes / Willow Weep For Me•Metronome•1956','\
Bill Leslie•Diggin\' The Chicks•Argo (6)•1962','\
The Don Ellis Orchestra•Live In 3⅔/4 Time•Pacific Jazz•1966','\
Art Blakey & The Jazz Messengers•Live! Vol. 1•Trip Jazz•1974','\
The J.J. Johnson Quintet•Jazz Gallery•Philips•0','\
Wynton Marsalis•Wynton Marsalis\' First Recordings•Kingdom Jazz•1983','\
Wynton Marsalis•Wynton•no label•1988','\
The Dave Brubeck Quartet•Angel Eyes•Crown Records (2)•1964'),'\
\
Another Star\
':('\
Carmen McRae•Tonight He\'s Out To Break Another Heart / Star Eyes•Decca•1956','\
Kenji Omura•Guitar Work Shop Vol. 2 Live•Flying Dog•1978','\
Dan Siegel•Another Time Another Place•Pausa Records•1984','\
Abbey Lincoln•Wholly Earth•Verve Records•1998','\
Cedar Walton•The Trio 3•Red Record•1986','\
Alan Broadbent Trio•Another Time•Trend (3)•1987','\
Cedar Walton•Animation•Columbia•1978','\
Herbie Mann•Mellow•Atlantic•1981','\
Asako Toki•Standards On The Sofa•LD&K•2004','\
Gerry Mulligan•Little Big Horn•GRP•1983','\
Susanna And The Magical Orchestra•3•Rune Grammofon•2009'),'\
\
Another Time\
':('\
Matt Bianco•Our Love•Victor•1993','\
Jerry Granelli•Another Place•veraBra Records•1993','\
Barry Altschul•Another Time / Another Place•Muse Records•1978','\
Boney James•Trust•Spindletop Records•1992','\
Carmen Cavallaro•Cocktails With Cavallaro•Coral•1970','\
The Keef Hartley Band•The Time Is Near....•Deram•1970','\
Roy Powell•Rendezvous (Live In London)•Nagel Heyer Records•2007','\
Ralph MacDonald•Universal Rhythm•Polydor•1984','\
Max Roach His Chorus And Orchestra•It\'s Time•Impulse!•1962','\
Amalgam (2)•Another Time•Vinyl Records•1976','\
Bob James•Quartette Humaine•Okeh•2013','\
Tony Guerrero (2)•Another Day Another Dream•Calnova•1991','\
$.99 Dreams•Three Songs For Another Time•Masters Chemical Society•2011','\
Trevor Watts String Ensemble•Cynosure•Ogun•1976','\
Abbey Lincoln•Wholly Earth•Verve Records•1998','\
Carmen Cavallaro•Cocktail Time With Carmen Cavallaro•Brunswick•0'),'\
\
Anthropology\
':('\
Dizzy Gillespie Sextet•Ol\' Man Rebop / Anthropology•no label•1948','\
Clifford Jordan•Cliff Craft•Blue Note•1957','\
Don Byas•Anthropology•Black Lion Records•0','\
James Moody•Feelin\' It Together•Muse Records•1974','\
Don Byas•A Night In Tunisia•Black Lion Records•1989'),'\
\
Anything Goes\
':('\
John Williams (4)•Anything Goes•Polydor•1984','\
Ron Carter•Anything Goes•Kudu•1975','\
Mel Powell•Anything Goes / That Old Black Magic•Capitol Records•1948','\
Jutta Hipp And Her German Jazzmen•Jutta Hipp And Her German Jazzmen•MGM Records•0','\
Tony Bennett•Anything Goes•Polydor•2014','\
Cybill Shepherd•My Heart Belongs To  Daddy•Paramount Records•1974','\
Max Greger Und Sein Orchester•Strict Tempo Dancing•Polydor•0','\
Oscar Peterson•Plays Cole Porter•Clef Records•0','\
Dakota Staton•Dynamic! Part 2•Capitol Records•1958','\
Stan Getz•Getz Meets Mulligan In Hifi Vol. 2•Verve Records•0','\
The Oscar Peterson Trio•Stage Right•VSP•1966','\
André Previn•By Request•RCA Victor•0','\
Ron Carter•Anything Goes•Kudu•1975','\
Pee Wee Hunt•Cole Porter Ala Dixie•Capitol Records•1958'),'\
\
Appointment In Ghana\
':('\
Jackie McLean•Street Singer•Blue Note•1980','\
The Crusaders•At The Lighthouse•Pacific Jazz•1962','\
Jackie McLean•Jackie\'s Bag•Blue Note•1960','\
Various•Afro Blue Vol.2/The Roots And Rhythms Of Jazz•Blue Note•1998','\
Christopher Hollyday•Christopher Hollyday•Novus•1989','\
Jackie McLean•New Wine In Old Bottles•East Wind•1978','\
The Crusaders•The Best Of...•Pacific Jazz•1993','\
Various•Blue Note 50th Anniversary Collection Volume 2 1956-1965 - The Jazz Message•Blue Note•1989','\
Marc Cary•Focus•Motéma•2006'),'\
\
April\
':('\
Peter Kowald•Mirrors - Broken But No Dust•Balance Point Acoustics•2001','\
Kiyoshi Matsutakeya•I\'ll Remember April•P-Vine Records•1996','\
John Tchicai•West Africa Tour (Sierra Leone Liberia & Guinea) April 1985•Sagittarius A-Star•2012','\
Uwe Kropinski•Solo•AMIGA•1985','\
Glenn Miller•This Is Glenn Miller - Vol. II (Instrumentals)•RCA Victor•1950','\
Clifford Brown And Max Roach•Live At The Bee Hive•Columbia•1979','\
Sam Lanin And His Dance Orchestra•April Showers / Wana•Cameo (3)•1922','\
Les Baxter & His Orchestra•April In Portugal / Suddenly•Capitol Records•1953','\
Louis Armstrong And His Orchestra•April In Portugal / Ramona•Decca•0','\
The Art Van Damme Quintet•Carioca•Columbia•1953','\
Richard Hayman And His Orchestra•April In Portugal / Anna•Mercury•1953','\
Count Basie Big Band•April In Paris•Clef Records•1956','\
Wild Bill Davis•Manhattan / April In Paris•Coral•0'),'\
\
April In Paris\
':('\
Wild Bill Davis•Manhattan / April In Paris•Coral•0','\
Count Basie Big Band•April In Paris•Clef Records•1956','\
Sauter-Finegan Orchestra•Doodletown Races / April In Paris•RCA Victor•1955','\
Wild Bill Davis Trio•April In Paris / Lullaby Of Birdland•Epic•1955','\
Sauter-Finegan Orchestra•Doodletown Fifers / April In Paris•no label•1953','\
Ahmad Jamal•April In Paris / Like Someone In Love•Argo (6)•1958','\
Ella Fitzgerald•Ella And Louis Vol. 2•Verve Records•0','\
Count Basie•April In Paris / One O\'Clock Jump•Verve Records•0','\
Sarah Vaughan•The Divine Sarah•EmArcy•1957','\
Artie Shaw And His Orchestra•April In Paris / King For A Day•Victor•1940','\
Josephine Baker•Quatre Chansons De Paris•RCA Victor•1962','\
Charlie Parker With Strings•April In Paris / If I Should Lose You•Blue Star•0'),'\
\
April Joy\
':('\
Pat Metheny Group•Pat Metheny Group•ECM Records•1978','\
David Friedman•Winter Love April Joy•East Wind•1975','\
George Shearing•Masters Of Jazz 2•Capitol Records•1976','\
George Wallington Trio•The George Wallington Trio•Savoy Records•1956','\
César Camargo Mariano•Duo•Trama•2002','\
Out Of Print•Dancing In The Brain•Unit Records (2)•2015','\
Clifford Brown•Clifford Brown•EmArcy•1990','\
Cannonball Adderley•Cannonball Adderley\'s Finest Hour•Verve Records•2001','\
Ferrante & Teicher•Holiday For Pianos•United Artists Records•1963','\
Helen Merrill•Brownie Homage To Clifford Brown•Verve Records•1994'),'\
\
April Skies\
':('\
Mantovani And His Orchestra•Four Continental Favourites•Decca•1959','\
Wardell Gray•Los Angeles All Stars•Prestige•1953','\
Wardell Gray•Memorial Volume 2•Prestige•1955','\
Wardell Gray•The Chase•Giants Of Jazz•1990','\
Benny Goodman And His Orchestra•The ABC Collection•ABC Records•0','\
Charles Magnante And His Orchestra•Carnival In Far Away Places•Command•1967','\
George Wright (2)•Have Organ Will Travel•HiFi Records•1960','\
Andy Williams•Under Paris Skies•Cadence (2)•1960','\
Korla Pandit•Korla Pandit In Paris•Fantasy•1963','\
Bernie Green And His Orchestra•Futura•RCA Victor•1961','\
Bob Florence And His Orchestra•Name Band: 1959•Carlton•1959','\
Wardell Gray•Memorial Album•Prestige•1965','\
Dinah Washington•Dinah Washington Sings Standards - Jazz Masters 40•Verve Records•1994','\
Fausto Papetti•Oggi 4 - Quarantaseiesima Raccolta•CBS•1988'),'\
\
Arise Her Eyes\
':('\
Gary Burton•Seven Songs For Quartet And Chamber Orchestra•ECM Records•1974','\
Gary Burton•Throb•Atlantic•1969','\
Various•Re: Seoul•ECM Records•2013','\
Gary Burton / Chick Corea•Crystal Silence•ECM Records•1973','\
Gary Burton•Alone At Last•Atlantic•1971','\
Gary Burton•Gary Burton & Keith Jarrett / Gary Burton: Throb•Rhino Records (2)•1994'),'\
\
Armageddon\
':('\
Greg Adams (9)•Koolin Out•Hip City Records (2)•1983','\
Wayne Shorter•Night Dreamer•Blue Note•1964','\
Philip Cohran & The Artistic Heritage Ensemble•Armageddon•Katalyst Entertainment•2010','\
Steve Coleman And Five Elements•Rhythm People (The Resurrection Of Creative Black Civilization)•Novus•1990','\
Mother Gong•O Amsterdam•Voiceprint•2007','\
The Three Souls•Soul Sounds•Argo (6)•1965','\
Alice Coltrane•Astral Meditations•Impulse!•1999','\
Hank Jones•Favors•Verve Records•1997'),'\
\
Around Again\
':('\
Sarah Vaughan•Gone Again•Mercury•1957','\
Paul Bley Quintet•Barrage•ESP Disk•1965','\
The Paul Bley Group•Hot•Soul Note•1986','\
Paul Bley•Footloose•Savoy Records•1963','\
Paul Bley•Turns•Savoy Jazz•1987','\
Tony Bennett•The Very Thought Of You•Columbia Special Products•0','\
Masabumi Kikuchi•Poesy : The Man Who Keeps Washing His Hands•Philips•1971','\
Harry Connick Jr.•Connoisseur\'s Edition•Columbia•1991','\
Ray Conniff And His Orchestra & Chorus•Calling All Dancers! Rockin\' Around•Philips•0','\
no artist•Tanz! - Dansez! Hollywood Rhythms•Disco-Club•0','\
Cootie Williams•Around Midnight•Jaro International•1959','\
Bogusław Wyrobek•Twist Around The Clock•Polskie Nagrania Muza•1962','\
George Shearing•It\'s Real George•Coronet Records•1965','\
Paul Bley•Homage To Carla•Owl Records (4)•1993','\
Paul Bley•Syndrome•Savoy Jazz•1986','\
Steve Hobbs•On The Lower East Side•Candid•1993'),'\
\
As Time Goes By\
':('\
Teddy Wilson Trio•As Time Goes By / Whispering•Parlophone•1948','\
Billie Holiday•As Time Goes By / Embraceable You•Commodore•1948','\
Ambrose & His Orchestra•As Time Goes By / Three Dreams•Decca•0','\
Ace Cannon•Wonderland By Night / As Time Goes By•Hi Records•1966','\
Ray Anthony & His Orchestra•As Time Goes By / Scatterbrain•Capitol Records•1952','\
Eric Winstone And His Band•As Time Goes By / Let\'s Get Lost•Regal Zonophone•1943','\
Jacques Renard And His Orchestra•As Time Goes By / I\'m Sorry Dear•Brunswick•1943','\
Julius Wechter•As Time Goes By•A&M Records•1971','\
Rudy Vallee•As Time Goes By / Two In One Blues•Victor•0','\
Lee Richardson (4)•As Time Goes By / That Old Feeling•DeLuxe (2)•1955','\
Bill Snyder•11th Hour Melody•Decca•1956','\
Toni Harper•Never Trust A Stranger•GNP Crescendo•0','\
Jimmy Durante•Make Someone Happy•Warner Bros. Records•1996','\
Tiny Tim•Great Balls Of Fire•Reprise Records•1968','\
Sam Taylor And His Orchestra•Don\'t Take Your Love From Me / As Time Goes By•MGM Records•1955','\
Ray Conniff•Spielt Für Verliebte S\'Wonderful•Philips•0','\
Eric Alexander Quartet•My Favorite Things•Venus Records (5)•2007','\
Bryan Ferry•As Time Goes By•Virgin•1999'),'\
\
As We Speak\
':('\
Vic Lewis West Coast All-Stars•Plays Bill Holman•Candid•1993','\
David Sanborn•As We Speak•Warner Bros. Records•1982','\
Freeway Fusion•Textiles•JAJ Records•1988','\
Various•Sax Planet - The Best Of Saxophone Music•Landy Star Music•2000','\
Mark Egan•As We Speak•Wavetone Records•2006','\
David Sanborn•The Best Of David Sanborn•Warner Bros. Records•1994','\
Ian Shaw (2)•A World Still Turning•441 Records•2003','\
Lorez Alexandria•Dear To My Heart•Trend (3)•1987','\
David Sanborn•Then Again - The Anthology•Rhino Records (2)•2012','\
Barbra Streisand•Grand Prix 20•CBS/Sony•1979','\
Matt Monro•Heart Breakers - 20 Golden Greats From Matt Monro•EMI•1980'),'\
\
Asa\
':('\
Grupo Medusa•Grupo Medusa•Som Da Gente•1981','\
Hermeto Pascoal•A Música Livre De Hermeto Paschoal•Sinter•1973','\
Mark De Clive-Lowe•Heritage•Ropeadope•2019','\
Alexandru Andrieș•Nimic Nou Pe Frontul De Est•Romtrust Citizen•1993','\
Baden Powell•Le Coeur De Baden Powell - Volume 4 •Disques Festival•1974','\
Mandrake Som•O... Amigo•EMI•1977','\
Cosmos (21)•Musitopia•Canyon•1983','\
César Camargo Mariano•Cesar Camargo Mariano•Chorus Estudio•1990'),'\
\
Ask Me Now\
':('\
Joe Henderson•An Evening With•Red Record•1987','\
Perico Sambeat Quartet•Dual Force•no label•1994','\
Lew Tabackin•Angelica•Eastworld•1985','\
Anthony Braxton•Six Monk\'s Compositions (1987)•Black Saint•1988','\
Abdullah Ibrahim•Knysna Blue•Tiptoe•1994','\
The Thelonious Monk Quintet•5 By Monk By 5•Riverside Records•1959','\
Floros Floridis•The Manager In Charge•J.n.d. Records•1987','\
James Carter Quartet•Jurassic Classics•DIW•1994','\
Joe Henderson•The State Of The Tenor • Live At The Village Vanguard • Volume 1•Blue Note•1986','\
McGann•McGann•Rufus Records (2)•1995','\
Steve Lacy•Reflections•New Jazz•1959'),'\
\
At Last\
':('\
Guy Lombardo And His Royal Canadians•Blue Tango •Decca•1952','\
Glenn Miller And His Orchestra•Call Me Irresponsible / At Last•Epic•1969','\
Ronny Jordan•At Last•N-Coded Music•2003','\
Tony Martin (3)•Scusami / At Last•RCA Victor•0','\
Glenn Miller And His Orchestra•In The Mood / At Last•no label•1944','\
John Joseph Hall•Home At Last •CBS•1979','\
Glenn Miller And His Orchestra•That Old Black Magic / At Last•no label•1943','\
Herman Apple And His Group•Under Paris Skies•RCA Camden•0','\
Steely Dan•Deacon Blues•ABC Records•1977','\
The New Vaudeville Band•At Last•DJM Records (2)•1976','\
Steely Dan•Deacon Blues•ABC Records•1977','\
Glenn Miller And His Orchestra•At Last / Perfidia•RCA Victor•1952','\
Pascal Schumacher•Face To Face In Bremen - Live•Enja Records•2009','\
Wingy Manone•Awful Waffle Man•Coral•0','\
J.R. Mitchell•Live At Macalester College 72•Dogtown Records•1972','\
Rusty Bryant•Fire Eater•Prestige•1971'),'\
\
At Long Last Love\
':('\
Oscar Peterson•Action•MPS Records•1968','\
Keely Smith•Swing You Lovers•Dot Records•1960','\
Grant Green•I Want To Hold Your Hand•Blue Note•1965','\
Billy Taylor•One For Fun•Atlantic•1959','\
Ray Brown Trio•Some Of My Best Friends Are...Singers•Telarc•1998','\
Frank Sinatra•A Swingin\' Affair Part 2•Capitol Records•1957','\
The Claude Williamson Trio•The Fabulous Claude Williamson Trio•Contract Records•1961'),'\
\
Au Privave\
':('\
Charlie Parker And His Orchestra•Au Privave / Star Eyes •Mercury•1951','\
The Oscar Peterson Big 6•The Oscar Peterson Big 6 At The Montreux Jazz Festival 1975•Pablo Records•1975','\
Archie Shepp Quintet•Bird Fire•Impro•1979','\
Charlie Parker•The Magnificent Charlie Parker (Album #1)•Clef Records•0','\
The Oscar Peterson Big 6•The Oscar Peterson Big 6 At The Montreux Jazz Festival 1975•Pablo Records•1975','\
Keyboard Conclave•Klávesová Konkláva•Supraphon•1978','\
Frank Butler•The Stepper•Xanadu Records•1978'),'\
\
Autumn In New York\
':('\
Clifford Brown All Stars•Clifford Brown All Stars•EmArcy•1956','\
Charlie Parker With Strings•Autumn In New York / Temptation•Mercury•1952','\
The Modern Jazz Quartet•The Queen\'s Fancy•Prestige•1960','\
Jo Stafford•Autumn In New York / Autumn Leaves•Capitol Records•1955','\
Ranny Sinclair•Something To Sing About / Autumn In New York•Columbia•1964','\
Kenny Barron•Autumn In New York•Uptown Records (2)•1985','\
Arthur Blythe•Basic Blythe•CBS•1988','\
New York New York (2)•Sounds Of The Apple•Stash Records•1980','\
Nicki Parrott•Autumn Leaves•Venus Records (5)•2012','\
The George Shearing Quintet•The Shearing Spell•Capitol Records•1959','\
Sonny Stitt•Sonny\'s Blues•UpFront Records (3)•1977','\
George Coleman•Manhattan Panorama•Theresa Records•1985','\
Charlie Parker With Strings•Charlie Parker With Strings•Clef Records•1954','\
Ahmad Jamal Trio•At The Spotlight Club Vol.2•Argo (6)•1958'),'\
\
Autumn Leaves\
':('\
The Cannonball Adderley Quintet•Autumn Leaves•Blue Note•1958','\
Nicki Parrott•Autumn Leaves•Venus Records (5)•2012','\
Hampton Hawes•Piano Improvisation•International Joker Production•1977','\
Hampton Hawes•Piano Improvisation•International Joker Production•1977','\
Nicki Parrott•Autumn Leaves•Venus Records (5)•2012','\
Cannonball Adderley•Alison\'s Uncle / Autumn Leaves•Blue Note•1983','\
Maynard Ferguson•Autumn Leaves / Finger-Snappin\'•Mercury•1955','\
Jeremy Steig•Outlaws•Enja Records•1977'),'\
\
Autumn Nocturne\
':('\
Ray Anthony & His Orchestra•Tenderly / Autumn Nocturne•Capitol Records•0','\
Art Farmer Quartet•Autumn Nocturne / I Walk Alone•Prestige•1955','\
Dick Hyman And His Orchestra•Provocative Piano•Command•1960','\
Claude Thornhill And His Orchestra•Autumn Nocturne / Snowfall•Columbia•1947','\
Nicki Parrott•Autumn Leaves•Venus Records (5)•2012','\
Claude Thornhill And His Orchestra•Autumn Nocturne / Where Has My Little Dog Gone?•Columbia•1947','\
David Rose & His Orchestra•Autumn Leaves•MGM Records•1957','\
Lawrence Welk And His Sparkling Strings•Twilight Time•Coral•1959','\
Nicki Parrott•Autumn Leaves•Venus Records (5)•2012'),'\
\
Autumn Serenade\
':('\
David Rose & His Orchestra•Autumn Leaves•MGM Records•1957','\
Kenyon Hopkins And His Orchestra•Swingin\' Serenades•Capitol Records•1960','\
Lawrence Welk And His Sparkling Strings•Twilight Time•Coral•1959','\
Nicki Parrott•Autumn Leaves•Venus Records (5)•2012','\
Harry James And His Orchestra•It\'s Been A Long Long Time / Autumn Serenade•Columbia•1945','\
Bobby Hackett•Bobby Hackett With Strings•Sears•0','\
Bobby Hackett•Moonlight Becomes You•Pickwick/33 Records•1965','\
Dick Hyman And His Orchestra•Provocative Piano•Command•1960','\
Al Cohn And His "Charlie\'s Tavern" Ensemble•East Coast - West Coast Scene•RCA Victor•1955','\
George Shearing•The Shearing Touch•Capitol Records•1960','\
Georgie Auld•Manhattan With Strings•United Artists Records•1959'),'\
\
Avalon\
':('\
Paul Whiteman And His Orchestra•Dardanella / Avalon•Victor•1940','\
Charlie Ventura And His Orchestra•Avalon / Confessin\'•Mercury•1952','\
The Benny Goodman Quartet•Die Benny Goodman Story•Brunswick•1956','\
Stéphane Grappelli And His Hot Four•Avalon / Djangology•Decca•1937','\
Lenny Dee (2)•Caravan•Decca•1956','\
Alix Combelle•Al\'s Idea / Avalon•Swing (3)•1938','\
Jimmie Lunceford And His Orchestra•Sleepy Time Gal / Avalon•Brunswick•0','\
Natalie Cole•Route 66•WEA Music K.K.•1991','\
Harry James And His Orchestra•Ciribiribin (They\'re So In Love) / Avalon•Columbia•1939','\
The Benny Goodman Quartet•Avalon / The Man I Love•no label•0','\
Frans Poptie And His Swing Specials•Swing Specialities No. 2•Fontana•1957','\
The Benny Goodman Quartet•The Benny Goodman Story Volume 2 Part 2•Brunswick•1956'),'\
\
Avance\
':('\
Yellowjackets•Politics•GRP•1988','\
Chihiro Yamanaka•Forever Begins•Verve Records•2010','\
Cachao•Descargas•Classic Music (2)•2002','\
Stefano Bollani•Les Fleurs Bleues•Label Bleu•2001','\
Ursus Minor•Zugzwang•Hope Street•2005','\
David Koven•Nouveau Monde•EMI•1996','\
Die Goldenen Zitronen•Dead School Hamburg (Give Me A Vollzeitarbeit)•Cooking Vinyl•1998','\
Various•Subway Salsa: The Montuno Records Story•Vampi Soul•2012'),'\
\
Ay Arriba!\
':('\
no artist•April Jam•Open Reel•1980'),'\
\
Baby Come To Me\
':('\
Larry Adler•Lover Come Back To Me / My Melancholy Baby•Columbia•1938','\
Earl Grant•This Little Girl Of Mine•Decca•1964','\
The Manhattan Transfer•Baby Come Back To Me (The Morse Code Of Love)•Atlantic•1985','\
Claire Austin•When Your Lover Has Gone•Contemporary Records•1956','\
Basia•Until You Come Back To Me (That\'s What I\'m Gonna Do)•Epic•1990','\
SoulLexa•Demo-CD•Not On Label (SoulLexa meets JazzStefan Self-released)•2006','\
Oregon Jazz Band•One More Time•Not On Label•1964','\
Arturo Sandoval•Americana•N-Coded Music•1999','\
The Dutch Swing College Band•Boys Meet Girls•Philips•1966','\
Lily Frost•Lily Swings•Marquis Music•2008','\
George Wein & The Newport All-Stars•George Wein\'s Newport Jazz Festival All Stars•Smash Records (4)•1963','\
Roy Ayers Ubiquity•Vibrations•Polydor•1976'),'\
\
Baby It\'s Cold Outside\
':('\
Shirley Scott•Travelin\' Light•Prestige•1964','\
Spyro Gyra•A Night Before Christmas•Heads Up International•2008','\
Dean Martin•A Winter Romance•Capitol Records•1959','\
Holly Cole•Baby It\'s Cold Outside•Alert Music Inc.•2001','\
Dean Martin•Holiday Cheer•Capitol Records•1965','\
Various•Elf - Music From The Major Motion Picture•New Line Records•2003','\
Charlie McKenzie•Fabulous Songs Of The 40\'s•Dot Records•0','\
Ella Fitzgerald•Ella And Her Fellas•Decca•1957','\
Jo Stafford•Ski Trails•Columbia•1956'),'\
\
Baby I Love You\
':('\
Tom Scott•Baby I Love You•Impulse!•1967','\
Machito And His Orchestra•Baby I Love You / Alfie•RCA Victor•1967','\
Teddy Wilson And His Orchestra•Sailin’ / I Can\'t Give You Anything But Love•Brunswick•1937','\
Freddy Martin And His Orchestra•One-Zy Two-Zy (I Love You-Zy) / Sleepy Baby•RCA Victor•1946','\
Jerry King And His Orchestra•Gold Record•Promenade•0','\
Jimmy McGriff•I Can\'t Get No Satisfaction / I Can\'t Give You Anything But Love Baby•Solid State Records (2)•1966','\
Mindy Carson•Baby Baby Baby•Columbia•1958','\
Ben Pollack And His Pick-A-Rib Boys•I Can\'t Give You Anything But Love Baby / San Sue Strut•Discovery Records•1950','\
Shirley Horn•Close Enough For Love•Verve Records•1989','\
Fats Waller & His Rhythm•Darktown Strutters\' Ball / I Can\'t Give You Anything But Love Baby•Bluebird (3)•1940','\
Art Blakey & The Jazz Messengers•Art Blakey & The Jazz Messengers•Impulse!•1961','\
Houston Person•The Big Horn•Muse Records•1979','\
Reuben Wilson•On Broadway•Blue Note•1968','\
Nina Simone•A Portrait Of Nina•Trip•1974','\
Ray Charles•I Wonder•ABC-Paramount•1961'),'\
\
Backstage Sally\
':('\
Art Blakey & The Jazz Messengers•Buhaina\'s Delight•Blue Note•1963'),'\
\
Bags and Trane\
':('\
Milt Jackson•Bags & Trane•Atlantic•0','\
Milt Jackson•Bags & Trane•Atlantic•1961','\
John Coltrane•My Favorite Things•Not Now Music•2012','\
John Coltrane•The Atlantic Years – In Mono•Atlantic•2016','\
John Coltrane•The Heavyweight Champion - The Complete Atlantic Recordings•Rhino Records (2)•1995'),'\
\
Bags\' Groove\
':('\
Milt Jackson•Bags & Flutes•Atlantic•0','\
The Jay And Kai Quintet•Don\'t Argue / Bags\' Groove•Prestige•1955','\
Miles Davis All Stars•Vol. 1•Prestige•1955','\
J.J. Johnson•Bags\' Groove / Don\'t Argue•Prestige•1955','\
The Modern Jazz Quartet•Night In Tunisia / Bags\' Groove•Metronome•1959','\
Various•Newport In New York \'72 The Jam Sessions Vol 2•Atlantic•1972','\
Miles Davis•Bags Groove•Prestige•1957','\
Miles Davis•Miles Monk & Milt•Prestige•1966','\
The Modern Jazz Quartet•Milt Jackson Modern Jazz Quartet•Vogue Records•0','\
Woody Herman And The Las Vegas Herd•Jackpot! Part 1•Capitol Records•0'),'\
\
Baja Bajo\
':('\
John Patitucci•John Patitucci•GRP•1988','\
Charged Particles•Charged Particles•no label•1994','\
Ray Conniff And His Orchestra & Chorus•El Disco De Oro De Ray Conniff•CBS•1966'),'\
\
Ballet\
':('\
Krzysztof Komeda•Ballet Etudes•Polonia Records•1995','\
Fats Waller•Clothes-Line Ballet / Viper\'s Drag•no label•1935','\
George Russell•Othello Ballet Suite / Electronic Organ Sonata No. 1•Sonet•1970','\
Ambrose & His Orchestra•A Burmese Ballet / Early Morning Blues•Decca•1940','\
Guy Luypaerts•The Esquire Album Of Music For The Continental Host•RCA Victor•1955','\
Krzysztof Komeda•Ballet Etudes/The Music Of Komeda - A Jazz Message From Poland Presented By An International Quintet•Metronome•1963','\
Johnny Douglas And His Orchestra•Ballet Of The Bells / Solfeggio	•Decca•1954','\
Leonard Bernstein•Leonard Bernstein Conducts Gerswhin An American In Paris Coplan Billy The Kid Ballet Suite•RCA Camden•1958','\
Leroy Anderson And His "Pops" Concert Orchestra•Sandpaper Ballet / Song Of The Bells•Columbia•1955','\
Michel Legrand•Les Demoiselles De Rochefort (Bande Originale Du Film)•Philips•1967','\
Spyro Gyra•Live Concert Series•Infinity Records (2)•1979','\
Gary Burton Quartet•Live In Tokyo•Atlantic•1971','\
Louis Hooper•Lou Hooper Piano•Radio Canada International•1973'),'\
\
Baltimore Oriole\
':('\
Lorez Alexandria•Baltimore Oriole•Jazzman•2004','\
Lorez Alexandria•Baltimore Oriole•Jazzman•2004','\
Lorez Alexandria•Baltimore Oriole / Mother Earth•Argo (6)•1963','\
Various•Rewind! 3 12"•Ubiquity•2003','\
Bob Dorough•Devil May Care•52e Rue Est•1983','\
Various•Jazzier Rhythms•Hubbub Records•1996','\
Soesja Citroen•Shall We Dance - Or Keep On Moping•Timeless Sunny•1987','\
Various•Curtain Call Series Volume 6•Brunswick•1954','\
Maynard Ferguson•The Blues Roar•Mainstream Records•1964','\
Hoagy Carmichael•Hoagy Sings Carmichael With The Pacific Jazzmen•Jazztone (2)•1957','\
Lorez Alexandria•For Swingers Only•Argo (6)•1963'),'\
\
Ba-Lue Bolivar Ba-Lues-Are\
':('\
Thelonious Monk•Brilliant Corners•Riverside Records•1976','\
Thelonious Monk•Brilliant Corners•Riverside Records•1957','\
Steve Lacy•School Days - A 1963 Live Session Released For The First Time•Emanem•1975','\
Thad Jones•A Tribute To Monk And Bird•Tomato•1978'),'\
\
Barbados\
':('\
The Charlie Parker All-Stars•Barbados / Parker\'s Mood•Savoy Records•1948','\
Art Farmer Quintet•Mirage•Soul Note•1982','\
Art Farmer Quintet•At Boomers•East Wind•1976','\
Art Farmer•In Concert•Enja Records•1986','\
Art Farmer Sextet•Round About Midnight•Jugoton•1981','\
The Montgomery Brothers•Wes\' Best•Fantasy•1967','\
Roland Hanna•Bird Watching•Progressive Records (2)•1978','\
Charlie Parker•The \'Bird\' Returns•Savoy Records•1962','\
Chet Baker Trio•September Song•Marshmallow (3)•1986','\
Charlie Parker•Charlie Parker Memorial Volume 4•CBS•1963'),'\
\
Barbara\
':('\
Joachim Kühn•Live! The Kiel Concert - The Stuttgart Concert•Sandra Music Productions•1979','\
Ted Weems And His Orchestra•Barbara / Miss Annabelle Lee•Victor•1927','\
Lew Soloff•Yesterdays•King Records•1986','\
Horace Silver•Silver \'N Brass•Blue Note•1975','\
Paul Mille Et Son Orchestre•Walking On The Purple Bridge / Barbara "B"•Disques Vogue•1969','\
Charles Greenlee•I Know About The Life•Baystate•1977','\
Toshiko Akiyoshi•Toshiko And Modern Jazz•Columbia•1977','\
Second Sight•Flying With The Comet•Sunjump Records•1986','\
Toshiko Mariano And Her Big Band•Jazz In Japan Recorded In Tokyo•Vee Jay Records•1965','\
David Wertman•Earthly Delights•Sweet Earth Records•1978','\
Val Norman (2)•The Ballad Of Barbara Graham•Valor Records•1959','\
Jamey Aebersold•For You To Play... Horace Silver Eight Jazz Classics•JA Records•1978','\
Gil Evans•The Individualism Of Gil Evans•Verve Records•1964'),'\
\
Basin Street Blues\
':('\
Louis Armstrong And His All-Stars•Basin Street Blues•Decca•1953','\
Louis Armstrong And His Orchestra•After You\'ve Gone / Basin Street Blues•Parlophone•0','\
Benny Goodman And His Orchestra•Basin Street Blues / Beale Street Blues•Columbia•1934','\
Kid Koala•Basin Street Blues•Ninja Tune•2003','\
The Bob Wilber All Star Jazz Band•The Dixie Do-It-Yourself•Music Minus One•0','\
Clyde McCoy And His Orchestra•Sugar Blues / Basin Street Blues•Vogue Records (2)•1947','\
Duke Ellington•Back To Back Vol. 2 (Duke Ellington And Johnny Hodges Play The Blues)•Verve Records•1959','\
Santo Pecora And His Dixie Land Jazz Band•Basin Street Blues / Twelfth Street Rag•Mercury•1950','\
Louis Armstrong•St Louis Blues / Basin Street Blues•Odeon•1959','\
Herb Jeffries And His Orchestra•Basin Street Blues•Mercury•1950','\
Louis Armstrong And His Orchestra•Basin Street Blues / St. Louis Blues•Vocalion•1935','\
Nat Gonella & His Georgians•E Flat Blues / Basin Street Blues•Parlophone•1935','\
Albert Nicholas•Plays The Blues•Jazztone (2)•1956','\
Jimmy Smith•The Cat•Verve Records•1964','\
Milt Herth•Basin Street Blues / Twelfth Street Rag•Decca•0'),'\
\
Bass Blues\
':('\
Albert Ammons•Bass Goin\' Crazy / Suitcase Blues•Blue Note•1941','\
no artist•Daily Rag / Big Bass Horn Blues•Capitol Records•1949','\
Paul Chambers (3)•1st Bassman•Vee Jay Records•1960','\
Larry Willis•Steal Away•AudioQuest Music•1992','\
Art Davis Quartet•Life•Soul Note•1986','\
Herbie Mann•Flute Flight•Prestige•1957','\
Peter Ind•Looking Out•Esquire•1962','\
Paul Chambers (3)•Paul Chambers 1935-1969•Epitaph (2)•0','\
Ron Paley•Boxton•Neptune Records (17)•1977','\
Ray Brown•SuperBass•Telarc•1997','\
Bob Enevoldsen Quintet•Bob Enevoldsen Quintet•Tampa Records•1956'),'\
\
Batterie\
':('\
Jacques Loussier•Pulsion•CBS•1979','\
Art Tatum And His Band•Batterie Bounce / Lucille•Decca•0','\
Henri Renaud•Jazz Mobile•no label•1967','\
Carla Bley•Jazz Realities•Fontana•1966','\
Paul Bley Quintet•Barrage•ESP Disk•1965','\
Jaco Pastorius•Pastorius / Metheny / Ditmas / Bley•Improvising Artists Inc.•1976','\
Paul Bley Trio•Closer•ESP Disk•1966','\
no artist•Blood Lines •Milestone (4)•1999','\
Paul Bley•Notes•Soul Note•1988','\
Magma (6)•Concert 1976 - Opéra De Reims•AKT (3)•1996'),'\
\
Be Bop\
':('\
Stan Getz Quartet•As I Live And Bop / Interlude In Be Bop•no label•0','\
Various•Jazz Auf AMIGA 1947-1962 (1)•AMIGA•1981','\
Howard McGhee Quintet•Be Bop / Lover Man•Dial Records (3)•0','\
Dizzy Gillespie And His Orchestra•Cubana Be / Cubana Bop•no label•1948','\
Ella Fitzgerald•I\'ve Got a Feeling I\'m Falling / My Baby Likes to Be-Bop•Decca•1948','\
Shoichi Yui•The Amazing Shōichi Yui Volume 1•Blue Note•1984','\
Frank Zappa•Be Bop Tango•буд кон•0','\
Lionel Hampton And His Sextet•Cherokee / Rebop And Be-Bop•Brunswick Ltd.•1947','\
Charlie Barnet And His Orchestra•Be-bop Spoken Here / Gloomy Sunday•Capitol Records•0','\
Freddie Slack And His Orchestra•Mister Freddie\'s Boogie•Capitol Records•1948','\
Charlie Parker•Carvin\' The Bird•Drive Archive•1994','\
Babs Gonzales•Be-Bop Santa Claus / Watch Them Resolutions•King Records (3)•1955','\
Lester Young And His Band•These Foolish Things / Lester\'s Be-Bop Boogie•Esquire•0','\
Babs Gonzales•The Be-Bop Santa Claus / Manhattan Fable•Bruce Record Co. (2)•1954','\
Orchestra Bruno Martino•Belle From Barcelona / Calypso Be-Bop•Electrola•1959'),'\
\
Beautiful Love\
':('\
David Rose & His Orchestra•Beautiful Music To Love By  / Suddenly•MGM Records•1953','\
Frankie Carle And His Orchestra•Love Is A Beautiful Thing / Rue De Romance•Columbia•1949','\
Ray Hartley•Chanson D\'Amour (Song Of Love)•RCA Victor•1958','\
Benny Carter•The Urbane Mr. Carter•Karusell•1954','\
The Loving Tree•Beautiful Experience / Let Him Love You•Viva (3)•1970','\
Ella Fitzgerald•I\'ll Always Be In Love With You•Verve Records•1962','\
Benny Golson Quartet•Benny Golson Quartet•LRC Ltd.•1990','\
Various•Cool Whalin\' - Be Bop Vocals Rare And Unissued Material•Spotlite Records•1979','\
Kenny Dorham•Jazz Contrasts•Riverside Records•1957','\
John Coltrane•The Believer•Prestige•1964'),'\
\
Beauty and the Beast\
':('\
Mark Murphy•Beauty And The Beast•Muse Records•1987','\
Joe Sample•The Hunter•MCA Records•1983','\
Tony Bennett•Love Song From Beauty And The Beast•Columbia•1957','\
Pekka Pohjola•Flight Of The Angel•Pohjola Records•1986','\
Chris Hunter•Scarborough Fair•Paddle Wheel•1990','\
Jim Mullen•Thumbs Up•Coda Records (3)•1983','\
Dave Pike•Peligroso•CuBop•2000','\
Wayne Shorter•Native Dancer•Columbia•1975','\
The Jazz Networks•Beauty And The Beast•RCA•1993','\
Wayne Shorter•This Is Jazz Vol. 19•Columbia•1996'),'\
\
Begin The Beguine\
':('\
Stanley Black & His Orchestra•Begin The Beguine•Decca•1960','\
Artie Shaw And His Orchestra•Begin The Beguine•RCA Victor•0','\
Chubby Jackson And His Fifth Dimensional Jazz Group•Crown Pilots / Begin The Beguine•Cupol•1948','\
Les Paul And His Trio•Begin The Beguine / Dream Dust•Decca•1945','\
Billy Williams (5)•Begin The Beguine / For You•Coral•1960','\
Orchester Eddie Tower•Beguine / En Jouant Du Violon•Olympia•0','\
Art Tatum•The Genius Of Art Tatum•Karusell•0','\
Don Bader And The Schleppers•Begin The Beguine / Honky Tonk•MATTHEW RECORDS•0','\
Artie Shaw And His Orchestra•Begin The Beguine / Deep Purple•no label•1939','\
Artie Shaw And His Orchestra•Begin The Beguine / Deep Purple•no label•1939','\
Earl Guest•Begin The Beguine / Foxy•Columbia•1964','\
Glenn Miller And The Army Air Force Band•My Blue Heaven / Begin The Beguine•RCA Victor•0','\
The Checkmates (6)•Begin The Beguine (Stomp)•London International•1962','\
Diana Miller•Begin The Beguine / Night And Day•Sonora (2)•1940'),'\
\
Beneath It All\
':('\
Kenny Barron•Swamp Sally•Verve Records•1996','\
Needlepoint•The Diary Of Robert Reverie•BJK Music•2018','\
Wendy Matthews•Cafe Naturale•BMG Australia•2004','\
Emeli Sande•Our Version Of Events (Live At The Royal Albert Hall)•Capitol Records•2013','\
Carl Doy•Moonlight Piano•Columbia•1991','\
Mette Henriette Martedatter Rølvåg•Mette Henriette•ECM Records•2015','\
Various•Today\'s Favourites Tomorrow\'s Evergreens•no label•2006','\
Various•The Crossover Cafe II - Smooth Jazz & Sweet Soul•Universal Music Group International•2014','\
Richard Clayderman•Best Of (My Favourites)•Ariola•2011','\
Various•Bravo Hits 80•Polystar (3)•2013','\
Various•Great Romantic Piano Favorites•no label•2004','\
Richard Clayderman•Pianul Magic Al Lui Richard Clayderman•no label•2006','\
Sting•B-Sides & Rarities•Star Mark•2007','\
Various•Memories Are Made Of This (Great Stars Of The 50\'s)•no label•1990'),'\
\
Bernie\'s Tune\
':('\
Gerry Mulligan Quartet•Lullaby Of The Leaves / Bernie’s Tune•Pacific Jazz•1952','\
Wardell Gray•Live In Hollywood•Xanadu Records•1978','\
Chris Flory•Blues In My Heart•Stony Plain Records•2007','\
Various•Le 18 Gemme Del Jazz•Giants Of Jazz•1991','\
The Modernaires•Tributes In Tempo•Philips•1953','\
Blossom Dearie•The Adorable Blossom Dearie•Él•2019'),'\
\
Bess You Is My Woman\
':('\
Harry James And His Orchestra•Bess You Is My Woman / Shiny Stockings•MGM Records•1959','\
Peter Nero•Peter Nero On Tour•RCA Victor•1966','\
The Melachrino Orchestra•Selection From Porgy And Bess•La Voix De Son Maître•0','\
The Modern Jazz Quartet•The Modern Jazz Quartet Plays George Gershwin\'s Porgy & Bess•Atlantic•1965','\
Dino Martinelli And His Orchestra•Music from George Gershwin\'s "Porgy and Bess"•Fontana•1959','\
Rex Stewart•Porgy & Bess Revisited•Warner Bros. Records•1959','\
Buddy Collette And The Poll Winners•Porgy And Bess•Interlude (2)•1959','\
Ella Fitzgerald•Ella Und Louis Singen Aus Porgy And Bess•AMIGA•1966','\
Oscar Peterson•Porgy & Bess•Pablo Records•1976','\
Don Shirley•The Don Shirley Point Of View•Atlantic•1972','\
Quincy Jones•The Great Wide World Of Quincy Jones: Live!•Mercury•1984'),'\
\
Bessie\'s Blues\
':('\
Louis Armstrong And His Orchestra•Bessie Couldn\'t Help It / Dallas Blues•Odeon•1929','\
Garland Wilson•Blues En Si Bemol / Get Up Bessie•Brunswick•1932','\
Various•How Blue Can You Get? (Great Blues Vocals In The Jazz Tradition)•Bluebird (3)•1989','\
Pee Wee Hunt•Straight from Dixie! with Pee Wee Hunt•Capitol Records•0','\
Archie Shepp - Chet Baker Quintet•In Memory Of•L+R Records•1988','\
Bix Beiderbecke•Bixology•Ediciones Del Prado•1996','\
Pee Wee Hunt•Straight From Dixie!•Capitol Records•1955','\
The Bud Powell Trio•Time Was•RCA•1987','\
Jimmy Rushing•Big Little Bands•Onyx Records (3)•1974'),'\
\
Best Is Yet To Come The\
':('\
David Carroll & His Orchestra•Hallelujah Gathering•Mercury•1963','\
Louis Prima•You\'ll Never Get Away / The Best Is Yet To Come•Prima Magnagroove•0','\
Nancy Wilson•The Best Is Yet To Come•Capitol Records•1964','\
Val Doonican•Heaven Is My Woman\'s Love•Philips•1973','\
Tony Bennett•Tender Is The Night•Philips•1961','\
Grover Washington Jr.•Just The Two Of Us•Elektra•1989','\
Ernestine Anderson•Will I Find My Love Today / The Best Is Yet To Come•Sue Records Inc.•1963','\
Peggy Lee•I Believe In You•Capitol Records•1963','\
Gerald Albright•24/7•Concord Jazz•2012','\
David Carroll & His Orchestra•Happy Feet•Mercury•0','\
Carmen McRae•Sarah - Dedicated To You•Novus•1991','\
The Phil Woods Quintet•All Bird\'s Children•Concord Jazz•1991','\
Frank Sinatra•It Might As Well Be Swing•Reprise Records•1964','\
Russ Freeman (2)•Sahara•GRP•0','\
Chaka Khan•Classikhan•AGU•2004'),'\
\
Better Git It In Your Soul\
':('\
Charles Mingus•Jazz Gallery: Charles Mingus•Philips•1959','\
Charles Mingus•I Giganti Del Jazz Vol. 16•Curcio•1980','\
Oiling Boiling•Two Faces•CBS•1977','\
Pepper Adams•Plays The Compositions Of Charlie Mingus•Workshop Jazz•1964','\
Something Else•Rear Quarters•no label•1992','\
Woody Herman•Woody And Friends•Concord Jazz•1981','\
Charles Mingus•Alternate Takes•Columbia Jazz•1998','\
Various•Jazz Classics•Columbia•1997','\
Charles Mingus•Charles Mingus•Fabbri Editori•1989','\
Charles Mingus•Mingus - Monk•Armando Curcio Editore•1989'),'\
\
Bewitched\
':('\
Bo Rhambo Combo•Bewitched•Peacock Records•1958','\
Danny Welton•Bewitched / Manhattan Sunrise•Coral•1959','\
Luis Arcaraz Y Su Orquesta•Johnson Rag•RCA Victor•0','\
Jan August•Bewitched / Blue Prelude•Mercury•1950','\
Felix King And His Orchestra•Bewitched•Decca•1950','\
Mel Tormé•The Piccolino / Bewitched•Capitol Records•1950','\
Earl Grant•Bewitched•Decca•1968','\
Mantovani And His Orchestra•Dream Dream Dream•Decca•1954','\
Erroll Garner•Gone Garner Gonest - Vol. 2•Columbia•0','\
Ella Fitzgerald•Ella Fitzgerald Sings The Rodgers  And Hart Song Book•Verve Records•1957','\
Bill Snyder And His Orchestra•Drifting Sands / Bewitched•Tower (7)•1950','\
Steve Lawrence (2)•I Will Wait For You / Bewitched•Columbia•1965'),'\
\
Beyond All Limits\
':('\
Jamey Aebersold•For You To Play... Woody Shaw Eight Classic Jazz Originals•JA Records•1976','\
Larry Young•Unity•Blue Note•1966','\
Larry Young•In Paris The ORTF Recordings•Resonance Records•2016','\
Robbie Williams•Sing When You\'re Winning / Swing When You\'re Winning•EMI•0','\
Larry Young•The Complete Blue Note Recordings Of Larry Young•Mosaic Records (2)•1991'),'\
\
Bidin\' My Time\
':('\
Georgie Fame•Because I Love You•CBS•1967','\
Georgie Fame•Bidin\' My Time (\'Cos I Love You)•CBS•1967','\
Ruby Braff•Fireworks•Inner City Records•2007','\
Dennis Lotis•Bidin\' My Time•Columbia•1958','\
Ruby Braff•Ruby Braff Goes "Girl Crazy"•Warner Bros. Records Inc.•1959','\
Dennis Lotis•Bidin\' My Time•Columbia•1958','\
Stanley Black & His Orchestra•Dancing Time•London Records•1951','\
Ruth Olay•"It\'s About Time" Featuring Ruth Olay•Top Rank International•0','\
Les & Larry Elgart•Les & Larry Elgart And Their Orchestra•Columbia•1957','\
Woody Herman•Songs For Hip Lovers•Verve Records•1957'),'\
\
Big Nick\
':('\
Jackie McLean•\'Bout Soul•Blue Note•1968','\
John Coltrane•Ride Again!!•Impulse!•1968','\
John Coltrane•Big Nick•MCA Records•1981','\
John Coltrane•From The Original Master Tapes•Impulse!•1988','\
Ben Sidran•Live At The Elvehjem Art Museum•Cryonic Inc.•1986','\
The Tony Williams Lifetime•Lifetime•Polydor•1975'),'\
\
Big P\
':('\
Nat Adderley Sextet•Autumn Leaves - Live At Sweet Basil•Bellaphon•1991','\
The Cannonball Adderley Quintet•At The Lighthouse•Riverside Records•1960','\
René Thomas•Blue Note Paris 1964•Royal Jazz•1990','\
Antonio Hart•For Cannonball & Woody•Novus•1993','\
The Cannonball Adderley Quintet•What Is This Thing Called Soul (In Europe - Live!)•Pablo Live•1984','\
The Gene Estes Band•Westful - Jazz In Hollywood•Nocturne (3)•1976','\
The Cannonball Adderley Quintet•What Is This Thing Called Soul (In Europe - Live!)•Pablo Live•1984','\
The Gene Estes Band•Westful - Jazz In Hollywood•Nocturne (3)•1976','\
The Riverside Reunion Band•Hi-Fly•Milestone (4)•1994','\
The New Jazz Orchestra• Western Reunion London 1965•Decca•1965','\
Jimmy Heath And His Orchestra•Really Big!•Riverside Records•1960','\
Various•On The Spot - A Peek At The 1960\'s Nordic Jazz Scene•Ricky-Tick Records•2006','\
Nat Adderley Quintet•Talkin\' About You•Landmark Records (3)•1991','\
Dave Torkanowsky•Steppin\' Out•Rounder Records•1989'),'\
\
Billie\'s Bounce\
':('\
Art Pepper•Inglewood Jam 1952•Absord Music Japan•2009','\
Mal Waldron•You And The Night And The Music (Mal \'84)•King Records•1984','\
The Montgomery Brothers•And 5 Others•World Pacific Records•1958','\
Reese Markewich Quintet•New Designs In Jazz With The Reese Markewich Quintet•Blue Moon (4)•2001','\
Barbara Dennerlein•Tribute To Charlie•Koala Records•1987','\
Charlie Parker•Charlie Parker•Nocturne•2003','\
Esquire All Stars•Esquire Jazz Concert•Giants Of Jazz•1998','\
Don Byas•"Ambiances Et Slows"•Barclay•1975','\
Various•Grand Theft Auto Vice City Official Soundtrack Box Set•Epic•2002','\
Various•All The Breaks•All The Breaks•2005'),'\
\
Bills\' Hit Tune\
':('\
The Bill Evans Trio•Consecration II - Last•Alfa Jazz•1989','\
Bill Evans•We Will Meet Again•Warner Bros. Records•1980','\
The Bill Evans Trio•Highlights From Turn Out The Stars•Warner Bros. Records•1996','\
Bill Evans•His Last Concert In Germany•West Wind•1989','\
The Bill Evans Trio•Turn Out The Stars•Warner Bros. Records•1996','\
The Bill Evans Trio•Consecration•Alfa Jazz•1989','\
Count Basie•The Big Band Leader•Past Perfect 24 Carat Gold Edition•2000'),'\
\
Bird Food\
':('\
Ornette Coleman•Bird Food•Atlantic•1959','\
Wolfgang Dauner Trio•Dream Talk•CBS•1964','\
Ornette Coleman•Change Of The Century•Atlantic•1960','\
no artist•Ornette For Ever•Moshé-Naïm•1996','\
Hakuei Kim•Trisonique•area azzurra•2011','\
Ayumi Koketsu•Rainbow Tales•M & I•2012','\
Steve Khan•Subtext•Tone Center•2014','\
Denny Zeitlin•Time Remembers One Time Once•ECM Records•1983','\
Charlie Haden•American Dreams•Verve Records•0','\
Joe Lovano•Flying Colors•Blue Note•1998'),'\
\
Bird Of Beauty\
':('\
ITS (4)•Rainbow•JVC•1980','\
Joe Gallardo•Sol•GCP•1975','\
Wayne Shorter•This Is Jazz Vol. 19•Columbia•1996','\
Herbie Mann•Herbie Mania•Atlantic•1976','\
Stanley Turrentine•Wonderland (Stanley Turrentine Plays The Music Of Stevie Wonder)•Blue Note•1987','\
Catia•Saudade De Paris•POSSION HeADS•2003','\
Peter Jacques (2)•Keyboard Flashes•EMI•1975','\
Eri Ohno•Eri My Dear•Better Days (2)•1982','\
Nnenna Freelon•Tales Of Wonder•Concord Jazz•2002','\
Svante Thuresson•Just In Time•WEA•1982','\
Herbie Mann•Discothèque•Atlantic•1975','\
Ernestine Anderson•Hello Like Before•Concord Jazz•1977'),'\
\
Birdland\
':('\
Various•Lullaby Of Birdland•RCA Victor•1955','\
Various•Lullaby Of Birdland (Volume 1)•RCA Victor•1956','\
Various•Lullaby Of Birdland (Volume 2)•RCA•0','\
Various•Lullaby Of Birdland Vol. 3•RCA•0','\
Weather Report•Birdland•Columbia•1977','\
Kai Winding•An Afternoon At Birdland•"X"•1956','\
Weather Report•Birdland•CBS•1977','\
Weather Report•Birdland•Columbia•1977','\
Ella Fitzgerald•Lullaby Of Birdland•Decca•1954','\
Charlie Ventura And His Orchestra•Lullaby In Rhythm / Birdland•RCA Victor•1949','\
Ella Fitzgerald•Later / Lullaby Of Birdland•Decca•1954','\
Weather Report•Birdland•CBS•1977','\
The Manhattan Transfer•Birdland•Atlantic•1979','\
Weather Report•River People / Birdland•CBS•1978','\
Quire (2)•Ain\'t Misbehavin\'•RCA•0','\
Sarah Vaughan•Lullaby Of Birdland / September Song•EmArcy•0','\
Ralph Flanagan And His Orchestra•Did I Remember / Lullaby Of Birdland•RCA Victor•0'),'\
\
Birth of the Blues\
':('\
Ziggy Elman & His Orchestra•The Birth Of The Blues / Sunny Disposish•MGM Records•1951','\
Pete Fountain•Birth Of The Blues / Begin The Beguine•Coral•0','\
Lenny Dee (2)•Plantation Boogie•Decca•1954','\
Harry Bidgood And His Broadcasters•The Birth Of The Blues / Little White House •Broadcast (2)•0','\
Richard Maltby And His Orchestra•Theme From War And Peace / The Birth Of The Blues•RCA•1956','\
Sonny Stitt•Blows The Blues•Verve Records•1960','\
Sammy Davis Jr.•Love (Your Magic Spell Is Everywhere)•Decca•1954','\
Frank Sinatra•The Birth Of The Blues •Columbia•1954','\
Gerry Mulligan Quartet•Vol. 2•Artist•0','\
101 Strings•Rhapsody In Blue•Mode Disques•0'),'\
\
Black and Blue\
':('\
Louis Armstrong And His Orchestra•Black And Blue / Sweet Savannah Sue•Parlophone•0','\
Sidney Bechet•Some Of These Days / Black And Blue•Melodisc (3)•1949','\
The Lou McGarity Big Eight•Blue Lou•Argo (6)•1960','\
no artist•Dinah / (What Did I Do To Be So) Black And Blue•Bluebird (3)•1940','\
Al Caiola•Serenade In Blue•Savoy Records•1956','\
Rocketnumbernine•Meyouweyou•Smalltown Supersound•2013','\
Duke Ellington And His Orchestra•Riding On A Blue Note / The New Black And Tan Fantasy•Parlophone•0','\
The Dave Brubeck Quartet•Concord On A Summer Night•Concord Jazz•1982','\
Dollar Brand•Black Lightning•The Sun•1976','\
The Sun Ra Arkestra•El Is A Sound Of Joy•Modern Harmonic•2017','\
André Previn•Like Blue•MGM Records•1960','\
Duke Ellington And His Orchestra•Black And Blue / Jungle Jamboree•Brunswick•1939'),'\
\
Black and Tan Fantasy\
':('\
Jimmie Lunceford And His Orchestra•Black And Tan Fantasy / Solitude•Brunswick•0','\
Duke Ellington And His Orchestra•Ellington \'55 (Part 1)•Capitol Records•1955','\
Duke Ellington And His Orchestra•Black And Tan Fantasy / Ring Dem Bells•Odeon•0','\
Stefano Bollani Trio•Black And Tan Fantasy•Venus Records (5)•2003','\
Duke Ellington And His Orchestra•Black And Tan Fantasy / What Can A Poor Fellow Do?•Okeh•1928','\
Duke Ellington And His Orchestra•Riding On A Blue Note / The New Black And Tan Fantasy•Parlophone•0','\
David Rose & His Orchestra•The Stripper•MGM Records•1968','\
Duke Ellington•Duke Ellington\'s Band Shorts•Biograph•1978','\
Kenny Ball And His Jazzmen•Kenny\'s Big 4•Pye Jazz•1961','\
Duke Ellington And His Orchestra•Ellingtonia - Vol. 1 “The Twenties”•Philips•0','\
Louis Armstrong•Louis Armstrong & Duke Ellington•Avenue (6)•1974','\
Theatre Bizarre Orchestra•Dance With The Devil!!•Hold Fast•2017','\
The Dutch Swing College Band•Ice Cream•Philips•1959'),'\
\
Black Coffee\
':('\
Johnny Hammond•Black Coffee•Riverside Records•1963','\
Ella Fitzgerald•Lover\'s Gold / Black Coffee•Decca•1949','\
Pat Suzuki•Daddy / Black Coffee•Vik•1958','\
Sarah Vaughan•Black Coffee / As You Desire Me•Columbia•0','\
Pride Of The Cross•Tommy\'s Blue Valentine•Big Beat Records•1985','\
9DW•Black Coffee / Vicoden Reality•Wax Poetics Records•2009','\
Jacintha•Lush Life•Groove Note•2001','\
Kazuo Yashiro Trio•Black Nag•Takt Jazz Series•1997','\
Earl Grant•Black Coffee / I\'m Just Lucky So And So•Decca•1964','\
SoulLexa•Demo-CD•Not On Label (SoulLexa meets JazzStefan Self-released)•2006','\
Peggy Lee•You\'ve Got To See Mamma Every Night (Or You Can\'t See Mamma At All)•Decca•1964','\
Sonny Criss•This Is Criss!•Prestige•1966','\
Cat Anderson•plays at 4 a.m.•Columbia•1958','\
Duke Pearson•Profile•Blue Note•1960','\
The Kai Winding Trombones•The Incredible Kai Winding Trombones•Impulse!•1961'),'\
\
Black Diamond\
':('\
The Rippingtons•Black Diamond•Windham Hill Jazz•1997','\
Ralph Moore Quartet•623 C Street•Criss Cross Jazz•1987','\
Wayne Shorter•Introducing Wayne Shorter•Vee Jay Records•1959','\
Eddie Daniels•Blackwood•GRP•1989','\
The Roland Kirk Quartet•Rip Rig & Panic•Limelight•1965','\
Wayne Shorter•Wayne Shorter•GNP Crescendo•1973','\
Various•Transonic 11•Transonic Records (4)•2002','\
no artist•Tradition In Colour•Encore!•1962','\
Claude Yvoire•Jewels From Cartier•RCA Victor•1956'),'\
\
Black Ice\
':('\
Jim Snidero•Stream Of Consciousness•Savant•2013','\
The Dutch Swing College Band•Ice Cream•Philips•1959','\
The Jeff Lorber Fusion•Soft Space•Inner City Records•1978','\
Mikołaj Trzaska•Tar & Feathers•Gusstaff Records•2014','\
Lyle Mays•Solo (Improvisations For Expanded Piano)•Warner Bros. Records•2000','\
The Jeff Lorber Fusion•Lift Off•Arista•1985','\
The Jeff Lorber Fusion•Now Is The Time•Heads Up International•2010','\
Old Merry Tale Jazzband•Live In Der Fabrik - Heute Dixieland•Intercord•1973','\
Stuart Hamm•Kings Of Sleep•Food For Thought Records•1989','\
Beryl Moreland•Last Call•Blackwards Records•1996','\
Irene Schweizer•Live In Zürich•Intakt Records•2013','\
Pete Candoli•For Pete\'s Sake•Kapp Records•1960','\
Angelo Baroncini•Music For Movement•Roman Record Company•1969','\
Nelli Rees•Jazz Noir•Candid•2003','\
Tape Five•Swing Patrol•Chinchin Records•2012'),'\
\
Black Monday\
':('\
Andrew Hill•Andrew!!!•Blue Note•1968','\
Georgie Fame•A Declaration Of Love•ITM ARCHIVES•2015','\
Teddy Buckner And His Dixieland Band•A Salute To Louis Armstrong•Disques Vogue•0','\
The Brian White~Alan Gresty Ragtimers•Muggsy Remembered•Jazzology•1988','\
Rod Mason Jazz Band•Stars Fell On Alabama•Jeton•1979','\
Polaris Celebration Band•Jazz Me Blues•Not On Label (Polaris Celebration Band Self-released)•1986','\
Earl Hines•Reunion In Brussels•Red Baron•1992','\
Dave Burrell•Windward Passages•Hat Hut Records•1980','\
Earl Hines•Earl Hines live! Aalborg Denmark 1965•Storyville•1994','\
Frank Rosolino•Turn Me Loose!•Reprise Records•1961'),'\
\
Black Narcissus\
':('\
Ornicar Big Band•Mais Où Est Donc Ornicar?•IDA Records•1984','\
Heidi Vogel•Turn Up The Quiet•Far Out Recordings•2013','\
Joe Henderson•Henderson\'s Habiliment•VICTOR WORLD GROUP•1971','\
Nexus (50)•Nexus•Four Leaf Clover Records•1978','\
Frank Morgan Allstars•Reflections •Contemporary Records•1989','\
Steve Houben•Stephane Houben•MD (6)•1977','\
Joe Henderson•Black Narcissus•Milestone (4)•1976','\
Joe Henderson•Big Band•Verve Records•1996','\
Guido Manusardi•Children Dance•Dire (2)•1986','\
Flora Purim•Encounter•Milestone (4)•1977','\
Joe Henderson•Power To The People•Milestone (4)•1969'),'\
\
Black Nile\
':('\
Wayne Shorter•Night Dreamer•Blue Note•1964','\
MaseQua Myers•Black Land Of The Nile / Communion Song #3•Jazzman•2004','\
Gregory Porter•Water•Motéma•2011','\
Rachel Z Trio•On The Milky Way Express•Tone Center•2000','\
ETC (10)•ETC•Red Record•1990','\
Carlos Garnett•Black Love•Muse Records•1974','\
Famoudou Don Moye•Jam For Your Life•AECO Records•1985','\
Jeff "Tain" Watts•Megawatts•Sunnyside•1991'),'\
\
Black Orpheus\
':('\
The Brass Ring•California Dreamin\'•Dunhill•0','\
Sadayasu Fujii•Prelude To A Kiss•Nadja•1976','\
Vince Guaraldi•Live At El Matador•Fantasy•1966','\
Kunihiko Sugano•The Days Of Wine And Roses•Nadja•1976','\
Harry Edison•Seven Eleven•51 West•1979','\
Ramsey Lewis•Dancing In The Street•Cadet•1967','\
Kenny Barron Trio•Imo Live•Whynot•1983','\
Levon Ichkhanian•After Hours•Jazz Heritage Society•1996','\
Masabumi Kikuchi Sextet•Matrix•VICTOR WORLD GROUP•1969','\
Dylan Cramer•All Night Long•Casa Records•1999'),'\
\
Blackberry Winter\
':('\
Keith Jarrett•Priceless Jazz Collection•GRP Records Inc.•1998','\
Various•Priceless Jazz Sampler 2•GRP•1998','\
Keith Jarrett•Bop-Be•ABC Impulse!•1978','\
Keith Jarrett•Best Of Keith Jarrett•ABC Records•1978','\
Keith Jarrett•Silence•GRP•1992','\
Dolly Dawn•Memories Of You•Dawn Records (12)•1981','\
Nicki Parrott•Winter Wonderland•Venus Records (5)•2012','\
Hilary Kole•Haunted Heart •Victor•2009','\
Marlena Shaw•Dangerous•Concord Jazz•1996','\
Eileen Farrell•Sings Alec Wilder•Reference Recordings•1990','\
Teddi King•Lovers & Losers•Audiophile (2)•1976','\
David Daniels (3)•A Quiet Thing (Songs For Voice And Guitar)•Virgin Classics•2003','\
Keith Jarrett•Mysteries - The Impulse Years 1975-1976•Impulse!•1996'),'\
\
Blame It On My Youth\
':('\
Chris Connor•Come Back To Sorrento / Blame It On My Youth•Bethlehem Records•1958','\
Gary Burton Quartet•Easy As Pie•ECM Records•1981','\
The George Shearing Quintet•Burnished Brass - Part 1•Capitol Records•1958','\
The Nat King Cole Trio•After Midnight Part 4•Capitol Records•1957','\
The New Sound Quartet•Summertime•no label•2005','\
Keith Jarrett•The Melody At Night With You•ECM Records•1999','\
The Super Jazz Trio•Something Tasty•Baystate•1979','\
Stefan Pasborg•Live At SMK•ILK Music•2014','\
Art Farmer Quintet•Blame It On My Youth•Contemporary Records•1988','\
Sebastian Böhlen Quartet•Miscela•Laika Records•2014','\
Bob Wilber•New Clarinet In Town•Classic Editions•1960','\
Manhattan Trinity•Love Letters•M & I•2001','\
Keith Jarrett Trio•The Cure•ECM Records•1991','\
Ken Peplowski•Double Exposure•Concord Jazz•1988','\
Sidsel Storm•Sidsel Storm•Calibrated•2008'),'\
\
Blessed Relief\
':('\
The Muffin Men•Muffin Men•Muffin Records•1993','\
The Mothers•The Grand Wazoo•Bizarre Records•1972','\
Stefano Bollani•Sheik Yer Zappa•Decca•2014','\
Frank Zappa•Wazoo Joe\'s Domage•Vaulternative Records (2)•2008','\
Marco Pacassoni Group•Frank & Ruth•Esordisco•2018','\
Frank Zappa•Clean American Version •Rykodisc•1995','\
Frank Zappa•Joe\'s Domage•Vaulternative Records•2004'),'\
\
Blizzard of Lies\
':('\
Maria Muldaur•Transblucency•Uptown Records (2)•1986','\
Dave Frishberg•Live At Vine Street•Fantasy•1985','\
Shaynee Rainbolt•At Home •33 Records•2006','\
Susannah McCorkle•How Do You Keep The Music Playing?•PA USA•1985'),'\
\
Bloomdido\
':('\
Charlie Parker And His Orchestra•Bloomdido / Melancholy Baby•Mercury•1950','\
The Phil Woods Quartet•Live Volume One•Clean Cuts•1980','\
Didier Malherbe•Melodic Destiny•ottersongs•1981','\
Bird (28)•Bird And Diz•Mercury•1952','\
Christopher Hollyday•Christopher Hollyday•Novus•1989','\
Gary Bartz Quintet•Libra•Milestone (4)•1968','\
Phil Woods•Crazy Horse•Atlas Record (2)•1980','\
Hank Jones•Bop Redux•Muse Records•1977','\
Ron Carter•In A Jazz Tradition•EmArcy•1988','\
Per Husby Septett•Peacemaker•Studentersamfundets Plateselskap•1977','\
Charlie Parker•The Essential Charlie Parker•no label•1961','\
Hank Jones Trio•Hank Jones Trio With Mads Vinding & Al Foster•Storyville•1991','\
Charlie Parker•Talkin\' Bird•Verve Records•1999','\
Supersax•Supersax & L.A. Voices Volume 2•CBS•1984','\
Various•Our Best•Clef Records•1955','\
Akira Ohmori•Trust In Blue•Denon•1988'),'\
\
Blue A La Mode\
':('\
Message (9)•The Art Of Blakey•King Record Co. Ltd•1993','\
Howard Lucraft•Showcase For Modern Jazz•Decca•0','\
Joe Henderson•The Blue Note Years•Blue Note•1993','\
Various•Cool Jazz - Third Stream•The Franklin Mint Record Society•1985','\
Sonny Stitt•Stitt\'s Bits: The Bebop Recordings 1949-1952•Prestige•2006','\
Joe Henderson•The Milestone Years•Milestone (4)•1994','\
Fats Waller & His Rhythm•The Last Years (1940-1943)•Bluebird (3)•1989','\
Claude Nougaro•L\'amour Sorcier•Mercury•2014','\
Various•100 Best Of Blue Note•EMI Music Belgium•2011'),'\
\
Blue And Sentimental\
':('\
Gene Ammons And His Band•Chabootie / Blue And Sentimental•Prestige•1951','\
Georgie Auld•Blue And Sentimental / Tenderly•Coral•1952','\
Count Basie Orchestra•Blue And Sentimental / Doggin\' Around •Decca•1938','\
Tommy Dorsey And His Orchestra•In A Sentimental Mood...•Decca•1956','\
Lynn Hope•Shockin\' / Blue And Sentimental•King Records (3)•1960','\
Erroll Garner•Blue And Sentimental / Pavanne•Atlantic•1950','\
Count Basie Orchestra•Blue And Sentimental / Oh Lady Be Good•Decca•1938','\
Mary Ann McCall•Melancholy Baby•Coral•1959','\
Sonny Stitt•Jazz At The Hi-Hat•Roost•1954','\
Count Basie Sextet•The Count Basie Sextet•Karusell•0','\
Buck Clayton•Jumpin\' At The Woodside•Columbia•1955','\
Count Basie•String Along With Basie•Roulette•0','\
Illinois Jacquet•Illinois Jacquet With Wild Bill Davis•Black And Blue•1973'),'\
\
Blue Bossa\
':('\
Richard Davis (2)•As One•Muse Records•1976','\
George Benson•Jazz On A Sunday Afternoon Vol. II•Accord (2)•1981','\
Boillat Therace Quintet•The Best Selection•KS Music•2001','\
Defunkt•Illusion•Hannibal Records•1982','\
Stuff Combe•Stuff Combe 5 + Percussion•M Records (3)•1974','\
Patrizia Scascitelli•Patrizia Scascitelli•Edizioni Di Cultura Popolare•1976','\
Art Farmer•What Happens ?...•Campi-Editore Recording•1968','\
The Birds Of Paradise (3)•Bossa Blue Port / Giggle Wiggle•Newman Records•1966','\
Marco Rizo•Bossa Nova - Brazilian Jazz•Somerset•1964','\
The Brasiléros•The Girl From Ipanema•Diplomat Records•0','\
Curtis Fuller•Curtis Fuller Meets Roma Jazz Trio•Timeless Records (3)•1987','\
Tete Montoliu Trio•Catalonian Nights Vol.1•SteepleChase•1981','\
Bobby McFerrin•Play•Blue Note•1992','\
Combojazz•No Speed•Electromantic Music•2005'),'\
\
Blue Comedy\
':('\
Cuong Vu 4-tet•Ballet - The Music Of Michael Gibbs•RareNoise Records•2017','\
Gary Burton Quartet•In Concert•RCA Victor•1968','\
Gary Burton•Gary Burton / Larry Coryell•RCA Victor•1977','\
Gary Burton•3 In Jazz•RCA Victor•1963','\
Gary Burton•Artist\'s Choice•Bluebird (3)•1987','\
Quintorigo•Opposites•Incipit Records•2019','\
Paul Whiteman•The Birth Of Rhapsody In Blue (Paul Whiteman\'s Historic Aeolian Hall Concert Of 1924)•Musicmasters•1986'),'\
\
Blue Daniel\
':('\
Rob McConnell & The Boss Brass•Tribute•Pausa Records•1981','\
Shelly Manne & His Men•At The Black Hawk Vol. 1•Contemporary Records•1960','\
Lloyd McNeill•Tanner Suite•ASHA Recording Co. Inc.•1969','\
Frank Rosolino•Jazz A Confronto 4•Horo Records•1973','\
The Cannonball Adderley Quintet•At The Lighthouse•Riverside Records•1960','\
The Cannonball Adderley Quintet•Paris 1960•Pablo Records•1997','\
Frank Rosolino And His Quartet•Frank Talks!•Storyville•1998','\
Gil Cuppini Quintet•What\'s New? Vol. 2•Meazzi Edizioni Discografiche•1961','\
Phineas Newborn Trio•The Newborn Touch•Contemporary Records•1966','\
Einar Iversen•Me And My Piano•NorDisc•1967'),'\
\
Blue Gardenia\
':('\
Nat King Cole•Blue Gardenia•Capitol Records•1953','\
Lee Morgan•Standards•Blue Note•1998','\
Eric Alexander Quartet•Lazy Afternoon - Gentle Ballads IV•Venus Records (5)•2009','\
Johnny Mathis•Call Me•Fontana•1961','\
Dexter Gordon•Landslide•Blue Note•1980','\
Houston Person•Why Not!•Muse Records•1991','\
Harold Vick•Commitment•Muse Records•1974','\
Echoes Of Swing•Blue Pepper•ACT (4)•2013','\
Paolo Fresu Quintet•Songlines / Night & Blue•Tǔk Music•2010','\
Nat King Cole•The Best Of Nat King Cole•Capitol Records•1960','\
Dinah Washington•For Those In Love•Emarcy•1955','\
Tito Puente•Blue Gardenia•LaserLight Digital•1993','\
Ran Blake•Film Noir•Arista Novus•1980'),'\
\
Blue In Green\
':('\
Wallace Roney•Verses•Muse Records•1987','\
Toots Thielemans And His American Band•"Do Not Leave Me"•Stash Records•0','\
Miles Davis•Sextet & Quintet •CBS•1989','\
Miles Davis•Kind Of Blue•Columbia•1959','\
Jeremy Taylor (9)•Reggae Interpretation Of Kind Of Blue•Secret Stash Records•2009','\
Art Farmer•Maiden Voyage•Interface (3)•1983'),'\
\
Blue Monk\
':('\
Thelonious Monk•Blue Monk•Bandstand•1987','\
Art Blakey & The Jazz Messengers•Blue Monk / Evidence •Atlantic•1960','\
Thelonious Monk Trio•Blue Monk / Bye-Ya•Prestige•1959','\
Thelonious Monk•Blue Monk•Jazz MasterWorks•1985','\
Charlie Rouse•Epistrophy - The Last Concert•Landmark Records (3)•1989','\
Thelonious Monk•European Tour•Denon•1985','\
Richard Davis (2)•As One•Muse Records•1976','\
Thelonious Monk•Blue Monk•Jazz Hour•1989','\
Thelonious Monk•Blue Monk•Jazz Hour•1989','\
Thelonious Monk•Thelonious Monk Plays•Prestige•1954','\
The Thelonious Monk Quartet•In Europe•Unique Jazz•0','\
Bennie Wallace•Live At The Public Theater•Enja Records•1978'),'\
\
Blue Moon\
':('\
Vaughn Monroe And His Orchestra•Blue Moon / Shine On Harvest Moon•RCA Victor•0','\
Ray Conniff And His Orchestra & Chorus•Honeycomb / Blue Moon•Columbia•1964','\
Teddy Tyle Quintet•Moon Shot•Golden Crest•1957','\
The Dave Brubeck Trio•Blue Moon / Tea For Two•Coronet (5)•1949','\
Duke Ellington Quintet•Blue Moon / Ultra Deluxe•Capitol Records•1954','\
Erroll Garner•Like It Is / Blue Moon•MGM Records•0','\
The Dave Brubeck Quartet•The Brubeck Quartet At Storyville•Fantasy•1953','\
Ivory Joe Hunter•Blue Moon / U Name It•MGM Records•1951','\
Oscar-Gautschi-Quintett•Dance Time Vol.1•Polydor•1955','\
Klaus Wunderlich•Swing Again•Telefunken•1962','\
Santo & Johnny•Blue Moon / Summertime•Canadian American Records Ltd.•0','\
Cozy Cole All Stars•Just One More Chance / Blue Moon•Keynote Recordings (2)•1944','\
Red Norvo Sextet•Red\'s Rose Room - Red\'s Blue Room•"X"•1955'),'\
\
Blue Room\
':('\
Red Norvo Sextet•Red\'s Rose Room - Red\'s Blue Room•"X"•1955','\
Miles Davis And His Band•Morpheus / Blue Room•Prestige•1951','\
Miles Davis•Blue Period•Prestige•1953','\
Flip Phillips Quartet•Lover / Blue Room•Mercury•0','\
Thad Jones•Detroit-New York Junction•Blue Note•1956','\
no artist•Blue Room / Milenberg Joys•Bluebird (3)•1934','\
Red Norvo•Just A Mood The Red Norvo Small Bands•Bluebird (3)•1987','\
The Miles Davis Sextet•Blue Miles•Esquire•1961','\
Michel Sardaby•Blue Sunset•Disques Debs•1967','\
Muggsy Spanier•Dixieland Jamboree•Mercury•1956','\
Tommy Dorsey And His Orchestra•Liza Jane / The Blue Room•Decca•1954'),'\
\
Blue Seven\
':('\
Patrizia Scascitelli•Patrizia Scascitelli•Edizioni Di Cultura Popolare•1976','\
Berndt Egerbladh•Plays The Organ With A Swing•Nashville Records•1968','\
Junko Onishi Trio•Cruisin\'•no label•1993','\
Various•Jazz For A Lazy Day•Jazz Heritage•1999','\
Sonny Rollins•Saxophone Colossus•Prestige•1957'),'\
\
Blue Silver\
':('\
Anita Bryant•Silver And Blue•Columbia•1968','\
Al Cohn•Silver Blue•Xanadu Records•1977','\
Rob McConnell & The Boss Brass•Tribute•Pausa Records•1981','\
Dexter Gordon•The Comeback•Jazz Row•2008','\
The Harold Land / Blue Mitchell Quintet•Mapenzi•Concord Jazz•1977','\
The Horace Silver Quintet•The Jody Grind•Blue Note•1967','\
Victor Silvester And His Ballroom Orchestra•Dance Encores•Columbia•0','\
Della Reese•Yes Indeed / Blue And Orange Birds•Great Lakes (3)•1954','\
Horace Silver•Jazz Profile: Horace Silver•Blue Note•1997','\
Both Hands Free•Both Hands Free•Kemp / Pegrum Music Ltd.•1976','\
European Tuba Quartet•Heavy Metal - Light Industry•FMP•1989','\
Paolo Fresu Quintet•Songlines / Night & Blue•Tǔk Music•2010','\
Kokomo Wellington•Whispering Jazz•King Records (3)•0','\
Paul Murphy•The Return Of Jazz Club•BGP Records•2014','\
Bob Wills & His Texas Playboys•Texas Playboy Rag / Silver Dew On The Blue Grass Tonight•Columbia•1945','\
David Poe•David Poe•550 Music•1997','\
Arnold Sterling•Here\'s Brother Sterling•Polystar Co.','Ltd.•1992','\
Gonzalo Rubalcaba•The Blessing•no label•1991','\
Glen Velez•Assyrian Rose•CMP Records•1989'),'\
\
Blue Spirits\
':('\
Klaus Ignatzek Group•Live At Leverkusener Jazztage•NABEL•1987','\
Freddie Hubbard•Blue Spirits•Blue Note•1965','\
Mary Lou Williams Trio•Free Spirits•SteepleChase•1976','\
John Shaw (4)•Spirits Fly With The Wind•Aisha Records•1984','\
Enrico Rava Quintet•Andanada•Soul Note•1983','\
Jean-Luc Ponty•No Absolute Time•Atlantic Jazz•1993','\
Various•Blue Note Trip - Jazzanova - Lookin\' Back•Blue Note•2005','\
Roland Kirk•Volunteered Slavery•Atlantic•1969','\
Various•Spiritual Jazz Vol.9 - Blue Notes Parts I & II•Jazzman•2019'),'\
\
Blue Train\
':('\
John Coltrane•Blue Train•Blue Note•1957','\
John Coltrane Quintet•The Complete Paris Concerts•Magnetic Records (6)•1991','\
John Coltrane•Coltranology•BYG Records•1973','\
Bo Wärmell•Blue Train/Rue Chaptal•Jazz Records (2)•1962','\
The John Coltrane Sextet•Jazz Club Collection Vol 6•United Artists Records•1975','\
John Coltrane•Blue Train•Blue Note•2008'),'\
\
Blue Tuesday\
':('\
The Jimmy Bruno Group•Midnight Blue•Concord Jazz•2001','\
Allotria Jazzband München•Flat Foot•Elite Special•1983','\
Count Basie•Basie\'s Back In Town•Philips•0','\
Count Basie Orchestra•Basie\'s Back In Town•Epic•1955','\
Ichiko Hashimoto•High Excentrique•Polydor•1988','\
The Chico Hamilton Quintet•Gongs East!•Warner Bros. Records•1959','\
Jules Deelder•Jazz•Butler Records (3)•2018','\
The Orphan Newsboys•Laughing At Life•Stomp Off Records•1991','\
Orchester Frank Valdor•Tanzparty Bei Frankie•Europa•0','\
Various•Blues & Polar•Blue Note•1999','\
Eugene Chadbourne•The Lost Eddie Chatterbox Session•Not On Label (Eugene Chadbourne Self-Released)•1977','\
Various•Dancing To The Bands Again•Music For Pleasure•1994'),'\
\
Blues By Five\
':('\
Budd Johnson•Blues A La Mode•Felsted•1958','\
McCoy Tyner•The Real McCoy•Blue Note•1967','\
Miles Davis•Bluing: Miles Davis Plays The Blues•Prestige•1996'),'\
\
Blues Connotation\
':('\
Robben Ford•Blues Connotation•ITM Pacific•1997','\
Allan Praskin Quartet•Encounter•Three Blind Mice•1971','\
Buddy DeFranco•Blues Bag•Vee Jay Records•1965','\
Chick Corea•The Beginning•LaserLight Digital•1996','\
Bobby McFerrin•Play•Blue Note•1992','\
Ernst-Ludwig Petrowsky Quartett•SelbViert•FMP•1980','\
Ornette Coleman•The Best Of Ornette Coleman•Atlantic•1970'),'\
\
Blues For Alice\
':('\
Al Haig•Reminiscence•Progressive Records (2)•1977','\
Mark Whitfield•True Blue•Verve Records•1994','\
Carsten Meinert Kvartet•To You•M. S. Records•1968','\
George Otsuka Trio•Page 1•Takt Jazz Series•1967','\
Archie Shepp•Looking At Bird•SteepleChase•1981','\
Supersax•Dynamite !!•MPS Records•1979','\
Charlie Parker•Bird - The Original Recordings Of Charlie Parker•Verve Records•1988','\
Al Haig-Jimmy Raney Quartet•Special Brew•Spotlite Records•1976','\
Joseph Jarman•Inheritance•Baybridge Records•1984','\
Charlie Parker•The Magnificent Charlie Parker•Clef Records•1955'),'\
\
Blues For Philly Joe\
':('\
Sonny Rollins•Newk\'s Time•Blue Note•1959','\
Sonny Rollins•Jazz Profile: Sonny Rollins•Blue Note•1998','\
Jimmy Smith•5 Original Albums•Blue Note•2018'),'\
\
Blues For Wood\
':('\
Carter Jefferson•The Rise Of Atlantis•Timeless Records (3)•1979','\
Peter Leitch Quintet•Portraits And Dedications•Criss Cross Jazz•1989','\
Woody Shaw•United•Columbia•1981','\
Volker Kriegel•With A Little Help From My Friends•Liberty•1968','\
Buddy Rich Big Band•The Best Of Buddy Rich•World Pacific Jazz•1969','\
Woody Herman And His Orchestra•Rhapsody In Wood•First Heard Records•1979','\
Jamey Aebersold•For You To Play... Woody Shaw Eight Classic Jazz Originals•JA Records•1976','\
Oscar Klein•Pickin\' The Blues•Metronome•1974','\
Hardin & York•The World\'s Smallest Big Band•Bell Records•1970','\
Various•Freedom Time•Counterpoint Records•1997','\
Buddy Rich•Mr Drums: Buddy Rich & His Band Live On King Street•Cafe Records•1986','\
Phil Upchurch•Love Is Strange•Go Jazz•1995','\
Buddy Rich•Best Of Buddy Rich•Liberty•1970','\
Martin Mull•Normal•Capricorn Records•1974'),'\
\
Blues For Yna Yna\
':('\
Gerald Wilson Orchestra•New York New Sound•Mack Avenue•2003','\
Gerald Wilson Orchestra•You Better Believe It!•Pacific Jazz•1961','\
Les McCann•Jazz Waltz•Pacific Jazz•1963','\
Gerald Wilson Orchestra•The Best Of The Gerald Wilson Orchestra•World Pacific Jazz•1970','\
The Norman Amadio Trio•The Norman Amadio Trio•Canadian Talent Library•0','\
Gildo Mahones•The Great Gildo / Soulful Piano•Prestige•1964','\
Various•All Jazz•Fontana•0'),'\
\
Blues In the Closet\
':('\
The Tritones (2)•Sweet And Lovely / Blues In The Closet•Jamie•1957','\
The Oscar Pettiford Quartet•Mr. Pettiford\'s Convalescence•Bertelsmann Schallplattenring•1959','\
James Moody And His Band•Blues In The Closet / Nobody Knows (The Trouble I\'ve Seen)•Prestige•1955','\
Various•Session In Brass•Session•1970','\
Red Garland•Alone With The Blues•Moodsville•1960','\
The Bud Powell Trio•At The Golden Circle Volume 2•SteepleChase•1978','\
Duke Jordan Trio•The Great Session•Steeplechase•1981','\
Red Garland•Lil\' Darlin\'•Status Records (2)•1965','\
Oscar Pettiford•The Legendary Oscar Pettiford•Black Lion Records•1975','\
Kenny Drew•In Concert•SteepleChase•1979','\
Sunao Wada Quartet•Blues-Blues-Blues•Three Blind Mice•1977','\
Kenny Drew•In Concert•SteepleChase•1979','\
Sunao Wada Quartet•Blues-Blues-Blues•Three Blind Mice•1977','\
The Master Trio•Blues In The Closet•Baybridge Records•1984','\
The Kenny Drew Trio•At The Brewhouse•Idem Home Video•2002','\
Jimmy Giuffre•IAI Festival•Improvising Artists Inc.•1978','\
Chet Baker•Chet Is Back!•RCA•1978','\
The Bud Powell Trio•At The Golden Circle Volume 4•SteepleChase•1980','\
Christian Escoude / Pierre Michelot Quartet•Live At The Village Vanguard 1991•Emarcy•1991','\
Toots Thielemans•Live In The Netherlands•Pablo Live•1982','\
no artist•Vinnie Burke\'s String Jazz Quartet•ABC-Paramount•1957','\
Chet Baker•The Italian Sessions•RCA•1990','\
Herbie Mann•My Kinda Groove•Atlantic•1965','\
Oscar Pettiford•Germany 1958/1959•Jazzhaus•2013','\
Dusko Goykovich•Celebration•Hot House Records (2)•1987','\
The Walter Bishop Jr. Trio•Speak Low•Jazztime•1961'),'\
\
Blues In The Night\
':('\
Jimmy Smith•The Cat•Verve Records•0','\
Frank Sinatra•Ebb Tide •Capitol Records•1959','\
Jimmie Lunceford And His Orchestra•Blues In The Night•Decca•1942','\
Max Roach•Drummin\' The Blues•Liberty•1958','\
Harry James And His Orchestra•Crazy Rhythm / Blues In The Night•Parlophone•1945','\
Illinois Jacquet And His Orchestra•Blues In The Night / What\'s The Riff•Mercury•1953','\
Various•Something New Something Blue•Columbia•1959','\
Benny Goodman Sextet•Blues In The Night / Where Or When•Okeh•1942','\
Rosemary Clooney•Blues In The Night•Columbia•1953','\
Dinah Shore•Blues In The Night / Sometimes•Bluebird (3)•1942','\
Nellie Lutcher•Blues In The Night / Breezin\' Along With The Breeze•Decca•0','\
Randy Weston•Self Portraits. The Last Day•Verve Records•1990','\
101 Strings•Rhapsody In Blue•Mode Disques•0','\
Mark Murphy•That\'s How I Love The Blues•Riverside Records•1963','\
Frank Sinatra•Sings For Only The Lonely•Capitol Records•1958','\
Al Grey•Night Song•Argo (6)•1963','\
Bobby Hackett•Blues With A Kick•Capitol Records•1959','\
Tommy Wills•Tommy\'s Dream•Gregory Records•1962','\
Les & Larry Elgart•My Heart Belongs To Daddy / Blues In The Night•Columbia•1964'),'\
\
Blues on the Corner\
':('\
McCoy Tyner•The Real McCoy•Blue Note•1967','\
Jeff Palmer•Ease On•AudioQuest Music•1993','\
Eddie Condon•The Spirit Of Condon•no label•1973','\
Count Basie•Kansas City Shout•Pablo Records•1980','\
Chartbusters!•Volume 1•NYC Records•1995','\
McCoy Tyner Big Band•Journey•Verve Records•1993','\
Kirk Lightsey Quartet•First Affairs•Lime Tree•1987'),'\
\
Bluesette\
':('\
Toots Thielemans•Bluesette / Duke\'s Place•ABC-Paramount•1964','\
Tony Mottola•Tequila•Project 3 Total Sound•1970','\
Toots Thielemans•Bluesette / The Mountain Whistler•ABC-Paramount•1963','\
no artist•Bluesette / Brand New Morning•Cadet•1968','\
Sarah Vaughan•Bluesette / You Got It Made•Mercury•1964','\
Charles Earland•Mama Roots•Muse Records•1978','\
André Kostelanetz And His Orchestra•The Fall Of Love•CBS•1964','\
Christian Escoude Octet•Gipsy Waltz•Mercury•1989','\
Toots Thielemans•Ne Me Quitte Pas•Milan•1987','\
Phil Seamen Trio•Phil Seamen Meets Eddie Gomez•Saga (5)•1968','\
Force (26)•Second Force•Trio Records•1981','\
Pori Big Band•Pori Jazz 80•Pori Jazz Productions•1980','\
Toots Thielemans•Toots•Metronome•1963'),'\
\
Body and Soul\
':('\
Jazz At The Philharmonic•Norman Granz\' Jazz At The Philharmonic Vol.5•Mercury•1946','\
Tony Bennett•Body And Soul•Columbia•2011','\
Thelonious Monk•Live! At The Village Gate•Xanadu Records•1985','\
Eddie Jefferson•Body And Soul•Triumph Records (7)•1959','\
Lester Young Trio•Body And Soul / Indiana•Philo Recordings•1942','\
Archie Shepp•Body And Soul•Horo Records•1978','\
Coleman Hawkins And His Orchestra•Body And Soul•RCA•0','\
Tex Beneke•Body and Soul / Stormy Weather•RCA Victor•1947','\
Coleman Hawkins And His Orchestra•Body And Soul / Fine Dinner•Bluebird (3)•1940','\
Benny Goodman Trio•Body And Soul / After You\'ve Gone•Victor•1935','\
Sarah Vaughan•Body And Soul / When We\'re Alone•Parlophone•1947'),'\
\
Body And Soul\
':('\
Jazz At The Philharmonic•Norman Granz\' Jazz At The Philharmonic Vol.5•Mercury•1946','\
Tony Bennett•Body And Soul•Columbia•2011','\
Thelonious Monk•Live! At The Village Gate•Xanadu Records•1985','\
Eddie Jefferson•Body And Soul•Triumph Records (7)•1959','\
Lester Young Trio•Body And Soul / Indiana•Philo Recordings•1942','\
Archie Shepp•Body And Soul•Horo Records•1978','\
Coleman Hawkins And His Orchestra•Body And Soul•RCA•0','\
Tex Beneke•Body and Soul / Stormy Weather•RCA Victor•1947','\
Coleman Hawkins And His Orchestra•Body And Soul / Fine Dinner•Bluebird (3)•1940','\
Benny Goodman Trio•Body And Soul / After You\'ve Gone•Victor•1935','\
Sarah Vaughan•Body And Soul / When We\'re Alone•Parlophone•1947'),'\
\
Bohemia After Dark\
':('\
The Diamond Five•Poll Winners Jazz•Fontana•1961','\
Clifford Jordan•Hello Hank Jones•Eastworld•1978','\
Cannonball Adderley•A Day With Cannonball Adderley 1963•Baybridge Records•1982','\
Cannonball Adderley•The Sextet•Milestone (4)•1982','\
Eddy Louiss•Orgue Vol. 2•America Records•1973','\
Cannonball Adderley Sextet•Lugano 1963•TCB Records (2)•1995'),'\
\
Bolivia\
':('\
Victor Silvester And His Silver Strings•Voodoo Rhythm•Columbia•1953','\
The Ulf Sandberg Quartet•Ulf Sandberg Quartet•Acid Jazz•1993','\
Gato Barbieri•Bolivia•Flying Dutchman•1973','\
Doug Raney Quintet•I\'ll Close My Eyes•SteepleChase•1982','\
Freddie Hubbard•At Jazz Jamboree Warszawa \'91 - A Tribute To Miles•no label•1991','\
Freddie Hubbard•Bolivia•Musicmasters•1991','\
Cedar Walton Quartet•Third Set•SteepleChase•1983','\
Monty Alexander•Saturday Night•Limetree Records•1988'),'\
\
Boogie Down\
':('\
Lovekrauts•Boogie Street•Alternation (2)•1995','\
The Will Bradley-Johnny Guarnieri Band•Live Echoes Of The Best In Big Band Boogie•RCA Victor•1960','\
Various•A Decca Presentation Of Boogie Woogie Music•Decca•1940','\
Rob Agerbeek•The Boogie Rocks•Oldie Blues•1975','\
Sugar Chile Robinson•Go Boy Go•Oldie Blues•1980','\
Various•Boogie Blues (Women Sing & Play Boogie Woogie)•Rosetta Records•1983','\
Various•Boogie Woogie Greatest Hits•Boogie Woogie•0','\
East Bay Rhythm•A Little Love Will Help•7 Bridges Recordings•2001','\
Mr. Confuse•Boogie Down EP•Confunktion Records•2014','\
Main Stream Power Band•Swing Is Here•MWM Records München•1976','\
Various•Organ Boogie Woogie•Suzy•1983','\
Various•R&B And Boogie Woogie Volume 2 "Hey Lawdy" •Swing House Records•1982','\
Will Bradley And His Orchestra•Boogie-Woogie•Epic•1954'),'\
\
Boogie Stop Shuffle\
':('\
The Chris Potter Quartet•Lift - Live At The Village Vanguard•Sunnyside•2004','\
Gil Evans•Live 1986 - Unissued•Musica Jazz•1994','\
Alexander von Schlippenbach•Live At Café Amores•NoBusiness Records•2018','\
Kyle Eastwood•In Transit•Jazz Village•2017','\
Mingus Dynasty•Chair In The Sky•Elektra•1979','\
Arne Domnérus Orkester•Arne Domnérus•Metronome•1961','\
Roberto Ottaviano Six Mobiles•Mingus: Portrait In Six Colours•Splasc(h) Records•1988','\
New York Ska-Jazz Ensemble•Step Foward•Brixton Records•2008','\
Kevin Mahogany•Pussy Cat Dues "The Music Of Charles Mingus"•Enja Records•2000','\
Jerry Granelli•Dance Hall•Justin Time•2018'),'\
\
Booker\'s Waltz\
':('\
Klaus Ignatzek Quintet•Silent Horns•Candid•1995'),'\
\
Boplicity\
':('\
Miles Davis And His Orchestra•Boplicity / Israel•Capitol Records•1949','\
Miles Davis•Classics In Jazz Part 3•Capitol Records•0','\
Various•Cool And Quiet•Capitol Records•1953','\
Franco Cerri•International Jazz Meeting•Columbia•1961','\
Miles Davis•Birth Of The Cool•Capitol Records•1957','\
Karl Ratzer•Happy Floating•Rst Records•1994'),'\
\
Born To Be Blue\
':('\
Helen Merrill•Helen Merrill•EmArcy•1954','\
Mildred Bailey•Mildred Bailey Sings•Royale•1951','\
Freddie Hubbard And His Orchestra•Born To Be Blue•Pablo Records•1982','\
Dexter Gordon Trio•Lullaby For A Monster•SteepleChase•1981','\
Helen Merrill•Helen Merrill•EmArcy•1955','\
Helen Merrill•Helen Merrill•EmArcy•2014','\
Freddie Hubbard•The Best Of Freddie Hubbard Live And In Studio•Pablo Records•1983','\
Wynton Kelly•New Faces–New Sounds•Blue Note•1953','\
Gene Ammons•Twisting The Jug•Prestige•1962','\
Tommy Flanagan Trio•The Tommy Flanagan Trio•Prestige•1960'),'\
\
Boston Marathon\
':('\
Gary Burton•Good Vibes•Atlantic•1970'),'\
\
Both Sides of the Coin\
':('\
Steps Ahead•Steps Ahead•Elektra Musician•1983','\
Steps Ahead•In Europe•Idem Home Video•2002'),'\
\
Bouncing With Bud\
':('\
no artist•Bouncing With Bud / Wail•Blue Note•0','\
The Claude Williamson Trio•Kenton Jazz Presents Claude Williamson•Capitol Records•1954','\
René Urtreger•Joue Bud Powell•Barclay•1955','\
no artist•Bouncing With Bud•Vogue Productions•1955','\
Art Blakey•Blakey In Paris•Epic•1961','\
Al Haig•A Portrait Of Bud Powell•Interplay Records•1978','\
Charles McPherson•Live In Tokyo•Xanadu Records•1976','\
David Hazeltine Trio•Cleopatra\'s Dream•Venus Records (5)•2006','\
Bud Powell•Alternate Takes•Blue Note•1985','\
Hank Mobley•Mobley\'s Message•Prestige•1956','\
Pepper Adams Quartet•Ephemera•Zim Records•1974','\
Bud Shank•This Bud\'s For You...•Muse Records•1985'),'\
\
Boy Next Door\
':('\
Kai Winding Quartet•Jay And Kai•London Records•1956','\
Martha Raye•Lotus Land / The Boy Next Door•Discovery Records•1949','\
George Van Eps•Blue Guitar•Philips•0','\
The Jimmy Giuffre 4•Ad Lib•Verve Records•1960','\
The Johnny Griffin Quartet•Johnny Griffin•Argo (6)•1958','\
Jimmy Giuffre•Olympia 23 Fevrier 1960 - 27 Fevrier 1965•Trema•1999','\
Johnny Griffin•Introducing Johnny Griffin•Blue Note•1956','\
Martha Raye•The Voice Of Martha Raye•Discovery Records•1950','\
Kai Winding•Lionel Hampton Presents: Kai Winding•no label•1977','\
Lars Gullin Quartet•New Sounds From Europe - Vol. 3 Sweden•Vogue Records•1953'),'\
\
Brainville\
':('\
Sun Ra•Jazz By Sun Ra Vol. 1•Transition•1957','\
Quin Kirchner•The Other Side Of Time•Astral Spirits•2018','\
Sun Ra•Four Classic Albums Plus Bonus Singles•Real Gone•2012'),'\
\
Breakfast Wine\
':('\
Lomax / Wrigley•Lord Of An Unerring Bow•Oro Neese•2000','\
Jack Wilson•Plays Brazilian Mancini•Vault•1965','\
Sandvika Storband•Come Rain Or Come Shine•SS (4)•1989','\
Henry Mancini•As Mùsicas de Henry Mancini Em Bossa Nova•CID•0','\
Salvagnini Quartet•Mancini Dry•Velut Luna•2002','\
The Starlight Woodwinds•The Love Album•Columbia•0','\
Henry Mancini•The Very Best Of Henry Mancini•RCA•1981','\
Various•Academy Award Winning Songs•no label•1970','\
Erich Kunzel•Mancini\'s Greatest Hits•Telarc•1989','\
Shirley Bassey•12 Of Those Songs•Columbia•1968','\
Henry Mancini•Moon River: The Best Of Henry Mancini•Camden•2009','\
Henry Mancini•Grand Collection•Квадро-Диск•2004','\
Henry Mancini•The Best Of Henry Mancini•Camden•1997','\
Barney Kessel•Breakfast At Tiffany\'s ˙/ Bossa Nova / Contemporary Latin Rhythms•Collectables•2002','\
Julie London•The End Of The World / Nice Girls Don\'t Stay For Breakfast•EMI•1997','\
Shirley Bassey•Shirley Bassey•EMI•1993','\
Shirley Bassey•I\'m In The Mood For Love•Music For Pleasure•1981','\
Longines Orchestra•100 Golden Hits Vol. II•Longines Symphonette Society•0'),'\
\
Brian\'s Song\
':('\
Jacinta (2)•Songs Of Freedom•EMI Music Portugal•2009','\
Various•Stereo Spectacular•no label•1975'),'\
\
Bright Boy\
':('\
Wardell Gray•Los Angeles All Stars•Prestige•1953','\
Wardell Gray•Memorial Volume 2•Prestige•1955','\
Cannonball Adderley•Cannonball Adderley-Live!•Capitol Records•1965','\
Gerry Mulligan Quartet•The Shadow Of Your Smile•Moon Records (4)•1989','\
Charquet & Co•Sharkey & Co•Association Française Des Amateurs De Jazz Nouvelle Orléans•1969','\
Allen Toussaint•The Bright Mississippi•Nonesuch•2009','\
Susan Osborn•Susan•Golden Throat Recordings•1987','\
Various•Rare And Hot ! 1925-1930•Historical Records•1967','\
Various•Sounds Of The Seasons•MCA Records•1988','\
Casey Abrams•Casey Abrams•Concord Records•2012','\
Wardell Gray•Memorial Album•Prestige•1965','\
Adrian Brett•Sentimental Dreams•K-Tel•1982','\
Al Caiola•Sound Of Christmas•United Artists Records•1967','\
Wardell Gray•Central Avenue•Prestige•1976'),'\
\
Bright Moments\
':('\
Andy Sheppard•Bright Moments•Island Records•1990','\
Admin•Spirit Boogie•Omena LTD•2016','\
Max Roach Double Quartet•Bright Moments•Soul Note•1987','\
Lonnie Liston Smith•The Best Of Lonnie Liston Smith•Columbia•1980','\
Roland Kirk•Bright Moments•Atlantic•1973','\
Lonnie Liston Smith•Loveland•Columbia•1978','\
Grover Washington Jr.•Skylarkin\'•Motown•1980','\
Steve Turre•The Music Of Rahsaan Roland Kirk•Stash Records Inc.•1986'),'\
\
Bright Size Life\
':('\
Martin Taylor•Triple Libra•Wave (4)•1981','\
Pat Metheny•Bright Size Life•ECM Records•1976','\
Pat Metheny•Selected Recordings•ECM Records•0','\
Pat Metheny•The Gathering Sky•All Stars (8)•2006','\
Pat Metheny•Trio → Live•Warner Bros. Records•2000','\
Jaco Pastorius•The Essential Jaco Pastorius•Epic•2007'),'\
\
Brilliant Corners\
':('\
Various•The New Wave In Jazz•Impulse!•1966','\
Anthony Braxton•Six Monk\'s Compositions (1987)•Black Saint•1988','\
Either/Orchestra•Dial E•Accurate Records•1986','\
Cecil Taylor•The New Breed•ABC Impulse!•1978','\
Floros Floridis•The Manager In Charge•J.n.d. Records•1987','\
Thelonious Monk•Greatest Hits•Riverside Records•1962','\
Thelonious Monk•Brilliant Corners•Riverside Records•1957','\
Thelonious Monk•Panorama•Riverside Records•1969'),'\
\
Broadway Blues\
':('\
Oliver Nelson•More Blues And The Abstract Truth•Impulse!•1964','\
Tsuyoshi Yamamoto Trio•Blues For Tee•Three Blind Mice•1975','\
Gerry Mulligan And His Sextet•Mainstream Of Jazz Vol. 2•Mercury•1984','\
The Earl Hines Trio•Hines & Eldridge•Mercury International•1965','\
Illinois Jacquet•Jacquet St.•Classic Jazz•1981','\
Jaco Pastorius•Blackbird•Alfa Jazz•1991','\
Illinois Jacquet•The Message•Argo (6)•1963','\
Earl Hines•Spotlight On Earl "Fatha" Hines And Buck Clayton•Tiara Records•0','\
Buddy Tate•Buddy Tate Et Wild Bill Davis•Black And Blue•0','\
Frank Wess•Opus De Blues•Savoy Jazz•1984','\
Ricky Ford•Ebony Rhapsody•Candid•1990'),'\
\
Brothers Of The Bottom Row\
':('\
Julian Joseph•The Language Of Truth•EastWest•1991'),'\
\
Brown Skin Girl\
':('\
Sonny Rollins•The Sound Of Sonny•Gateway Records•1977','\
Monty Alexander•Here Comes The Sun•MPS Records•1971','\
Roy Haynes•The Island•Explore Records•2007','\
Sonny Rollins•The Bridge / What’s New?•Not Now Music•2013','\
no artist•Now Hear This•Columbia•1957','\
Harumi Kaneko•I Love New York•Philips•1980','\
Kenya•My Own Skin•Expansion•2015','\
Phillip Lassiter•Philthy•GroundUP Music (2)•2014','\
Various•10th Anniversary New Orleans Jazz & Heritage Festival•Flying Fish (2)•1979','\
Ivy Pete And His Limbomaniacs•Limbo Party•Stereo-Fidelity•0','\
Frank Sinatra•The Voice•Reprise Records•1983','\
Harry Belafonte•Harry Belafonte & Miriam Makeba•RCA•1975'),'\
\
Brownout\
':('\
Gary Burton•The New Quartet•ECM Records•1973'),'\
\
B-String\
':('\
Muhal Richard Abrams•Spiral: Live At Montreux 1978•Novus•1978','\
Ted Heath And His Orchestra•The Ted Heath Orchestra Plays Beatles Bach & Bacharach•London Records•1969','\
John Dankworth•Johnny Dankworth / Billy Strayhorn•Roulette•1972','\
Johann Sebastian Bach•Basically Bach•Decca•1982','\
Stéphane Grappelli•We\'ve Got The World On A String•Angel Records•1982','\
David Rose & His Orchestra•Concert With A Beat•MGM Records•1961','\
Walter Steffens•Ecstasy•Labor•1975','\
Jacques Loussier Trio•The Best Of Play Bach•Telarc•2004','\
Dominic Miller•Shapes•Inversion Records•2003','\
Moondog (2)•Instrumental Music By Louis Hardin•Musical Heritage Society•1978','\
Todd Rundgren•Runddans•Smalltown Supersound•2015'),'\
\
Bud Powell\
':('\
Chick Corea & Friends•Remembering Bud Powell•Stretch Records•1997','\
Chick Corea & Friends•Remembering Bud Powell -Live•-Image Entertainment•1999','\
Chick Corea & Friends•Remembering Bud Powell -Live•-Image Entertainment•1999','\
Chick Corea•Live In Molde•MNJ Records•2005','\
The Bud Powell Trio•At The Golden Circle Volume 5•SteepleChase•1982','\
Jimmy Mosher Quintet•Satyric Horn•ITI Records•1984','\
Gary Burton / Chick Corea•Chick Corea & Gary Burton•TDK Mediactive•2004','\
Chucho Valdés•Live At The Village Vanguard•Blue Note•2000','\
Gary Burton / Chick Corea•In Concert Zürich October 28 1979•ECM Records•1980','\
Gary Burton / Chick Corea•The New Crystal Silence•Concord Records•2008','\
The John Dentz Reunion Band•December 5 & 6•M & K Realtime Records•1981','\
Zimbo Trio•Música Viva•Tom Brasil•1996'),'\
\
Budo\
':('\
Miles Davis•Budo / Move•Capitol Records•1949','\
Miles Davis•Junior Jazz Gallery•Philips•1960','\
The Miles Davis Quintet•Jazz Gallery•Philips•0','\
Miles Davis•Classics In Jazz Part 3•Capitol Records•0','\
Miles Davis & His Tuba Band•Pre-Birth Of The Cool•Durium•1974','\
Charlie Barnet•The Modern Idiom•Capitol Records•1952','\
Miles Davis•Jazz & Blues Collection•Editions Atlas•1995','\
Stan Getz Quintet•Jazz At Storyville Volume 2 •Royal Roost•1952','\
John Coltrane•Trane\'s Blues•Giants Of Jazz•1987','\
Miles Davis•The Complete Birth Of The Cool•Capitol Jazz•1998','\
Shorty Rogers•Yesterday Today And Forever•Concord Jazz•1983','\
The Miles Davis Quintet•Miles Davis Quintet•Giants Of Jazz•1986','\
Stan Getz•At Storyville - Vol. 2•Roost•1957','\
Miles Davis•Birth Of The Cool•Capitol Records•1957'),'\
\
Bud\'s Bubble\
':('\
Bud Powell•The Definitive•Blue Note•2002','\
The Bud Powell Trio•Bud•Roost•1958','\
Bud Powell•The Best Years•Roulette•0'),'\
\
Bunko\
':('\
Lennie Niehaus•Vol. 3: The Octet #2•Contemporary Records•1955'),'\
\
Bu\'s Delight\
':('\
Gabriel Latchin Trio•The Moon And I•ALYS JAZZ•2019'),'\
\
Buster Rides Again\
':('\
Medeski Martin & Wood•Tonic•Blue Note•2000','\
Bud Powell•The Amazing Bud Powell Vol. 4 - Time Waits•Blue Note•1958','\
Bud Powell•The Best Of Bud Powell•Blue Note•1989'),'\
\
But Beautiful\
':('\
Flip Phillips And His Orchestra•But Beautiful / Bright Blues•Mercury•0','\
Nat King Cole•But Beautiful / Look No Further•Capitol Records•1958','\
Mark Murphy•Mark Murphy - A Beautiful Friendship : Remembering Shirley Horn•Gearbox Records•2013','\
Art Pepper•Friday Night At The Village Vanguard•Contemporary Records•1980','\
Tex Beneke And His Orchestra•You Don\'t Have To Know The Language / But Beautiful•RCA Victor•1948','\
Art Pepper•Art Lives•Galaxy•1983','\
Shirley Bassey•Good Bad But Beautiful•United Artists Records•1975','\
The Michel Petrucciani Trio•Live At The Village Vanguard Volume 2•Video Artists International•1982','\
Art Pepper•Arthur\'s Blues•Original Jazz Classics•1991','\
The Peter King Quartet•Brother Bernard•Miles Music•1988','\
The Tubby Hayes Quintet•Down In The Village•Fontana•1963','\
Yasuko Agawa•L.A. Night•Invitation•1987','\
Hank Jones Trio•Arigato•Progressive Records (2)•1977','\
Teddy Edwards•Nothin\' But The Truth!•Prestige•1967'),'\
\
But Not For Me\
':('\
Miles Davis All Stars•But Not For Me•Prestige•1955','\
Ben Webster•Meets Bill Coleman•Black Lion Records•1989','\
Miles Davis•Miles Davis And The Modern Jazz Giants•Metronome•1958','\
The Oscar Peterson Trio•Rough Ridin\' / But Not For Me•Mercury•1952','\
Ahmad Jamal•Seleritus / But Not For Me •Parrot (2)•1954','\
Harry James And His Orchestra•The Mole / But Not For Me•Columbia•1942','\
Miles Davis•Bags Groove•Prestige•1957','\
Chet Baker•Strollin\'•Enja Records•1986','\
Miles Davis•Oleo•Prestige•1971','\
Ahmad Jamal Trio•But Not For Me•Argo (6)•1958'),'\
\
Butterfly\
':('\
The Oscar Peterson Trio•Poor Butterfly / Honeydripper•no label•0','\
Benny Goodman Sextet•The Sheik / Poor Butterfly•Columbia•1940','\
George Bishop•Like A Butterfly•Innovative Communication•1992','\
Benny Goodman And His Orchestra•Poor Butterfly / Hora Stacato•Columbia•0','\
Ahmad Jamal•Billy Boy / Poor Butterfly•Argo (6)•1960','\
[dunkelbunt]•Cinnamon Girl •Chat Chapeau Records•2008','\
Dick Stabile And His Orchestra•Poor Butterfly / Without A Song•Bethlehem Records•1958','\
The Oscar Peterson Trio•Sweet Georgia Brown / Poor Butterfly•no label•0','\
Reggie Msomi And His Jazz Africa•Soweto Grooving•Soul Jazz Pop•1976','\
The Kilimanjaro Darkjazz Ensemble•Black Wing Butterfly / Goya•Parallel Corners•2007','\
Donald Byrd & 125th Street N.Y.C.•Butterfly / I Feel Like Loving You Today•Elektra•1981'),'\
\
Bye Bye Blackbird\
':('\
Nick Lucas•Bye Bye Blackbird / Adorable•Brunswick•1926','\
John Coltrane•Bye Bye Blackbird•Pablo Live•1981','\
The Oscar Peterson Trio•Bye Bye Blackbird•Verve Records•1957','\
The Miles Davis Quintet•Davis\' Cup•Philips•1956','\
Bill Henderson (3)•Bye Bye Blackbird / Bad Luck•Vee Jay Records•1960','\
Miles Davis•Miles Tones•Jazz Bird•1980','\
John Coltrane•Favorites•Jazz Bird•1980','\
Dean Martin•Happy Feet / Bye Bye Blackbird•Capitol Records•1950','\
Keith Jarrett Trio•Bye Bye Blackbird•ECM Records•1993'),'\
\
Byrdlike\
':('\
Freddie Hubbard•Above And Beyond•Metropolitan•1999','\
Freddie Hubbard•Back To Birdland•M & K Realtime Records•1981','\
Freddie Hubbard•Rollin\'•MPS Records•1982','\
George Cables•Cables\' Vision•Contemporary Records•1980','\
The V.S.O.P. Quintet•The Quintet•Columbia•1977','\
The V.S.O.P. Quintet•V.S.O.P•CBS/Sony•1985','\
Tim Hagans•Hubsongs - The Music Of Freddie Hubbard•Blue Note•1998','\
Various•A Winning Season Of Jazz•Columbia•1977','\
Various•In Performance At The Playboy Jazz Festival•Elektra Musician•1984'),'\
\
Call For All Demons A\
':('\
The Sun Ra Arkestra•Angels And Demons At Play•El Saturn Records•1967','\
The Sun Ra Arkestra•Angels And Demons At Play / The Nubians Of Plutonia•Evidence (5)•1993','\
The Sun Ra Arkestra•Music From Tomorrow\'s World•Atavistic•2002','\
Xenat-Ra•Science For The Soundman•Not On Label•2012','\
Susanne Abbuehl•Compass•ECM Records•2006','\
Slagerij Van Kampen•Link•Solid (4)•1993','\
Sun Ra•Four Classic Albums Plus Bonus Singles•Real Gone•2012','\
Sun Ra•Singles (The Definitive 45\'s Collection 1952–1991)•Strut•2016','\
Sun Ra•Singles (The Definitive 45\'s Collection 1952–1991)•Strut•2016','\
Sun Ra•Singles Volume 1: The Definitive 45s Collection 1952-1961•Strut•2016'),'\
\
Canyon Song\
':('\
Stanley Clarke•The Rite Of Strings•Gai Saber•1995','\
Oregon•Distant Hills•Vanguard•1973','\
Paul Winter (2)•Canyon Lullaby•Living Music•1997','\
Oregon•Best Of The Vanguard Years•Vanguard•2000','\
Garrett List•The Unbearably Light•Records/Music For Treesasbl•1995','\
Al Di Meola•Live At Montreux 1994•Eagle Vision•2005','\
Paul Winter (2)•Wolf Eyes•Living Music•1988','\
Oregon•Our First Record•Vanguard Freestyle•1980','\
Paul Winter And Friends•Living Music Collection \'86•Living Music•1986','\
The String Cheese Incident•Outside Inside•SCI Fidelity Records•2001','\
Gabor Szabo•His Great Hits•Impulse!•1971','\
Oregon•The Essential Oregon•Vanguard•1981','\
Martin Böttcher•Winnetou Melodien•EastWest Records GmbH•1996'),'\
\
Capim\
':('\
The Manhattan Transfer•Brasil•Atlantic•1987','\
Ayumi Koketsu•O Pato•M & I•2018','\
Herbie Mann•Astral Island•Atlantic•1983','\
Filo Machado•Cantando Um Samba•Malandro Records•1999','\
The Manhattan Transfer•The Manhattan Transfer Anthology • Down In Birdland•Rhino Records (2)•1992'),'\
\
Captain Marvel\
':('\
Chick Corea•Chick Corea•Polydor•1987','\
Stan Getz•Captain Marvel•Columbia•1975','\
Chick Corea•Light As A Feather•Polydor•1973'),'\
\
Caravan\
':('\
Cozy Cole•Caravan•Grand Award Records•1959','\
The Cozy Cole Septet•Caravan•Felsted•1959','\
Dee Dee Bridgewater•Heartache Caravan•Polydor•1989','\
Duane Eddy•Caravan•Gregmark•1961','\
Mudd•Kerry\'s Caravan•Rong Music•2005','\
Bert Kaempfert & His Orchestra•Caravan•Decca•1967','\
Ralph Marterie And His Orchestra•Caravan / Pretend•Mercury•0','\
Duke Ellington And His Orchestra•Caravan / Solitude•RCA•0','\
Duke Ellington And His Orchestra•Caravan / Azure•Brunswick•1937','\
Benny Goodman And His Orchestra•Stardust / Caravan•Philips•0','\
Lenny Dee (2)•Caravan•Decca•1956','\
Freddie Brocksieper Quintett•Caravan / Cymbal Promenade •Brunswick•0','\
Reggae Clinic 65•Take Five / Caravan / Wheels•International Bestseller Company•1979','\
Lionel Hampton And His Orchestra•Advent / Caravan•Glad-Hamp Records•0','\
Barney Bigard And His Jazzopaters•Caravan / Stompy Jones•Vocalion (2)•1937','\
Ambrose & His Orchestra•Cotton Pickers Congregation / Caravan•Decca•1937','\
Joe Valino•Garden Of Eden / Caravan•Vik•1956','\
Gene Dersin Und Sein Orchester•One O\'Clock Jump / Caravan•Decca•1944','\
Ed Graham (2)•Hot Stix•M & K RealTime Records•1978','\
Joe Daniels And His Hot Shots•Santiago / Coon Town Caravan•Parlophone•1943'),'\
\
Careful\
':('\
Lars Gullin Quartet•Vol. 1•Metronome•1954','\
Bing Crosby•Happy Holiday / Be Careful It\'s My Heart•Brunswick•0','\
Lucky Millinder And His Orchestra•Please be Careful / Backslider\'s Ball •King Records (3)•1952','\
Bob Manning (2)•Honestly / I\'d Better Be Careful•Capitol Records•1955','\
no artist•Earth Angel / Step Careful Heart•MGM Records•1955','\
The Jimmy Giuffre Trio•Princess•Fini Jazz•1990','\
Michel Petrucciani•Power Of Three•Blue Note•1987','\
Eydie Gormé•Dormi-Dormi-Dormi / Be Careful It\'s My Heart•no label•1958','\
Gary Burton•Times Square•ECM Records•1978','\
Michel Petrucciani•Power Of Three – Live At Montreux•Pioneer LDCE Ltd.•1990','\
Jim Hall•Live At Town Hall Vol. 2•Musicmasters•1991','\
John Williams (5)•Williams Tell•EmArcy•1955','\
Gary Burton•Something\'s Coming!•RCA Victor•1964','\
Jim Hall•Jazz Impressions Of Japan•Paddle Wheel•1980'),'\
\
Careless Love\
':('\
The Hi-Fi Dixieland Kings•Wildcat Blues / Careless Love•Grammoclub Ex Libris•1960','\
Original Tuxedo Jazz Orchestra•Careless Love / Black Rag•Okeh•1925','\
Claude Luter & Son Jazz Band•Careless Love Blues / Pimlico•Swing (3)•1947','\
Sidney Bechet•Careless Love / Down Home Rag•Vogue Productions•0','\
Kid Ory And His Creole Jazz Band•Careless Love / Do What Ory Say•Crescent (6)•1945','\
Ray Charles•You Don\'t Know Me / Careless Love•ABC-Paramount•1962','\
no artist•Maryland My Maryland / Careless Love•Jazz Ltd.•1949','\
no artist•Winin\' Boy Blues / Careless Love•Blue Note•1946','\
The Dutch Swing College Band•Careless Love Blues / Doctor Jazz•Philips•1953','\
Kid Ory And His Creole Jazz Band•Do What Ory Said / Careless Love•Jazz Man (2)•0','\
Sidney Bechet•Careless Love•Vogue Productions•0','\
George Lewis And His New Orleans Stompers•Don\'t Go \'Way Nobody / Careless Love Blues•Climax Records (7)•0','\
Humphrey Lyttelton And His Band•When The Saints Go Marching In / Careless Love•Saturne•0'),'\
\
Casa Forte\
':('\
Flora Purim•Casa Forte•Milestone (4)•1974','\
Erik Escobar•New Samba Jazz•Altrisuoni•2006','\
Ira Kris Group•Jazzanova•MPS Records•1972','\
The North Texas State University Lab Band•Lab \'69•Century Records (4)•1969','\
Edu Lobo•Sergio Mendes Presents Lobo•A&M Records•1970','\
Peter Herbolzheimer Rhythm Combination & Brass•Latin Groove•Koala Records•1987','\
Helen Merrill•Casa Forte•Trio Records•1980'),'\
\
Catch Me\
':('\
Mr. Confuse•Catch Me•Confunktion Records•2014','\
Perry Como•Catch A Falling Star / Dream Along With Me•RCA Victor•1976','\
Lene Alexandra Øien•Try To Catch Me•Day 1 Entertainment•2012','\
Ray Mantilla Space Station•Dark Powers•Red Record•1989','\
Myriam Alter•Where Is There•Enja Records•2007','\
Curtis Amy•The Blues Message•Pacific Jazz•1960','\
Sylvia McNeill•That\'s Alright By Me / Catch A Robber By The Toe•RCA Victor•1969','\
Sonny Criss•I\'ll Catch The Sun!•Prestige•1969','\
The Neil Cowley Trio•Displaced•Hide Inside Records•2006','\
Dave Brubeck•A La Mode•Fantasy•1960','\
Kendrick Scott Oracle•We Are The Drum•Blue Note•2015','\
Udo Schild•Live At Kölner Philharmonie 1999•Meyer Records•2017','\
Andy Panayi Quartet•Blown Away•RSJH Music Limited•1998','\
Lyn Leon•Glass Lounge•Percords•2001','\
Mark Murphy•Mark Murphy\'s Hip Parade•Capitol Records•1960'),'\
\
Caught Up In The Rapture\
':('\
Anita Baker•Talk To Me•Elektra•1990','\
Steven Kindler•Across A Rainbow Sea•Global Pacific Records•1990','\
George Shaw•Let Yourself Go!•TBA Records & Tapes•1987','\
Anita Baker•Rapture•Elektra•1986','\
Calvin Brooks•A Smooth Flight•Brooks Burgess-Brooks Productions•1989','\
Pan Assembly•Midnight•Carotte•0','\
Various•Woman In Love Volume 8•Arcade•1987','\
Various•100 Hits Woman•100 Hits•2007'),'\
\
Central Park West\
':('\
The Odean Pope Saxophone Choir•Locked & Loaded (Live At The Blue Note)•Half Note Records Inc.•2006','\
John Coltrane•The Best Of John Coltrane•Atlantic•1970','\
Tommy Flanagan•Giant Steps (In Memory Of John Coltrane)•Enja Records•1988','\
Tommy Flanagan•Giant Steps (In Memory Of John Coltrane)•Enja Records•1982','\
John Coltrane•Coltrane\'s Sound•Atlantic•1964'),'\
\
Ceora\
':('\
Andrew Hill•Faces Of Hope•Soul Note•1980','\
Lee Morgan Quintet•Live At The Lighthouse \'70•Fresh Sound Records•1991','\
Lee Morgan•Live Sessions•Trip Jazz•1975','\
Lee Morgan•Lee Morgan•The Blue Note Label Group•2007','\
Lee Morgan•Cornbread•Blue Note•1967','\
Nueva Manteca•Varadero Blues•Timeless Records (3)•1989','\
Frank Morgan•Lament•Contemporary Records•1986','\
Lee Morgan•Memorial Album•Blue Note•1974','\
Bobby Watson (2)•Round Trip•Red Record•1987','\
Joey DeFrancesco•Live: The Authorized Bootleg•Concord Jazz•2007'),'\
\
C\'est What\
':('\
Nobuo Hara and His Sharps & Flats•My Fair Lady And Other Broadway Show Spectaculars•Festival Records•0','\
Helena Vondráčková•Kam Zmizel Ten Starý Song•Supraphon•1992'),'\
\
Chain of Fools\
':('\
Jimmy Brown (10)•Chain Of Fools / I Heard It Through The Grapevine•Abet•1968','\
Herbie Mann•Memphis Underground•Atlantic•1969','\
Julien Lourau Groove Gang•Groove Gang•Label Bleu•1995','\
Magnus Lindgren•Stockholm Undergound•ACT (4)•2017','\
Jimmy Smith•Plays The Hits•Verve Records•2010'),'\
\
Chairs And Children\
':('\
Gary Burton•Reunion•GRP•1990','\
Harry Belafonte•Play Me•RCA Victor•1973'),'\
\
Chameleon\
':('\
Stanley Jordan•Chameleon•Arista•1994','\
The Frank Cunimondo Trio•Sagittarius•Mondo (5)•1975','\
Lars Färnlöfs Orkester•The Chameleon•RCA Victor•1969','\
Herbie Hancock•Chameleon / Vein Melter•Columbia•1974','\
Lionel Hampton And His Jazz Inner Circle•Chameleon / Mister Sunshine•Glad-Hamp Records•0','\
Herbie Hancock•Watermelon Man / Chameleon•Columbia•1974','\
Herbie Hancock•Head Hunters•Columbia•1973','\
Monty Alexander•Unlimited Love - Live & In Concert•BASF•1976'),'\
\
Change of Mind\
':('\
Charles Earland•Charles III•Prestige•1973','\
Masaru Imada + Kenji Kohsei Quartet•All Of A Glow•Seven Seas•1978','\
Peter Erskine•Peter Erskine•Contemporary Records•1982','\
Defunkt•In America•Antilles•1988','\
Kathy Stobart•Arbeia•Spotlite Records•1978','\
T-Square•脚線美の誘惑 Kyakusenbi No Yuhwaku•CBS/Sony•1982','\
Charles Earland•Charles III•Prestige•1973','\
Warm Dust•Peace For Our Time Neville Chamberlain 30th September 1938•Trend (2)•1970','\
Johannes Enders•ZeitGeistMaschine•Laika Records•2015','\
Carmen McRae•Ms. Magic•Accord (2)•1982','\
Quincy Jones•Body Heat•A&M Records•1974'),'\
\
Charade\
':('\
Quartette Trés Bien•Charade•Decca•1964','\
Henry Mancini And His Orchestra•Charade•RCA Victor•1963','\
Sammy Kaye And His Orchestra•Charade•Brunswick•1964','\
Sammy Kaye And His Orchestra•Charade•Brunswick•1964','\
Greg Hatza•The Wizardry Of Greg Hatza•Coral•1967','\
Sahib Shihab•Sahib\'s Jazz Party•Debut Records (3)•1964','\
The Sensational Guitars Of Dan & Dale•Henry Mancini Favorites•Diplomat Records•0','\
Rudolph Statler Orchestra And Chorus•Henry Mancini Favorites•Wyncote•1964'),'\
\
Charmed Circle\
':('\
Cedar Walton•Animation•Columbia•1978'),'\
\
Chase\
':('\
Dexter Gordon•The Chase•Dial Records (3)•1947','\
The Camelots (2)•The Chase•Comet (5)•0','\
no artist•The Chase / The Duel•Jazztone (2)•0','\
Wardell Gray•The Chase And The Steeplechase•Decca•1952','\
Chuck Mangione•Chase The Clouds Away•A&M Records•1975','\
Die Musikwissenschaft•A Diminished Augmentation•Recycled Bird•2011','\
Lionel Hampton And His Sextet•Bouncing At The Beacon / Chasin\' With Chase•no label•0','\
Art Taylor•Taylor\'s Tenors•Metronome•1959','\
no artist•The Get Away And The Chase•Verve Records•0','\
Wardell Gray•The Chase•Giants Of Jazz•1990','\
The Buddy Brennan Quartet•Big River•Warwick•1959','\
Wardell Gray•The Chase And The Steeple Chase•MCA Records•1980'),'\
\
Chasin\' the Train\
':('\
The Oscar Pettiford Quartet•New Stars •- New Sounds Volume  2•Mercer Records•1951','\
Chick Corea Akoustic Band•Live From The Blue Note Tokyo•Stretch Records•1996','\
John Coltrane•Anthology•Il Sole 24 Ore•2011','\
Various•Texas: Black Country Dance Music 1927-1935•Document Records (2)•1993'),'\
\
Cheese Cake\
':('\
Dexter Gordon•The Squirrel •Blue Note•2001','\
Dexter Gordon Quartet•Cheese Cake•SteepleChase•1979','\
Manhattan Jazz Quintet•Plays Blue Note•Paddle Wheel•1988','\
Dexter Gordon•The Best Of Dexter Gordon•Blue Note•1988','\
Various•Blue Note 50th Anniversary Collection Volume 2 1956-1965 - The Jazz Message•Blue Note•1989','\
Paul Smith Quartet•Fine Sweet And Tasty•Tampa Records•1953','\
Paul Smith Quartet•Cocktail Hour•Tampa Records•1957','\
Dexter Gordon•Go!•Blue Note•1962'),'\
\
Chega De Saudade\
':('\
Various•Jazz Jamboree \'71 - Vol. 1•Polskie Nagrania Muza•1971','\
Klaus Doldinger Quartett•Bossa Nova •Philips•1962','\
Vinicius De Moraes•The Poet Of The Bossa Nova•New Continent•2017','\
Dizzy Gillespie Quintet•En Concert Avec Europe 1 - Olympia 24 Novembre • 1965•RTE•1994','\
Antonio Carlos Jobim•Brazil’s Greatest Composer•Jazz Images•2018','\
João Gilberto•Performance•EMI•1989','\
Maria Creuza•Yo...•Trova•1971'),'\
\
Chelsea Bells\
':('\
Gary Burton•Hotel Hello•ECM Records•1975','\
Gary Burton•Works•ECM Records•1984','\
Acker Bilk•London Is My Cup Of Tea•Studio 2 Stereo•1967','\
Duke Ellington•1969 All-Star White House Tribute•Blue Note•2002','\
Duke Ellington•Highlights From The Duke Ellington Centennial Edition•RCA Victor•2000','\
Fats Waller•Complete Victor Piano Solos•Definitive Records (2)•2006'),'\
\
Chelsea Bridge\
':('\
Duke Ellington And His Orchestra•What Good Would It Do? / Chelsea Bridge•Victor•1942','\
Jim Hall Trio•Jim Hall Live In Tokyo•A&M Records•1976','\
Duke Ellington And His Orchestra•The Works Of Duke - Integrale Volume 17•RCA•0','\
Ron Carter•Carnaval•Galaxy•1983','\
Gary Bartz•Ju Ju Man•Catalyst Records (3)•1976','\
Denny Zeitlin•Tidal Wave•Palo Alto Records•1984','\
Art Farmer•What Happens ?...•Campi-Editore Recording•1968','\
Gerry Mulligan•Gerry Mulligan Meets Ben Webster•Verve Records•1960','\
Pepper Adams•The Master•Muse Records•1980'),'\
\
Cherokee\
':('\
Count Basie Orchestra•Cherokee •Brunswick•1939','\
Jørgen Ingmann•Anna / Cherokee•Metronome•0','\
Wynton Kelly•Cherokee / Moonglow•Blue Note•0','\
Enoch Light And The Light Brigade•Cherokee / Flying Home•Project 3 Total Sound•0','\
Charlie Barnet•Charleston Alley / Cherokee•Mercury•1952','\
Charlie Barnet And His Orchestra•Cherokee / Pompton Turnpike•Everest•0','\
Herbie Fields And His Orchestra•Moon Nocturne / Cherokee•RCA Victor•1947','\
Various•Music For Jazz Dancers•Freestyle Records (2)•2010','\
James Moody With Strings•Pennies From Heaven / Cherokee•Prestige•1952','\
Dizzy Gillespie•Jazz At Massey Hall Volume 4•Debut Records (3)•1958','\
Earl Bostic And His Orchestra•What! No Pearls / Cherokee•Odeon•1954','\
Stan Kenton•Contemporary Concepts Part 2•Capitol Records•0','\
Charlie Barnet And His Orchestra•Cherokee / The New Redskin Rhumba•Cardinal (2)•1947','\
Ray Noble And His Orchestra•Cherokee / By The Waters Of Minnetonka•Brunswick•1938','\
Tex Beneke And His Orchestra•St. Louis Blues March / Cherokee Canyon•RCA Victor•1948'),'\
\
Chicken Feathers\
':('\
Bugge Wesseltoft•Songs•Jazzland Recordings•2011','\
Eric Scortia•A Night On The Town•Heads Up International•1993','\
Steve Kuhn•Steve Kuhn Live In New York•Cobblestone•1972','\
Patrick Williams•Think•Verve Records•1968','\
Steve Kuhn Trio•Sing Me Softly Of The Blues•Venus Records (5)•1997','\
Monica Zetterlund•Chicken Feathers•SR Records•1972','\
Todd Rhodes•Dance Music That Hits The Spot•King Records (3)•1960','\
The Columbus Jazz Orchestra•Big Band Swing Blues & All That Jazz•Jazz Arts Group Of Columbus•1996','\
Teddi King•A Girl and Her Songs•RCA•0','\
Carmen McRae•Birds Of A Feather•DECCA•1958','\
Winifred Atwell•Plays A Further Fifty All Time Hits•Hallmark Music & Entertainment•2012','\
Various•Boogie Woogie•Documents•2003'),'\
\
Chick\'s Tune\
':('\
Chick Corea•Music Forever & Beyond: The Selected Works Of Chick Corea 1964-1996•GRP•1996','\
The Modernaires•Tributes In Tempo•Philips•1953'),'\
\
Child is Born A\
':('\
Terumasa Hino Sextet•Fuji•Victor•1972','\
Kenny Burrell•God Bless The Child•CTI Records•1971','\
Pepper Adams•Twelfth & Pingree•Enja Records•1975','\
Eddie Daniels•Brief Encounter•Muse Records•1980','\
Bill Evans•Quintessence•Fantasy•1977','\
Art Farmer•Big Blues•CTI Records•1979','\
Bobby Shew Quintet•Class Reunion•Sutra Records•1980','\
Jimmy Smith Trio•The Master II•Blue Note Records•1994','\
Tommy Flanagan•Our Delights•Galaxy•1979'),'\
\
Children\'s Song\
':('\
Eero Koivistoinen•For Children•Kustannusosakeyhtiö Otava•1970','\
Linda Hill•Lullaby For Linda•Nimbus West Records•1981','\
Stanley Clarke•Children Of Forever•Polydor•1973','\
Bill Dixon•Thoughts•Soul Note•1987','\
Bob Degen•Sequoia Song•Enja Records•1976','\
Center Of The World•Solos & Duets. Volume 7•Sun Records (2)•1975','\
Courtney Pine•To The Eyes Of Creation•Island Records•1992','\
Lonnie Liston Smith•A Song For The Children•Columbia•1979','\
Ole Amund Gjersvik•A Voice From The Past•Acoustic Records•1992','\
Glen Moore•In Concert•Vanguard•1977','\
Rodney Franklin•Skydance•Columbia•1985','\
Idiot Band•Toxic Trash•Not On Label (Idiot Band Self-released)•2014','\
Stanley Clarke•Children Of Forever•Polydor•1976','\
Daniel Erdmann•Ten Songs About Real Utopia•Arjunamusic•2015','\
Kyoto Jazz Sextet•Unity•Extra Freedom Ltd.•2017','\
Tom Scott•Born Again•GRP•1992','\
Trio Stendhal•Something Happened•Sentemo Records•1992'),'\
\
Chippie\
':('\
Ornette Coleman•Something Else!!!!•Contemporary Records•1958','\
no artist•Ornette For Ever•Moshé-Naïm•1996','\
Ornette Coleman•The Shape Of Jazz To Come•Not Now Music•2010','\
John Zorn•Spy Vs. Spy: The Music Of Ornette Coleman•Nonesuch•1988','\
Stefano Bollani•Les Fleurs Bleues•Label Bleu•2001'),'\
\
Choices\
':('\
Nakama (2)•Grand Line•Nakama Records•2016','\
The Michael Brecker Band•The Cost Of Living•Jazz Door•1994','\
Michael Brecker•Michael Brecker•MCA Impulse!•1987','\
Terence Blanchard•Live•Blue Note•2018','\
Phillip Wilson•The Phillip Wilson Project•Jazz Door•1994','\
Kinga Głyk•Dream•Warner Music•2017','\
Grant Geissman•Take Another Look•Bluemoon•1990','\
McCoy Tyner Big Band•Journey•Verve Records•1993','\
Romain Pilon Trio•The Magic Eye•Jazz&People•2015','\
Sam Gendel•4444•Terrible Records (2)•2017','\
Various•Cool Struttin\' Vol. One•Amber Records•1993','\
Charles Blenzig•Charles Blenzig•Chase Music Group•1989','\
Tina May•Never Let Me Go•33 Records•1992','\
Tauk•Collisions•Not On Label•2014'),'\
\
Christmas Waltz The\
':('\
Guy Lombardo And His Royal Canadians•White Christmas•Decca•0','\
Frank Sinatra•What Ever Happened To Christmas / The Christmas Waltz•Reprise Records•1968','\
Frank Sinatra•What Ever Happened To Christmas / The Christmas Waltz•Reprise Records•1968','\
Various•Herb Wong Presents More Mistletoe Magic: Swinging Holiday Jazz•Palo Alto Records•1985','\
Mantovani And His Orchestra•Twelve Days Of Christmas•Decca•1963','\
Guy Lombardo And His Royal Canadians•White Christmas / The Anniversary Waltz•Decca•1946','\
Frank Sinatra•Mistletoe And Holly/The Christmas Waltz•Capitol Records•1957','\
The Eddie Higgins Trio•Christmas Songs•Venus Records (5)•2004','\
Various•White Christmas•London Records•0','\
Peggy Lee•Christmas Carousel•Capitol Records•1960','\
Lawrence Welk And His Champagne Music•Jingle Bells•Coral•1957','\
Peggy Lee•Happy Holiday•Capitol Records•1965'),'\
\
Chromazone\
':('\
Mike Stern•Time In Place•Atlantic Jazz•1988','\
Mike Stern Band•New Morning - The Paris Concert•in-akustik•2009','\
Charged Particles•Charged Particles•no label•1994'),'\
\
Circle\
':('\
Chico Freeman Quartet•No Time Left•Black Saint•1979','\
Acoustic Alchemy•Mr. Chow / The Stone Circle•MCA Records•1987','\
Miles Davis•Miles Davis•AMIGA•1981','\
David Murray & Low Class Conspiracy•Vol. I: Penthouse Jazz•Circle Records (2)•1977','\
Annette Warren•Circle / Tame Me•ABC-Paramount•1955','\
Paul Horn•Joy / The Desert Is A Circle•Paramount Records•1971','\
Masabumi Kikuchi•Susto•CBS/Sony•1981','\
Max Highstein•Touch The Sky•Estúdio Eldorado•1987','\
Howard Riley•Duality•View Records•1982','\
European Jazz All Stars•Room 1220•Trio Records•1970','\
Louis Armstrong•Short But Sweet / The Circle Of Your Arms•Mercury•1965','\
The Lloyd McNeill Quartet•Washington Suite•ASHA Recording Co. Inc.•1970','\
RQ•Solid Ground•Blu Mar Ten Music•2018'),'\
\
Circular Motion\
':('\
The Phil Markowitz Trio•Sno\' Peas•Bellaphon•1991','\
Various•Helsinki Cooler Vol. 1•Cymbidium Records•2005','\
Alter-Natives•Hold Your Tongue•SST Records•1986'),'\
\
Cirrus\
':('\
Dharma Quintet•End Starting•SFP•1971','\
Bertil Strandbergs Kvintett•Cirrus•Arac•1973','\
Bobby Hutcherson•Cirrus•Blue Note•1974','\
Laurie Holloway•Cumulus•Hobo (2)•1979','\
Howard Riley•Flight•Turtle Records•1971','\
Egba•Egba•Grammofonverket•1974','\
Communication (4)•Communication•Grammofonverket•1974','\
Bonobo•The North Borders•Ninja Tune•2013','\
John Pisano•Makin\' It -  Guitar Duets•Decca•1958','\
The Kenny Bird Orchestra•Walk The Round•Palm Records•1987','\
The Kenny Bird Orchestra•Volume 4•Altaxon•0'),'\
\
Clockwise\
':('\
Timeless All Stars•At Onkel Pö\'s Carnegie Hall Hamburg 1982•Jazzline•2019','\
Billy Higgins•Soweto•Red Record•1979','\
Cedar Walton•Eastern Rebellion 3•Timeless Records (3)•1980','\
Akira Sakata Trio•Counter Clockwise Trip•Frasco•1975','\
The Barry Harris Sextet•Bull\'s Eye!•Prestige•1968','\
Timeless All Stars•It\'s Timeless•Baystate•1982','\
Jamey Aebersold•Volume 35: Nine Jazz Originals•JA Records•1985','\
Gene Ammons•Boss Tenors: Straight Ahead From Chicago August 1961•Verve Records•1962','\
Bobby Hutcherson•Conception: The Gift Of Love•Columbia•1979','\
Django Deluxe•Driving•Edel•2015','\
Katsuo Kuninaka•Warm Current•Frasco•1979'),'\
\
Close Enough For Love\
':('\
Cedar Walton•Eastern Rebellion 4•Timeless Records (3)•1984','\
Milt Jackson•A London Bridge•Pablo Records•1988','\
The Jacky Terrasson Trio•Lover Man•Venus Records (5)•2009','\
Stan Getz Quartet•The Dolphin•Concord Jazz•1981','\
Jackie & Roy•East Of Suez•Concord Jazz•1981','\
Claire Martin•Devil May Care•Linn Records•1993','\
The Singers Unlimited•Easy To Love•Pausa Records•1981','\
Ahmad Jamal•American Classical Music•Shubra•1982','\
Bill Watrous•A Time For Love•GNP Crescendo•1993','\
Helen Merrill•Casa Forte•Trio Records•1980','\
Bucky & John Pizzarelli•2 X 7 = Pizzarelli•Stash Records•1980','\
Shelly Manne•Fingering•Atlas Record (2)•1981','\
Buddy DeFranco•Mr. Lucky•Pablo Records•1984','\
David Hazeltine Trio•Pearls•Venus Records (5)•2001','\
LA4•Zaca•Concord Jazz•1980','\
Rob McConnell & The Boss Brass•All In Good Time•Palo Alto Records•1983','\
Ellyn Rucker•Ellyn•Capri Records (6)•1988'),'\
\
Close To You\
':('\
French Kicks•Close To Modern•Startime Intl Fader Label Enterprises•2002','\
Sarah Vaughan•Close To You / Out Of This World•Mercury•1960','\
Chico Freeman•The Search•India Navigation•1983','\
Buddy Johnson And His Orchestra•Keep Me Close To You / You Got To Walk The Chalk Line•Decca•1950','\
Billy Eckstine•Hold Me Close To You / If They Ask Me•MGM Records•1952','\
Kenny Barron•What If?•Enja Records•1986','\
The De Castro Sisters•With My Eyes Wide Open•ABC-Paramount•1959','\
Lionel Hampton•Jazzmaster!!!•Versatile•1977','\
Frank Sinatra•Close To You Part 1•Capitol Records•1956','\
Paris Match•Volume One•Aosis Records•2000','\
Øyvind Nypan•Big City•Losen Records•2018','\
Leon Spencer Jr.•Louisiana Slim•Prestige•1971','\
Aleksander Mazur Quartet•Bacharach•Polskie Nagrania Muza•1975','\
Nancy Wilson•Tender Loving Care•Capitol Records•1966','\
Art Pepper•One September Afternoon•Galaxy•1981','\
Monty Alexander•Taste Of Freedom•MGM Records•1970'),'\
\
Close Your Eyes\
':('\
Jimmy McGriff•Close Your Eyes•Sue Records Inc.•1964','\
Hadda Brooks•Close Your Eyes / Old Man River•Modern Records (2)•1956','\
Humphrey Lyttelton And His Band•Close Your Eyes / Bad Penny Blues•Parlophone•1956','\
Art Blakey & The Jazz Messengers•Munich \'59•Birdland (7)•2012','\
The Merry Macs•The Christmas Cha Cha / Close Your Eyes•Portrait (3)•1961','\
The Roy Eldridge-Benny Carter Orchestra•The Moon Is Low•Clef Records•1955','\
Herb Lance•Drifting Water•DeLuxe (2)•1957','\
Eric Kloss•Close Your Eyes / That\'s The Way It Is•Prestige•0','\
Art Blakey & The Jazz Messengers•Au Théâtre Des Champs-Élysées•RCA•1960','\
Art Blakey & The Jazz Messengers•At The Jazz Corner Of The World Vol. 1•Blue Note•1959','\
Pat Martino•East!•Prestige•1968','\
Anita Baker•You\'re My Everything•Blue Note•2004','\
Houston Person•Goodness!•Prestige•1969'),'\
\
Cold Duck Time\
':('\
Les McCann•Compared To What•Atlantic•1969','\
Blake Hawley•The Standard Duo•Not On Label (Blake Hawley Self-released)•2013','\
Rusty Bryant•Soul Liberation•Prestige•1970','\
Les McCann•Swiss Movement•Atlantic•1969','\
Brother Jack McDuff•Bringin\' It Home•Concord Jazz•1999','\
Tommy Schneider & Friends•The Hidden Port•Kolibri Records•2012','\
Jeff Golub•Do It Again•GRP•2002','\
Brian Bromberg•Downright Upright•Seven Seas•2006','\
Poncho Sanchez•Latin Soul•Concord Picante•1999','\
Rusty Bryant•Legends Of Acid Jazz•Prestige•1996'),'\
\
Colors of Chloe\
':('\
Michel Petrucciani•Both Worlds•Disques Dreyfus•1997'),'\
\
Come Fly With Me\
':('\
Frank Sinatra•Come Fly With Me•Capitol Records•1978','\
Positive Flow•The City Streets•Native Source Recordings Limited•2005','\
Frank Sinatra•Nice \'N\' Easy / Come Fly With Me•Capitol Records•1986','\
Frank Sinatra•Sinatra At The Sands•Reprise Records•1966','\
Frank Sinatra•The Lady Is A Tramp•Capitol Records•1958','\
LaVerne Butler•No Looking Back•Chesky Records•1993','\
Michael Bublé•How Can You Mend A Broken Heart•Warner Music•2003','\
Frank Sinatra•Sinatra At The Sands Vol.1•Reprise Records•1966','\
Richie Cole•Pure Imagination•Concord Jazz•1987','\
Jackie Allen (2)•The Men In My Life•A440 Music Group•2003','\
Curtis Stigers•One More For The Road•Concord Jazz•2017','\
Frank Sinatra•Duets II•Capitol Records•1994'),'\
\
Come Rain Or Come Shine\
':('\
Barbra Streisand•Timeless Live In Concert•Columbia•2000','\
Wynton Kelly•Come Rain Or Come Shine•Vee Jay Records•1961','\
The Bill Evans Trio•The 1960 Birdland Sessions•Cool & Blue Records•1992','\
Plas Johnson And His Orchestra•Come Rain Or Come Shine / The Big Twist•Capitol Records•1957','\
Stanley Turrentine•Up At "Minton\'s" Vol. 2•Blue Note•1961','\
Georgia Gibbs•Come Rain Or Come Shine / I Want You To Be My Baby•Mercury•1955','\
Ed Bickert•From Canada With Love•PM•1976','\
Ray Charles•Come Rain Or Come Shine / Tell Me You\'ll Wait For Me•Atlantic•1960','\
Art Blakey & The Jazz Messengers•Hard Champion•Paddle Wheel•1987','\
John Coltrane•The Last Trane•Prestige•1965','\
Dexter Gordon•Montmartre Collection Volume 3•Black Lion Records•1978'),'\
\
Come Sunday\
':('\
Duke Ellington And His Orchestra•Black Brown And Beige•Columbia•1958','\
Oscar Peterson•Come Sunday•Verve Records•1963','\
Ben Webster•Master Of Jazz Vol. 5•Storyville•1984','\
Andrew Hill•Live At Montreux•Arista•1975','\
Oscar Peterson•During This Time•Art Of Groove•2014','\
Jeri Southern•Come By Sunday / Nothing At All•Decca•1955','\
The Oscar Peterson Trio•The Trio•Pablo Records•1974','\
Eric Dolphy•Iron Man•Douglas•1968'),'\
\
Comin\' Home Baby\
':('\
Michael Bublé•Comin\' Home Baby•143 Records•2008','\
The Joe Thomas Group•Comin\' Home Baby / More•Cobblestone•1968','\
Herbie Mann•The Best Of Herbie Mann•Atlantic•1970','\
Herbie Mann• Summertime/Comin\' Home Baby•Atlantic•1962','\
The Kai Winding Orchestra•More / Comin\' Home Baby•Verve Records•1963','\
Quincy Jones•Soul Bossa Nova / Comin\' Home Baby•Seven Up Records•2001','\
The Peddlers•Comin\' Home Baby•CBS•1968','\
Frances Faye•Comin Home Baby•Audio Fidelity Records Inc.•0','\
Herbie Mann•Herbie Mann At The Village Gate•Atlantic•1962','\
Herbie Mann•Standing Ovation At Newport•Atlantic•1965','\
Casey And The Pressure Group•Comin\' Home Baby•Polydor•1971','\
Mel Tormé•Comin\' Home Baby•Atlantic•1962'),'\
\
Como En Vietnam\
':('\
Various•Jazz Na Koncertnom Podiju Vol. 4•Jugoton•1980','\
Gary Burton•Times Square•ECM Records•1978','\
Gary Burton•Gary Burton & Keith Jarrett•Atlantic•1971','\
Dave Matthews Trio•American Pie•Sweet Basil (2)•1990','\
Putte Wickman•Happy New Year!•EMI•1973','\
Gary Burton•Gary Burton•Supraphon•1981','\
Gary Burton•Gary Burton & Keith Jarrett / Gary Burton: Throb•Rhino Records (2)•1994','\
Keith Jarrett•Somewhere Before: The Keith Jarrett Anthology (The Atlantic Years 1968-1975)•Warner Jazz•2008','\
Kip Hanrahan•At Home In Anger Which Could Also Be Called Imperfect Happily•Yellowbird•2011'),'\
\
Compared to What\
':('\
Coco Stephens•Compared To What•Kurt Records (2)•2014','\
Les McCann•Music Box•Jam (15)•1984','\
Les McCann•Compared To What / Philly Dog•Atlantic•0','\
Anita Moore•Compared To What / Didn\'t We•Advent Records (2)•0','\
Les McCann•Compared To What•Atlantic•1969','\
Anita Moore•Compared To What?  / Blues Of The New World•Advent Records (2)•2011','\
Ray Charles•Compared To What / Now That We\'ve Found Each Other•Atlantic•1980','\
Passport (2)•Doldinger Jubilee \'75•Atlantic•1975','\
Les McCann•Swiss Movement•Atlantic•1969','\
Junko Onishi•Fragile•no label•1998'),'\
\
Con Alma\
':('\
Ray Barretto•Se Traba / Alma Con Alma•Fania Records•1972','\
Dizzy Gillespie Quintet•Liederhalle Stuttgart November 27 1961 - Kongresshalle Frankfurt November 29 1961•Jazzhaus•2012','\
Dizzy Gillespie•Duets•Verve Records•1958','\
Dizzy Gillespie•Gillespie En Vivo•Areito•1985','\
Ray Barretto•Gracias•Fania Records•1978'),'\
\
Conception\
':('\
Miles Davis And His Band•Conception / Bluing (Pt. 3)•Prestige•1953','\
Clifford Brown Sextet•Conception E.P.•Vogue•1955','\
Bugge Wesseltoft•New Conception Of Jazz•Jazzland Recordings•1997','\
Billy Bang•Outline No. 12•Celluloid•1983','\
Bob Wilson•In The Midnight Hour•Sound Stage 7•0','\
The George Shearing Quintet•East Of The Sun (And West Of The Moon) / Conception•MGM Records•1949','\
Charlie Haden•Silence•Soul Note•1989','\
Ultramarine (3)•Programme Jungle•Bloomdido•1985','\
Sonny Clark Trio•Sonny Clark Trio•Time Records (3)•1960','\
Miles Davis•The New Sounds•Prestige•1951','\
Sonny Clark•My Conception•Blue Note•1979'),'\
\
Conference of the Birds\
':('\
David Holland Quartet•Conference Of The Birds•ECM Records•1973','\
Nexus (46)•Urban Shout•Splasc(h) Records•1988'),'\
\
Confessin (That I Love You)\
':('\
Sonny Stitt•Stitt\'s It / Confessin\' (That I Love You)•Prestige•1952','\
Louis Armstrong And His Orchestra•Confessin\' That I Love You / Our Monday Date•Decca•1939','\
Lionel Hampton And His Orchestra•Confessin\' (That I Love You) / Drum Stomp•Victor•1937','\
Lester Young Quintet•I Can\'t Give You Anything But Love / I\'m Confessin\' That I Love You /•Blue Star•0','\
Louis Armstrong And His Orchestra•Once In A While / Confessin\' (That I Love You)•Decca•1952','\
Louis Prima & Keely Smith•I\'m Confessin\' (That I Love You)•Dot Records•1959','\
Harry James And His Orchestra•When Your Lover Has Gone / I\'m Confessin\' (That I Love You)•Columbia•1945','\
Ella Fitzgerald•And Her Tears Flowed Like Wine / Confessin\' (That I Love You)•Decca•1944','\
Django Reinhardt•Django Reinhardt (EP)•Verve Records•1963','\
Marc Ribot Trio•Live At The Village Vanguard•Pi Recordings (2)•2014','\
Louis Armstrong•Satchmo 1944 & 47•DAN•0','\
Clark Terry Quartet•Eddie Costa: Memorial Concert•Colpix Records•1963','\
Django Reinhardt•Django - Swing It Lightly•CBS•1985','\
Guy Lombardo And His Royal Canadians•Souvenirs•Decca•1951','\
Herb Ellis•Seven Come Eleven (From Their Live Performance At The Concord Summer Festival)•Concord Jazz•1974','\
Count Basie And The Kansas City Seven•Mostly Blues And Some Others•Pablo Records•1986'),'\
\
Confirmation\
':('\
Benny Bailey Quintet•Benny Bailey Quintet•Sonet•0','\
The Great Jazz Trio•At The Village Vanguard Vol.2•East Wind•1977','\
Tete Montoliu Trio•Secret Love•Timeless Records (3)•1978','\
Jimmy Smith•Confirmation•Blue Note•1979','\
Art Blakey Quintet•A Night At Birdland Vol. 3•Blue Note•1954','\
Manhattan Jazz Quintet•Autumn Leaves•Paddle Wheel•1985'),'\
\
Contemplation\
':('\
Art Blakey & The Jazz Messengers•Buhaina\'s Delight•Blue Note•1963','\
Passport (2)•Infinity Machine•Atlantic•1976'),'\
\
Continental The\
':('\
Larry Adler•Continental / Smoke Gets In Your Eyes•Columbia•1936','\
Eddie Heywood Trio•The Continental / Heywood\'s Boogie•no label•1948','\
Ray Conniff And His Orchestra & Chorus•\'S Wonderful•CBS•1962','\
Various•Dbx Encoded Disc Vol.1•Technics•0','\
David Rose & His Orchestra•Strings Of Fantasy•no label•1955','\
The George Shearing Quintet•The Continental / East Of The Sun (West Of The Moon)•MGM Records•1949','\
Pantaleón Perez Prado E La Sua Orchestra Cubana•Madunina•Disques Vogue•0','\
Bill Doggett• Let\'s Do The Continental / Pony Walk•Warner Bros. Records•0','\
The George Shearing Quintet•The Continental / Nothing But D. Best•MGM Records•1949','\
Directions•Echoes•Soul Static Sound•1997','\
Eddie Heywood And His Orchestra•Jasmine / The Continental (You Kiss While You\'re Dancing)•Decca•0','\
Louis Prima•The Continental Twist•London Records•0'),'\
\
Cookin\'\
':('\
Willis Jackson•Cookin\' Sherry•Prestige•1960','\
Roy Porter Quintet•Juicy / Home Cookin\' (Good Cookin\')•King Records (3)•0','\
Genghis Kyle•Sumptin\' Cookin\' / Genghis Blues•Timbre (2)•0','\
Horace Silver•The Best Of Horace Silver Vol. I•Blue Note•1988','\
Various•Wildflowers 5 (The New York Loft Jazz Sessions)•Douglas•1977','\
The Horace Silver Quintet•Home Cookin\'•Blue Note•1957','\
The Jimmy Neeley Trio•What\'s Cookin\' /  Grits \'N\' Greens•Tru-Sound•1962','\
no artist•Night Train / Bluff City Cookin\'•Mega Records (4)•1972','\
Lambert Hendricks & Ross•High Flying•Columbia•1962','\
Joe Swift•Crazy \'Bout Your Cookin\' / Right Now Baby•Exclusive (2)•1949','\
G. Love•Hot Cookin\'•Brushfire Records•2007'),'\
\
Cool Blues\
':('\
Charlie Parker•Charlie Parker On Dial Volume 2•Spotlite Records•1972','\
The Charlie Parker Quartet•Cool Blues / Quasimado•Dial Records (3)•1949','\
Jackie McLean•Bluesnik•Blue Note•1961','\
The Horace Silver Quintet•Señor Blues•Blue Note•1956','\
The Charlie Parker Quartet•Bird\'s Nest / Cool Blues•Tono•1948','\
Bobby Byrne And His NBC Dixieland Band•Dixieland Vs Birdland - A Battle Of Jazz•MGM Records•1954','\
Johnny Hodges•Alto Blue•VSP•1966','\
Ray Brown•Jazz At The Philharmonic One O\'Clock Jump 1953•Verve Records•1983','\
Charlie Parker•Memories Of Bird•Esquire•0','\
Charlie Parker•Bird Blows The Blues•Dial Records (3)•1949','\
Charlie Parker•Volume 6: Bongo Bop•Saga (5)•1969'),'\
\
Cool Green\
':('\
Jackie McLean•Bluesnik•Blue Note•1961','\
Richie Cole•Cool "C"•Seven Seas•1981','\
Neil Larsen•Smooth Talk•MCA Records•1989','\
Various•A Time To Remember 1951•EMI•1998','\
Wynton Marsalis•Marsalis Plays Monk (Standard Time Vol. 4)•Columbia•1999','\
Billy May•Johnny Cool•United Artists Records•1963','\
Paula Faour•Cool Bossa Struttin\'•JSR•2002','\
Nino Tempo•Live At Cicada•Atlantic Jazz•1995','\
Gene Krupa And His Orchestra•Gene Krupa Dance Parade•Columbia•0','\
Bela Babai And His Orchestra•Gypsy Love•Columbia•1955','\
Joe Pass•The Best Of Joe Pass•Pablo Records•1983'),'\
\
Coral\
':('\
Walter Bishop Jr.•Coral Keys•Black Jazz Records•1971','\
Zbigniew Seifert•Kilimanjaro•PolJazz•1979','\
Archie Shepp•Coral Rock•America Records•1970','\
no artist•Cute•Reprise Records•1964','\
Bryan Savage•Rush Hour•Higher Octave Jazz•2001','\
Bill Hardman•Politely•Muse Records•1982','\
Freddie Hubbard•The Black Angel•Atlantic•1970','\
Emily Remler•Transitions•Concord Jazz•1984','\
Svin•Virgin Cuts•Mom Eat Dad Records•2018','\
Gary Burton•Times Square•ECM Records•1978','\
Jason Rebello•Permanent Love•Novus•1993'),'\
\
Corcovado\
':('\
Stan Getz•The Girl From Ipanema•Verve Records•1964','\
Grant Green•I Want To Hold Your Hand•Blue Note•1965','\
The Jack Wilson Quartet•The Jack Wilson Quartet•Atlantic•1963','\
Ron Carter•When Skies Are Grey...•no label•2000','\
Antonio Carlos Jobim•Corcovado / One Note Samba•Verve Records•1964','\
Antonio Carlos Jobim•The Girl From Ipanema•Verve Records•0','\
Antonio Carlos Jobim•Corcovado / One Note Samba•Verve Records•1964','\
Miles Davis•Orbits•Columbia Musical Treasuries•1968','\
Gabor Szabo•More Sorcery•Impulse!•1967','\
Antonio Carlos Jobim•Corcovado / The Girl From Ipanema•Verve Records•0'),'\
\
Core\
':('\
Gerry Mulligan And His Sextet•Presenting The Gerry Mulligan Sextet - Vol. 2•EmArcy•1957','\
Soil & "Pimp" Sessions•表Nothin’裏Girl•HMV Record Shop•2014','\
Art Blakey & The Jazz Messengers•Free For All•Blue Note•1965','\
Muriel Grossmann•Golden Rule•RR GEMS•2018','\
Orchester Heinz Neubrand•T\'ho Voluto Bene / Anema E Core•Elite Special•0','\
Orchester Béla Sanders•Tanz Mit Béla Sanders: Rumba/Bolero - 2. Folge•Philips•1961','\
Brew Moore•Live In Europe 1961•Sonorama•2015','\
Stu Goldberg•Piru•MPS Records•1981'),'\
\
Cork \'n Bib\
':('\
Lee Konitz•Inside Hi-Fi•Atlantic•1956','\
Lee Konitz•Lee Konitz Meets Jimmy Giuffre•Verve Records•1959','\
Lee Konitz•Lee Konitz Meets Jimmy Giuffre•Verve Records•1996','\
Lennie Tristano•The Complete Atlantic Recordings Of Lennie Tristano Lee Konitz & Warne Marsh•Mosaic Records (2)•1997'),'\
\
Cottontail\
':('\
Ben Webster•Plays Duke Ellington•Storyville•1988','\
Flip Phillips Sextet•Cottontail / Blues For The Midgets•Mercury•1953','\
Illinois Jacquet•Illinois Jacquet And His Orchestra•Clef Records•0','\
Duke Ellington And His Orchestra•Don\'t Get Around Much Anymore (Never No Lament) / Cottontail•Victor•0','\
Gene Krupa•The Drum Battle•Verve Records•1983','\
Clark Terry•Jive At Five•Enja Records•1990','\
Oscar Peterson•Oscar Peterson Plays Duke Ellington•Mercury•1953','\
Hal Galper•Naturally•BlackHawk Records•1987','\
Lew Tabackin•Vintage Tenor•RCA•1978','\
George Jenkins And His All Stars•Drum Stuff•Tampa Records•1956','\
Illinois Jacquet•Collates•Mercury•1952'),'\
\
Could It Be You\
':('\
Charles McPherson•Beautiful!•Xanadu Records•1975','\
Dick Griffin•The Eighth Wonder•Strata-East•1974','\
Ella Fitzgerald•Ella Fitzgerald In Person•Verve Records•1961','\
Sonny Rollins•Sonnymoon For Two•Moon Records (4)•1990','\
Sonny Rollins•Oleo•Ediciones Del Prado•1996','\
Various•All Time Favorites•Seeburg•1956','\
Myriam Alter•Where Is There•Enja Records•2007','\
Don Elliott•At The Modern Jazz Room•ABC-Paramount•1958','\
Phil Upchurch•Name Of The Game•Jam (15)•1983','\
Stanisław Sojka•Don\'t You Cry•PolJazz•1979','\
Monty Alexander•Stir It Up - The Music Of Bob Marley•Telarc•1999','\
Frank Sinatra•La Voce Un Mito•Cobra Record•1972','\
Shirley Scott•Shirley\'s Sounds•Prestige•1961','\
Mickey Tucker•The Crawl•Muse Records•1980','\
The Jacobs Brothers (2)•In Jazz•Fontana•1958','\
Bing Crosby•Blue Of The Night•Decca•1947','\
John Mehegan•How I Play Jazz Piano•Savoy Record Co. Inc.•1956','\
Les Brown And His Band Of Renown•The Swingin\' Sound•Signature (4)•1960','\
Karin Krog•Where You At?•Enja Records•2003'),'\
\
Countdown\
':('\
Wilbur Harden•Mainstream 1958: The East Coast Jazz Scene Vol. 2•Arista•1977','\
The Dave Brubeck Quartet•Countdown / Eleven Four•Columbia•1962','\
Phil Tate And His Orchestra•Green Turtle•Oriole•1959','\
John Coltrane•Giant Steps•Atlantic•1960','\
Brian Fahey And His Orchestra•Countdown•Major Minor•1969','\
The Dave Brubeck Quartet•Three\'s A Crowd / Countdown / Eleven Four / Waltz Limp•CBS•1966','\
Dave "Baby" Cortez•Countdown / Summertime (Cha-Cha-Cha)•Roulette•1966','\
Tomasz Stańko & Adam Makowicz Unit•Tomasz Stańko & Adam Makowicz Unit•JG-Records•1975','\
John Coltrane•The Complete Mainstream 1958 Sessions•Lone Hill Jazz•2004','\
John Coltrane•Giant Steps•Atlantic•1960'),'\
\
Country Roads\
':('\
Ray Charles•Every Saturday Night•Probe•1973','\
Ray Charles•Never Ending Song Of Love / Take Me Home Country Roads•Probe•1972','\
Gary Burton•Like Minds•Concord Records•1998','\
The NDR Big Band•Bravissimo - 50 Years NDR Bigband•ACT (4)•1996','\
Robin Harp•Country Western•Bonanza (3)•0','\
The Mike Gibbs Band•Just Ahead•Polydor•1972','\
Gary Burton Quartet•Country Roads & Other Places•RCA Victor•1969','\
Various•John Denver\'s World  An All-Star Salute•RCA Special Products•1976','\
The Fabulous Inkspots•Ray Richardson\'s Fabulous Inkspots•Periwinkle Records•0','\
The 24th. Street Band•Bokutachi•Better Days (2)•1981','\
Billy Vaughn And His Orchestra•Volume II•Movieplay Brasil•1992','\
Lena Martell•Hello Misty Morning•Pye Records•1977','\
Lisa Ono•Best 2002-2006•Suite¡ Supuesto!•2002','\
Lenny Dee (2)•Easy Loving•Decca•1971','\
Gary Burton•Artist\'s Choice•Bluebird (3)•1987','\
Lisa Ono•Jambalaya - Bossa Americana•Virgin•2006'),'\
\
Cousin Mary\
':('\
Manfred Schulze Formation•Geithain 1976•Not On Label•2009','\
John Coltrane•The Best Of John Coltrane•Atlantic•1970','\
The Hiroshi Fukumura Quintet•Morning Flight•Three Blind Mice•1973','\
Tommy Flanagan•Giant Steps (In Memory Of John Coltrane)•Enja Records•1988','\
John Coltrane•Giant Steps•Atlantic•1960','\
Tommy Flanagan•Giant Steps (In Memory Of John Coltrane)•Enja Records•1988','\
John Coltrane•Giant Steps•Atlantic•1960','\
Leon Thomas•Gold Sunrise On Magic Mountain•Mega Records (4)•1971','\
Tommy Flanagan•Giant Steps (In Memory Of John Coltrane)•Enja Records•1982'),'\
\
Crazeology\
':('\
Charlie Parker•Charlie Parker On Dial (Volume 6)•Spotlite Records•1971','\
The Charlie Parker Sextet•Crazeology / Relaxing At Camarillo•Blue Star•0','\
The Charlie Parker Sextet•Charlie Parker All Star Sextet•Sonet•1957','\
The Hank Mobley Quintet•Mobley\'s 2nd Message•Prestige•1957','\
Hampton Hawes•For Real!•Contemporary Records•1961','\
Charlie Parker•The Art Of Charlie Parker - Vol. 1: The Fabulous Bird•Concert Hall•1955','\
Steve Nelson Jazz Quartet•Easy Living•Venus Records (5)•2018','\
Francesco Cafiso Quartet•Seven Steps To Heaven•Venus Records (5)•2008','\
Charlie Parker•Diz And The Bird•Everest Records Archive Of Folk & Jazz Music•0','\
Charlie Parker•The Bop Originators•Napoleon•0'),'\
\
Crazy He Calls Me\
':('\
Linda Ronstadt•What\'s New•Asylum Records•1983','\
Billie Holiday•You\'re My Thrill / Crazy He Calls Me•Decca•1949','\
Clifford Brown All Stars•Jams 2•Emarcy•1983','\
Swing (5)•Serenade In Blue•Planet (15)•1981','\
Lucy Ann Polk•Don\'t Do Something To Someone Else•RCA Victor•1950','\
Dakota Staton•Crazy He Calls Me - Part 1•Capitol Records•1959','\
Ramsey Lewis•The Groover•Cadet•1972','\
Andrea Motis• Live At Palau De La Música •Jazz To Jazz•2015','\
Aretha Franklin•Aretha\'s Jazz•Atlantic•1984','\
Laura Yager•Laura•Ovation Records•1970','\
Wynton Kelly•New Faces–New Sounds•Blue Note•1953','\
Etta Jones•I\'ll Be Seeing You•Muse Records•1988','\
Herb Geller Sextette•The Herb Geller Sextette•EmArcy•1955'),'\
\
Crazy Rhythm\
':('\
Jazz At The Philharmonic•Norman Granz\' Jazz At The Philharmonic Vol. 3•Mercury•1946','\
Harry James And His Orchestra•Crazy Rhythm / Easter Parade•Columbia•1942','\
Coleman Hawkins And His All Star Jam Band•Honeysuckle Rose / Crazy Rhythm•Swing (3)•1937','\
Coleman Hawkins Swing Four•Get Happy / Crazy Rhythm•Signature (4)•1944','\
Coleman Hawkins And His Orchestra•Body And Soul•RCA•0','\
Jazz At The Philharmonic•Jazz At The Philharmonic•Opera•0','\
Harry James And His Orchestra•Crazy Rhythm / Blues In The Night•Parlophone•1945','\
Django Reinhardt•Django Reinhardt•Electrola•1959','\
Benny Goodman And His Orchestra•All The Cats Join In / Crazy Rhythm•Columbia•1948','\
Dorothy Collins•Mountain High - Valley Low / Crazy Rhythm•Audivox•1954','\
Harry James And His Orchestra•Crazy Rhythm•Columbia•1957','\
The Red Garland Quintet•Dig It!•Prestige•1962'),'\
\
Creek\
':('\
The Blackbyrds•Rock Creek Park•Fantasy•1975','\
Pete Johnson•Sixth Avenue Express / Pine Creek•Victor•1941','\
Jelly Roll Morton Trio•Shreveport-Stomp / Deep Creek-Blues•no label•0','\
The Blackbyrds•Happy Music / Rock Creek Park•Fantasy•1991','\
Buddy Tate•Live At Sandy\'s•Muse Records•1980','\
The Blackbyrds•Rock Creek Park / Thankful \'Bout Yourself•Fantasy•1975','\
George Wallington Quintet•The New York Scene•New Jazz•1957','\
Allaudin Mathieu•Listening To Evening•Sona Gaia Productions•1985','\
Buddy Tate•Just Jazz•Uptown Records (2)•1984','\
Ray Pizzi•Conception•Pablo Records•1977','\
The Georgia Baths•Mill Creek Ravine In Winter / Rube Goldberg Machine•Not On Label (The Georgia Baths Self-released)•2013'),'\
\
Creepin\'\
':('\
The Horace Silver Quintet•Horace Silver Quintet Volume 3•Blue Note•1954','\
Nautilus (25)•Creepin\'•Agogo Records•2017','\
Blue Mitchell•Creepin\'•RCA•1975','\
Kenny Rankin•Creepin\' / Lost Up In Loving You•Little David Records•1975','\
Stone Alliance•Stone Alliance•PM•1976','\
no artist•Creepin\' Around •Hi Records•1969','\
Max Roach•Swish•New Artists•1982','\
Horace Silver•Horace Silver And The Jazz Messengers•Blue Note•1956','\
Boney James•Trust•Spindletop Records•1992','\
Blue Mitchell•Stratosonic Nuances•RCA•1975'),'\
\
Crescent\
':('\
Rob Mazurek•Alternate Moon Cycles•International Anthem Recording Company•2014','\
John Coltrane•Coltrane In Tokyo Vol.2•MCA Records•1980','\
John Coltrane•Offering: Live At Temple University•Impulse!•2014','\
Bobby Hutcherson•Farewell Keystone•Theresa Records•1988','\
Arthur Blythe•Da - Da•CBS•1986','\
Woody Shaw•Night Music•Elektra Musician•1983'),'\
\
Criss Cross\
':('\
The Duke Of Burlington•Flash•International Polydor Production•1970','\
The Duke Of Burlington•Criss Cross•Signal (5)•1970','\
Steve Lacy•The Straight Horn Of Steve Lacy•Candid•1960','\
Thelonious Monk•Criss-Cross•Columbia•0','\
Calvin Keys•Shawn-Neeq•Black Jazz Records•1971','\
Michael Beck•Aphorism•Unit Records (2)•2015','\
Thelonious Monk•At Newport 1963 & 1965•Columbia•2002','\
Thelonious Monk•The London Collection: Volume Two•Black Lion Records•1988','\
Thelonious Monk•The Essence Of Thelonious Monk•Columbia•1991','\
Milt Jackson•Wizard Of The Vibes•Blue Note•1952','\
André Hodeir•American Jazzmen Play Andre Hodeir\'s Essais•Savoy Records•1957'),'\
\
Crystal Love\
':('\
Wilbert Longmire•Crystal Clear / But I Love You•Tappan Zee Records•1980','\
Yuji Ohno•Space Kid•CBS/Sony•1978','\
David Murray Latin Big Band•Now Is Another Time•Justin Time•2003','\
Music Magic•Music Magic•GMT Records•1979','\
Mulgrew Miller•The Countdown•Landmark Records (3)•1989','\
Mike Curb And The Waterfall•The Doors Songbook•Forward Records (3)•0','\
Makoto Ozone•Makoto Ozone•Columbia•1984','\
The Mystic Moods Orchestra•Another Stormy Night•Bainbridge Records•1983','\
1986 Omega Tribe•DJ Special•Vap•1987','\
Ray Gaskins•Can\'t Stop•MT Records•1995','\
Gary Burton / Chick Corea•In Concert Zürich October 28 1979•ECM Records•1980','\
Van Lynn And His Orchestra•Listening Pleasure•Brunswick•1957','\
Space Jazz Trio•Vol. 1•YVP Music•1986','\
Les Reed And His Orchestra•Love Is All•London Records•1969','\
Orlando Julius & The Ashiko•Love Peace & Happiness•Jungle Records (11)•1978','\
Paul Hardcastle•VII•no label•2013','\
Wilbert Longmire•With All My Love•Tappan Zee Records•1980'),'\
\
Crystal Silence\
':('\
Izabella Effenberg•Crystal Silence (Music For Array Mbira)•Unit Records (2)•2019','\
Chick Corea•Live In Molde•MNJ Records•2005','\
Arild Andersen•Celebration•ECM Records•2012','\
The Woody Herman Big Band•World Class•Concord Jazz•1984','\
Chick Corea•Return To Forever•ECM Records•1972','\
The Woody Herman Big Band•Aurex Jazz Festival \'82•Eastworld•1982','\
Gary Burton•Gary Burton And The Berklee All-Stars•JVC•1986'),'\
\
Cubano Chant\
':('\
Junior Mance•Live At Sweet Basil•Flying Disk•1977','\
El Chicano•Cubano Chant / Viva La Raza•Kapp Records•1971','\
Ron Carter•When Skies Are Grey...•no label•2000','\
The Essence All Stars•Afro Cubano Chant•Hip Bop Essence•1995','\
Art Blakey & The Jazz Messengers•Drum Suite•Columbia•1957','\
Art Taylor•Taylor\'s Wailers•Prestige•1957','\
Cal Tjader•Live At The Funky Quarters•Fantasy•1972','\
Charles Kynard•Warm Winds•World Pacific Records•1964','\
Roberto Fonseca•ABUC•Impulse!•2016'),'\
\
Cute\
':('\
Lenny Dee (2)•Daydream / Cute•Decca•1967','\
Lionel Hampton•Trick Or Treat / Cute•Impulse!•1964','\
no artist•Cute•Reprise Records•1964','\
Clark Terry•Jive At Five•Enja Records•1990','\
Tito Puente And His Orchestra•Cute Chick / A La Salud•RCA Victor•1957','\
Joe Farnsworth Quartet•My Heroes tribute to the Legends•Venus Records (5)•2014','\
Freddie Redd•Redd\'s Blues•Blue Note Records•2002','\
Takeshi Inomata•Stop\' Over•Fic•0','\
Eiji Kitamura•Eight Degrees North •CBS/Sony•1980','\
Lee Morgan•Charisma•Blue Note•1969','\
Bill Perkins•West Coast Tenors•Xanadu Records•1988'),'\
\
D Minor Mint\
':('\
Freddie Hubbard•Breaking Point•Blue Note•1964','\
Freddie Hubbard•The Best Of Freddie Hubbard•Blue Note•1989','\
Freddie Hubbard•MMTC: (Monk Miles Trane & Cannon)•MusicMasters Jazz•1995'),'\
\
Daahoud\
':('\
Clifford Brown•Embraceable You / Daahoud•Limelight•1964','\
Clifford Brown And Max Roach•Däähoud•EmArcy•0','\
Dizzy Gillespie•The Trumpet Summit Meets The Oscar Peterson Big 4•Pablo Today•1980','\
Clifford Brown And Max Roach•Clifford Brown And Max Roach•Emarcy•1954','\
Clifford Brown And Max Roach•Clifford Brown And Max Roach•EmArcy•2005','\
Clifford Brown And Max Roach•Clifford Brown And Max Roach•EmArcy•1955','\
Emily Remler•East To Wes•Concord Jazz•1988','\
Ray Bryant Trio•Piano Piano Piano Piano•Original Jazz Classics•1993'),'\
\
Dancing In The Dark\
':('\
Charlie Parker With Strings•Dancing In The Dark•Mercury•1950','\
Artie Shaw And His Orchestra•Dancing In The Dark / Yolanda•no label•1946','\
Ray Anthony & His Orchestra•Dragnet / Dancing In The Dark•Capitol Records•1953','\
Artie Shaw And His Orchestra•Star Dust•RCA•0','\
David Rose & His Orchestra•Poinciana / Dancing In The Dark•Victor•1944','\
Jan August•Dancing In The Dark / Night And Day•Brunswick•1948','\
Joe Loss & His Orchestra•Changing Partners / Dancing In The Dark•no label•1954','\
Frank Sinatra•Cheek To Cheek / Dancing In The Dark•Capitol Records•1958','\
Frank Sinatra•Song from "Some Came Running"•Capitol Records•1959','\
Artie Shaw•Artie Shaw•RCA Victor•1958','\
Artie Shaw•Star Dust•RCA Records•0','\
Artie Shaw And His Orchestra•The King Of The Clarinet = El Rey Del Clarinete•RCA Victor•1961','\
Herman Foster•The Explosive Piano Of Herman Foster•Epic•1961','\
Artie Shaw And His Orchestra•Nightmare•RCA Victor•1953','\
Charlie Parker With Strings•Charlie Parker With Strings•Clef Records•0','\
Earl Bostic And His Orchestra•La Cucaracha Cha Cha / Dancing In The Dark•King Records (3)•0','\
Artie Shaw•Tribute To Artie Shaw•Crown Records (2)•1959'),'\
\
Dancing In The Street\
':('\
Donald Byrd•Dancing In The Street / Onward \'Til Morning•Blue Note•1976','\
The Mariachi Brass•Dancing In The Street•World Pacific Records•1966','\
Ramsey Lewis•Girl Talk / Dancing In The Street•Cadet•1967','\
The Ramsey Lewis Trio•Soul Incorporated•Chess•1968','\
The Ramsey Lewis Trio•Soul Incorporated•Chess•1968','\
Donald Byrd•Caricatures•Blue Note•1976','\
Ramsey Lewis•The Best Of Ramsey Lewis•Fontana•1972','\
Jan Garber And His Orchestra•Street Of Dreams•Decca•1961','\
Pete Jolly•Herb Alpert Presents Pete Jolly•A&M Records•1968','\
David Liebman•Classic Ballads•Candid•1991','\
Tiger Okoshi•Echoes Of A Note•JVC•1993','\
The Mariachi Brass•Double Shot•World Pacific Records•1966','\
Les Brown And His Band Of Renown•Les Brown\'s In Town•Capitol Records•1956'),'\
\
Dancing On the Ceiling\
':('\
Ella Fitzgerald•Sings The Rodgers & Hart Song Book Vol. 5•Verve Records•0','\
Smith Ballew And His Orchestra•Snuggled On Your Shoulder / Dancing On The Ceiling•Oriole (3)•1932','\
Dorothy Ashby•The Jazz Harpist•Regent•1957','\
Billy Butterfield And The Essex Five•College Jazz Sampler•Somerset•1955','\
Hazel Scott•Great Scott!•Columbia•1947','\
Frank Wess•North South East.....Wess•Savoy Records•1956','\
The Jazz Modes•Jazzville Vol. 1•Dawn (3)•1956','\
Stan Freeman•Piano Moods•Columbia•1950','\
Ben Webster•At The Nuway Club October 5th 1958•Nostalgia (8)•1982','\
Sonny Stitt•Sonny Stitt•Argo (6)•1958','\
Ralph Flanagan And His Orchestra•Let\'s Dance Again With Flanagan•RCA Victor•1951','\
The Red Norvo Trio•Dancing On The Ceiling With The Red Norvo Trio•Brunswick•0','\
Frank Sinatra•In The Wee Small Hours - Part 2•Capitol Records•1955'),'\
\
Darn That Dream\
':('\
Sam Taylor (2)•Misty / Darn That Dream•Decca•1962','\
Miles Davis And His Orchestra•Venus De Milo / Darn That Dream•Capitol Records•1950','\
Miles Davis•Classics In Jazz Part 3•Capitol Records•0','\
Monica Zetterlund•Swedish Sweet 2•Columbia•1958','\
Art Farmer•In Concert•Enja Records•1986','\
Dexter Gordon Quartet•Swiss Nights Vol. 2•Steeplechase•1978','\
Andrew Hill•Verona Rag•Soul Note•1987'),'\
\
Day By Day\
':('\
Shakatak•Day By Day•Polydor•1985','\
Les Brown And His Orchestra•Day By Day / Doctor Lawyer Indian Chief•Columbia•1946','\
The Court Jesters (3)•Rangers Waltz / Day By Day•Clarion Records (2)•0','\
Roy Meriwether•Nubian Lady•Stinger Productions•1973','\
Chris Montez•Nothing To Hide / Day By Day•A&M Records•1974','\
Frank Sinatra•Day By Day / You Are Too Beautiful•Columbia•1946','\
Shirley Bassey•Never Never Never •United Artists Records•1973','\
Sonny Rollins•Live In London Volume 2•Harkit Records•2005','\
Milt Buckner•I Giganti Del Jazz Vol. 13•Curcio•1980','\
Yuri Tashiro Piano Trio•Digital Explosion•Eastworld•1980','\
Nenad Vasilić•Live In Theater Akzent•Metropolis Records (4)•2018','\
Brian Mann•Café Du Soleil•Narada Equinox•1990','\
Greetje Kauffeld•And Let The Music Play•Polydor•1974','\
Ray Anthony•Ray Anthony Plays For Dancers In Love Part 1•Capitol Records•0','\
Inaba & Nakamure Duo•Conversation•Three Blind Mice•1975','\
Al Grey•Dizzy Atmosphere•Specialty•1957','\
Yoshiko Goto•I\'m Glad There Is You•Denon•1972','\
Coleman Hawkins All Star Band•At Newport•Verve Records•1958','\
Sandviken Big Band•Hello Dolly•Intersound (5)•1980','\
Lou Donaldson•Poinciana•Jazz Bird•1979'),'\
\
Day Dream\
':('\
Joe Kučera•Balance•Music Vision (3)•1986','\
Johnny Hodges And His Orchestra•Day Dream / Junior Hop•Bluebird (3)•1941','\
Day Is Over•Day Is Over•Scandia•1975','\
Yuri Tashiro Piano Trio•Digital Explosion•Eastworld•1980','\
Bing Crosby•Bing With A Beat Vol. II•RCA Victor•1957','\
Red Callender•Callender Speaks Low•Crown Records (2)•1957','\
June Christy•The Misty Miss Christy Part 2•Capitol Records•0','\
Inaba & Nakamure Duo•Conversation•Three Blind Mice•1975','\
Erica Lindsay (2)•Dreamer•Candid•1992','\
Marion Brown•Passion Flower•Baystate•1978','\
Helen Merrill•The Feeling Is Mutual•Milestone (4)•1967','\
Tanzorchester Horst Wende•Strict Tempo Dancing - Slow Foxtrot•Polydor•1961','\
Johnny Hodges And His Orchestra•More Of Johnny Hodges And His Orchestra Album #2•Clef Records•1954','\
Roland Hanna Trio•Dream•Venus Records (5)•2001','\
Jacinta (2)•Day Dream•EMI Music Portugal•2006'),'\
\
Day In Vienna\
':('\
Roy Hargrove•Nothing Serious•Verve Records•2006','\
Roy Hargrove Quintet•Nothing Serious•Verve Records•2005','\
Dexter Gordon•A Day In Copenhagen•MPS Records•1969','\
Various•On The Spot - A Peek At The 1960\'s Nordic Jazz Scene•Ricky-Tick Records•2006','\
Nicola Conte•Cosmic Forest - The Spiritual Sounds Of MPS•MPS Records•2018','\
Janis Siegel•At Home•Atlantic•1987','\
Johnny Dorelli•Viaggio Sentimentale•CGD•1965','\
Jan Garber And His Orchestra•Golden Waltzes From The Blue Room•Decca•0','\
Robert Mandell•Beyond The Blue Horizon•Warwick Records•0','\
Al Bowlly•Goodnight Sweetheart•World Records (6)•1986','\
This That & The 3rd•Summer In Vienna•Personal Records (2)•2014','\
Frankie Carle And His Rhythm•37 Favourites For Dancing•RCA•1959'),'\
\
Day In Day Out\
':('\
no artist•Adiós •Hispavox•1961','\
Stan Kenton And His Orchestra•Road Show Volume 1•Creative World•1975','\
Slide Hampton•Jazz With A Twist•Atlantic•1962','\
Ronnie Scott•The Couriers Of Jazz•London Records•1960','\
The Horace Silver Trio•Vol. 2•Blue Note•1954','\
Smith Dobson•Sasha Bossa•Quartet Records (2)•1988','\
Jackie Jocko•Like Wow•Wynne•1959','\
Carmen McRae•Carmen McRae At The Flamingo Jazz Club•Ember Records•1961','\
Joe Kennedy•Magnifique!•Black And Blue•1980','\
The Page Cavanaugh Big Band•Something\'s Happening at Page Cavanaugh\'s!•Reprise Records•1961','\
Frank Strozier•Cool Calm And Collected•Vee Jay Records•1993','\
Dorothy Donegan•Donnybrook With Donegan•Capitol Records•1959','\
Stan Levey•This Time The Drum\'s On Me•Bethlehem Records•1955','\
Ray Brown All-Star Big Band•With The All-Star Big Band•Verve Records•1962','\
The Bob Wilber All Star Jazz Band•Sing Or Play With A Band•Music Minus One•0','\
Duke Ellington•Duke Ellington (Historic Recording)•LaserLight•0','\
Al Grey•Boss Bone•Argo (6)•1963','\
The Bob Wilber All Star Jazz Band•Sing Or Play With A Band•Music Minus One•0','\
Frank Sinatra•Come Dance With Me (Part 3)•Capitol Records•1959','\
Billie Holiday•Songs For Distingué Lovers•Verve Records•1958'),'\
\
Day Waves\
':('\
Various•Music For Wellbeing III•Fønix Musik•2004','\
Stan Getz•Captain Marvel•Columbia•1975','\
Joe Carter Quartet•My Foolish Heart•Empathy Records•1985','\
Jay Arrigo & Friends•Sounds: Like Fun•AVI Records•1984','\
Earl Bostic And His Orchestra•Earl Bostic And His Alto Sax (No.2)•Parlophone•1954','\
Naoya Matsuoka•Splash & Flash•Warner Bros. Records•1985','\
Aske Jacoby•Transfer Power•Sweet Silence Record Company•2004','\
Susanne Sundfør•Take One•Your Favourite Music•2008','\
Mo Foster•Time To Think•Primrose Hill Records•2002','\
John Murtaugh•Blues Current•Polydor•1970','\
Jonathan Cain•For A Lifetime•Higher Octave Music•1998'),'\
\
Days and Nights Waiting\
':('\
Charles Lloyd•In The Soviet Union: Recorded At The Tallinn Jazz Festival•Atlantic•1970','\
Steve Wilson (2)•Passages•Stretch Records•2000','\
The Blue Vipers Of Brooklyn•Forty Days And Forty Nights•Not On Label•0','\
Keith Jarrett•Le Virtuose Du Piano•Wea Music•1996','\
Kathy Kirby•Kathy Kirby Sings 16 Hits From Stars And Garters•Decca•1963','\
András Wahorn•Tengerhajózás / Seafaring•Bad Quality Records•1991','\
Francis Goya•MP3 Collection•Zebra Studio (2)•0'),'\
\
Days Of Wine And Roses\
':('\
Eddie "Lockjaw" Davis•Days Of Wine And Roses / Speak Low•RCA Victor•1966','\
Woody Herman And His Orchestra•Jazz Me Blues•Philips•0','\
Dexter Gordon Quartet•Swiss Nights Vol. 1•SteepleChase•1976','\
Eddie Cano•Our Day Will Come / Days Of Wine And Roses•Reprise Records•1963','\
Henry Mancini And His Orchestra•Days Of Wine And Roses / Seventy Six Trombones•RCA Victor•1962','\
Dexter Gordon•Tangerine•Prestige•1975','\
Andy Williams•Can\'t Get Used To Losing You•Columbia•1963','\
Vince Guaraldi•Vince Guaraldi \ Bola Sete \ And Friends•Fantasy•1963','\
Cedar Walton•Spectrum•Prestige•1968','\
Rudolph Statler Orchestra And Chorus•Henry Mancini Favorites•Wyncote•1964','\
Jimmy McGriff•The Days Of Wine And Roses•Solid State Records (2)•1967','\
Henry Mancini And His Orchestra•Big Noise From Winnetka / The Days Of Wine & Roses•RCA•1962','\
Hideo Ichikawa•Invitation•RCA•1976','\
Kunihiko Sugano•The Days Of Wine And Roses•Nadja•1976','\
Clark Terry•Brhams Lullabye•Bingow Records•1981','\
John Wood (12)•"Say Hey"•Los Angeles Phonograph Records•1978'),'\
\
De Pois De Amor O\'Vazio\
':('\
Wayne Shorter•Odyssey Of Iska•Blue Note•1971','\
The 4•Square Game•Polydor•1984'),'\
\
Dear Old Stockholm\
':('\
The Miles Davis Sextet•Dear Old Stockholm / Would\'n You•Blue Note•0','\
The Miles Davis Quintet•Davis\' Cup•Philips•1956','\
John Coltrane•Dear Old Stockholm•GRP•1993','\
Donald Byrd Quintet•Byrd In Paris•Brunswick•1958','\
Louis Van Dyke Trio•Loosdrecht Jazz Concours•Philips•1961','\
Bud Powell•Writin\' For Duke 63•Mythic Sound•1989','\
Scott Hamilton•Swedish Ballads ... & More•Stunt Records•2013','\
John Coltrane•Ride Again!!•Impulse!•1968','\
Richard Davis (2)•With Understanding•Muse Records•1975','\
Richard Davis (2)•The Philosophy Of The Spiritual•Cobblestone•1972','\
Miles Davis•Young Man With A Horn•Blue Note•1952','\
John Coltrane•Big Nick•MCA Records•1981'),'\
\
Dearly Beloved\
':('\
Benny Goodman And His Orchestra•Dearly Beloved/I\'m Old Fashioned•Columbia•1942','\
Sonny Rollins•Our Man In Jazz•RCA Victor•1963','\
Glenn Miller And His Orchestra•Dearly Beloved / I\'m Old Fashioned•Victor•1942','\
John Coltrane•Sun Ship•Impulse!•1971','\
no artist•Mambo With Tjader Volume 3•Fantasy•1955','\
Tommy Whittle Quintet•A Touch Of Latin•Saga (5)•1958'),'\
\
Decision\
':('\
Sonny Rollins•Decision•Blue Note•1957','\
Frédéric Alarie•Moon Bass•Fidelio Audio•0','\
Paul Motian•Reincarnation Of A Love Bird•JMT•1994','\
The Tim Whitehead Band•Decision•Editions EG•1988','\
The Thing (2)•Again•The Thing Records•2018','\
Sonny Rollins•Sonny Rollins Volume 1•Blue Note•1957','\
Sam Phipps•Animal Sounds•Dream Records (19)•1981','\
Frank Lowe•Decision In Paradise•Soul Note•1985'),'\
\
Dedicated To You\
':('\
Billy Eckstine•You\'re All I Need / Dedicated To You•MGM Records•1950','\
no artist•Havana Cafe•Chesky Records•1992','\
The Mills Brothers•Dedicated To You / Big Boy Blue•Decca•1937','\
McCoy Tyner•Jazz Roots•Telarc•2000','\
Fred Hersch•Alone At The Vanguard•Palmetto Records•2011','\
The Lonnie Plaxico Group•Live At Jazz Standard•441 Records•2003','\
Billy Eckstine•Dedicated To You•MGM Records•1956','\
Fumio Karashima•Piranha•Whynot•1976','\
Albert Mangelsdorff•The Wide Point•MPS Records•1975','\
Nat King Cole•Tell Me All About Yourself Part 2•Capitol Records•0','\
Alan Pasqua•Dedications•Postcards•1999','\
John Coltrane•John Coltrane And Johnny Hartman•Impulse!•1963','\
The Manhattan Transfer•Smile Again (Dedicated To Angela From Alan)•Atlantic•1981','\
Steve Khan•Public Access•GRP•1990','\
The Keith Tippett Group•Dedicated To You But You Weren\'t Listening•Vertigo•1971'),'\
\
Dee Song\
':('\
Tatsu Aoki•Basser Live•Asian Improv Records•1999','\
Shamek Farrah And Folks•La Dee La La•Ra Records (2)•1980','\
Kenny Drew•Moonlit Desert•Baystate•1982','\
Doctorolive•First Dee-Jay On The Moon•Radikal Records•1999','\
Andy Narell•The Passage: Music For Steel Orchestra•Heads Up International•2004','\
Booker Ervin•Down In The Dumps•Savoy Records•1978','\
Enrico Pieranunzi Marc Johnson Joey Baron•Deep Down•Soul Note•1987','\
Chick Corea•Verve Jazz Masters 3•Verve Records•1993','\
Lungiswa Plaatjies•Ekhaya•M.E.L.T. 2000•2000','\
Dee Dee Bridgewater•Dee Dee\'s Feathers•Okeh•2015','\
Roger Williams (2)•Songs Of The Fabulous Forties - Part 1•Kapp Records•1960'),'\
\
Deep Purple\
':('\
Larry Clinton And His Orchestra• My Reverie / Deep Purple•Bell Records•0','\
Artie Shaw And His Orchestra•Deep Purple / Pastel Blue•Bluebird (3)•1939','\
Don Byas Quintet•Deep Purple / Them There Eyes•Jamboree Records (2)•1945','\
Billy Cotton And His Band•Deep Purple / Little Sir Echo•Rex•1939','\
Art Tatum Trio•Moonglow/Honeysuckle Rose•Brunswick•0','\
Art Tatum•Deep Purple / Tea For Two•Decca•1939','\
Jimmy Jackson & His Orchestra•Deep Purple / Snow Plow•RPM Records (5)•1952','\
Earl Bostic•Smoke Rings / Deep Purple•Gusto Records (2)•1977','\
Earl Bostic And His Orchestra•Deep Purple / Smoke Rings•King Records (3)•1953','\
Larry Clinton And His Orchestra•My Reverie / Deep Purple•RCA Victor•1955','\
Larry Clinton And His Orchestra•Larry Clinton•RCA Victor•1958','\
Percy Faith & His Orchestra•Oodles Of Noodles•RCA Victor•1949','\
Art Pepper Quartet•Straight Ahead Jazz Vol. Two•Straight Ahead Jazz•0'),'\
\
Delevans\
':('\
Jeff Lorber•It\'s A Fact•Arista•1982'),'\
\
Delgado\
':('\
Eddie Gomez•Mezgo•Epic/Sony•1986','\
Eddie Gomez•Discovery•Columbia•1986','\
Richard Stoltzman•Innervoices•RCA Victor•1989','\
Various•Gute Zeiten Schlechte Zeiten Vol. 16 - Die Doppel-Duft CD•Edel Records•1998'),'\
\
Delores\
':('\
Kenny Barron•Sunset To Dawn•Muse Records•1973','\
Vincent Herring•Folklore - Live At The Village Vanguard•Limelight•1992','\
Carl Allen & Manhattan Projects•Echoes Of Our Heroes •Alfa Jazz•1993','\
Courtney Pine•Journey To The Urge Within•Antilles New Directions•1986','\
Various•The Best Of Club 51 Records•Relic Records•0','\
Russ Morgan And His Orchestra•Dance Along With Russ Morgan And His Music In The Morgan Manner  •Everest•0','\
Frankie Carle And His Orchestra•Top Of The Mark•RCA Victor•1960','\
Weather Report•Live In Offenbach 1978•Art Of Groove•2011','\
Weather Report•Forecast: Tomorrow•Legacy•2006','\
Various•Instrumentals Soul-Style 2•History Of Soul•2016'),'\
\
Deluge\
':('\
Sam Rivers•Vol. 2•Improvising Artists Inc.•1977','\
Dave Douglas•The Infinite•Bluebird (3)•2002','\
Wayne Shorter•Juju•Blue Note•1964','\
Enrico Pieranunzi Trio•Infant Eyes•Challenge Records (3)•2000'),'\
\
Desafinado\
':('\
Lloyd Mayers•Desafinado / Alone Together•United Artists Records•1962','\
Alice Babs•Desafinado / Jazzfuga•Polydor•1963','\
Enoch Light Big Band Bossa Nova•Desafinado / One Note Samba•Command•1962','\
Si Zentner And His Orchestra•The Elephant\'s Tango / Desafinado•Liberty•1962','\
Dizzy Gillespie•Desafinado / Pau De Arara•Philips•1962','\
Astrud Gilberto•The Girl From Ipanema / Desafinado•Old Gold (2)•1990','\
Kenny G (2)•What A Wonderful World•Arista•1999','\
Pat Thomas (5)•Desafinado / One Note Samba•Verve Records•1962','\
Dizzy Gillespie•The New Sound In Jazz: "Bossa Nova: - Desafinado•Philips•1962','\
Stan Getz•Play Desafinado & One Note Samba•Verve Records•1962','\
Billy Patt Quintett•Passion (An Act Of Love)•Sabra Records•1964','\
McCoy Tyner Quintet•Jazz Jamboree 74 Vol. 2•Polskie Nagrania Muza•1975'),'\
\
Desert Air\
':('\
Gary Burton•Works•ECM Records•1984','\
Abdullah Ibrahim•Desert Flowers•Enja Records•1992','\
Gary Burton / Chick Corea•Crystal Silence•ECM Records•1973','\
Ron Escheté•Spirit\'s Samba•JAS (2)•1977','\
Manfred Schoof•Timebreaker•UBM Records•1990','\
Chick Corea•Selected Recordings•ECM Records•2002','\
Ross Traut•The Duo Life•Columbia•1991','\
Lerner & Loewe•The Little Prince (Original Motion Picture Soundtrack)•ABC Records•1974','\
Various•Pop Classics - The Long Versions 3•Arcade•1992','\
Uton•Violin Massage•Om Ha Sva Ha Ksha Ma La Va Ra Yam•2007'),'\
\
Desire\
':('\
Andrew Hill•Change•Blue Note•2007','\
Goran Kajfeš Subtropic Arkestra•The Reason Why Vol. 1•Headspin Recordings•2013','\
no artist•My Surpressed Desire / Rhythm King•Columbia•1929','\
The Human Arts Ensemble•Under The Sun•Not On Label•1974','\
Núria Andorrà•Kokoro•Sirulita•2018','\
Chris Connor•That\'s My Desire•Atlantic•1960','\
Louis Armstrong•Takes Two To Tango / That\'s My Desire•Brunswick•1952','\
Louis Armstrong•That\'s My Desire / Baby It\'s Cold Outside•Decca•1952','\
Werner Müller Und Sein Orchester•La Cumparsita•Decca•1955','\
Ella Fitzgerald•That\'s My Desire / A Sunday Kind Of Love •Decca•0'),'\
\
Detour Ahead\
':('\
Woody Herman And His Orchestra•Not Really the Blues / Detour Ahead•Capitol Records•1949','\
Fumio Karashima•Transparent•Polydor•1987','\
Milt Jackson•Goodbye•CTI Records•1974','\
Rein De Graaff / Dick Vennik Quartet•Modal Soul•Timeless Records (3)•1977','\
Junior Cook•Somethin\'s Cookin\'•Muse Records•1982','\
Cedar Walton•My Funny Valentine•Bellaphon•1991'),'\
\
Devil May Care\
':('\
Miles Davis•Blue Xmas•Columbia•2014','\
Miles Davis•Seven Steps To Heaven / Devil May Care•Columbia•0','\
Miles Davis•Blue Christmas•CBS•1983','\
Miles Davis•Facets•CBS•1967','\
SoulLexa•Demo-CD•Not On Label (SoulLexa meets JazzStefan Self-released)•2006','\
Bob Dorough•Devil May Care•52e Rue Est•1983','\
Julie Kelly•Some Other Time•Chase Music Group•1989','\
Bob Dorough•Devil May Care•Bethlehem Records•1956','\
Tommy Dorsey And His Orchestra•What\'ll I Do?•RCA•0','\
Miles Davis•Basic Miles - The Classic Performances Of Miles Davis•Columbia•1973','\
Jackson Sloan•Old Angel Midnight•Prima Records•1989'),'\
\
Dewey Square\
':('\
Charlie Parker•Charlie Parker On Dial Volume 4•Spotlite Records•1970','\
The Charlie Parker Quintet•Dewey Square / Quasimado•Blue Star•0','\
Lou Donaldson•Lou Takes Off•Blue Note•1958','\
The Charlie Parker Quintet•Bongo Bop•Sonet•1960','\
Dewey Redman Quartet•The Struggle Continues•ECM Records•1982','\
Phil Woods•The Young Bloods•Prestige•1956','\
Jimmy Heath•New Picture•Landmark Records (3)•1985','\
Blake Hawley•The Standard Duo•Not On Label (Blake Hawley Self-released)•2013','\
Birdology•Birdology (Live At The TBB Jazz Festival Vol. 2)•Verve Records•1990','\
Klaus Weiss Quintet•Salt Peanuts•Jeton•1982','\
Joe Lovano Us Five•Bird Songs•Blue Note•2011','\
Charlie Parker•All Stars Quintet & Sextet Volume 2•UP•1978','\
Ed Blackwell Trio•Walls-Bridges•Black Saint•1996'),'\
\
Dexter\
':('\
Dexter Gordon•Dexter Rides Again•Savoy Records•1958','\
Dexter Gordon•Long Tall Dexter•Savoy Records•1976','\
Dexter Gordon•Master Takes. The Savoy Recordings•Savoy Jazz•1985','\
Dexter Gordon•Dextrose•TIM GmbH•2000','\
Dexter Gordon Quartet•Billie\'s Bounce•SteepleChase•1983','\
Dexter Gordon•Settin\' The Pace•Savoy Jazz•1998','\
Wingy Carpenter And The Wingies•Preachin\' Trumpet Blues / Dexter Blues•Brunswick•0','\
Hampton Hawes•A Little Copenhagen Night Music•Arista•1977','\
Sonny Grey•Parisian Concert•Futura Records (2)•1973','\
Dexter Gordon•Live At The Amsterdam Paradiso Volume One•Affinity•1980','\
Dexter Gordon Quartet•Cheese Cake•SteepleChase•1979'),'\
\
Dexterity\
':('\
Charlie Parker•Bird Of Paradise / Dexterity•Dial Records (3)•1949','\
The Joe Daley Trio•At Newport \'63•RCA Victor•1963','\
Charlie Parker•Charlie Parker On Dial Volume 4•Spotlite Records•1970','\
Paul Chambers (3)•Chambers\' Music: A Jazz Delegation From The East•Jazz: West•1956','\
The Art Ensemble Of Chicago•Message To Our Folks•BYG Records•1969','\
Jason Stein Quartet•Lucille!•Delmark Records•2017','\
Kenny Barron•What If?•Enja Records•1986','\
Yusef Lateef•Lost In Sound•Charlie Parker Records•1962'),'\
\
Diane\
':('\
Billy May And His Orchestra•Diane / Perfida•Capitol Records•0','\
Bo Rhambo Combo•Diane•Imperial•1958','\
Bo Rhambo•Diane•Imperial•1962','\
Mantovani And His Orchestra•Diane / Charmaine•Decca•1951','\
The Miles Davis Quintet•Steamin\' With The Miles Davis Quintet•Metronome•1961','\
The Bachelors•I Believe / Diane•Decca•1964','\
Miles Davis•Surry With The Fringe On Top•Prestige•1963','\
Joe Harnell & His Orchestra•Diane •Kapp Records•0','\
The Bachelors•Diane•London Records•1964','\
Ping Pong•Rhythm Walk•Big Mouth•1982','\
The New Woody Shaw Quintet•Vol.1 At Onkel Pö\'s Carnegie Hall Hamburg 1982•Jazzline•2017'),'\
\
Dienda\
':('\
Branford Marsalis•Selections•CBS/Sony•1987','\
Branford Marsalis•Royal Garden Blues•CBS•1986','\
Laurent Coq Quartet•Like A Tree In The City•Cristal Records•2004','\
Jan Maksimovič•Thousands Seconds Of Our Life•NoBusiness Records•2019','\
Sting•...All This Time•A&M Records•2001'),'\
\
Dig\
':('\
Miles Davis And His Band•Dig?•Prestige•1952','\
Flavio Ambrosetti•Jazz Stars•Dire (2)•1968','\
Art Farmer•Trumpets All Out•Prestige•1964','\
Raise The Roof!•Horns & Beats•JJ-Tracks•1999','\
Art Farmer•Three Trumpets•Prestige•1957','\
Hank Mobley•Soul Station•Blue Note•1960','\
Julius Wechter•Can You Dig It?•A&M Records•0','\
Ted Heath And His Music•Asia Minor•Decca•1955','\
The Jonah Jones Quartet•I Dig Chicks!•Capitol Records•1959'),'\
\
Dindi\
':('\
LA4•The L.A.4•Concord Jazz•1976','\
Victor Assis Brasil•Toca Antonio Carlos Jobim•Quartin•1970','\
Arturo Sandoval•L. A. Meetings•CuBop•2001','\
Kazumi Watanabe•Olive\'s Step•Better Days (2)•1977','\
Janet Lawson•Two Little Rooms•United Artists Records•1970'),'\
\
Disguise Sphinx\
':('\
Ornette Coleman•Something Else!!!!•Contemporary Records•1958','\
Ornette Coleman•The Shape Of Jazz To Come•Not Now Music•2010','\
Various•100 Hits Jazz•100 Hits•2013'),'\
\
Django\
':('\
The Modern Jazz Quartet•The Modern Jazz Quartet Plays Django ･ Milano•Prestige•1955','\
Etat Major•Django Jet•Mankin Records•1982','\
Joe Pass•For Django•Pacific Jazz•1964','\
Miles Davis•The Winners Of Down Beat\'s Readers Poll 1960 "Horns "•Philips•1960','\
The Modern Jazz Quartet•Vol. 2: Django / Milano / One Bass Hit•Metronome•1955','\
Quintette Du Hot Club De France•Paramount Stomp / Swinging With Django•Victor•1941','\
Chet Baker•Studio Trieste•CTI Records•1982'),'\
\
Do Nothing \'Til You Hear From Me\
':('\
Teddy Charles Trio•3 For Duke•Jubilee•1957','\
Johnny Griffin•Do Nothing \'Til You Hear From Me•Riverside Records•1963','\
Mose Allison•Autumn Song•Prestige•1959','\
Susie Arioli Swing Band•Pennies From Heaven•Justin Time•2002','\
Don Burrows•Burrows\' Jazz Brothers - A Retrospective•ABC Records (3)•1982','\
Carmen Lundy•Night And Day•CBS/Sony•1987','\
The Australian All-Stars•Jazz For Beach-Niks•Columbia•1959','\
The Australian All-Stars•Jazz For Beach-Niks•Columbia•1959','\
Duke Ellington•The Essence Of Duke Ellington•Legacy•1981','\
Molly Johnson•Because Of Billie•Universal Music Canada•2014','\
Steve Tyrell•This Guy\'s In Love•Columbia•2003','\
Louis Armstrong•I\'ve Got The World On A String•Verve Records•1960'),'\
\
Do You Know What It Means\
':('\
Louis Armstrong And His Dixieland Seven•Do You Know What It Means To Miss New Orleans / Endie•RCA Victor•1946','\
Pete Fountain•A Closer Walk•Coral•1959','\
Louis Armstrong•Do You Know What It Means To Miss New Orleans / Jack-Armstrong Blues•RCA•0','\
Roman New Orleans Jazz Band•Do You Know What It Means To Miss New Orleans / Down By The Riverside•RCA Italiana•1959','\
Louis Armstrong•The Standard Oil Sessions•Dot Time Records•2017','\
no artist•Do You Know What It Means To Miss New Orleans? / Blues My Naughty Sweetie Gives To Me•Good Time Jazz•1959','\
no artist•Bob Scobey\'s Frisco Band•Good Time Jazz•1953','\
Louis Armstrong And His All-Stars•Satchmo The Great•Philips•1958','\
Kid Ory•The Kid Ory Story: Storyville Nights•Verve Records•1962','\
Joe Sealy•Double Entendre•Sea Jam•1990','\
Old Timers•Aquarium Live No. 4•Poljazz•1977','\
Wild Bill Davison•Jazz On A Saturday Afternoon Vol. 3•Jazzology•0','\
Stéphane Grappelli•Live In Warsaw•no label•1996','\
Don Burrows•George Golla Duo•Other Places Other Times•First American Records•1980'),'\
\
Doce Presenca\
':('\
Simone (3)•Vício•Discos CBS•1987','\
Rosa Passos•Romance•Telarc•2008','\
Eliane Elias•Fantasia•Blue Note•1992','\
Josee Koning•Dois Mundos•VIA Jazz•1998'),'\
\
Dock Of The Bay The\
':('\
Oliver Nelson•Melissa / The Dock Of The Bay•Impulse!•0','\
Percy Sledge•The Dock Of The Bay / Warm And Tender Love•Maybellene•1987','\
no artist•(Sittin\' On) The Dock Of The Bay•A&M Records•1969','\
no artist•(Sittin\' On) The Dock Of The Bay•A&M Records•1969','\
Nino Tempo & April Stevens•Sea Of Love / (Sittin\' On) The Dock Of The Bay•Bell Records•1969','\
Jimmy Caravan•Hey Jude•Vault•1969','\
B & G Rhythm•B & G Rhythm•Polydor•1978','\
Takeshi Inomata & His West Liners•Come Together!•VICTOR WORLD GROUP•1969','\
Mongo Santamaria•Dock Of The Bay•Harmony (4)•1971','\
Jimmy Smith•I\'m Gon\' Git Myself Together•MGM Records•1971','\
no artist•Crystal Illusions•A&M Records•1969'),'\
\
Dogs in the Wine Shop\
':('\
Michael Brecker•Now You See It... (Now You Don\'t)•GRP•1990'),'\
\
Doin\' the Pig\
':('\
Gary Burton•Throb•Atlantic•1969','\
Gary Burton•Gary Burton & Keith Jarrett / Gary Burton: Throb•Rhino Records (2)•1994'),'\
\
Dolphin\
':('\
Miles Davis•On Green Dolphin Street•Jazz Door•1992','\
Red Callender Sextet•Dolphin Street Boogie / Poinciana•Recorded In Hollywood•1951','\
Miles Davis•The Miles Davis Quintet & Sextet•CBS/Sony•1973','\
Julian Priester•Polarization•ECM Records•1977','\
Victor Feldman•Green Dolphin Street / Overfat Cat•Vee Jay Records•1965','\
The Miles Davis Sextet•Miles At Newport•CBS•1968','\
Ahmad Jamal•Freeflight•Impulse!•1971','\
The Three Sounds•On Green Dolphin Street / Love For Sale•Blue Note•1960','\
Herbie Hancock•Dedication•CBS/Sony•1974','\
Miles Davis•The Final Tour: Copenhagen March 24 1960•Columbia•2018','\
Phil Manzanera•Mato Grosso•Black Sun (2)•1990','\
Miles Davis•Blue Christmas•CBS•1983','\
Sonny Rollins Quartet•"Live" In Europe•Unique Jazz•0','\
Miles Davis•Copenhagen 1960•Royal Jazz•1989','\
Monty Alexander•Unlimited Love - Live & In Concert•BASF•1976'),'\
\
Dolphin Dance\
':('\
The Miles Davis Sextet•Miles At Newport•CBS•1968','\
Ahmad Jamal•Freeflight•Impulse!•1971','\
Herbie Hancock•Dedication•CBS/Sony•1974','\
Miles Davis•The Miles Davis Quintet & Sextet•CBS/Sony•1973','\
Oscar Peterson•The Sound Of The Trio•Verve Records•1961','\
Al Haig•Strings Attached•Choice (7)•1975','\
Ron Carter•Third Plane•JVC•1978','\
Herbie Hancock Trio•Herbie Hancock Trio With Ron Carter + Tony Williams•CBS/Sony•1981','\
Oscar Peterson•The Sound Of The Trio•Verve Records•1961'),'\
\
Domingo\
':('\
The Eddie "Lockjaw" Davis Quintet•Jaws In Orbit•Metronome•1960','\
Various•Hungarian Noir. A Tribute To The Gloomy Sunday•Piranha•2016','\
Tony Christie•No Vayas A Reno•MCA Records•1973','\
Lee Morgan•Vol. 3•Blue Note•1957','\
Eddie "Lockjaw" Davis•The Best Of Eddie "Lockjaw" Davis With Shirley Scott•Prestige•1970','\
no artist•Pico Bello 15. Folge / Pico Bello 16. Folge•Electrola•0','\
Charly Antolini•In The Groove•MPS Records•1972','\
Cal Tjader•A Fuego Vivo•Concord Jazz Picante•1982'),'\
\
Domino Biscuit\
':('\
Gary Burton•Works•ECM Records•1984','\
Gary Burton•Hotel Hello•ECM Records•1975'),'\
\
Donna Lee\
':('\
Charlie Parker•Charlie Parker Memorial Volume Two•Realm Jazz Savoy Series•1963','\
Charlie Parker•Buzzy•Savoy Records•1947','\
Lee Konitz•Lee Konitz With Warne Marsh•Atlantic•1955','\
Steve Lacy•The Straight Horn Of Steve Lacy•Candid•1960','\
Don Patterson•Boppin\' & Burnin\'•Prestige•1968','\
Art Pepper•Arthur\'s Blues•Original Jazz Classics•1991','\
Arturo Sandoval•No Problem - Recorded Live At Ronnie Scott\'s Club•Jazz House•1987','\
Wardell Gray Sextet•Out Of Nowhere•Straight Ahead Jazz•0','\
Charlie Parker•The Complete Studio Recordings On Savoy Years Vol. 2•Savoy Jazz•2000'),'\
\
Don\'t Ask Why\
':('\
Ruth Welcome•Sentimental Zither•Capitol Records•1964'),'\
\
Don\'t Be Blue\
':('\
Elvis Presley•Elvis In The ‘50s - 1956•RCA•1979','\
Cootie Williams And His Orchestra•Cootie Williams And His Orchestra•Storyville•0','\
Mars (4)•Rehearsal Tapes And Alt. Takes NYC 1976-1978•Anòmia•2012','\
Mel Tormé•The Best Of The Capitol Years•Capitol Records•1992','\
Benny Goodman•The Gold Collection•Retro (2)•1997','\
Eubie Blake•The Eighty-Six Years Of Eubie Blake•Columbia•1973','\
Eubie Blake•The Eighty-Six Years Of Eubie Blake•Columbia•1973','\
Glenn Miller•The All-Time Greatest Hits•Starlite (4)•1988'),'\
\
Don\'t Be That Way\
':('\
no artist•Jim Robinson And His New Orleans Band•Pearl Records (5)•1964','\
Joe Pass•Virtuoso In New York•Pablo Records•2004','\
Norio Maeda•N.Maeda Meets 5 Saxophones•Audio Lab. Record•1976','\
Various•Big Band•RCA Victor•1979','\
Benny Goodman•The Gold Collection•Retro (2)•1997','\
Syd Lawrence And His Orchestra•Big Band Swing•Philips•1983','\
no artist•Anita Sings For Oscar•Lone Hill Jazz•2008','\
Big Maybelle•Candy!•Savoy Jazz•2002','\
Glenn Miller•The All-Time Greatest Hits•Starlite (4)•1988','\
Various•Slow Dancing Through The Years•Sony Music Special Products•1994','\
Ella Fitzgerald•All My Life•Le Chant Du Monde•2010'),'\
\
Don\'t Blame Me\
':('\
Barry Harris (2)•At The Jazz Workshop•Riverside Records•1960','\
Howard McGhee•That Bop Thing•Bethlehem Records•1978','\
Miles Davis•The Very Best Of...•FonoTeam•0','\
Frank Morgan•Love Lost & Found•Telarc•1995','\
Art Tatum•Master Of Jazz 3 - Art Tatum•EMI•1976','\
Charlie Parker•Charlie Parker•Nocturne•2003','\
Count Basie Orchestra•"Early Count"•MCA Records•0'),'\
\
Don\'t Get Around Much Anymore\
':('\
Woody Herman•1963 – The Swingin’est Big Band Ever•Philips•1963','\
Woody Herman•1963 – The Swingin’est Big Band Ever•Philips•1963','\
Duke Ellington•Duke Ellington\'s Greatest Hits•Harmony (4)•1971','\
Elsie Bianchi Trio•At Chateau Fleur De Lis•Sonorama•2017','\
Louis Armstrong•Recording Together For The First Time / The Great Reunion Of Louis Armstrong And Duke Ellington•Mobile Fidelity Sound Lab•0','\
Duke Ellington•Duke Ellington•RCA•1978','\
Eddie Brunner•In Memoriam•Swiss Jazz•0','\
Various•20 Original Hit Songs Of 1949•The CDCard Company•2006','\
Natalie Cole•Unforgettable With Love•Elektra•1991','\
Sammy Davis Jr.•The Best Of Sammy Davis Jr.•Decca•1966','\
Nat King Cole•The Natural Collection•The Natural Collection•1996'),'\
\
Don\'t Worry About Me\
':('\
Carol Kidd•All My Tomorrows•Aloi Records•1985'),'\
\
Doodlin\'\
':('\
Ray Charles•Doodlin\'•Atlantic•1960','\
Dizzy Gillespie•Joogie Boogie / Doodlin\'•Verve Records•1962','\
Lambert Hendricks & Ross•Doodlin\' / Spirit Feel•United Artists Records•1959','\
Dizzy Gillespie Big Band•Doodlin\' / Dizzy\'s Blues•Norgran Records•1956','\
Ray Charles•The Great Ray Charles•Metronome•1958','\
Horace Silver•The Preacher•Blue Note•1955','\
The Mastersounds•The Mastersounds Play Compositions By Horace Silver•World Pacific Records•1960','\
The Mastersounds•The Mastersounds Play Compositions By Horace Silver•World Pacific Records•1960','\
The Horace Silver Quintet•Horace Silver Quintet Volume 3•Blue Note•1954','\
Harry James And His Orchestra•Doodlin\' / I\'ll Take Care Of Your Cares•MGM Records•1960','\
Dizzy Gillespie•World Statesman•Karusell•1957','\
Dizzy Gillespie•At Newport•Verve Records•1957','\
Peggy Lee•Got That Magic•Capitol Records•1963'),'\
\
Doors\
':('\
Eric Kloss•Doors•Cobblestone•1972','\
Ballrogg•Cabin Music•Hubro•2012','\
Spike Jones And His City Slickers•Behind Those Swinging Doors / Red Wing•Bluebird (3)•1941','\
Truly Smith•Windows And Doors / Take A Broken Heart•Decca•1967','\
Mike Nock•Ondas•ECM Records•1982','\
Spike Jones And His City Slickers•Behind Those Swinging Doors / The Sheik Of Araby•RCA Victor•1947','\
Tied & Tickled Trio•La Place Demon•Morr Music•2011','\
Spike Jones And His City Slickers•Behind Those Swinging Doors / The Sheik Of Araby•RCA Victor•1947','\
Yasuaki Shimizu•One Hundred•Staubgold•2009','\
Captain Supernova•Doors Of Perception•Cold Busted•2016','\
Guillaume Perret & The Electric Epic•Open Me•Kakoum Records•2014','\
Steve Tibbetts•Northern Song•ECM Records•1982','\
no artist•Face To Face•Intuition Records•1995','\
Brother Jack McDuff•To Seek A New Home•Blue Note•1970'),'\
\
Down for Double\
':('\
Count Basie•Basie\'s Back In Town•Philips•0','\
Count Basie Orchestra•Basie\'s Back In Town•Epic•1955','\
Lambert Hendricks & Ross•Sing A Song Of Basie•ABC-Paramount•1958','\
Buddy Rich And His Orchestra•This One\'s For Basie•Norgran Records•1956','\
Mario Pavone•Sharpeville•Alacra Records•1988','\
Count Basie Orchestra•The Best Of Basie•Saga Eros•1970','\
Shorty Rogers•Shorty Rogers Courts The Count•RCA Victor•1954','\
Newport Youth Band•The Newport Youth Band At The Newport Jazz Festival•Coral•1959','\
Count Basie•Down For Double•Showcase•1985','\
Count Basie Orchestra•The Count Basie Story Vol. 1•Mode Disques•0'),'\
\
Doxy\
':('\
Sonny Rollins•Our Man In Jazz•RCA Victor•1963','\
Miles Davis•Miles Davis And The Modern Jazz Giants•Metronome•1958','\
Tubby Hayes•Jazz Of Modern Times 4. Folge•Fontana•1962','\
Miles Davis•Miles Davis With Sonny Rollins•Prestige•1954','\
Dexter Gordon•The Monmartre Collection Vol. 1•Polydor•1971','\
Dexter Gordon•Both Sides Of Midnight•Black Lion Records•1988','\
Ray Draper•A Tuba Jazz•Jubilee•1959','\
John Coates Jr•Tokyo Concert•Omnisound (2)•1980','\
Phil Woods•Phil Woods & The Japanese Rhythm Machine•RCA•1976','\
Tubby Hayes•Tubbs In N.Y.•Fontana•1962','\
Oliver Nelson•Taking Care Of Business•New Jazz•1960'),'\
\
Dreamin\'\
':('\
no artist•California Dreamin\'•Columbia•1969','\
The Brass Ring•California Dreamin\'•Dunhill•0','\
José Feliciano•Light My Fire / California Dreamin\'•RCA Victor•1968','\
José Feliciano•Light My Fire / California Dreamin\'•RCA Victor•1968','\
Willie Bobo•Kojak-Theme / Dreamin\'•Blue Note•1977','\
Malta (3)•Summer Dreamin\'•JVC•1985','\
The Brass Ring•Guantanamera•RCA Victor•1966','\
The Heath Brothers•Dreamin\'•Columbia•1981','\
Björn Ingelstam•Fiol Sessions•Fiol Optik•2014','\
Prism (9)•Dreamin\'•SMS Records•1986','\
George Benson•Collaboration•Warner Bros. Records•1987','\
Chick Bullock & His Levee Loungers•Blossoms On Broadway / You Can\'t Stop Me From Dreamin\'•Perfect (3)•1937','\
José Feliciano•Light My Fire•RCA Victor•1968','\
Paul Hardcastle•Transcontinental•Rytone Entertainment•2011'),'\
\
Dreamsville\
':('\
Pat Suzuki•The Duke Of Kent / Dreamsville•RCA Victor•1959','\
Sami Linna Quartet•Sami Linna Quartet•Timmion Records•2019','\
Ray Anthony•Music From Peter Gunn•Capitol Records•1959','\
Henry Mancini And His Orchestra•Love Theme From "Phaedra"•RCA•1962','\
Skinnay Ennis And His Orchestra•Dreamsville Ohio / Around And Around She Goes•Victor•1941','\
Ray Anthony•Music From Peter Gunn•Capitol Records•1959','\
The Wes Montgomery Trio•Guitar On The Go•Riverside Records•1966','\
The Phil Woods Quintet•Bop Stew•Concord Jazz•1988','\
Hal Galper•Dreamsville•Enja Records•1987','\
Shelly Manne & His Men•Play Peter Gunn•Contemporary Records•1959','\
Alvin Tyler•Graciously•Rounder Records•1987','\
Mari Nakamoto•Little Girl Blue•Three Blind Mice•1974','\
Benny Bailey•Midnight In Europe•MCE•1964'),'\
\
Drive\
':('\
Shukou Mizuno•Shuko Mizuno\'s "Jazz Orchestra \'73"•Three Blind Mice•1973','\
Artie Shaw And His Orchestra•Bedford Drive / Tabu•Victor•1945','\
Particle Dreams•Drive Carefully•Gorgeous Lights•2017','\
Jean-Luc Ponty•Beach Girl / Sunset Drive•Atlantic•1979','\
Bobbi Humphrey•Harlem River Drive•Blue Note•1973','\
Al Lombardy His Clarinet And Orchestra•New Summit Ridge Drive / Choppin\'•Dot Records•1953','\
Johnny Beecher•Reveries / Summit Ridge Drive•CRC Charter•1962','\
The Necks•Drive By•Fish Of Milk•2003','\
Artie Shaw And His Gramercy Five•Special Delivery Stomp / Summit Ridge Drive•no label•1941','\
Artie Shaw And His Gramercy Five•Summit Ridge Drive / Cross Your Heart•Victor•1940','\
Hugo Montenegro And His Orchestra•Dark Eyes•Time Records (3)•1962','\
Gerry Mulligan•Jazz Makers•Philips•0','\
Marden Hill•Sixty Minute Man•Polystar•1993','\
Clark Terry•Amen (Lilies Of The Field) / East Side Drive•Cameo•1960','\
Paul Jeffrey•Family•Mainstream Records•1972','\
Sergio Fanni Quintet•Hard Suite•Carosello•1975'),'\
\
Duff\
':('\
Eddie Condon And His All-Stars• I\'ve Found A New Baby / Duff Campbell\'s Revenge•Philips•0','\
Brother Jack McDuff•Goodnight It\'s Time To Go•Prestige•1961','\
Brother Jack McDuff•Steppin\' Out•Prestige•1969','\
Brother Jack McDuff•Tough \'Duff•Prestige•1960','\
Brother Jack McDuff•Brother Jack McDuff\'s Greatest Hits•Prestige•1966','\
Brother Jack McDuff•Brother Jack•Prestige•1960','\
Brother Jack McDuff•Rock Candy•Prestige•1972','\
Gene Ludwig Trio•Duff´s Blues•18th & Vine•2008','\
no artist•I\'m Entitled To You!!•Argo (6)•1958','\
The Dutch Swing College Band•The Dutch Swing College Band Meets Joe Venuti•DSC Production•0','\
Giovanni Guidi Trio•Tomorrow Never Knows •Venus Records (5)•2006','\
The Dutch Swing College Band•100 Years Of Jazz•STS Analog•2017'),'\
\
Duke\
':('\
Ran Blake•Duke Dreams "The Legacy Of Strayhorn-Ellington"•Soul Note•1981','\
Franz Koglmann•We Thought About Duke•hat ART•1995','\
Duke Ellington•Ellington At Newport 1956 (Complete)•Legacy•1999','\
Jacques Coursil Unit•Way Head•BYG Records•1969','\
Pat Suzuki•The Duke Of Kent / Dreamsville•RCA Victor•1959','\
Duke Ellington And His Orchestra•Snake Hip Dance / Lazy Duke•Parlophone•1933','\
Sidewalk Hot Jazz Orchestra•Pishi Pishi/ Serenade For Duke•JG-Records•1971','\
Duke Ellington And His Orchestra•The Duke Steps Out / Haunted Nights•no label•0','\
Duke Jordan•Blue Duke•RCA•1983','\
Duke Ellington And His Orchestra•Lazy Duke / What Can A Poor Fellow Do?•Parlophone•0','\
Buck Clayton•Buck Clayton Jam Session Vol. 2•Chiaroscuro Records•1975','\
Miles Davis•The Sound Of Miles Davis•Vap•1990'),'\
\
E.K.\'s Blues\
':('\
Benny Goodman•"The Complete Small Combinations" Volumes 3/4 (1937/1939)•RCA•1986','\
Various•Ragtime Fun•no label•1968'),'\
\
E.S.P.\
':('\
Fredrick Lonberg-Holm•Resistance•Bocian Records•2015','\
FLOOR BABA•Gamewave•DESKPOP•2015','\
no artist•C-o-n-s-t-a-n-t-i-n-o-p-l-e / Who Wouldn\'t Be Blue?•Victor•1928','\
Paul Whiteman And His Orchestra•C-o-n-s-t-a-n-t-i-n-o-p-l-e / Get Out And Get Under The Moon•Columbia•1928','\
University Six•C-O-N-S-T-A-N-T-I-N-O-P-L-E / Just A Night For Meditation•Harmony (4)•1928','\
Tomasz Stańko•Balladyna•GOWI Records•1994','\
Various•The Savoy Story•Musica Jazz•1992','\
Ethel Merman•Memories•Festival Records•1955','\
Various•1928•RCA Victor•1966','\
Helen Shapiro•Simply Shapiro•Katalyst Records•2000','\
Various•Ritam Rock Plemena Od Uragana Do Urbana•Vedis•2005','\
Various•Organ Magic!•no label•1977'),'\
\
Early Autumn\
':('\
Jo Stafford•Jambalaya / Early Autumn•Columbia•1952','\
Woody Herman And His Orchestra•Lemon Drop / Early Autumn•Capitol Records•1951','\
Woody Herman And His Third Herd•Early Autumn / Celestial Blues•Quality•1952','\
Nicki Parrott•Autumn Leaves•Venus Records (5)•2012','\
Ted Heath And His Orchestra•Botch-A-Me / Early Autumn•Decca•0','\
Billy Eckstine•Early Autumn•MGM Records•1952','\
Woody Herman And His Orchestra•Early Autumn / Keeper Of The Flame•Capitol Records•1949','\
Claude Thornhill And His Orchestra•Early Autumn / Oh You Beautiful Doll•Columbia•1947','\
Woody Herman•Lionel Hampton Presents:  Woody Herman•no label•1977','\
Woody Herman•Sound Of Jazz•Cleo•0','\
Nicki Parrott•Autumn Leaves•Venus Records (5)•2012','\
Woody Herman•Jazz Classics•Aurophon•1993','\
John Klemmer•Simpatico•JVC•1997','\
The Bill Evans Trio•Quiet Now•Affinity•1986'),'\
\
Easy\
':('\
Sarah Vaughan•Imagination•Mercury•1955','\
Rovi•Due Temi Con Variazioni (Two Themes With Variations)•Sound Work Shop•1978','\
Ann Cole•Easy Easy Baby / New Love•Baton Records•1956','\
The Invisible (2)•Easy Now•Ninja Tune•2015','\
Tony Bennett•Twilight World / Easy Come Easy Go•Columbia•1972','\
Harry James And His Orchestra•Friar Rock / Easy•Columbia•1946','\
Wardell Gray Quartet•Twisted / Easy Living•Gazell•1952','\
Billie Holiday•Easy Living / Deep Song•Decca•1947','\
Harry James And His Orchestra•Easy / Who\'s Sorry Now?•Parlophone•1946','\
Pascal Maupeu•Easy​/​Uneasy Music - Cd 1 & 2•Not On Label (Pascal Maupeu Self-released)•2015','\
Mat Mathews•Off Shore / Easy Melody•Coral•0','\
The Jazztet•Easy Living / Serenata•Argo (6)•0','\
Guy Lombardo And His Royal Canadians•Speak Low / Take It Easy•Decca•1943','\
Hank Crawford•Easy Living / Playmates•Atlantic•1961','\
The Ramsey Lewis Trio•Hang On Sloopy / Movin\' Easy•Cadet•1965','\
Sidney Bechet•Les Oignons / Ridin\' Easy Blues•Vogue Productions•1949','\
Johnny Hodges And His Orchestra•Easy Going Bounce / Indiana•Norgran Records•0','\
Marty Paich•Marty Paich•Cadence (2)•1958','\
Ronnie Laws•Heavy On Easy•Liberty•1981','\
The Ragamuffins (4)•Easy Winners•Pye Records•1974','\
Gary Crosby (2)•Easy Street / Lazybones•Decca•1956'),'\
\
Easy Living\
':('\
The Jazztet•Easy Living / Serenata•Argo (6)•0','\
Hank Crawford•Easy Living / Playmates•Atlantic•1961','\
Billie Holiday•Easy Living / Deep Song•Decca•1947','\
Wardell Gray Quartet•Twisted / Easy Living•Gazell•1952','\
Miles Davis•Blue Moods•Debut Records (3)•1959','\
Charlie Barnet And His Orchestra•Easy Living / O\'Henry•Capitol Records•1949','\
Dexter Gordon Quartet•Bouncin\' With Dex•SteepleChase•1976','\
Frank Butler•The Stepper•Xanadu Records•1978','\
Miles Davis•Blue Moods•Debut Records•1955','\
The Junior Cook Quintet•Junior\'s Cookin\'•Jazzland•1961','\
Lou Bennett (2)•Pentacostal Feeling•Philips•1966'),'\
\
Easy To Love\
':('\
The King Sisters•Easy To Love•Capitol Records•1957','\
Cannonball Adderley Sextet•Nippon Soul•Riverside Records•1967','\
Erroll Garner Trio•Lullaby Of Birdland / Easy To Love•Philips•0','\
David Rose & His Orchestra•Night And Day / Easy To Love•RCA Victor•1946','\
Milt Buckner•Rockin\' With Milt Part 3•Capitol Records•1955','\
Buck Hill Quartet•Easy To Love•SteepleChase•1982','\
Chet Baker Quartet•Chet Baker Quartet•Vogue•1954','\
no artist•So Easy To Love (Hard To Forget)•Columbia•1976','\
Billie Holiday And Her Orchestra•You Turned The Tables On Me / Easy To Love•Mercury•0','\
Claude Thornhill And His Orchestra•Just Plain Love / You\'re Not So Easy To Forget•Columbia•1947','\
Charlie Parker With Strings•A Charlie Parker Memorial•Ariston Records•1971','\
New York Trio•Begin The Beguine•Venus Records (5)•2006','\
Charlie Parker With Strings•Charlie Parker With Strings•Clef Records•0','\
Paul Chambers (3)•Chambers\' Music: A Jazz Delegation From The East•Jazz: West•1956','\
Charlie Parker•Bird With Strings (Live At The Apollo Carnegie Hall & Birdland)•Columbia•1977','\
The George Shearing Quintet•Love (Your Spell Is Everywhere) / It\'s Easy To Remember•MGM Records•0'),'\
\
Ecaroh\
':('\
The Mastersounds•The Mastersounds Play Compositions By Horace Silver•World Pacific Records•1960','\
The Horace Silver Trio•New Faces - New Sounds•Blue Note•1952','\
Art Blakey & The Jazz Messengers•The End Of A Love Affair / Ecaroh•Philips•1956','\
The Mastersounds•The Mastersounds Play Compositions By Horace Silver•World Pacific Records•1960','\
Jamey Aebersold•For You To Play... Horace Silver Eight Jazz Classics•JA Records•1978','\
Siegfried Kessler Trio•Invitation•Impro•1979','\
The Horace Silver Trio•Horace Silver Trio•Vogue•0','\
The Wes Montgomery Trio•The Wes Montgomery Trio•Riverside Records•1959','\
Turtle Island String Quartet•Metropolis•Windham Hill Jazz•1989','\
Art Blakey•The Jazz Messenger•Columbia•1991'),'\
\
Ecclusiastics\
':('\
10³²K•That Which Is Planted (Live In Buffalo And Rochester)•no label•2013','\
The Roland Kirk Quartet•Meets The Benny Golson Orchestra•Mercury•1963','\
Mingus Dynasty•Reincarnation•Soul Note•1982','\
Tonight At Noon (2)•To Mingus With Love•Prophone•2011','\
Jimmy Knepper Sextet•Tell Me...•Daybreak•1979','\
Mingus Big Band•Live In Tokyo•Sunnyside•2006','\
Roland Kirk•Hip!•Fontana•1965','\
Charles Mingus•Charles Mingus and Friends In Concert•Columbia•1973','\
Mingus Big Band•Mingus Big Band 93 - Nostalgia In Times Square•Dreyfus Jazz•1993','\
The Roland Kirk Quartet•The Roland Kirk Quartet Meets The Benny Golson Orchestra•Mercury•0','\
Position Alpha•The Great Sound Of Sound•Dragon (8)•1985'),'\
\
Eclypso\
':('\
Tommy Flanagan Trio•Tommy Flanagan Trio•Metronome•1957','\
Eraldo Volonté•Eraldo Volonté Presenta Jazz (Now) In Italy•Equipe (2)•1966','\
Tommy Flanagan Trio•Eclypso•Enja Records•1977','\
Tommy Flanagan•The Cats•New Jazz•1959','\
Tommy Flanagan Trio•Flanagan\'s Shenanigan\'s•Storyville•1994','\
Tommy Flanagan•Overseas•Prestige•1958','\
Various•Aurex Jazz Festival (1982): All Star Jam•Eastworld•1982','\
Art Farmer Quartet•Warm Valley•Concord Jazz•1983','\
John Coltrane•Modern Jazz Giants 2•Prestige•1998','\
Kenny Burrell•Kenny Burrell / John Coltrane•Prestige•1976'),'\
\
Eiderdown\
':('\
Pete La Roca•Basra•Blue Note•1965','\
Stan Getz Quartet•Live At Montmartre Vol. 2•Steeplechase•1986','\
The Bill Evans Trio•Crosscurrents•Fantasy•1978','\
no artist•Cosmic Chicken•Prestige•1975','\
Gary Burton•Right Time - Right Place•Sonet•1990','\
Stan Getz Quartet•Live At Montmartre•SteepleChase•1977'),'\
\
Eighty One\
':('\
Miles Davis•E.S.P.•Columbia•1965','\
Jean-Luc Ponty•Live At Donte\'s•Blue Note•1981','\
Herbie Hancock•A Tribute To Miles•Qwest Records•1994','\
The V.S.O.P. Quintet•Tempest In The Colosseum•CBS/Sony•1977','\
Jerry Gonzalez And The Fort Apache Band•Obatalà•Enja Records•1989','\
Sami Swoi•The Locust•Polskie Nagrania Muza•1982'),'\
\
Einbahnstrasse\
':('\
Ron Carter•Uptown Conversation•Embryo Records•1970','\
Kevin Hays•Andalucia•Blue Note•1997','\
Chick Corea•Chick Corea Herbie Hancock Keith Jarrett McCoy Tyner•Atlantic•1976','\
Ethan Iverson•The Purity Of The Turf•Criss Cross Jazz•2016','\
Houston Person•Now\'s The Time •Muse Records•1993','\
Various•Atlantic Jazz Piano•Atlantic•1986','\
Various•Atlantic Jazz•Atlantic•1986'),'\
\
El Gaucho\
':('\
Victor Silvester And His Silver Strings•Estoril•Columbia•1956','\
Wayne Shorter•Adam\'s Apple•Blue Note•1966','\
Kirk Lightsey•Shorter By Two - The Music Of Wayne Shorter Played On Two Pianos•Sunnyside•1989','\
Laurent De Wilde•Colors Of Manhattan•Gazebo•1990','\
Marc Ribot Y Los Cubanos Postizos•¡Muy Divertido! (Very Entertaining!)•Atlantic•2000','\
Rachel Z Trio•On The Milky Way Express•Tone Center•2000','\
Pedro Aznar•Caja De Música•Tabriz Music•2000','\
Roberto Delgado•Buenos Dias Ole\'•Polydor•0','\
Roberto Delgado•Music Box Dancer •Polydor•1979'),'\
\
Elizete\
':('\
Bud Shank•Brasamba!•Pacific Jazz•1963','\
Cal Tjader•Plays The Contemporary Music Of Mexico And Brazil•Verve Records•1962','\
Bud Shank•Brazil! Brazil! Brazil!•World Pacific Records•1966'),'\
\
Elm\
':('\
David Liebman / Richard Beirach•The Duo Live•Advance Music•1991','\
Richard Beirach•Elm•ECM Records•1979','\
Clever Girl•No Drum And Bass In The Jazz Room•Barely Regal Records•2010','\
Quest (13)•Quest•Trio Records•1982','\
Richard Beirach•Live In Tokyo “Solo Concert”•Trio Records•1982','\
Norbert Gottschalk•Stars•Mons Records•2013','\
Harold Johnson Sextet•House On Elm Street•H.M.E.•1967','\
no artist•Les Cargos•Label Bleu•1991'),'\
\
Elora\
':('\
J.J. Johnson•Afternoon In Paris•Sonet•0','\
Sonny Stitt•Sonny Stitt / Bud Powell / J.J. Johnson•Prestige•1956','\
Various•First Sessions 1949/50•Prestige•1978','\
Sonny Stitt•Genesis•Prestige•1975','\
Sonny Stitt•Stitt\'s Bits: The Bebop Recordings 1949-1952•Prestige•2006'),'\
\
Embraceable You\
':('\
Jimmy Dorsey And His Orchestra•Embraceable You / Fingerbustin\'•Decca•1941','\
Duke Jordan•Jazz Laboratory Series Vol. 1•Signal (3)•1955','\
James Moody And His Band•Two Fathers / Embraceable You•Prestige•1951','\
The Charlie Parker Quintet•Bongo Bop / Embraceable You•Dial Records (3)•1948','\
Clifford Brown•Embraceable You / Daahoud•Limelight•1964','\
Jazz At The Philharmonic•Norman Granz\' Jazz At The Philharmonic Vol. 13•Mercury•1951','\
Roy Eldridge And His Orchestra•Little Jazz Boogie / Embraceable You•Decca•1946','\
Billie Holiday•As Time Goes By / Embraceable You•Commodore•1948','\
Earl Bostic And His Orchestra•Flamingo / Embraceable You•Gusto Records (2)•1979','\
The Nat King Cole Trio•Sweet Lorraine / Embraceable You•Capitol Records•0','\
Earl Bostic And His Orchestra•Night And Day / Embraceable You•King Records (3)•1955','\
Jimmy Smith•Open House•Blue Note•1968'),'\
\
Emily\
':('\
Ted Nash Quintet•Live At Dizzy\'s Club Coca-Cola•Plastic Sax Records•2018','\
Gene Harris•Listen Here / Emily•Blue Note•1972','\
Urbie Green•Oleo•Pausa Records•1978','\
Frank Sinatra•Somewhere In Your Heart / Emily•Reprise Records•1964','\
Ray Brown•Two Bass Hits•European Music Productions•1988','\
Monty Alexander•Unlimited Love - Live & In Concert•BASF•1976','\
Yoshio Otomo Quartet•Moon Ray•Three Blind Mice•1977','\
Oscar Peterson•Travelin\' On•MPS Records•1969','\
Henry Thies And His Orchestra•Having You Around Is Heaven / Here Comes Emily Brown•Victor•1930','\
Tsuyoshi Yamamoto•Live At Misty \'77•Flying Disk•1977','\
Stan Getz•Live In Belgium 1974•Novadisc•0','\
Zoot Sims•Plays Johnny Mandel Quietly There•Pablo Records•1984','\
Ares Tavolazzi Trio•Kars•ARTIS Records•1989','\
Sonny Greenwich•Evol-ution Love\'s Reverse•PM•1979'),'\
\
Empathy\
':('\
Duke Pearson•Sweet Honey Bee•Blue Note•1967','\
The Steve Wright Big Band•Take Two•Steve Wright Music Endeavors•1981','\
Earl Bostic•A New Sound•King Records (3)•1964','\
Illinois Jacquet And His Orchestra•Illinois Jacquet And His Orchestra•Clef Records•1957','\
Theo Travis•View From The Edge•33 Records•1994','\
Hi-Tek (2)•Hi-Tek•Original Records•1981','\
Malcolm Braff Trio•Inside•Enja Records•2011','\
Jimmy Woode•The Colorful Strings Of Jimmy Woode•Argo (6)•1958','\
Special Providence•Essence Of Change•Giant Electric Pea•2015','\
Various•Spiritual Jazz Vol.9 - Blue Notes Parts I & II•Jazzman•2019','\
The Herbie Mann-Sam Most Quintet•The Herbie Mann-Sam Most Quintet•Bethlehem Records•1956'),'\
\
Enchance\
':('\
Joanne Brackeen•Special Identity•Antilles•1982','\
Chico Freeman•Essence Of Silence•Jive Music•2010'),'\
\
Endangered Species\
':('\
Various•The New Breed - Vocal Grooves•Blue Note•2002','\
Pat Metheny•Song X•Geffen Records•1986','\
Wayne Shorter•This Is Jazz Vol. 19•Columbia•1996','\
Dianne Reeves•New Morning•Blue Note•1997','\
Dianne Reeves•New Morning•Blue Note•1997','\
Wayne Shorter•Atlantis•Columbia•1985','\
Yatha Bhuta Jazz Combo•Yatha Bhuta Jazz Combo•All City Records (3)•2013','\
Dianne Reeves•The Best Of Dianne Reeves•Blue Note•2002','\
Esperanza Spalding•Radio Music Society•Heads Up International•2012'),'\
\
Epilogue\
':('\
Pat Martino•Starbright•Warner Bros. Records•1976','\
The Bill Evans Trio•Everybody Digs Bill Evans•Riverside Records•1959','\
Bobby Wellins•Culloden Moor Suite•Spartacus Records•2014','\
Károly Binder•Kontinentspiel•Krém•1989'),'\
\
Epistrophy\
':('\
The Thelonious Monk Quartet•Monk In Tokyo•CBS/Sony•1969','\
Thelonious Monk•Live At Rotterdam 1967•Fondamenta•2017','\
Thelonious Monk•At Newport 1963 & 1965•Columbia•2002','\
Steve Lacy•Epistrophy•BYG Records•1969','\
The Thelonious Monk Quartet•At Carnegie Hall•Blue Note•2005','\
Thelonious Monk•Blue Monk•Jazz MasterWorks•1985','\
The Thelonious Monk Quartet•Thelonious In Action•Riverside Records•1958','\
Richard Davis (2)•Epistrophy & Now\'s The Time•Muse Records•1972','\
Thelonious Monk Nonet•Live In Paris 1967•no label•1988','\
Thelonious Monk•San Francisco Holiday•Milestone (4)•1992','\
Kenny Clarke And His 52nd Street Boys•Epistrophy / Royal Roost (Rue Chaptal)•no label•1950'),'\
\
Equinox\
':('\
Project Karnak•Equinox•None More Records•2017','\
Harvie Swartz•Smart Moves•Gramavision•1986','\
Hubert Laws•Wild Flower•Atlantic•1972','\
Khan Jamal Trio•The Traveller•Steeplechase•1986','\
John Coltrane•The Best Of John Coltrane•Atlantic•1970'),'\
\
Equipoise\
':('\
Dwight Trible•Equipoise•Ninja Tune•2005','\
Roy Haynes Hip Ensemble•Equipoise / I\'m So High•Mainstream Records•0','\
Max Roach•Members Don\'t Git Weary•Atlantic•1968','\
Larry Coryell•Equipoise•Muse Records•1986','\
Stanley Cowell•Equipoise•Galaxy•1979','\
Stanley Cowell Trio•Close To You Alone•DIW•1990','\
Sonny Fortune•Great Friends•Black And Blue•1987','\
Roy Haynes•Roy-Alty•Dreyfus Jazz•2011','\
Roy Haynes•The Island•Explore Records•2007','\
Monnette Sudler•Where Have All The Legends Gone?•Heavenly Sweetness•2009','\
Jack DeJohnette•The DeJohnette Complex•Milestone (4)•1969','\
Stanley Cowell•Musa - Ancestral Streams•Strata-East•1974','\
Roy Haynes•Hip Ensemble•Mainstream Records•1971','\
Jerry Gonzalez•Avísale A Mi Contrario Que Aquí Estoy Yo •Warner Music Spain S.L.•2010','\
Floating Points•LateNightTales•LateNightTales•2019'),'\
\
Escher Sketch\
':('\
Michael Brecker•Now You See It... (Now You Don\'t)•GRP•1990'),'\
\
Eternal Child\
':('\
The Chick Corea Elektric Band•Eye Of The Beholder•GRP•1988','\
Avishai Cohen•Lyla•Sunnyside•2003','\
The Chick Corea Elektric Band•Live At Montreux 2004•Eagle Vision•2005','\
Chick Corea Akoustic Band•Live•Stretch Records•2018','\
Bugge Wesseltoft•It\'s Snowing On My Piano•ACT (4)•1997','\
New Swing Quartet•New Swing Quartet (Snimka Koncerta Održanog 23. 3. 1980. U Dvorani Vatroslav Lisinski Zagreb)•Jugoton•1980','\
Various•Que Rei Sou Eu? (Trilha Internacional Da Novela)•Som Livre•1989','\
Various•The Magical Sound Of The Panpipes (Volume 2)•Hallmark Records•1996','\
Various•Jazz In The City•Sony BMG Music Entertainment•2006','\
Chick Corea•Music Forever & Beyond: The Selected Works Of Chick Corea 1964-1996•GRP•1996','\
The Golden Gate Quartet•Golden Gate Quartet•Pathé Marconi EMI•1975','\
Various•Sony Music 100 Years: Soundtrack For A Century•Sony Music•1999'),'\
\
Evening In Concert\
':('\
Joanne Brackeen•Special Identity•Antilles•1982','\
Hiroshi Yasukawa•Six To Six•Atom (4)•1979','\
Vladimir Chekasin•Taxi Blues (Original Soundtrack)•DRG Records•1990','\
Various•Moonlight Moods•no label•1973','\
Various•All-Star Festival Of Easy-Listening Mood Music•no label•0'),'\
\
Everything Happens to Me\
':('\
Gerry Mulligan And His Sextet•Mainstream Of Jazz Vol. 3•EmArcy•1984','\
Charlie Parker With Strings•Just Friends / Everything Happens To Me•Karusell•1953','\
Gerry Mulligan And His Sextet•Presenting The Gerry Mulligan Sextet - Vol. 4•EmArcy•1957','\
The Tony Scott Quartet•Both Sides Of Tony Scott•RCA•0','\
Woody Herman And His Orchestra•Everything Happens To Me•Decca•1941','\
Art Blakey & The Jazz Messengers•Everything Happens To Me / Hank\'s Other Tune•Sonet•0','\
Stan Getz•Cool Stan In Cool Sweden Vol. 3•Karusell•1956','\
Tommy Dorsey And His Orchestra•Everything Happens To Me / Whatcha Know Joe?•Victor•1941','\
Art Pepper•Roadgame•Galaxy•1982','\
Dewey Redman•Choices•ENJA Records•1992','\
Benny Bailey•Mirrors•Freedom•1975','\
Erroll Garner•On The Sunny Side Of The Street•Savoy Records•0','\
Art Pepper•Rediscoveries•Savoy Jazz•1986','\
Art Pepper•Neon Art: Volume Three•Omnivore Recordings•2012','\
Donald Byrd•Byrd\'s Eye View•Transition•1955','\
Phil Woods•Chasin\' The Bird•Venus Records (5)•1998','\
Jerry Bergonzi•Lineage•Red Record•1991'),'\
\
Everything I Have Is Yours\
':('\
Herbie Fields And His Orchestra•Dardanella / Everything I Have Is Yours•Coral•1952','\
Billy Eckstine•I\'ll Be Faithful / Everything I Have Is Yours•MGM Records•1948','\
Joe Venuti And His Orchestra•Everything I Have Is Yours / My Dancing Lady•Perfect (3)•1934','\
Jerry Freeman And His Orchestra•I\'m Dancing On A Rainbow / Everything I Have Is Yours•Bluebird (3)•1933','\
Billy Eckstine•Four Great Standards•MGM Records•1954','\
John Jenkins (2)•John Jenkins With Kenny Burrell•Blue Note•1957','\
Billy Eckstine•Everything I Have Is Yours / (You Made Me Love You) Darling Why Did You?•Mercury•1963','\
Francy Boland And Orchestra•3. White Heat•MPS Records•1978','\
Noriko Miyamoto•Push•Yupiteru Records•1978','\
Shirley Bassey•Let\'s Face The Music (No. 2)•Columbia•1965','\
Ralph Marterie•Dancing On The Downbeat•Mercury•1953','\
Paul Weston And His Orchestra•Music For Romancing•Capitol Records•0','\
Billie Holiday•Billie Holiday•Clef Records•1954'),'\
\
Everything Must Change\
':('\
George Benson•Everything Must Change / The Wind And I•Warner Bros. Records•1977','\
The Atlantic Family•Everything Must Change•Atlantic•1978David "Fathead" Newman•Resurgence!•Muse Records•1981','\
Quincy Jones•Body Heat•A&M Records•1974','\
Johnny Lytle•Everything Must Change•Muse Records•1978','\
Archie Shepp Quartet•True Ballads•Venus Records (5)•1997','\
Richard "Groove" Holmes•Broadway•Muse Records•1982','\
The Atlantic Family•Live At Montreux•Atlantic•1978','\
Jan Akkerman•Can\'t Stand Noise•CBS•1983'),'\
\
Exactly Like You\
':('\
Erroll Garner Trio•Misty / Exactly Like You•Mercury•1954','\
The Benny Goodman Quartet•Dinah / Exactly Like You•no label•0','\
Mark Murphy•Fascinating Rhythm / Exactly Like You•Decca•1956','\
Oscar Peterson•Robbins Nest / Exactly Like You•Mercury•1950','\
Louis Armstrong And His Orchestra•Ain\'t Misbehavin\' / Exactly Like You•Vocalion (2)•1930','\
Teddy Wilson And His Orchestra•Booly-Ja-Ja / Exactly Like You•Columbia•1939','\
The Dukes Of Dixieland•Exactly Like You•Decca•0','\
Quintette Du Hot Club De France•Exactly Like You / In A Sentimental Mood•no label•0','\
Zoot Sims•Zoot Case•Sonet•1991','\
John Coltrane•Cattin\' With Coltrane And Quinichette•Prestige•1959','\
Count Basie Orchestra•Jumpin\' At The Woodside / Exactly Like You  •Coral•1949','\
Socarras And His Orchestra•Exactly Like You / Caravan•RCA Victor•0','\
Nina Simone•Exactly Like You•Colpix Records•1964','\
The Nelson Williams Quartet•Rockin\' Chair•Philips•1962','\
Johnny Guarnieri•Nobody\'s Sweetheart•Royale•0','\
Benny Goodman And His Orchestra•Love Me Or Leave Me / Exactly Like You•Victor•1936'),'\
\
Exercise #3\
':('\
Rich Matteson•The Art Of Improvisation Vol. 2•Music Minus One•1974','\
Rich Matteson•The Art Of Improvisation Vol. 1•Music Minus One•1974','\
Jim Chapin•Modern Jazz Drumming•Music Minus One•1970','\
Lester Young•The Master\'s Touch•Savoy Records•1956','\
Frank Zappa•Meat Light•Zappa Records•2016','\
Frank Zappa•антология творчества часть 5-6•Домашняя Коллекция•2004','\
Various•Jet Set: Airport Lounge•Riffage Records•1999','\
Various•Jet Set: Airport Lounge•Riffage Records•1999'),'\
\
Exercise #6\
':('\
Rich Matteson•The Art Of Improvisation Vol. 1•Music Minus One•1974','\
Rich Matteson•The Art Of Improvisation Vol. 2•Music Minus One•1974','\
Frank Zappa•антология творчества часть 5-6•Домашняя Коллекция•2004'),'\
\
Expression\
':('\
Masahiko Togashi•Guild For Human Music•Denon Jazz•1976','\
John Coltrane•Expression•Impulse!•1967','\
Cecil McBee•Alternate Spaces•India Navigation•1979','\
Sunny Murray Quintet•Aigu-Grave•Marge•1980','\
Andrzej Trzaskowski• Polish Jazz Vol. 2•Polskie Nagrania Muza•1989','\
Robohands•Dusk•Not On Label•2019','\
Lin Biviano Band•L.A. Expression / Love Is Stronger Far Than We•Creative World•1975','\
Black Unity Trio•Al-Fatihah•Salaam Records•1971'),'\
\
Eye Of the Hurricane\
':('\
The V.S.O.P. Quintet•Tempest In The Colosseum•CBS/Sony•1977','\
Herbie Hancock•Maiden Voyage•Blue Note•1965'),'\
\
Ezz-thetic\
':('\
Lee Konitz Sextet•Ezz-Thetic / Hi Beck•Prestige•1951','\
no artist•Live In An American Time Spiral•Soul Note•1983','\
Grant Green•Solid•Blue Note•1979','\
Stephan Kurmann Strings•Strings•TCB Records (2)•1988','\
The George Russell Sextet•Ezz-thetics•Riverside Records•1961','\
Miles Davis•Bluing•Past Perfect Silver Line•2000','\
Max Roach•+4•EmArcy•1957','\
Miles Davis•Conception•Prestige•1956','\
Grant Green•The Best Of Grant Green Vol. 1•Blue Note•0','\
The Lee Konitz Quartet•Ideal Scene•Soul Note•1986'),'\
\
Fables of Faubus\
':('\
The Charles Mingus Quintet•Mingus In Europe Volume I•Enja Records•1979','\
Charles Mingus•Live In Stuttgart 1964 !•Unique Jazz•2000','\
Charles Mingus•Astral Weeks•Moon Records (4)•1990','\
Charles Mingus Sextet•Concertgebouw Amsterdam Volume 2•Ulysse Musique•1986','\
Charles Mingus•Goodbye Pork Pie Hat•Jazz Hour•1989','\
Charles Mingus•Fables Of Faubus•Jazz Collection (7)•1990','\
Charles Mingus Sextet•Live In Copenhagen 1964•Landscape•1991','\
Charles Mingus•So Long Charlie•Ediciones Del Prado•1996','\
Charles Mingus•Meditations On Integration•Bandstand•1992','\
Charles Mingus Sextet•The Complete Bremen Concert•Jazz Lips•2010','\
Tonight At Noon (2)•To Mingus With Love•Prophone•2011','\
Charles Mingus•In Amsterdam 1964•DIW•1989','\
Pepper Adams•Plays The Compositions Of Charlie Mingus•Workshop Jazz•1964'),'\
\
Fall\
':('\
Various•How Ya Doin?•Nondo•1977','\
Lanu•Fall•Tru Thoughts•2011','\
Stefan Schmidt (19)•Klammer Fall•Not On Label (Stefan Schmidt self released)•2014','\
David Poe•Blue Glass Fall•Ulftone Music•2000','\
Masahiko Satoh•Samādhi•Express•1972','\
Pee Wee Hunt•Kitty•Capitol Records•0','\
The Dave Brubeck Quartet•The Brubeck Quartet At Storyville•Fantasy•1953','\
Michael Bublé•When I Fall In Love•Reprise Records•2018','\
Marc Cohen•My Foolish Heart•Jazz City•1988','\
Eddie Heywood•Secret Love•Mercury•1956','\
Mehldau & Rossy Trio•When I Fall In Love•Fresh Sound New Talent•1994','\
Maynard Ferguson & His Orchestra•Let\'s Fall In Love•Roulette•1959','\
Ahmad Jamal Trio•Let\'s Fall In Love / Ahmad\'s Blues•Argo (6)•1959','\
Miles Davis•Nefertiti•Columbia•1968','\
Ben Webster Quartet•Fall Of Love•Impulse!•1964','\
Cortex (17)•Live In New York•Clean Feed•2016','\
Goldfish (18)•9*Nove -La Memoria Delle Quattro Stagioni•-Not On Label•2012','\
Keely Smith•Open Your Heart•Atlantic•1966'),'\
\
Fall With Me\
':('\
Ivory Joe Hunter•Don\'t Fall In Love With Me / Siesta With Sonny•King Records (3)•1948','\
John Martyn•Please Fall In Love With Me•WEA•1981','\
Dinah Shore•Dearly Beloved•Victor•1942','\
Tony Bennett•Cloud 7•Columbia•1955','\
John Klemmer•Touch•ABC Records•1975','\
Johnny Lytle Trio•Happy Ground•Jazzland•1961','\
Rebekka Bakken•The Art Of How To Fall•Universal•2003','\
Carmen Cavallaro•Swingin\' Easy•Decca•1962'),'\
\
Falling Grace\
':('\
Jazz Parasites•Very Early•Phonector•2006','\
Tim Whitehead•Authentic•no label•1991','\
Christoph Neuhaus Trio•Matter Of Three•Unit Records (2)•2014','\
Gary Burton•Paris Encounter•Atlantic•1972','\
Jimmy Earl•Jimmy Earl•Legato•1995','\
Wolfgang Muthspiel•Live At The Jazz Standard•Material Records•2010','\
Allen Farnham Quartet•The Common Thread•Concord Jazz•1995','\
Pascal von Wroblewsky•So Easy•BuschFunk•1993'),'\
\
Falling In Love With Love\
':('\
Helen Merrill•Yesterdays / Falling In Love With Love•Mercury•0','\
The Pete Jolly Trio•Little Bird / Falling In Love With Love•Äva Records•0','\
Clifford Brown•Cliff Brown + Art Farmer With The Swedish All Stars (Vol. 2)•Metronome•1954','\
Jimmy Smith•A Date With Jimmy Smith Vol. 1 •Blue Note•1957','\
Harry Arnolds Orkester•Isn\'t It Romantic•Metronome•1954','\
Whittemore & Lowe•Falling In Love With Love / Brazil•RCA Victor•0','\
Mal Waldron•The Dealers•Status Records (2)•1965','\
Frank Sinatra•Sinatra Sings Rodgers and Hart •Columbia•1954','\
Tommy Dorsey And His Orchestra•Falling In Love With Love / I Wonder Who\'s Kissing Her Now•Decca•1953','\
Kenny Dorham•Kenny Dorham And Friends•JAZZLAND•1962','\
Attila Zoller•デュオローグ Duologue•Express•1971','\
Sammy Davis Jr.•In The Shelter Of Your Arms / Falling In Love With Love•Reprise Records•1963','\
Hank Mobley•Hank Mobley•Blue Note•1957','\
Joshua Breakstone•Remembering Grant Green•Evidence (5)•1996','\
Andy Williams•Andy Williams•CBS•1963','\
Frank Sinatra•Sinatra Swings Volume 1•Reprise Records•1961'),'\
\
Farmer\'s Market\
':('\
Various•Poor Man\'s Heaven•Bluebird (3)•2003'),'\
\
Fascinating Rhythm\
':('\
Mark Murphy•Fascinating Rhythm / Exactly Like You•Decca•1956','\
Joe Bari•Vieni Qui / Fascinating Rhythm•Leslie Records Inc•1949','\
Benny Goodman And His Orchestra•Fascinating Rhythm / It\'s The Talk Of The Town•Columbia•1948','\
Sol Hoopii And His Novelty Five•Fascinating Rhythm / Twelfth Street Rag•Decca•0','\
Carl Stevens•"Skin" And Bones•Mercury•0','\
George Gershwin•Gershwin By Knight•Wilson Audio•1992','\
Xavier Cugat•Swinging Cha-Cha-Chas•Mercury•1964','\
Philip Green And His Rhythm On Reeds•Rhythm On Reeds•Decca•1951','\
Don Ralke Orchestra•But You\'ve Never Heard Gershwin With Bongos•Warner Bros. Records•1962','\
Karel Gott•Karel Gott Sings•Supraphon•1970'),'\
\
Favela\
':('\
Vince Guaraldi Trio•I\'m A Loser / Favela •Fantasy•1966','\
Lee Konitz•Brazilian Serenade•Venus Records (5)•1996','\
Vince Guaraldi•Live At El Matador•Fantasy•1966','\
Kazuo Yashiro Trio•Black Nag•Takt Jazz Series•1997','\
Clare Fischer•Manteca!•Pacific Jazz•1965','\
Made In Brasil•Tudo Joia•Pausa Records•1984','\
Ike Quebec•Bossa Nova Soul Samba•Blue Note•1962','\
Iva Bittová•Entwine / Proplétám•Pavian Records (2)•2014'),'\
\
Fee-Fi-Fo-Fum\
':('\
Art Shaw And His New Music•Fee Fi Fo Fum / Chant•Vocalion (2)•1938','\
Wayne Shorter•Speak No Evil•Blue Note•1966','\
Kirk Lightsey•Lightsey 1•Sunnyside•1983','\
Kirk Lightsey Trio•Everything Happens To Me•Timeless Records (3)•1984'),'\
\
Feel Like Makin\' Love\
':('\
Dick Haymes•Feel Like Makin\' Love / Bein\' Green•GNP Crescendo•1975','\
Eef Albers•Feelings / Feel Like Makin\' Love•CBS•1977','\
no artist•Voodoo DJ Soul Essentials•Virgin•2000','\
Isao Suzuki Sextet•Ako\'s Dream•Three Blind Mice•1976','\
Tsuyoshi Yamamoto•Live At Misty \'77•Flying Disk•1977Lee Ritenour•Lee Ritenour & His Gentle Thoughts •JVC•1977','\
Rainbow (17)•Crystal Green•East Wind•1978','\
Harold Ousley•Sweet Double Hipness•Muse Records•1980','\
Roberta Flack•4 Super Hits•Atlantic•1978','\
Jessy J•Second Chances•Hitman Jazz•2015','\
Noriko Miyamoto•Vivid•Trio Records•1979','\
Keiko Lee•Imagine•Sony•1995','\
Bobby Lyle•The Power Of Touch•Atlantic Jazz•1997','\
Larry Coryell•Sketches Of Coryell•Shanachie•1996','\
Ray Conniff•Laughter In The Rain•Columbia•1975'),'\
\
Feelings and Things\
':('\
Cuong Vu 4-tet•Ballet - The Music Of Michael Gibbs•RareNoise Records•2017','\
Gary Burton / Chick Corea•Crystal Silence•ECM Records•1973','\
Gary Burton Quartet•Lofty Fake Anagram•RCA Victor•1968','\
Michael Gibbs•Michael Gibbs•Deram•1970','\
Various•Classic Jazz-Funk Mastercuts Volume 6 (The Definitive Jap-Jazz Mastercuts)•Mastercuts•1996','\
Various•The Jazz Arranger Volume 2 (1946-1963)•Columbia•1990','\
Various•Mad About You - The Final Frontier (Music From And Inspired By The Television Series)•Atlantic•1997'),'\
\
Feels So Good\
':('\
Lena Horne•Feels So Good•Buddah Records•1971','\
Jasper Davis & His Orchestra•Georgia Gigolo / It Feels So Good•Velvet Tone•0','\
Chuck Mangione•Feels So Good•A&M Records•1977','\
Grover Washington Jr.•Feels So Good•Kudu•1975','\
Lingua Franca (3)•The EP•no label•2008','\
Chuck Mangione•Fun And Games•A&M Records•1980','\
Sketch (9)•Colour Blind•PVK Records•1987','\
Quincy Jones•Stuff Like That / Ai No Corrida / Rise / Feels So Good•Old Gold (2)•1987','\
Steve Reid (5)•Dream Scapes•Eagle Music Group•2001','\
Grover Washington Jr.•At His Best•Motown•1985','\
Erskine Hawkins And His Orchestra•Live At Club Soul Sound•Stang Records•0','\
Grover Washington Jr.•Mister Magic / Feels So Good•Motown•1986'),'\
\
Fields We Know\
':('\
Pete Fountain•Pete Fountain\'s New Orleans•Coral•1959','\
Various•The Best Seventies Album In The World...Ever! Volume One•EMI 100•1997','\
Various•Tribute To The Beatles•Weton-Wesgram•2001','\
Various•Forever Changing - The Golden Age Of Elektra Records - 1963-1973•Rhino Records (2)•2006','\
Various•Background Moods (Music For Your Every Mood )•no label•1965','\
Various•Sony Music 100 Years: Soundtrack For A Century•Sony Music•1999'),'\
\
Filthy McNasty\
':('\
The Horace Silver Quintet•Doin\' The Thing - At The Village Gate•Blue Note•1961','\
Horace Silver•The Best Of Horace Silver•Blue Note•1969','\
David "Fathead" Newman•Fire! Live At The Village Vanguard•Atlantic•1989','\
Various•The Compositions Of Horace Silver•Riverside Records•1962','\
Hideo Shiraki Quintet•Plays Horace Silver•King Records•1962','\
The Bronx Horns•Silver In The Bronx•Timeless Records (3)•1998','\
Horace Silver•Paris Blues•Pablo Records•2002','\
Horace Silver•Horace Silver•Fabbri Editori•1989','\
Carlos Malcolm And His Afro-Jamaican Rhythms•Rucumbine•Son (2)•0','\
Paul Murphy•The Return Of Jazz Club•BGP Records•2014','\
New York Ska-Jazz Ensemble•Get This!•Moon Ska•1998'),'\
\
Fire\
':('\
John Zorn•50⁹ The Classic Guide To Strategy Volume Three•Tzadik•2004','\
Liquid Quintet•Bouquet•Sirulita•2019','\
Harold Martin (2)•Wild Fire•London House Records•0','\
Michael Garrick Band•Home Stretch Blues•Argo (2)•1972','\
Various•A Collection Of Various Interpretations Of Light My Fire•Roof Music•2003','\
Detail (4)•Okhela « To Make A Fire »•Affinity•1984','\
George Fischoff•Feel!•Fastfire Records•1985','\
Shirley Bassey•Light My Fire•Blue Note•1998','\
Jooklo Duo•The Warrior•Northern Spy•2010','\
Gabor Szabo•Fire Dance / Ferris Wheel•Skye Records•1969','\
Mal Waldron•Eric Dolphy & Booker Little Remembered Live At Sweet Basil Vol. II•Paddle Wheel•1987','\
Melody Gardot•Quiet Fire•Universal Music Classics & Jazz•2008','\
Joe Henderson•The Elements•Milestone (4)•1974','\
Rudy Vallee And His Connecticut Yankees•Vieni...Vieni... / Don\'t Play With Fire•Bluebird (3)•0','\
Ted Curson•Fire Down Below / The Very Young •Prestige•1963','\
Lee Morgan•The Genius Of Lee Morgan•Tradition Everest•0','\
The Iceburn Collective•Poetry Of Fire•Revelation Records (8)•1995','\
Les Brown And His Duke University Blue Devils•Swamp Fire / Dance Of The Blue Devils•Decca•1937','\
Ernie Watts•Chariots Of Fire•Qwest Records•1981'),'\
\
First Light\
':('\
Freddie Hubbard•Classics•Fantasy•1984','\
Freddie Hubbard•First Light•CTI Records•1972','\
Tony Perkins (2)•First Romance / Moon-Light Swim•RCA Victor•1957','\
Freddie Hubbard•The Baddest Hubbard (An Anthology Of Previously Released Recordings)•CTI Records•1975','\
John Abercrombie•Animato•ECM Records•1990','\
CTI All-Stars•CTI Summer Jazz At The Hollywood Bowl Live One•CTI Records•1977'),'\
\
First Moves\
':('\
Sonny Rollins•The Cutting Edge•Milestone (4)•1974','\
Exoterm•Exits Into A Corridor•Hubro•2019','\
Eddie Palmieri•Is Doin´It In The Park•G.R. Music•2013','\
Harry Belafonte•In Love With Harry Belafonte•RCA•1982'),'\
\
First Trip\
':('\
Jordan Berger•First•Dreambox Media•2010','\
Herbie Hancock•Speak Like A Child•Blue Note•1968','\
Toby Fichelscher•Busting The Bongos•Sonorama•2013','\
Herbie Hancock Trio•Hurricane!•V.I.E.W. Video•1992','\
Roy Haynes•Sugar Roy•Kitty Records•1976','\
Mario Rusca Trio•Reaction•Dynia World•1974','\
Claude Williamson•La Fiesta•Interplay Records•1979','\
Joe Henderson•Tetragon•Milestone (4)•1968','\
Herbie Hancock•The Finest In Jazz•Blue Note•2007','\
The Ron Carter Nonet•Eight Plus•Seoul Records Inc.•1990'),'\
\
Five Brothers\
':('\
Herbie Harper Quintet•Jazz In Hollywood Series•Nocturne Records•1954','\
Stan Getz Tenor Sax Stars•Five Brothers / Four And One Moore•New Jazz•1949','\
Gerry Mulligan Quartet•Paris Concert•Vogue•1957','\
Gerry Mulligan Quartet•Paris Concert•Pacific Jazz•1955','\
Herb Harper•Herbie Harper Featuring Bud Shank And Bob Gordon•Liberty•1956','\
Gerry Mulligan Quartet•En Concert Avec Europe 1 - Olympia 6 Octobre • 1962•Trema•1994','\
Gerry Mulligan Quartet•Concert De Paris •Disques Vogue•0','\
Claude Thornhill And His Orchestra•Claude Thornhill And His Orchestra Play The Great Jazz Arrangements Of Gerry Mulligan And Ralph Aldrich•Trend (3)•1953','\
Stan Getz•The Brothers•Prestige•1956','\
Sal Salvador•Plays Gerry Mulligan•Stash Records•1985','\
Various•Jazz Montage•Liberty•1963','\
Chet Baker•The  Newport Years Vol. 1•Musica Jazz•1989','\
Herb Harper•Jazz In Hollywood•Original Jazz Classics•1997','\
Stan Getz Quartet•Stan Getz Volume One•New Jazz•1950','\
Lee Konitz•Lee Konitz And The Gerry Mulligan Quartet•Pacific Jazz•1954'),'\
\
Five Hundred Miles High\
':('\
Stan Getz•Captain Marvel•Columbia•1975','\
Joe Pass•Virtuoso #2•Pablo Records•1977'),'\
\
Five Spot After Dark\
':('\
Shirley Scott•Five Spot After Dark•Prestige•1965','\
Shirley Scott•Blue Flames•Prestige•1964','\
Super Trombone•Take Five•Videoarts Music•2001','\
Various•The Definitive Jazz Scene Volume 3•Impulse!•1965','\
no artist•Blues-ette•Savoy Records•1959','\
Art Farmer•Brass Shout•United Artists Records•1959','\
Benny Golson•The Best Of Benny Golson•Concord Jazz•2009','\
Benny Golson Quintet•One More Mem´ry•Baystate•1982','\
Manhattan Jazz Quintet•Caravan•Paddle Wheel•1989'),'\
\
Flags\
':('\
no artist•The Lady From Nine Flags / Royal Saddle•Impulse!•1967','\
Lingomania•Grr...Expanders•Gala Records (4)•1988','\
no artist•Nine Flags•Impulse!•1966','\
Blurt•Poppycock•Toeblock•1986','\
Patrick Moraz•In Tokyo•Winterfold•2009','\
Patrick Moraz•Flags•EG•1985','\
Ryojiro Furusawa Group•Spicy Islands•Union Records (3)•1978','\
Steve Slagle•Rio Highlife•Atlantic•1986','\
The Carla Bley Band•European Tour 1977•WATT Works•1978','\
Two Banks Of Four•Junkyard Gods•Sonar Kollektiv•2008','\
The Carla Bley Big Band•Looking For America•WATT Works•2003','\
Paul Joyner•Quiet Lions•Slow Fidelity•2010','\
Various•Music Too Good For Words: No Speak Sampler•I.R.S. Records•1988'),'\
\
Flamingo\
':('\
Teddi King•Temptation / Flamingo•Coral•1959','\
Herb Alpert & The Tijuana Brass•Mame•A&M Records•1967','\
Erroll Garner•Flamingo / Twilight•Atlantic•1949','\
Earl Bostic And His Orchestra•Flamingo / Moonglow•Parlophone•0','\
Gene Krupa And His Orchestra•Let Me Off Uptown / Flamingo•Okeh•1941','\
no artist•Flamingo / Carioca•Mercury•1952'),'\
\
Flim Flam\
':('\
Laura Nyro•Wedding Bell Blues•Columbia•1972','\
The Bud Shank Quintet•Bud Shank\'s Sunshine Express•Concord Jazz•1976','\
Rex Stewart•Rex Stewart And The Ellingtonians•Riverside Records•1960','\
Various•Pure 4 (Who Got De Funk ?)•Pure Records (6)•1993','\
Julian Coryell•Jazzbo•Venus Records (5)•1995','\
Laura Nyro•Spread Your Wings And Fly: Live At The Fillmore East May 30 1971•no label•2004'),'\
\
Flower Is a Lonesome Thing\
':('\
Archie Shepp - Horace Parlan Duo•Reunion•L+R Records•1987','\
James Leary•James II•Vital Records (11)•1992','\
A Grandinote Trio•A Night Never To Forget•STS Analog•2016','\
Ed Bickert•Bye Bye Baby•Concord Jazz•1984','\
Seldon Powell Sextet•Seldon Powell Sextet Featuring Jimmy Cleveland•Roost•1956','\
Johnny Hodges•Jumpin\' With Johnny Hodges•Vogue•1973','\
Frank Zappa•антология творчества часть 1-2•Домашняя Коллекция•2004','\
Various•Les Triomphes Du Blues•Habana•2001'),'\
\
Fly By Night\
':('\
Session II•Session II•Yamaha•1979','\
Andy Williams•Fly By Night / Danny Boy•Columbia•1961','\
Session II•Session II•Yamaha•1979','\
Jan Harbeck Live Jive Jungle•Elevate•Stunt Records•2017','\
Lee Ritenour•Captain Fingers•Epic•1977','\
Matt Bianco•Say It\'s Not Too Late•WEA•1989','\
Freeez•Anti-Freeez•Beggars Banquet•1984','\
Brian Culbertson•Come On Up•Warner Bros. Records•2003','\
Bert Kaempfert•Wonderland By Night•Polydor•0','\
Wendell Harrison•Fly By Night•Wenha•1990','\
Shakatak•‘Shinin’ On’•Instinct Jazz•1998','\
Roland Kirk•Roland Kirk•Supraphon•1969','\
Roland Kirk•The Inflated Tear•Atlantic•1968'),'\
\
Fly Me to the Moon\
':('\
Bobby Womack•Fly Me To The Moon•Minit•1968','\
Yoko Takahashi•残酷な天使のテーゼ / Fly Me To The Moon•Starchild•1995','\
Unknown Artist•Moon River•Hoctor Records•1964','\
Joe Harnell•Fly Me To The Moon / Our Day Will Come•Kapp Records•0','\
Roy Haynes Quartet•Fly Me To The Moon (In Other Words)•Impulse!•1962','\
Wes Montgomery•Where Have All The Flowers Gone? / Fly Me To The Moon•A&M Records•1968','\
April Stevens•That\'s My Name•Imperial•1962','\
Various•Marbles On The Moon•Marble Arch Records•1969','\
Hampton Hawes•Recorded Live At The Great American Music Hall•Concord Jazz•1983','\
Joe Harnell & His Orchestra•Fly Me To The Moon / Harlem Nocturne•Kapp Records•1962','\
Jim Hall•Jim Hall / Red Mitchell•Artists House•1978','\
The Oscar Peterson Trio•The Oscar Peterson Trio Plays•Verve Records•1964','\
The Rhoda Scott Trio•Fly Me To The Moon / In My Little Corner Of The World•Tru-Sound•1962','\
Frank Sinatra•Hello Dolly!•Reprise Records•0'),'\
\
Flying Home\
':('\
Illinois Jacquet And His All Stars•Flying Home Part I / Flying Home Part II•Philo Recordings•1945','\
Enoch Light And The Light Brigade•Cherokee / Flying Home•Project 3 Total Sound•0','\
Joe Houston & Orchestra•Walking Home / Flying Home•Cash Records (4)•1955','\
Lionel Hampton And His Orchestra•Flying Home / Two Finger Boogie•Brunswick•0','\
Flip Phillips•Caravan / Flying Home•Mercury•1949','\
Lionel Hampton And His Quartet•Flying Home / It\'s A Blue World•Clef Records•1955','\
Lionel Hampton And His Orchestra•Flying Home / In The Bag•Decca•0','\
Ella Fitzgerald•Oh Lady Be Good! / Flying Home•Decca•1947','\
Ella Fitzgerald•Oh Lady Be Good! / Flying Home•Decca•1947','\
Duke Ellington And His Orchestra•Ellington \'55 Part 4•Capitol Records•1955','\
Charlie Ross Quartet•Turnpike Cruise / Flying Home•RKO Unique Records•1957','\
Brother Lee Roy And His Band•Wire Wheels / Indian Giver / Flying Home / Perdido•Philips•0','\
Lionel Hampton And His Quartet•Flying Home!•Verve Records•1989','\
Lionel Hampton And His Quartet•It\'S A Blue World•Blue Star•0'),'\
\
Foggy Day A\
':('\
Alex Kallao Trio•El Cumbanchero / A Foggy Day•Original (3)•1955','\
Sauter-Finegan Orchestra•Coco Bongo / A Foggy Day•RCA Victor•0','\
The Commanders•A Foggy Day / The Bat•Decca•0','\
The Dave Brubeck Quartet•A Foggy Day / Lyons Busy (Theme)•Fantasy•0','\
Lionel Hampton And His Quintet•A Foggy Day•Clef Records•1955','\
Lester Young And His Orchestra•A Foggy Day / Down \'N Adam•Mercury•1951','\
Jackie McLean Quintet•Lights Out!•Prestige•1956','\
Charles Mingus Jazz Workshop•Pithecanthropus Erectus•Atlantic•1956','\
Ella Fitzgerald•Ella Och Louis Vol. 1•Karusell•1957','\
Sonny Rollins•Live In London Volume 2•Harkit Records•2005'),'\
\
Follow Your Heart\
':('\
Bernie Nee•Follow Me•Columbia•1958','\
Weather Report•Follow Your Heart•Fabbri Editori•1994','\
Various•Current Cuts 1971•CTI Records•1971','\
Joe Farrell Quartet•Joe Farrell Quartet•CTI Records•1970','\
Various•Visions Of An Inner Mounting Apocalypse: A Fusion Guitar Tribute•Tone Center•2005','\
Tommy Smith•Peeping Tom•Blue Note•1990','\
3rd Force•Gentle Force•Higher Octave Music•2002','\
The Sons Of Champlin•Follow Your Heart•Capitol Records•1971','\
John McLaughlin•Live In Chicago•Oh Boy•1990','\
John McLaughlin•Live In Chicago•Oh Boy•1990','\
Dick McGarvin•Peaceful•Uncle Bear Records•1974'),'\
\
Foolkiller\
':('\
Mose Allison•Foolkiller •Atlantic•1966','\
Mose Allison•The Word From Mose•Atlantic•1964','\
Brian Auger•Brian Auger•Springboard•1975','\
Ben Sidran•Don\'t Let Go•Blue Thumb Records•1974','\
Julie Driscoll•Julie Driscoll & Brian Auger•Charly Records•1975','\
Mose Allison•The Mose Chronicles - Live In London Volume 2•Blue Note•2001'),'\
\
Fools Rush In\
':('\
Brook Benton•Endlessly / Fools Rush In•Philips•1978','\
Remo Capra•Just Say I Love Her / Fools Rush In•Columbia•1960','\
Mike Curb Congregation•Fools Rush In (Where Angels Fear To Tread) / Do You Wanna Dance ?•Capitol Records•1975','\
Shirley Bassey•Shirley Bassey•Columbia•1961','\
Frank Sinatra•Fools Rush In•Fontana•1959','\
Jack Montrose Sextet•Jack Montrose Sextet•Pacific Jazz•1955','\
Lawrence Welk•Love Is A Many Splendored Thing•Pickwick/33 Records•0','\
The Zoot Sims Quintet•Zoot!•Riverside Records•1956','\
Sonny Stitt•Inter-Action•Cadet•1966','\
Bill Crow Quartet•From Birdland To Broadway•Venus Records (5)•1996','\
Lee Konitz•Jazz A Confronto 32•Horo Records•1976','\
Frank Sinatra•Nice \'N\' Easy (Part 3)•Capitol Records•1960','\
Ray Eberle Orchestra•My Friend Glenn•Allegro Records•1967'),'\
\
Footprints\
':('\
The David Liebman Quintet•Pendulum•Artists House•1979','\
The Miles Davis Quintet•Live In Europe 1967 (The Bootleg Series Vol. 1)•Columbia•2011','\
Chico Freeman•Luminous•Jazz House Records•1989','\
Sacha Distel•Mood Music For Listening And Relaxation•no label•0'),'\
\
For All We Know\
':('\
Dinah Washington•I Wouldn\'t Know / For All We Know•Roulette•1962','\
Bill Doggett•For All We Know / Hometown Shout•King Records (3)•1962','\
Ray Conniff And His Orchestra & Chorus•Just Friends / For All We Know•CBS•1966','\
Dexter Gordon•The Monmartre Collection Vol. 1•Polydor•1971','\
Nina Simone•For All We Know / Good Bait•Bethlehem Records•1960','\
Dexter Gordon•Both Sides Of Midnight•Black Lion Records•1988','\
Stan Getz•Ginza Samba / For All We Know•Fantasy•1958','\
Billie Holiday•I\'m A Fool To Want You•Sony•1991','\
The Jazz Couriers•Tippin\' - The Jazz Couriers Live In Morecambe 1959•Gearbox Records•2012','\
The Andrews Sisters•Chattanooga Choo Choo / For All We Know•Decca•1941','\
Nat King Cole•The Very Thought Of You•Capitol Records•1958','\
Sarah Vaughan•Through The Years •Mercury•1959','\
Isao Suzuki•Cadillac Woman•Flying Disk•1977','\
Bill Coleman (2)•Swingin\' In London•Black Lion Records•1972','\
Sullivan Fortner•Aria•Impulse!•2015','\
Sonny Stitt•Sax Expressions•Royal Roost•1965','\
Bob Rockwell Quartet•On The Natch•SteepleChase•1987','\
Roger Williams (2)•Theme From "Love Story" / For All We Know•MCA Records•1971','\
Bob Mintzer Big Band•For the Moment•MCG Jazz•2012'),'\
\
For Heavens Sake\
':('\
Cal Tjader Quintet•Wachi Wara / For Heaven\'s Sake•Fantasy•1954','\
The Horace Silver Quintet•6 Pieces Of Silver•Blue Note•1956','\
Tom Harrell•Form•Contemporary Records•1990','\
Furusawa Ryojiro Quartet•You Wanna Rain•Frasco•1976','\
Red Rodney•The 3 R\'s•Muse Records•1982','\
Ray McKinley And His Orchestra•You Came A Long Way (From St. Louis)•RCA Victor•1948','\
John Hicks•Inc. 1•DIW•1988','\
Tubby Hayes•Live 1969•Harlequin•1986','\
Ben Webster•Ben Webster Plays Ballads•Storyville•1988','\
Hampton Hawes Trio•The Seance•Contemporary Records•1969','\
Benny Bailey•For Heaven\'s Sake•Hothouse•1989','\
Johnny Lytle Trio•Blue Vibes•Jazzland•1960','\
Archie Shepp/Michel Marre Quintet•You\'re My Thrill•Vent Du Sud•1986','\
Tony Reedus•Incognito•Enja Records•1991','\
Massimo Faraò Double Piano Quartet•The Masquerade is Over•Venus Records (5)•2017'),'\
\
For Minors Only\
':('\
Chet Baker Trio•Daybreak•SteepleChase•1980','\
Chet Baker•Chet Baker René Urtreger Aldo Romano Pierre Michelot•Carlyne•1989','\
Jimmy Heath•Picture Of Heath•Xanadu Records•1975','\
Art Blakey & The Jazz Messengers•Hard Drive•Bethlehem Records•1957','\
Chet Baker•Playboys•World Pacific Records•1957','\
Various•Deelder Draait•Sonic Scenery•2002','\
Les Brown And His Band Of Renown•The Cool Classics•Columbia•1955','\
Chet Baker•In Italy Unissued 1975-1988•Philology•1994'),'\
\
Forest Flower\
':('\
The Charles Lloyd Quartet•Forest Flower - Sunset•Atlantic•0','\
Charles Lloyd•Forest Flower•Atlantic•1967','\
Richard Davis (2)•Harvest•Muse Records•1979','\
Charles Lloyd•The Best Of Charles Lloyd•Atlantic•1970','\
Stephen Winfield•Forest Flower•Sona Gaia Productions•1984','\
Charles Lloyd•Forest Flower / Soundtrack•Rhino Records (2)•1994','\
Keith Jarrett•Directions: In The Charles Lloyd Mood•Eforfilms•2004','\
Chico Hamilton•The Best Of Chico Hamilton•Impulse!•1972','\
Various•Atlantic Jazz: Saxophones•Rhino Records (2)•1993','\
Charles Lloyd•Soundtrack•Atlantic•1969'),'\
\
Forever\
':('\
101 North•Forever Yours (Duet With Annette And Carl)•Capitol Records•1991','\
Stanley Jordan•Bolero•Arista•1994','\
Tony Martin (3)•Forever Amber / My Sin•RCA Victor•0','\
Harry James And His Orchestra•Lone Star Moon / Forever Amber•Columbia•1947','\
Kris Bowers•Heroes + Misfits•Concord Jazz•2014','\
John Joseph Hall•Home At Last •CBS•1979','\
Paul Jackson Jr.•Make It Last Forever•Atlantic•1990','\
Ulf Wakenius•Forever You•Stunt Records•2003','\
Gordon Jenkins•I\'m Forever Blowing Bubbles / You\'re Mine You!•Decca•1950','\
Acker Bilk And His Paramount Jazz Band•Stars And Stripes Forever / Creole Jazz•Columbia•1962','\
The Charlie Ventura Septet•East of Suez/I\'m Forever Blowing Bubbles•Decca•1949','\
Gordon Jenkins And His Orchestra•Blues For Beverly / I\'m Forever Blowing Bubbles•Columbia•1964','\
Enoch Light And The Light Brigade•Diamonds Are Forever / Fiddler On The Roof•Project 3 Total Sound•0'),'\
\
Fortune Smiles\
':('\
John McLaughlin•Where Fortune Smiles•Dawn (7)•1971','\
Karin Krog•Jazz Jamboree 75 Vol. 2•Polskie Nagrania Muza•0','\
Gary Burton•Gary Burton & Keith Jarrett•Atlantic•1971','\
Harry Beckett•Flare Up•Philips•1970','\
Various•Atlantic Jazz Introspection•Atlantic•1986','\
Keith Jarrett•Le Virtuose Du Piano•Wea Music•1996','\
Gary Burton•Gary Burton & Keith Jarrett / Gary Burton: Throb•Rhino Records (2)•1994','\
Various•The Dawn Take-Away Concert•Dawn (7)•1971'),'\
\
Four\
':('\
Kenny Graham And His Satellites•Moondog And Suncat Suites•MGM Records•1957','\
Graham Collier Music•Songs For My Father•Fontana•1970','\
Dave Lee (7)•Take Four / Five To Four On•Decca•1963','\
Barry Guy•Stringer•FMP•1983','\
Lionel Hampton All Stars•Gene Norman Presents "Just Jazz" Concert Star Dust / The Man I Love•Decca•0','\
Bob Cooper•Coop! The Music Of Bob Cooper•Contemporary Records•1958','\
Oleg Lundstrem Orchestra•In A Mellotone•Мелодия•1983','\
Lionel Hampton All Stars•Gene Norman Presents "Just Jazz" Concert Star Dust / The Man I Love•Decca•1951','\
The Dave Brubeck Quartet•Countdown / Eleven Four•Columbia•1962','\
Shorty Rogers And His Giants•Didi / Four Mothers•Capitol Records•1951','\
The Max Roach Trio•The Max Roach Trio Featuring The Legendary Hasaan•Atlantic•1965','\
Heikki Sarmanto Big Band•Everything Is It•Odeon•1972','\
Mingus Dynasty•The Next Generation•Columbia•1991','\
Michael Mantler•No Answer•WATT Works•0','\
Jon Hendricks•Cloudburst / Four Brothers•Decca•1955','\
George Benson•Breezin\' / Six To Four•Warner Bros. Records•1976','\
Karl Van Deun•Almadies•Aspen Edities•2019','\
no artist•However•MPS Records•1978','\
George Benson•Breezin\' / Six To Four•Warner Bros. Records•1976'),'\
\
Four Brothers\
':('\
Jon Hendricks•Cloudburst / Four Brothers•Decca•1955','\
Woody Herman And His Orchestra•Four Brothers / Keen And Peachy•Columbia•1949','\
Stan Getz Tenor Sax Stars•Five Brothers / Four And One Moore•New Jazz•1949','\
The Manhattan Transfer•Walk In Love•Atlantic•1978','\
Oleg Lundstrem Orchestra•In A Mellotone•Мелодия•1983','\
Jimmy Giuffre•Jimmy Giuffre (Part 1)•Capitol Records•1954','\
Woody Herman And His Orchestra•Four Brothers / Caldonia (What Makes Your Big Head So Hard?)•Columbia•0','\
The Jimmy Giuffre Trio•Princess•Fini Jazz•1990','\
Woody Herman•Live At Monterey•Atlantic•0','\
The Manhattan Transfer•Je Voulais (Te Dire Que Je T\'Attends) / Four Brothers•Atlantic•1978','\
Woody Herman•Live At Monterey•Atlantic•1976','\
Gianni Basso Quartet•Quartetto Gianni Basso•Vedette Records•1981'),'\
\
Four On Six\
':('\
Groovy Jazz Trio•Blue Songs•GJT Records Downloads•2015','\
Wynton Kelly Trio•Smokin\' At The Half Note•Verve Records•1965','\
Wes Montgomery•Twisted Blues•Ediciones Del Prado•1996','\
Wes Montgomery•Willow Weep For Me•Verve Records•1969','\
John Scofield•Solar•Fonomusic•1985'),'\
\
Four Winds\
':('\
Sammy Kaye And His Orchestra•The Four Winds And The Seven Seas•RCA Victor•1949','\
Guy Lombardo And His Royal Canadians•The Four Winds And The Seven Seas / When My Dreamboat Comes Home•Decca•1949','\
Mel Tormé•The Four Winds And The Seven Seas•Capitol Records•1949','\
Anthony Braxton•News From The 70s (Solos Duo Quartets)•Musica Jazz•1998','\
David Holland Quartet•Conference Of The Birds•ECM Records•1973','\
Michael Shrieve•Stiletto•Novus•1989','\
Dave Holland Trio•Triplicate•ECM Records•1988','\
Anthony Braxton•Quartet (Graz) 1976•Braxton Bootleg•2011','\
Eric Vloeimans•Umai•Challenge Records (3)•2000','\
Yosuke Yamashita New York Trio•Dazzling Days•Verve Records•1993','\
Buddy Collette And His Swinging Shepherds•Buddy Collette\'s Swinging Shepherds•EmArcy•1958','\
Barbara Dennerlein•Tribute To Charlie•Koala Records•1987'),'\
\
Fox Hunt\
':('\
no artist•Elysees / Fox Hunt•Jazz Parade•1950','\
Herb Alpert & The Tijuana Brass•Fox Hunt•A&M Records•1974','\
Herb Alpert & The Tijuana Brass•Fox Hunt•A&M Records•1974','\
Bill Barron•The Tenor Stylings Of Bill Barron•Savoy Records•1961','\
Kai Winding•Modern Jazz Trombones•Prestige•1951','\
Maynard Ferguson & His Orchestra•Maynard \'63•Roulette•1963','\
Maynard Ferguson•The Essence Of Maynard Ferguson•Columbia•1993','\
Chuck Mangione•Everything For Love•Chesky Records•2000','\
J.J. Johnson•Trombone By Three•Prestige•1956','\
J.J. Johnson•Looking Back•Prestige•1963','\
Maynard Ferguson•M.F. Horn 4&5: Live At Jimmy\'s•Columbia•1974','\
Maynard Ferguson•This Is Jazz•Columbia•1996'),'\
\
Freddie Froo\
':('\
Pepper Adams•Pepper Adams 5•Interlude (2)•1959','\
Pepper Adams Quintet•Pepper Adams Quintet•Mode Records•1957'),'\
\
Freddie the Freeloader\
':('\
The Wes Montgomery Trio•Portrait Of Wes•Riverside Records•1965','\
Wes Montgomery•The Artistry Of Wes Montgomery•Riverside Records•1986','\
Stanley Jordan•Magic Touch•Blue Note•1985','\
Hagood Hardy Sextet•Morocco•Unidisc•0','\
Miles Davis•Evolution Of The Groove•Columbia•2007','\
Houston Person•The Nearness Of You•Muse Records•1978','\
Philip Catherine Quartet•"Live"•Dreyfus Jazz•1997'),'\
\
Free\
':('\
The Ornette Coleman Double Quartet•Free Jazz•Atlantic•1961','\
Curiosity Killed The Cat•Free•Mercury•1987','\
Max Roach Quartet•Scott Free•Soul Note•1985','\
The Ornette Coleman Double Quartet•Free Jazz•Atlantic•1961'),'\
\
Freedom Jazz Dance\
':('\
Eddie Harris•Freedom Jazz Dance•Atlantic•1966','\
Woody Herman•The First Thing I Do / Freedom Jazz Dance•Fantasy•1973','\
Phil Woods And His European Rhythm Machine•Woods-Notes•International Joker Production•1977','\
Eddie Jefferson•Things Are Getting Better / Freedom Jazz Dance•Muse Records•1974','\
Passport (2)•Doldinger Jubilee Concert•Atlantic•1974'),'\
\
Freedomland\
':('\
Yellowjackets•Live Wires•GRP•1992','\
Yellowjackets•Greenhouse•MCA Records•1991','\
Yellowjackets•Collection•GRP•1995','\
Various•GRP 10th Anniversary Collection•GRP•1992'),'\
\
Friday Night at the Cadillac Club\
':('\
Bob Berg•Short Stories•Chase Music Group•1987','\
Bob Berg•The JazzTimes Superband•Concord Records•2000','\
Rhythmstick•Rhythmstick•CTI Records•1990'),'\
\
Friday the 13th\
':('\
Keith Tippett•Friday The 13th•Nrl Records•1997','\
Gil Evans•The British Orchestra•Mole Jazz•1983','\
The Prestige Jazz Quartet•The Prestige Jazz Quartet•Prestige•1957','\
Roswell Rudd•Regeneration•Soul Note•1983','\
Steve Grossman•Katonah•DIW•1986','\
The Steve Lacy Quartet•One Fell Swoop•Silkheart•1987','\
Thelonious Monk•Thelonious Monk / Sonny Rollins•Prestige•1956','\
The Thelonious Monk Orchestra•At Town Hall•Riverside Records•1959','\
Gil Evans•Live At Sweet Basil Vol.2•Electric Bird•1986','\
Branford Marsalis•Bloomington•Columbia•1993'),'\
\
Friends\
':('\
Eddie Harris•Olifant Gesang / Just Friends•Vee Jay Records•1961','\
Not James Player•Friends Again / Can We Still Be Friends•Ultimate Records (4)•1981','\
Charlie Parker•Just Friends•Verve Records•0','\
Bob James•Friends / Blue Lick•Tappan Zee Records•1979','\
Ornette Coleman•Friends And Neighbors - Ornette Live At Prince Street•Flying Dutchman•1970','\
Claude Bolling•With The Help Of My Friends•no label•0','\
John Kirby And His Orchestra•Milumbu / Can\'t We Be Friends•Columbia•1941','\
Supersax•Parker\'s Mood / Just Friends•Capitol Records•1973','\
Billy May And His Orchestra•Whatever Lola Wants•Capitol Records•1957','\
Charlie Parker With Strings•Just Friends / Everything Happens To Me•Karusell•1953','\
Dizzy Gillespie•The Trumpet Summit Meets The Oscar Peterson Big 4•Pablo Today•1980','\
Pete Rugolo Orchestra•The Shrike•Columbia•1955','\
Ray Conniff And His Orchestra & Chorus•Just Friends / For All We Know•CBS•1966','\
Ebanda Manfred•Ami (Let\'s Still Be Friends)•Mini Records•1983','\
Death Sentence: Panda!•Insects Awaken•Upset! The Rhythm•2008'),'\
\
Friends and Strangers\
':('\
Dave Grusin•Live In Japan•JVC•1980','\
Dave Grusin•Live In Japan•ARISTA GRP•1981','\
Ronnie Laws•Classic Masters•Capitol Records•1984','\
Ronnie Laws•Friends And Strangers•Blue Note•1977','\
Dave Grusin•Mountain Dance•JVC•1980','\
Ronnie Laws•The Best Of Ronnie Laws•Blue Note•1992','\
Various•Classic Jazz-Funk Mastercuts Volume 6 (The Definitive Jap-Jazz Mastercuts)•Mastercuts•1996','\
Various•Blue \'70s Blue Note Got Soul•Blue Note•2000','\
Various•The New Groove (The Blue Note Remix Project Volume 1)•Blue Note•1996'),'\
\
From Day To Day\
':('\
Mulgrew Miller Trio•From Day To Day•Landmark Records (3)•1990','\
Astrud Gilberto•The Shadow Of Your Smile•Verve Records•1965','\
Horace Silver•Horace Silver Trio•Blue Note•1956','\
Peter White•Perfect Moment•Columbia•1998','\
Diana Krall•From This Moment On•Verve Records•2006','\
Paul Weston And His Orchestra•Music For A Rainy Night•Columbia•1954'),'\
\
From This Moment On\
':('\
Diana Krall•From This Moment On•Universal Music•2006','\
Les Brown And His Band Of Renown•Concert At The Paladium Vol. 5•Coral•1955','\
Les Brown And His Band Of Renown•My Heart Belongs To Daddy / From This Moment On•Coral•1953','\
Frank Sinatra•If I Had You•Capitol Records•0','\
John Jenkins (2)•John Jenkins With Kenny Burrell•Blue Note•1957','\
Ella Fitzgerald•Ella Fitzgerald Sings The Cole Porter Song Book•Verve Records•0','\
Mal Waldron•Mal/2•Prestige•1957','\
The Eddie Davis-Johnny Griffin Quintet•Tough Tenor Favorites•JAZZLAND•1963','\
Kenny Dorham•This Is The Moment - Sings And Plays•Riverside Records•1958','\
Brad Mehldau•Live In Tokyo•Nonesuch•2004','\
Chauncey Gray•A Night At The El Morocco•Decca•1952','\
Les Brown And His Band Of Renown•Invitation•Coral•1954','\
Rosemary Clooney•On Stage•Columbia•1955','\
John Coltrane•Jazz Interplay•Prestige•1964'),'\
\
Funk Dumplin\
':('\
Buck Hill Quartet•Scope•SteepleChase•1979','\
Johnny Coles•Katumbo (Dance)•Mainstream Records•1972'),'\
\
Funkallero\
':('\
Mike Wofford Quartet•Funkallero•Trend (3)•1988','\
Stan Getz•Previously Unreleased Recordings•Verve Records•1973','\
Stan Getz•Live In Belgium 1974•Novadisc•0','\
Bill Evans•Unknown Session•Riverside Records•1983','\
The Howard Alden Trio•Your Story - The Music Of Bill Evans•Concord Jazz•1994','\
Bill Evans•The Bill Evans Album•Columbia•1971','\
Herbie Mann•Peace Pieces - The Music Of Bill Evans•Kokopelli Records•1995','\
David Hazeltine Trio•Waltz For Debby•Venus Records (5)•1999','\
Stan Getz•The Chick Corea / Bill Evans Sessions•Verve Records•1976'),'\
\
Funky\
':('\
Rusty Bryant•Night Train Now!•Prestige•1969','\
The Brecker Brothers•Heavy Metal Be-Bop•Arista•1978','\
The Brecker Brothers•Collection / Volume One•Novus•1990','\
Lou Donaldson•Funky Mama•Blue Note•1962','\
Pretty Purdie And The Playboys•Funky Mozart•Mega Records (4)•1971','\
Candy Dulfer•2 Funky•RCA•1993','\
Jimmy Smith•Funky Broadway•Verve Records•1967','\
James Moody•Timeless Aura•Vanguard•1976','\
André Brasseur•Funky / Rocking Chair•Fonit Cetra International•1968','\
Armando Peraza•Wild Thing / Funky Broadway•Skye Records•0','\
Charlie Brown (9)•C.C. Rider / Funky (Sunny)•Flying Dutchman•0','\
Namie Amuro•Funky Town•Avex Trax•2007','\
Papa John Creach•Filthy Funky•Grunt (3)•1972'),'\
\
Games People Play\
':('\
Dizzy Gillespie•Galveston•Solid State Records (2)•1969','\
Bert Kaempfert•Love Me Happy / Games People Play•Decca•0','\
Mel Tormé•Willie And Laura Mae Jones•Capitol Records•0','\
Dizzy Gillespie•Medley - Aquarius / Let The Sunshine In•Solid State Records (2)•1969','\
Floyd Cramer•Ob-La-Di Ob-La-Da / Games People Play•RCA•1969','\
Björn J:Son Lindh•Sissel•Metronome•1973','\
Tony Smith And The Aristocrats•Hi-Yo Silver•DeTone Records•0','\
George Duke•George Duke•Pacific Jazz•1978','\
Acker Bilk And His Paramount Jazz Band•Leave Off...It\'s Us!•Pye Records•1975','\
Johnny Watson Orchestra•Johnny Watson Orchestra•Avenue (6)•1969','\
Shirley Scott•Something•Atlantic•1970','\
George Duke•Save The Country•Liberty•1970','\
Bobby Christian•Vibe-brations•Ovation Records•1970','\
Steve Allen (3)•Soulful Brass #2•Flying Dutchman•1969','\
Bert Kaempfert•Meine Lieblingsmelodien•Polydor•1971','\
Ace Cannon•Help Me Make It Through The Night•Project 3 Records•1987','\
Living Jazz•Hot Butter & Soul•RCA Camden•1970','\
Ace Cannon•Sax Man•Hi Records•1977','\
Buddy Rich And The Big Band Machine•Speak No Evil•RCA Victor•1976'),'\
\
Gaviota\
':('\
Batida•Terra Do Sul•Timeless Records (3)•1987','\
Clare Fischer•Machaca•MPS Records•1980','\
Zweebop•Zweebop•Baby Grand•1977','\
Limousine (4)•II•no label•2011','\
Lisa Rich•Touch Of The Rare•Trend (3)•1985','\
Feather (6)•Chen Yu Lips•Trend (3)•1982','\
Elena Burke•Elena Burke•Areito•0','\
Orquesta Cubana•Mano A Mano•Velvet (2)•0','\
Frank Quintero•Despues De La Tormenta•CBS•1976','\
Ana Belén•Querida Ana•Epic•1993'),'\
\
Gee Baby Ain\'t I Good To You\
':('\
Butch Thompson•Trio West•Triangle Jazz LTD.•1984','\
Ella Fitzgerald•Live in Cologne 1974•Jazzline•2016','\
Lorraine Geller•At The Piano•Dot Records•1959','\
Matt Dusk•Just The Two Of Us•Magic Records•2015','\
Dr. John•Live At Montreux 1995•Eagle Records•2012','\
Nat King Cole•The Natural Collection•The Natural Collection•1996'),'\
\
Gemini\
':('\
Cannonball Adderley Sextet•Gemini•Riverside Records•1962','\
Gordon Lee Quartet•Land Whales in New York•Gleeful Music•1990','\
Sean Jones (2)•Gemini•Mack Avenue•2005','\
The Miles Davis Quintet•Double Image•Moon Records (4)•1989','\
Jim Pepper•Dakota Song•Enja Records•1987','\
Walt Dickerson•Divine Gemini•SteepleChase•1978','\
Nat Adderley•Here Are Nat & J. "Cannonball" Adderley At Their Rare Of All Rarest Performances Vol. 1•Kings Of Jazz•1975','\
Stanley Turrentine•I\'ll Be There•Elektra•1982','\
Mary Lou Williams Trio•Zodiac Suite•Folkways Records•1975','\
Walt Dickerson•Tenderness•SteepleChase•1985','\
Cannonball Adderley Sextet•In New York•Riverside Records•1962','\
Richard "Groove" Holmes•Living Soul•Prestige•1966','\
Darol Anger•Tideline•Windham Hill Records•1982','\
Milt Jackson Quintet•\'Live\' At The Village Gate•Riverside Records•1967'),'\
\
Gentle Rain\
':('\
Jimmy Smith•Mission Impossible / The Gentle Rain•Verve Records•1969','\
The Kenny Drew Trio•Ruby My Dear•SteepleChase•1980','\
Tubby Hayes Quartet•The Syndicate: Live At The Hopbine 1968 Vol.1•Gearbox Records•2015','\
Quincy Jones And His Orchestra•Quincy Plays For Pussycats•Mercury•1965','\
no artist•Uptown Express•Palo Alto Jazz•1985','\
Art Farmer•Gentle Eyes•Mainstream Records•1972','\
John Lewis (2)•Genes of Jazz Featuring John Lewis & Ray Brown•Sounds Of Soul Records•1987','\
Patrice Caratini•Le Chauve Et Le Gaucher•Open (3)•1978','\
Pliva Jazz Laboratory•Pliva Jazz Laboratory•Jazzette•2002'),'\
\
Gentle Rain The\
':('\
Jimmy Smith•Mission Impossible / The Gentle Rain•Verve Records•1969','\
Tubby Hayes Quartet•The Syndicate: Live At The Hopbine 1968 Vol.1•Gearbox Records•2015','\
Quincy Jones And His Orchestra•Quincy Plays For Pussycats•Mercury•1965','\
Art Farmer•Gentle Eyes•Mainstream Records•1972','\
John Lewis (2)•Genes of Jazz Featuring John Lewis & Ray Brown•Sounds Of Soul Records•1987','\
George Benson•Beyond The Blue Horizon•CTI Records•1971','\
Byron M. Davis•Dazzling Thunderstorm•Metacom•1993','\
Sarah Vaughan•Copacabana•Pablo Today•1981','\
Roy Castle•Songs For A Rainy Day•Columbia•1966'),'\
\
Gentle Wind and Falling Tear\
':('\
Gary Burton•3 In Jazz•RCA Victor•1963'),'\
\
Georgia on my mind\
':('\
Eva Olmerová•Georgia / Zpívám Dál•Panton•1980','\
Artie Shaw And His Orchestra•Star Dust / Georgia On My Mind•no label•1942','\
Quintette Du Hot Club De France•Swing Guitars / Georgia On My Mind•no label•0','\
Mildred Bailey•Rockin\' Chair / Georgia On My Mind•Bluebird (3)•1937','\
Floyd Cramer•Boogie Woogie•RCA•1979','\
Germana Caroli•A Swinging Woman•Manhattan Records (2)•1981','\
The Dave Brubeck Quartet•Georgia On My Mind•CBS•0','\
Hoagy Carmichael And His Orchestra•Rockin\' Chair / Georgia (On My Mind)•Victor•1937','\
Glenn Miller And His Orchestra•Georgia On My Mind / Jersey Bounce•no label•0','\
Louis Armstrong And His Orchestra•Lazy River / Georgia On My Mind•Parlophone•0','\
The Dave Brubeck Quartet•Georgia On My Mind•Fontana•1959','\
Jazz Orchestra Silver Bell•Georgia On My Mind / Sweet Sue Just You•Silver Bell•0','\
Nat Gonella•Georgia On My Mind / Sweet Sue - Just You•Decca•1934','\
Glen Gray & The Casa Loma Orchestra•Casa Loma Caravan (Part 2)•Capitol Records•1957','\
Frankie Laine•Georgia On My Mind / You\'re Just The Kind•Mercury•1949','\
Ray Charles•Georgia On My Mind / What\'d I Say•Stateside•1968'),'\
\
Geraldine\
':('\
Jerry Bergonzi•Inside Out•Red Record•1990','\
Yellowjackets•Twenty Five•Heads Up International•2006','\
Yellowjackets•Live Wires•GRP•1992','\
Gigi Gryce And The Jazz Lab Quintet•Gigi Gryce And The Jazz Lab Quintet•Riverside Records•1957','\
Lawrence Welk•Strictly For Dancing•Dot Records•0','\
Jean-Pierre Llabador•Brussels•Ausfahrt•1987','\
Yellowjackets•The Spin•MCA Records•1989','\
Various•GRP & KACE 103.9 FM Present The Smooth Sounds Of The Quiet Storm Volume II•GRP Records Inc.•1992','\
Donald Byrd•Young Byrd•Milestone (4)•1977','\
Big Joe Turner•Singing The Blues•BluesWay•1967'),'\
\
Get Happy\
':('\
Benny Goodman And His Orchestra•Christopher Columbus / Get Happy•Victor•1936','\
Sonny Rollins•A Night At The "Village Vanguard" Volume 3•Blue Note•1983','\
Harry James And His Orchestra•Get Happy / Melancholy Rhapsody•Columbia•1950','\
Red Norvo And His Selected Sextet•Get Happy / Congo Blues•Comet (8)•1945','\
Tony Pastor And His Orchestra•Blossoms / Get Happy•Bluebird (3)•1941','\
Charlie Parker•The Immortal Session (Vol. 1)•Sonet•1957','\
Coleman Hawkins Swing Four•Get Happy / Crazy Rhythm•Signature (4)•1944','\
Art Tatum•Sweet Lorraine / Get Happy•Decca•0','\
The Tierney Sutton Band•On The Other Side•Telarc Jazz•2007','\
Bud Powell•Piano Favorites•Clef Records•0','\
Red Callender Sextet•These Foolish Things / Get Happy•Sunset Recordings (3)•1945','\
Charlie Ventura•An Evening With Charlie Ventura And Mary Ann McCall•Norgran Records•0','\
Red Norvo•Red Norvo\'s Fabulous Jam Session•Dial Records (3)•1951','\
Bobby Byrne And His NBC Dixieland Band•Dixieland Vs Birdland - A Battle Of Jazz•MGM Records•1954','\
Harry James And His Orchestra•Get Happy•Columbia•1955','\
Oscar Peterson•Jumpin\' With Symphony Sid / Get Happy•Mercury•0','\
Lil Armstrong And Her Swing Band•Oriental Swing / Let\'s Get Happy Together•Decca•1938','\
June Christy•I\'ll Remember April / Get Happy•Capitol Records•1949'),'\
\
Get Here\
':('\
Humphrey Lyttelton And His Band•Sunday Morning / Get Out Of Here•Tempo (14)•1949','\
Dizzy Gillespie•Dizzy Gillespie Jam•Gruppo Editoriale Fabbri•1981','\
Humphrey Lyttelton And His Band•Wolverine Blues / Get Out Of Here And Go On Home•Parlophone•1951','\
Kid Ory And His Creole Jazz Band•Kid Ory\'s Creole Jazz Band 1944-45 Vol. 1•Good Time Jazz•1953','\
Kid Ory And His Creole Jazz Band•Get Out Of Here / Blues For Jimmie•Crescent (6)•1945','\
Mark Murphy•Mark Murphy - A Beautiful Friendship : Remembering Shirley Horn•Gearbox Records•2013','\
John Coltrane•Standard Coltrane•Prestige•1962','\
Arti & Mestieri•Progday•Electromantic Music•2003','\
Humphrey Lyttelton And His Band•Humphrey Lyttelton And His Band•Tempo Records (5)•1955','\
Barrelhouse Jazzband•The New Orleans Renaissance•L+R Records•1987','\
Cullen Knight•Looking Up•Tree Top Records (5)•1978'),'\
\
Get Out Of Town\
':('\
J.J. Johnson•Jennie\'s Song / Get Out Of Town•Columbia•1960','\
The Mary Kaye Trio•Get Out Of Town•Decca•1955','\
Rich Perry•Time Was•SteepleChase•2012','\
Gerry Mulligan•Jeru•Columbia•1963','\
Trio Komedy•Jazz Jamboree 1960 Nr 4•Polskie Nagrania Muza•1960','\
Mark Murphy•Mark Murphy - A Beautiful Friendship : Remembering Shirley Horn•Gearbox Records•2013','\
René Thomas Quintet•René Thomas Et Son Quintette•BMG•1997','\
Ella Fitzgerald•Ella Fitzgerald Sings The Cole Porter Song Book - Volume 2•Verve Records•0','\
Cecil Taylor Trio•Love For Sale•United Artists Records•1959','\
Cecil Taylor Trio•Love For Sale•United Artists Records•1959','\
Various•8 Ways to Jazz - the music of Cole Porter•Riverside Records•1958','\
Frank Strozier Sextet•Remember Me•Steeplechase•1977'),'\
\
Get Ready\
':('\
James Ingram•Get Ready•Warner Bros. Records•1991','\
The Dave Brubeck Quartet•Experiments In Time - Vol. 2•Fontana•0','\
The Dave Brubeck Quartet•Time Out Volume 1•CBS•0','\
The Dave Brubeck Quartet•Three To Get Ready / Who\'s Afraid•Columbia•1966','\
The Dave Brubeck Quartet•Three To Get Ready•Columbia•1963','\
Dave Brubeck•Take Five / Three To Get Ready•Atlantic•0','\
Billy Harper•Soran-Bushi B.H.•Denon•1978','\
Dave Brubeck•Blue Rondo (A La Turk)•Atlantic•1973','\
Stefan Raab•Get Ready•UBM Records•1993','\
Woody Herman And His Orchestra•At The Woodchoppers Ball•Ember Records•1965','\
Dave Brubeck•Moscow Night•Concord Jazz•1988','\
Woody Herman•Live At Peacock Lane Hollywood•Bandstand•1988','\
Woody Herman And The Thundering Herd•Crown Royal•LaserLight Digital•1992','\
Eric Mintel Quartet•Impressions Of Jazz•Jazz Lions•1996','\
Woody Herman•Ready Get Set Jump•Ediciones Del Prado•1996','\
Dave Brubeck•Dave Brubeck And Paul Desmond•Giants Of Jazz•1984','\
Dave Brubeck•Star-Collection•Midi•1975','\
The Dave Brubeck Quartet•Time Out•Columbia•1998'),'\
\
Gettin\' It Togetha\'\
':('\
Bobby Timmons•Walkin! Wadin! Sittin! Ridin! / Gettin\' It Togetha\'•Prestige•1965','\
Bobby Timmons•Chun-King•Prestige•1965','\
Bobby Timmons•The Prestige Trio Sessions•Prestige•2003'),'\
\
Ghost Of A Chance\
':('\
Charlie Ventura Sextet•Ghost Of A Chance / Tea For Two•Sunset Recordings (3)•0','\
Erroll Garner•All Of Me / I Don\'t Stand A Ghost Of A Chance•Savoy Records•1949','\
Artie Shaw And His Orchestra•(I Don\'t Stand) A Ghost Of A Chance / Let\'s Walk•Musicraft•1946','\
Flip Phillips•Jazz At The Philharmonic - Norgran Blues 1950•Verve Records•1983','\
Marc Charig•Pipedream•Ogun•1977','\
Johnny Smith Quintet•Moonlight In Vermont •Royal Roost•1956','\
Lester Young•I Don\'t Stand A Ghost Of A Chance / Back Home Again In Indiana•Savoy Records•1948','\
Lew Tabackin•Vintage Tenor•RCA•1978','\
Lester Young•Jazz Masters•Savoy-Musidisc•0','\
Lionel Hampton All Stars•Besuch Auf Einem Wolkenkratzer•Jazztone (2)•1956','\
no artist•Dexterity•Concert Hall Society•1955','\
Sonny Stitt•Constellation•Cobblestone•1972','\
Hal Galper Trio•Rebop•Enja Records•1995'),'\
\
Ghost Of A Chance A\
':('\
Charlie Ventura Sextet•Ghost Of A Chance / Tea For Two•Sunset Recordings (3)•0','\
Erroll Garner•All Of Me / I Don\'t Stand A Ghost Of A Chance•Savoy Records•1949','\
Artie Shaw And His Orchestra•(I Don\'t Stand) A Ghost Of A Chance / Let\'s Walk•Musicraft•1946','\
Johnny Smith Quintet•Moonlight In Vermont •Royal Roost•1956','\
Flip Phillips•Jazz At The Philharmonic - Norgran Blues 1950•Verve Records•1983','\
Lew Tabackin•Vintage Tenor•RCA•1978','\
Lester Young•I Don\'t Stand A Ghost Of A Chance / Back Home Again In Indiana•Savoy Records•1948','\
Marc Charig•Pipedream•Ogun•1977','\
Lionel Hampton All Stars•Besuch Auf Einem Wolkenkratzer•Jazztone (2)•1956','\
Lester Young•Jazz Masters•Savoy-Musidisc•0','\
Artie Shaw•Artie Shaw Plays•Royale•0','\
Hal Galper Trio•Rebop•Enja Records•1995','\
Johnny Smith Quintet•Jazz At NBC•Royal Roost•1953'),'\
\
Giant Steps\
':('\
Anthony Braxton•Duo (Verona) 1989•Braxton Bootleg•2011','\
John Coltrane•Giant Steps•Atlantic•1960','\
John Coltrane•John Coltrane•Fabbri Editori•1979','\
Toshiyuki Miyama & The New Herd•Orchestrane New Herd Plays John Coltrane•Denon Jazz•1977','\
Bob Mintzer•The Saxophone featuring Two T\'s•Novus•1993','\
Toshiko Akiyoshi Trio•Time Stream•Eastworld•1985','\
Jamey Aebersold•Eight Jazz Originals By John Coltrane•JA Records•1983','\
Nobuo Hara and His Sharps & Flats•Giant Steps•King Records•1978','\
The Visitors (10)•In My Youth•Muse Records•1973','\
Archie Shepp•California Meeting - Live "On Broadway"•Soul Note•1987','\
Songyi Jeon Quintet•Straight•Not On Label (Songyi Jeon Self-released)•2015','\
George Muribus•Trio \'77•Catalyst Records (3)•1977','\
Franco Cerri•Demoiselle•Not On Label•1979','\
Archie Shepp•I Know About The Life•Sackville Recordings•1981','\
John Coltrane•The Best Of John Coltrane•Atlantic•1970'),'\
\
Girl From Ipanema\
':('\
David James•Girl From Ipanema•Sus Records•1989','\
Astrud Gilberto•The Girl From Ipanema•Verve Records•1984','\
Afro Blue Persuasion•Philadelphia Mambo / Girl From Ipanema•Tramp Records•2018','\
Stan Getz•The Girl From Ipanema•MGM Records•1964','\
Astrud Gilberto•The Girl From Ipanema / Desafinado•Old Gold (2)•1990','\
The Glenn Miller Orchestra•The Girl From Ipanema•Epic•1965','\
Tony Mottola•Brasilia / The Girl From Ipanema•Command•0','\
Herbie Mann•Soft Winds / The Girl From Ipanema•Atlantic•1963','\
Brother Jack McDuff•The Girl From Ipanema•Prestige•1965','\
Stan Getz•The Girl From Ipanema•Verve Records•1964','\
Warren Covington And His Orchestra•The Girl From Ipanema•Decca•1964','\
Astrud Gilberto•The Girl From Ipanema•Image Records•1977','\
Stan Getz•The Girl From Ipanema•Verve Records•1964','\
Herb Alpert & The Tijuana Brass•All My Lovin\'•A&M Records•0','\
Antonio Carlos Jobim•Corcovado / The Girl From Ipanema•Verve Records•0','\
Ernie Heckscher•The Girl From Ipanema•Columbia•1964'),'\
\
Girl Talk\
':('\
Neal Hefti His Orchestra & Chorus•Girl Talk / Lonely Girl•CBS•1965','\
Buddy Greco•This Is Your Life•Reprise Records•1968','\
Ramsey Lewis•Girl Talk / Dancing In The Street•Cadet•1967','\
Galapagos Duck•Moomba Jazz \'76 Live From Dallas Brooks Hall Vol. 2•44 Records (2)•1976','\
Joe Beck Trio•Girl Talk•Venus Records (5)•2003','\
Ralph Moore (2)•Furthermore•Landmark Records (3)•1990','\
Jimmy McGriff Organ And Blues Band•The Worm•Solid State Records (2)•1968','\
Dakota Staton•I Want A Country Man•Groove Merchant•1973','\
Cedar Walton•The Trio 3•Red Record•1986','\
Chet Baker•My Foolish Heart•IRD Records (2)•1989','\
The Red Star Orchestra•Olivia Sings For The Red Star•Polydor•2012','\
Ray Bryant•Here\'s Ray Bryant•Pablo Records•1976','\
The Three Sounds•Live At The \'It Club\' Volume 2•Blue Note•2000','\
Quartette Trés Bien•Four Of A Kind•Decca•1968'),'\
\
Give Me The Simple Life\
':('\
Mavis Rivers•At Sundown / Give Me The Simple Life•Capitol Records•0','\
Sammy Kaye•It Might As Well Be Spring / Give Me The Simple Life•Victor•1945','\
no artist•Jay Cameron\'s International Sax-Band•Swing (3)•1955','\
The Four Freshmen•Four Freshmen And Five Trumpets Part 2•Capitol Records•0','\
Various•Jazz Horizons: Down Beat Jazz Concert Vol. 2•Dot Records•0','\
Billy Taylor Trio•The Billy Taylor Trio•Prestige•1953','\
Cal Tjader Trio•The Cal Tjader Trio•Fantasy•1953','\
Oscar Peterson•Oscar\'s Choice•MPS Records•1974','\
Shirley Scott•Blue Seven•Prestige•1965','\
Stan Getz Quintet•Interpretations By The Stan Getz Quintet #3•Norgran Records•1955','\
Wes Montgomery•One Night In Indy•Resonance Records•2015','\
Various•Laboratory Test Record: Sound Showcase•United Artists Ultra Audio•1960'),'\
\
Gloria\'s Step\
':('\
The Bill Evans Trio•The Legendary Trio•Fantasy•0','\
Various•Музыка Ретро•Домашняя Коллекция•2000'),'\
\
God Bless the Child\
':('\
Tony Bennett•God Bless The Child•Columbia•1998','\
Eddie Harris•My Buddy•Vee Jay Records•1961','\
Keith Jarrett•God Bless The Child (Edit)•ECM Records•1983','\
Freddie Hubbard•At Jazz Jamboree Warszawa \'91 - A Tribute To Miles•no label•1991','\
Eric Dolphy•In Europe Vol. 1•Prestige•1964','\
Freddie Hubbard•Bolivia•Musicmasters•1991','\
George Freeman•Franticdiagnosis•Bam-Boo Records•1972','\
Vivian Reed•God Bless The Child / Sweet Georgia Brown•H & L Records•1976','\
Walt Dickerson•To My Queen•New Jazz•1962','\
Ruth Olay•God Bless The Child / I Ain\'t Got Nothin\' But The Blues•ABC Records•1966','\
The Pablo All-Stars Jam•Montreux \'77•Pablo Live•1977','\
Eric Dolphy•Stockholm Sessions•Enja Records•1981'),'\
\
Goin\' Home\
':('\
Harry James (2)•The Melancholy Trumpet / Goin\' Home•Columbia•1952','\
Tommy Dorsey And His Orchestra•Goin\' Home / Humoresque•Victor•1937','\
McCoy Tyner•Asante•Blue Note•1974','\
The Three Sounds•Goin\' Home•Blue Note•1958','\
Yusef Lateef•Salt Water Blues / Goin\' Home•Riverside Records•1960','\
Ted Dale And His Orchestra•"Goin\' Home"/" Stars In My Eyes"•Silvertone Record Club•1950','\
Percy Faith & His Orchestra•Goin\' Home Train•Columbia•1959','\
Stanley Turrentine•Hustlin\'•Blue Note•1965','\
Clarence Shaw•Carnival Sketches•Argo (6)•1964','\
Charles Earland•Intensity•Prestige•1972','\
Ike Quebec•Bossa Nova Soul Samba•Blue Note•1962','\
The Three Sounds•The 3 Sounds•Blue Note•1958','\
Sonny Phillips•My Black Flower•Muse Records•1977','\
Yellowjackets•Mirage À Trois•Warner Bros. Records•1983'),'\
\
Golden Lady\
':('\
The Sun Ra Arkestra•The Nubians Of Plutonia•El Saturn Records•1969','\
José Feliciano•Golden Lady•RCA Victor•1974','\
Abbey Lincoln•In Paris / Painted Lady•Blue Marge•1980','\
Duke Ellington And His Orchestra•2 - Hy\'a Sue•Philips•0','\
Kurt Elling•The Gate•Decca•0','\
Mark De Clive-Lowe•Live At The Blue Whale•Mashibeats•2017','\
Zbigniew Lewandowski•Golden Lady•Polskie Nagrania Muza•1989','\
Soulive•Steady Groovin\'•Blue Note•2005','\
Marion Brown Quintet•Offering•Venus Records (5)•1993','\
Special EFX•Double Feature•GRP•1988','\
Mal Waldron•Songs Of Love And Regret•Free Lance•1987','\
Acoustic Alchemy•Against The Grain•GRP•1994','\
Duke Ellington And His Orchestra•Mood Ellington•Columbia•1949'),'\
\
Golden Notebooks\
':('\
Gerry Mulligan•The Age Of Steam•A&M Records•1972'),'\
\
Gone With the Wind\
':('\
Percy Faith & His Orchestra•Tara Theme (From Gone With The Wind)•Columbia•1967','\
Billy May And His Orchestra•Gone With The Wind / Romance•Capitol Records•1953','\
Stan Getz Quartet•Gone With The Wind / Hershey Bar•Royal Roost•0','\
Mel Tormé•Gone With The Wind / Little White Lies•Musicana•1948','\
Ella Fitzgerald•Mack The Knife / Gone With The Wind•Verve Records•0','\
The Dave Brubeck Quartet•Georgia On My Mind•Fontana•1959','\
The Dave Brubeck Quartet•Don\'t Worry \'Bout Me•Philips•1956','\
Art Tatum•The Tatum Group Masterpieces Vol. 8•Pablo Records•1990','\
Wynonie Harris•Here Comes The Blues / She\'s Gone With The Wind•Apollo Records (2)•1946','\
Clifford Brown Ensemble•Clifford Brown Ensemble Featuring Zoot Sims•Vogue•1956','\
Art Tatum•Gone With The Wind / Stormy Weather•Decca•1937','\
Hans Koller New Jazz Stars•For Moderns•Harmona•0','\
The Martyn Ford Orchestra•Theme From "Gone With The Wind"•Mountain•1976','\
Billy May And His Orchestra•It\'s Billy May Time•Capitol Records•0','\
Dolo Coker•California Hard•Xanadu Records•1977'),'\
\
Good Bait\
':('\
John Coltrane•Good Bait•Prestige•1959','\
Gene Norman•Manteca - Emanon - Good Bait•Gene Norman Presents•1955','\
Dizzy Gillespie•Good Bait / Early Mornin\' Blues•Philips•1963','\
Fats Navarro•Blowing At The Royal Roost•Ediciones Del Prado•1996','\
Dizzy Gillespie•I Can\'t Get Started / Good Bait•Manor•1946','\
Fats Navarro•Royal Roost Sessions 1948•Fresh Sound Records•1991','\
Werner Pfüller Quintett•Good Bait / En Avant / Blaue Straßen / Rosé•AMIGA•1962','\
Fats Navarro•At The Royal Roost 1948 (Volume 1)•Beppo Records•0','\
Fats Navarro•Featured With The Tadd Dameron Band•Milestone (4)•1977','\
Dizzy Gillespie•Gillespie Concert N.1 1950•Super Oscar•1975','\
Nina Simone•For All We Know / Good Bait•Bethlehem Records•1960','\
Fats Navarro•Fats Navarro Featured With The Tadd Dameron Quintet•JAZZLAND•1961','\
The Billy Wallace Trio•Good Bait / A Pretty Girl is Like A Melody•GIG Records (7)•1956','\
Dexter Gordon•Live At The Amsterdam Paradiso Volume One•Affinity•1980','\
Art Pepper•Renascence•Galaxy•2000','\
James Moody•Too Heavy For Words•MPS Records•1973','\
Dizzy Gillespie And His Orchestra•Gene Norman Presents Dizzy Gillespie And His Orchestra Featuring Chano Pozo•Vogue Records•1954'),'\
\
Good Evening Mr. and Mrs. America\
':('\
Tom Scott•Tom Cat•Ode Records (2)•1975','\
Tom Scott•Tom Scott & The L.A. Express / Tom Cat / New York Connection•BGO Records•2014','\
Frank Sinatra•The Complete Reprise Studio Recordings•Reprise Records•1995','\
Various•Sony Music 100 Years: Soundtrack For A Century•Sony Music•1999'),'\
\
Good Life The\
':('\
Eddie Heywood•Canadian Sunset (Bossa Nova)•Liberty•1963','\
Sarah Vaughan•A Taste Of Honey / The Good Life•Roulette•1963','\
Lalo Schifrin•Broken Date•MGM Records•1963','\
Asako Toki•Standards•LD&K•2004','\
The Oscar Peterson Trio•The Good Life•Pablo Live•1984','\
Tony Bennett•The Good Life•Columbia•0','\
Lloyd Mayers•Taste Of Honey•United Artists Jazz•1962','\
Sammy Davis Jr.•We\'ll Be Together Again•Reprise Records•1966','\
Tony Bennett•The Good Things In Life•Verve Records•1972','\
Jack Wilson•The Two Sides Of Jack Wilson•Atlantic•1964','\
Clark Terry Sextet•Clark Terry Sextet•Cameo Parkway•1962','\
The Three Sounds•Today\'s Sounds•Limelight•1966','\
Eddie "Lockjaw" Davis•Light And Lovely•Black And Blue•0','\
Frank Sinatra•Hello Dolly!•Reprise Records•0','\
Hank Mobley•The Turnaround•Blue Note•1965','\
Tony Bennett•The Good Things In Life•MGM Records•1972','\
The Three Sounds•Today\'s Sounds•Limelight•1966','\
Charlie Haden•Quartet West•Verve Records•1987'),'\
\
Good Morning Heartache\
':('\
Billie Holiday•Good Morning Heartache / No Good Man•Decca•1946','\
Lou Donaldson•Sanford And Son Theme / Good Morning Heartache•Blue Note•1973','\
Various•Aurex Jazz Festival (1980): Jazz At The 80\'s•Eastworld•1980','\
Natalie Cole•Sophisticated Lady (She\'s A Different Lady)•Capitol Records•1976','\
Kunihiko Sugano•The Days Of Wine And Roses•Nadja•1976','\
George Coleman•George Coleman At Yoshi\'s•Theresa Records•1989','\
Art Pepper•Ballads By Four•Galaxy•1981','\
Hank Crawford•Wildflower•Kudu•1973','\
Webster Young•For Lady•Prestige•1957','\
Kellye Gray•Standards In Gray•Justice Records (2)•1990','\
Lou Donaldson•Poinciana•Jazz Bird•1979','\
Yasuda Minami•South•Bellwood Records•1974','\
Kunihiko Sugano Trio•Everything Happens To Me•Audio Lab. Record•1975','\
Kenny Burrell•Both Feet On The Ground•Fantasy•1973','\
Joe Henderson•Black Narcissus•Milestone (4)•1976'),'\
\
Goodbye Look\
':('\
no artist•Look Around•A&M Records•1968','\
no artist•Look Around•A&M Records•1968','\
Cal Tjader•Breathe Easy•Galaxy•1978','\
Sonny Rollins•Together At Newport 1963•Jazz On Jazz•2015'),'\
\
Goodbye Porkpie Hat\
':('\
Lauren Newton•Voiceprint•Extraplatte•1988','\
Jerry Gonzalez•Music For Big Band•EmArcy•2007','\
The Judy Roberts Band•The Judy Roberts Band•Madonna Records•1979','\
The Aki Takase Septet•Oriental Express•Omagatoki•1996','\
Jay Clayton•Sound Songs•JMT Productions•1986','\
Charles Mingus•Three Or Four Shades Of Blues•Atlantic•1977','\
Karl Denson•Herbal Turkey Breast•Minor Music•1993','\
No BS Brass Band•Fight Song: A Tribute to Charles Mingus•Not On Label•2013','\
Denny Zeitlin•Trio•Windham Hill Jazz•1988'),'\
\
Got a Match\
':('\
Lou Stein•Got A Match / Who Slammed The Door•Mercury•1958','\
The Chick Corea Elektric Band•Live From Elario\'s (The First Gig)•Stretch Records•1996','\
The Chick Corea Elektric Band•The Chick Corea Elektric Band•GRP•1986','\
Charged Particles•Charged Particles•no label•1994','\
The Chick Corea Elektric Band•Live At Montreux 2004•Eagle Vision•2005','\
Roger Webb•Number 7  - Sound Waves•Media Music The Professional•0','\
The Ames Brothers•Merry Christmas•Vogue Coral•1954','\
Moses Dillard & Tex-Town Display•Now!•Tex-Town Records•1969'),'\
\
Grand Central\
':('\
Ron Escheté•Line-Up•Muse Records•1981','\
The Cannonball Adderley Quintet•In Chicago•Mercury•1959','\
The Cannonball Adderley Quintet•In Chicago•Mercury•1959','\
The Cannonball Adderley Quintet•In Chicago•Mercury•1960','\
Robert Q. Lewis•I\'d Like To Baby You / Grand Central Station•MGM Records•0','\
Poncho Sanchez•Psychedelic Blues•Concord Picante•2009','\
Henryk Miśkiewicz•No More Love•Polonia Records•2000'),'\
\
Green Dolphin Street\
':('\
Miles Davis•On Green Dolphin Street•Jazz Door•1992','\
Miles Davis•The Miles Davis Quintet & Sextet•CBS/Sony•1973','\
Victor Feldman•Green Dolphin Street / Overfat Cat•Vee Jay Records•1965','\
Harry Edison•Blues For Christine•Sue Records Inc.•1964','\
The Miles Davis Sextet•Miles At Newport•CBS•1968','\
The Three Sounds•On Green Dolphin Street / Love For Sale•Blue Note•1960','\
Miles Davis•The Final Tour: Copenhagen March 24 1960•Columbia•2018','\
The Oscar Peterson Trio•Very Tall•Verve Records•1963','\
Sonny Rollins Quartet•"Live" In Europe•Unique Jazz•0','\
Miles Davis•Copenhagen 1960•Royal Jazz•1989','\
Sonny Rollins Quartet•Stuttgart 1963 Concert•Jazz Connoisseur•0','\
Sonny Rollins Quartet•In Europe 1963 - Vol. II•Jazz Up•1989','\
Miles Davis•Blue Christmas•CBS•1983','\
Monty Alexander•Unlimited Love - Live & In Concert•BASF•1976','\
Miles Davis•Miles Davis At Plugged Nickel Chicago•CBS/Sony•1976'),'\
\
Green Dolphin Street On\
':('\
Miles Davis•On Green Dolphin Street•Jazz Door•1992','\
Miles Davis•The Miles Davis Quintet & Sextet•CBS/Sony•1973','\
Miles Davis•The Final Tour: Copenhagen March 24 1960•Columbia•2018','\
The Miles Davis Sextet•Miles At Newport•CBS•1968','\
The Three Sounds•On Green Dolphin Street / Love For Sale•Blue Note•1960','\
The Oscar Peterson Trio•Very Tall•Verve Records•1963','\
Miles Davis•Copenhagen 1960•Royal Jazz•1989','\
Sonny Rollins Quartet•Stuttgart 1963 Concert•Jazz Connoisseur•0','\
Miles Davis•Blue Christmas•CBS•1983','\
Miles Davis•Miles Davis At Plugged Nickel Chicago•CBS/Sony•1976','\
Oscar Peterson•The Sound Of The Trio•Verve Records•1961','\
The Miles Davis Quintet•Live•Unique Jazz•0'),'\
\
Green Mountains\
':('\
Gary Burton Quartet•Live In Tokyo•Atlantic•1971','\
Gary Burton Quartet•Live In Tokyo•Atlantic•2013','\
Michael Davis•Absolute Trombone •Hip-Bone Music•1997','\
Gary Burton•Alone At Last•Atlantic•1971','\
Gary Burton Quartet•Country Roads & Other Places•RCA Victor•1969','\
Various•Yesterdays Goodies•United Artists Records•1964','\
The Golden Gonk•Hye & Hellow•Shack In The Barley Productions•2005'),'\
\
Gregory is Here\
':('\
The Matteson - Phillips Tubajazz Consort•The Matteson-Phillips Tubajazz Consort•Mark Records•1977','\
Jamey Aebersold•Horace Silver - Eight Jazz Classics:  Volume 17•JA Records•1978','\
Horace Silver•The Best Of Horace Silver Vol. II•Blue Note•1989','\
Horace Silver•In Pursuit Of The 27th Man•Blue Note•1973','\
Various•It Happened In.... Pescara (1969-1989)•Philology•1990'),'\
\
Groove Merchant\
':('\
Jerome Richardson•Groove Merchant •Verve Records•1967','\
Jon Hendricks & Company•Love•Muse Records•1982','\
Thad Jones / Mel Lewis Orchestra•Central Park North•Solid State Records (2)•1969','\
Tommy Chase•Groove Merchant•Stiff Records•1987','\
Herb Ellis•Windflower•Concord Jazz•1978','\
Thad Jones & Mel Lewis•Live On Tour Switzerland•Lester Recording Catalog•2006','\
Thad Jones & Mel Lewis•Thad Jones Mel Lewis & UMO•RCA Victor•1978','\
Thad Jones & Mel Lewis•Thad Jones / Mel Lewis•Lester Recording Catalog•1990','\
Holly Hofmann•Take Note !•Capri Records (6)•1989'),'\
\
Groove Yard\
':('\
The Montgomery Brothers•Groove Yard•Riverside Records•1961','\
Billy Hart Quartet•One Is The Other•ECM Records•2014','\
Les McCann•Soul Hits•Pacific Jazz•1964','\
Project G-7•A Tribute To Wes Montgomery Volume I•Evidence (5)•1993','\
The Montgomery Brothers•Groove Yard•Riverside Records•1961','\
Larry Fuller Trio•Easy Walker•GML (4)•2001','\
Wes Montgomery•March 6 1925-June 15 1968•Riverside Records•1968','\
Pat Martino•Remember: A Tribute To Wes Montgomery•Blue Note•2006','\
The Trio (10)•The Trio•Riverside Records•1961','\
Joe Beck•Empathy•Gryphon•1980','\
Marian McPartland•In My Life•Concord Jazz•1993','\
Scott Hamilton•Race Point•Concord Jazz•1992','\
Wes Montgomery•Groove Brothers•Milestone (4)•1979','\
Wes Montgomery•The Best Of Wes Montgomery•Riverside Records•0'),'\
\
Groovin\' High\
':('\
Bird (28)•Bird & Diz In Concert•Sonet•0','\
Dizzy Gillespie•Groovin\' High•Philips•1964','\
Various•Tribute To Charlie Parker•Verve Video•1991','\
Stan Getz•Groovin\' With Getz•Custom Records (2)•1966','\
Lou Donaldson•Lou Takes Off•Blue Note•1958','\
Dizzy Gillespie•Dizzy Gillespie Plays•Royale•0','\
Hampton Hawes Quartet•All Night Session Vol. 1•Contemporary Records•1958','\
Stan Getz•Groovin\' High•Crown Records (2)•1957','\
Sonny Stitt & His West Coast Friends•Groovin\' High•Atlas Record (2)•1980','\
Archie Shepp Quartet•Splashes (Tribute To Wilbur Little)•L+R Records•1987','\
Stan Getz•Groovin\' High•Modern Records (2)•1956'),'\
\
Grow Your Own\
':('\
Gary Burton•Gary Burton & Keith Jarrett•Atlantic•1971','\
The Mike Gibbs Band•Just Ahead•Polydor•1972','\
Gary Burton•Gary Burton & Keith Jarrett / Gary Burton: Throb•Rhino Records (2)•1994','\
Keith Jarrett•Le Virtuose Du Piano•Wea Music•1996','\
John Schroeder•Witchi Tai To•Pye Records•1971','\
Gary Burton•Turn Of The Century•Atlantic•1976','\
Lina Nyberg•Close•Prophone•1993','\
Keith Jarrett•Somewhere Before: The Keith Jarrett Anthology (The Atlantic Years 1968-1975)•Warner Jazz•2008','\
Basil Fomeen And His Orchestra•Song Hits Of 1928•Decca•1947','\
Various•The Sound Spectrum•When! Recordings•1995'),'\
\
Growing\
':('\
The Great Revivers•Growing Older•Fnr•2017','\
Burt Bacharach•Something Big•A&M Records•1973','\
Ornette Coleman•Man On The Moon / Growing Up•Stateside•1969','\
Lee Morgan•Infinity•Blue Note•1981','\
Piero Condorelli Sonora Art Quartet•Sonora•Innowo•1990','\
Morten Schantz•Godspeed•Edition Records•2017','\
Cees Slinger•Sling Shot!•Timeless Records (3)•1986','\
Little Eye•EP•Ethbo Records•1992','\
New Zion Trio•Sunshine Seas•RareNoise Records•2016','\
Sven Libaek•Inner Space (The Lost Film Music Of Sven Libaek)•Trunk Records•2006','\
Alvin Queen•A Day In Holland•Nilva Records•1983','\
no artist•(Now And Then There Is) A Fool Such As I•Argo (6)•1959','\
Paul Hoffert•The Jazz Roots Of Paul Hoffert•Chateau•1961','\
Volker Kriegel•Spectrum•MPS Records•1971','\
John Patitucci•John Patitucci•GRP•1988','\
Fats Waller & His Rhythm•Dream Man / I\'m Growing Fonder Of You•Victor•1934','\
The M.P. Olsson Quintet•Going With The Flow•Lotus Eye Music•1985'),'\
\
Guaruja\
':('\
Randy Brecker•Amanda•Passport Jazz•1985','\
Randy Brecker•Randy In Brasil•Mama Records (2)•2008','\
Charlie Byrd•More Brazilian Byrd•Columbia•1967','\
Paulinho Da Costa•Breakdown•A&M Records•1991'),'\
\
Gush\
':('\
Maria Schneider Orchestra•Evanescence•Enja Records•1994','\
Louis Bellson•Louie Bellson Jam•Pablo Records•1979'),'\
\
Hackensack\
':('\
The Benson Orchestra Of Chicago•Doodle-Doo-Doo / Back In Hackensack New Jersey•Victor•1924','\
Frank Foster•Locomotive•Metronome•1957','\
The Thelonious Monk Quartet•Bye-Ya•Columbia•1963','\
The Thelonious Monk Quartet•In Europe•Unique Jazz•0','\
The Thelonious Monk Quartet•Thelonious Monk In Europe Vol. 2•Riverside Records•1964','\
Tony Fruscella•Fru\'n Brew (Previously Unissued Recordings From The Open Door)•Spotlite Records•1981','\
Art Pepper•Inglewood Jam 1952•Absord Music Japan•2009','\
Thelonious Monk•Hackensack•Drive (3)•1989','\
Thelonious Monk•Criss-Cross•Columbia•0','\
Pascal Schumacher•Face To Face In Bremen - Live•Enja Records•2009','\
The Thelonious Monk Quintet•Thelonious Monk Quintet•Prestige•1954','\
The Bud Powell Trio•At The Golden Circle Volume 1•SteepleChase•1978','\
Thelonious Monk•Blue Monk•Bandstand•1987','\
Engstfeld Plümer Weiss•Drivin\'•NABEL•1985','\
Thelonious Monk•At Newport 1963 & 1965•Columbia•2002','\
Jimmy Smith•Jazz Profile: Jimmy Smith•Blue Note•1997','\
The Bob Cooper - Conte Candoli Quintet•The Bob Cooper - Conte Candoli Quintet•V.S.O.P. Records•1994'),'\
\
Half Nelson\
':('\
Miles Davis•Birdland 1951•Blue Note•2004','\
The Charlie Parker All-Stars•Chasing The Bird / Half-Nelson•Metronome•1949','\
Joe Roland•Half-Nelson / Sally Is Gone•Mercer Records•1950','\
Fats Navarro•Goin To Mintons / Half-Nelson•Savoy Records•1947','\
Miles Davis•At His Rare Of All Rarest Performances Vol. 1•Kings Of Jazz•1981','\
Gerry Mulligan Quartet•Gene Norman Presents The Gerry Mulligan Quartet•Gene Norman Presents•1954','\
Miles Davis•Miles Davis At Birdland 1951•Beppo Records•0','\
Art Farmer•In Concert•Enja Records•1986','\
Charlie Parker•Charlie Parker Memorial Volume 3•Realm Jazz•1963','\
Charlie Parker•Apartment Jam Sessions•Zim Records•1977','\
Xanadu•Xanadu At Montreux Volume Three•Xanadu Records•1979','\
Charlie Rouse•Social Call•Uptown Records (2)•1984','\
Jackie McLean•The Source Vol.2•SteepleChase•1974','\
Anthony Braxton•In The Tradition Volume 2•SteepleChase•1976','\
Frank Morgan•Lament•Contemporary Records•1986','\
Gerry Mulligan Quartet•Gene Norman Presents The Gerry Mulligan Quartet•Gene Norman Presents•1954','\
Sam Most•Plays Bird Bud Monk And Miles•Bethlehem Records•1957','\
Charlie Parker•The \'Bird\' Returns•Savoy Records•1962'),'\
\
Hallucinations\
':('\
Pascal Schumacher•Face To Face In Bremen - Live•Enja Records•2009','\
Miles Davis & His Tuba Band•Pre-Birth Of The Cool•Durium•1974','\
The Phil Woods Quartet•Live Volume One•Clean Cuts•1980','\
Ellis Marsalis•Piano In E/Solo Piano•Rounder Records•1991','\
The Herb Robertson Brass Ensemble•Shades Of Bud Powell•JMT•1988','\
Alfredo Naranjo Jazz Band•A Través del Tiempo•Lyric (2)•1996','\
Bud Powell•Simply Amazing!!•Accord (2)•1982','\
Kenny Barron Quintet•Images•Gitanes Jazz Productions•2004','\
Shankar•M.R.C.S.•ECM Records•1991','\
John Campbell (18)•After Hours•Contemporary Records•1989','\
Terence Blanchard•Magnetic•Blue Note•2013'),'\
\
Happy Little Sunbeam\
':('\
Chet Baker Quartet•Chet Baker Plays The Compositions Of Russ Freeman•Pacific Jazz•0','\
Chet Baker Quartet•Chet Baker Quartet Featuring Russ Freeman•Pacific Jazz•1953','\
Chet Baker•The Trumpet Artistry Of Chet Baker•Pacific Jazz•1955','\
Chet Baker Quartet•The Lost Holland Concert - September 18 1955•RLR Records•2006','\
Elsie Bianchi•Fly Me To The Moon (Unreleased Swiss Radio Jazz 1960-62)•Sonorama•2011','\
Chet Baker•The Best Of Chet Baker Plays•Pacific Jazz•1992','\
Chet Baker•The Definitive Chet Baker•Blue Note•2002','\
Iancsy Körössy•Kőrössy János És Együttese•Qualiton•1964','\
Various•Jazz West Coast•Pacific Jazz•1955','\
Chet Baker•Plays And Sings•World Pacific Jazz•1968','\
Chet Baker Quartet•The Complete Pacific Jazz Studio Recordings Of The Chet Baker Quartet With Russ Freeman•Mosaic Records (2)•1987'),'\
\
Hard Eights\
':('\
Lyle Mays•Fictionary•Geffen Records•1993'),'\
\
Harlem Nocturne\
':('\
Georgie Auld•Harlem Nocturne / Tenderly•Coral•0','\
David Rose & His Orchestra•Vanessa•MGM Records•1953','\
Lounge Lizards•Harlem Nocturne = Harlem Nocturno•Editions EG•1981','\
Georgie Auld•Manhattan / Harlem Nocturne•United Artists Records•0','\
The Tokyo Happy Coats•Harlem Nocturne / Forevermore "Kinito Itsumademo"•King Records (3)•1970','\
Georgie Auld•Lullaby Of Broadway / Harlem Nocturne•Coral•1953','\
Stan Kenton And His Orchestra•Hush-a-Bye / Harlem Nocturne•Capitol Records•1953','\
Earl Bostic•Harlem Nocturne / September Song•King Records (3)•1969','\
J.J. Jones And Band•Harlem Nocturne / Cool•Ebb•1957','\
no artist•Harlem Nocturne•Mega Records (4)•1972','\
René Bloch And His Big Latin Band•Gilette Cha Cha•HiFi Records•0','\
Randy Brooks And His Orchestra•Harlem Nocturne / A Night At The Deuces•Decca•1947','\
Earl Bostic And His Orchestra•Harlem Nocturne / I Hear A Rhapsody•King Records (3)•1956'),'\
\
Harlequin\
':('\
The Modern Jazz Quartet•The Comedy•Atlantic•1962','\
Chuz Alfred•Jazz- Young Blood•Savoy Records•1955','\
Lee Ritenour•Live From The Record Plant•Verve Video•1985','\
Scott Cossu•Islands•Windham Hill Records•1984','\
Weather Report•Heavy Weather•Columbia•1977','\
Toshiko Akiyoshi Jazz Orchestra•Desert Lady / Fantasy•Columbia•1994','\
Paul McCandless•Heresay•Windham Hill Records•1988','\
Paul McCandless•Heresay•Windham Hill Records•1988','\
Weather Report•Heavy Weather•Columbia•1977'),'\
\
Haunted Ballroom\
':('\
Victor Feldman•The Artful Dodger•Concord Jazz•1977','\
Judy Roberts•Nights In Brazil•Inner City Records•1981','\
Ken Mackintosh•His Saxophone And His Orchestra•no label•0'),'\
\
Have You Met Miss Jones ?\
':('\
Stan Getz Quintet•Have You Met Miss Jones / Erudion•Mercury•1953','\
Jack Montrose•Arranged/Played/Composed By Jack Montrose With Bob Gordon•Atlantic•1955','\
Ted Heath And His Music•The Faithful Hussar•London Records•0','\
Stan Getz•The Artistry Of Stan Getz•Clef Records•1953','\
Lucky Thompson•Lucky In Paris•Panorama (4)•0','\
Tal Farlow•Fuerst Set•Xanadu Records•1975','\
Bing Crosby•Bing Sings Whilst Bregman Swings•Verve Records•1956','\
Benny Goodman And His Orchestra•Swing Into Spring•Columbia•1958','\
Art Farmer Quintet•You Make Me Smile•Soul Note•1985','\
The Chet Baker Quintet•Smokin\' With The Chet Baker Quintet•Prestige•1966','\
Linc Chamberland•Yet To Come•Muse Records•1983','\
Frank Sinatra•Sinatra Swings Volume 1•Reprise Records•1961'),'\
\
Havona\
':('\
Weather Report•Heavy Weather•Columbia•1977','\
Weather Report•Heavy Weather•Columbia•1977','\
Jaco Pastorius•Modern American Music...Period! The Criteria Sessions•Omnivore Recordings•2014'),'\
\
He Was Too Good To Me\
':('\
Chris Connor•Chris Connor•Atlantic•1956','\
Joe Newman•Hangin\' Out•Concord Records•1984','\
Peter Herbolzheimer Rhythm Combination & Brass•Smile•Koala Records•1989','\
Monica Zetterlund•It Only Happens Every Time•EMI•1978','\
Ann Burton•Blue Burton•Artone•1967','\
Nina Simone•At The Village Gate•Colpix Records•1962','\
Anamari•Anamari•Atlantic•1964','\
Chris Connor•Chris Connor•Atlantic•1956','\
Grażyna Auguścik•Pastels•GMA Records•1997','\
Renee Geyer•Difficult Woman•Larrikin•1994'),'\
\
Head and Shoulders\
':('\
Cedar Walton Trio•Cedar!•Prestige•1967','\
Cedar Walton•Plays Cedar Walton - The Prestige Collection•Original Jazz Classics•1988','\
Frank Wagner (2)•Jazz Dancing•Gateway Records•1977','\
Various•Turn Back The Hands Of Time•RCA Victor•1973'),'\
\
Heat Wave\
':('\
The Crusaders•On Broadway / Heat Wave•World Pacific Records•1964','\
Marilyn Monroe•Heat Wave•Maybellene•1987','\
Ray Anthony•Juke Box Special / Heat Wave•Capitol Records•1955','\
Carl Kress•Heat Wave / Chicken A-La-Swing•Brunswick•1937','\
Humphrey Lyttelton And His Band•Jazz With Lyttelton (No. 2)•Parlophone•0','\
Marilyn Monroe•When I Fall In Love•Zuma (2)•1987','\
Art Farmer And His Orchestra•The Aztec Suite•United Artists Records•1959','\
Bing Crosby•Bing Sings Whilst Bregman Swings•Verve Records•0','\
no artist•Jazz•Clef Records•1953','\
Marilyn Monroe•There\'s No Business Like Show Business•RCA Victor•1954','\
Ahmad Jamal•Heat Wave•Cadet•1966','\
Keiichi Oku•The Good Bad Girl•JVC•1981','\
Albert Mangelsdorff•Mainhattan Modern Lost Jazz Files•Sonorama•2015','\
Tommy Flanagan Trio•Norman Granz\' Jazz In Montreux Presents Tommy Flanagan Trio \'77•Eagle Vision•2005','\
Satoko Fujii Ma-do•Heat Wave•Libra Records (5)•2008','\
Louis Bellson•Drumorama!•Verve Records•1957','\
Shirley Scott•Soul Duo•Impulse!•1967'),'\
\
Heaven\
':('\
Workshy•Heaven Sent•Canyon International•1993','\
The Pasadena Roof Orchestra•Pennies From Heaven / Back In Your Own Backyard•CBS•1978','\
Ben Webster And His Orchestra•Pennies From Heaven / Tenderly•Norgran Records•1954','\
Chapter And The Verse•All This And Heaven Too•Rham!•1988','\
The Big Three (3)•The Big Three•Hi-Life Records (2)•0','\
Heinz Schönberger Quintett•Pennies From Heaven - Ohio Blues•Brunswick•1955','\
Louis Prima•Buona Sera / Pennies From Heaven•Capitol Records•0','\
Michael Boothman•Heaven•Tabu Records•1977','\
Jimmy Scott•Heaven•Warner Bros. Records•1996','\
James Moody With Strings•Pennies From Heaven / Cherokee•Prestige•1952','\
The Alice Hall Trio•Pennies From Heaven / Caravan•Capitol Records•1949','\
Nas•Heaven (Blackbeard Reworks)•Blackbeard•2003','\
Jimmie Lunceford And His Orchestra•My Blue Heaven / Stomp It Off•Decca•1936','\
Ingrid Chavez•Heaven Must Be Near•Paisley Park•1991','\
Various•The Money Or The Gun - Stairways To Heaven•Phonogram•1992','\
Louis X•A White Man’s Heaven Is A Black Man’s Hell•A Muslim Sings•1960','\
Don Byas All Stars•Pennies From Heaven / Jamboree-Jump•Jamboree Records (2)•1945','\
Jackie & Roy•Winds Of Heaven / Lady Madonna•Capitol Records•1968','\
Seymour And His Heartbeat Trumpet• My Blue Heaven / Harbor Lights •Argo (6)•1959','\
Gus Arnheim And His Orchestra•Sleepy Valley / This Is Heaven•Victor•1929'),'\
\
Hello\
':('\
Larry Carlton•Hello Tomorrow•MCA Records•1987','\
The Ferko String Band•Golden Slippers•Palda•1947','\
Claudine Longet•Hello Hello / Wanderlove•A&M Records•1967','\
Toshiyuki Honda Radio Club•Something Coming On•Who Ring•1988','\
Claudine Longet•Hello Hello / Here There And Everywhere•A&M Records•0','\
Sammy Davis Jr.•Hello Detroit•Motown•1984','\
The Art Ensemble Of Chicago•Go Home•Galloway Records•1970','\
Eddie Cantor•If I Give Up The Saxophone (Will You Come Back To Me?) / Hello Sunshine Hello•Victor•1929','\
Claudine Longet•Meditation•A&M Records•1968','\
Lawrence Welk And His Orchestra•Southtown U.S.A.•Ranwood•1970','\
Louis Armstrong•Hello Dolly / Moon River•MCA Records•1980','\
Pete Fountain•Hello Dolly / Tippin\' In•Coral•0','\
The Mound City Blue Blowers•One Hour / Hello Lola•Victor•1930','\
Jimmy McGriff•Close Your Eyes•Sue Records Inc.•1964','\
Art Blakey•Blakey•EmArcy•0','\
Lloyd Price And His Orchestra•Hello Bill•ABC-Paramount•0','\
Miss 600•Hello•Membran•2013','\
Norman Brooks•Hello Sunshine / You\'re My Baby•Zodiac Records (7)•1953'),'\
\
Hello You Lovers\
':('\
Ray Conniff•Broadway In Rhythm•Philips•1961','\
Mantovani And His Orchestra•Hello Young Lovers•London Records•0','\
Keely Smith•Swing You Lovers•Dot Records•1960','\
Joe Diorio•Bonita•Zdenek Records•1980','\
Count Basie Orchestra•Broadway - Basie\'s Way•ABC Records•1972','\
Ray Conniff•Broadway In Rhythm•Philips•0','\
Ray Conniff•Broadway In Rhythm•Philips•0','\
Wilbur Harden•The King And I•Savoy Records•1958','\
Rosemary Clooney•With Love•Concord Jazz•1981','\
Toots Thielemans•Only Trust Your Heart•Concord Jazz•1988','\
Frank Sinatra•It Might As Well Be Swing•Reprise Records•1964'),'\
\
Henninger Flats\
':('\
Gary Burton Quartet•Green Apple•Moon Records (4)•1989'),'\
\
Here\'s That Rainy Day\
':('\
Kazumi Watanabe•Infinite•Express•1971','\
Art Farmer•Homecoming•Mainstream Records•1971','\
Art Pepper•First Live In Japan•Polydor•1990','\
Dee Dee Bridgewater•Live In Paris•Affinity•1987','\
Eric Alexander Quartet•Recado Bossa Nova•Venus Records (5)•2014','\
The Boys From Rochester•The Boys From Rochester•Feels So Good Records•1989','\
Joakim Milder•Consensus•Opus 3 Records•1992','\
Datevik Hovanesian•Day Dream•Мелодия•1986','\
Jay Arrigo & Friends•Sounds: Like Fun•AVI Records•1984','\
Yuko Asano•Fragrance Yuko','A•RCA•1985','\
Jon Hendricks•Cloudburst•Enja Records•1982','\
Stan Getz•Jazz Gala  \'80•Kingdom Jazz•1982','\
David Spinozza•Here\'s That Rainy Day•CBS/Sony•1983','\
Severi Pyysalo•Autumn Leaves - Severi Comes•Selecta (2)•1984','\
Johnny Hammond•Soul Flowers•Prestige•1968'),'\
\
Here\'s That Sunny Day\
':('\
Lionel Hampton•The Complete Lionel Hampton Quartets And Quintets With Oscar Peterson On Verve•Verve Records•1999','\
Louis Armstrong•The Definitive Collection•Hip-O Records•2006','\
Judy Garland•The Judy Garland Show: The Show That Got Away•Hip-O Records•2002','\
Frank Sinatra•The Sinatra Touch•Capitol Records•1968','\
Benny Goodman•On The Air (1937-1938)•Columbia Jazz Masterpieces•1993','\
Lester Young•Lester Young•Nocturne•2003','\
Frank Sinatra•The Works•Longines Symphonette Society•1973','\
Frank Sinatra•The Capitol Years•Capitol Records•1990','\
Teddy Wilson Trio•The Complete Verve Recordings Of The Teddy Wilson Trio•Mosaic Records (2)•1997','\
Frank Sinatra•The Platinum Collection•EMI•2004','\
Mildred Bailey•It Had To Be You•History•0'),'\
\
Herzog\
':('\
Bobby Hutcherson•Total Eclipse•Blue Note•1968','\
Hutcherson-Land Quintet•Blow Up•Jazz Music Yesterday•1990','\
Hutch Demouilpied•Otherness•Entropy Records (2)•2011','\
Linus (39)•Onland•Not On Label•2014','\
Various•Melodien Für Millionen Folge 2•Ariola•1985'),'\
\
Hey There\
':('\
The Jonah Jones Quartet•Just In Time•Capitol Records•1958','\
Jack Pleis And His Orchestra•Hey There / Lies•Decca•1955','\
Maynard Ferguson & His Orchestra•Let\'s Fall In Love•Roulette•1959','\
Rosemary Clooney•Hey There / This Ole House•Columbia•1954','\
Sammy Davis Jr.•Hey There / My Funny Valentine •Brunswick•1955','\
Buddy Greco•Around The World•Epic•1961','\
Johnnie Ray•Hey There / Hernanado\'s Hideaway•Columbia•1954','\
Rosemary Clooney•Hey There / Wake Me•Coronet (2)•1956','\
Rosemary Clooney•Hey There / Come On A My House•Columbia•0','\
The Johnston Brothers•Hernando\'s Hideaway•Decca•1955','\
Jon Eardley•Hey There Jon Eardley•Prestige•1955','\
The 25 Pianos Of Tommy Garrett•25 Pianos Play Evergreens of Broadway•Premier Series•1962','\
Mantovani•And Music By...•Decca•1958','\
Toshiko Akiyoshi•Toshiko Akiyoshi Trio•Eastworld•1983','\
Jon Eardley•From Hollywood To New York•Original Jazz Classics•1990','\
Sir Charles Thompson Trio•Sir Charles Thompson Trio•Vanguard Recording Society Inc.•1955','\
Rosemary Clooney•Rosemary Clooney•Columbia•0'),'\
\
Hi Beck\
':('\
Lee Konitz Sextet•Ezz-Thetic / Hi Beck•Prestige•1951','\
Lee Konitz•At Storyville•Storyville (3)•1954','\
Lee Konitz•At Storyville•Black Lion Records•1988','\
Lee Konitz•Sound Of Surprise•BMG France•1999','\
"Jojo" Takayanagi Second Concept•Cool Jojo•Three Blind Mice•1980','\
Lee Konitz•Wild As Springtime•G.F.M. Records•1984','\
Lee Konitz•Ezz-thetic•New Jazz•1964','\
Lee Konitz•Medium Rare•Label Bleu•1986','\
Boulou Ferré•Trinity•SteepleChase•1983','\
Michel Doneda•Général Gramofon•Nato•1988','\
Lee Konitz•Jazz At Storyville•Storyville (3)•1956','\
Lee Konitz•Ezz-thetic!•Prestige•1970'),'\
\
Hi Fly\
':('\
Eric Dolphy•In Europe Vol. 1•Prestige•1964','\
Art Blakey & The Jazz Messengers•At The Jazz Corner Of The World Vol. 2•Blue Note•1960','\
Horace Parlan Trio•Pannonica•Enja Records•1984','\
Karin Krog•Hi-Fly•Compendium Records•1976'),'\
\
Hideaway\
':('\
Tex Beneke And His Orchestra•Mr. Peepers / Danny\'s Hideaway•Coral•1953','\
Georgie Fame•Hideaway•Epic•1968','\
Unknown Artist•Ideas•Hoctor Records•0','\
Archie Bleyer•The Naughty Lady Of Shady Lane / Hernando\'s Hideaway•Cadence (2)•0','\
Archie Bleyer•Hernando\'s Hideaway•Cadence (2)•1954','\
Johnnie Ray•Hernando\'s Hideaway / Going-Going-Gone•Philips•0','\
Johnnie Ray•Hey There / Hernanado\'s Hideaway•Columbia•1954','\
Victor Silvester And His Ballroom Orchestra•Hernando\'s Hideaway•Columbia•1955','\
Barefoot (2)•It\'s Like That / Hideaway•OneTwo Records•2005','\
Jimmy Dorsey And His Orchestra•Heavenly Hideaway / An Overture To Love•Decca•1942','\
David Sanborn•Live At Montreux 1984  •Eagle Eye Media•2009','\
The Johnston Brothers•Hernando\'s Hideaway•Decca•1955','\
Pee Wee Hunt•Classics Ala Dixie•Capitol Records•1960','\
The Johnston Brothers•Yes Sir That\'s My Baby / Hernandos Hideaway•Decca•0','\
Ray Martin And His Concert Orchestra•More Martin Magic•Columbia•1956','\
Ray Martin And His Concert Orchestra•Hernando\'s Hideaway / The Bavarian Wedding March•Columbia•1955'),'\
\
Hi-Fly\
':('\
Eric Dolphy•In Europe Vol. 1•Prestige•1964','\
Art Blakey & The Jazz Messengers•At The Jazz Corner Of The World Vol. 2•Blue Note•1960','\
Horace Parlan Trio•Pannonica•Enja Records•1984','\
Karin Krog•Hi-Fly•Compendium Records•1976'),'\
\
Ho-Ba-La-La\
':('\
Ithamara Koorax•Bim Bom - The Complete João Gilberto Songbook•Motéma•2009','\
Martin Denny•Latin Village•Liberty•1964','\
João Gilberto•The Warm World Of João Gilberto•Atlantic•1963','\
João Gilberto•Vol. II•Odeon•1966','\
The Andre Tanker Five•Afro Blossom West•Atman•1969','\
René Touzet And His Orchestra•Bossa Nova - Brazil To Hollywood•GNP Crescendo•1963','\
Charlie Byrd Trio•Brazilian Byrd•Riverside Records•1962','\
Norma Bengell•Ooooooh! Norma•Odeon•1959','\
João Gilberto•The Warm World Of João Gilberto•WaxTime•2013'),'\
\
Hocus Pocus\
':('\
Steve Lacy•Hocus-Pocus•Les Disques Du Crépuscule•1986','\
Lee Morgan•The Sidewinder•Blue Note•1964','\
Lee Morgan•Memorial Album•Blue Note•1974'),'\
\
Hold On I\'m Coming\
':('\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014'),'\
\
Hold Out Your Hand\
':('\
Dave Grusin•Rag Bag•ARISTA GRP•1981','\
Steve Kuhn•Steve Kuhn•Buddah Records•1971','\
Dave Grusin•Mountain Dance•JVC•1980','\
Karin Krog•We Could Be Flying•Polydor•1975','\
Sheila Jordan•Sheila•SteepleChase•1978','\
Si Zentner And His Orchestra•My Cup Of Tea•RCA Victor•1965','\
Mose Allison•Young Man Mose•Prestige•1958','\
Steve Kuhn•The Early 70\'s•Columbia Music Entertainment•2007','\
Charlie Kunz•Old Time Music Hall Songs No. 1•Decca•1958','\
Various•We Can Work It Out (Covers & Cookies Of Lennon McCartney & The Beatles)•Harmless•2005','\
Various•Mojo Club Presents Dancefloor Jazz Volume Four (Light My Fire)•Motor Music•1995','\
Kim Cordell•I Sing In A Pub•Roulette•1965'),'\
\
Honeysuckle Rose\
':('\
The Dorsey Brothers Orchestra•Honeysuckle Rose•Decca•1934','\
The Johnny Dankworth Seven•Honeysuckle Rose•Parlophone•1953','\
Various•A Jam Session At Victor•Victor•1937','\
Django Reinhardt•Honeysuckle Rose/ Souvenirs•Decca•1938','\
Tommy Dorsey•Honeysuckle Rose / Blues•no label•1937','\
Various•A Jam Session At Victor•Victor•1937','\
Sidney Bechet And His Orchestra•High Society / Honeysuckle Rose•Blue Star•0','\
Benny Goodman And His Orchestra•Honeysuckle Rose / Spring Song•Columbia•1939'),'\
\
Horacescope\
':('\
Various•100 Hits Jazz•100 Hits•2013'),'\
\
Horizon\
':('\
Harry Tavitian•Horizons•Leo Records•1985','\
Adam Lane Trio•Absolute Horizon•NoBusiness Records•2013','\
Sidney Bechet And His Blue Note Jazz Men•Blue Horizon / Muskrat Ramble•Blue Note•0','\
Mabumi Yamaguchi Quartet•After The Rain•Union Records (3)•1976','\
Eric Gale•Blue Horizon•Elektra Musician•1982','\
Solidarity Unit Inc.•Red Black & Green•Not On Label•1972','\
Espen Eriksen Trio•Perfectly Unhappy•Rune Grammofon•2018','\
McCoy Tyner•Horizon•Milestone (4)•1980'),'\
\
Hot House\
':('\
Wardell Gray•Hot House•Modern Records (2)•1949','\
The Quintet•Jazz At Massey Hall Volume Three•Debut Records•1953','\
Dizzy Gillespie•Jazz At Massey Hall Volume 3•Debut Records (3)•1958','\
Charlie Parker•Charlie Parker Volume III•Everest Records Archive Of Folk & Jazz Music•1972','\
Ella Fitzgerald•The Hot Canary / Come On-A My House•Brunswick•0','\
The Original Memphis Five•Oh! Sister Ain\'t That Hot / House Of David Blues•Banner•1924','\
Erroll Garner•Starring The Magic Artistry Of Erroll Garner / Also Starring George Wallington•Premier (7)•1966','\
Stan Getz•Groovin\' With Getz•Custom Records (2)•1966','\
Dizzy Gillespie•Jazz Masters•Musidisc•0','\
Sonny Criss•Sonny Criss - Gerald Wiggins - Erroll Garner - Stan Getz•Crown Records (2)•1963','\
Wally Rose•Honky-Tonkin\'•Columbia•1955','\
no artist•Lonesome•Metronome•0','\
Bud Powell•Hot House•Fontana•1966','\
Out Of The Blue (3)•Inside Track•Blue Note•1986','\
Miles Davis All Stars•Miles Davis All Stars And Gil Evans•Beppo Records•0','\
Charlie Parker•An Evening At Home With The Bird•Savoy Records•1961','\
Out Of The Blue (3)•Inside Track•Blue Note•1986','\
John Patton•Blue John•Blue Note•1986'),'\
\
Hotel Hello\
':('\
Gary Burton•Hotel Hello•ECM Records•1975','\
T-Square•うち水にRainbow•CBS/Sony•1983','\
Bullfrog•Bullfrog•Ropeadope Records•2001Janis Siegel•Friday Night Special•Telarc Jazz•2003','\
Michael Feinstein•The Sinatra Project•Concord Records•2008','\
Josephine Baker•Josephine Baker•EMI•1990','\
Various•Romantic Instrumental•Bomba Music•2001','\
The Cat Empire•Live On Earth•EMI•2009','\
The Cat Empire•Live On Earth•EMI•2009','\
Various•On The Rocks Part One•Capitol Records•1997','\
Lester Lanin And His Orchestra•Dance To The Music Of Lester Lanin•Philips•0','\
Quintet Eddy Young•In The Cocktail-Bar•Artone•1965','\
Nancy Wilson•The Essence Of Nancy Wilson: Four Decades Of Music•Capitol Records•2002','\
Various•Easy Listening Swing•no label•1985','\
Various•The Ultimate Grammy Box•Legacy•1999'),'\
\
Hotel Overture\
':('\
Gary Burton•Hotel Hello•ECM Records•1975','\
Yoshitaka Minami•Silk Screen•CBS/Sony•1981','\
Carla Bley•Escalator Over The Hill•JCOA Records•0','\
Maurice Jarre•Doctor Zhivago•Turner Entertainment Co.•1995'),'\
\
Hotel Vamp\
':('\
Gary Burton•Hotel Hello•ECM Records•1975','\
The Tremendous Talents Orchestra•Hotel Paradies•Dino Music•1989'),'\
\
House of Jade\
':('\
Chet Baker Trio•This Is Always•SteepleChase•1982','\
NY5•Music For Violin & Jazz Quartet•Jam (15)•1981','\
Wayne Shorter•Juju•Blue Note•1964','\
Wayne Shorter•Juju•Blue Note•1964','\
Laurent De Wilde•Odd and Blue•IDA Records•1989','\
Chet Baker•Little Girl Blue•Philology•1988','\
Chet Baker•Live In Chateauvallon 1978•no label•1989','\
Harold Mabern•Joy Spring•Sackville Recordings•1985','\
Bill Jaffee & His Islanders•Hawaiian Paradise•Fidelio•1959','\
Lionel Hampton•Tempo And Swing (The All-Star Groups Volume 3 – 1939-40)•RCA•1992'),'\
\
How Do You Keep The Music Playing?\
':('\
Shirley Bassey•How Do You Keep The Music Playing•ZYX Records•1991','\
Gary Bartz•Shadows•Timeless Records (3)•1992','\
Houston Person•Always On My Mind•Muse Records•1985','\
Steve Smith (5)•Steve Smith And Buddy\'s Buddies Featuring Buddy Rich Alumni•Tone Center•1999','\
Pieces Of A Dream•In Flight•Manhattan Records•1993','\
Arturo Sandoval•Dream Come True•GRP•1993','\
Various•Magical Duos•GRP•1993','\
Robin Meloy Goldsby•Somewhere In Time•Evergreen Music (4)•2005','\
Michel Legrand•Live At Fat Tuesday\'s•Verve Records•1990','\
Hansi Lang•This Is The Slow Club•Serious Entertainment (2)•2005','\
Milt Jackson•Reverence And Compassion•Qwest Records•1993','\
Milt Jackson•Reverence And Compassion•Qwest Records•1993','\
Pedro Paulo Castro-Neves•Pedro Paulo Castro Neves & Michel Legrand•Sigla•1985','\
George Benson•Big Boss Band•Warner Bros. Records•1990','\
Walter Boeykens•The Other Side•Travel Sound•1994','\
Simone Kopmajer•Romance•Venus Records (5)•2004'),'\
\
How High the Moon\
':('\
Jazz At The Philharmonic•How High The Moon•Mercury•1947','\
Howard McGhee Sextet•How High The Moon•Vogue Productions•1948','\
The Dave Brubeck Quartet•How High The Moon•Fantasy•0','\
Ella Fitzgerald•How High The Moon•Verve Records•1960','\
Calvin Jackson•How High The Moon•Reprise Records•0','\
Stan Kenton And His Orchestra•How High The Moon / Interlude•Capitol Records•1948','\
Benny Goodman Septet•How High The Moon / Bedlam•Capitol Records•0','\
Ray Anthony•Jam Session At The Tower Part 3•Capitol Records•1956','\
Jazz At The Philharmonic•Jazz At The Philharmonic (Volume Number 1)•Asch Records•1945','\
Jimmy Smith•How High The Moon•Blue Note•1957','\
Lionel Hampton And His Orchestra•1 - Jazz•Philips•1955','\
Oscar Peterson•How High The Moon / Nameless•Mercury•1951','\
Les McCann•The Truth•Pacific Jazz•1969','\
Dodo Marmarosa Trio•Mellow Mood / How High The Moon•Atomic Records (12)•1945','\
The Dave Brubeck Trio•Squeeze Me / How High The Moon•Fantasy•1951','\
Don Byas Quintet•How High The Moon / Ko Ko•Savoy Records•1945','\
Ella Fitzgerald•How High The Moon / Smooth Sailing•Brunswick•0','\
Stan Getz•Groovin\' With Getz•Custom Records (2)•1966','\
Randy Brooks And His Orchestra•Thunder Rock•Decca•1955'),'\
\
How Insensitive\
':('\
Doris Day•Meditation / How Insensitive (Insensataez)•Columbia•1964','\
The Lee Gagnon Quartet•La Jazztek•Capitol Records•1968','\
Dexter Gordon•Sophisticated Giant•Columbia•1977','\
Pat Martino•The Visit!•Cobblestone•1972','\
Kellye Gray•Standards In Gray•Justice Records (2)•1990','\
Oscar Peterson•Jazz Brasileiro•Trolley Car Records•0','\
Frank Sinatra•Sinatra And Jobim•Reprise Records•1967'),'\
\
How Little We Know\
':('\
Frank Sinatra•(How Little It Matters) How Little We Know / Five Hundred Guys•Capitol Records•1956','\
Hoagy Carmichael And His Orchestra•How Little We Know / Hong Kong Blues•ARA (2)•1945','\
Chris Connor•Witchcraft•Atlantic•0','\
Robin Kenyatta•Until•Vortex Records (2)•1968','\
Frank Sinatra•This Is Sinatra - Volume Two (Part 4)•Capitol Records•1958','\
Buddy Clark (3)•How Little We Know / I Understand / Lonesome Road•V Disc•1945','\
Frank Sinatra•Hey! Jealous Lover•Capitol Records•0','\
Polly Bergen•Today\'s Hits•RCA Camden•1956','\
The Johnny Mann Singers•This Guy\'s In Love With You. The Look Of Love•Liberty•1968','\
The Phil Woods Quintet•Ballads & Blues•Venus Records (5)•2009','\
Dean Martin•Relaxin\'•Tower•1966','\
Various•The Biggest Hits Of \'56 Vol. 2•RCA Camden•0','\
The Phil Woods Quintet•Ballads & Blues•Venus Records (5)•2009','\
Carmen McRae•Something To Swing About•Kapp Records•1960','\
Kathy Barr•Do It Again•Ava•1964','\
Frank Strozier•Long Night•Jazzland•1961'),'\
\
How Long Has This Been Going On?\
':('\
Gloria Estefan•How Long Has This Been Going On•Sony Music Latin•2013','\
Felicia Sanders•How Long Has This Been Going On•Columbia•1954','\
Marian McPartland•Marian McPartland At The Hickory House Part 2•Capitol Records•0','\
Svein Olav Herstad Trio•The Ballad Book•Curling Legs•2017','\
Tommy Flanagan•The Cats•New Jazz•1959','\
The Jay And Kai Quintet•Dec.3','1954•Metronome•1955','\
Karin Krog•Jazz Jamboree 75 Vol. 2•Polskie Nagrania Muza•0','\
Ben Webster•Live At The Haarlemse Jazzclub•Cat Records (7)•1972','\
Pepper Adams•Live•no label•1995','\
Stan Getz•Blue Skies•Concord Jazz•1995','\
Manny Albam•The Jazz Greats Of Our Time - Vol. 2•Coral•1958','\
Kellye Gray•Standards In Gray•Justice Records (2)•1990','\
Frank Rosolino Quintet•Frank Rosolino Quintet•Mode Records•1957','\
Ben Webster•Ben And "Sweets"•Columbia•1987','\
Ben Webster•Wanted To Do One Together•Columbia•1962','\
Ben Webster•Live In Denmark•Vantage Records (2)•1990'),'\
\
How My Heart Sings\
':('\
Larry Coryell•Together•Concord Jazz•1985','\
Bill Evans•Montreux II•CTI Records•1970','\
Mitchel Forman•Now And Then- A Tribute To Bill Evans•BMG•1993','\
The Bill Evans Trio•Camp Fortune 1974•Radio Canada International•1976','\
Klaus Treuheit Trio•Nardis•SFP (3)•1986','\
Jimmy Raney•Stolen Moments•SteepleChase•1979','\
Various•Current Cuts 1971•CTI Records•1971','\
Bill Evans•Time Remembered•Get Back•2007','\
The Bill Evans Trio•"Live"•Verve Records•1971','\
The Bill Evans Trio•How My Heart Sings•Riverside Records•1964','\
Bill Evans•Jazzhouse•Milestone (4)•1987','\
Bill Evans•Time To Remember - Live In Europe 1965-72•Natasha Imports•1992','\
Gene Bertoncini•Bridges•GJB Music•1977'),'\
\
How Sweet It Is\
':('\
Patrick Williams•How Sweet It Is! (Music From The Film Score)•RCA Victor•1968','\
Count Basie Orchestra•Warm Breeze•Pablo Today•1981','\
Merl Saunders•Keystone Encores Volume II•Fantasy•1988','\
Joyce Bond•How Sweet It Is (To Be Loved By You) / Nothing Can Stop Me Loving You•Orbitone Records•1988','\
Merl Saunders•Keystone Encores Volume II•Fantasy•1988','\
Jack Say Orchestra And Chorus•The Girl That I Marry (The Music Of Irving Berlin)•RCA Camden•1959','\
Mari Kvien Brunvoll•Mari Kvien Brunvoll•Jazzland Recordings•2012','\
Victor Young And His Singing Strings•Say It With Music (Irving Berlin Compostions)•Decca•0','\
Merl Saunders•Keystone Encores•Fantasy•1988','\
Coleman Hawkins•Classic Tenors•Stateside•1964','\
Térez Montcalm•Voodoo•Marquis•2005','\
Coleman Hawkins•Classic Tenors•Flying Dutchman•1972','\
The Lincolns (4)•Take One•Attic•1983','\
The Dave Brubeck Trio•Distinctive Rhythm Instrumentals•Fantasy•1956'),'\
\
Hullo Bolinas\
':('\
Enzo Pietropaoli•Orange Park•Gala Records (4)•1989','\
Gary Burton / Chick Corea•In Concert Zürich October 28 1979•ECM Records•1980','\
Gary Burton•Quartet Live•Concord Jazz•2009','\
Niño Josele•Paz•Calle 54 Records•2006','\
Bill Evans•Bill Evans Live In Tokyo•CBS/Sony•1973','\
Chano Domínguez Trio•Con Alma•Venus Records (5)•2005','\
Jean-Yves Thibaudet•Conversations With Bill Evans•Decca•1997','\
Gary Burton•Alone At Last•Atlantic•1971'),'\
\
Hummin\'\
':('\
The Cannonball Adderley Quintet•Hummin\' / Country Preacher•Capitol Records•1969','\
Nat Adderley•Hummin\'•Little David Records•1976','\
The Hassles•You\'ve Got Me Hummin\'•United Artists Records•1967','\
Brother James & Sugar Mama•You Got Me Hummin / It Ain\'t Easy•Roadshow•1972','\
Quincy Jones•Gula Matari•A&M Records•1970','\
J.J. Johnson•The Yokohama Concert•Pablo Live•1978','\
Nat Adderley•Hummin\'•Little David Records•1976'),'\
\
Humpty Dumpty\
':('\
Jimmy Nicol & The Shubdubs•Humpty Dumpty•Pye Records•1964','\
Esperanza Spalding•Junjo•Ayva Musica•2006','\
Akio Sasajima•Humpty Dumpty•Enja Records•1993','\
MVP (5)•Truth In Shredding•Tone Center•1990','\
Chick Corea•Super Trio (Live At The One World Theatre April 3rd 2005)•Mad Hatter Productions•2006','\
Nobuo Hara And His Sharps & Flats•Humpty Dumpty•Lob•1978','\
Chick Corea Akoustic Band•Live•Stretch Records•2018','\
Marc Moulin•Placebo Years 1971-1974•Blue Note•2006','\
The Ornette Coleman Quartet•This Is Our Music•Atlantic•1961','\
Kenny Wheeler•Mirrors•Edition Records•2013'),'\
\
I Believe In You\
':('\
Sarah Vaughan•I Believe In You•Roulette•1963','\
Louis Prima•Illya Darling / I Believe In You•United Artists Records•1967','\
no artist•Viennese Nightingale•RCA Victor•1961','\
Talk Talk•I Believe In You•Parlophone•1988','\
Charles Veal Jr.•If You Ever Need Somebody / I Believe In You•Capitol Records•1980','\
The Blues Groove•Makin\' It / I Believe In You•Verve Records•1966','\
Erroll Garner•I Only Have Eyes For You•Savoy Records•1950','\
Gerry Mulligan Quartet•The Gerry Mulligan Quartet•Verve Records•1962','\
Bing Crosby•I Can\'t Begin To Tell You / I Can\'t Believe That You\'re In Love With Me•Decca•1945','\
Louis Armstrong And His Orchestra•You Don\'t Learn That In School / I Believe•RCA Victor•1947','\
The Red Norvo Trio•I\'ve Got You Under My Skin / I Can\'t Believe That You\'re In Love With Me•Jazz Selection•1953','\
Talk Talk•I Don\'t Believe In You•Parlophone•1986','\
Frankie Laine•West End Blues•Mercury•0','\
The Caravan Orchestra•Jerome Kern Dance Album•Caravan (4)•1949','\
Coleman Hawkins All Star Band•At Newport•Verve Records•1958','\
Peggy Lee•I Believe In You•Capitol Records•1963','\
Shelly Manne•Empathy•Verve Records•1962'),'\
\
I Can\'t Get Started\
':('\
Buddy DeFranco Quintet•Cooking The Blues•Verve Records•1958','\
Charles Mingus•My Favorite Quintet•Fantasy•1964','\
Joe Pass•Northsea Nights•Pablo Live•1980','\
Lol Coxhill•Halim•Nato•1993','\
Cybill Shepherd•Mad About The Boy•Inner City Records•1980','\
Acker Bilk•Stranger On The Shore•Columbia•1961','\
Dinah Washington•Music For Late Hours•Mercury•1956','\
Various•Concord Jazz Guitar Collection - Volumes 1 And 2•Concord Jazz•1987','\
Kenny Ball And His Jazzmen•More Kenny Ball And His Midnight In Moscow Jazzmen•Kapp Records•1963','\
Satoru Oda & His Group•Tenor Sax In Love•Festival Records•1964'),'\
\
I Can\'t Help It\
':('\
Malene Mortensen•Can\'t Help It•Stunt Records•2015','\
Billie Holiday•Greatest Hits•Columbia•1995','\
Various•Mo\' Steppers•Motown•1994','\
Chris Minh Doky•A Jazz Life•EMI Music Denmark•2008','\
Elvis Presley•Walk A Mile In My Shoes - The Essential 70\'s Masters•RCA•1995','\
Elvis Presley•20 Original Albums•RCA•2012','\
Various•Les Triomphes Du Blues•Habana•2001'),'\
\
I Concentrate On You\
':('\
Cal Tjader Modern Mambo Orchestra•Fascinatin\' Rhythm / I Concentrate On You•Fantasy•0','\
Dinah Washington•Not Without You / I Concentrate On You•Mercury•1955','\
Billy Daniels•That Ol\' Black Magic•Mercury•1956','\
Billy Daniels•That Old Black Magic / I Concentrate On You•Oriole•1952','\
Russell Malone Quartet•Wholly Cats•Venus Records (5)•1998','\
Brad Mehldau Trio•Blues and Ballads•Nonesuch•2016','\
Frank Sinatra•Sinatra\'s Swingin\' Session Part 3•Capitol Records•1961','\
Frank Sinatra•Sinatra And Jobim•Reprise Records•1967','\
Dave Liebman Quartet•The Opal Heart•Enja Records•1979','\
Houston Person•The Big Horn•Muse Records•1979','\
The Frankie Capp Percussion Group•In A Tribute To Artie Shaw•Kimberly•0','\
Oscar Peterson•Oscar Peterson In Paris•Joker (2)•1977','\
Herb Ellis•Soft & Mellow•Concord Jazz•1979','\
Grant Green•Nigeria•Blue Note•1980','\
Oscar Peterson•Girl Talk•MPS Records•1968'),'\
\
I Could Write a Book\
':('\
The Mastersounds•Golden Earrings•Fantasy•1961','\
Les Brown And His Band Of Renown•I Could Write A Book / Easy To Love•Columbia•0','\
Miles Davis•When I Fall In Love•Prestige•1961','\
Alice Babs•Studio Jazz Mit Alice Babs •Electrola•1959','\
Buddy Greco•They Took John Away / I Could Write A Book•Epic•1961','\
Ella Fitzgerald•Ella Sings "Pal Joey"•no label•1958','\
no artist•Hi-Lo\'s New Sound•Philips•0','\
The Frankie Capp Percussion Group•In A Tribute To Artie Shaw•Kimberly•0','\
Sonny Rollins•On The Outside•Bluebird (3)•1990','\
Jimmy Raney Trio•Wistaria•Criss Cross jazz•1986'),'\
\
I Could Write A Book\
':('\
The Mastersounds•Golden Earrings•Fantasy•1961','\
Les Brown And His Band Of Renown•I Could Write A Book / Easy To Love•Columbia•0','\
Miles Davis•When I Fall In Love•Prestige•1961','\
Alice Babs•Studio Jazz Mit Alice Babs •Electrola•1959','\
Buddy Greco•They Took John Away / I Could Write A Book•Epic•1961','\
Ella Fitzgerald•Ella Sings "Pal Joey"•no label•1958','\
no artist•Hi-Lo\'s New Sound•Philips•0','\
The Frankie Capp Percussion Group•In A Tribute To Artie Shaw•Kimberly•0','\
Jimmy Raney Trio•Wistaria•Criss Cross jazz•1986','\
Sonny Rollins•On The Outside•Bluebird (3)•1990'),'\
\
I Cover the Waterfront\
':('\
Artie Shaw And His Orchestra•I Cover The Waterfront•Victor•0','\
Erroll Garner•I Cover The Waterfront•Savoy Records•1949','\
Mel Tormé•I Cover The Waterfront / Country Fair•Musicraft•1948','\
Eddie Heywood And His Orchestra•Begin The Beguine / I Cover The Waterfront•Commodore•1944','\
Lester Young Trio•I Cover The Waterfront•Clef Records•1953','\
Jimmy McGriff Trio•I Cover The Waterfront / Slow But Sure•Solid State Records (2)•1966','\
Martha Raye•Sweet Lorraine / I Cover The Waterfront•Apollo Records (2)•1948','\
The Ink Spots•Prisoner Of Love / I Cover The Waterfront•Decca•1946','\
Vic Schoen And His Orchestra•I Cover The Waterfront•Decca•0','\
Jimmy Smith•I Cover The Waterfront•Blue Note•1956','\
Zoot Sims•Poll Winners Jazz•Fontana•0','\
Billie Holiday And Her Orchestra•I Cover The Waterfront / Lover Come Back To Me•Commodore•1945','\
Guy Lafitte Et Son Orchestre•Sweet Topsy / I Got Rythm / I Cover The Waterfront / Mélodie Au Crépuscule•Ducretet Thomson•1954','\
Django Reinhardt Et Son Quintette•I Cover The Waterfront•Decca•0','\
Erroll Garner•Erroll Garner•Philips•0','\
Erroll Garner•The Greatest Erroll Garner•Savoy-Musidisc•0','\
Vic Dickenson Septet•Vic Dickenson Septet Vol.II•Vanguard•1953'),'\
\
I Cover The Waterfront\
':('\
Artie Shaw And His Orchestra•I Cover The Waterfront•Victor•0','\
Erroll Garner•I Cover The Waterfront•Savoy Records•1949','\
Mel Tormé•I Cover The Waterfront / Country Fair•Musicraft•1948','\
Eddie Heywood And His Orchestra•Begin The Beguine / I Cover The Waterfront•Commodore•1944','\
Lester Young Trio•I Cover The Waterfront•Clef Records•1953','\
Jimmy McGriff Trio•I Cover The Waterfront / Slow But Sure•Solid State Records (2)•1966','\
Martha Raye•Sweet Lorraine / I Cover The Waterfront•Apollo Records (2)•1948','\
The Ink Spots•Prisoner Of Love / I Cover The Waterfront•Decca•1946','\
Vic Schoen And His Orchestra•I Cover The Waterfront•Decca•0','\
Jimmy Smith•I Cover The Waterfront•Blue Note•1956','\
Zoot Sims•Poll Winners Jazz•Fontana•0','\
Guy Lafitte Et Son Orchestre•Sweet Topsy / I Got Rythm / I Cover The Waterfront / Mélodie Au Crépuscule•Ducretet Thomson•1954','\
Billie Holiday And Her Orchestra•I Cover The Waterfront / Lover Come Back To Me•Commodore•1945','\
Django Reinhardt Et Son Quintette•I Cover The Waterfront•Decca•0','\
Erroll Garner•Erroll Garner•Philips•0','\
Erroll Garner•The Greatest Erroll Garner•Savoy-Musidisc•0'),'\
\
I Didn\'t Know About You\
':('\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014'),'\
\
I Didn\'t Know What Time It Was\
':('\
Art Blakey & The Jazz Messengers•Ugetsu•Riverside Records•1963','\
Brad Mehldau•The Art Of The Trio Volume One•Warner Bros. Records•1997','\
Charlie Parker•The Essential Charlie Parker•no label•1961','\
Stéphane Grappelli•Live In Warsaw•no label•1996','\
Bud Shank•Pacific Jazz Presents Bud Shank And Laurindo Almeida•Pacific Jazz•1987','\
Various•Eastwood After Hours • Live At Carnegie Hall•Malpaso Records•1997','\
Various•Slow Dancing Through The Years•Sony Music Special Products•1994','\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014'),'\
\
I Fall In Love Too Easily\
':('\
Frank Sinatra•I Fall In Love Too Easily / I Begged Her•Columbia•1944','\
Grady Tate•Hooray•Skye Records•1969','\
The Miles Davis Quintet•Live In Berlin 1969•Gambit Records•2010','\
Buster Williams•Heartbeat•Muse Records•1979','\
Lars Gullin Quintet•Bugs•Metronome•1954','\
Mehldau & Rossy Trio•When I Fall In Love•Fresh Sound New Talent•1994','\
George Otsuka Trio•Page 2•Takt Jazz Series•1968','\
Philip Catherine•Oscar•Igloo•1990','\
Tete Montoliu•Face To Face•SteepleChase•1984','\
Magnus Broo Trio•Rules•Moserobie Music Production•2018','\
Ali Ryerson•Blue Flute•Red Baron•1992','\
Niels-Henning Ørsted Pedersen•Double Bass•SteepleChase•1976','\
Keith Jarrett•Standards Vol. 2•ECM Records•1985','\
Tony Bennett•Cloud 7•Columbia•1955','\
The Miles Davis Quintet•No Blues•Jazz Music Yesterday•1990','\
Miles Davis•Complete Live At Plugged Nickel 1965•Sony Records•1992','\
Marc Cohen•My Foolish Heart•Jazz City•1988','\
The Michael Wolff Trio•Jumpstart•Jimco Records•1995','\
Miles Davis•Miles And More - Live In Berlin Nov. 07 1969•Darkroom Entertainment•2004'),'\
\
I Get A Kick Out Of You\
':('\
Roger Williams (2)•I Get A Kick Out Of You•Kapp Records•1969','\
Frank Sinatra•I Get A Kick Out Of You / My Funny Valentine•Capitol Records•1955','\
The Pete Jolly Sextet•I Get A Kick Out Of You•RCA Victor•1955','\
Billy Daniels•I Get A Kick Out Of You / Too Marvelous For Words•Mercury•0','\
Gene Norman•In Concert•Gene Norman Presents•1955','\
Shorty Rogers•Shorty Rogers And The Lighthouse All Stars•Tampa Records•0','\
Various•8 Ways to Jazz - the music of Cole Porter•Riverside Records•1958','\
Morton Gould•Temptation•RCA•1958','\
Kenny Dorham•Live 1953-56-64•Royal Jazz•1990','\
Charlie Parker•Charlie Parker Plays Cole Porter•Verve Records•1957','\
Shirley Bassey•Let\'s Face The Music (No. 2)•Columbia•1965','\
Ella Fitzgerald•I Get A Kick Out Of You / Dream Dancing / I\'ve Got You Under My Skin•ZYX Records•1988'),'\
\
I Got It Bad\
':('\
Eric Alexander Quartet•Gentle Ballads II•Venus Records (5)•2007','\
Woody Herman And His Orchestra•That\'s Right / I Got It Bad•Capitol Records•1949','\
Various•Jazz Na Koncertnom Podiju Vol. 1•Jugoton•1977','\
Jimmy Coe And His Orchestra•Cole Tater / I Got It Bad And That Ain\'t Good•King Records (3)•1952','\
Duke Ellington And His Orchestra•Take The "A" Train•RCA Victor•0','\
Jan Ptaszyn Wróblewski•Mainstream•Polskie Nagrania Muza•1974','\
Nina Simone•I Got It Bad•Colpix Records•1962','\
Jimmy Dorsey And His Orchestra•The White Cliffs of Dover / I Got It Bad (And That Ain\'t Good)•Decca•1941','\
Benny Goodman And His Orchestra•Why Don\'t You Do Right? / I Got It Bad (And That Ain\'t Good)•Columbia•0','\
Elsie Bianchi Trio•I\'ll Take Romance•Swiss Record•1962','\
Harold Ashby•The Viking•Gemini Records (7)•1989','\
Earl Hines•It Don\'t Mean A Thing If It Ain\'t Got That Swing!•Black Lion Records•1974','\
Ella Fitzgerald And Her Famous Orchestra•Melinda The Mousie / I Got It Bad And That Ain\'t Good•Decca•1941','\
June Valli•The Torch•RCA Victor•0','\
Bill Evans•New Piano Conceptions•Riverside Records•0','\
Pete Jolly•Quartet•RCA Victor•1955','\
Les Brown And His Orchestra•Nothin\' / I Got It Bad And That Ain\'t Good•Okeh•1941','\
Earl Hines And His Orchestra•Earl And Billy•no label•1955','\
Sonny Criss•At The Crossroads with Sonny Criss•no label•1959','\
Helen Merrill•No Tears No Goodbyes•Owl Records (4)•1984','\
Earl Hines•It Don\'t Mean A Thing If It Ain\'t Got That Swing!•Black Lion Records•1974','\
Jackie Gleason•Music Martinis And Memories (Part 1)•Capitol Records•0','\
The Al Belletto Sextet•Sounds And Songs•Capitol Records•0','\
Bunny Berigan & His Orchestra•I Got It Bad / The White Cliffs Of Dover•Elite (3)•1941'),'\
\
I Got Rhythm\
':('\
Benny Goodman Sextet•Slipped Disc / I Got Rhythm•Parlophone•1946','\
Stéphane Grappelli And His Hot Four•Limehouse Blues / I Got Rhythm•Decca•1935','\
Count Basie•I Got Rhythm / Boone\'s Blues•Verve Records•1967','\
Roy Fox & His Band•You\'ve Got What Gets Me / I Got Rhythm•Decca•0','\
Metronome All Stars•Royal Flush / I Got Rhythm•Columbia•1942','\
Quintet Johnny Meyer•I Got Rhythm / Blue Skies•Philips•0','\
Benny Goodman•Benny Goodman Plays Gershwin•CBS•1983','\
Glenn Miller And His Orchestra•I Got Rhythm / Sleepy Time Gal•Columbia•0','\
Don Redman And His Orchestra•I Got Rhythm / Hot And Anxious•Brunswick•0','\
Oscar Peterson•I Got Rhythm / My Blue Heaven•no label•1953','\
Kansas City Six•Prez And Friends (A Complete Session)•Commodore•1980','\
Oscar Peterson•I Got Rhythm / My Blue Heaven•no label•1953','\
Felix Mendelssohn & His Hawaiian Serenaders•In The Mood / I Got Rhythm•Columbia•0'),'\
\
I Gotta Right To Sing The Blues\
':('\
Jack Teagarden And His Orchestra•I Gotta Right To Sing The Blues / Yankee Doodle•Brunswick•1939','\
Billie Holiday And Her Orchestra•I Gotta Right To Sing The Blues / Yesterdays•Commodore•1939','\
Louis Armstrong And His Orchestra•I Gotta Right To Sing The Blues / High Society•Bluebird (3)•0','\
Louis Armstrong And His Orchestra•I Gotta Right To Sing The Blues / There\'s A Cabin In The Pines•Victor•1945','\
Jack Teagarden•Big T\'s Jazz•Decca•1956','\
Billie Holiday•Fine And Mellow 1939 And 1944•Commodore•1979','\
Louis Prima•The Wildest Show At Tahoe Part 2•Capitol Records•1958','\
Fran Warren•I Gotta Right To Sing The Blues•RCA Victor•1951','\
Benny Goodman And His Orchestra•Texas Tea Party•Columbia•1955','\
Benny Goodman•Texas Tea Party•Columbia•0','\
Louis Armstrong And His Orchestra•I Gotta Right To Sing The Blues•no label•0','\
Julie London•About The Blues•Liberty•1957','\
Buddy Tate•Jive At Five•Mahogany (3)•0','\
Jimmy Giuffre•The Four Brothers Sound•Atlantic•1959'),'\
\
I Guess I\'ll Have To Change My Plan\
':('\
Bud Freeman•Midnight Session•DOT Records•1960'),'\
\
I Had The Craziest Dream\
':('\
Astrud Gilberto•Stay •Verve Records•1967','\
Harry James And His Orchestra•I Had The Craziest Dream / A Poem Set To Music•Columbia•1942','\
Della Reese•Della By Starlight•RCA•1960','\
Harry James And His Orchestra•Sweet Trumpet•Philips•0','\
Dizzy Reece•Blues In Trinity•Blue Note•1958','\
Billy Mitchell•The Colossus Of Detroit•Xanadu Records•1978','\
Harry James And His Orchestra•I\'ve Heard That Song Before•Columbia•0','\
Kenny Dorham•Quiet Kenny•New Jazz•1959','\
Jimmy Smith•Stranger In Paradise•Bravo! Records•1965','\
Chuck Mangione Quintet•Recuerdo•Jazzland•1962'),'\
\
I Hadn\'t Anyone Till You\
':('\
The Carla Bley Big Band•Appearing Nightly•WATT Works•2008','\
Ella Fitzgerald•Lo Mejor De Ella Fitzgerald. Vol. II•Coral•1970','\
Mel Tormé•The Best Of The Capitol Years•Capitol Records•1992','\
Flip Phillips•Swing Is The Thing•Verve Records•2000','\
Patrick Williams•Sinatraland•EMI-Capitol Entertainment Properties•1998','\
Ella Fitzgerald•Ella Fitzgerald•Nocturne•2003'),'\
\
I Have The Feeling I\'ve Been Here Before\
':('\
Lillian Roth•Lillian Roth Sings•Tops Records•1957','\
Various•We Remember Them Well•no label•1986','\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014'),'\
\
I Hear a Rhapsody\
':('\
John Coltrane•Lush Life•Metronome•1961','\
101 Strings•Rhapsody•Somerset•1961','\
Earl Bostic And His Orchestra•Harlem Nocturne / I Hear A Rhapsody•King Records (3)•1956','\
Ray Anthony & His Orchestra•I Hear A Rhapsody / For Dancers Only •Capitol Records•0','\
The George Shearing Quintet•I Hear A Rhapsody / Body And Soul•MGM Records•1953','\
Jackie McLean•Action•Blue Note•1967','\
Earl Bostic•Earl Bostic (Vol. 18)•King Records (3)•1956','\
Billy Higgins•Bridgework•Contemporary Records•1987','\
Lee Konitz•Toot Sweet•Owl Records (4)•1982','\
Bob Mintzer Big Band•Papa Lips•CBS/Sony•1984','\
John Coltrane•Lush Life•Prestige•1961','\
no artist•Uptown Express•Palo Alto Jazz•1985','\
Akio Sasajima•Akio With Joe Henderson•Muse Records•1988'),'\
\
I Heard It Through The Grapevine\
':('\
Earl Klugh•I Heard It Through The Grapevine / Kiko•Blue Note•1976','\
Marisa Monte•Marisa!•World Pacific Records•1992','\
Red Prysock•I Heard It Through The Grapevine / Groovy Sax•Chess•1968','\
Jimmy Brown (10)•Chain Of Fools / I Heard It Through The Grapevine•Abet•1968','\
D D Douglas•Heard It Through The Grapevine•Slique-D Records•1991','\
Harold Mabern•Rakin\' And Scrapin\'•Prestige•1969','\
Eric Gale•Let\'s Stay Together•Artful Balance Records•1988','\
Antonio Forcione•Dedicato•Naim Label•1996','\
Earl Klugh•Living Inside Your Love•Blue Note•1976','\
"Stix" Hooper•Lay It On The Line•Artful Balance•1989','\
Karen Souza•Hotel Souza•Music Brokers•2012','\
Sounds Nice•Love At First Sight•Parlophone•1970','\
Various•The Artful Balance Collection - Volume 2•Artful Balance Records•1989','\
Bob Mintzer•Urban Contours•DMP•1989','\
Jazz Jamaica•Double Barrel•Hannibal Records•1998','\
Peter White•Groovin\'•Heads Up International•2016'),'\
\
I Let a Song Go Out of My Heart\
':('\
Dizzy Gillespie - Stan Getz Sextet•The Dizzy Gillespie - Stan Getz Sextet•Clef Records•1954','\
Duke Ellington And His Orchestra•I Let A Song Go Out Of My Heart / Mighty Like The Blues•Parlophone•1948','\
Johnny Hodges And His Orchestra•I Let A Song Go Out Of My Heart / Don\'t Get Around Much Anymore•Norgran Records•1955','\
Duke Ellington And His Orchestra•The Gal From Joe\'s / I Let A Song Go Out Of My Heart•Brunswick•1938','\
Mildred Bailey And Her Orchestra•I Let A Song Go Out Of My Heart / Rock It For Me•Vocalion (2)•1938','\
Ray Anthony & His Orchestra•Singin\' In The Rain / I Let A Song Go Out Of My Heart•Capitol Records•1952','\
Duke Ellington And His Orchestra•Ellingtonia - Vol. 2 “The Thirties”•Philips•0','\
Erroll Garner Trio•Erroll Garner Trio•Disques Vogue•1954','\
Norris Turney•I Let A Song...•Black And Blue•1978','\
Duke Ellington•Duke Ellington Plays Duke Ellington•Philips•0','\
Jimmy Smith•A Date With Jimmy Smith Vol. 2•Blue Note•1957','\
Eddie Miller (2)•Ellington Echoes•Decca•0','\
Dinah Washington•After Hours With Miss D•Emarcy•1955','\
The Art Van Damme Quintet•Lullaby Of Broadway•Philips•1957','\
Dizzy Gillespie - Stan Getz Sextet•The Dizzy Gillespie - Stan Getz Sextet•Norgran Records•1954','\
Jimmy Dorsey And His Orchestra•I Let A Song Go Out Of My Heart / If You Were In My Place (What Would You Do?)•Decca•1938','\
Terry Gibbs•Terry Gibbs Plays The Duke•Mercury•1957'),'\
\
I Love Lucy\
':('\
Victor Feldman•Your Smile•Choice (7)•1974','\
Richie Cole•Hollywood Madness•Muse Records•1980','\
Medeski Scofield Martin & Wood•Juice•Indirecto Records•2014','\
Barry Harris (2)•For The Moment•Uptown Records (2)•1985','\
101 Strings•A Tribute To John Lennon•Alshire•1981','\
Ronnie Aldrich•Tomorrow\'s Yesterdays•London Records•1979','\
no artist•Steppin\' Out•Pausa Records•0','\
Stephen Scott (5)•The Beautiful Thing•Jazz Heritage•1997','\
101 Strings•101 Strings Play A Tribute To The Beatles•Madacy Entertainment•1996','\
no artist•Naked Beauty•Marquis Music•2003','\
Barry Harris (2)•Live At Maybeck Recital Hall Volume Twelve•Concord Jazz•1991','\
John Gary•John Gary•Pickwick/33 Records•0','\
no artist•Portraits Of Cuba•Chesky Records•1996','\
Michael Franks•Dragonfly Summer•Reprise Records•1993','\
Napa Valley Duo•An American In Paris•IAC Records•2018'),'\
\
I Love Paris\
':('\
Michel Legrand Et Son Orchestre•The New I Love Paris•Columbia•1961','\
Michel Legrand•Legrand Piano•Columbia•1960','\
Erroll Garner Trio•Garner In Paris•Philips•1958','\
Michel Legrand Et Son Trio•Paris Jazz Piano•Philips•1961','\
Paul Moer•I Love Paris•Del-Fi Records•1961','\
Pierre Legendre•I Remember Paris•Custom Records (2)•0','\
Franck Pourcel Et Son Grand Orchestre•París•Odeon•1976','\
Les Baxter His Chorus And Orchestra•I Love Paris / Gigi•Capitol Records•1953','\
Roger Roger And His Orchestra•Paris Te Amo•Hispavox•1956','\
Andy Williams•Under Paris Skies•Cadence (2)•1960','\
The Parris Mitchell Strings•From Paris With Love.•Pickwick/33 Records•0','\
Ike Isaacs With His London Guitars•London Guitars - Paris Fashion•World Record Club•1968','\
The Ramsey Lewis Trio•I Love Paris / Song Of India•Argo (6)•1959','\
Fontanna And His Orchestra•The Magic Of Paris•Buckingham Records•0'),'\
\
I Love You\
':('\
Gordon Jenkins And His Orchestra And Chorus•Would I Love You (Love You Love You) / I Love You Much Too Much•Decca•1951','\
Chris Montez•The More I See You•A&M Records•1966','\
Charlie Parker•Plays Standards - Verve Jazz Masters 28•Verve Records•1994','\
Carmen Cavallaro•For Sweethearts Only•Brunswick•0','\
Stan Getz•Serenity•EmArcy•1991','\
Michael Franks•When I Give My Love To You•Warner Bros. Records•1985','\
Marina Laslo•I Wish You Love•MLM Music•2010','\
Varetta Dillard•I Love You / I Love You Just The Same•Savoy Records•1953','\
Monty Alexander•Triple · Treat · I I I•Concord Jazz•1989','\
Jerry King And His Orchestra•Gold Record•Promenade•0','\
Lester Young Quintet•I Can\'t Give You Anything But Love / I\'m Confessin\' That I Love You /•Blue Star•0','\
Gloria Lynne•I Wish You Love•Everest•1964','\
The Alan Tew Orchestra•To The One I Love•Pye Records•1975','\
John Coltrane•Lush Life•Metronome•1961','\
The Johnny Mann Singers•Ballads Of The King•Liberty•1961','\
Various•8 Ways to Jazz - the music of Cole Porter•Riverside Records•1958','\
Peggy Lee•If You Go•Capitol Records•1961','\
Peggy Lee•If You Go•Capitol Records•1961','\
Kay Starr•I Cry By Night•Capitol Records•1962','\
Thelonious Monk•Standards•Columbia•1989','\
Linda Ronstadt•I Love You For Sentimental Reasons•Asylum Records•1986','\
King Oliver & His Orchestra•Don\'t You Think I Love You? / Struggle Buggy•Victor•1930','\
Bobby Short•Speaking of Love The Songs of Bobby Short•Atlantic•1958','\
Felicia Sanders•I Wish You Love•Time Records (3)•1960','\
Nancy Wilson•I Wish You Love•CEMA Special Markets•1991','\
John Coltrane•Lush Life•Prestige•1963','\
Gene Ammons•Love I Found You•Prestige•1963','\
The "New" Ambassador Hotel Orchestra•Japanese Sandman / I Love You•Coral•1954','\
Carmen McRae•I\'ll Love You / I Love The Ground You Walk On•Decca•1958'),'\
\
I Loves You Porgy\
':('\
no artist•(I Loves You) Porgy / Tango Bongo •Carlton•1959','\
Nina Simone•Little Girl Blue•Charly Records•1987','\
Miles Davis•I Loves You Porgy / It Ain\'t Necessarily So•Columbia•1961','\
Nina Simone•I Loves You Porgy•Philips•1964','\
Nina Simone•I Loves You Porgy•Bethlehem Records•1959','\
Nina Simone•I Loves You Porgy / My Baby Just Cares For Me •Bethlehem Records•0','\
Various•Ultimate Jazz•Verve Records•1998','\
James Morrison•James Morrison At The Winery•ABC Records (3)•1985','\
Paul Bley•When Will The Blues Leave•ECM Records•2019','\
Monica Zetterlund•Porgy And Bess•Columbia•1959','\
Nina Simone•My Baby Just Cares For Me•Charly Records•1982','\
Ruth Brown•Late Date With Ruth Brown•Atlantic•0','\
Various•By George*And Ira: Red Hot On Gershwin•Verve Records•1998','\
Miles Davis•Love Songs•Columbia•1999'),'\
\
I May Be Wrong\
':('\
Benny Green And His Quintet•I May Be Wrong•Decca•1954','\
John Kirby And His Orchestra•Opus 5 / I May Be Wrong•Vocalion (2)•1939','\
The Dave Brubeck Quartet•I May Be Wrong / On A Little Street In Singapore•Fantasy•1952','\
Stan Kenton And His Orchestra•Gambler\'s Blues / I May Be Wrong•Decca•0','\
Count Basie Orchestra•Boogie Woogie / Exactly Like You•Decca•1937','\
Gerry Mulligan Quartet•I May Be Wrong / I\'m Beginning To See The Light•Swing (3)•1953','\
Sid Phillips Band•Dixie Beat•no label•1959','\
Charlie Parker•The Happy "Bird"•Charlie Parker Records•1961','\
Hoagy Carmichael•Huggin\' And Chalkin\' / I May Be Wrong But I Think You\'re Wonderful•Decca•1946','\
Gene Krupa And His Orchestra•Please Don\'t Play Number Six Tonight / I May Be Wrong•Columbia•1947','\
Gerry Mulligan Quartet•Gerry Mulligan Quartet Vol. 1•Vogue•0','\
Georgie Auld And His Orchestra•In The Land Of Hi-Fi Volume 2•EmArcy•0','\
Frank Rosolino•I Play Trombone•Bethlehem Records•1956'),'\
\
I Mean You\
':('\
Count Basie Orchestra•Feedin\' The "Bean" / I Do Mean You•Parlophone•0','\
Thelonious Monk•\'Round Midnight•Milestone (4)•1982','\
Jeff Beck•You Know What I Mean•Epic•1975','\
Bud Powell•Tribute To Thelonious 64•Mythic Sound•1989','\
Thelonious Monk•Bop Fathers "In Paris"•Lotus•1978','\
OYEZ (2)•I Mean You•Timeless Records (3)•1988','\
Thelonious Monk•Monk In France•Riverside Records•1965','\
Bobby Hutcherson•Nice Groove•Baystate•1984','\
Sarah Vaughan•Count Basie / Sarah Vaughan•Roulette•0','\
The Thelonious Monk Quintet•5 By Monk By 5•Riverside Records•1959','\
Bobby Hutcherson•Four Seasons•Timeless Records (3)•1985','\
Randy Weston•Portraits Of Thelonious Monk•Verve Records•1989','\
The Thelonious Monk Quartet•Live At The Five Spot Discovery!•Blue Note•1993','\
Valaida Snow•I Ain\'t Gonna Tell / If You Don\'t Mean It•Chess Record Corp.•1953','\
Sullivan Fortner•Aria•Impulse!•2015','\
Thelonious Monk•Monk In France•Riverside Records•1965','\
Bobby Hutcherson•Nice Groove•Baystate•1984','\
Ottilie Patterson•I Hate Myself (For Being So Mean To You)•Columbia•1962','\
Johnny Griffin•Call It Whachawana•Galaxy•1983'),'\
\
I Only Have Eyes For You\
':('\
Roberto Inglez And His Orchestra•Whispering / I Only Have Eyes For You•Parlophone•1950','\
George Shearing Trio•I Only Have Eyes For You•London Records•0','\
Slim Gaillard And His Orchestra•I Only Have Eyes For You / As You Are•Mercury•1952','\
Werner Müller Mit Dem RIAS-Tanzorchester•Trumpet-Boogie / I Only Have Eyes For You•Brunswick•1952','\
Stan Getz Quartet•I Only Have Eyes For You / Night And Day•Elite Special•0','\
Coleman Hawkins Quintet•\'S Wonderful / I Only Have Eyes For You•Keynote Recordings (2)•1944','\
Boyd Raeburn And His Orchestra•Boyd Meets Stravinsky / I Only Have Eyes For You•Jewel•1946','\
The Flamingos•I Only Have Eyes For You•End•1959','\
Eddie "Lockjaw" Davis•I Only Have Eyes For You / Chihuahua•Royal Roost•1955','\
Cleo Laine•You\'ll Answer To Me•Fontana•1961','\
Billie Holiday And Her Orchestra•I Only Have Eyes For You / These Foolish Things•Mercury•0','\
Jimmy Giuffre•Jimmy Giuffre (Part 1)•Capitol Records•1954','\
Stan Getz Quartet•I\'m Gettin\' Sentimental Over You / I Only Have Eyes For You•Metronome•0','\
Jo Stafford•St. Louis Blues / I Only Have Eyes For You•Snowy Bleach•1950','\
Freddy Gardner•I\'m In The Mood For Love / I Only Have Eyes For You•Columbia•1948','\
no artist•I Only Have Eyes For You •ECM Records•1985','\
Oscar Peterson•Oscar Peterson At Carnegie•Clef Records•1952'),'\
\
I Remember Clifford\
':('\
The Bud Powell Trio•At The Golden Circle Volume 3•SteepleChase•1979','\
Oscar Pettiford Orchestra•An "Oscar" For Oscar•Electrola•1959','\
Art Blakey & The Jazz Messengers•Aurex Jazz Festival \'83•Eastworld•1983','\
Cedar Walton Quartet•Bluesville Time•Criss Cross Jazz•1985','\
Stan Getz Quartet•At Montreux•Polydor•1977','\
Art Blakey & The Jazz Messengers•I Remember Clifford•Fontana•1961','\
Sonny Rollins•Alternatives•Bluebird (3)•1992','\
Roger Guérin•Roger Guérin - Benny Golson•Columbia•1959','\
Lee Morgan•Vol. 3•Blue Note•1957','\
The Great Jazz Trio•Milestones•East Wind•1978'),'\
\
I Remember You\
':('\
Hank & Carol Diamond•Exodus / I Remember You•Workshop Jazz•1962','\
Grant Green•Remembering•Blue Note•1980','\
Artie Shaw And His Orchestra•All I Remember Is You / Octoroon•Bluebird (3)•1939','\
Stan Getz•Serenity•EmArcy•1991','\
Clifford Brown And Max Roach•Live At The Bee Hive•Columbia•1979','\
no artist•Heartaches / I Remember You•Ariola America•1976','\
Charlie Parker•Charlie Parker•Clef Records•1954','\
Jackie McLean Quartet•Tune Up•SteepleChase•1987','\
Stanley Turrentine•Cherry•CTI Records•1972','\
Jack La Forge His Piano & Orchestra•I Remember You•Regina Records Company•0','\
Lee Konitz•Motion•Verve Records•1961','\
Tal Farlow•Second Set•Xanadu Records•1977','\
Ken Dodd•The Key•Columbia•1962','\
Harry James And His Orchestra•I Remember You / Last Night I Said A Prayer•Columbia•1942','\
Jimmy Dorsey And His Orchestra•I Remember You / If You Build A Better Mousetrap•Decca•1942','\
Ray Conniff And The Singers•Young At Heart•CBS•1963'),'\
\
I Say A Little Prayer For You\
':('\
Wes Montgomery•Georgia On My Mind / I Say A Little Prayer For You•A&M Records•1968','\
Maulawi•Orotunds•180 Proof Records•2014','\
Ahmad Jamal•Tranquility•Abc Records•1968','\
Cal Tjader•Cal Tjader Sounds Out Burt Bacharach•Skye Records•1968','\
Cal Tjader•Solar Heat - Sounds Out Burt Bacharach•Vampi Soul•2003','\
Ahmad Jamal•Tranquility / Outertimeinnerspace•Impulse!•2015','\
Woody Herman•Light My Fire•Cadet•1969','\
Russell Malone•Black Butterfly•Columbia•1993','\
Woody Herman And The Thundering Herd•Keep On Keepin\' On: 1968-1970•Chess•1998','\
Jonathan Knight (3)•Lonely Harpsichord Memories Of That Rainy Night•Viva (3)•0','\
The Earl Klugh Trio•Volume One•Warner Bros. Records•1991','\
Burt Bacharach•Reach Out•A&M Records•1967'),'\
\
I Should Care\
':('\
Archie Shepp•Coral Rock•America Records•1970','\
Jimmy Dorsey And His Orchestra•Twilight Time / I Should Care•Decca•1945','\
Dizzy Gillespie And His Orchestra•Swedish Suite / I Should Care•RCA Victor•1949','\
Ralph Flanagan And His Orchestra•Tippin\' In / I Should Care•RCA Victor•0','\
Gloria Lynne•Indian Love Call•Everest•1964','\
The Brew Moore Quartet•I Should Care•SteepleChase•1982','\
Chet Baker•Chet Baker•Armando Curcio Editore•1991','\
Seiichi Nakamura•Let\'s Swing Now•Victor•1976','\
The Four Clefs•Why Should I Care? / The Jive Is Jumpin\'•Bluebird (3)•1942','\
Tommy Dorsey And His Orchestra•I Should Care / Please Don\'t Say No•Victor•1945','\
Clifford Jordan And The Magic Triangle•On Stage Vol. 2•SteepleChase•1978','\
Bernt Rosengren Quartet•Surprise Party•SteepleChase•1983','\
Varsity Eight•Easy Melody / You Didn\'t Care When You Broke My Heart•Cameo (3)•1924','\
Diana Krall•Why Should I Care•Verve Records•1999','\
Paul Gonsalves Quartet•Boom-Jackie-Boom-Chick•Vocalion (3)•1964','\
Milt Jackson•Milt Jackson Quartet•Original Jazz Classics•1982','\
Art Farmer•The Summer Knows•East Wind•1977','\
The Modern Jazz Quartet•European Concert : Volume One•Atlantic•1962','\
Milt Jackson•Milt Jackson Quartet•Prestige•1955'),'\
\
I Thought About You\
':('\
Etta Jones•Don\'t Worry About Me / I Thought About You•King Records (3)•1961','\
Miles Davis•Someday My Prince Will Come•CBS•1962','\
Kenny Burrell•I Thought About You•Prestige•1963','\
Billie Holiday And Her Orchestra•Love Me Or Leave Me / I Thought About You•Clef Records•0','\
Gordon Jenkins and his Orchestra and Chorus•I Thought About Marie•Decca•1952','\
Frank Foster And The Loud Minority•Manhattan Fever•Denon•1978','\
Frank Rosolino•Thinking About You•Sackville Recordings•1984','\
Xanadu•Xanadu At Montreux Volume Three•Xanadu Records•1979','\
Terence Blanchard•Wandering Moon•Sony Classical•2000','\
Stan Getz•Voyage•BlackHawk Records•1986','\
Sadao Watanabe•Iberian Waltz•Takt Jazz Series•1967','\
Louis Stewart•I Thought About You•Lee Lambert•1979','\
Miles Davis•My Funny Valentine - Miles Davis In Concert•Columbia•1965'),'\
\
I Want To Be Happy\
':('\
Lester Young•I Want To Be Happy•Verve Records•0','\
Red Nichols And His Five Pennies•Tea For Two / I Want To Be Happy•Brunswick•1934','\
Tony Osborne And His Orchestra•I Want To Be Happy Cha Cha / Marrakesh•no label•1958','\
Chick Webb And His Orchestra•I Want To Be Happy / Hallelujah!•Decca•1937','\
Tony Bennett•Tea For Two / I Want To Be Happy•Columbia•1971','\
Glenn Miller And His Orchestra•In The Mood / I Want To Be Happy•Bluebird (3)•1939','\
Claude Luter•Charleston Vol.11•Disques Vogue•0','\
Sammy Davis Jr.•The Candy Man / I Want To Be Happy•MGM Records•1971','\
Cal Tjader•Love Me Or Leave Me•Savoy Records•1953','\
Little Jazz Trumpet Ensemble•Roy Eldridge And His Trumpet Ensemble - Volume 8•Mercury•0','\
Lester Young Trio•№.2•Clef Records•1953','\
Tommy Dorsey And His Orchestra•I Want To Be Happy Cha Cha•Brunswick•1958','\
Enoch Light And The Light Brigade•I Want To Be Happy Cha Cha / Cara Mia Cha Cha•Grand Award Records•1958'),'\
\
I Wanted To Say\
':('\
Stan Getz•Voyage•BlackHawk Records•1986','\
Kenny Barron Quintet•Quickstep•Enja Records•1991','\
Stan Getz Quartet•Live In Paris•Dreyfus Jazz•1996','\
David Sills (3)•Bigs•Naxos Jazz•2001','\
Bugge Wesseltoft•New Conception Of Jazz: Sharing•Jazzland Recordings•1998','\
MoZella•I Will•Maverick•2006','\
Jim Brickman•By Heart: Piano Solos•Windham Hill Records•1995','\
Shirley Eikhard•Let Me Down Easy•Attic•1975','\
Billy Goldenberg•Play It Again Sam (Dialogue And Music From The Original Soundtrack Of The Paramount Picture)•Paramount Records•1972','\
Santana•Greatest Hits•Columbia•2012','\
Frank De Vol•Portraits: The Creative Sounds Of Frank De Vol•Jasmine Records•2010','\
Santana•The Ultimate Collection•Columbia•2000'),'\
\
I Was Doing All Right\
':('\
Ella Fitzgerald And Her Savoy Eight•It\'s Wonderful / I Was Doing All Right•Decca•1938','\
Oscar Peterson•Oscar Peterson Plays George Gershwin•Columbia•0','\
Dexter Gordon•Doin\' Allright•Blue Note•1961','\
Jim Hall•Good Friday Blues: The Modest Jazz Trio•Pacific Jazz•1960','\
Stan Getz•Stan Getz And The Oscar Peterson Trio•Verve Records•1957','\
Various•Inspiration In Sax•Cotton Fields•0','\
Oscar Peterson•The Gershwin Songbooks•Verve Records•1996','\
Diana Krall•Doing All Right•Vinyl Passion•2010'),'\
\
I Will Be Here For You\
':('\
Al Jarreau•High Crime•WEA•1985','\
Al Jarreau•Mornin\'•WEA•1983','\
Art Farmer•On The Road•Contemporary Records•1976','\
Al Jarreau•In Concert Live At London\'s Wembley Arena•Westwood One•1984','\
Chico Randall•Relax\'n With Chico Randall•Roulette•1960','\
Natalie Cole•Inseparable•Capitol Records•1975','\
Al Jarreau•Jarreau•Warner Bros. Records•1983','\
Al Jarreau•In London•WEA•1985'),'\
\
I Will Wait For You\
':('\
Louis Armstrong•Willkommen / I Will Wait For You•Brunswick•1971','\
The Dukes Of Dixieland•Exactly Like You•Decca•0','\
Steve Lawrence (2)•I Will Wait For You / Bewitched•Columbia•1965','\
Louis Armstrong•I Will Wait For You•Brunswick•1968','\
Buddy Greco•She\'s A Carioca (Ela E Carioca)•Reprise Records•1967','\
Steve Kuhn Trio•I Will Wait for You: The Music of Michel Legrand•Venus Records (5)•2014','\
Takashi Mizuhashi•Interplay Now•Carnival (2)•1981','\
Sonny Stitt•I Keep Comin\' Back!•Roulette•1966','\
Donald Byrd•The Creeper•Blue Note•1981','\
Michel Legrand•Recorded Live At Jimmy\'s•RCA•1975','\
Al Jarvis (2)•Makes Love To The Piano•Celestial Records (3)•1978','\
Doc Severinsen•Ja-Da•MCA Special Products•1986','\
Sharel Cassity Quartet•Manhattan Romance•Venus Records (5)•2014','\
Herb Alpert & The Tijuana Brass•This Guy\'s In Love With You•Ariola•0'),'\
\
I Wish I Knew\
':('\
Lionel Hampton And His Orchestra•Red Top•Decca•0','\
Chet Baker•Chet Baker Sings And Plays•Pacific Jazz•1955','\
Harry James And His Orchestra•The More I See You / I Wish I Knew•Columbia•1945','\
Spike Milligan•Wish I Knew/Will I Find My Love Today•Parlophone•1958','\
Nat King Cole•The Very Thought Of You•Capitol Records•1958','\
The 360 Degree Music Experience•Safe•Red Record•1980','\
Billy Taylor Trio•I Wish I Knew How It Would Feel To Be Free•Tower•1968','\
Ahmad Jamal•Wild Is The Wind / I Wish I Knew•Cadet•1968','\
Lionel Hampton•Live At The Blue Note•Telarc Jazz•1991','\
The Bill Evans Trio•Explorations•Riverside Records•1961','\
Billy Taylor Trio•I Wish I Knew (How It Would Feel To Be Free)•Capitol Records•1986'),'\
\
I Wish I Were In Love Again\
':('\
Sarah Vaughan•I Got Rhythm•Columbia•1965','\
Frank Sinatra•À Paris•Capitol Records•1962','\
André Previn•Like Love•Columbia•1960','\
Latin Jazz Quintet•The Latin Jazz Quintet•United Artists Records•1961','\
Frank Stallone•Day In Day Out•A.1. Records•1991','\
Trigger Alpert•Trigger Happy!•Riverside Records•1956','\
Frank Stallone•In Love In Vain•Paradise Musicwerks•2003','\
Mel Tormé•Songs For Any Taste•Parlophone•1959','\
Rocky Cole•Smooth & Rocky•Roulette•1960','\
Jack Haskell•Let\'s Fall In Love•Jubilee•1957','\
Buddy Greco•I Like It Swinging•Columbia•1961','\
Eric Dolphy•Hot & Cool Latin•Blue Moon (4)•1996','\
Emil Coleman•Emil Coleman Lights Up The Plaza•Philips•1962','\
Ruby Braff / George Barnes Quartet•Braff/Barnes Quartet Salutes Rodgers And Hart•Concord Jazz•1975','\
Sid Ramin And His Orchestra•Love Is A Swingin\' Word•RCA Victor•1959','\
Rosemary Clooney•Show Tunes•Concord Jazz•1989'),'\
\
Icarus\
':('\
Paul Winter (2)•Icarus / Jenny•A&M Records•1972','\
Paul Winter (2)•Minuit / Icarus•Epic•1972','\
Dave Pike•Let The Minstrels Play On•Muse Records•1980','\
Ralph Towner•Matchbook•ECM Records•1975','\
Oregon•Live In New Orleans•Hi Hat•2016','\
Oscar Rocchi•Metamorphosis•Ring•1981','\
Ralph Towner•Diary•ECM Records•1974','\
Вежливый Отказ•Ethnic Experiences•Rockadillo Records•1990','\
Patricia Barber•Mythologies•Blue Note•2006','\
Greg & Bev Smith•No Baggage•Intima Records•1988'),'\
\
Ice Cream Konitz\
':('\
Lee Konitz•Subconscious-Lee•Prestige•1955','\
Boulou Ferré•Trinity•SteepleChase•1983','\
Lee Konitz•The New Sounds•Prestige•1951','\
Lee Konitz•Sax Of A Kind - Lee Konitz In Sweden 1951/53•Dragon (8)•1979','\
Anthony Braxton•Quintet (Tristano) 1997•New Braxton House•2012'),'\
\
Ictus\
':('\
Peter Lemer Quintet•Local Colour•ESP Disk•1968','\
Bobby Naughton Units•Understanding•Otic Records•1972','\
Attila Zoller Quartet•The Horizon Beyond•Emarcy•1966','\
The Jimmy Giuffre Trio•Thesis•Verve Records•1961','\
The Jimmy Giuffre Trio•1961•ECM Records•1992','\
Paul Bley•Turns•Savoy Jazz•1987','\
Paul Bley & Scorpio•Paul Bley & Scorpio•Milestone (4)•1973','\
Paul Bley•Turning Point•Improvising Artists Inc.•1975','\
Paul Bley Quintet•Barrage•ESP Disk•1965','\
Masabumi Kikuchi•Masabumi Kikuchi With Gil Evans•Philips•1972','\
Gary Burton Quintet•Dreams So Real - Music Of Carla Bley•ECM Records•1976','\
Paul Bley•Live•SteepleChase•1986'),'\
\
Ida Lupino\
':('\
Paul Bley•Turns•Savoy Jazz•1987','\
Paul Bley•Ramblin\'•BYG Records•1969','\
Paul Bley•Turning Point•Improvising Artists Inc.•1975','\
Mary Halvorson•Meltframe•Firehouse 12 Records•2015','\
John Scofield•John Scofield•Trio Records•1978','\
Paul Bley•Open To Love•ECM Records•1973','\
Mete Erker Trio•Live•Sympathetic Vibrations Music•2016','\
Gebhard Ullmann•Per-Dee-Doo•NABEL•1990','\
Michel Portal•Dockings•Label Bleu•1998','\
Nexus (50)•Nexus•Four Leaf Clover Records•1978','\
Larry Goldings•Big Stuff•Warner Bros. Records•1996','\
Gary Burton•Right Time - Right Place•Sonet•1990'),'\
\
Idol Gossip\
':('\
Woody Herman•I Giganti Del Jazz Vol. 49•Curcio•0','\
no artist•Idol Gossip•Chiaroscuro Records•1976'),'\
\
If I Loved You\
':('\
Georgie Auld And His Orchestra•My Blue Heaven / If I Loved You•Mercury•1955','\
Frank Sinatra•If I Loved You / You\'ll Never Walk Alone•Columbia•1950','\
Eddie Calvert•Moonglow - Theme From "Picnic" / If I Loved You•Columbia•1956','\
Ray Conniff And The Singers•Young At Heart•CBS•1963','\
Toni Dalli•Just Say I Love Her / If You Loved Me•Columbia•1958','\
Harry James And His Orchestra•Sweet Trumpet•Philips•0','\
Eddie Calvert•Trumpet Serenade (No 2)•Columbia•1957','\
Erroll Garner•Piano•Mercury•1946','\
Mantovani And His Orchestra•Hello Young Lovers•London Records•0','\
Paul Bley•Live Again•SteepleChase•1987','\
David Schnitter•Glowing•Muse Records•1981','\
Georgie Auld And His Orchestra•In The Land Of Hi-Fi Volume 2•EmArcy•0','\
Frank Sinatra•Vol. 2•Columbia•1956','\
Roberto Rossani And His Orchestra•Soft Warm Mood•Somerset•1959','\
Barry Harris Trio•Vicissitudes•MPS Records•1975','\
Frank Sinatra•Frank Sinatra Vol. 3•Joker (2)•1974','\
Guy Lombardo And His Royal Canadians•If I Had A Girl Like You / Last Night On The Back Porch•Decca•1964','\
Les Brown And His Band Of Renown•Invitation•Coral•1954','\
Dinah Washington•Music For A First Love•Mercury•1956','\
Bud Powell•Holidays In Edenville 64•Mythic Sound•1989'),'\
\
If I Should Lose You\
':('\
Charlie Parker With Strings•April In Paris / If I Should Lose You•Blue Star•0','\
Dinah Washington•Tears And Laughter•Mercury•1962','\
Buddy DeFranco•Pretty Moods•Norgran Records•1954','\
The Four Freshmen•Voices In Latin•Capitol Records•1958','\
Yoshio Otomo Quartet•Moon Ray•Three Blind Mice•1977','\
NYSQ•Heaven Steps To Seven•Whirlwind Recordings Ltd•2018','\
The Oscar Peterson Quartet•If You Could See Me Now•Pablo Records•1986','\
Hank Mobley•Soul Station•Blue Note•1960','\
Paul Gonsalves Quartet•Boom-Jackie-Boom-Chick•Vocalion (3)•1964','\
Johnny Coles Quartet•The Warm Sound•Epic•1961','\
Bernie Senensky•Friday The 14th•Unity Records (16)•1989'),'\
\
If I Were a Bell\
':('\
Sarah Vaughan•The Big Three•Roulette•0','\
Various•Ginparis Session - June 26','1963•Three Blind Mice•1971','\
Lloyd Robinson•I\'ll Try / If I Were A Bell•D Darling•1962','\
Jimmy Smith Trio•Live At The Village Gate•Metro Records•1965','\
Miles Davis•Cookin\' At The Plugged Nickel•Columbia•1987','\
Elvin Jones•Heart To Heart•Denon•1981','\
The Miles Davis Sextet•Jazz At The Plaza Vol. 1•Columbia•1973','\
Miles Davis•In Person Saturday Night At The Blackhawk San Francisco Volume 2•Columbia•1989','\
Miles Davis•Greatest Hits•Prestige•1967','\
Various•The Very Best Of Prestige Records•Prestige•2009'),'\
\
If There Is Someone Lovelier Than You\
':('\
John Coltrane•Settin\' The Pace•Prestige•1961','\
Tal Farlow•The Tal Farlow Album•Karusell•1955','\
Enrico Pieranunzi Marc Johnson Joey Baron•New Lands•Timeless Records (3)•1984','\
Sonny Red•Breezing•Jazzland•0','\
Enrico Pieranunzi•Autumn Song•Enja Records•1985','\
John Coltrane•Rain Or Shine•Prestige•1980','\
Bobby Hackett•Trumpet Solos With Bill Challis•Brunswick•1950','\
John Coates Jr•Portrait - At The Piano With Rhythm•Savoy Records•1956','\
Tommy Dorsey And His Orchestra•You And The Night And The Music•Decca•1951','\
André Kostelanetz•You And The Night And The Music•Columbia Special Products•0'),'\
\
If You Could See Me Now\
':('\
Jon Eardley•Hey There Jon Eardley•Prestige•1955','\
Horace Tapscott•In New York•Interplay Records•1979','\
Shakatak•If You Could See Me Now•Polydor•1983','\
Sarah Vaughan•Sings After Dark №. 2•MGM Records•1956','\
Archie Shepp•Tray Of Silver•Denon•1979','\
Wynton Kelly Trio•Smokin\' At The Half Note•Verve Records•1965','\
Randy Weston Trio•The Randy Weston Trio•Riverside Records•1955','\
The Oscar Peterson Quartet•If You Could See Me Now•Pablo Records•1986','\
Continuum (5)•Mad About Tadd•Quicksilver•1982','\
Roy Brooks•Beat•Workshop Jazz•1964'),'\
\
If You Never Come to Me\
':('\
Yasuko Agawa•Lady September•Invitation•1985','\
Milt Jackson & Strings•Feelings•Pablo Records•1976','\
Maximilian Geller Quartet•Smile•Edition Collage•1993','\
Harry Allen (2)•Eu Não Quero Dançar ~ I Won\'t Dance•RCA Victor•1998','\
Frank Sinatra•Francis Albert Sinatra & Antonio Carlos Jobim•Reprise Records•1967','\
Roger Kellaway•Meets The Duo Gene Bertoncini And Michael Moore•Solid Records (6)•2018','\
Eddie Drennon & The B.B.S. Unlimited•Would You Dance To My Music•Casablanca•1977','\
Sandy Patton•Waltz Forever My Love•JHM Records•1996','\
Nancy Harrow•You Never Know•Atlantic•1963','\
Chet Baker•Chet•Riverside Records•1959'),'\
\
I\'ll be Around\
':('\
Bobby Caldwell•Come Rain Or Come Shine•Sin-Drome Records•1999','\
Dr. John•Live At Montreux 1995•Eagle Records•2012','\
Various•In The Wee Small Hours•Columbia House•1974','\
Frank Sinatra•Night And Day 2 CD Set•MCPS Ltd.•0','\
Various•Fabulous Memories Of The Fabulous \'40s•no label•1981','\
Various•Dig That Crazy Santa Claus : Classic R&B / Blues Christmas Cuts 1953 - 56•Contrast Records (7)•2017','\
AK (2)•Say That You Love Me -Best Of NY Sweet Electro•-Virgin•2010','\
Benny Goodman•Small Group Recordings•Intense Rarities•2001','\
Various•We Remember Them Well•no label•1986','\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014'),'\
\
I\'ll Get By\
':('\
Lionel Hampton And His Orchestra•Jazz Archives•PMF Records•1990','\
Various•Singin’ In The Rain: Famous Stage And Screen Personalities•Saville Records•1990','\
Billie Holiday•Rare And Unissued Recordings From The Golden Years - Volume One•Queen-disc•1984','\
Esquire All Stars•Esquire Jazz Concert•Giants Of Jazz•1998','\
Kevin Mahogany•Pride & Joy•Telarc•2002','\
Frank Sinatra•Night And Day 2 CD Set•MCPS Ltd.•0','\
Basil Fomeen And His Orchestra•Song Hits Of 1928•Decca•1947','\
Sacha Rubin•No Balaio•London Records•1967','\
Various•Your Hit Parade • 1944•Time Life Music•1990','\
Various•Running The Voodoo Down (Explorations In Psychrockfunksouljazz 1967-80)•Festival Records•2016','\
Fred Astaire•Puttin On The Ritz - Fred Astaire\'s Greatest Hits•Black Tulip•0','\
The Big Ben Banjo Band•Strummin\' On The Old Banjo•Jasmine Records•2017','\
George Duke•George Duke Часть 1-2•Домашняя Коллекция•0'),'\
\
I\'ll Remember April\
':('\
Kenny Drew•The Modernity Of Kenny Drew•Norgran Records•1954','\
The Mitchell-Ruff Trio•The Catbird Seat•Atlantic•1961','\
Phineas Newborn Trio•Fabulous Phineas•RCA Victor•1958','\
Various•Norman Granz Jazz Concert #1•Norgran Records•0','\
Johnny Hartman•Songs From The Heart•Bethlehem Records•1992','\
Pete Hamill•New York City Story•CBS/Sony•1986','\
The Walter Norris Trio•Lush Life•Concord Jazz•1991','\
Various•The Concert 23.6.1958 - Baden Baden - Unreleased Radio Tapes•Delta (18)•1988','\
Wes Montgomery•Body And Soul (Recorded Live At Ronnie Scott\'s Club)•no label•1996','\
Michael Carvin•Marsalis Music Honors Michael Carvin•Marsalis Music•2006'),'\
\
I\'ll Take Romance\
':('\
Monica Zetterlund•Spring Is Here•Dragon (8)•1988','\
Various•Slow Dancing Through The Years•Sony Music Special Products•1994'),'\
\
Ill Wind\
':('\
Charlie Barnet And His Orchestra•All The Things You Are / Ill Wind•Capitol Records•0','\
The George Shearing Quintet•Ill Wind / Drume Negrita•MGM Records•1955','\
Lee Morgan•Cornbread•Blue Note•1967','\
The Horace Silver Quintet•Further Explorations•Blue Note•1958','\
Oscar Peterson•The Sound Of The Trio•Verve Records•1961','\
Oscar Peterson•The Sound Of The Trio•Verve Records•1961'),'\
\
Illuminados\
':('\
Eliane Elias•Brazilian Classics•Blue Note•2003'),'\
\
I\'m A Fool To Want You\
':('\
Chet Baker•Love Song•Baystate•1987','\
Julius Watkins•French Horns For My Lady•Philips•1962','\
Kathryn Williams•Resonator•One Little Indian•2016','\
Dee Dee Bridgewater•Midnight Sun•DDB Records (2)•2011','\
Terri Lyne Carrington•The Mosaic Project: Love And Soul•Concord Records•2015','\
Mina (3)•Mina N. 2•Rifi•1966','\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014'),'\
\
I\'m Afraid\
':('\
Monty Alexander•Trio•Concord Jazz•1981','\
Brian Byrne (2)•Jenny\'s Wedding (Original Motion Picture Soundtrack)•Varèse Sarabande•2015','\
Oliver Nelson•The Argo Verve And Impulse Big Band Studio Sessions•Mosaic Records (2)•2006','\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014','\
David Bowie•MP3 Collection•Digital Records (6)•2016'),'\
\
I\'m All Smiles\
':('\
Hampton Hawes•I\'m All Smiles•Contemporary Records•0','\
Carol Kidd•All My Tomorrows•Aloi Records•1985','\
Andy Williams•Almost There•CBS•1965','\
Benny Goodman•"The Complete Small Combinations" Volumes 3/4 (1937/1939)•RCA•1986'),'\
\
I\'m Getting Sentimental Over You\
':('\
Jack Sheldon Quintet•Jack Sheldon Quintet•Jazz: West•1955','\
Chet Baker•The Best Thing For You•A&M Records•1989','\
Bill Evans•Getting Sentimental•Milestone (4)•2003','\
Count Basie Orchestra•Basie\'s Timing•MPS Records•1976','\
Lawrence Welk•200 Years Of American Music•Ranwood•1975'),'\
\
I\'m Glad There is You\
':('\
Chet Baker Sextet•Tommyhawk / I’m Glad There Is You•Pacific Jazz•0','\
Laila Dalseth•Glad There Is You•Talent (2)•1978','\
Mina (3)•Mina N. 2•Rifi•1966','\
Jack Jones•Dear Heart•Kapp Records•1965','\
Dinah Washington•The Essential Dinah Washington•Not Now Music•2012','\
Maynard Ferguson•The Complete Roulette Recordings of the Maynard Ferguson Orchestra•Mosaic Records (2)•1994','\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014'),'\
\
I\'m Losing You\
':('\
Amy Winehouse•Back To Black: The Real Story Behind The Modern Classic •Eagle Vision•2018'),'\
\
I\'m Old Fashioned\
':('\
Cybill Shepherd•Mad About The Boy•Inner City Records•1980','\
The Kenny Drew Trio•Misty•After Beat•2006','\
Lee Kwang Cho•I\'m Old Fashioned [LP + SACD]•Audioguy Records•2015','\
Glenn Miller•Vol. II Original Recordings From 1938 To 1942 •RCA Victor•1973','\
Eubie Blake•The Eighty-Six Years Of Eubie Blake•Columbia•1973','\
Eubie Blake•The Eighty-Six Years Of Eubie Blake•Columbia•1973','\
Helen Shapiro•Simply Shapiro•Katalyst Records•2000','\
Various•Slow Dancing Through The Years•Sony Music Special Products•1994'),'\
\
I\'m Through With Love\
':('\
Scott Hamilton•Who Cares?•Fonè•2015','\
Marilyn Monroe•Philippe Peseux•Nocturne•0','\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014'),'\
\
Imagination\
':('\
Johnny Hammond•Imagination - Pt. 1•Arrow Records (7)•0','\
Glenn Miller And His Orchestra•Star Dust / Imagination•no label•1940','\
Chet Baker Quartet•Imagination / Russ Job•Pacific Jazz•0','\
Ray Anthony•Pure Imagination / Spanish Harlem•Ranwood•1971','\
no artist•Imagination / Feelin\' No Pain•Okeh•1927','\
Coleman Hawkins Quartet•Imagination / Cattin\' At Keynote •Keynote Recordings (2)•1944','\
Terry Gibbs•Seven Come Eleven / Imagination - Vol. 1•EmArcy•1957','\
Ray Anthony•Pure Imagination / Okie From Muskogee•Ranwood•1971','\
Bill Harris And His Orchestra•Bill Harris And His Orchestra•Clef Records•1954','\
Illinois Jacquet•So In Love•Argo (6)•1965','\
The King Sisters•Imagination•Capitol Records•1957','\
The Charleston Chasers•Sugar Foot Strut / Imagination•Columbia•1928','\
Bix Beiderbecke And His Orchestra•Wa-Da-Da / Imagination•Parlophone•0','\
Tony Fruscella•Fru\'n Brew (Previously Unissued Recordings From The Open Door)•Spotlite Records•1981','\
Johnny Johnson And His Orchestra•Lights Out / Too Much Imagination•Perfect (3)•1936','\
Chet Baker Quartet•Chet Baker Quartet•Vogue•1954'),'\
\
Impressions\
':('\
The John Coltrane Quartet•Live In Europe - Volume 2•Beppo Records•0','\
Zbigniew Seifert•Kilimanjaro•PolJazz•1979','\
John Coltrane•John Coltrane•Heart Note Records•1987','\
Erroll Garner•Reverie / Impressions•Atlantic•1949','\
John Coltrane•Live In Paris•BYG Records•0','\
John Coltrane•The Coltrane Legacy•The Greatest Jazz•1991','\
John Coltrane•European Tour 1961•Le Chant Du Monde•2017','\
The Blue Train•Live On Mount Meru (Volume Two)•Historic Performances Records•0','\
Robert Ruff•Shaza-Ra•Baystate•1978','\
The John Coltrane Quartet•Creation•Blue Parrot Records (2)•0'),'\
\
In A Mellow Tone\
':('\
The Manhattan Transfer•Love For Sale•Atlantic•1978','\
John & Jerry Case•Sextet Sessions•Priority Records (7)•1972','\
Red Norvo And His Overseas Spotlight Band•1-2-3-4 Jump / In A Mellow Tone•V Disc•1943','\
Ben Webster•Ben Webster And Associates•Verve Records•1959','\
Buddy Tate Quartet•Tate A Tete At La Fontaine•Storyville•1976','\
Count Basie•Loose Walk•Pablo Records•1988','\
Gene Harris•Live In London•Resonance Records•2008','\
Earl Hines•Earl Meets Sweets And Jaws•Ex Libris•1979','\
Jimmy McGriff•Black Pearl•Blue Note•1971','\
The Ellington All Stars•In A Mellow Tone•Riverside Records•1968','\
Coleman Hawkins•Night Hawk•Prestige Swingville•1961','\
Art Pepper•Intimate Art Pepper•Analogue Productions•2000'),'\
\
In A Sentimental Mood\
':('\
Duke Ellington And His Orchestra•Solitude / In A Sentimental Mood•Columbia•0','\
Duke Ellington•Sophisticated Lady•Master (2)•1937','\
Hannibal Marvin Peterson•Naima•Eastworld•1978','\
Bill Doggett•In A Sentimental Mood•King Records (3)•1971','\
Duke Ellington And His Orchestra•Caravan / In A Sentimental Mood•RCA Victor•1948','\
Duke Ellington And His Orchestra•In A Sentimental Mood / Showboat Shuffle•Columbia•0','\
Sonny Stitt•In A Sentimental Mood / Take The "A" Train•Catalyst Records (3)•1977','\
Quintette Du Hot Club De France•Exactly Like You / In A Sentimental Mood•no label•0','\
Toshiyuki Miyama & The New Herd•Take The "A" Train•Three Blind Mice•1975','\
Jimmy Dorsey And His Orchestra•Stompin\' At The Savoy / In A Sentimental Mood•Decca•1936','\
Bill Doggett•In A Sentimental Mood / Who\'s Who•King Records (3)•1956','\
Bennie Wallace•Live At The Public Theater•Enja Records•1978','\
Michel Petrucciani•Power Of Three•Blue Note•1987','\
Milt Jackson•Jackson\'sville•Savoy Records•1956','\
Art Blakey & The Jazz Messengers•Keystone 3•Concord Jazz•1982','\
Clark Terry•Duke With A Difference•Riverside Records•1957','\
Kwintet Ptaszyna Wróblewskiego•Jazz Jamboree 1960 Nr 3•Polskie Nagrania Muza•1960'),'\
\
In Case You Missed It\
':('\
Art Blakey & The Jazz Messengers•Album Of The Year•Timeless Records (3)•1981','\
Charli Persip And Superband•In Case You Missed It•Soul Note•1985','\
Marlon Simon•In Case You Missed It•Jazzheads•2007','\
Bobby Watson & Horizon•Post-Motown Bop•Blue Note•1991'),'\
\
In Love With Night\
':('\
Carla Bley•Night-glo•WATT Works•1985','\
Bill Perkins•Confluence•Interplay Records•1979','\
Bill Perkins•The Front Line•Trio Records•1978','\
Norman Luboff Choir•A Choral Spectacular•RCA Victor•1962','\
Michel Sardaby•Night Blossom•DIW•1990','\
Bert Kaempfert•Meine Lieblingsmelodien•Polydor•1971','\
Fred Waring & The Pennsylvanians•Listening Time•Decca•1949','\
Nick DeCaro•Love Storm•Invitation•1990','\
Andy LaVerne•Double Standard•Triloka Records•1993','\
Andy LaVerne•Double Standard•Triloka Records•1993','\
Bert Kaempfert•Blue Melody•Five•1986','\
Joe Newman Quartet•In A Mellow Mood•Stash Records Inc.•1982','\
Larry Adler•Again!•Audio Fidelity•1968','\
Ahmad Jamal•At The Blackhawk•Argo (6)•1962','\
Billy Taylor Quartet•Where You\'ve Been?•Concord Jazz•1981','\
Gerry Mulligan Quartet•Mulligan And Baker!•Jazztone (2)•1957','\
The Miles Davis Quintet•Steamin\' With The Miles Davis Quintet•Prestige•1961'),'\
\
In Pursuit of the 27th Man\
':('\
Horace Silver•In Pursuit Of The 27th Man•Blue Note•1973','\
Various•Mod Jazz From Blue Note•Blue Note•2004'),'\
\
In The Days Of Our Love\
':('\
The Young Lovers (2)•Those Were The Days•Design Records (2)•0','\
Peggy Lee•Close Enough For Love•DRG Records•1979','\
Marian McPartland•At The Festival•Concord Jazz•1980','\
Bert Kaempfert•Warm And Wonderful•Polydor•0','\
Marian McPartland•In My Life•Concord Jazz•1993','\
Bert Kaempfert•One Lonely Night•Polydor•1969','\
Felix Slatkin•Our Winter Love•Liberty•1963','\
Poul Hindberg Quintet•Like Someone In Love•Olufsen Records•2001','\
Koji Moriyama•Live At Misty•Victor•1979','\
Eden Atwood•There Again•Concord Jazz•1995','\
Louis Armstrong•Satchmo! - A Musical Autobiography Of Louis Armstrong Vol. 3•Brunswick•0','\
Ray Anthony•The Smash Hits Of \'63!•Capitol Records•1964','\
no artist•My Ship•Trio Records•1975','\
Dave Pell Octet•The Dave Pell Octet Plays Today\'s Hits In Jazz•Liberty•1963','\
Lawrence Welk•1963\'s Early Hits•Dot Records•1963','\
Horst Jankowski•A Walk In The Black Forest•Verve Records•2006'),'\
\
In The Midnight Hour\
':('\
Mike Sharpe•The Sharpest Sax•Liberty•1968','\
Betty Carter•Round Midnight•Roulette•1975','\
Teddy Wilson•And Then They Wrote•Columbia•1960','\
Kenny Bernard•Live \'65•Acid Jazz•2011','\
Billy Larkin And The Delegates•Hole In The Wall•World Pacific Records•1965','\
Lou Rawls•Central Park Music Festival•Music Images•0','\
Erskine Hawkins•The Hawk Blows At Midnight•Decca•1961','\
Various•My Fellow Americans - Soundtrack•TVT Soundtrax•1996','\
Coleman Hawkins•The "Hawk" Talks•Decca•1955','\
no artist•Turn On Your Love Light•Hi Records•1968','\
The Total Eclipse (3)•Symphony For Soul•Liberty Records Inc.•1967','\
Various•Soul To Soul•Rhino Home Video•2004','\
Charlie Haden•Come Sunday•Emarcy•2011'),'\
\
In the Wee Small Hours of the Morning\
':('\
Hank Crawford•Brian\'s Song / In The Wee Small Hours Of The Morning•Kudu•1972','\
Frank Sinatra•Strangers In The Night•Reprise Records•1986','\
Julie London•In The Wee Small Hours Of The Morning•Liberty•1960','\
Frank Sinatra•It Never Entered My Mind / In The Wee Small Hours Of The Morning •Capitol Records•1955','\
Art Farmer•Live In Tokyo•King Records•1977','\
Frank Sinatra•Strangers In The Night•Reprise Records•1986','\
Art Blakey & The Jazz Messengers•Caravan•Riverside Records•1962','\
Art Blakey & The Jazz Messengers•Caravan•Riverside Records•1962','\
Tsuyoshi Yamamoto Trio•Daahoud•East Wind•1976','\
Frank Sinatra•In The Wee Small Hours Part 1•Capitol Records•1955','\
Steve Moore (5)•STEBMO•Invada•2009','\
Sadao Watanabe•Sadao Meets Sharps & Flats•RCA•1973'),'\
\
In Walked Bud\
':('\
Art Blakey & The Jazz Messengers•Art Blakey\'s Jazz Messengers With Thelonious Monk•Metronome•1958','\
Art Blakey & The Jazz Messengers•Art Blakey\'s Jazz Messengers With Thelonious Monk•Metronome•1959','\
Steve Lacy Four•Morning Joy (Live At Sunset Paris)•hat ART•1990','\
Art Blakey & The Jazz Messengers•Keystone 3•Concord Jazz•1982','\
Eddie "Lockjaw" Davis•Live! The Midnight Show•Prestige•1964','\
The Thelonious Monk Quartet•Live At The Five Spot Discovery!•Blue Note•1993','\
Don Pullen•Plays Monk•Paddle Wheel•1985','\
Bobby Hutcherson•Good Bait•Landmark Records (3)•1985'),'\
\
In Your Own Quiet Place\
':('\
Gary Burton•Gary Burton & Keith Jarrett•Atlantic•1971','\
Gary Burton•Gary Burton & Keith Jarrett / Gary Burton: Throb•Rhino Records (2)•1994','\
Gary Burton•Turn Of The Century•Atlantic•1976'),'\
\
In Your Own Sweet Way\
':('\
The Miles Davis Quintet•Workin\' With The Miles Davis Quintet•Metronome•1960','\
Chet Baker Trio•Mr. B•Timeless Records (3)•1984','\
Richard Beirach•Elegy For Bill Evans•Trio Records•1981','\
Chet Baker Quartet•In Your Own Sweet Way•Circle Records (2)•1983','\
Danny Thompson Trio•Live 1967•What Disc?•1999','\
Georges Arvanitas Trio•Live Again•Futura Records (2)•1973','\
Chet Baker Trio•Someday My Prince Will Come•SteepleChase•1983','\
Kenny Dorham•Jazz Contemporary•Time Records (3)•1960','\
Sestetto Basso-Valdambrini•The Best Modern Jazz In Italy 1962•RCA Victor•1962','\
Fumio Karashima Trio•Round Midnight•Full House (3)•1983','\
Eiji Nakayama•Sweet View - Live In Japan•Apollon•1988','\
Bill Evans•Alone (Again)•Fantasy•1977','\
Curtis Amy•Tippin\' On Through•Pacific Jazz•1962'),'\
\
Incentive\
':('\
Horace Silver•Silver \'N Voices•Blue Note•1977','\
Horace Silver•Essential Blue -The Classic Of Horace Silver•-Blue Note•2007'),'\
\
Inchworm\
':('\
John Coltrane•European Tour 1962•Le Chant Du Monde•2017','\
John Coltrane•Favorites•Jazz Bird•1980','\
Gene DiNovi•Remembrance•Marshmallow (3)•1992','\
The John Coltrane Quartet•The Complete November 19 1962 Stockholm Concerts•Domino Records (7)•2011','\
John Coltrane•The Complete Graz Concert \'62•Magnetic Records (6)•1992','\
John Coltrane•In A Soulful Mood•Music Club•1994','\
Gina Saputo•Swingin\' On A Star•GSJQ Productions•2003','\
Sheila Jordan•The Crossing•BlackHawk Records•1986','\
Patricia Barber•Cafe Blue•Premonition Records•1994','\
Rachelle Ferrell•First Instrument•Blue Note•1995'),'\
\
Indian Lady\
':('\
The Don Ellis Orchestra•Turkish Bath / Indian Lady•Columbia•1967','\
The Don Ellis Orchestra•Electric Bath•Columbia•1967','\
The Don Ellis Orchestra•Autumn•Columbia•1968','\
Sathima Bea Benjamin•WindSong•Ekapa•1985','\
Chet Baker•Sextet & Quartet•Music•1960','\
Coleman Hawkins•Wrapped Tight•Impulse!•1965'),'\
\
Indian Summer\
':('\
The George Shearing Quintet•Indian Summer / Appreciation•MGM Records•1953','\
Tony Martin (3)•Careless / Indian Summer•Decca•1939','\
Sidney Bechet And His New Orleans Feetwarmers•Indian Summer / Preachin\' Blues•Bluebird (3)•1940','\
Stan Getz Quartet•What\'s New / Indian Summer•Prestige•1951','\
Les Baxter & His Orchestra•Indian Summer / Quiet Village•Capitol Records•1952','\
Mrs. Mills•Candy Floss•Parlophone•1968','\
Glenn Miller And His Orchestra•Careless / Indian Summer•no label•1940','\
Duke Ellington And His Orchestra•Indian Summer / The Jeep Is Jumpin\' •Bethlehem Records•0','\
Tommy Dorsey And His Orchestra•Indian Summer / A Lover Is Blue•Victor•1939','\
The Melachrino Orchestra•Begin The Beguine / Indian Summer•no label•0','\
Wild Bill Davis Trio•Indian Summer / Theme From The Joe Louis Story•Okeh•1953','\
Stan Getz Quartet•Vol.1•Prestige•1949','\
Zoot Sims•Zoot Simms In Hollywood•New Jazz•1954','\
Espen Eriksen Trio•Perfectly Unhappy•Rune Grammofon•2018','\
Eddie Calvert•My Horn Goes Round The World (No. 2)•Columbia•0','\
Chet Baker Quartet•The Lost Holland Concert - September 18 1955•RLR Records•2006'),'\
\
Indiana\
':('\
Various•Hot Versus Cool•MGM Records•1953','\
The Dave Brubeck Trio•Laura / Indiana•Coronet (5)•1949','\
Louis Armstrong•Armstrong And Condon At Newport•Philips•1956','\
no artist•Ostrich Walk / Indiana•Century (13)•1948','\
Harry James And His Orchestra•Indiana / Record Session•Parlophone•1943','\
Original Dixieland Jazz Band•Indiana / Darktown Strutters\' Ball•Columbia•1917','\
Johnny Hodges And His Orchestra•Easy Going Bounce / Indiana•Norgran Records•0','\
Teddy Wilson Trio•You\'re Mine You / Indiana•Metronome•1953','\
Jimmy McGriff•Something To Listen To•Blue Note•1970','\
Lee Konitz•Inside Hi-Fi Vol. 2•Metronome•1957','\
Red Nichols And His Five Pennies•Indiana / Dinah•Brunswick•1929','\
Earl Hines And His Orchestra•Indiana / Ridin\' And Jivin\'•no label•1944','\
Lawrence Welk And His Champagne Music•Mary Ann / Indiana Holiday•Coral•1958'),'\
\
Invitation\
':('\
Hank Crawford•River\'s Invitation•Milestone (4)•1986','\
Pete Terrace Quintet•Dinah / Invitation•Fantasy•1955','\
Joe Loco And His Orchestra•Teenagers\' Wail•Columbia•1955','\
Ernie Andrews•River\'s Invitation Pt. 1 / River\'s Invitation Pt. 2•Tangerine Records•1965','\
Carmen McRae•Invitation / Lo And Behold•Decca•0','\
Joe Henderson•Jazz Patterns•Everest Records Archive Of Folk & Jazz Music•0','\
Joe Henderson•An Evening With•Red Record•1987','\
Dakota Staton•Invitation •Capitol Records•0','\
Chris Connor•Invitation / I Sold My Heart To The Junkman•Atlantic•1960','\
Charles McPherson•Today\'s Man•Mainstream Records•1973','\
Andrew Hill Trio•Invitation•SteepleChase•1975','\
Andrew Hill•Spiral•Arista•1975','\
George Benson•Oleo•Music Mirror•1993','\
The Joanne Brackeen Trio•Invitation•Freedom•1978'),'\
\
Inner Urge\
':('\
Jerry Bergonzi•Lineage•Red Record•1991','\
Joe Henderson•Inner Urge•Blue Note•1965','\
Wallace Roney•Village•Warner Bros. Records•1997','\
Charli Persip And Superband•No Dummies Allowed•Soul Note•1989','\
Sal Nistico•Empty Room•Red Record•1989','\
Gideon Van Gelder•Perpetual•Kindred Spirits•2010','\
Lionel Hampton & His Big Band•Cookin\' In The Kitchen•Jazz Heritage•1992','\
Joe Henderson•Big Band•Verve Records•1996','\
The Blue Note 7•Mosaic: A Celebration Of Blue Note•Blue Note•2009','\
Antonio Sanchez (2)•Migration•C.A.M. Jazz•2007','\
Cyril Achard Trio•Trace•Lion Music•2007'),'\
\
Inside In\
':('\
Markus Stockhausen•Cosi Lontano...Quasi Dentro•ECM Records•1989','\
George Benson•Inside Love (So Personal)•Warner Bros. Records•1983','\
Keith Jarrett / Gary Peacock / Jack DeJohnette•Inside Out•ECM Records•2001','\
Han Bennink Trio•Bennink & Co.•ILK Music•2013','\
The Jonah Jones Quartet•Jonah Jumps Again•Capitol Records•1959','\
Marlon Jordan Quintet•Learson\'s Return•Columbia•1991','\
Umberto Fiorentino•Inside Colors•Platinum (8)•2002','\
Gerald Albright•Bermuda Nights•Atlantic•1988','\
Count Basie Orchestra•Inside Basie Outside•VSP•1966','\
Andreas Loven•District Six•Losen Records•2016','\
Jay Zelenka•Circle•Freedonia Music•2017','\
Yoshiaki Masuo•Good Morning•Electric Bird•1979','\
James Moody•Something Special•Novus•1986','\
Gary Burton•Hotel Hello•ECM Records•1975','\
Antonio Faraò•Black Inside•Enja Records•1999'),'\
\
Interplay\
':('\
Idrees Sulieman•Interplay For 2 Trumpets And 2 Tenors•Prestige•1957','\
Paul Bley Quartet•The Paul Bley Quartet•ECM Records•1988','\
ICP Orchestra•Live Soncino•Instant Composers Pool•1979','\
Miroslav Vitous Group•Miroslav Vitous Group•ECM Records•1981','\
John Coltrane•Dakar•Prestige•1981','\
John Coltrane•Dakar•Prestige•1981','\
Atmosfear•En Trance•MCA Records•1981','\
Giorgio Azzolini•What\'s Happening?•Juke Box•1966','\
Bill Evans•Peace Pieces•Riverside Records•1969','\
M. Sasaji & L.A. Allstars•Birdland•Columbia•2000','\
Uli Beckerhoff•Stay•NABEL•1989','\
Herbie Mann•Peace Pieces - The Music Of Bill Evans•Kokopelli Records•1995','\
RQ•Solid Ground•Blu Mar Ten Music•2018','\
John Coltrane•Jazz Interplay•Prestige•1964'),'\
\
Intrepid Fox\
':('\
Kazumi Odagiri Trio•突撃神風特攻隊•no label•1976','\
Freddie Hubbard•Hot Horn•Imagem•1984','\
Don Sebesky•Full Cycle•Paddle Wheel•1983','\
Various•Aurex Jazz Festival (1980): Jazz At The 80\'s•Eastworld•1980','\
Freddie Hubbard•Red Clay•CTI Records•1970','\
Freddie Hubbard•A Little Night Music•Fantasy•1983','\
The Essence All Stars•Hub Art - A Celebration Of The Music Of Freddie Hubbard•Hip Bop Essence•1995','\
Freddie Hubbard•Pinnacle Live & Unreleased From Keystone Korner•Resonance Records•2011','\
Freddie Hubbard•Jazz Moods - Hot•Legacy•2004','\
Various•¡Con Mucho Ritmo! - The Very Best Of TropiJazz•TropiJazz•2005'),'\
\
Invitation\
':('\
Hank Crawford•River\'s Invitation•Milestone (4)•1986','\
Pete Terrace Quintet•Dinah / Invitation•Fantasy•1955','\
Joe Loco And His Orchestra•Teenagers\' Wail•Columbia•1955','\
Ernie Andrews•River\'s Invitation Pt. 1 / River\'s Invitation Pt. 2•Tangerine Records•1965','\
Carmen McRae•Invitation / Lo And Behold•Decca•0','\
Joe Henderson•Jazz Patterns•Everest Records Archive Of Folk & Jazz Music•0','\
Joe Henderson•An Evening With•Red Record•1987','\
Chris Connor•Invitation / I Sold My Heart To The Junkman•Atlantic•1960','\
Charles McPherson•Today\'s Man•Mainstream Records•1973','\
The Joanne Brackeen Trio•Invitation•Freedom•1978','\
Andrew Hill Trio•Invitation•SteepleChase•1975','\
Andrew Hill•Spiral•Arista•1975','\
George Benson•Oleo•Music Mirror•1993'),'\
\
Iris\
':('\
Miles Davis•E.S.P.•Columbia•1965','\
The Joanne Brackeen Trio•Invitation•Freedom•1978','\
Shampoo Meuchiine•Iris•Not On Label (Pascal Maupeu Self-released)•2014','\
Naïm Amor•Soundtracks•FILMguerrero•2001','\
John Coltrane•Stellar Regions•Impulse!•1995'),'\
\
Is It Really True?\
':('\
Ann Margret•3 Great Girls•RCA•1963','\
Nappy Brown•Don\'t Be Angry!•Savoy Jazz•1984','\
Various•Broken Hearted•Musicbank•2003','\
Various•The Best Of 1980-1990•EMI•1990','\
Various•Rock Era - Love Songs•Wisepack Ltd.•1991','\
Burt Bacharach•The Look Of Love - The Burt Bacharach Collection•Warner Strategic Marketing•2001','\
Various•Mood Music From The Movies•no label•1971','\
Various•We Remember Them Well•no label•1986','\
Elvis Presley•Walk A Mile In My Shoes - The Essential 70\'s Masters•RCA•1995','\
Burt Bacharach•Anyone Who Had A Heart : The Art Of The Songwriter•Universal Music Group International•2013','\
Elvis Presley•20 Original Albums•RCA•2012'),'\
\
Isfahan\
':('\
Lee Konitz•Creative Music Studio - Woodstock Jazz Festival 1•Douglas Music•1997','\
The John Bunch Quintet•John\'s Bunch•Famous Door•1975','\
Art Farmer•Something To Live For (The Music Of Billy Strayhorn)•Contemporary Records•1987','\
Gary Burton Quartet•Easy As Pie•ECM Records•1981','\
Mike Wofford Quartet•Funkallero•Trend (3)•1988','\
Nico Niquo•Timeless•Daisart•2018','\
Trio65•Vol.1 Music By Billy Strayhorn•NuJazzCity•2000','\
John Heard•Heard Ranier Ferguson•ITI Records•1983','\
Sphere (16)•Sphere•Verve Records•1998','\
Han Bennink Trio•Parken•ILK Music•2009'),'\
\
Island\
':('\
Akira Sakata•Pochi•Better Days (2)•1980','\
Spill (6)•Stereo•corvo records•2018','\
Michael Franks•Island Life•Warner Bros. Records•1987','\
The Andrews Sisters•Winter Wonderland / Christmas Island•Decca•1946','\
Flip Phillips And His Orchestra•Long Island Boogie / Stardust•Clef Records•1954','\
Tom Scott•Rock Island Rocket / Refried•Ode Records (2)•1975','\
Stan Getz Quartet•Long Island Sound / Mar-Cia•New Jazz•1949','\
Monday Michiru•Introspection•Polydor•2000','\
no artist•Coney Island Washboard / Wolverine Blues•Good Time Jazz•1955','\
David Sanborn•So Far Away•Reprise Records•1988','\
Earl Bostic And His Orchestra•Song Of The Islands / Liebestraum•Parlophone•1954','\
Ray Turner•The Entertainer\'s Rag / Rock Island Rag•Capitol Records•1950','\
Harry Belafonte•Island In The Sun•RCA•1958','\
Johnny B (2)•Mare Island Holiday / Del Rocco Rag•Not On Label•1980'),'\
\
Island Birdie\
':('\
Elvin Jones•In Europe•Enja Records•1992','\
McCoy Tyner•Port Au Blues•Past Perfect Silver Line•2000','\
McCoy Tyner•Looking Out•Columbia•1982','\
McCoy Tyner•Live At The Musicians Exchange Cafe•no label•1988'),'\
\
Isn\'t It A Pity\
':('\
Mel Tormé•Nothing Without You•Concord Jazz•1992'),'\
\
Isn\'t It Romantic\
':('\
Cal Tjader•Vibist•Quality Records Limited•1954','\
The Eddie Higgins Trio•Haunted Heart•Venus Records (5)•1997','\
Various•Rodgers & Hart Gems•Pacific Jazz•1992'),'\
\
Isoar\
':('\
Nguyên Lê•Zanzibar•EmArcy•2006'),'\
\
Isotope\
':('\
Kosuke Mine Quintet•Mine•Three Blind Mice•1970','\
Kirk Lightsey Trio•Isotope•Criss Cross Jazz•1983','\
Kazumi Watanabe•Infinite•Express•1971','\
George Otsuka Quintet•Go On\'•Three Blind Mice•1972','\
Joe Henderson•The State Of The Tenor • Live At The Village Vanguard • Volume 1•Blue Note•1986','\
Joe Henderson•Inner Urge•Blue Note•1965','\
Joe Henderson•Big Band•Verve Records•1996'),'\
\
Israel\
':('\
Miles Davis And His Orchestra•Boplicity / Israel•Capitol Records•1949','\
Miles Davis•Classics In Jazz Part 2•Capitol Records•1954','\
Ack Van Rooyen•Homeward•Mood Records•1982','\
Giorgio Azzolini•Crucial Moment•Car Juke Box•1968','\
Phil Woods•Chasin\' The Bird•Venus Records (5)•1998','\
Toshiko Akiyoshi•Toshiko And Modern Jazz•Columbia•1977','\
Toshiko Mariano And Her Big Band•Jazz In Japan Recorded In Tokyo•Vee Jay Records•1965','\
Miles Davis•Classics In Jazz •Capitol Records•1954','\
Gene Krupa And His Chicagoans•Chicago Style•Parlophone•0'),'\
\
It Ain\'t Necessarily So\
':('\
Hash Brown And His Ignunt Strings•The Hash Brown Sounds•Philips•1962','\
Various•Back To Black•Lo Recordings•2005','\
Jamie Cullum•Devil May Care!•Candid•2010','\
Gilles Peterson•Magic Peterson Sunshine•Edel Records•2016','\
The Amazing Keystone Big Band•We Love Ella.•nome•2018','\
Carol Kidd•Crazy For Gershwin•Linn Records•1994','\
Brian Auger•Back To The Beginning...Again: The Brian Auger Anthology Volume 2•Freestyle Records (2)•2016','\
Various•We Remember Them Well•no label•1986','\
Various•Airs Célèbres Du Monde Entier•no label•1965'),'\
\
It Always Is\
':('\
Oscar Peterson•Plays Irving Berlin•Mercury•1954','\
Tom Harrell•Sail Away•Contemporary Records•1989','\
Sonny Stitt•The Last Stitt Sessions Vol. 1•Muse Records•1983','\
Sammy Kaye•Sammy Kaye Plays Irving Berlin For Dancing•RCA Victor•0','\
Roland Kirk•Hip!•Fontana•1965','\
Lena Horne•Sometimes I\'m Happy•MGM Records•0','\
Teresa Brewer•American Music Box Vol. 1 - The Songs Of Irving Berlin•Doctor Jazz•1987','\
Betty Carter•Betty Carter•Bet-Car Productions•1976','\
Burt Bacharach•At This Time•Columbia•0','\
Chieli Minucci•Got It Goin\' On!•Shanachie•2005','\
Ernie Freeman•Ernie Freeman Plays Irving Berlin•Imperial•1956','\
Jack Say Orchestra And Chorus•The Girl That I Marry (The Music Of Irving Berlin)•RCA Camden•1959','\
Chet Baker•My Funny Valentine•Pacific Jazz•1994','\
The Keef Hartley Band•Seventy Second Brave•Deram•1972','\
Al Jolson•The Jolson Story - Among My Souvenirs•Brunswick•1957','\
Wayne King And His Orchestra•Wayne King Plays Irving Berlin Melodies•RCA Victor•1952','\
Sonny Stitt•The Last Stitt Sessions Vol. 1 & 2•Muse Records•1984','\
Victor Young And His Singing Strings•Say It With Music (Irving Berlin Compostions)•Decca•0'),'\
\
It Could Happen To You\
':('\
Ahmad Jamal•Excerpts From The Blues / It Could Happen To You•Parrot (2)•1955','\
Dinah Washington•It Could Happen To You•Mercury•1960','\
Eje Thelins Kvintett•So Far•Columbia•1963','\
Warne Marsh•Report Of The 1st Annual Symposium On Relaxed Improvisation•Revelation Records (3)•1973','\
The J.J. Johnson Sextet•Jay Jay Johnson•Blue Note•1953','\
Brew Moore•No More Brew•Storyville•1981','\
Dakota Staton•Dynamic! Part 2•Capitol Records•1958','\
Jackie McLean Quintet•Jackie\'s Pal•Prestige•1956','\
The Kenny Dorham Quintet•Scandia Skies•SteepleChase•1980','\
The Miles Davis Quintet•Relaxin\' With The Miles Davis Quintet•Prestige•1958','\
Ryo Fukui•Scenery•Nadja•1976','\
Miles Davis•If I Were A Bell•Pilz•1993'),'\
\
It Don\'t Mean a Thing\
':('\
Mel Tormé•In Concert Tokyo•Concord Records•1989','\
Stuff Smith•Violin-Summit•SABA•1967','\
Various•Guitar And Bass•Verve Records•1991','\
Ernestine Anderson•My Kinda Swing•Mercury•1960','\
Jacques Doudelle•Jazzouillis Orchestra•Not-On-Label (Jacques Doudelle Self-Released)•1986','\
Louis Armstrong•Recording Together For The First Time / The Great Reunion Of Louis Armstrong And Duke Ellington•Mobile Fidelity Sound Lab•0','\
Ella Fitzgerald•Live in Cologne 1974•Jazzline•2016','\
Johnny Guarnieri•The Duke Again•Coral•1957'),'\
\
It Had To Be You\
':('\
Artie Shaw And His Orchestra•It Had To Be You / If I Had You•Victor•1941','\
Artie Shaw And His Orchestra•Jungle Drums / It Had To Be You•Bluebird (3)•1938','\
Isham Jones Orchestra•It Had To Be You / After The Storm•Brunswick•1924','\
Martha Love•When They Ask About You / It Had To Be You•Decca•0','\
Nelson Riddle•It Had To Be You•Paramount Records•1974','\
Julie London•It Had To Be You / Saddle The Wind•London American Recordings•0','\
Dinah Shore•Whatever Lola Wants / It Had To Be You•RCA Italiana•0','\
Harry Connick Jr.•Recipe For Love / It Had To Be You•Columbia•1991','\
Coleman Hawkins And His Orchestra•Body And Soul / It Had To Be You•Bluebird (3)•1944','\
Harry Roy And His Band•Barrel House Boogie / It Had To Be You•Decca•1945','\
Harry Connick Jr.•It Had To Be You•CBS•1989','\
Jimmie Lunceford And His Orchestra•It Had To Be You / Keep Smilin\' Keep Laughin\' Be Happy•Decca•0','\
Count Basie Orchestra•It Had To Be You / How Am I To Know•Roulette•1960','\
Various•Jazz City Presents...•Bethlehem Records•1957','\
Billy Cotton•Broken Toys•Columbia•1961','\
Ben Light•I\'ll Get By / It Had To Be You•Tempo (7)•0','\
Bing Crosby•Granada / It Had To Be You•Decca•1953'),'\
\
It Happens Every Day\
':('\
Hubert Laws•Love Gets Better•Columbia•1978','\
Hubert Laws•Say It With Silence•Columbia•1978','\
The Vindonissa Jazz Orchestra•Soul Lady•Activ-Records•1975','\
Flavornaughts•Flavornaughts•NINEBARecords•1996','\
Bobby Scott•The Compleat Musician•Atlantic•1960','\
Di Philipi•You Must Have Dreamt It•Not On Label (Didier Jean Self-released)•2004','\
Santo & Johnny•I Grandi Successi Originali•Sony Music•2009','\
Sarah Vaughan•American Singer•Book-Of-The-Month Records•1980','\
Frank Sinatra•The Columbia Years 1943-1952: The Complete Recordings•Columbia•1993','\
Frank Sinatra•The Capitol Years•Capitol Records•1984','\
Frank Sinatra•Concepts•Capitol Records•1992','\
Various•Singers And Soloists Of The Swing Bands•Smithsonian Collection•1987'),'\
\
It Might As Well Be Spring\
':('\
Richard "Groove" Holmes•This Here / It Might As Well Be Spring•Pacific Jazz•1967','\
Ralph Burns And His Ensemble•Spring Sequence•Period Records•1955','\
Ray Conniff & His Orchestra•Hollywood In Rhythm No. 1•Philips•1960','\
Stan Getz•It Might As Well Be Spring / The Song Is You•Royal Roost•1951','\
Kenny Dorham Septet•Blue Spring•Riverside Records•1959','\
Sarah Vaughan•You Go To My Head / It Might As Well Be Spring•Crown Records (31)•1947','\
Sammy Kaye•It Might As Well Be Spring / Give Me The Simple Life•Victor•1945','\
Paul Weston And His Orchestra•How Deep Is The Ocean / It Might As Well Be Spring•Capitol Records•1945','\
no artist•Groove Blues•Prestige•1961','\
Ralph Moore Quintet•Rejuvenate!•Criss Cross Jazz•1989','\
Shirley Bassey•Till - And Other Great Songs•Columbia•1962','\
Nina Simone•Children Go Where I Send You / It Might As Well Be Spring•Pye Records•1959','\
Sonny Stitt•Dumpy Mama•Flying Dutchman•1975','\
Lucio Dalla•Lucio Dalla Marco Di Marco•Fonit Cetra•1985','\
Herb Geller•Stax Of Sax•Jubilee•1958','\
Stan Getz•The Complete Roost Session Vol. 2•Royal Roost•1981','\
Julian Priester Sextet•Spiritsville•JAZZLAND•1960','\
Michael Moore Quartet•Easter Sunday•Ramboy Recordings•2011'),'\
\
It Never Entered My Mind\
':('\
The Miles Davis Quartet•It Never Entered My Mind•Prestige•0','\
Bill Henderson (3)•Sleepy / It Never Entered My Mind•Vee Jay Records•1960','\
Stan Getz•At The Opera House•Karusell•1958','\
The Miles Davis Quintet•Workin\' With The Miles Davis Quintet•Metronome•1960','\
Linda Ronstadt•When I Fall In Love•Asylum Records•1985','\
Miles Davis•Live In New York•Bandstand•1987','\
Frank Sinatra•It Never Entered My Mind / In The Wee Small Hours Of The Morning •Capitol Records•1955','\
Stan Getz•At The Opera House•Verve Records•1957','\
Ella Fitzgerald•Ella Fitzgerald Sings The Rodgers And Hart Song Book (Part 7)•Verve Records•0'),'\
\
I\'t the Talk of the Town\
':('\
Marty Grosz Quartet•Just For Fun!•Nagel Heyer Records•1997','\
Jackie Davis•Jumping Hi-Fi Hammond•Jasmine Records•2008','\
Elvis Presley•Walk A Mile In My Shoes - The Essential 70\'s Masters•RCA•1995','\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014','\
Roland Kirk•Rahsaan: The Complete Mercury Recordings Of Roland Kirk•Mercury•1990','\
Various•Les Triomphes Du Jazz•Habana•2000'),'\
\
It Was A Very Good Year\
':('\
Della Reese•It Was A Very Good Year / Solitary Woman•ABC Records•1966','\
The Three Sounds•The Frown / It Was A Very Good Year•Blue Note•1966','\
Ray Bryant Trio•Gotta Travel On•Cadet•1966','\
Della Reese•It Was A Very Good Year / I Had To Know My Way Around•Stateside•1968','\
Frank Sinatra•Main Theme From "The Cardinal" (Stay With Me) / It Was A Very Good Year•Reprise Records•0','\
Earl Grant•If I Only Had Time (Je N\'Aurai Pas Le Temps)•Decca•0','\
Eddie Harris•Mean Greens•Atlantic•1966','\
Marlena Shaw•Take A Bite•Columbia•1979','\
Larry Ridley•Sum Of The Parts•Strata-East•1975','\
Phil Palumbo and Pals•Phil Palumbo and His Pals•PAP Records•0','\
Trudy Pitts•Introducing The Fabulous Trudy Pitts•Prestige•1967','\
Toshiko Akiyoshi•Solo Piano•RCA•1975','\
The Howard Roberts Quartet•All-Time Greatest Instrumental Hits•Capitol Records•1967'),'\
\
It\'s a Raggy Waltz\
':('\
The New Brubeck Quartet•Live At Montreux•Tomato•1978','\
Dave Brubeck•Greatest Hits•Companion•0','\
Dave Brubeck•Dave Brubeck Collection•CBS Records Australia Limited•1980','\
Barbara Moore•A Little Moore Barbara•CBS•1967','\
Dave Brubeck•Dave Brubeck\'s All-Time Greatest Hits•CBS•1974','\
Various•Les Plus Grands Moments Du Jazz•CBS•1989','\
The Dave Brubeck Quartet•The Columbia Studio Albums Collection 1955-1966•Columbia•2012','\
Various•Jazz Stars - Jazz Classics•CBS Special Products•1977'),'\
\
It\'s All Right With Me\
':('\
Frank Sinatra•Mack The Knife•Qwest Records•1984','\
Ella Fitzgerald•Ella Fitzgerald Sings The Cole Porter Song Book•Verve Records•0','\
Bernard Peiffer•Bernard Peiffer Plays Cole Porter\'s Can-Can•Laurie Records•1960','\
Chris Connor•This Is Chris•Bethlehem Records•1955','\
Art Farmer•Meet The Jazztet•Argo (6)•1960','\
Laila Dalseth Quintet•Daydreams•Hot Club Records•1984','\
Brad Mehldau•Live In Marciac•Nonesuch•2011','\
Oscar Peterson•Oscar Peterson•Supraphon•1972','\
Evans Bradshaw Trio•Pieces Of Eighty-Eight•Riverside Records•1959','\
Ella Fitzgerald•Ella Fitzgerald At The Montreux Jazz Festival 1975•Pablo Records Original Jazz Classics Fantasy•1993','\
Wild Bill Davis•Flying Home•Sunset Records•1968'),'\
\
It\'s De-Lovely\
':('\
Marian McPartland Quintet•It’s De-Lovely / Flamingo•Federal (5)•0','\
Bob Cooper•Shifting Winds•Capitol Records•1955','\
Syd Lawrence And His Orchestra•This Is A Lovely Way To Spend An Evening•Philips•1974','\
Ted Coleman Band•Taking Care Of Business•JSR Records•1980','\
Carlos Barbosa-Lima•Plays The Music Of Luiz Bonfá And Cole Porter•Concord Concerto•1984','\
Stanley Black•Plays For Latin Lovers•Decca•1957','\
Various•The Dance Band Years - The 1930\'s•Saville Records•0','\
Various•Concord Jazz Guitar Collection - Volumes 1 And 2•Concord Jazz•1987','\
Ella Fitzgerald•Ella Fitzgerald\'s Tribute To Cole Porter•Verve Records•1964','\
Various•Jazz Legends: Classic Song Books•Universal•2004','\
Minus 8•Minuit•Compost Records•2002','\
Dick Haymes•Classic Years•Pegasus•2000'),'\
\
It\'s Magic\
':('\
Scott Colley•The Magic Line•Arabesque Jazz•2000','\
Ella Fitzgerald•Sweet And Hot Part 1•Brunswick•0','\
Charisse & Moffett Family Jazz Band•It\'s Luv•Venus Records (5)•1995','\
Grover Washington Jr.•At His Best•Motown•1985','\
Grover Washington Jr.•Mister Magic / Feels So Good•Motown•1986','\
Nat King Cole•Thank You Pretty Baby•Capitol Records•1967','\
Spiral Deluxe•Voodoo Magic•Axis•2018','\
Drum Circus•Magic Theatre•Garden Of Delights•2003','\
Larry Carlton•Deep Into It•Warner Bros. Records•2001','\
Vassilis Tsabropoulos•Images•Lyra•1992','\
Bobby Enriquez•Live In Tokyo Volume II•GNP Crescendo•1984','\
Doris Day•Sunset Boulevarde•Coronet (2)•0','\
The Paul Smith Ensemble•Carnival! In Percussion•Verve Records•1961','\
The Michel Petrucciani Trio•Live At The Village Vanguard•Concord Jazz•1985','\
Grover Washington Jr.•Greatest Performances•Motown•1983','\
Esquivel And His Orchestra•Other Worlds Other Sounds•RCA Victor•1961'),'\
\
It\'s Only a Paper Moon\
':('\
Frans Poptie And His Swing Specials•Swing Specialities No. 1•Fontana•1957','\
The Nat King Cole Trio•After Midnight Part 4•Capitol Records•1957','\
Bennie Wallace•Bennie Wallace In Berlin•Enja Records•2001','\
Miles Davis•The Unique - Vol. 2•Giants Of Jazz•1986','\
Stéphane Grappelli•Steph \'N\' Us•Cherry Pie•1977','\
Wild Bill Davis•In Atlantic City•RCA Victor•1967','\
Frans Poptie•Swing Specialities•Philips•1958','\
Stéphane Grappelli•Vintage 1981•Concord Jazz•1981','\
Johnny Hodges•In A Mellotone•Bluebird (3)•1990','\
Unknown Artist•Now Dig This! / Jazz In 2 Keys•Music Minus One•0','\
Enrique Villegas•Tributo A Monk•Trova•1967','\
Oliver Jones (5)•The Many Moods Of Oliver Jones•Justin Time•1984'),'\
\
It\'s You\
':('\
Citizen Swing•Cure Me With The Groove•Macola Record Co.•1992','\
Larry Carlton•Deep Into It•Warner Bros. Records•2001','\
Stefano Bollani Trio•Black And Tan Fantasy•Venus Records (5)•2003','\
Fats Waller & His Rhythm•Oh Baby Sweet Baby / You Asked For It - You Got It  •no label•1943','\
Carol Sloane•But Not For Me•CBS/Sony•1987','\
Ella Fitzgerald•(If You Can\'t Sing It) You\'ll Have To Swing It•Decca•1952','\
The Style Council•Have You Ever Had It Blue•Polydor•1986','\
Hi-Force•Can U Feel It Baby•Polydor•1992','\
Cal Tjader•Vibist•Quality Records Limited•1954','\
Walt Dickerson Trio•To My Son•Steeplechase•1980','\
Don Elliott•At The Modern Jazz Room•ABC-Paramount•1958','\
Dexter Gordon•North Sea Jazz Legendary Concerts•Bob City•2013','\
Billy Harper•The Believer•Baystate•1980','\
Miles Perkin Quartet•The Point In Question•Clean Feed•2019','\
Martha Love•When They Ask About You / It Had To Be You•Decca•0','\
Artie Shaw And His Orchestra•Connecticut / Don\'t You Believe It Dear•Musicraft•1946','\
Martha Love•When They Ask About You / It Had To Be You•Decca•0','\
Frank Sinatra•Sing And Dance No. 2 With Frank Sinatra•Philips•0','\
Jason Roebke•Rapid Croche•482 Music•2003','\
Erroll Garner•Garner Gone Gonest•Philips•0','\
The Crusaders•The Good And Bad Times•MCA Records•1986','\
Everette Harp•For The Love•Blue Note•2000','\
Kid Thomas Valentine•Red Wing•Jazz Crusade•1966','\
Frank Sinatra•La Voce Un Mito•Cobra Record•1972','\
Roland Kirk•Hip!•Fontana•1965','\
Mitchel Forman•Only A Memory•Soul Note•1983','\
Various•France\'s Concert Anthology Vol. 1 (Live In Paris - Antibes - Nice)•no label•1989','\
Artie Shaw And His Orchestra•It Had To Be You / If I Had You•Victor•1941','\
Stanley Turrentine•Let It Go•Impulse!•1966','\
Sarah Vaughan•Bluesette / You Got It Made•Mercury•1964'),'\
\
It\'s You Or No One\
':('\
Dexter Gordon•North Sea Jazz Legendary Concerts•Bob City•2013Earl Coleman•Returns•Prestige•1956','\
Cal Tjader•Vibist•Quality Records Limited•1954','\
Stefano Bollani Trio•Black And Tan Fantasy•Venus Records (5)•2003','\
J.J. Johnson•The Eminent Jay Jay Johnson Vol. 2•Blue Note•1955','\
Various•Dazzling Jazz - Modern•Philips•0','\
Chas Burchell•Unsung Hero − The Undiscovered Genius Of Chas Burchell•In+Out Records•1994','\
George Shearing•Piano•Concord Jazz•1990','\
Ahmad Jamal Trio•Jamal At The Pershing Vol. 2•Argo (6)•1961','\
Eden Atwood•No One Ever Tells You•Concord Jazz•1993','\
Cal Tjader•Good Vibes•Savoy Jazz•1989','\
J.J. Johnson•Let\'s Hang Out•Verve Records•1993','\
Various•Fire Into Music•CTI Records•1976','\
Duke Ellington And His Orchestra•The Uncollected Duke Ellington And His Orchestra Volume 2 - 1946•Hindsight Records (2)•1978','\
Don Nelson (2)•The Wind•Mode Records•1957','\
Tal Farlow•Tal Farlow•Verve Records•1995','\
Susie Arioli•Night Lights•Spectra Musique•2008','\
Ian Shaw (2)•In A New York Minute•Milestone (4)•1999','\
Johnny Smith•Plus The Trio•Roost•1960'),'\
\
I\'ve Found a New Baby\
':('\
The River Boat Five•On A Swinging Date•Mercury•1960','\
Squirrel Nut Zippers•The Inevitable•Mammoth Records•1995','\
Nat King Cole•Nat King Cole•Giants Of Jazz•1986','\
Sidney Bechet•Petite Fleur•Not On Label•2001'),'\
\
I\'ve Got A Crush On You\
':('\
Carol Kidd•Crazy For Gershwin•Linn Records•1994','\
Tony Bennett•Love Is Here To Stay•Verve Records•2018','\
Frank Sinatra•Best of Duets•Capitol Records•2013','\
Ella Fitzgerald•Ella Fitzgerald•Nocturne•2003'),'\
\
I\'ve Got the World on a String\
':('\
"Hot Lips" Page Sextet•Trumpet Time•Jazztone (2)•1955','\
Dr. John•Ske-Dat-De-Dat The Spirit Of Satch•Concord Records•2014','\
Patrick Williams•Sinatraland•EMI-Capitol Entertainment Properties•1998','\
Sarah Vaughan•The Magic Of Sarah Vaughan•Mercury•1959','\
Ella Fitzgerald•Lo Mejor De Ella Fitzgerald. Vol. II•Coral•1970','\
Bob Shreve•Good Ole’ Bob Doing His Thing•King Records (3)•1970','\
Ella Fitzgerald•Ella Fitzgerald•Nocturne•2003','\
Metropole Orchestra•Metro\'s Midnight Music - Rare Jazz Tracks From The Dutch No\'s Radio Show 1970 - 75•Sonorama•2006','\
Ella Fitzgerald•All My Life•Le Chant Du Monde•2010','\
The Big Ben Banjo Band•Strummin\' On The Old Banjo•Jasmine Records•2017','\
Various•We Remember Them Well•no label•1986'),'\
\
I\'ve Got You Under My Skin\
':('\
Asako Toki•Standards On The Sofa•LD&K•2004','\
Frank Sinatra•Best of Duets•Capitol Records•2013','\
Patrick Williams•Sinatraland•EMI-Capitol Entertainment Properties•1998','\
Fred Waring & The Pennsylvanians•Fred Waring Music-Cole Porter Songs•Decca•1949','\
Stan Getz•Intoit•Past Perfect Silver Line•0','\
Frank Sinatra•La Voz En Argentina•Reprise Records•1981','\
Frank Sinatra•The Very Best Of•Magic Records•2015'),'\
\
I\'ve Never Been in Love Before\
':('\
Harry Connick Jr.•In Concert On Broadway•Columbia•2011','\
Various•More Piano Favourites•Hallmark Music & Entertainment•1999'),'\
\
Jackie\
':('\
Bossa Nostra•Voyage To Brazilia•Irma•2000','\
Don Byas•A Tribute To Cannonball•Columbia•1979','\
Acting Seven•Babel•KKM Records•1988','\
Jean-Michel Pilc•Live At Iridium New-York•Dreyfus Jazz•2005','\
Thelonious Monk•Hackensack•Drive (3)•1989','\
Charles Mingus Jazz Workshop•Pithecanthropus Erectus•Atlantic•1956','\
Rodney Franklin•Windy City•Columbia•1980','\
Thelonious Monk•Blue Monk•Jazz Hour•1989'),'\
\
Jaco\
':('\
Jaco Pastorius Big Band•Word Of Mouth Revisited•Heads Up International•2003','\
Jaco Pastorius•Pastorius / Metheny / Ditmas / Bley•Improvising Artists Inc.•1976','\
Pat Metheny Group•Clouds•Paradise (12)•1991','\
Herbie Hancock•Live Voyage•Not On Label (Herbie Hancock)•2006','\
Pat Metheny Group•Pat Metheny Group•ECM Records•1978','\
Tony Darren•Sun Song•Telarc•1998'),'\
\
Jacob\'s Ladder\
':('\
Eastern Rebellion•Just One Of Those...Nights At The Village Vanguard•MusicMasters Jazz•1995'),'\
\
Je Ne Sais Pas\
':('\
Jean-Pierre Mas•Rue De Lourmel•Owl Records (4)•1977','\
Lionel Hampton•Verve Jazz Masters 26•Verve Records•1994','\
Léo Denis•Trompette Succes Vol. 2 •Tournesol•0','\
Lionel Hampton•Verve Jazz No. 13•Metro Records•0','\
Lionel Hampton•Verve Jazz No. 13•Metro Records•0','\
no artist•Tu Ne Sais Pas / Je Reviens Vers Le Bonheur / Fich\' Le Camp Jack / Sexy Twist•La Voix De Son Maître•1962','\
Lionel Hampton•Lionel Hampton•Verve Records•1987','\
Line Renaud•Line Renaud Y Orquesta•Pathé•1954','\
Madeleyne Cross•J\'Aimerais Tellement Ça•RCA Victor•0','\
Various•Crazy! Time Vol. 34 - Crazy! Acid Jazz•New Sounds Multimedia•1995','\
Salt (19)•La Solution•Agogo Records•2014','\
Dany Brillant•Dolce Vita•Columbia•2001'),'\
\
Jean De Fleur\
':('\
Grant Green•Idle Moments•Blue Note•1964','\
no artist•Onesime Grosbois E Il Suo Pianoforte D\'Occasione•Columbia•1956','\
Grant Green•Street Funk & Jazz Grooves (The Best Of Grant Green)•Blue Note•1993','\
Aimable•50 Ans De Succes D\'accordeon•Disques Vogue•0','\
Various•Les Chansons De L\'Occupation•no label•0'),'\
\
Jeannine\
':('\
The Cannonball Adderley Quintet•Jeannine•Riverside Records•1960','\
The Plaza Band•Sweet Sue - Just You / Jeannine  •Edison Bell Radio•1929','\
Donald Byrd•At The Half Note Cafe Vol. 2•Blue Note•1963','\
Earl Bostic And His Orchestra•Josephine•King Records (3)•1957','\
Various•Blue Bop•Blue Note•1986','\
Duke Pearson•Angel Eyes•Polydor•1968'),'\
\
Jelly Roll\
':('\
Lionel Hampton And His Orchestra•Jelly Roll•Brunswick•0','\
The Mezzrow-Bechet Quintet•Gone Away Blues / Jelly Roll•Royal Jazz (2)•0','\
Lonnie Johnson (2)•Drunk Again / Jelly Roll Baker•King Records (3)•0','\
no artist•Doctor Jazz Stomp / Jelly Roll Blues•no label•1949','\
Bunny Berigan & His Orchestra•Jelly-Roll Blues / \'Deed I Do•Victor•1939','\
Sidney Bechet And His Blue Note Jazz Men•Jelly Roll / I\'ve Found A New Baby•Vogue Records•0','\
Lu Watters And The Yerba Buena Jazz Band•At A Georgia Camp Meeting / Original Jelly Roll Blues•Melodisc (3)•0','\
Louis Armstrong•Frankie And Jhonny•Visadisc•0','\
Lazy Ade And His Late Hour Boys•Hiawatha •Swaggie Records•1956','\
Stanley Clarke•Jamaican Boy•Nemperor Records•1979','\
Ade Monsbourgh•Recorder In Ragtime•Swaggie Records•1956','\
Joe "Fingers" Carr•Mister Ragtime part 2•Capitol Records•1956','\
Charles Mingus•Jazz Gallery: Charles Mingus•Philips•1959','\
Lawson-Haggart Jazz Band•JellyRoll\'s Jazz No 1•Decca•1957','\
Stanley Clarke•Slow Dance•Epic•1978','\
Donald Byrd•Slow Drag•Blue Note•1968','\
Jelly Roll Morton•A Treasury Of Immortal Performances•RCA Victor•1952','\
Jelly Roll Morton•A Treasury Of Immortal Performances•RCA Victor•1952','\
Gannets•Transmissions Of Not•Babel•2012','\
Art Hodes•Pagin\' Mr. Jelly•Candid•1989'),'\
\
Jersey Bounce\
':('\
Jimmy Dorsey And His Orchestra•Jersey Bounce / My Little Cousin•Decca•1942','\
Benny Goodman And His Orchestra•Jersey Bounce / A String Of Pearls•Columbia•1948','\
Milt Herth And His Trio•Jersey Bounce / Pennsylvania Polka•Decca•1942','\
Jan Savitt And His Top Hatters•Always In My Heart / Jersey Bounce•Victor•1942','\
Enoch Light And The Light Brigade•Jersey Bounce / Tuxedo Junction•Project 3 Total Sound•0','\
The Benny Goodman Quartet•The Benny Goodman Story Volume 2 Part 2•Brunswick•1956','\
Enoch Light And The Light Brigade•Jersey Bounce / Tuxedo Junction•Project 3 Total Sound•0','\
Benny Goodman And His Orchestra•Jersey Bounce / A String Of Pearls•Okeh•1942','\
Earl Hines And His Orchestra•Jersey Bounce / Sally Won\'t You Come Back•Bluebird (3)•1941','\
Benny Goodman And His Orchestra•Jersey Bounce / Don\'t Be That Way•Decca•0','\
Glenn Miller And His Orchestra•Georgia On My Mind / Jersey Bounce•no label•0','\
Shep Fields And His Rippling Rhythm•Keep Cool (Gin And Quinac) / Jersey Bounce•MGM Records•1953','\
The Top-Notchers•Jersey Bounce•Town And Country•1955','\
Benny Goodman And His Orchestra•Jersey Bounce / String Of Pearls / Long John Silver•V Disc•1945','\
Harry James And His Orchestra•Jersey Bounce / Theme From Orfeu Negro•MGM Records•1961'),'\
\
Jinrikisha\
':('\
Joe Henderson•Page One•Blue Note•1963','\
Kyoto Jazz Sextet•Mission•Blue Note•2015','\
James Last•Western Party And Square Dance•Polydor•1977'),'\
\
Jitterbug Waltz\
':('\
Shirley Scott•Happy Talk / Jitterbug Waltz•Prestige•1962','\
Vince Guaraldi Quintet•Zelao / Jitterbug Waltz•Fantasy•1963','\
Fats Waller & His Rhythm•We Need A Little Love / The Jitterbug Waltz•Bluebird (3)•1942','\
Jimmy Smith•There\'ll Never Be Another You•Blue Note•1957','\
Eric Dolphy•Conversations•FM (6)•1963','\
Eric Dolphy•Music Matador•Bluenite•1999','\
Erroll Garner Trio•Jitterbug Waltz / This Funny Thing That They Call Love•Vogue Records•1956','\
Ted Heath And His Music•Selection From "Fats" Waller Album - Volume 2•London Records•1954','\
Frank Foster•Fearless Frank Foster•Prestige•1966','\
no artist•The Touch Of Tony Scott (Walkin\' On Air)•RCA•1956','\
Eric Dolphy•Eric Dolphy•Everest Records Archive Of Folk & Jazz Music•1968','\
The Barry Altschul Quartet•Irina•Soul Note•1983'),'\
\
Jitterbug Waltz The\
':('\
Fats Waller & His Rhythm•We Need A Little Love / The Jitterbug Waltz•Bluebird (3)•1942','\
Jimmy Smith•There\'ll Never Be Another You•Blue Note•1957','\
Ted Heath And His Music•Selection From "Fats" Waller Album - Volume 2•London Records•1954','\
no artist•The Touch Of Tony Scott (Walkin\' On Air)•RCA•1956','\
Eric Dolphy•Alone Together•Tobacco Road•0','\
James Morrison•James Morrison At The Winery•ABC Records (3)•1985','\
Pierre Michelot•Bass & Bosses•EmArcy•1990','\
Greg Osby•The Invisible Hand•Blue Note•2000','\
Michel Sardaby•Voyage•Harmonic Records•1984','\
Herb Geller•Fire In The West•Jubilee•1957','\
The Chick Corea New Trio•Past Present & Futures•Stretch Records•2001'),'\
\
Jody Grind\
':('\
Horace Silver•The Jody Grind•Blue Note•1966','\
The Horace Silver Quintet•The Jody Grind•Blue Note•1967','\
Bob James Trio•Straight Up•Warner Bros. Records•1996','\
Jamey Aebersold•Horace Silver - Eight Jazz Classics:  Volume 17•JA Records•1978','\
Various•Baptist Beat!•Blue Note•1987','\
Horace Silver•Greatest Hits•CEMA Special Markets•1992','\
Horace Silver•The Very Best•Blue Note•2005','\
Horace Silver•The Best Of Horace Silver Vol. II•Blue Note•1989','\
Meirelles E Os Copa 7•Tropical•London Records•1969','\
Quintetto X•Novo Esquema Da Bossa•Right Tempo•1995','\
Dee Dee Bridgewater•Love And Peace - A Tribute To Horace Silver•Verve Records•1995'),'\
\
Johnny One Note\
':('\
George Wallington Quintet•George Wallington Quintet At The Bohemia (Featuring The Peck)•Progressive Records (2)•1955','\
Various•Kings Of Drums - Jazz Party 2•CBS•1972','\
The Tubby Hayes Quintet•Down In The Village•Fontana•1963','\
Clarke-Boland Big Band•Now Hear Our Meanin\'•Columbia•1965','\
Clarke-Boland Big Band•Now Hear Our Meanin\'•Columbia•1965','\
Various•Demonstration Record•London Records•1962','\
Eddie Maynard And His Orchestra•Moonlight Serenade-The Glenn Miller Sound•Diplomat Records•0','\
Various•Showcase - Phase 4•Decca•1962','\
Charlie Mariano•Charlie Mariano•Bethlehem Records•1956'),'\
\
John\'s Waltz\
':('\
Oliver Nelson And His Orchestra•Jacqueline•Impulse!•0','\
Clifford Jordan Quartet•Night Of The Mark VII•Muse Records•1975','\
John Klemmer•Intensity•Impulse!•1973','\
Herb Ellis•Softly... But With That Feeling•Verve Records•1961','\
Dannie Richmond\'s "In" Crowd•"In" Jazz For The Culture Set•Impulse!•1965','\
Gary Burton•New Vibe Man In Town•RCA Victor•1962','\
Dannie Richmond\'s "In" Crowd•"In" Jazz for the Culture Set•Impulse!•1971','\
Dannie Richmond\'s "In" Crowd•"In" Jazz for the Culture Set•Impulse!•1971','\
Oliver Nelson And His Orchestra•The Kennedy Dream•Impulse!•1967','\
George Shearing•Piano•Concord Jazz•1990','\
The Diamond Five•Something Old Something New Something Pink Something Blue•EMI•1975','\
Monty Alexander•Alexander The Great•Pacific Jazz•1965','\
Brian Bromberg•It\'s About Time: The Acoustic Project•Nova Records (3)•1991','\
Charles Neville•& Diversity•LaserLight Digital•1990'),'\
\
Joint is Jumpin\'\
':('\
Hank Jones•Ain\'t Misbehavin\'•Galaxy•1979','\
Jack Sheldon Quintet•Hollywood Heroes•Concord Jazz•1988','\
Fats Waller & His Rhythm•Your Feet\'s Too Big•RCA•1960','\
Fats Waller•Your Feets Too Big•RCA Victor•0','\
Various•The Headliners•PGP RTB•1986','\
Fats Waller•Ain\'t Misbehavin\'•Design (2)•1987','\
Fats Waller•The Fats Waller Legacy•Olympic Records (4)•1973','\
Fats Waller•Fats Waller•Joker (2)•1971','\
Fats Waller•"Fats" Waller Favorites•Victor•1944','\
Charlie Norman•The Joint Is Really Jumpin\' 1945-1947•Odeon•1982','\
Fats Waller & His Rhythm•\'Fats\' Waller Favourites•no label•0'),'\
\
Jordu\
':('\
Duke Jordan•Jazz Laboratory Series Vol. 1•Signal (3)•1955','\
Jay C. Birdlander•Jordu / The Champ•Vogue•1979','\
Clifford Brown And Max Roach•Däähoud•EmArcy•0','\
The Diamond Five•Poll Winners Jazz•Fontana•1961','\
Barney Wilen•Barney•RCA•1960','\
Clifford Brown And Max Roach•Clifford Brown And Max Roach•Emarcy•1954','\
Hampton Hawes Quartet•All Night Session Vol. 1•Contemporary Records•1958','\
Martial Solal Trio•Jazz À Gaveau•Columbia•1962','\
Manhattan Jazz Quintet•Autumn Leaves•Paddle Wheel•1985','\
Max Roach•Again Volume One•Affinity•1980','\
Tommy Flanagan•Our Delights•Galaxy•1979','\
Martial Solal Trio•Solal!•Milestone (4)•1967','\
Ryan Kisor•Kisor •Videoarts Music•2000'),'\
\
Joshua\
':('\
Bobby Scott•Driftwood/Oh Joshua•ABC-Paramount•0','\
Sidney Bechet And His Blue Note Jazz Men•Joshua Fit The Battle of Jericho / Tailgate Ramble•Jazz Selection•0','\
Sidney Bechet And His Blue Note Jazz Men•Joshua Fit The Battle of Jericho / Tailgate Ramble•Jazz Selection•0','\
Miles Davis•Miles Davis In Europe•Columbia•1964','\
Miles Davis•Miles A Antibes•CBS•1964','\
Pierre Leduc•Information•Elysée (2)•1966','\
The New Woody Shaw Quintet•Vol.1 At Onkel Pö\'s Carnegie Hall Hamburg 1982•Jazzline•2017','\
Humphrey Lyttelton And His Band•Just Once For All Time / Joshua Fit The Battle Of Jericho•Parlophone•1954','\
no artist•When The Saints Go Marching In•Tip-Top•0','\
Ralph Flanagan And His Orchestra•Spring Will Be A Little Late This Year / Joshua•RCA Victor•1950'),'\
\
\Journey to Recife\
':('\
The Paul Winter Sextet•Journey To Recife•Columbia•1962','\
The Paul Winter Sextet•Jazz Meets The Bossa Nova•Columbia•1962'),'\
\
Joy Spring\
':('\
Clifford Brown And Max Roach•Däähoud•EmArcy•0','\
Freddie Hubbard And His Orchestra•Born To Be Blue•Pablo Records•1982','\
Clifford Brown And Max Roach•Clifford Brown And Max Roach•Emarcy•1954','\
The Frank Foster Quintet•Chiquito Loco•Bingow Records•1979','\
Anthony Braxton•Seven Standards 1985 Volume I•Magenta (2)•1985','\
Clifford Brown Ensemble•Clifford Brown Ensemble Featuring Zoot Sims•Vogue•1956','\
Larry Coryell•Equipoise•Muse Records•1986','\
Barney Kessel•Barney Kessel\'s Swingin\' Party At Contemporary•Contemporary Records•1963','\
The George Shearing Quintet•On The Sunny Side Of The Strip•Capitol Records•1960','\
no artist•Groove Blues•Prestige•1961'),'\
\
Joy To the World\
':('\
Steve Erquiaga•A Time For Joy (Reflections In Guitar)•Maranatha! Music•1985','\
Try-Tone•A Cappella 1•Next Records (4)•1997','\
Various•Sounds Of The Seasons•MCA Records•1988','\
Larry Ferrari•Merry Christmas Carols•Sure•1965','\
Various•Joyous Christmas  Volume 7•Columbia Special Products•1973','\
Frank Sinatra•Have Yourself A Merry Little Christmas•Reprise Records•1963','\
Hagood Hardy•A Very Special Christmas With Hagood Hardy•K-Tel•1978','\
Peter White•Songs Of The Season•Columbia•1997','\
Masahiko Satoh•さすらいのギター ／ 驚異のモーグ・サウンド•Victor•1972','\
Bley-Peacock Synthesizer Show•Revenge: The Bigger The Love The Greater The Hate•Polydor•1971','\
Various•The Spirit Of Christmas Volume Two•BMG Special Products•1997','\
The Mexicali Brass•Christmas With The Mexicali Brass•Crown Records (2)•1964','\
101 Strings•Instrumental Music From The Ross Hunter Production Lost Horizon And Other Selections•Alshire•1972','\
Various•Happy Holidays Volume 14•RCA Special Products•1979','\
no artist•Hark The Herald Angels Swing•World Jazz Records•1972'),'\
\
Joyce\'s Samba\
':('\
Aécio Flávio Sexteto•Música Popular Brasileira Em Expansão•Festival (22)•1965','\
Various•Jazz Panorama III•Балкантон•1976','\
Oscar Castro-Neves•Oscar!•SBK Especial•1987','\
Various•Wave Music Volume Three•Wavemusic•2001'),'\
\
Ju-Ju\
':('\
Los Patos•Voodoo Ju Ju Obsession•Disques Festival•1969','\
The Spirit Of Voodoo•Voodoo Ju Ju Obsession•Vega•1969','\
Marcus Miller•Live•Not On Label•1998','\
Passport (2)•Infinity Machine / Ju-Ju Man•ATCO Records•1976','\
Brother Jack McDuff•Ju Ju•Chess•1977','\
Passport (2)•Infinity Machine•Atlantic•1976','\
Gary Bartz•Ju Ju Man•Catalyst Records (3)•1976'),'\
\
Jump For Me\
':('\
Count Basie Orchestra•Jump For Me / Boogie Woogie•Parlophone•0','\
Paul Quinichette And His Swingtette•Like Who?•United Artists Records•1959','\
Paul Quinichette•Paul Quinichette•United Artists Records•1960','\
Benny Carter And His Orchestra•Jazz Off The Air Vol. 3•Spotlite Records•1980','\
Count Basie•Count Basie•LaserLight Digital•1989','\
Count Basie•Kansas City Style•Giants Of Jazz Records•1977','\
Buddy Rich And His Orchestra•This One\'s For Basie•Norgran Records•1956','\
Lester Young•Lester Young Memorial Album Volume 2•Fontana•1959','\
Harry James (2)•All Time Favorites•Columbia•1946','\
Various•The Sound Of Big Band Jazz In Hi-Fi!•World Pacific Records•1959','\
Various•An Odyssey Of Immortal Jazz Performances•Charlie Parker Records•0'),'\
\
Jump Monk\
':('\
Charles Mingus•Mingus At The Bohemia•Debut Records•1956','\
The Charles Mingus Quintet•Chazz!•Fantasy•1962','\
Charles Mingus•Mingus At The Bohemia•Debut Records•1956','\
Tonight At Noon (2)•To Mingus With Love•Prophone•2011','\
Charles Mingus•"Pithecanthropus Erectus" 1955-1957•Giants Of Jazz•1988','\
Mingus Big Band•Live At The Theatre Boulogne-Billancourt Paris Vol. 1•Soul Note•1989','\
Charles Mingus•Charles Mingus and Friends In Concert•Columbia•1973','\
Charles Mingus•Mingus•Prestige•1972','\
Mingus Big Band•Gunslinging Birds•Dreyfus Records•1995','\
Langston Hughes•The Weary Blues With Langston Hughes•MGM Records•1958'),'\
\
Jumping With Symphony Sid\
':('\
The George Shearing Quintet•I\'ll Remember April•MGM Records•1950','\
The George Shearing Quintet•I\'ll Remember April / Jumping With Symphony Sid•MGM Records•1950','\
Fats Navarro•At The Royal Roost 1948 (Volume 1)•Beppo Records•0','\
Miles Davis•Hi-Hat All-Stars•Fresh Sound Records•1987','\
The George Shearing Quintet•Lullaby Of Birdland•MGM Records•1957','\
Stan Getz•At Storyville - Vol. 2•Roost•1957','\
Charlie Parker•Bird With Strings (Live At The Apollo Carnegie Hall & Birdland)•Columbia•1977','\
Erwin Lehn•The German Jazz Hurricane•Columbia•1956','\
no artist•Morris Grants Presents J.U.N.K.•Argo (6)•1961','\
Tadd Dameron•The Great Jazz Concerts At The Original "Royal Roost" - Never Available Heretofore!•Jung Cat Records•0','\
Georgie Fame•A Declaration Of Love•ITM ARCHIVES•2015','\
Earl Hines And His All-Stars•Earl Hines And His Esquire All Stars Featuring Dicky Wells•Storyville•1985','\
Stan Getz•Jazz Summit•Disques Vogue•1972'),'\
\
June 15th 1967\
':('\
Gary Burton•Artist\'s Choice•Bluebird (3)•1987'),'\
\
Juntos\
':('\
Omar Sosa•Bembon (Roots III)•Midnight Sun•2000','\
Los Grillos (2)•Todos Juntos•Discos Heriba•1972','\
Lito Vitale Cuarteto•La Senda Infinita•Gasa•1989','\
Los Antiques•Sincerely Antique•Funny•1973','\
Toquinho•À Sombra De Um Jatobá•Milan•1990','\
Ted Nash (2)•The Brothers Nash•Liberty•1956','\
El Chicano•Celebration•KAPP Records•1972','\
Antonio Fuentes•Cuerdas Que Lloran En Mexico•Discos Fuentes•1974','\
The Blues And Soul Players•Dixieland•Olympo•1972','\
Pedro Iturralde•Los Ojos De Eva•Hispavox•1982','\
Lourdes Gil•Lourdes Gil Y Los Galantes•Areito•1969'),'\
\
Just a Few\
':('\
The Bud Shank Quintet•Compositions Of Shorty Rogers•Nocturne Records•1954','\
The Bud Shank Quintet•Compositions Of Shorty Rogers•Nocturne Records•1954','\
Barre Phillips•For All It Is•Japo Records•1973','\
Poncho Sanchez•El Mejor•Concord Jazz Picante•1992','\
Bud Shank•The Talents Of Bud Shank•Kimberly•1963','\
Terje Rypdal•Rypdal & Tekrø•RCA•1994','\
Bud Shank•Bud Shank - Shorty Rogers - Bill Perkins•Pacific Jazz•1955','\
John Abercrombie•Speak Easy•PAO Records•1999','\
Eric Gales Trio•Ghost Notes•Tone Center•2013','\
Cannonball Adderley•Cannonball And Eight Giants•Milestone (4)•1973','\
Zdeněk Pulec•V Plechovém Balení (Evergreens In Brass)•Supraphon•1984','\
Andrzej Dąbrowski•Do Zakochania Jeden Krok•Pronit•1972','\
Shorty Rogers•The Complete Atlantic And EMI Jazz Recordings Of Shorty Rogers•Mosaic Records (2)•1989'),'\
\
Just A-sittin\' and A-rockin\'\
':('\
Stan Kenton And His Orchestra•Artistry Jumps / Just A-Sittin\' And A-Rockin\'•Capitol Records•1945','\
The Delta Rhythm Boys•Just A-Sittin\' And A-Rockin\' / Don\'t Knock It•Decca•1946','\
The Delta Rhythm Boys•Just A-Sittin\' And A-Rockin\' / No Pad To Be Had•Decca•1946','\
Stan Kenton And His Orchestra•Just A-Sittin\' And A-Rockin\' / I Told Ya I Love Ya Now Get Out•Capitol Records•1949','\
Jimmy Forrest•Soul Street•New Jazz•1964','\
Shirley Scott•Scottie Plays The Duke•Prestige•1959','\
The Chico Hamilton Quintet•The Original Ellington Suite•Pacific Jazz•2000','\
Duke Ellington And His Orchestra•Featuring Paul Gonsalves•Fantasy•1984','\
The Kenny Burrell Trio•A Night At The Vanguard•Argo (6)•1960','\
Wim Overgaauw•Dedication•Park (2)•1978','\
Paul Gonsalves•Just A-Sittin And A-Rockin•Black Lion Records•1973','\
John Dankworth•5 Steps To Dankworth•Verve Records•1957','\
Duke Ellington•We Love You Madly•Pickwick•0'),'\
\
Just Friends\
':('\
Eddie Harris•Olifant Gesang / Just Friends•Vee Jay Records•1961','\
Charlie Parker•Just Friends•Verve Records•0','\
Supersax•Parker\'s Mood / Just Friends•Capitol Records•1973','\
Billy May And His Orchestra•Whatever Lola Wants•Capitol Records•1957','\
Charlie Parker With Strings•Just Friends / Everything Happens To Me•Karusell•1953','\
Dizzy Gillespie•The Trumpet Summit Meets The Oscar Peterson Big 4•Pablo Today•1980','\
Ray Conniff And His Orchestra & Chorus•Just Friends / For All We Know•CBS•1966','\
Don Patterson•Tune Up!•Prestige•1971','\
Etta Jones•You Came A Long Way From St. Louis•Prestige•1962','\
Jimmy Smith•Groovin\' At Smalls\' Paradise (Volume 2)•Blue Note•1958','\
Chet Baker•Chet Baker Sings And Plays•Pacific Jazz•1955','\
Anthony Braxton•In The Tradition•SteepleChase•1974','\
Tatsuya Takahashi 3•Impression•Audio Lab. Record•1980','\
Cecil Taylor Quintet•Hard Driving Jazz•United Artists Records•1959'),'\
\
Just In Time\
':('\
Lee Morgan•Expoobident•Vee Jay Records•1961','\
Ray Anthony•Just In Time/Tres Chic•Capitol Records•1960','\
The Jonah Jones Quartet•Just In Time•Capitol Records•1958','\
Earl Bostic•720 In The Books / Just In Time•King Records (3)•1960','\
Booker Ervin•No Land\'s Man / Just In Time•Prestige•1963','\
Barney Kessel•Let\'s Cook!•Contemporary Records•1963','\
Eliane Elias•A Long Story•Manhattan Records•1991','\
Gerry Mulligan•The Winners Of Down Beat\'s Readers Poll 1960 (Reeds)•Philips•1960','\
Sadao Watanabe•Sadao Watanabe•King Records•1961','\
Joe Morello•It\'s About Time•RCA•1962','\
Vic Godard•Hey Now (I\'m In Lové)•London Records•1981','\
Benny Golson Quartet•Free•Argo (6)•1963','\
Tom Rainey•Obbligato•Intakt Records•2014','\
Ella Fitzgerald•Ella In Hollywood•Verve Records•1961','\
Booker Ervin•Exultation!•Prestige•1963','\
Jed Levy•Good People•Reservoir (2)•1988','\
Ray Anthony•Sings Très Chic Just In Time•Capitol Records•1960'),'\
\
Just One Of Those Things\
':('\
The Dave Brubeck Quartet•Just One Of Those Things / Stardust•Swing (3)•1953','\
Buddy DeFranco And His Trio•Carioca / Just One Of Those Things•MGM Records•1952','\
Dave Brubeck•My Romance / Just One Of Those Things•Fantasy•1952','\
André Previn•Just One Of Those Things / Should I•no label•0','\
Benny Goodman Sextet•Tiger Rag / Just One Of Those Things•Parlophone•1947','\
Kay Thompson•Eloise / Just One Of Those Things•Cadence (2)•0','\
Sammy Davis Jr.•Just One Of Those Things / Earthbound•Decca•1956','\
Tommy Dorsey And His Orchestra•Just One Of Those Things / Love For Sale•RCA Victor•1949','\
Doris Day•Somebody Loves Me •Columbia•1950','\
Ella Fitzgerald•Concert In Europe•Verve Records•0','\
The Oscar Peterson Quartet•Just One Of Those Things / Willow Weep For Me•Karusell•0','\
Erroll Garner•Fabulous Garner•Philips•0','\
Sammy Davis Jr.•All Of You•Brunswick•0','\
Enoch Light And The Light Brigade•Begin The Beguine / Just One Of Those Things•Command•0','\
Jack Costanzo & His Afro Cuban Band•Just One Of Those Things / Chopsticks Mambo•GNP•1957','\
Ray Conniff And His Orchestra & Chorus•Say It With Music•Philips•1960','\
George Wallington Trio•A Day In Paris•Vogue•1972'),'\
\
Just Squeeze Me\
':('\
Coleman Hawkins•Coleman Hawkins•Fabbri Editori•1980','\
The Red Garland Trio•Perdido / Just Squeeze Me•Prestige•1959','\
Louisiana Rhythm Kings•Squeeze Me / Sweet Sue-Just You•Brunswick•0','\
The Bechet / Spanier Big Four•Squeeze Me / Sweet Sue Just You•H. R. S.•1940','\
Duke Ellington And His Orchestra•Just Squeeze Me (But Don\'t Tease Me) / Swamp Fire•RCA Victor•1946','\
Coleman Hawkins•Back In Bean\'s Bag•Columbia•1963','\
The Bechet / Spanier Big Four•Muggsy Spanier With Sidney Bechet•Melodisc (3)•1956','\
Chris Connor•A Jazz Date With Chris Connor•Metronome•1958','\
Shirley Scott•Queen Of The Organ•Impulse!•1965','\
Lena Horne•Lena Horne•Tops Records•1958','\
Joe Newman•Good \'n\' Groovy•Prestige Swingville•1961','\
Slide Hampton Octet•Sister Salvation•Atlantic•1960','\
Bjarne Nerem•Mood Indigo•Gemini Records (7)•1988','\
Earl Hines•Earl Meets Harry•Black And Blue•1978','\
Duke Robillard•Conversations In Swing Guitar•Stony Plain Records•1999'),'\
\
Just the Way You Are\
':('\
Diana Krall•Just The Way You Are•Verve Records•2002','\
Acker Bilk•Song For Guy•Pye Records•1980','\
Grover Washington Jr.•Just The Way You Are / Loran\'s Dance•Motown•1979','\
Sy Oliver And His Orchestra•To Think You\'ve Chosen Me! / Just The Way You Are•Decca•1950','\
Ahmad Jamal•One•20th Century Fox Records•1978','\
Rosemary Clooney•With Love•Concord Jazz•1981','\
Mike Mandel•Sky Music•Vanguard•1978','\
Cal Tjader•Breathe Easy•Galaxy•1978','\
Grover Washington Jr.•Plays The Hits•Verve Records•2010','\
Freddy Cole•Love Makes The Changes•Fantasy•1998','\
Boy Katindig•Midnight Lady•A & W Horizon•1978','\
Laurindo Almeida•New Directions•Crystal Clear Records•1979','\
Grant Green•Easy•Versatile•1978','\
Morgana King•Everything Must Change•Muse Records•1979'),'\
\
Just You Just Me\
':('\
Teddy Wilson Quintet•Just For You Blues / Just You Just Me•Musicraft•1945','\
Erroll Garner•Just You Just Me / Yesterdays•Selmer•0','\
Various•Norman Granz\' Jam Session #7•Clef Records•1955','\
Coleman Hawkins•Coleman Hawkins•Fabbri Editori•1980','\
no artist•Just You Just Me / Henderson Romp•Capitol Records•1948','\
Louis Armstrong And His All-Stars•Satchmo At Pasadena - Part 4•Brunswick•0','\
Lester Young Quartet•Just You Just Me / I Never Knew•Mercury•0','\
The Rounders (7)•Marianne / Just You Just Me•Apex (3)•1929','\
Lionel Hampton And His Sextet•The Soul Of Lionel Hampton•Musidisc•1971','\
Caterina Valente•Istanbul / Just You Just Me•Brunswick•1954','\
Red Norvo And His Orchestra•Just You Just Me / You Must Have Been A Beautiful Baby•Brunswick•1938','\
Jack Hylton And His Orchestra•Just You Just Me / Hang On To Me•no label•1929','\
Pianica Maeda•Just You Just Me / South Of The Border•Nutmeg•1989','\
Wardell Gray•Shades Of Gray•Custom Records (2)•0','\
Count Basie And The Kansas City Seven•Sometimes I\'m Happy•Mercury•1955','\
Hank Mobley•Tenor Conclave•Prestige•1957','\
Gene Krupa•Playing Some Of The Selections They Played In The Benny Goodman Movie•Clef Records•1956','\
Alice Babs•Side By Side•Decca•1959','\
Benny Goodman And His Orchestra•Benny Goodman And His Orchestra•Philips•1955','\
The Nat King Cole Trio•After Midnight Part 1•Capitol Records•1957','\
Thelonious Monk•The Unique Thelonious Monk•Riverside Records•1956'),'\
\
Kahlil The Prophet\
':('\
Jackie McLean•Destination... Out!•Blue Note•1964'),'\
\
Katrina Ballerina\
':('\
The New Woody Shaw Quintet•Vol.1 At Onkel Pö\'s Carnegie Hall Hamburg 1982•Jazzline•2017','\
Woody Shaw•The Moontrane•Muse Records•1975','\
Woody Shaw•United•Columbia•1981','\
Woody Shaw•Dark Journey•32 Jazz•1997','\
Jamey Aebersold•For You To Play... Woody Shaw Eight Classic Jazz Originals•JA Records•1976','\
Woody Shaw Quartet•Live In Bremen 1983•Elemental Music•2018','\
Woody Shaw•The Complete CBS Studio Recordings Of Woody Shaw•Mosaic Records (2)•1992','\
Woody Shaw•The Complete Columbia Albums Collection•Columbia•2011'),'\
\
Keep That Same Old Feeling\
':('\
Side Effect•Keep That Same Old Feeling•Fantasy•1977','\
The Crusaders•Keep That Same Old Feeling•ABC Records•1976','\
The Crusaders•Those Southern Knights•ABC Blue Thumb•1976','\
The Crusaders•Priceless Jazz Collection•GRP•1998','\
Various•B&G Party•BGP Records•1988','\
The Crusaders•Power Of Our Music; The Endangered Species (live In South Africa)•Indigo Blue Entertainment Inc.•2000','\
The Klang•Coming Home•Night Sky•1994','\
Billy Reed And The Street People•Billy Reed And The Street People•Acme Records (9)•1979'),'\
\
KELO\
':('\
Miles Davis•Vol. 2•Blue Note•1953','\
Just Be-Bop•Just Be-Bop•Discomate•1980','\
Miles Davis•Volume 2•Blue Note•1990','\
Art Blakey & The Jazz Messengers•Not Yet•Soul Note•1988','\
Various•The Master Grooves Of Rudy Van Gelder - The Legendary Blue Note Masterpieces•Blue Note•2002','\
Thelonious Monk Jr.•Changing Of The Guard•Blue Note•1998'),'\
\
Kentucky Oysters\
':('\
The George Russell Sextet•Stratusphunk•Riverside Records•1960','\
The George Russell Sextet•Stratusphunk / The Stratus Seekers•Riverside Records•2012','\
Various•Cold Castle National Jazz 1962 Festival Moroka-Jabavu•New Sound (4)•1962'),'\
\
Kicker\
':('\
Bill Doggett•The Kicker / Mudcat•ABC-Paramount•1965','\
Grant Green•Solid•Blue Note•1979','\
The Chick Corea Elektric Band•Inside Out•GRP•1990','\
Charles Earland•Unforgettable•Muse Records•1992','\
Bobby Hutcherson•The Kicker•Blue Note•1999','\
Joe Henderson Sextet•The Kicker•Milestone (4)•1968','\
The Horace Silver Quintet•Song For My Father (Cantiga Para Meu Pai)•Blue Note•1964'),'\
\
Kids Are Pretty People\
':('\
The Billy Mitchell Quintet•A Little Juicy•Philips•1964','\
Danish Radio Big Band•By Jones I Think We\'ve Got It•Metronome•1978','\
Joe Lovano Quartet•Classic! Live At Newport•Blue Note•2016','\
Thad Jones / Mel Lewis Orchestra•Monday Night•Solid State Records (2)•1969','\
Hank Jones•Just For Fun•Galaxy•1977','\
Thad Jones & Mel Lewis•Thad Jones Mel Lewis & UMO•RCA Victor•1978','\
Hank Jones•Upon Reflection - The Music Of Thad Jones•Verve Records•1993','\
Joe Lovano•Kids (Live At Dizzy\'s Club Coca-Cola)•Blue Note•2007','\
Thad Jones / Mel Lewis Orchestra•The Complete Solid State Recordings Of The Thad Jones/Mel Lewis Orchestra•Mosaic Records (2)•1994','\
Ray Charles•Genius + Soul = Jazz•Concord Records•1997'),'\
\
Killer Joe\
':('\
Benny Golson•The New Killer Joe•CBS•1977','\
The Jazztet•Mox Nix / Killer Joe•Argo (6)•1960','\
Quincy Jones•Killer Joe / Maybe Tomorrow•A&M Records•1970','\
Quincy Jones•Killer Joe / Oh Happy Day•A&M Records•1970','\
Tommy Chase•Killer Joe•Stiff Records•1987','\
The Killer Joe Orchestra•The Mlle / Killer Joe•Atlantic•1965','\
Jeff Tyzik•Jammin\' In Manhattan•Polydor•1984','\
Charles Earland•Living Black!•Prestige•1971','\
Joki Freund Sextet•Yogi Jazz•CBS•1963','\
Lionel Hampton•Flyin\' Home•Quintessence•1978','\
One For All (3)•Killer Joe•Venus Records (5)•2005','\
Philly Joe Jones Octet•Filet De Sole•Marge•1992','\
Lionel Hampton•Europa Jazz•Europa Jazz•1981','\
Benny Golson•Killer Joe•Columbia•1977','\
George Kawaguchi•Killer Joe•Union Jazz•1982','\
The Jazztet•Voices All•Eastworld•1983','\
Lionel Hampton•Good Vibes•CBS Special Products•1979','\
Ben Sidran•Live At The Elvehjem Art Museum•Cryonic Inc.•1986'),'\
\
Killing Me Softly With His Song\
':('\
David "Fathead" Newman•Killing Me Softly With His Song•Atlantic•1973','\
Eric Gale•Forecast•Kudu•1973','\
Various•Audio Inspection Vol. 4•Philips•1979','\
Barney Kessel•Two Way Conversation•Sonet•1974','\
Hampton Hawes•At The Piano•Contemporary Records•1978','\
Woody Herman•Feelin\' So Blue•Fantasy•1981','\
Roberta Flack•4 Super Hits•Atlantic•1978','\
Sonny Stitt•Mr. Bojangles•Cadet•1973','\
Blue Mitchell•The Last Tango=Blues•Mainstream Records•1973','\
Tim Weisberg•Dreamspeaker•A&M Records•1973','\
Eric Alexander Quartet•Gentle Ballads III•Venus Records (5)•2008','\
Roland Hanna•Sir Elf:•Choice (7)•1973','\
Sonny Stitt•In Style•Muse Records•1982'),'\
\
Knock On Wood\
':('\
Jerome Richardson•Groove Merchant •Verve Records•1967','\
Buddy Morrow And His Orchestra•All Night Long / Knock On Wood•RCA Victor•1954','\
Reuben Wilson•Orange Peel / Knock On Wood•Blue Note•1969','\
Willie Bobo•Knock On Wood•Verve Records•1967','\
Reuben Wilson•Blue Mode•Blue Note•1970','\
Oceans (2)•Second Chance•Breeze Records (6)•1986','\
Johnny Hammond•Gettin\' Up•Prestige•1967','\
George Benson•Pacific Fire•CTI Records•1983','\
Poncho Sanchez•Raise Your Hand•Concord Picante•2007','\
Herbie Mann•Deep Pocket•Kokopelli Records•1994','\
The S.S.O. Orchestra•Soul Stars•Hansa International•1981','\
Larry Carlton•Discovery•MCA Records•1987'),'\
\
La Fiesta\
':('\
McCoy Tyner Quintet•Jazz Jamboree 74 Vol. 2•Polskie Nagrania Muza•1975','\
Gary Burton / Chick Corea•The New Crystal Silence•Concord Records•2008','\
Merino Costa And His Tijuana Color•La Felicidad•CBS•1968','\
Lalo Schifrin•Che!•Tetragrammaton Records•1969','\
Chick Corea•An Evening With Chick Corea And Herbie Hancock•Polydor•1979','\
Stan Getz Quartet•At Montreux•Polydor•1977','\
Stan Getz Quartet•Portrait•Joker (2)•1977','\
Herbie Hancock•Herbie Hancock And Chick Corea•CBS/Sony•1981','\
Tohru Aizawa Quartet•Tachibana Vol. 1•Tachibana Record•1975'),'\
\
La Nevada Blues\
':('\
Various•25 Ans De Musique D\'avant Nova•Nova Records•2007'),'\
\
La Samba\
':('\
Nicos Jaritz Sextet•Macumba•Amadeo•1980','\
Various•Rendez-Vous•Street Jazz Records•1995','\
Claudio Roditi•Claudio Rio & Friends•no label•1996','\
Ornella Vanoni•La Voglia La Pazzia L\'Incoscienza L\'Allegria•Vanilla•1976','\
Jerry Mengo Et Son Orchestre•Música De La Película "La Samba Fantástica"•Telefunken•1956'),'\
\
La Vida Feliz\
':('\
McCoy Tyner•La Leyenda De La Hora (The Legend Of The Hour)•Columbia•1981','\
Chicago (2)•Te Buscare Toda la Vida = I\'ve Been Searchin\' So Long / Llamame = Call On Me / Hombre Feliz = Happy Man / Deseando Estuvieras Aqui = Wishing You Were Here•CBS•1974','\
Pieces Of A Dream•Ahead To The Past•Blue Note•1999','\
Elizeth Cardoso•Disco De Ouro•Copacabana•1974','\
Alma Y Vida•Cronología•RCA•1993','\
Paloma San Basilio•Escorpio•Columbia•2001','\
Beny More•Lo Mejor De Beny More•RCA Victor•1965','\
DJ Maestro•Blue Note Trip - Sunset / Sunrise•Blue Note•2003','\
Various•Chill: Brazil 3•Warner Music Brasil•2004'),'\
\
Lady Bird\
':('\
Tadd Dameron Septet•Jahbero / Lady Bird•Blue Note•1949','\
Barney Wilen•Barney•RCA•1960','\
Benny Goodman And His Orchestra•Buckle Down Winsocki / Shady Lady Bird•Columbia•1941','\
Dexter Gordon•More Power!•Prestige•1969','\
Al Cohn•True Blue•Xanadu Records•1977','\
Archie Shepp•Lady Bird•Denon•1979','\
Wardell Gray Sextet•Out Of Nowhere•Straight Ahead Jazz•0','\
Miles Davis•Lady Bird•Jazz Showcase•1975','\
Archie Shepp•Lady Bird•Denon•1979','\
Abbey Lincoln•In Paris / Painted Lady•Blue Marge•1980','\
Fats Navarro•The Fabulous Fats Navarro Volume 2•Blue Note•1957','\
Communication (4)•Live At Fat Tuesday\'s New York Vol.2•Paddle Wheel•1981','\
Don Byas•A Night In Tunisia•Black Lion Records•1989','\
Bud Powell•Relaxin\' At Home 61-64•Mythic Sound•1989'),'\
\
Lady\'s Blues\
':('\
Bengt Hallberg And His Swedish All Stars•Vol. 2•Metronome•1954','\
King Oliver•Petits Jazz Pour Tous 2•Philips•1955','\
Earl Hines•Dixieland Band•Jazz Panorama (2)•0','\
Ray Bryant•Shake A Lady•Sue Records Inc.•0','\
Count Basie Orchestra•High Tide / Lazy Lady Blues•Columbia•1946','\
The Floyd Morris Trio•Lady Be Good / Organ Blues•Apex (4)•1960','\
Gene Ammons•Play Me•Prestige•1973','\
Randy Weston•Uhuru Afrika•Roulette•1961','\
Stan Getz Quartet•Live At Montmartre Vol. 1•Imagem•1986','\
Herbie Mann•Herbie Mann With The Wessel Ilcken Trio•Philips•0','\
Roy Evans•My Old Lady Blues / The New St. Louis Blues•Columbia•1928','\
Roy Evans•My Old Lady Blues / The New St. Louis Blues•Columbia•1928','\
Gerry Mulligan And His Sextet•Mainstream Of Jazz Vol. 2•Mercury•1984','\
John Coltrane•Trane\'s Blues•Giants Of Jazz•1987','\
Charles Lloyd•Manhattan Stories•Resonance Records•2014','\
no artist•NBC\'s Chamber Music Society Of Lower Basin Street - Volume 2•Victor•1941','\
Flip Phillips•Jazz At The Philharmonic - Norgran Blues 1950•Verve Records•1983','\
Various•Jazz-Club • Alto Sax•Verve Records•1989','\
Dinah Shore•NBC\'s Chamber Music Society Of Lower Basin Street•RCA Camden•1964'),'\
\
Lakes\
':('\
Lee Hannah•Infinitely•Healthy Tapes•2018','\
Brian Hughes•Between Dusk...And Dreaming•Justin Time Records•1990','\
Pat Metheny•Watercolors•ECM Records•1977','\
Buddy DeFranco•Cross Country Suite•Dot Records•1958','\
Allan Holdsworth•The Things You See•Disques JMS•1980','\
Allan Holdsworth•The Things You See / Sunbird•JMS.•1989','\
The Scene Is Now•Total Jive•Lost Records (9)•1986','\
Franck Biyong•Visions Of Kamerun•Afrolectric Music•2010'),'\
\
Lament\
':('\
Firehouse Five Plus Two•Fireman\'s Lament / San•Good Time Jazz•0','\
Colosseum II•Lament•MCA Records•1977','\
Kay Starr•Fool Fool Fool / Kay\'s Lament•Capitol Records•1952','\
Duke Ellington And His Orchestra•Clarinet Lament / Echoes Of Harlem•Brunswick•1936','\
Duke Ellington And His Orchestra•no title•Brunswick•no year','\
Duke Ellington And His Orchestra•Never No Lament / Cotton Tail•Victor•1940','\
Barney Bigard And His Orchestra•Lament For Javanette / Ready Eddy•Bluebird (3)•1941','\
Duke Ellington And His Orchestra•Merry-Go-Round / Clarinet Lament•Polydor•0','\
Joe Marsala And His Delta Six•Twelve Bar Stampede / Feather Bed Lament•Decca•1941','\
Kay Starr•Foolin\' Around•Capitol Records•1961','\
Red Nichols And His Five Pennies•Glory Glory / Bugler\'s Lament•Capitol Records•1955','\
Jym Young•Puzzle Box•Freedom•1975','\
Duke Ellington And His Orchestra•Drop Me Off At Harlem / Clarinet Lament•Parlophone•1943'),'\
\
Lamp Is Low The\
':('\
Gloria Lynne•He Needs Me / The Lamp Is Low•Everest•1961','\
Chet Baker Quartet•The Lamp Is Low / Maid In Mexico•Pacific Jazz•1953','\
Chet Baker Quartet•The Chet Baker Quartet•Pacific Jazz•0','\
Don Patterson•The Return Of Don Patterson•Muse Records•1974','\
Booker Ervin•The Song Book•Prestige•1964','\
Booker Ervin•The Song Book•Prestige•1964','\
The Baroque Jazz Ensemble•The Baroque Jazz Ensemble•Catalyst Records (3)•1977','\
The Oscar Peterson Trio•Oscar Peterson Trio With Ray Brown And Ed Thigpen - Ljubljana 1964•Giants Of Jazz•1996','\
Gene Bertoncini•Close Ties - Works By Bach Ellington Gershwin Ravel And Others•Musical Heritage Society•1987','\
Tommy Dorsey And His Orchestra•Sweet And Lovely / The Lamp Is Low / It Must Be Jelly \'Cause Jam Don\'t Shake Like That / Flyin\' Home•V Disc•1944','\
Carmen Lundy•Good Morning Kiss•BlackHawk Records•1986','\
Richard Beirach•Convergence•Triloka Records•1990','\
Eddie Thompson Trio•When Lights Are Low•HEP Records (3)•1980','\
Vic Dickenson•Mainstream•Atlantic•1958','\
Chet Baker Quartet•Chet Baker Quartet•Pacific Jazz•1953','\
Orquesta Chucho Zarzosa•Marimba Cascade•RCA Victor•1956'),'\
\
Las Vegas Tango\
':('\
Gil Evans•The Individualism Of Gil Evans•Verve Records•1964','\
Michael Shrieve•Stiletto•Novus•1989','\
Gary Burton•Good Vibes•Atlantic•1970','\
Robert Wyatt•The End Of An Ear•CBS•1970','\
Nels Cline Trio•Silencer•Enja Records•1992','\
Gil Evans•Verve Jazz Masters 23•Verve Records•1994','\
Gil Evans•Las Vegas Tango•DeAgostini•1991','\
Various•Stoned Soul Picnic•Warner Jazz•2003'),'\
\
Last First\
':('\
Evan Parker•Nailed•FMP•2000','\
Tomasz Stańko•Balladyna•ECM Records•1976','\
Prism (9)•Live Alive Vol. 2 (In \'85)•SMS Records•1987','\
Erica Lindsay (2)•Dreamer•Candid•1992','\
Wibutee•Eight Domestic Challenges•Jazzland Recordings•2001','\
Gary Peacock•Shift In The Wind•ECM Records•1980','\
Food•Last Supper•Rune Grammofon•2004','\
Kip Hanrahan•A Few Short Notes From The End Run•American Clavé•1986'),'\
\
Last Nite\
':('\
Henry Hayes And His Orchestra•Last Nite / If You\'ll Be My Love•Savoy Records•0','\
Larry Carlton•Last Nite•MCA Records•1987','\
Terje Rypdal•Blue•ECM Records•1987','\
Larry Carlton•Sleepwalk•Warner Bros. Records•1982','\
Larry Carlton Trio•New Morning: The Paris Concert•in-akustik•2009','\
Ronny Jordan•At Last•N-Coded Music•2003','\
Sacred Spirit•Volume 8: Jazzy Chill Out•Higher Octave Music•2003','\
A.Y.B. Force•Lost Breaks•P-Vine Records•2006','\
Lou Rawls•At Last•Blue Note•1989','\
Various•California Skaquake 2: The Aftershock•Moon Ska•1996'),'\
\
Last Page\
':('\
Phil Woods•Back In New York•Vedette Records•1977','\
Phil Woods•Musique Du Bois•Muse Records•1974','\
Phil Woods And His European Rhythm Machine•Phil Woods And His European Rhythm Machine•Les Disques Pierre Cardin•1970','\
Putte Wickman•Songs Without Words•Zenith (7)•1985','\
Aske Jacoby•Luna Plena Super Me•Sony Music•2016','\
Various•Drum Nation (Volume Two)•Magna Carta•2005','\
Labfield•Bucket Of Songs•Hubro•2014','\
Ken Nordine•Devout Catalyst•Grateful Dead Records•1992','\
Various•Best Of Acid Jazz•Global Television•1996','\
Various•Jumping The Shuffle Blues•Fantastic Voyage•2011'),'\
\
Last Season\
':('\
Maria Schneider Orchestra•Evanescence•Enja Records•1994','\
Maria Schneider Orchestra•Days Of Wine And Roses - Live At Jazz Standard•ArtistShare•2000','\
Jackie Ryan•This Heart of Mine•OpenArt Records•2003','\
Various•CD Compilation #14•MCA Records Canada•1991','\
Gilles Peterson•Worldwide Programme 1•no label•2000','\
Various•Mega Jukebox Top 100•Arcade•1994','\
Various•Forever Changing - The Golden Age Of Elektra Records - 1963-1973•Rhino Records (2)•2006','\
Various•Rock And Roll Hall Of Fame + Museum - Live•Sony Music•2010','\
David Bowie•MP3 Collection•Digital Records (6)•2016'),'\
\
Last Train From Overbrook\
':('\
Don Patterson•Four Dimensions•Prestige•1968','\
The Eddie Davis-Johnny Griffin Quintet•Griff & Lock•Jazzland•1961','\
Clarke-Boland Big Band•Jazz Is Universal•Atlantic•1962','\
James Moody•Don\'t Look Away Now!•Prestige•1969','\
James Moody•Hey!  It\'s James Moody•Argo (6)•1960','\
Eddie "Lockjaw" Davis•Bacalao•Prestige•1960','\
Eddie "Lockjaw" Davis•Straight Ahead•Pablo Records•1976','\
James Moody•Last Train From Overbrook•Argo (6)•1958','\
James Moody•Return From Overbrook•Chess•1996','\
James Moody•Moody\'s Mood•Chess•0','\
Various•Bebop Hard Bop and Funk•The Franklin Mint Record Society•1986','\
Various•Jazz In Switzerland 1930-1975 (Swiss Jazz)•Swiss Radio International•1997'),'\
\
Laura\
':('\
The Dave Brubeck Trio•Laura / Indiana•Coronet (5)•1949','\
Sam Taylor (2)•Anna / Laura•Moodsville•1962','\
Norman Luboff Choir•Laura / Tenderly•Philips•0','\
George Coleman•Playing Changes•no label•1991','\
Erroll Garner•Laura / Somebody Loves Me•Savoy Records•1945','\
Don Byas And His Orchestra•Laura / Cement Mixer•Blue Star•1947','\
Count Basie Orchestra•Secret Love•Command•1967','\
Pete Rugolo Orchestra•Laura / Early Stan•Columbia•1954','\
Charlie Parker With Strings•Dancing In The Dark•Mercury•1950','\
Jay White (3)•Laura•Essex Records (3)•1953','\
Lou Donaldson•Possum Head•Argo (6)•1964','\
Stan Kenton And His Orchestra•Jump For Joe / Laura•Capitol Records•1951'),'\
\
Laurie\
':('\
Lloyd Ellis•Annie Laurie / Waltzing Guitars•Mercury•1955','\
Leslie "Jiver" Hutchinson And His Coloured Orchestra•Annie Laurie / I Can\'t Get Started•Supraphon•0','\
Maxine Sullivan & Her Orchestra•Annie Laurie / Blue Skies•Vocalion (2)•0','\
Jimmie Lunceford And His Orchestra•Annie Laurie / \'Frisco Fog•Decca•1938','\
"Bumps" Meyers Sextet•Bumpin\' With Bumps / Annie Laurie•Selective Records•1949','\
Gene Redd•New Annie Laurie / New Sidewalks Of New York•King Records (3)•1960','\
Guy Lombardo And His Royal Canadians•Annie Laurie / Roamin\' In The Gloamin\'•Decca•1964','\
Gene Krupa And His Orchestra•Prelude To A Stomp / Fare Thee Well Annie Laurie•Brunswick•1938','\
Art Pepper•Renascence•Galaxy•2000','\
Jazz Doctors•Hemslöjd•Storyville•1961','\
Eugene Cossmann And His Orchestra•Farewell Waltz•Columbia•1956'),'\
\
Lazy Bird\
':('\
Pat Martino•East!•Prestige•1968','\
John Coltrane•Blue Train•Blue Note•1957'),'\
\
Leila\
':('\
João Donato•Leilíadas•Elektra Musician•1986','\
Les Negresses Vertes•Leila•Virgin•2000','\
The Phil Woods Quartet•Leila / Abstraction•Epic•1957','\
Leila Negra•Leila Negra Singt Für Unsere Kleinen / Mamatschi / Silberpferdchen•Donauland•0','\
Jac Berrocal•Musiq Musik•Futura Records (2)•1973','\
Monk Montgomery•Montgomeryland•Pacific Jazz•1960','\
Rahmann•Rahmann•Polydor•1979','\
Anouar Brahem•Le Pas Du Chat Noir•ECM Records•2002','\
Herbie Mann•Herbie Mann With The Wessel Ilcken Trio•Philips•0','\
Various•Ernest In Love - (Original Off-Broadway Cast)•Columbia Masterworks•1960','\
Hot Club Of Detroit•Hot Club Of Detroit•Mack Avenue•2006','\
Wes Montgomery•The Best of Wes•CEMA Special Markets•1993','\
Wes Montgomery•A Portrait Of Wes Montgomery•World Pacific Jazz•1968','\
Wes Montgomery•Easy Groove•Pacific Jazz•1966'),'\
\
Lennie-Bird\
':('\
Warne Marsh Quartet•The Unissued 1975 Copenhagen Studio Recordings•Storyville•1997','\
Lee Konitz•Spirits•Milestone (4)•1972','\
Warne Marsh Quintet•Jazz Exchange Vol. 1•Storyville•1976','\
The Lee Konitz Quartet•Tranquility•Verve Records•1957','\
Lenny Popkin•Falling Free•Choice (7)•1981','\
Lennie Tristano Quartet•The Lennie Tristano Quartet•Atlantic•1981','\
Anthony Braxton•Eight (+3) Tristano Compositions 1989 - For Warne Marsh•hat ART•1990','\
Lee Konitz•Live At The Half Note•Verve Records•1994','\
Lennie Tristano•Lennie Tristano•Fabbri Editori•1989','\
Count Basie•"The Best Of" The Roulette Years•EMI•1991','\
Count Basie Orchestra•The Complete Roulette Live Recordings Of Count Basie And His Orchestra (1959-1962)•Mosaic Records (2)•1991','\
Lennie Tristano•The Complete Atlantic Recordings Of Lennie Tristano Lee Konitz & Warne Marsh•Mosaic Records (2)•1997'),'\
\
Lennie\'s Pennies\
':('\
Lennie Tristano Quartet•The Lennie Tristano Quartet•Atlantic•1981','\
Anthony Braxton•Eight (+3) Tristano Compositions 1989 - For Warne Marsh•hat ART•1990','\
Lennie Tristano•The Complete Atlantic Recordings Of Lennie Tristano Lee Konitz & Warne Marsh•Mosaic Records (2)•1997'),'\
\
Leroy the Magician\
':('\
Gary Burton•Good Vibes•Atlantic•1970','\
Various•Right On! Vol 5•Warner Music UK Ltd.•2004'),'\
\
Lester Leaps In\
':('\
Jazz At The Philharmonic•Norman Granz\' Jazz At The Philharmonic Vol. 4•Disc Records•1946','\
Jazz At The Philharmonic•Norman Granz\' Jazz At The Philharmonic Vol. 12•Mercury•0','\
Jazz At The Philharmonic•Norman Granz\' Jazz At The Philharmonic - Vol. 12•Mercury•1950','\
Charlie Parker•An Historic Meeting At The Summit•Charlie Parker Records•1961','\
Earl Bostic And His Orchestra•Pompton Turnpike / Lester Leaps In•King Records (3)•1958','\
Count Basie And The Kansas City Seven•Dickie\'s Dream / Lester Leaps In•Vocalion (2)•1939','\
Lester Young•Prez In Europe•Polydor•1974','\
James Moody And His Band•Lester Leaps In / Out Of Nowhere•Prestige•1950','\
Count Basie•Jam Session At The Montreux Jazz Festival 1975•Pablo Records•1975'),'\
\
Let Me Be the One\
':('\
Webster Lewis•Let Me Be The One•Epic•1981','\
Sammy Kaye And His Orchestra•The Midnight Ride / (Let Me Be) The One In Your Heart•Columbia•1953','\
Peabo Bryson•You\'re Looking Like Love To Me•Capitol Records•1983','\
Music Machine (7)•Music Machine•Not On Label•1972','\
Stewy Von Wattenwyl Trio•To The Point•Brambus Records•1996','\
Xavier Rudd•Good Spirits•Salt. X Records Ltd.•2005','\
Joe Thomas•Make Your Move•Lester Radio Corporation•1979','\
Oleta Adams•My Heart Won\'t Lie•Fontana•1994','\
Stanley Turrentine•Stanley Turrentine•UpFront Records (3)•1971','\
Lena Horne•It\'s Love•RCA Victor•1955','\
The Reign Of Kindo•Happy However After•Not On Label (The Reign Of Kindo Self-Released)•2018','\
Webster Lewis•Let Me Be The One•Epic•1981','\
Marilyn Scott•Take Me With You•The Engine•1996','\
no artist•After The Ball•Mercury•1960','\
Nancy Wilson•Kaleidoscope•Capitol Records•1971','\
Bert Kaempfert•Today•Polydor Spezial•0','\
Barb Jungr•Just Like A Woman (Hymn To Nina)•Linn Records•2008','\
Roy Ayers•I\'m The One (For Your Love Tonight)•Columbia•1987','\
Elizabeth Shepherd•Parkdale•Do Right! Music•2008','\
Pleasure (4)•Straight Ahead - The Best Of Pleasure Volume 1•BGP Records•1992','\
Peggy Lee•The Best Of Peggy Lee•MCA Records•2002'),'\
\
Let\'s Call The Whole Thing Off\
':('\
Nina Hagen•Bigband Explosion•SPV Recordings•2003','\
Vince Giordano And The Nighthawks•Dancin\' Cheek To Cheek•Sine Qua Non•0','\
Fred Astaire•The Essential Fred Astaire•Columbia•2004','\
Sammy Kaye And His Orchestra•Song And Dance Movie Hits•Columbia•1960','\
Billie Holiday•Greatest Hits•Columbia•1995','\
The Ink Spots•Swing High! Swing Low!•Conifer•1989','\
Fred Astaire•Swing Time / The Gay Divorcee / Top Hat / Shall We Dance - Original Soundtracks•EMI•1975','\
Billie Holiday•The Billie Holiday Story Volume II•Columbia•1973','\
Various•The Golden Age Of British Dance Bands•World Records (6)•0','\
Fred Astaire•Starring Fred Astaire•Columbia•1973','\
Billie Holiday•"The Golden Years" Volume II•Columbia•1966','\
Fred Astaire•An Evening With Fred Astaire •Nostalgia•1985'),'\
\
Let\'s Do It\
':('\
Tal Farlow•Second Set•Xanadu Records•1977','\
George Benson•Let\'s Do It Again•Warner Bros. Records•1988','\
George Van Eps•Blue Guitar•Philips•0','\
Airto Moreira•Life After That•Narada World•2003','\
Stanley Turrentine•Let It Go•Impulse!•1966','\
Lisa Ono•Boas Festas•Suite¡ Supuesto!•2000','\
no artist•Wrap This!•Music Of Content•2015','\
Alex Deutsch•Pink Inc.•DIW•1991','\
Lettuce (3)•Fly•Velour Recordings•2012','\
George Braith•Laughing Soul•Prestige•1966','\
Lee Kwang Cho•I\'m Old Fashioned [LP + SACD]•Audioguy Records•2015','\
Ella Fitzgerald•Ella Fitzgerald At The Montreux Jazz Festival 1975•Pablo Records Original Jazz Classics Fantasy•1993','\
Steely Dan•Old Regime•Thunderbolt•1986','\
Alphonse Mouzon•Love Fantasy•Optimism Incorporated•1987'),'\
\
Let\'s Fall in Love\
':('\
Nat King Cole•Let There Be Love•Capitol Records•1992','\
Keith Jarrett•Standards Vol. 2•ECM Records•1985','\
The Art Van Damme Quintet•Lullaby Of Broadway•Philips•1957','\
Lee Kwang Cho•I\'m Old Fashioned [LP + SACD]•Audioguy Records•2015','\
Denny Seiwell Trio•Boomerang•Quarto Valley Records•2018','\
Julie London•Cry Me A River•Special Projects•1984','\
Marilyn Scott•Handpicked•Engine Entertainment•2005','\
Lush Strings•More Lush Strings For Lovers•Custom Records (2)•1967','\
The Carmen Cavallaro Camp•The Carmen Cavallaro Camp Plays The 3B\'s•GWP Records•0','\
Александр Ростоцкий•Jazz Ballads•L-Junction•1999','\
Hugo & Luigi Chorus•Let\'s Fall In Love•RCA Victor•1963','\
Jacaranda Muse•September Sun•Heavenly Sweetness•2012','\
Sol Raye•The Unforgettable Nat "King" Cole•Stereo Gold Award•1977','\
Nat King Cole•The Best Of Nat King Cole•Music For Pleasure•1980','\
Rob McConnell & The Boss Brass•Rob McConnell\'s Boss Brass 2•Canadian Talent Library•1969'),'\
\
Let\'s Go Dancin\'\
':('\
Victor Feldman•Secret Of The Andes•Nautilus Recordings•1982','\
Everette Harp•For The Love•Blue Note•2000','\
Various•All Singing - All Talking - All Rocking•Warner Bros. Records•1973','\
Various•Launch•Launch Media•2000'),'\
\
Let\'s Stay Together\
':('\
RM Jazz Legacy•RM Jazz Legacy•Key Of Life+•2015','\
Eric Darius•Night On The Town•Higher Octave Music•2004','\
Bill Mason•Gettin\' Off / Outlook•Westbound Records•1999','\
Bobby Broom•Livin\' For The Beat•Arista•1984','\
Ronnie Laws•Fever•Blue Note•1976','\
Long John Baldry•Let The Heartaches Begin•Pye Records•1967','\
Roberta Flack•Roberta•Atlantic•1994','\
Unknown Artist•Love & Sax•Hallmark (6)•1995','\
Various•Night Calls•EMI•1993','\
Various•The Crossover Cafe II - Smooth Jazz & Sweet Soul•Universal Music Group International•2014','\
Dinah Washington•The Divine Miss Dinah Washington•Verve Records•2017','\
Various•15 Χρόνια Ποπ + Ροκ 1978-1993•BMG•1993'),'\
\
Liberated Brother\
':('\
Horace Silver•Liberated Brother / Nothin\' Can Stop Me Now•Blue Note•1973','\
Various•The Master Grooves Of Rudy Van Gelder - The Legendary Blue Note Masterpieces•Blue Note•2002','\
Weldon Irvine•Liberated Brother•Nodlew Music•1972','\
Hi-Fly•Samboogaloo•Tramp Records•2007','\
Horace Silver•In Pursuit Of The 27th Man•Blue Note•1973','\
Various•Blue Note\'s Sidetracks Vol. 4 - Caliente!•EMI Music Belgium•2004','\
DJ Maestro•Blue Note Trip - Somethin\' Old / Somethin\' Blue•EMI•2007','\
DJ Maestro•Blue Note Trip - Somethin\' Old / Somethin\' Blue•Blue Note•2007'),'\
\
Lie Awake\
':('\
Akphaezya•Anthology II : Links From The Dead Trinity•Ascendance Records•2008'),'\
\
Lies\
':('\
Jonathan Butler•Lies•Jive•1987','\
Kareem (4)•Rumours And Lies•Exploding Plastic Records•1997','\
Oscar Peterson•Little White Lies / Lover•Mercury•0','\
Blue Barron And His Orchestra•Afraid / Sugar Coated Lies•MGM Records Division•1951','\
The Red Norvo Trio•Little White Lies / Move•Swing (3)•1953','\
The George Shearing Quintet•For You / Little White Lies•MGM Records•1951','\
Chick Webb And His Orchestra•Little White Lies / F. D. R. Jones•Brunswick•1939','\
The George Shearing Quintet•Little White Lies / Pick Yourself Up•MGM Records•0','\
Mel Tormé•Gone With The Wind / Little White Lies•Musicana•1948','\
Tommy Dorsey And His Orchestra•I\'ll Never Smile Again / Little White Lies•RCA Victor•0','\
Ella Fitzgerald•Trying / My Bonnie Lies Over The Ocean•Decca•1952','\
Jack Pleis And His Orchestra•Hey There / Lies•Decca•1955','\
Eartha Kitt•An Englishman Needs Time / Little White Lies•Columbia•1963','\
Eddie Heywood•All About You / Lies•RCA Victor•1957','\
Michael Franks•The Camera Never Lies•Warner Bros. Records•1987'),'\
\
Light as a Feather\
':('\
Chick Corea•Light As A Feather•Polydor•1973','\
The Tronosonic Experience•The Tronosonic Experience•Losen Records•2017','\
Azymuth•Live At The Copacabana Palace•SBA•1985','\
Flora Purim•Butterfly Dreams•Milestone (4)•1973'),'\
\
Like a Lover (O Cantador)\
':('\
no artist•The Look Of Love•A&M Records•1968','\
Andy Bey•Shades Of Bey•Evidence (5)•1998','\
Sarah Vaughan•Sings For Lovers•Pablo Records•2006','\
Sérgio Mendes•Portrait Of Sergio Mendes•A&M Records•1973'),'\
\
Like Father Like Son\
':('\
Billy Childs•Twilight Is Upon Us•Windham Hill Records•1989','\
Richard Harris•The Richard Harris Love Album•Dunhill•1972','\
Various•Baadasssss! (Original Motion Picture Soundtrack)•BBE•2004','\
Klaus Wunderlich•Hits Again 2•Telefunken•1972','\
Joe Loss & His Orchestra•Joe Loss Pop Dance Party 33 Hits•Odeon•1972','\
Various•Hits Of The Years 1960 - 1975•Object Enterprises•1988','\
Frank Zappa•антология творчества часть 1-2•Домашняя Коллекция•2004','\
Various•70\'s Best Of•Not On Label•2006','\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014'),'\
\
Like Someone in Love\
':('\
The Dave Brubeck Quartet•In Europe - No. 1•Fontana•1958','\
Phil Woods•Squire\'s Parlor•Fontana•0','\
Ahmad Jamal•April In Paris / Like Someone In Love•Argo (6)•1958','\
Eric Dolphy•At The Five Spot Volume 2•Prestige•1963','\
The Dave Brubeck Quartet•Wonderful Wonderful Copenhagen•Fontana•1960','\
Art Blakey & The Jazz Messengers•Munich \'59•Birdland (7)•2012','\
Tommy Dorsey And His Orchestra•Sleigh Ride In July / Like Someone In Love•Victor•1944','\
The John Coltrane Sextet•Jazz Club Collection Vol 6•United Artists Records•1975','\
Joe Holiday And His Band•Hello To You / Like Someone In Love•Prestige•1953','\
Michael Garrick Trio•You\'ve Changed•HEP Records (3)•1981','\
Nobuo Hara and His Sharps & Flats•Giant Steps•King Records•1978','\
Cecil Taylor Quintet•Hard Driving Jazz•United Artists Records•1959','\
Herman Foster•The Explosive Piano Of Herman Foster•Epic•1961','\
Lem Winchester•Another Opus•Prestige•1960'),'\
\
Like Sonny\
':('\
John Coltrane•Coltrane Jazz•Atlantic•1961','\
Fred Anderson Quartet•Birdhouse•Okka Disk•1996','\
Akira Miyazawa•Yamame•King Records•1977','\
John Coltrane•Alternate Takes•Atlantic•1974','\
Kenny Garrett•Pursuance: The Music Of John Coltrane•Warner Bros. Records•1996','\
Joe Chambers And Friends•New York Concerto•Baystate•1981','\
Jorge López Ruiz•B.A. Jazz•VIK•1961'),'\
\
Li\'l Darlin\'\
':('\
Kenny Burrell•When Lights Are Low•Concord Jazz•1979','\
Various•Le 18 Gemme Del Jazz•Giants Of Jazz•1991','\
Jon Hendricks•Times Of Love•Philips•1972','\
Georgie Fame•The Whole World’s Shaking (Complete Recordings 1963-1966)•Polydor•2015'),'\
\
Limbo\
':('\
Duke Ellington And His Orchestra•Limbo Jazz•Impulse!•1962','\
The Tides•Midnight Limbo / Limbo Rock•Mercury•0','\
Candido•Soul Limbo / Jump Back•Blue Note•1970','\
David Carroll & His Orchestra•Big Girls Don\'t Cry Limbo•Mercury•1962','\
Cyril Diaz & Orchestra•Tabu / Limbo•Cook•1959','\
Andrew Hill•Compulsion•Blue Note•1967','\
Chubby Checker•Chubby Checker\'s Greatest Hits•Impact Music Promotions Inc.•1980','\
Michel Petrucciani•Power Of Three•Blue Note•1987','\
The Whodads•Bongo Festeris•Kinky Star•2000','\
Randy Weston•Portraits Of Duke Ellington•Verve Records•1990','\
Olatunji And His Drums Of Passion•Saturday Night Limbo / Lady Kennedy•Columbia•1963','\
Michel Petrucciani•The Best Of Michel Petrucciani - The Blue Note Years 1986-1994•Blue Note•1998','\
Herb Alpert & The Tijuana Brass•Struttin\' With Maria•Festival Records•1963'),'\
\
Limehouse Blues\
':('\
The Art Van Damme Quintet•Limehouse Blues•Capitol Records•1949','\
Bobby Maxwell And His Swinging Harps•Limehouse Blues / Plink Plank Plunk•Mercury•1952','\
Quintette Du Hot Club De France•Limehouse Blues / After You\'ve Gone•Victor•1936','\
Billy Hadnott And His Orchestra•Limehouse Blues / Junk Wagon•Federal (5)•1952','\
Ernie Heckscher•Limehouse Blues/Mack The Knife•Verve Records•0','\
Bengt Hallberg And His Swedish All Stars•Vol. 2•Metronome•1954','\
Stéphane Grappelli And His Hot Four•Limehouse Blues / I Got Rhythm•Decca•1935','\
Fletcher Henderson And His Orchestra•Limehouse Blues / Big John\'s Special•Brunswick•0'),'\
\
Lisa\
':('\
Acker Bilk And His Paramount Jazz Band•Mona Lisa•Columbia•1965','\
Nat King Cole•Unforgettable / Mona Lisa•Capitol Records•0','\
Ferrante & Teicher•Negligee•United Artists Records•1962','\
David Sanborn•Creeper / Lisa•Warner Bros. Records•1980','\
Charlie Spivak And His Orchestra•Mona Lisa / Loveless Love•London Records•0','\
Taivaantemppeli•Jazz-Liisa 2•Svart Records•2016','\
Nat King Cole•Mona Lisa / Too Young•Capitol Records•1961','\
Dennis Day•Mona Lisa / A Shawl Of Galway Grey•RCA Victor•1950','\
Viktor Lazlo•Balade De Lisa•Polydor•1992','\
Anna Högberg Attack•Anna Högberg Attack•Omlott•2016','\
Harry James And His Orchestra•Mona Lisa / La Vie En Rose•Columbia•1950','\
The Bobby Havana Boys•Latin Rhythms For Dancing•Warner Bros. Records•1959','\
Nat King Cole•Mona Lisa / Baby Wont You Say You Love Me•Capitol Records•1950'),'\
\
Litha\
':('\
Stan Getz•Sweet Rain•Verve Records•1967','\
Chick Corea•Tones For Joan\'s Bones•Vortex Records (2)•1968','\
Louis Stewart•I Thought About You•Lee Lambert•1979','\
Chick Corea•Tones For Joan\'s Bones•Vortex Records (2)•1968','\
Chick Corea•Inner Space•Atlantic•1973','\
Stan Getz•The Chick Corea / Bill Evans Sessions•Verve Records•1976'),'\
\
Little B\'s Poem\
':('\
Elvis Presley•Walk A Mile In My Shoes - The Essential 70\'s Masters•RCA•1995','\
David Bowie•MP3 Collection•Digital Records (6)•2016'),'\
\
Little Chicago Fire\
':('\
Les DeMerle•On Fire•Palo Alto Records•1982','\
Count Basie Orchestra•Live At El Morocco•Telarc Jazz•1992','\
Various•Superhits Of The Superstars•K-Tel•1975','\
Various•Party Megamix 2•Prism Leisure•1994','\
Various•Les Triomphes Du Blues•Habana•2001','\
Various•The Story Of Beat-Club Volume 2 1968-1970•ARD Video•2008','\
Various•The Story Of Beat-Club Volume 2 1968-1970•ARD Video•2008','\
Various•Les Triomphes Du Jazz•Habana•2000','\
Various•Forever Changing - The Golden Age Of Elektra Records - 1963-1973•Rhino Records (2)•2006','\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014','\
Various•The Complete Vinyl Collection•Bellevue Publishing Uk Ltd•2016'),'\
\
Little Niles\
':('\
Kenny Barron•Spiral•Eastwind•1984','\
Randy Weston•Little Niles•United Artists Records•1959','\
Horace Tapscott•The Tapscott Sessions Vol. 8•Nimbus West Records•0','\
Eugen Cicero•In Town•SABA•1965','\
Paul Serrano Quintet•Blues Holiday•Riverside Records•1961','\
The New Phil Woods Quintet•Integrity The New Phil Woods Quintet Live•Red Record•1985','\
John Heard & Co.•The Jazz Composer\'s Song Book•Straight Ahead Records•2005','\
Donald Byrd•Jazz Lab•Columbia•1957','\
James Spaulding•Gotstabe A Better Way•Muse Records•1990','\
Oscar Pettiford Orchestra•Oscar Pettiford Orchestra In Hi-Fi Volume Two•ABC-Paramount•1958','\
Bobby Hutcherson•In The Vanguard•Landmark Records (3)•1987','\
Randy Weston•Tanjah•Polydor•1973','\
Randy Weston•Earth Birth•Verve Records•1997'),'\
\
Little Rootie Tootie\
':('\
Thelonious Monk Trio•Little Rootie Tootie / Monk\'s Dream•Prestige•1953','\
Thelonious Monk Trio•The Thelonious Monk Trio•Prestige•1954','\
Steve Lacy•Only Monk•Soul Note•1987','\
Thelonious Monk•The Thelonious Monk Memorial Album•Milestone (4)•1982','\
Thelonious Monk•Panorama•Riverside Records•1969','\
Thelonious Monk•Greatest Hits•Riverside Records•1962','\
Jerry Gonzalez•Rumba Para Monk•Sunnyside•1989','\
Thelonious Monk Trio•Thelonious•Prestige•1953','\
Thelonious Monk•In Person•Milestone (4)•1976','\
Buell Neidlinger•SwinGrass \'83•Antilles•1983','\
The Thelonious Monk Orchestra•At Town Hall•Riverside Records•1959','\
Thelonious Monk Jr.•Monk On Monk•N2K Encoded Music•1997','\
no artist•Monk\'s Moods•EMusic•2001'),'\
\
Little Sunflower\
':('\
Ethnic Heritage Ensemble•Be Known: Ancient / Future / Music•Spiritmuse Records•2019','\
Freddie Hubbard•Little Sunflower / The Love Connection•Columbia•1979','\
Freddie Hubbard•The Love Connection•Columbia•1979','\
Chuck Mangione Quartet•The Chuck Mangione Quartet•Mercury•1977','\
Freddie Hubbard•Above And Beyond•Metropolitan•1999','\
The Essence All Stars•Hub Art - A Celebration Of The Music Of Freddie Hubbard•Hip Bop Essence•1995','\
Johnny Lytle•Happy Ground•Muse Records•1991','\
Dwight Trible•Living Water•no label•2004','\
Manny Oquendo•Ritmo Sonido Estilo•Montuno Records•1983','\
Helge Lien Trio•To The Little Radio•DIW•2006','\
Kenny Burrell•Special Requests (And Other Favorites) Live At Catalina\'s•HighNote Records Inc.•2013','\
Tito Puente•Live At The Playboy Jazz Festival•Playboy Jazz•2002','\
Various•Jazz I Umeå•Expo Norr•1971','\
Dave Valentin•Red Sun•GRP•1993','\
Christian McBride•Number Two Express•Verve Records•1996'),'\
\
Little Waltz\
':('\
Les Paul•Tennessee Waltz / Little Rock Getaway•Capitol Records•0','\
Charlie Hearnshaw Quartet•So Slam It!•Miles Music•1990','\
Fats Waller & His Rhythm•We Need A Little Love / The Jitterbug Waltz•Bluebird (3)•1942','\
Ron Carter Quartet•Piccolo•Milestone (4)•1977','\
Guy Lombardo And His Royal Canadians•The Little Fairy Waltz / Tin Pan Alley Rag•Decca•1951','\
New York Jazz Quartet•In Concert In Japan•Salvation (4)•1975','\
Eric Dolphy•Music Matador•Bluenite•1999','\
Gil Evans•Farewell -  Live At Sweet Basil•Electric Bird•1988','\
Randy Weston•Little Niles•United Artists Records•1959','\
Eric Dolphy•Eric Dolphy•Everest Records Archive Of Folk & Jazz Music•1968','\
Horace Tapscott•The Tapscott Sessions Vol. 8•Nimbus West Records•0','\
Duke Pearson•Prairie Dog•Atlantic•1966','\
Paul Bley•Sonor•Soul Note•1984','\
Bernie Senensky•New Life•PM•1976'),'\
\
Little Wind\
':('\
Kohsuke Mine•Out Of Chaos•East Wind•1974','\
Mel Tormé•Gone With The Wind / Little White Lies•Musicana•1948','\
Kazumi Watanabe•Olive\'s Step•Better Days (2)•1977','\
Maija Hapuoja•The Voice•Bluebird (2)•1980','\
The Jimmy Giuffre Trio•7 Pieces•Verve Records•1959','\
Dwight Trible•Living Water•no label•2004','\
Polly Bergen•Today\'s Hits•RCA Camden•1956','\
Elvis Stanić Group•Terra Sacra•Croatia Records•1997','\
Roy Williams (3)•Royal Trombone (Roy Williams In Sweden With John McLevy','Len Skeat And The Swedish All Stars)•Phontastic•1984','\
Miriam Makeba•Forbidden Games•RCA International•1973','\
Vince Guaraldi•Vince Guaraldi With The San Francisco Boys Chorus•D&D•1967','\
Ain Soph (2)•5 Or 9 / Five Evolved From Nine•Made In Japan Records•1992','\
Geri Allen•Twylight•Minor Music•1989','\
Dannie Richmond\'s "In" Crowd•"In" Jazz For The Culture Set•Impulse!•1965','\
Terje Rypdal•After The Rain•ECM Records•1976','\
Dannie Richmond\'s "In" Crowd•"In" Jazz for the Culture Set•Impulse!•1971','\
Claes Crona•With A Little Help From My Friend(s)•Skivbolaget•1985','\
Ray Bryant•Up Above The Rock•Cadet•1968'),'\
\
Liturgy\
':('\
Port Mone•Thou•Hevhetia•2014','\
Gary Burton Quartet•Duster•RCA Victor•1967','\
Gary Burton•Gary Burton / Larry Coryell•RCA Victor•1977','\
Michael Gibbs•Michael Gibbs•Deram•1970','\
Edgar Summerlin•Ring Out Joy•Avant Garde Records (2)•1968','\
Various•Universe 5 - A Hearts Of Space Collection•Hearts Of Space•1999'),'\
\
Locomotion\
':('\
Ferry Davis•Eso Beso (Bossa Nova) / Locomotion•Pain Expo Brood•0','\
The John Coltrane Sextet•Jazz Club Collection Vol 6•United Artists Records•1975','\
John Coltrane•Blue Train•Blue Note•2008'),'\
\
Lone Jack\
':('\
Pat Metheny Group•Pat Metheny Group•ECM Records•1978','\
Pat Metheny•Trio 99→00•Warner Bros. Records•2000','\
Tony Hymas•Oyaté•Nato•1990','\
Various•Themes Like Old Times (90 Of The Most Famous Original Radio Themes)•Viva (3)•1969','\
The Famous Choraliers•The Famous Choraliers And The Longines Symphonette In The World\'s Most Honored Family Singing And Listening Songs•Longines Symphonette Society•0'),'\
\
Lonely Dreams\
':('\
Freddie Hubbard•First Light•CTI Records•1971','\
Edgar Meyer•Dreams Of Flight•MCA Records•1987','\
Terry Gibbs•Terry Gibbs•EmArcy•1955','\
David Kikoski•Persistent Dreams•Triloka Records•1992','\
Charlie Haden Quartet West•In Angel City•Verve Records•1988','\
Dennis Coffey•Motor City Magic•TSR Records•1986','\
Laboratorium•Anatomy Lesson•Face Music Switzerland•1987','\
Felix Slatkin•Street Scene•Liberty•1961','\
Johnny Bothwell•Whatever Happened To Johnny Bothwell?•Bob Thiele Music•1974'),'\
\
Lonely Woman\
':('\
The Modern Jazz Quartet•Lonely Woman / Trieste•Atlantic•0','\
The Ornette Coleman Trio•Live At The Tivoli \'65•Magnetic Records (6)•1992','\
Ornette Coleman•The Shape Of Jazz To Come•Atlantic•1959','\
Ornette Coleman•The Unprecedented Music Of Ornette Coleman = 未踏峰•International Joker Production•1977','\
Ornette Coleman•"In Concert"•Not On Label (Ornette Coleman)•0','\
Rosko•Private Moments•Columbia•1987','\
The Marzette Watts Ensemble•The Marzette Watts Ensemble•Savoy Records•1969'),'\
\
Long Ago and Far Away\
':('\
Guy Lombardo And His Royal Canadians•Long Ago (And Far Away) / Humoresque•Decca•1944','\
Tim Weisberg•Long Ago And Far Away•A&M Records•1972','\
The Phil Woods Quartet•Live From New York•Palo Alto Records•1985','\
Bing Crosby•Long Ago (And Far Away) / Is You Is Or Is You Ain\'t (Ma Baby?)•Brunswick•0','\
Gene Ammons•Boss Tenors In Orbit!•Verve Records•1962','\
Chico Hamilton Quintet The•Gongs East!•Warner Bros. Records•1959','\
Glenn Miller And The Army Air Force Band•Marvelous Miller Moods•RCA Victor•1957','\
Rhoda Scott•À L\'Orgue Hammond - Ballades № 1•Barclay•1973','\
David Kikoski•Dave Kikoski•Epic•1994','\
Charlie Haden•Long Ago And Far Away•Impulse!•2018','\
Gil Mellé•Patterns In Jazz•Blue Note•1956','\
Herbie Harper Sextet•Herbie Harper Sextet!•Mode Records•1957'),'\
\
Long As You Know You\'re\
':('\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014'),'\
\
Living Yours\
':('\
Jan Garbarek•Belonging•ECM Records•1974','\
Thad Jones & Mel Lewis•Potpourri•Philadelphia International Records•1974','\
101 North•Forever Yours•Capitol Records•1991','\
Peter Lehel Quartet•Ballads•Good International Co.•2000','\
Susan Osborn•Susan•Golden Throat Recordings•1987','\
Teddy Wilson•Sunny Morning Vol. 3•Musicraft•1985','\
Eddie Higgins•Standards By Request 1st Day•Venus Records (5)•2008','\
Billie Holiday•The Quintessential Billie Holiday Volume 4 (1937)•Columbia•1988','\
Keith Jarrett•Selected Recordings•ECM Records•2002','\
Teddy Wilson•1946•Classics (11)•1998','\
Various•The Bridges Of Madison County - Music From The Motion Picture•Malpaso Records•1995'),'\
\
Look At The Birdie\
':('\
Art Blakey & The Jazz Messengers•Roots & Herbs•Blue Note•1970','\
Louis Armstrong•Hello Dolly!•Kapp Records•1964','\
Art Blakey•Eight Classic Albums•Reel To Reel Music Company•0','\
Art Blakey & The Jazz Messengers•The Complete Blue Note Recordings Of Art Blakey\'s 1960 Jazz Messengers•Mosaic Records (2)•1992','\
Various•100 Best Of Blue Note•EMI Music Belgium•2011'),'\
\
Look To the Sky\
':('\
John McNeil•Look To The Sky•SteepleChase•1979','\
Antonio Carlos Jobim•Wave•A&M Records•1967','\
Emily Remler•Firefly•Concord Jazz•1981','\
Antonio Carlos Jobim•Look To The Sky•A&M Records•1970','\
Jon Goin•Waltz At Big Sky•MCA Records Inc.•1988','\
Various•Sampler \'88 Volume One•MCA Records•1988'),'\
\
Looking Back\
':('\
Nat King Cole•Looking Back / Do I Like It•Capitol Records•1958','\
Nat King Cole•One Sun / Looking Back•Capitol Records•1965','\
Guy Lombardo And His Royal Canadians•More And More / Looking Back To See•Decca•1954','\
Harvie Swartz•Smart Moves•Gramavision•1986','\
Dan Siegel•Nite Ride•Inner City Records•1980','\
Nat King Cole•Looking Back•Capitol Records•1958','\
Shai Maestro Trio•Untold Stories•Motéma•2015','\
Anthony Wilson Nonet•Power Of Nine•Groove Note•2006','\
Nat King Cole•Nat King Cole\'s Greatest!•Capitol Records•0','\
Cherrystones•Free Sleazy Pieces EP•Stark Reality•1998','\
Jon Eberson•Anatomy Of The Guitar•NorDisc•1979','\
Supersister (2)•Iskander•Polydor•1973','\
Humphrey Lyttelton•I Play As I Please•Decca•1958','\
Ray Brown•As Good As It Gets•Concord Jazz•0','\
Steve Kuhn•Seasons Of Romance•Postcards•1995','\
Peter Prisco•It\'s About Time•Zinnia Records•1986'),'\
\
Loose Ends\
':('\
Andre Espeut•This Ain\'t How It Ends / Cut Loose•Imagenes•2015','\
Trummor & Orgel•Hopes And Dreams•Introspection•2015','\
Mike Stern•Jigsaw•Atlantic Jazz•1989','\
Fieldtrip•Fieldtrip•Not On Label (Fieldtrip Self-released)•2007','\
Gary Burton•The New Quartet•ECM Records•1973','\
Ferrante & Teicher•Soundblast - The Sound Of Tomorrow Today!•Westminster•1956','\
Ferrante & Teicher•Soundproof - The Sound Of Tomorrow Today!•Westminster•0','\
Ben Shepherd•In Deep Owl•INDRI Ltd.•2013','\
Sérgio Mendes•Timeless•Concord Records•2006','\
Various•25 Ans De Musique D\'avant Nova•Nova Records•2007'),'\
\
Love Came on Stealthy Fingers\
':('\
Carla White•Mood Swings•Milestone (4)•1988','\
Irene Kral•Where Is Love?•Choice (7)•1975','\
Mishka Adams•God Bless The Child•Candid•2005','\
Karin Krog•Break Of Day•Meantime Records (2)•2014','\
Janis Siegel•Slow Hot Wind•Varèse Sarabande•1995','\
Carmen McRae•Live•VideoArts•1986'),'\
\
Love Dance\
':('\
George Benson•Love X Love•Warner Bros. Records•1980','\
George Benson•Love X Love•Warner Bros. Records•1980','\
Eddie Harris•Freedom Jazz Dance•Atlantic•1966','\
Ted Heath And His Music•Shall We Dance•Decca•1959','\
Woody Shaw•Love Dance•Muse Records•1976','\
Harold Land•Xocia\'s Dance•Muse Records•1982','\
The Ramsey Lewis Trio•For The Love Of A Princess•Argo (6)•1964','\
Ethel Merman•Something To Dance About / You\'re Just In Love•Brunswick•0','\
David Wertman•Wide Eye Culture•Sunmuse Records•1983','\
Carmen Lundy•Changes•Afrasia Productions•2012','\
Madeleine Peyroux•Dance Me To The End Of Love•Universal•2004','\
Brenda Ray•Ramshackle Rumble•Aficionado Recordings•2014','\
Percy Faith & His Orchestra•Temptation•Hurrah Records (2)•1963','\
Sounds Orchestral•The Hopping Dance•Piccadilly•1966','\
The Charles Lloyd Quartet•Journey Within•Atlantic•1967'),'\
\
Love For Sale\
':('\
Sidney Bechet Quartet• Love For Sale / Shake \'Em Up •Columbia•1947','\
Alan Clare•Screwball•Parlophone•1962','\
Chet Baker•Strollin\'•Enja Records•1986','\
Clifford Jordan•Hello Hank Jones•Eastworld•1978','\
Erroll Garner•Cottage For Sale•Savoy Records•1949','\
Eddie Harris•Freedom Jazz Dance•Atlantic•1966','\
The Conley Graves Trio•Love For Sale / St. Louis Blues•Decca•1956','\
Stan Kenton And His Orchestra•Opus In Pastels / Love For Sale•Capitol Records•1950','\
Lloyd Glenn And Band•Hyde Park / Love For Sale•Aladdin (6)•1957','\
The Dick Hyman Trio•Love For Sale / Down Home Melody•Command•1960','\
The Three Sounds•On Green Dolphin Street / Love For Sale•Blue Note•1960','\
The Arthur Lyman Group•Love For Sale•HiFi Records•1963','\
Clifford Jordan•Hello Hank Jones•Eastworld•1978','\
Art Tatum•. . . Again! - The Tatum Group Masterpieces•Pablo Records•1976','\
Erroll Garner•Love For Sale / Don\'t Worry About Me•Blue star•0','\
Dexter Gordon•XXL - Live At The Left Bank•Prestige•2002','\
Buddy Merrill•Love For Sale / Armen\'s Theme•Accent (2)•1968','\
Oscar Peterson•Oscar Peterson At JATP•VSP•1966','\
Tommy Dorsey And His Orchestra•Just One Of Those Things / Love For Sale•RCA Victor•1949','\
Marian McPartland•Marian McPartland Moods Volume 2•Quality•0','\
Joyce Bryant•Love For Sale /  A Shoulder To Weep On•Okeh•1952'),'\
\
Love Is A Many Splendored Thing\
':('\
Eddie Calvert•Love Is A Many Splendored Thing / Spellbound•Columbia•1955','\
Woody Herman And His Orchestra•Love Is A Many-Splendored Thing / House Of Bamboo•Capitol Records•1955','\
Joe Loco And His Quintet•Love And Marriage / Love Is A Many-Splendored Thing•Columbia•1955','\
Victor Silvester And His Ballroom Orchestra•Love Is A Many Splendored Thing•Columbia•1956','\
David Rose & His Orchestra•You And You Alone / Love Is A Many-Splendored Thing•MGM Records•1955','\
Ray Conniff•\'S Hollywood•Columbia•0','\
Kirk Lightsey Trio•Temptation•Baystate•1988','\
Jimmy Smith•At Club "Baby Grand" Wilmington Delaware Volume 2•Blue Note•1956','\
Karel Gott•Jezebel / Je Krásné Lásku Dát•Supraphon•1964','\
Kunihiko Sugano Trio•Love Is A Many Splendored Thing•Three Blind Mice•1974','\
Victor Silvester And His Ballroom Orchestra•Dance Encores•Columbia•0','\
101 Strings•Play Hits Made Famous By Nat King Cole•Alshire•1972'),'\
\
Love Letter\
':('\
Maynard Ferguson•Hollywood Jam Sessions•Fresh Sound Records•2005','\
Barbara Young•My First Love Letter•Trend (9)•0','\
Michel Petrucciani•Trio In Tokyo•Dreyfus Jazz•1999','\
Burt Ward•Boy Wonder I Love You / Dear Jeepers•US Ltd.•0','\
Duke Ellington And His Orchestra•Duke Ellington\'s Third Sacred Concert The Majesty Of God As Performed In Westminster Abbey•RCA Victor•1975','\
Duke Ellington And His Orchestra•Duke Ellington\'s Third Sacred Concert The Majesty Of God As Performed In Westminster Abbey•RCA Victor•1975','\
Sarah Vaughan•I\'m Gonna Sit Right Down And Write Myself A Letter•MGM Records•1950','\
The Leslie Drayton Orchestra•Love Is A Four-Letter Word•Esoteric Records (3)•1986','\
Buddy Arnold•Wailing•ABC-Paramount•1986','\
Eddie Harris•Yeah You Right•Lakeside Music•1993','\
Fats Waller & His Rhythm•Fats Waller And His Rhythm•La Voix De Son Maître•0','\
Fats Waller & His Rhythm•I\'m Gonna Sit Right Down And Write Myself A Letter / Everybody Loves My Baby•no label•0','\
Dave McKenna•Concord Duo Series 2 •Concord Jazz•1993','\
The Bill Evans Trio•Letter To Evan•Dreyfus Jazz•1992'),'\
\
Love Me Or Leave Me\
':('\
Cal Tjader•Love Me Or Leave Me•Savoy Records•0','\
Gerry Mulligan Quartet•Jeru / Love Me Or Leave Me•Swing (3)•1953','\
Gerry Mulligan Quartet•3e Salon Du Jazz Paris 1954 à Pleyel•Jazz Selection•1956','\
Gerry Mulligan Quartet•Paris Concerrt•Pacific Jazz•1956','\
Billie Holiday And Her Orchestra•Love Me Or Leave Me / I Thought About You•Clef Records•0','\
Nina Simone•Love Me Or Leave Me / Little Girl Blue•ZYX Records•1988','\
Lawrence Welk And His Champagne Music•Love Me Or Leave Me / Hey Mr. Banjo•Coral•1955','\
Lena Horne•Love Me Or Leave Me / I Love To Love•RCA Victor•1955','\
Benny Goodman And His Orchestra•St. Louis Blues / Love Me Or Leave Me•no label•0','\
Billy Eckstine•Only You / Love Me Or Leave Me•MGM Records•1955','\
Benny Goodman And His Orchestra•Love Me Or Leave Me / Exactly Like You•Victor•1936','\
Cal Tjader•Love Me Or Leave Me•Savoy Records•1953','\
Gerry Mulligan Quartet•The Gerry Mulligan Quartet Vol. 2•Vogue•1955','\
Nina Simone•My Baby Just Cares For Me•Carrere•1987','\
Martial Solal•Rèunion A Paris•Swing (3)•1956'),'\
\
Love Speaks Louder Than Words\
':('\
Wilbert Longmire•The Best Of Wilbert Longmire•Tappan Zee Records•1981','\
Al Jarreau•High Crime•Warner Bros. Records•1984','\
Wilbert Longmire•With All My Love•Tappan Zee Records•1980','\
Various•The Best Of Rare•Ariola•1990','\
Various•25 Ans De Musique D\'avant Nova•Nova Records•2007'),'\
\
Love Vibrations\
':('\
Sonny Stitt•Black Vibrations•Prestige•1972','\
Buster Williams•Crystal Reflections•Muse Records•1976','\
Various•Coolin\' - A Soul Jazz Journey•pHo Records•1996','\
Richard "Groove" Holmes•Jazz Milestone Series•Pacific Jazz•1966','\
Steve Douglas•Reflections In A Golden Horn•Mercury•1969','\
Dorothy Ashby•Afro-Harping•Cadet•1968','\
James Last•Seduction•Polydor•1980','\
Steve Kujala•The Arms Of Love•Sonic Edge•1989','\
Dee Dee Bridgewater•Afro Blue•Trio Records•1974','\
David T. Walker•Plum Happy•Zea Records•1970','\
The Horace Silver Quintet•That Healin\' Feelin\' (The United States Of Mind / Phase 1)•Blue Note•1970'),'\
\
Love Walked In\
':('\
Dinah Washington•Unforgettable / Love Walked In•Mercury•0','\
Erroll Garner•I Surrender Dear•Savoy Records•1949','\
Benny Goodman And His Orchestra•Love Walked In / Ramona / Soft As Spring / Tangerine•Philips•0','\
Dinah Washington•Love Walked In•Esquire Mercury•1960','\
Sonny Stitt•Plays Arrangements From The Pen Of Quincy Jones•Sonet•0','\
The Dave Brubeck Octet•The Way You Look Tonight / Love Walked In•Fantasy•1950','\
Brother Jack McDuff•The Midnight Sun•Prestige•1968','\
Art Blakey & The Jazz Messengers•Keystone 3•Concord Jazz•1982','\
George Shearing•George Shearing And The Montgomery Brothers•Riverside Records•1964','\
Max Roach Quintet•Graz 1963 Concert•Jazz Connoisseur•0','\
Art Blakey & The Jazz Messengers•Keystone 3•Concord Jazz•1982','\
George Benson•Jazz On A Sunday Afternoon Vol. III•Accord (2)•1982','\
LA4•Just Friends•Concord Jazz•1978'),'\
\
Love Come Back To Me\
':('\
Clifford Brown•Cliff Brown + Art Farmer With The Swedish All Stars (Vol. 2)•Metronome•1954','\
Butterball (4)•Lover Come Back To Me•Bronjo•1958','\
Dinah Washington•Newport \'58•Mercury•1959','\
Jan Garber And His Orchestra•Come Back To Me / I Love You Because•Capitol Records•1950','\
Flip Phillips•Lover•Clef Records•0','\
Artie Shaw And His Orchestra•This Is Artie Shaw And His Orchestra•RCA Victor•0','\
Dinah Washington•The Complete Dinah Washington Vol. 12 1954•Official (3)•1989','\
Teuvo Suojärvi Quartet•Suomalaista Jazzia •Scandia•0','\
Flip Phillips Quartet•Flip Phillips Quartet•Clef Records•1953','\
Nat King Cole•Love Is A Many Splendored Thing•Capitol Records•0','\
Teddy Edwards•It\'s About Time•Pacific Jazz•1960','\
Rachelle Ferrell•\'Til You Come Back To Me•Capitol Records•1992','\
Conte Candoli•West Coast Wailers•Atlantic•1955','\
The Manhattan Transfer•Baby Come Back To Me (The Morse Code Of Love)•Atlantic•1985','\
Lonnie Plaxico•Iridescence•Muse Records•1991','\
Donald Byrd•Off To The Races•Blue Note•1959','\
Keiko Lee•Kickin\' It•Columbia•1996'),'\
\
Lover\
':('\
Erroll Garner•Lover (Part 1) / Lover (Part 2)•Vogue Records•0','\
Teuvo Suojärvi Quartet•Suomalaista Jazzia •Scandia•0','\
Stan Kenton And His Orchestra•Soothe Me / Lover•Capitol Records•1948','\
Flip Phillips•Lover•Clef Records•0','\
Gene Krupa And His Orchestra•Lover / Boogie Blues•Columbia•1946','\
Conte Candoli•West Coast Wailers•Atlantic•1955','\
no artist•First Class•no label•2001','\
Oscar Peterson•Little White Lies / Lover•Mercury•0','\
Stan Kenton And His Orchestra•The Peanut Vendor / Lover•Capitol Records•1950','\
Supersax•Salt Peanuts (Supersax Plays Bird Volume 2)•Capitol Records•1974','\
Dick Contino•Lover / 12th Street Rag•Horace Heidt Presents•1949','\
Flip Phillips Quartet•Flip Phillips Quartet•Clef Records•1953','\
no artist•Good Lover•EastWest Records America•1992'),'\
\
Lover Man\
':('\
The Charlie Parker Quintet•Lover Man / Don\'t Blame Me•History Of Jazz (2)•0','\
Howard McGhee Quintet•Be Bop / Lover Man•Dial Records (3)•0','\
Gerry Mulligan Quartet•Lover Man / Lady Be Good•Swing (3)•1953','\
Jutta Hipp And Her German Jazzmen•Jutta Hipp And Her German Jazzmen•MGM Records•0','\
Conte Candoli•West Coast Wailers•Atlantic•1955','\
Stan Getz•Lover Man•Moon Records (4)•1990','\
Dizzy Gillespie And His All Star Quintet•Shaw\' Nuff / Salt Peanuts / Lover Man / Stupendous•Pathé•0','\
Archie Shepp Quintet•Bird Fire•Impro•1979','\
El Cuarteto Del Chivo Borraro•En Vivo•Qualiton (2)•1973','\
Johnny Griffin•Jazz Jamboree 63 Vol. 2•Polskie Nagrania Muza•1963','\
Ben Sidran•Lover Man•CBS/Sony•1984','\
Erroll Garner•Lover Man / What Is This Thing Called Love•Vogue Productions•1948','\
Seiichi Nakamura Trio•Adventure In My Dream•Three Blind Mice•1975','\
The Charlie Parker Quintet•Lover Man•Barclay-Verve•1960','\
Jimmy Smith•House Party•Blue Note•1958','\
Supersax•Salt Peanuts (Supersax Plays Bird Volume 2)•Capitol Records•1974','\
Gil Mellé Quintet•Volume 2•Blue Note•1953'),'\
\
Love\'s Haunts\
':('\
Dewey Bergman•Romantic Echoes Of Paris•Colortone•0','\
Kitty Kallen•Little Things Mean A Lot•Vocalion (2)•1954','\
Ethel Smith•Parade•MCA Coral•1973','\
Ethel Smith•Miss Smith Goes To Paris•Decca•0','\
Toni Arden•Miss Toni Arden•Decca•1958'),'\
\
Loxodrome\
':('\
Steps Ahead•In Europe•Idem Home Video•2002','\
Steps Ahead•Steps Ahead•Elektra Musician•1983'),'\
\
Lucky Southern\
':('\
Tom Lellis•And In This Corner...•Inner City Records•1981','\
Airto Moreira•Free•CTI Records•1972','\
Jorge Navarro•Navarro Con Polenta•Aleluya Records•1977','\
The Gaylords•At The Shamrock•Mercury•1962','\
Chihiro Yamanaka•Abyss•Verve Records•2007','\
Colors Of Jazz•For Tropical Nights•Sony Masterworks•1991','\
Kevin Beadle•The Best Of Inner City Records•BBE•2016','\
Various•Diggin\' Deeper 5 - The Roots Of Acid Jazz•Columbia•2001','\
Ma Rainey•Mother Of The Blues Volume 1•Riverside Records•0','\
Ma Rainey•Mother Of The Blues Volume 1•Riverside Records•0'),'\
\
Lucky To Be Me\
':('\
Bill Evans•Minority•Riverside Records•0','\
Carmen McRae•Ooh (What\'cha Doin\' To Me) / If I\'m Lucky (I\'ll Be The One)•Decca•1954','\
Dave McKenna•Solo Piano•Chiaroscuro Records•1973','\
Tommy Flanagan•Lonely Town•Blue Note•1979','\
The Bill Evans Trio•Everybody Digs Bill Evans•Riverside Records•1959','\
Kenny Burrell•Sunup To Sundown•Contemporary Records•1991','\
Doc Cheatham•LIVE!•Natasha Imports•1987','\
Bobby Scott•Bobby Scott Plays The Music Of Leonard Bernstein•Verve Records•1959','\
The John Bunch Trio•The Best Thing For You•Concord Jazz•1987','\
Tony Scott Septet•Scott\'s Fling•RCA Victor•1955'),'\
\
Lullaby In Rhythm\
':('\
Charlie Ventura And His Orchestra•Lullaby In Rhythm / Birdland•RCA Victor•1949','\
Erroll Garner•Lullaby In Rhhthm / Undecided•Philips•0','\
Various•Norman Granz\' Jam Session #9•Verve Records•1957','\
The Boots Mussulli Quartet•Diga Diga Doo•Capitol Records•0','\
Erroll Garner•Gone Garner Gonest - Vol. 2•Columbia•0','\
The Dave Brubeck Quartet•Dave Brubeck Concert•Brunswick•1956','\
The Dave Brubeck Trio•You Stepped Out Of A Dream / Lullaby In Rhythm•Fantasy•1950','\
Erroll Garner•I Can\'t Get Started•Philips•0','\
Les Brown And His Band Of Renown•Le\'s Dance Vol. 1•Coral•1953','\
Dave Brubeck•Son Piano Et Ses Rhytmes•Vogue Productions•0','\
Roger Mozian•Spectacular Percussion•MGM Records•1960','\
Shelly Manne•Shelly Manne Vol. 2•Contemporary Records•1954'),'\
\
Lullaby of Birdland\
':('\
Various•Lullaby Of Birdland•RCA Victor•1955','\
Various•Lullaby Of Birdland (Volume 1)•RCA Victor•1956','\
Various•Lullaby Of Birdland (Volume 2)•RCA•0','\
Various•Lullaby Of Birdland Vol. 3•RCA•0','\
Ella Fitzgerald•Later / Lullaby Of Birdland•Decca•1954','\
Ella Fitzgerald•Lullaby Of Birdland•Decca•1954','\
Kai Winding•An Afternoon At Birdland•"X"•1956','\
Astor Piazzolla Y Su Quinteto•Lullaby Of Birdland•Tico Records•1959','\
Frank Barcley His Piano And Rhythm•Something (Old New Borrowed Blue) Vol. 2•Metronome•1956','\
Ralph Flanagan And His Orchestra•Did I Remember / Lullaby Of Birdland•RCA Victor•0','\
Quire (2)•Ain\'t Misbehavin\'•RCA•0','\
Sarah Vaughan•Lullaby Of Birdland / September Song•EmArcy•0','\
Ted Heath And His Music•Seven Eleven•London Records•1954','\
Erroll Garner Trio•Lullaby Of Birdland / Easy To Love•Philips•0'),'\
\
Lullaby of Broadway\
':('\
Georgie Auld•Lullaby Of Broadway / Harlem Nocturne•Coral•1953','\
The Brasshats•Ring Dem Bells / Lullaby Of Broadway•Victory (5)•1946','\
David Rose & His Orchestra•Strings Of Fantasy•no label•1955','\
The Boswell Sisters•Fare Thee Well Annabelle / Lullaby Of Broadway •Decca•1936','\
The Andrews Sisters•My Dearest Uncle Sam•Decca•1947','\
Ella Fitzgerald•Ev\'ry Time We Say Goodbye•Honey Bee Records•1988','\
Norrie Paramor And His Orchestra•Holiday In New York•Columbia•1956','\
Georgie Auld•Manhattan With Strings•United Artists Records•1959','\
The Charlie Parker All-Stars•Summit Meeting At Birdland•Columbia•1977','\
Werner Müller Und Sein Orchester•Holiday In New York•Polydor•1956','\
The Art Van Damme Quintet•Lullaby Of Broadway•Philips•1957','\
Ellis Larkins•Manhattan At Midnight•Decca•1956'),'\
\
Lullaby of the Leaves\
':('\
Gerry Mulligan Quartet•Lullaby Of The Leaves / Walkin\' Shoes•Swing (3)•1953','\
Frank Barcley His Piano And Rhythm•Something (Old New Borrowed Blue) Vol. 2•Metronome•1956','\
Erroll Garner•Lullaby Of The Leaves / Margie•Atlantic•1951','\
Gerry Mulligan Quartet•Lullaby Of The Leaves / Bernie’s Tune•Pacific Jazz•1952','\
Benny Goodman Sextet•Lullaby Of The Leaves / Temptation Rag•Columbia•0','\
Art Tatum•Sweet Lorraine / Lullaby Of The Leaves•Brunswick•0','\
Dizzy Gillespie•Lullaby Of The Leaves / On The Alamo•Jazz Selection•1951','\
Nicolas Montier•Lullaby•Venus Records (5)•0','\
Gerry Mulligan Quartet•The Original Gerry Mulligan Quartet•Fontana•0','\
Art Tatum•Piano Solos•Brunswick•1957','\
Gerry Mulligan Quartet•Gerry Mulligan Quartet•Pacific Jazz•1954','\
Gerry Mulligan Quartet•Vol. 3•Vogue Productions•1955','\
Various•Jazz For A Sunday Afternoon Volume 1•Solid State Records (2)•1968'),'\
\
Lunar Tune\
':('\
Booker Ervin•The Freedom Book•Prestige•1964','\
Booker Ervin•The Freedom And Space Sessions•Prestige•1979','\
Various•The Avengers & Other Top Sixties TV Themes•Sequel Records•1998'),'\
\
Lush Life\
':('\
Tony Scott (2)•Lush Life•Core Records (3)•1989','\
The Nat King Cole Trio•Lush Life / Lillian•Capitol Records•1951','\
John Coltrane•Lush Life•Prestige•1963','\
Archie Shepp•Montreux One•Arista•1976','\
Bobby Timmons•This Here•Riverside Records•0','\
John Coltrane•My One And Only Love / Lush Life•Impulse!•1963','\
Nat King Cole•I Miss You So / Lush Life•Capitol Records•1951','\
Harry James And His Orchestra•Lush Life / I Don\'t Think You Love Me Anymore•Columbia•1953','\
Stan Getz Quartet•At Montreux•Polydor•1977','\
Anthony Braxton•In The Tradition•SteepleChase•1974','\
Howard Riley•10.11.12•NoBusiness Records•2015','\
Enrico Pieranunzi•A Long Way•Carosello•1978','\
George Lewis•The George Lewis Solo Trombone Record•Sackville Recordings•1977','\
Stan Getz Quartet•Portrait•Joker (2)•1977','\
Elia Fleta•Lush Life / This Can\'t Be Love / My Romance / Honeysuckle Rose•Concentric (2)•1967','\
Сергей Гурбелошвили•Classical Jazz Ballades•Мелодия•1990','\
Archie Shepp•The Free Jazz Tenorman•Editions Atlas•1991','\
Alix Pascal•Determinations•Ayizan Records Inc.•2003'),'\
\
Madagascar\
':('\
Wilbur De Paris And His New New Orleans Jazz•Madagascar - Are You From Dixie•Atlantic•1955','\
Mort Garson•Madagascar•MGM Records•1960','\
Hugo Winterhalter Orchestra•Theme From "Popi"•Musicor Records•0','\
Robert de Rycke•Shish-Kebab / Madagascar•Decca•0','\
John Abercrombie Quartet•Abercrombie Quartet•ECM Records•1980','\
The Players•Madagascar Lady•Openskye•1981','\
Jakob Magnússon•Special Treatment•Warner Bros. Records•1979','\
Weather Report•Night Passage•ARC (3)•1980','\
André Brasseur•On Fire!•RKM•1977'),'\
\
Magician In You\
':('\
Keith Jarrett•Keith Jarrett•Fabbri Editori•1980','\
Gary Burton•Good Vibes•Atlantic•1970','\
Keith Jarrett•Keith Jarrett•Fabbri Editori•1989','\
Keith Jarrett•Expectations•Columbia•1972','\
Dead Combo (2)•Odeon Hotel•Sony Music•2018','\
Various•Discobar Galaxie - 25 Light Years•N.E.W.S.•2019','\
Various•Berlin - Tag & Nacht 2 (Die Hits Der Coolsten WG Der Stadt) •Sony Music•2012','\
Various•Themes Like Old Times (90 Of The Most Famous Original Radio Themes)•Viva (3)•1969'),'\
\
Mahjong\
':('\
Sean Khan•Slow Burner•Far Out Recordings•2011','\
Will Calhoun•Celebrating Elvin Jones•Motéma•2016','\
Linc Chamberland•A Place Within•Muse Records•1977','\
Kiyoshi Kitagawa•Ancestry•Atelier Sawano•2004','\
Wayne Shorter•Juju•Blue Note•1964','\
Ginger Root•Mahjong Room•Acrophase Records•2018'),'\
\
Maiden Voyage\
':('\
Herbie Hancock•Spider•Columbia•1977','\
Herbie Hancock•Dedication•CBS/Sony•1974','\
Monday Michiru•Maiden Japan•Kitty Records•1994','\
Kenny Barron•Spiral•Eastwind•1984','\
Hutcherson-Land Quintet•Blow Up•Jazz Music Yesterday•1990','\
Chick Corea•An Evening With Chick Corea And Herbie Hancock•Polydor•1979','\
Herbie Hancock•Herbie Hancock And Chick Corea•CBS/Sony•1981','\
Karin Krog & Friends•Joy•Sonet•1968','\
Maynard Ferguson•Dimensions Vol. 1 Feat. Maynard Ferguson•EmArcy•0','\
Sharon Redd•Does Your Mama Know About Me•Columbia•1977','\
The V.S.O.P. Quintet•Tempest In The Colosseum•CBS/Sony•1977','\
Herbie Hancock•Herbie Hancock•Armando Curcio Editore•1991'),'\
\
Make Me a Memory (Sad Samba)\
':('\
Grover Washington Jr.•Just The Two Of Us•Elektra•1981','\
Grover Washington Jr.•Just The Two Of Us / Make Me A Memory (Sad Samba)•Elektra•1980','\
Grover Washington Jr.•Winelight•Elektra•1980'),'\
\
Make Someone Happy\
':('\
Jack Haskell•Make Someone Happy•Strand Records (2)•1961','\
The New Allegros•For Lovers Only•Roulette•1963','\
Ray Bloch And His Orchestra•You\'ve Got To Make Someone Happy / Skating•Columbia•1954','\
J. Lawrence Cook•I\'m A Sugar Daddy / Make Someone Happy Today•Abbey (2)•1950','\
Jimmy Durante•Make Someone Happy•Warner Bros. Records•1996','\
Woody Herman And His Orchestra•Live In Seattle•Moon Records (4)•1989','\
Ahmad Jamal•Live At The Montreal Jazz Festival 1985•Atlantic•1986','\
Stanley Turrentine•In Memory Of•Blue Note•1979','\
Dianne Reeves•Bridges•Blue Note•1999','\
Stanley Turrentine•In Memory Of•Blue Note•1979','\
Walter Bishop Jr.•Valley Land•Muse Records•1976','\
Kenny Burrell•Special Requests (And Other Favorites) Live At Catalina\'s•HighNote Records Inc.•2013','\
Barney Kessel•Poor Butterfly•Concord Jazz•1977','\
Bobby Timmons•Soul Food•Prestige•1966','\
J.J. Johnson•J.J.\'s Broadway•Verve Records•1963','\
Bill Evans•Alone (Again)•Fantasy•1977','\
Jane Bunnett•New York Duets•EMI Music Canada•1989'),'\
\
Mallet Man\
':('\
Gary Burton•The New Quartet•ECM Records•1973','\
Chico Hamilton•Man From Two Worlds•Impulse!•1964'),'\
\
Mamacita\
':('\
Kenny Dorham•Mamacita•Blue Note•1964','\
Kenny Dorham•Trompeta Toccata•Blue Note•1965','\
Blue Mitchell•Step Lightly•Blue Note•1980','\
David Sanborn•Sanborn•Warner Bros. Records•1976','\
Rob Agerbeek Quintet•Home Run•Polydor•1972','\
Rob Agerbeek Quintet•Home Run•Polydor•1972','\
Joe Henderson Sextet•The Kicker•Milestone (4)•1968','\
Teddy Edwards Sextet•It\'s All Right•Prestige•1967'),'\
\
Man Facing North\
':('\
Yellowjackets•Like A River•GRP•1993','\
Yellowjackets•Raising Our Voice•Mack Avenue Records•2018','\
Yellowjackets•Collection•GRP•1995'),'\
\
Man I Love The\
':('\
Norman Granz•Jazz At The Philharmonic Vol 11•Mercury•1951','\
Jazz At The Philharmonic•Norman Granz\' Jazz At The Philharmonic - Vol. 11•Mercury•0','\
Clark Terry Septet•Cats vs. Chicks (A Jazz Battle Of The Sexes)•MGM Records•1954','\
Tex Beneke And His Orchestra•Poinciana / The Man I Love•RCA Victor•1948','\
The Benny Goodman Quartet•Avalon / The Man I Love•no label•0','\
Gene Norman•Just Jazz Concert - Star Dust / The Man I Love•Decca•1951','\
Miles Davis•Miles Davis And The Modern Jazz Giants•Prestige•1959','\
Billie Holiday•Night And Day / The Man I Love•Vocalion (2)•1939','\
Art Tatum Trio•The Man I Love / I Know That You Know•Dial Records (3)•1949','\
Miles Davis•Miles Monk & Milt•Prestige•1966','\
Miles Davis All Stars•Miles Davis All Stars (Vol. 2)•Prestige•1955','\
Coleman Hawkins Swing Four•The Man I Love / Sweet Lorraine•Signature (4)•1944','\
Lionel Hampton And His Orchestra•The Man I Love / Oh Babe•Decca•0','\
Miles Davis•Miles Davis And The Modern Jazz Giants•Prestige•1969','\
Kenny Burrell•Blue Lights Vol. 2•Blue Note•1958'),'\
\
Man In the Green Shirt\
':('\
Weather Report•Tale Spinnin\'•Columbia•1975','\
Weather Report•This Is Jazz 10 - Weather Report•Columbia•1996','\
Weather Report•The Best Of Weather Report•Columbia•2002','\
Various•Celebrating The Music Of Weather Report•Telarc•2000','\
Weather Report•Collections•Sony BMG Music Entertainment•2008','\
Weather Report•Live & Unreleased•Columbia•2002','\
Weather Report•The Columbia Albums 1971-1975•Columbia•2012','\
Frank Zappa•антология творчества часть 3-4•Домашняя Коллекция•2004'),'\
\
Man That Got Away The\
':('\
Judy Garland•April Showers•Capitol Records•0','\
Tommy Dorsey And His Orchestra•The Man That Got Away / The High And The Mighty•Bell Records•1954','\
Georgia Gibbs•The Man That Got Away / More Than Ever•Mercury•1954','\
Tommy Dorsey And His Orchestra•Dance Party II•Varieton•1955','\
Fran Warren•Just Friends•MGM Records•1958','\
Georgia Gibbs•The Man That Got Away•Mercury•1955','\
Various•Great Jazz Artists Play Compositions Of Harold Arlen•Riverside Records•1961','\
The Gerald Wiggins Trio•Wiggin With Wig•Dig Records•1956','\
Shirley Bassey•The Wonderful Shirley Bassey•Music For Pleasure•1973','\
Etta Jones•Save Your Love For Me•Muse Records•1981','\
Joe Bushkin•In Concert Town Hall•Reprise Records•1964','\
Dizzy Gillespie•Concert In Paris•Royal Roost•1957','\
Frank Strozier•Long Night•Jazzland•1961','\
Shirley Bassey•The Golden Sound Of Shirley Bassey•MGM Records•1965','\
Rosemary Clooney•Rosemary Clooney Sings The Lyrics Of Ira Gershwin•Concord Jazz•1980','\
Mark Andrews & His Orchestra•Music For Lonely Lovers•Promenade•1957','\
Peter Appleyard Orchestra•Percussive Jazz•Audio Fidelity•1960','\
Art Tatum•The Tatum Solo Masterpieces Vol. 4•Pablo Records•1975','\
Coleman Hawkins•Good Old Broadway•Moodsville•1962'),'\
\
Manha de Carneval\
':('\
Baden Powell•Tristeza On Guitar•SABA•1966','\
Jacintha•Lush Life•Groove Note•2001','\
Jacintha•Best Of Jacintha•Groove Note•2008','\
Mario Pezzotta E La Sua Orchestra•Anni \'50 L\'Era Del Night•Durium•1974','\
Lars Erstrand Quartet•Dream Dancing•Opus 3 Records•1991','\
Baden Powell•Three Originals (Tristeza On Guitar/Poema On Guitar/Apaixonado)•MPS Records•1993','\
Fausto Papetti•Isn\'t It Saxy?•Heartbeat (6)•1988','\
Jens Brenke•Die Mitternachtsplatte•Electrola•1964'),'\
\
Manteca\
':('\
Dizzy Gillespie And His Orchestra•Manteca / Cool Breeze•RCA Victor•1949','\
Gene Norman•Manteca - Emanon - Good Bait•Gene Norman Presents•1955','\
Tatsuya Takahashi 3•Impression•Audio Lab. Record•1980','\
Dizzy Gillespie•Cool Breeze•RCA Victor•1952','\
Shelly Manne & His Men•The Manne We Love•Eastworld•1979','\
Marty Wilson And His Orchestra•Jun\'gala•Warner Bros. Records•1961','\
Dizzy Gillespie•Gillespie En Vivo•Areito•1985','\
The Red Garland Trio•Manteca•Prestige•1958','\
LA4•The L.A.4•Concord Jazz•1976'),'\
\
Masquerade\
':('\
George Benson•This Masquerade•Warner Bros. Records•1976','\
Naoyuki Fujii•Manhattan•Pony Canyon•1988','\
Thomas Diethelm•The Flyer•Polydor•1983','\
no artist•Norwegian Wood•A&M Records•1970','\
Frankie Carle And His Orchestra•Rockin\' Horse Cowboy / Midnight Masquerade•Columbia•1947','\
Alvino Rey And His Orchestra•Mama Blues / Midnight Masquerade•Capitol Records•1947','\
Johnny Hammond•The Masquerade Is Over / All Soul•New Jazz•1959','\
Lou Donaldson•Blues Walk•Blue Note•1958','\
Sonny King (2)•Masquerade / You\'re Nobody Till Somebody Loves You•Colpix Records•1959','\
Lou Donaldson•Blues Walk•Blue Note•1958','\
Keith Jarrett•God Bless The Child (Edit)•ECM Records•1983','\
George Benson•This Masquerade / Breezin\'•Warner Bros. Records•1976','\
George Benson•This Masquerade•Warner Bros. Records•1976','\
The Dave Brubeck Quartet•Jazz Goes To Junior College: I\'m Afraid The Masquerade Is Over / St. Louis Blues•Columbia•1957'),'\
\
Masquerade is Over\
':('\
Johnny Hammond•The Masquerade Is Over / All Soul•New Jazz•1959','\
Lou Donaldson•Blues Walk•Blue Note•1958','\
Keith Jarrett•God Bless The Child (Edit)•ECM Records•1983','\
The Dave Brubeck Quartet•Jazz Goes To Junior College: I\'m Afraid The Masquerade Is Over / St. Louis Blues•Columbia•1957','\
Jimmy Dorsey And His Orchestra•Let\'s Stop The Clock / The Masquerade Is Over•Decca•1939','\
Jimmy Witherspoon•I Don\'t Know•Reprise Records•1961','\
Jimmy Scott•What Good Would It Be / The Masquerade Is Over•Sharp Record Co.•1959','\
Paul Bryant•Something\'s Happening•Fantasy•1963','\
George Benson•Blue Bossa •Blue Moon Productions•2006','\
The Dave Brubeck Quartet•Back Home•Concord Jazz•1979','\
The George Benson Quartet•Live At "Casa Caribe" Volume 1•Jazz View•0'),'\
\
Matinee Idol\
':('\
Yellowjackets•Matinee Idol•Warner Bros. Records•1981','\
Yellowjackets•Yellowjackets•Warner Bros. Records•1981','\
Rufus Wainwright•Rufus Wainwright•DreamWorks Records•1998','\
Yellowjackets•The Best Of•Warner Bros. Records•1999','\
Yellowjackets•Twenty Five•Heads Up International•2006'),'\
\
May Dance\
':('\
Togashi-Yamashita Duo•Kizashi (兆)•Next Wave•1980','\
John Abercrombie•Gateway•ECM Records•1975','\
Miles Davis•Blue Christmas•CBS•1983','\
Arild Andersen•Celebration•ECM Records•2012','\
Sammy Kaye•May I Still Hold You / Friendly Mountains•RCA Victor•1948','\
Brian Hughes•Between Dusk...And Dreaming•Justin Time Records•1990','\
Guy Luypaerts•The Esquire Album Of Music For The Continental Host•RCA Victor•1955','\
The Silver Strings (3)•The Silver Strings•Deacon Records•1971','\
Nicolas Simion Group•Balkan Jazz•Intuition Records•2001','\
Masahiko Satoh•MSB•Openskye•1980','\
Miles Davis•Basic Miles - The Classic Performances Of Miles Davis•Columbia•1973','\
Pete Brown & Piblokto!•Things May Come And Things May Go But The Art School Dance Goes On Forever•Harvest•1970','\
Sunset Hills Hotel•Reservation Calendar•Interface (3)•1987'),'\
\
Mean to Me\
':('\
Etta Jones•Osculate Me Daddy / Mean To Me•RCA Victor•1946','\
Sarah Vaughan•Mean To Me / Signing Off•Continental (6)•1946','\
The Tony Kinsey Quintet•Mean To Me•Decca•0','\
no artist•Mean To Me / My Kinda Love•Victor•1929','\
Walter Gil Fuller And His Orchestra•Mean To Me / The Scene Changes•Vogue Records•0','\
Lester Young Trio•Man I Love•Clef Records•1953','\
Rose Murphy•Mean To Me / Lindy Lou•Decca•1955','\
Sarah Vaughan•Mean To Me / Interlude Night In Tunisia•Vogue Productions•0','\
Sarah Vaughan•Mean to Me / What More Can a Woman Do?•Lenox (2)•1948','\
Lil Armstrong And Her Swing Band•Let\'s Call It Love / You Mean So Much To Me•Decca•1937','\
Johnny Guarnieri•Nobody\'s Sweetheart•Royale•0','\
The Modern Jazz Sextet•The Modern Jazz Sextet•Verve Records•0','\
The Modern Jazz Quartet•Star-Collection•Midi•1972','\
Della Reese•The Most Beautiful Words / You Mean All The World To Me•RCA•1961','\
Buck Clayton•Jazz Gallery•Philips•1959','\
Georges Arvanitas Trio•Cocktail For Three•Pretoria•1959'),'\
\
Meditation\
':('\
Yusef Lateef•Meditations•Atlantic•1990','\
Jabrane M. Sebnat\ufeff•Meditation Of The Directions•Alifia International AB•0','\
John Coltrane•Transition•Impulse!•1970','\
Friedrich Gulda•The Air From Other Planets•MPS Records•1969','\
Teddy Stauffer Und Seine Original Teddies•St. Louis Blues / Meditation•Telefunken•1938','\
Astrud Gilberto•Meditation / And Roses And Roses•Verve Records•1965','\
Bruno Henriksens Danseorkester•Meditation / In The Mood•Odeon•0','\
Dick Sells•Muzik Zur Meditation•Not On Label (Robert Julian Horky Self-released)•1982','\
Abdullah Ibrahim•No Fear No Die (S\'en Fout La Mort)•Tiptoe•1990'),'\
\
Mellow Mood\
':('\
Dodo Marmarosa Trio•Mellow Mood / How High The Moon•Atomic Records (12)•1945','\
Jimmy Smith•Further Adventures Of Jimmy And Wes•Verve Records•1969','\
Kenny Burrell•For Duke•Fantasy•1980','\
Kenny Burrell•For Duke•Fantasy•1980','\
The Ellington All Stars•In A Mellow Tone•Riverside Records•1968','\
Marcus Roberts•Plays Ellington•Novus•1995','\
Al Grey•Grey\'s Mood•Black And Blue•1976','\
The Jazzinvaders•That\'s What You Say!•Unique•2013','\
Sathima Bea Benjamin•Sathima Sings Ellington•Ekapa•1979','\
no artist•Volume 2•KHY Suomen Musiikki Oy•2015','\
Duke Ellington•This Is Jazz │ 7•Columbia•1996'),'\
\
Memories of Tomorrow\
':('\
Iskra (3)•A New Day•Polydor•1986','\
Hitoshi Hamada•Memories Of Tomorrow•Audio Lab. Triangle•0','\
Ulf Wakenius•Notes From The Heart (Plays The Music Of Keith Jarrett)•ACT (4)•2006','\
Kim Pensyl•Eyes Of Wonder•GRP•1993','\
Bill Coleman (2)•Bill And The Boys•Concert Hall•1972','\
Various•18 Top Hits•18 Top Hits•1955','\
Jeff Victor•Summer Sojourn•NorthWord Press•1995','\
David Becker Tribune•Leaving Argentina•Straw House•2007','\
Cleveland Watkiss•Blessing In Disguise•Polydor•1991','\
Bob James•The New Cool•Yamaha Music Communications•2015','\
Lillian Boutté•But ... Beautiful•Dinosaur Entertainment•1996','\
Mark Turnbull•Portrait Of The Young Artist•Reprise Records•1968','\
Various•Memories Are Made Of This•Ronco•1981','\
Various•20 Fabulous No 1\'s Of The 50\'s•Music For Pleasure•1984','\
The Free Design•Raindrops•Siesta•1998','\
Various•Sentimental Journey•Teledisc•1991'),'\
\
Memories Of You\
':('\
Rafael Mendez•Memories Of You•Decca•0','\
Benny Goodman Sextet•Soft Winds / Memories Of You•Columbia•0','\
Zoot Sims Quartet•Jane-O / Memories Of You•Prestige•1950','\
The John Young Trio•You Go To My Head / Memories Of You•Chance Records (3)•1953','\
Joe "Fingers" Carr•Memories Of You / Henderson Stomp•Capitol Records•0','\
Paul Weston And His Orchestra•Memories Of You/The Naked Sea•Columbia•1955','\
Robert Wyatt•Shipbuilding / Memories Of You•Rough Trade•1982','\
Illinois Jacquet And His All Stars•Memories Of You / Merle\'s Mood•Apollo Records (2)•1946','\
no artist•Memories Of You / Autumn Rhapsody•RCA Victor•0','\
Thelonious Monk•The Unique Thelonious Monk•Riverside Records•1956','\
The Pud Brown Trio•Take The "A" Train / Memories Of You•Capitol Records•1953','\
Benny Goodman Trio•The Benny Goodman Story Volume 4•Decca•0','\
Lionel Hampton And His Orchestra•Memories Of You / The Jumpin\' Jive•Victor•1939','\
Benny Goodman Trio•The Benny Goodman Story Volume 2 Part 1•Brunswick•1956','\
Benny Goodman Sextet•Memories Of You / King Porter Stomp•Columbia•0','\
Burnie Peacock & His Orchestra•Charmaine / Memories Of You•King Records (3)•1951','\
Chuck Hedges•Clarinet Climax•Jazzology•1983','\
Glen Gray & The Casa Loma Orchestra•If I Love Again / Memories Of You•Decca•0'),'\
\
Memphis Underground\
':('\
Herbie Mann•Memphis Underground / New Orleans•Atlantic•1969','\
Eddie Harris•Listen Here / Memphis Underground•Atlantic•0','\
Herbie Mann•It\'s A Funky Thing - Right On•Atlantic•1969','\
Larry Coryell•Difference•Egg•1978','\
Herbie Mann•Memphis Underground•Atlantic•1969','\
Herbie Mann•Mellow•Atlantic•1981'),'\
\
Menina Flor\
':('\
Nelson Martins Dos Santos•Nelsinho E Seus Trombones•Magisom•1963','\
Stan Getz•The Very Best Of Stan Getz•Verve Records•0','\
Octeto De César Camargo Mariano•Octeto De César Camargo Mariano•Som Maior•1965','\
Walter Wanderley•O Autêntico Walter Wanderley•Philips•1965','\
Julinho (7)•O Som Do Julinho•Equipe•1969','\
Hélio Mendes•Na Bossa•MUSIPLAY•0','\
Wilson Simonal•Charme Tropical•Fermata•1985','\
The Dutch Swing College Band•Latin On The Rocks•DSC Production•1972','\
Quarteto Arpoador•Bossa No Castelinho•Esquema•0','\
Os Catedráticos•Tremendão•Equipe•1964','\
Caterina Valente•Caterina Valente E Luiz Bonfá•London Records•1963','\
Zimbo Trio•Zimbo Trio•RGE•1964','\
Zimbo Trio•Vol. II•Fermata•1971','\
Luiz Bonfá•Recado Novo•Odeon•1963','\
Maria Toledo•Sings The Best Of Luiz Bonfa•United Artists Records•1967','\
Maria Toledo•Sings The Best Of Luiz Bonfa•United Artists Records•1967'),'\
\
Mercy Mercy Mercy\
':('\
Cannonball Adderley•Mercy Mercy Mercy•Capitol Records•1966','\
Buddy Rich Big Band•Mercy Mercy Mercy / Big Mama Cass•Pacific Jazz•1968','\
no artist•Cat Call•Marmalade•1967','\
Art Farmer Quintet•Mercy Mercy Mercy•Columbia•0','\
The Zawinul Syndicate•No Mercy For Me (Mercy Mercy Mercy)•Columbia•1988','\
Cannonball Adderley•Mercy Mercy Mercy•Capitol Records•0','\
Grover Washington Jr.•Mercy Mercy Me•Kudu•1972','\
Nancy Wilson•Mercy Mercy Mercy•Capitol Records•1967','\
Milira•Mercy Mercy Me (The Ecology)•Motown•1990','\
Mayafra Combo•Mayafra•Carosello•1978','\
Cannonball Adderley•Cannonball - Volume One•Dobre Records•1977','\
The Cannonball Adderley Quintet•Cannon-ball In Japan•Capitol Records•1966','\
Giovanni Hidalgo•Villa Hidalgo•Messidor•1992'),'\
\
Metamorphosis\
':('\
Arthur Blythe•Metamorphosis•India Navigation•1979','\
Sonny Simmons•Staying On The Watch•ESP Disk•1966','\
The Bill Dixon Orchestra•Intents And Purposes•RCA Victor•1967','\
Arthur Blythe•Elaborations•CBS•1982','\
The Horace Silver Quintet•The Stylings Of Silver•Blue Note•1957','\
George Adams Quintet•Paradise Space Shuttle•Timeless Muse•1979','\
Elation (11)•Elation•Acheulian Handaxe•2018'),'\
\
Mevlevia\
':('\
Gary Burton Quintet•Ring•ECM Records•1974','\
Mozaik (6)•Ardından•Ada Müzik•1985'),'\
\
Michelle\
':('\
Bud Shank•Michelle •Ricordi International•1966','\
Stan Getz•Early Stan•Prestige•1963','\
Al Hirt•Sweet Sauce•Monument•1974','\
Bud Shank•Michelle / Ontem A Note•World Pacific Records•1966','\
Stan Getz Quartet•Too Marvelous For Words / Michelle•Prestige•0','\
Masahiko Sato Trio•Palladium•Express•1969','\
Gato Barbieri•Obsession•Affinity•1978','\
Les Baxter & His Orchestra•Michelle•Hanna-Barbera Records•1965','\
Ramsey Lewis•Lakeshore Cowboy•Columbia•1981','\
Gato Barbieri Quartet•In Search Of The Mystery•ESP Disk•1967','\
Pheeroan Aklaff•House Of Spirit: Mirth•no label•1980','\
Dominique (25)•Chante... Michelle•Trianon•1966','\
The Sandpipers•For Baby•A&M Records•1967','\
Albert Dailey Trio•That Old Feeling•SteepleChase•1979'),'\
\
Midland\
':('\
Billy Childs•Twilight Is Upon Us•Windham Hill Records•1989'),'\
\
Midnight Mood\
':('\
Chas. Johnson Orchestra--Midnight Mood / Rompin\' On The Ramp--Prize (2)--1949','\
Joe Harriott--Journey--Moonlight Tunes--2011','\
Danilo Perez--Panamonk--Impulse!--1996','\
The Bill Evans Trio--Camp Fortune 1974--Radio Canada International--1976','\
Masao Yagi--Masao Yagi Plays Thelonious Monk--King Records--1960','\
Frank Morgan--Mood Indigo--Antilles--1989'),'\
\
Midnight Silence\
':('\
Charlie Haden•Silence•Soul Note•1989','\
Kenny Kirkland•Kenny Kirkland•GRP•1991','\
Lonnie Plaxico•Plaxico•Muse Records•1990','\
Martin Taylor•Kiss And Tell•Columbia•1999','\
Various•Conrad Silvert Presents Jazz At The Opera House•Columbia•1983','\
Steve Coleman And Five Elements•On The Rising Of The 64 Paths•Label Bleu•2003','\
The Mystic Moods Orchestra•Sampler•Soundbird (2)•1975','\
Андрей Рябов•Джаз Tête-À-Tête•Мелодия•1988','\
Various•For Example - Workshop Freie Musik 1969 - 1978•FMP•1978','\
Carmen McRae•Live At Century Plaza•Atlantic•1975','\
Charles Coleman•Plays•Jubilee•1969','\
Eric Winstone & His Orchestra•Stay Later•Stereo Plus 3•1973','\
Ferrante & Teicher•Midnight Cowboy•United Artists Records•1969'),'\
\
Midnight Sun\
':('\
Coleman Hawkins•Midnight Sun / Spellbound•Decca•0','\
Akiko•Waters Of March•Verve Records•2002','\
Les Brown And His Band Of Renown•Ruby / Midnight Sun •Coral•1953','\
Les Brown And His Band Of Renown•Ruby / Midnight Sun•Coral•1953','\
Lionel Hampton And His Orchestra•Jelly Roll•Brunswick•0','\
Leroy Lovett•Midnight Sun / Unchained Melody•Atlantic•1954','\
Lionel Hampton And His Orchestra•Midnight Sun / Airmail Special•Clef Records•1955','\
Lionel Hampton And His Orchestra•Midnight Sun•Glad-Hamp Records•0','\
Lionel Hampton And His Septet•Blow-Top Blues / Midnight Sun•Decca•1952','\
Ella Fitzgerald•The Swingin\' Shepherd Blues / Midnight Sun•no label•1957','\
Barney Kessel•To Swing Or Not To Swing•Contemporary Records•0','\
Harry James And His Orchestra•Dancing At The Palladium•Philips•1954','\
no artist•Mambo With Tjader Volume 1•Fantasy•0','\
Márta Szirmay•Modern Jazz•Qualiton•1963','\
Harvey Mandel•Baby Batter / Midnight Sun•Janus Records•1972','\
Air (4)•Air Raid•Whynot•1976','\
Brother Jack McDuff•The Midnight Sun•Prestige•1968','\
Quincy Jones•Quincy\'s Home Again•Metronome•1958','\
Mezzoforte•Midnight Sun•Steinar•1984','\
Marv Meredith•Strings And All That Jazz!•Strand Records (2)•1959'),'\
\
Midnight Sun Will Never Set\
':('\
Sarah Vaughan•Sarah With Feeling•Mercury•1959','\
Gustav Brom•Gustav Brom Plays Quincy Jones•Supraphon•0','\
Eric Alexander•Gentle Ballads•Venus Records (5)•2005','\
Acker Bilk•Call Me Mister•Metronome•0','\
Benny Carter And His Orchestra•Further Definitions•Impulse!•1962','\
Johnny Griffin•Do Nothing \'Til You Hear From Me•Riverside Records•1963','\
Earl Van Riper•Detroit\'s Grand Piano Man•Parkwood Records•1987','\
Freddie Roach•Brown Sugar•Blue Note•1964','\
Kunihiko Sugano•Sincerely Yours•Paddle Wheel•1980'),'\
\
Milano\
':('\
The Modern Jazz Quartet•The Modern Jazz Quartet Plays Django ･ Milano•Prestige•1955','\
Jimmy Pratt•Madison Str Milano / Cheek To Cheek - Jimmy Pratt Presents Herb Geller And His Saxophone•Variety (2)•1962','\
The Modern Jazz Quartet•Vol. 2: Django / Milano / One Bass Hit•Metronome•1955','\
Bob Cooper•Milano Blues•Music•1959','\
The Dining Rooms•Milano Calibro 9 / No Problem•Schema•2005','\
Don Pullen•Milano Strut•Black Saint•1979','\
Similado•Capriccio A Milano•Elicona Edizioni Musicali•1990','\
Tullio De Piscopo•Oulelè Magidì•Costa Est•1991','\
The Modern Jazz Quartet•The Modern Jazz Quartet Plays Jazz Classics•Prestige•1966','\
The Modern Jazz Quartet•The Modern Jazz Quartet•Prestige•1955','\
Toshiko Akiyoshi Jazz Orchestra•Wishing Peace From "Liberty Suite"•Ascent Records (2)•1986','\
The Modern Jazz Quartet•Los Grandes Del Jazz 5•Sarpe•1980','\
The John Lewis Group•Kansas City Breaks•Finesse Records (3)•1982','\
The 360 Degree Music Experience•Beautiful Africa•Soul Note•1979','\
Maad•Maad•Divergo (2)•1976'),'\
\
Miles Ahead\
':('\
The Miles Davis Quartet•When Lights Are Low / Miles Ahead•Prestige•1955','\
Miles Davis•Miles Davis 1957-1958 Meets Gil Evans Julian "Cannonball" Adderley John Coltrane Bill Evans•Giants Of Jazz•1989','\
The Miles Davis Quartet•When Lights Are Low•Prestige•1953','\
Miles Davis•Miles Davis Transcribed Solos•JA Records•1980','\
Miles Davis•Mellow Miles•Columbia•1991','\
The Miles Davis Quartet•Miles Davis Quartet•Prestige•2011','\
The Miles Davis Quartet•Miles Davis Quartet•Prestige•1954'),'\
\
Mine is Yours\
':('\
Joe Henderson•Jazz Patterns•Everest Records Archive Of Folk & Jazz Music•0','\
David Liebman Group•Turn It Around•Owl Records (4)•1992','\
Ray Brown•Bass Hit!•Verve Records•1957','\
Don Tweedy And His Orchestra•To Lovers With Love•Target Records (8)•1972','\
Bob Mintzer•Spectrum•DMP•1988','\
Julie London•Julie London Sings Latin In  A Satin Mood•Liberty•1963','\
Stan Getz•The Final Concert Recording•Eagle Records•2000','\
Vi Redd•Lady Soul•Atco Records•1963','\
Django Reinhardt•Djangologie 15 (1946-1947)•Pathé•0','\
Artie Kaplan•Greatest Hits•Edigsa•1982','\
Various•All Dogs Go To Heaven: Original Motion Picture Soundtrack•Curb Records•1989'),'\
\
Minor Mishap\
':('\
Pepper Adams•Critics\' Choice•World Pacific Records•1957','\
Tommy Flanagan•The Cats•New Jazz•1959','\
The Master Trio•The Master Trio•Baybridge Records•1983','\
Freddie Hubbard•Groovy!•Fontana•1966','\
Andy Panayi Quartet•Blown Away•RSJH Music Limited•1998','\
Duke Pearson•Dedication!•Prestige•1970','\
Tommy Flanagan Trio•Flanagan\'s Shenanigan\'s•Storyville•1994','\
Nisse Sandström•Home Cooking•Phontastic•1981','\
Kenny Burrell•Prestige Profiles•Prestige•2006','\
Kenny Burrell•Kenny Burrell / John Coltrane•Prestige•1976','\
Various•Aurex Jazz Festival (1982): All Star Jam•Eastworld•1982'),'\
\
Minor Mood\
':('\
Errol Parker Trio•Opus•Brunswick•1964','\
Milt Jackson•Jackson\'sville•Savoy Records•1956','\
Yusef Lateef•Other Sounds•New Jazz•1959','\
Idea6•Metropoli•Dejavu•2006','\
Idea6•Remix Vol 1•Dejavu•2006','\
Paul Gonsalves•Just Friends•Columbia•1965','\
Stanley Turrentine•Stan "The Man" Turrentine•Time Records (3)•0','\
Clifford Brown•New Star On The Horizon•Blue Note•1953','\
Don Friedman•Later Circle•Baystate•1983'),'\
\
Minority\
':('\
Clifford Brown•The Paris Collection Vol. 2•Disques Vogue P.I.P.•1979','\
Art Blakey•Salute To Birdland•Mercury•1954','\
The Ramsey Lewis Trio•Them Changes / Unsilent Minority•Cadet•1970','\
Pat Martino•Strings!•Prestige•1968','\
Bill Evans•Minority•Riverside Records•0','\
Jack DeJohnette•Jackeyboard•Trio Records•1973','\
Donald Byrd•Kofi•Blue Note•1995','\
Gigi Gryce Clifford Brown Sextet•"Jazz Time Paris" Vol. 11•Vogue Productions•0','\
Gigi Gryce Quintet•The Hap\'nin\'s•Prestige•1960','\
Bobby Watson (2)•Beatitudes•New Note Records•1985','\
Art Blakey•Blakey•EmArcy•1955','\
Tommy Chase Quartet•Hard!•Boplicity Records•1984','\
Red Mitchell•Blues For A Crushed Soul•Sonet•1978','\
The Cannonball Adderley Quintet•Portrait Of Cannonball•Riverside Records•1958','\
Frank Wess•Two At The Top•Uptown Records (2)•1983','\
Jack DeJohnette•The Jack DeJohnette Piano Album•Landmark Records (3)•1985','\
Frank Foster•The Loud Minority•Mainstream Records•1974'),'\
\
Minute By Minute\
':('\
Larry Carlton•Minute By Minute•MCA Records•1987','\
Stanley Clarke•Live At The Greek•Slamm Dunk•1994','\
Various•The Premiere Collection Volume I•MCA Records•1990','\
Larry Carlton•Collection•GRP•1990','\
Larry Carlton•Discovery•MCA Records•1987','\
Al Martino•Just Yesterday•Capitol Records•1966','\
Bobby Lyle•Hands On•Heads Up International•2006','\
Larry Carlton•New Morning: The Paris Concert•335 Records Inc.•2011','\
Nicolas Humbert•Step Across The Border•RecRec Music•1991','\
Run_Return•Sum Of An Abstract•Boombox•2002','\
Charles Tyler•Sixty Minute Man•Adelphi Records Inc.•1980','\
Harold Ashby Quartet•Born To Swing•Master Jazz Recordings•0','\
Keshavan Maslak•Loved By Millions•Leo Records•1981','\
HiM•1110•After Hours•2008'),'\
\
Misty\
':('\
Richard "Groove" Holmes•Misty•Prestige•1965','\
Erroll Garner•Quartet•UP•1977','\
Georgie Auld•Manhattan•Coral•0','\
Willie Mitchell•Barefootin\'•Hi Records•1967','\
Jam Session N• 6•Misty Sunrise / China Boy•Swing (3)•1947','\
Claude McLin•Misty / Satin Doll•Allegro (12)•1960','\
Chris Connor•Senor Blues•Atlantic•1960','\
Sam Taylor (2)•Misty / Darn That Dream•Decca•1962','\
Erroll Garner Trio•Misty / Exactly Like You•Mercury•1954','\
Duke Ellington And His Orchestra•Misty Mornin\' / Saratoga Swing•no label•1938','\
Chris Connor•Senor Blues•Atlantic•1960','\
Eddie "Lockjaw" Davis•Misty / In The Kitchen•Prestige•1963','\
Erroll Garner•Misty / Dreamy•Columbia•0','\
Various•Newport In New York \'72 - The Jam Sessions Vol 3•Atlantic•1972','\
Erroll Garner•Misty / Solitaire•Columbia•1959'),'\
\
Miyako\
':('\
Wayne Shorter•Schizophrenia•Blue Note•1969','\
Ricky Ford•Shorter Ideas•Muse Records•1985','\
Jane Ira Bloom•As One•JMT Productions•1985','\
Christian McBride•Number Two Express•Verve Records•1996','\
The Fred Hersch Trio•Horizons•Concord Jazz•1985','\
Wojciech Jachna•Sundial II•Hevhetia•2016','\
Jimmy Rowles•Music\'s The Only Thing On My Mind•Progressive Records (2)•1981','\
The John Dentz Reunion Band•December 5 & 6•M & K Realtime Records•1981','\
Fred Hersch•Songs Without Words•Nonesuch Records•2001'),'\
\
Mo\' Joe\
':('\
The Horace Silver Quintet•The Cape Verdean Blues•Blue Note•1965','\
Joe Henderson Sextet•The Kicker•Milestone (4)•1968','\
Dizzy Gillespie•Jambo Caribe•Limelight•1964','\
Various•The Story So Far (The Sampler) (Essential Argo / Cadet Grooves)•Charly Records•1994','\
Jerry Granelli•Music Has Its Way With Me•Perimeter Records (3)•1999'),'\
\
Moanin\'\
':('\
Art Blakey & The Jazz Messengers•Moanin\'•Blue Note•1958','\
Lambert Hendricks & Ross•Moanin\' / Cloudburst•Columbia•1959','\
Bobby Timmons•Moanin\'•Riverside Records•0','\
Art Blakey•Blues March / Moanin•Blue Note•1976','\
Benny Golson•Blues March•Columbia•1960','\
Art Blakey & The Jazz Messengers•Blues March / Moanin\'•CBS•0','\
Benny Golson•Blues March•Columbia•1960','\
Duke Ellington And His Orchestra•The Mystery Song / Moanin\'•Victor•1931','\
no artist•Moanin\' Low / Ring Dem Bells•Parlophone•1931','\
Beryl Bryden•Moanin\'•Columbia•1962','\
Leo Reisman And His Orchestra•Moanin\' Low / Ain\'t Misbehavin•Victor•1929','\
Art Blakey & The Jazz Messengers•Moanin\' / Justice•Fontana•1960'),'\
\
Modadji\
':('\
Hubert Laws•The San Francisco Concert•CTI Records•1977'),'\
\
Modesty Blues\
':('\
Eric Le Lann Quartet•I Mist You•Blue Silver•1986','\
Various•The Soul Of Jazz Volume 1•Gitanes Jazz Productions•1995'),'\
\
Molten Glass\
':('\
Joe Farrell Quartet•Joe Farrell Quartet•CTI Records•1970','\
The Muffins•Chronometers•Cuneiform Records•1993'),'\
\
Moment\'s Notice\
':('\
Joey Alexander•Eclipse•Motéma•2018','\
Slide Hampton•Exodus•Philips•1962','\
no artist•Blood Lines •Milestone (4)•1999','\
Various•JJ 69 - New Faces In Polish Jazz•Polskie Nagrania Muza•1970','\
René Urtreger•Pianos Puzzle•PDU•1972','\
Tubby Hayes•England´s Late Jazz Great•IAJRC•1987'),'\
\
Monk On The Run\
':('\
Various•Everything I Do Gonna Be Funky•Brown Sugar Records•2004'),'\
\
Monkey\'s Uncle\
':('\
Various•Les Triomphes Du Blues•Habana•2001','\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014'),'\
\
Monk\'s Mood\
':('\
Bennie Wallace•Live At The Public Theater•Enja Records•1978','\
Michele Rosewoman Quartet•The Source•Soul Note•1984','\
Brian Smith•Southern Excursion•Ode Records•1984','\
Enrico Intra•The Blues•Dire (2)•1991','\
Gary Bartz•Reflections On Monk - The Final Fronteer•SteepleChase•1989','\
Masao Yagi•Masao Yagi Plays Thelonious Monk•King Records•1960','\
The Thelonious Monk Quartet•At Carnegie Hall•Blue Note•2005','\
Cedar Walton•The Maestro•Muse Records•1981','\
Danilo Perez•Panamonk•Impulse!•1996','\
Bobby Scott Trio•Great Scott•Bethlehem Records•1954','\
Giorgio Gaslini•Gaslini Plays Monk•Soul Note•1981','\
Krzysztof Herdzin•We Mean Monk•GOWI Records•1998','\
Archie Shepp•Archie Shepp + The New York Contemporary Five•Storyville•1972'),'\
\
Monk\'s Sphere\
':('\
Various•Lenox School Of Jazz•Atlantic•1959','\
Miles Okazaki•Work Volumes 1-6  (The Complete Compositions Of Thelonious Monk)•Not On Label (Miles Okazaki Self-released)•2018','\
Alexander von Schlippenbach•Monk\'s Casino•Intakt Records•2005','\
Frank Kimbrough•Monk\'s Dreams: The Complete Compositions Of Thelonious Sphere Monk•Sunnyside•2018'),'\
\
Montage\
':('\
Langston Hughes•The Weary Blues With Langston Hughes•MGM Records•1958','\
Dave Grusin•One Of A Kind•GRP•1985','\
Lalo Schifrin•Jackie Chan In Battle Creek Brawl•Victor•1980','\
Dave Grusin•One Of A Kind•GRP•1984','\
Roland Young•Mystiphonic•EM Records•2013','\
Lalo Schifrin•Battle Creek Brawl (Original Soundtrack)•Victor•1980','\
Dave Grusin•500 Miles (Theme From Winning)•Decca•1969','\
Stan Kenton And His Orchestra•Fire Fury And Fun•Creative World•1974','\
Kenyon Hopkins•Mister Buddwing (Music From The Original Soundtrack)•Verve Records•1965','\
Grover Washington Jr.•No Tears In The End / Body And Soul (Montage)•Kudu•1972','\
Dave Grusin•One Of A Kind•GRP•1984','\
Dave Grusin•One Of A Kind•Polydor•1977','\
The Jimmy Giuffre Trio•The Easy Way•Verve Records•1959'),'\
\
Mood Indigo\
':('\
Duke Ellington And His Orchestra•Solitude / Mood Indigo•Columbia•1940','\
Duke Ellington And His Orchestra•Mood Indigo / Solitude•Columbia•0','\
Sonny Greer•Mood Indigo / The Mooche•Capitol Records•1945','\
Jimmie Lunceford And His Orchestra•Sophisticated Lady / Mood Indigo•Brunswick•0','\
Duke Ellington And His Orchestra•Mood Indigo / Runnin\' Wild!•Brunswick•1933','\
Johnny Hodges•Dance Bash #2•Norgran Records•1955','\
Duke Ellington•Sophisticated Lady•Master (2)•1937','\
Duke Ellington And His Orchestra•Mood Indigo / The Mooche•Victor•1935','\
Nat Gonella & His Georgians•Delta Serenade / Mood Indigo•Odeon•1938','\
Paul Robeson•Solitude / Mood Indigo•no label•1937','\
Duke Ellington And His Orchestra•Mood Indigo / St. James Infirmary•Disque Gramophone•0','\
Duke Ellington And His Orchestra•Bundle Of Blues / Mood Indigo•Brunswick•1933','\
no artist•Mood Indigo / One O\'clock Jump•Epic•1954','\
Duke Ellington•Caravan•RCA Victor•1958'),'\
\
Moon And Sand\
':('\
Roy Haynes•Sugar Roy•Kitty Records•1976','\
Vladimir Shafranov Trio•Live At Groovy•Kompass Records•1981','\
Bobo Stenson Trio•Very Early•Dragon (8)•1987','\
Fred Taylor Trio•Circling•Not On Label (Fred Taylor Trio Self-released)•2008','\
Aaron Heick•Europe•Venus Records (5)•2009','\
Various•Novus Sampler `90•Novus•1990','\
Kenny Burrell•Guitar Forms•Verve Records•1965','\
The Fred Hersch Trio•Horizons•Concord Jazz•1985','\
Keith Jarrett•Standards Vol. 2•ECM Records•1985','\
Janis Siegel•Slow Hot Wind•Varèse Sarabande•1995'),'\
\
Moon Germs\
':('\
Billy Cobham•Moon Germs•Atlantic•1974','\
Joe Farrell•Moon Germs•CTI Records•1973','\
Billy Cobham•Palindrome•BHM Productions•2013','\
no artist•Billy Cobham\'s Glass Menagerie•TDK (3)•2002','\
Billy Cobham•Total Eclipse•Atlantic•1974','\
Billy Cobham•Palindrome•Varèse Sarabande•2009'),'\
\
Moon Glow\
':('\
Duke Ellington And His Orchestra•Solitude / Moon Glow•Brunswick•1934','\
Joe Daniels And His Hot Shots•Nobody\'s Sweetheart / Moon Glow•Parlophone•1937','\
The Benny Goodman Quartet•Runnin\' Wild / Moon Glow•no label•0','\
Stéphane Grappelli And His Hot Four•Moon Glow / It Don\'t Mean A Thing•Decca•1935','\
The Benny Goodman Quartet•Moon Glow / Dinah•Victor•1936','\
Benny Carter•Plays Pretty•Blue Star•1955','\
Isao Suzuki•Samba Club•Paddle Wheel•1981','\
Marta Hristea•Villacross Passage•Electrecord•1998','\
Kenny Ball And His Jazzmen•Tribute To Tokyo•Pye Jazz•1964','\
The Blue Angel Jazz Club•Jazz At Pasadena \'68 Volume 1•The Blue Angel Jazz Club•1969','\
Billie Holiday•Billie Holiday•Clef Records•1954','\
Billy Vaughn And His Orchestra•The Best Of Billy Vaughn•Dot Records•1969'),'\
\
Moon Rays\
':('\
The Horace Silver Quintet•Further Explorations•Blue Note•1958','\
Vince Guaraldi•Vince Guaraldi \ Bola Sete \ And Friends•Fantasy•1963','\
Pharoah Sanders•Moon Child•Timeless Records (3)•1990','\
Jackie King•Moon Magic•Indigo Moon Records•1999','\
Pharoah Sanders•\' Finest•Dopeness Galore•2008','\
Jaki Byard•Jaki Byard With Strings!•Prestige•1968','\
Miles Davis•The Unique - Vol. 2•Giants Of Jazz•1986','\
Pharoah Sanders Quartet•The Creator Has A Master Plan•Venus Records (5)•2003','\
John Mehegan•Jazz In Africa Vol. 1•Continental Records (8)•1959','\
Miles Davis•Milestones •Dreyfus Jazz•2001','\
Erroll Garner•Deep Purple•Pickwick/33 Records•0'),'\
\
Moonchild\
':('\
Doug Carn•Moonchild•Black Jazz Records•1971','\
Tim Weisberg•Moonchild•MCA Records•1979','\
Various•Jazz Jamboree \'71 - Vol. 1•Polskie Nagrania Muza•1971','\
Jacques Loussier•Pagan Moon•CBS•1982','\
Gary Burton•Gary Burton & Keith Jarrett•Atlantic•1971','\
John Zorn•Moonchild (Songs Without Words)•Tzadik•2006','\
Tim Weisberg•Night-Rider!•MCA Records•1979','\
Giovanni Hidalgo•Worldwide•Sony Discos Inc.•1993','\
Paz•Paz Are Back•Spotlite Records•1982','\
Various•Atlantic Jazz: Best Of The \'70s•Rhino Records (2)•1994','\
Travis & Fripp•Live At Coventry Cathedral•Panegyric•2010','\
Gary Burton•Alone At Last•Atlantic•1971'),'\
\
Moondance\
':('\
Van Morrison•That\'s Life•Verve Records•1996','\
Bobby Mcferrin•Moondance / Jubilee•Elektra Musician•1982','\
Michael Bublé•Sway•143 Records•2004','\
Various•Jazzier Rhythms 2•Hubbub Records•1997','\
no artist•Tokyo\'s Coolest Combo In Tokyo•Triad•1993','\
Kalle Salonen•Barracuda Man•Texicalli Records•2016','\
Various•August Rush (Music From The Motion Picture)•Columbia•2007','\
Soiled Mattress And The Springs•Honk Honk Bonk!•Teenage Teardrops•2007','\
Various•Musician\'s Guide Volume 2•Elektra Musician•1982','\
Various•Bag Of Goodies•no label•1991','\
Παντελής Μπενετάτος•Stand-Art•Eros Music•1995','\
B.B. Blunder•Workers\' Playtime•United Artists Records•1971','\
Grady Tate•Movin\' Day•Janus Records•1974','\
Michael Bublé•Come Fly With Me•Reprise Records•2004','\
Nathan East•Nathan East•Yamaha Entertainment Group Of America•2014','\
Laurence Saltiel Quartet•Moondance•Aphrodite Records•2005','\
Julian Wasserfuhr & Roman Wasserfuhr•Relaxin\' in Ireland•ACT (4)•2018','\
Ramsey Lewis•Meant To Be•Narada Jazz•2002'),'\
\
Moonglow\
':('\
Muggsy Spanier And His Dixieland Band•Moonglow / Sunday•Mercury•1951','\
The Benny Goodman Quartet•Die Benny Goodman Story•Brunswick•1956','\
Adrian Rollini Trio•Moonglow / Pavanne•Vocalion (2)•1939','\
Earl Bostic And His Orchestra•Flamingo / Moonglow•Parlophone•0','\
Wynton Kelly•Cherokee / Moonglow•Blue Note•0','\
Wynton Kelly•Cherokee / Moonglow•Blue Note•0','\
Earl Bostic And His Orchestra•Moonglow / Ain\'t Misbehavin\'•King Records (3)•0','\
Stéphane Grappelli And His Hot Four•China Boy / Moonglow•Decca•1937','\
Ruby Braff Quartet•I\'m Shooting High / Moonglow•Philips•0','\
Earl Bostic And His Orchestra•Moonglow / Autumn Leaves•Gusto Records (2)•1982','\
Scooby Doo All Stars•Ernie\'s Journey / Moonglow•Zephyr Records•1957','\
Artie Shaw And His Orchestra•Moonglow / Serenade To A Savage•Victor•1941','\
Gene Krupa•Moonglow / Blues For Benny•Clef Records•1956'),'\
\
Moonlight in Vermont\
':('\
Johnny Smith Quintet•Tabu / Moonlight In Vermont•Royal Roost•1953','\
Sam Butera•Moonlight In Vermont / Thinking Mans Sax•Prima Magnagroove•1964','\
Hans Koller Quintett•Moonlight In Vermont / Stompin\' At The Savoy•Brunswick•1953','\
Gerry Mulligan Quartet•Gerry Mulligan´s Swing House•Brunswick•1959','\
Gerry Mulligan Quartet•Paris Concert•Vogue•1957','\
Marian McPartland•Marian McPartland Moods Volume 2•Quality•0','\
Billy Butterfield And His Orchestra•Moonlight In Vermont / There Goes That Song Again•Capitol Records•1944','\
Tony Scott (2)•Lost Tapes (Germany 1957 | Asia 1962)•Jazzhaus•2014','\
Jørgen Leth Quintet•Jazz Jamboree 1962 Vol. 4•Polskie Nagrania Muza•1962','\
Gerry Mulligan Quartet•A Night In Rome Vol. 2•Fini Jazz•1990','\
Gerry Mulligan Quartet•Gerry Mulligan Quartet•Fantasy•1953','\
Don Byas•Anthropology•Black Lion Records•0','\
Gerry Mulligan Quartet•Paris Concert•Pacific Jazz•1955','\
Ella Fitzgerald•Ella Och Louis Vol. 1•Karusell•1957','\
Ray Anthony•Plays For Dream Dancing Part 1•Capitol Records•1961'),'\
\
Moonlight Serenade\
':('\
Glenn Miller And His Orchestra•Sunrise Serenade / Moonlight Serenade•RCA Victor•0','\
Archie Bleyer Orchestra•Moonlight Serenade / Sunrise Serenade•Cadence (2)•0','\
Glenn Miller•Evergreen•RCA Victor•0','\
Ray Anthony & His Orchestra•Serenade In Blue / Moonlight Serenade •Capitol Records•0','\
Eumir Deodato•Moonlight Serenade / Havana Strut•MCA Records•1974','\
Cyril Stapleton And His Orchestra•Tonight (Perfidia) / Moonlight Serenade•Decca•0'),'\
\
Moonrays\
':('\
The Mastersounds•The Mastersounds Play Compositions By Horace Silver•World Pacific Records•1960','\
The Mastersounds•The Mastersounds Play Compositions By Horace Silver•World Pacific Records•1960','\
Roy Harte•Perfect Percussion: The 44 Instruments Of Roy Harte And Milt Holland•World Pacific Records•1961'),'\
\
Moontide\
':('\
Larry Cansler•Pacific Dreams•Voss Records•1988','\
The David Liebman Quintet•If They Only Knew•Timeless Records (3)•1981','\
Jack Wilkins•Reunion•Chiaroscuro Records•2001','\
Gil Fuller•Gil Fuller & The Monterey Jazz Festival Orchestra Featuring Dizzy Gillespie•Pacific Jazz•1965','\
Pat Riccio And His Band•Stranger On The Shore•Arc Sound Ltd.•0','\
Gil Fuller•Dizzy Gillespie & James Moody With Gil Fuller & The Monterey Jazz Festival Orchestra.•Blue Note•2008'),'\
\
Moontrane\
':('\
Bobby Hutcherson•Live At Montreux•Blue Note•1974','\
Dexter Gordon•The Best Of Dexter Gordon•Columbia•1980','\
Louis Hayes•Ichi-Ban•Timeless Records (3)•1976','\
Woody Shaw•The Moontrane•Muse Records•1975','\
Charles Earland•Live At The Lighthouse•Prestige•1972','\
Dexter Gordon•Sophisticated Giant•Columbia•1977','\
Larry Young•Unity•Blue Note•1966'),'\
\
Moose the Mooche\
':('\
Charlie Parker•Charlie Parker On Dial Volume 1•Spotlite Records•1970','\
The Charlie Parker Septet•Yardbird Suite / Moose The Mooche•Dial Records (3)•1946','\
The Charlie Parker All-Stars•Night In Tunisia•Sonet•0','\
Gonzalo Rubalcaba•Rapsodia•Blue Note•1993','\
Richie Cole•The Many Faces Of Bird - The Music Of Charlie Parker•Verve Digital•1989','\
Ron Carter•Carnaval•Galaxy•1983','\
Bob Degen•Sequoia Song•Enja Records•1976','\
Various•The Compositions of Charlie Parker•Riverside Records•1962','\
Charlie Parker•Charlie Parker Septet•Jazztone (2)•1956','\
Dizzy Reece•Blowin\' Away•Interplay Records•1978','\
The Bud Powell Trio•At The Golden Circle Volume 4•SteepleChase•1980','\
The Bud Powell Trio•At The Golden Circle Volume 2•SteepleChase•1978','\
Warne Marsh•Star Highs•Criss Cross Jazz•1982','\
Hank Jones•Bop Redux•Muse Records•1977','\
Giorgio Azzolini•What\'s Happening?•Juke Box•1966','\
Bud Powell•The Amazing Bud Powell Vol. 3 - Bud!•Blue Note•1957','\
Sphere (16)•Bird Songs•Verve Records•1988'),'\
\
More I See You\
':('\
Chris Montez•The More I See You•A&M Records•1966','\
Chris Montez•The More I See You / Call Me•Fermata•1967','\
Carmen Cavallaro And His Orchestra•The More I See You / In Acapulco•Decca•0','\
Harry James And His Orchestra•The More I See You / I Wish I Knew•Columbia•1945','\
Richard "Groove" Holmes•The More I See You•Prestige•1966','\
no artist•Henri Renaud All Stars Vol. 2•Swing (3)•1954','\
Bill Ramsey•The Late Late Show•Supraphon•1967','\
Phineas Newborn Jr.•Here Is Phineas (The Piano Artistry Of Phineas Newborn Jr.)•Atlantic•1956','\
Roberta Peck•Extraordinary•Columbia•1967','\
Houston Person•The Big Horn•Muse Records•1979','\
Jimmy Heath•Triple Threat•Riverside Records•1962','\
Quartette Trés Bien•Our Thing•Decca•1968'),'\
\
More I See You The\
':('\
Chris Montez•The More I See You•A&M Records•1966','\
Chris Montez•The More I See You / Call Me•Fermata•1967','\
Carmen Cavallaro And His Orchestra•The More I See You / In Acapulco•Decca•0','\
Harry James And His Orchestra•The More I See You / I Wish I Knew•Columbia•1945','\
Richard "Groove" Holmes•The More I See You•Prestige•1966','\
no artist•Henri Renaud All Stars Vol. 2•Swing (3)•1954','\
Phineas Newborn Jr.•Here Is Phineas (The Piano Artistry Of Phineas Newborn Jr.)•Atlantic•1956','\
Bill Ramsey•The Late Late Show•Supraphon•1967','\
Roberta Peck•Extraordinary•Columbia•1967','\
Quartette Trés Bien•Our Thing•Decca•1968','\
Jimmy Heath•Triple Threat•Riverside Records•1962','\
Houston Person•The Big Horn•Muse Records•1979','\
Sam Most•Mostly Flute•Xanadu Records•1976','\
Sarah Vaughan•Ooh! What A Day!•Roulette•1960'),'\
\
More Love\
':('\
Stan Kenton And His Orchestra•More Love Than Your Love / Skoot•Capitol Records•1954','\
Jane Morgan•Enchanted Island•Kapp Records•1958','\
Time And Space•Need Your Love Once More / Crazy Love Songs•Postmodern Jazz•1994','\
Dianne Reeves•More To Love•EMI USA•1990','\
Helen Humes And Her All-Stars•He Don\'t Love Me Any More / Pleasing Man Blues•Philo Recordings•1946','\
Chris Montez•The More I See You•A&M Records•1966','\
Al Jarreau•All Of My Love•Wea•1989','\
Buddy Johnson And His Orchestra•Jet / No More Love•Decca•1951','\
Sylvia Syms•I Cry For More•Decca•1957','\
Al Martino•Al Martino\'s Best•Capitol Records•1966','\
Jimmy Dorsey And His Orchestra•No One Ever Lost More•Fraternity Records•1957','\
Cleo Laine•Sigh No More Ladies•Fontana•1964','\
Ray Anthony•The More I Love You / Just A Closer Walk With Thee•Ranwood•1969','\
Richard Hayes•Babalu / More Than Love•Mercury•1952','\
Teddy Walters•The More I Go Out With Somebody Else / I\'ll Close My Eyes•Musicraft•1947','\
Fats Waller & His Rhythm•Let\'s Sing Again / The More I Know You•Victor•1936'),'\
\
More Than You Know\
':('\
Perry Como•Surrender / More Than You Know•RCA Victor•1946','\
Benny Goodman Trio•Nobody\'s Sweetheart / More Than You Know•no label•1937','\
Benny Goodman Trio•China Boy / More Than You Know•no label•1936','\
Erroll Garner•More Than You Know•Regent•1950','\
Dexter Gordon•North Sea Jazz Legendary Concerts•Bob City•2013','\
Don Byas•Don Wails With Kenny•Columbia•1960','\
Mildred Bailey And Her Orchestra•\'Long About Midnight / More Than You Know•Vocalion (2)•1936','\
Dr. John•Makin\' Whoopee!•Warner Bros. Records•1989','\
Perry Como•Without A Song / More Than You Know•RCA Victor•1951','\
Chrystian•More Than You Know•Young•1975','\
Billy Eckstine•More Than You Know•MGM Records•1955','\
Randy Brooks and his Orchestra•The Man With The Horn / More Than You Know•Decca•1948','\
Dakota Staton•I Love You More Than You\'ll Ever Know / (I Want A) Country Man•Groove Merchant•1973','\
Teddy Wilson And His Orchestra•More Than You Know / Sugar•Columbia•1941','\
Sonny Rollins•Sonny Rollins And Thelonious Monk•Prestige•1955','\
Sonny Rollins•Moving Out•Prestige•1956','\
Benny Goodman And His Orchestra•Jazz Gallery•Philips•1959'),'\
\
Morning\
':('\
Benny Sings•On Christmas Morning•Sonar Kollektiv•2007','\
Lee Ritenour•The Best•JVC•1980','\
Paul Horn•Too High •Epic•1974','\
Bonjour (4)•Bonjour•Cantaloupe Music•2016','\
Bonjour (4)•Bonjour•Cantaloupe Music•2016','\
Scott Dubois (2)•Winter Light•ACT (4)•2015','\
Laura Mvula•She•RCA Victor•2012','\
Count Basie Orchestra•Good Morning Blues / Doggin\' Around•Decca•1938','\
The Nat King Cole Trio•Slow Down / Early Morning Blues•Decca•0','\
Spyro Gyra•Morning Dance•Infinity Records (2)•1979','\
Spyro Gyra•Live Spyro Gyra•Infinity Records (2)•1979','\
Terje Rypdal•To Be Continued•ECM Records•1981','\
Lee Ritenour•Morning Glory / Sugarloaf Express•Elektra•1978','\
no artist•Bluesette / Brand New Morning•Cadet•1968','\
Spyro Gyra•Morning Dance•Infinity Records (2)•1979','\
René Thomas•I Giganti Del Jazz Vol. 83•Curcio•0','\
Larry Cansler•Street People / Texas Morning•Warner Bros. Records•0','\
Kellye Gray•Standards In Gray•Justice Records (2)•1990'),'\
\
Morning Dance\
':('\
Spyro Gyra•Morning Dance•Infinity Records (2)•1979','\
Spyro Gyra•Live Spyro Gyra•Infinity Records (2)•1979','\
Spyro Gyra•Morning Dance•Infinity Records (2)•1979','\
Norman Connors•Dance Of Magic•Cobblestone•1972','\
Spyro Gyra•Live Concert Series•Infinity Records (2)•1979','\
Billy Higgins•Mr. Billy Higgins•Riza Records•1985','\
Aylers Angels•Never Morning•Dialect Records•1998','\
Pharoah Sanders•Thembi•Impulse!•1971','\
The Dave Brubeck Quartet•Brandenburg Gate: Revisited•Columbia•1963','\
Chico Freeman•Peaceful Heart Gentle Spirit•Contemporary Records•1980'),'\
\
Morning Sprite\
':('\
Chick Corea Akoustic Band•Alive•GRP•1991','\
Chick Corea Akoustic Band•Chick Corea Akoustic Band•GRP•1989','\
Chick Corea Akoustic Band•Chick Corea Akoustic Band•GRP•1989','\
Chick Corea Akoustic Band•Live•Stretch Records•2018'),'\
\
Moten\'s Swing\
':('\
Harry James And His Orchestra•Moten Swing (Beginning) / Moten Swing (Conclusion)•Columbia•1947','\
Count Basie Orchestra•Louisiana / Moten Swing•Parlophone•0','\
Buck Clayton With His All-Stars•A Buck Clayton Jam Session•Columbia•1954','\
Barney Kessel•To Swing Or Not To Swing•Contemporary Records•0','\
Buck Clayton•How Hi The Fi•Columbia•1954','\
Andy Kirk And His Clouds Of Joy•Give Her A Pint (And She\'ll Tell It All) / Moten Swing•Decca•1936','\
Count Basie•Basie Jam #3•Pablo Records•1979','\
Gerry Mulligan•Nightwatch•United Artists Records•1961','\
Gene Ammons•Twisting The Jug•Prestige•1962','\
Bob Brookmeyer•Kansas City Revisited•United Artists Records•1959'),'\
\
Mother of the Dead Man\
':('\
The Mike Gibbs Band•Just Ahead•Polydor•1972','\
Gary Burton Quartet•Lofty Fake Anagram•RCA Victor•1968','\
Carla Bley•Go Together•WATT Works•1993','\
Gary Burton•Gary Burton / Larry Coryell•RCA Victor•1977','\
Gary Burton Quartet•A Genuine Tong Funeral•RCA Victor•1968','\
Gary Burton•Artist\'s Choice•Bluebird (3)•1987','\
Butch Hancock•No 2 Alike•Rainlight Records•1990','\
Various•LAFMS: The Lowest Form Of Music•Cortical Foundation•1996','\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014','\
Ella Fitzgerald•Portrait•Past Perfect 24 Carat Gold Edition•2003','\
Bob Dylan•Radio Radio: Theme Time Radio Hour Volume One•Mischief Music•2008','\
George Michael•MP3 Звездная Серия•Star Records (20)•2005'),'\
\
Mountain Greenery\
':('\
Mel Tormé•Mountain Greenery•Atlantic•1975','\
Ella Fitzgerald•Ella Fitzgerald Sings The Rodgers  And Hart Song Book•Verve Records•1957','\
Bing Crosby•I\'ve Got Five Dollars•Verve Records•1956','\
Paul Smith (5)•Liquid Sounds Part 2•Capitol Records•1954','\
Victor Silvester and His Silver Strings•Victor\'s Favourite Quicksteps No. 2•Columbia•1960','\
Bing Crosby•Bing Sings Whilst Bregman Swings•Verve Records•0','\
Paul Smith (5)•Liquid Sounds•Capitol Records•1954','\
Jackie & Roy•Storyville Presents Jackie And Roy•Storyville (3)•1955','\
Joe Derise•Joe Derise Sings•Bethlehem Records•1955','\
Al Cohn Quartet•Al Cohn Quartet With Henri Renaud•Vogue Records•1954','\
Dave Pell Octet•The Dave Pell Octet Plays Again•Fresh Sound Records•1984','\
Bud Freeman•Something Tender•United Artists Jazz•1963'),'\
\
Move\
':('\
Various•Move - Jam Session•EmArcy•1954','\
Miles Davis•Birdland 1951•Blue Note•2004','\
Miles Davis•Miles Davis At Birdland 1951•Beppo Records•0','\
Lonnie Smith•Move Your Hand•Blue Note•1970','\
Miles Davis•Budo / Move•Capitol Records•1949','\
J.J. Johnson•Debut Records\' Jazz Workshop Volume One: Trombone Rapport•Debut Records•1953','\
David Borsu•Move•Counterpoint Records•2006','\
Stan Getz•At Storyville Vol. 1•Sonet•0','\
Evan Parker Trio•The Bishop\'s Move•Les Disques Victo•2004','\
Jimmie Lunceford And His Orchestra•I\'m Gonna Move To The Outskirts Of Town•Decca•1942','\
The George Shearing Quintet•Thine Alone / Geneva\'s Move•MGM Records•0','\
The Red Norvo Trio•Little White Lies / Move•Swing (3)•1953','\
Parov Stelar•Move On!•Etage Noir Recordings•2004','\
Don Pullen•Five To Go•Horo Records•1976','\
Miles Davis•Birdland Days•Fresh Sound Records•1991','\
Jeff Tyzik•Prophecy•Capitol Records•1981','\
Miles Davis•Classics In Jazz Part 3•Capitol Records•0','\
Ray Charles•Makin\' Whoopee•no label•1964'),'\
\
Moving Out\
':('\
Art Farmer•Live In Tokyo•King Records•1977','\
The Catholics•Barefoot•Rufus Records (2)•1999','\
Al Sears•Swing\'s The Thing•Prestige Swingville•1960','\
Barney Wilen Quintet•Barney Wilen Quintet•Guilde Du Jazz•1957','\
Sam Most•From The Attic Of My Mind•Xanadu Records•1980','\
Gerardo Frisina•Movement •Schema•2014','\
Various•Jazz In Europe•Concert Hall•1969','\
Specs Powell•Movin\' In•Roulette•1957','\
Djabe•Forward•Gramy Records•2014','\
Sandy Patton•Waltz Forever My Love•JHM Records•1996','\
Dego•The More Things Stay The Same•2000 Black•2015','\
The Bloom Green Group•Discoteque•Haparanda•1971','\
Roy Ayers Ubiquity•Vibrations•Polydor•1976','\
Various•Dusty Fingers Volume Four•Strictly Breaks Records•1998'),'\
\
Mozambique\
':('\
Eddie Heywood•Lost Love•RCA Victor•0','\
The Village Stompers•Mozambique•Columbia•1964','\
Les Baxter His Chorus And Orchestra•Tamboo! (Part 3)•Capitol Records•1955','\
Eddie Heywood•Lost Love / Mozambique•RCA Victor•1956','\
Ted Daniel Quintet•Tapestry•Sun Records (2)•1977','\
Cellula New York•Cellula / New York•Hovado Records•1989','\
Emily Remler•Catwalk•Concord Jazz•1985','\
Daniel Humair•"Edges"•Label Bleu•1991','\
Jimmy McGriff•Giants Of The Organ In Concert•Groove Merchant•1973','\
Oscar Peterson•Oscar Peterson & Dizzy Gillespie•Pablo Records•1975','\
Les Baxter His Chorus And Orchestra•Tamboo!•Capitol Records•1955','\
Archie Shepp•A Sea Of Faces•Black Saint•1975','\
Juju (9)•Live At 131 Prince Street•P-Vine Records•2002','\
Die Elefanten•Nervous City•Nektar•1985','\
Emily Remler•Retrospective Volume Two: "Compositions"•Concord Jazz•1991'),'\
\
Mr. Broadway Theme From\
':('\
The Dave Brubeck Quartet•Jazz Impressions Of New York•Columbia•1965','\
Oliver Nelson•More Blues And The Abstract Truth•Impulse!•1964','\
Bill Evans•"Theme From The V.I.P.s" And Other Great Songs•MGM Records•1963','\
The Crusaders•Heat Wave•Pacific Jazz•1963','\
Dave Brubeck•Dave Brubeck•Supraphon•1971','\
Dave Brubeck•Dave Brubeck•Europa•0'),'\
\
Mr. Clean\
':('\
Weldon Irvine•Live In Nashville April 3 1999•91 WRVU Nashville•2000','\
Freddie Hubbard•Straight Life•CTI Records•1971','\
J.J. Johnson•Pinnacles•Milestone (4)•1980','\
Brother Jack McDuff•Brother Jack Meets The Boss•Prestige•1962','\
Peter Herbolzheimer•Scenes (Live At Ronnie Scott\'s Club)•MPS Records•1974','\
CTI All-Stars•Montreux Jazz Festival 2009•CTI Records•2010','\
Richard "Groove" Holmes•Comin\' On Home•Blue Note•1971','\
J.J. Johnson•Chain Reaction (Yokohama Concert Vol. 2)•Pablo Records•2002','\
Peter Herbolzheimer Rhythm Combination & Brass•Waitaminute•MPS Records•1973','\
Weldon Irvine•The Best Of (Vol. 1)•Cool Note Music•1997','\
Weldon Irvine•Liberated Brother•Nodlew Music•1972'),'\
\
Mr. Gone\
':('\
Dolo Coker•California Hard•Xanadu Records•1977','\
Freddie Slack And His Orchestra•Mr. Five By Five / The Thrill Is Gone•Capitol Records•1942','\
Peter King Quintet•Speed Trap•no label•1996','\
Jimmy Hamilton•It\'s About Time•Prestige Swingville•1961','\
Flow (17)•Flow•CTI Records•1970','\
Weather Report•Mr. Gone•ARC (3)•1978','\
Budd Johnson•Mr Bechet•Black And Blue•1997','\
Art Hodes•Pagin\' Mr. Jelly•Candid•1989','\
Chris Botti•Midnight Without You•Verve Forecast•1997'),'\
\
Mr. Jin\
':('\
Art Blakey & The Jazz Messengers•Indestructible•Blue Note•1966','\
Kyoto Jazz Sextet•Mission•Blue Note•2015','\
James Last•Voodoo-Party•Polydor•1971'),'\
\
Mr. Jones\
':('\
Annette Hopfenmüller•Goodbye Mr. Jones•Marlboro Music•1987','\
Elvin Jones•Poly-Currents•Blue Note•1970','\
Esko Linnavalli•A Good Time Was Had By All•Finnlevy•1976','\
Elvin Jones•Mr. Jones•Blue Note•1973','\
Hadley Caliman•Celebration•Catalyst Records (3)•1977','\
BT Edits•BT Edits: Volume 1•Bermuda Triangle Records•2008','\
Luigi Bonafede•Another Side Of Me•La Drogueria Di Drugolo S.r.l.•1991','\
Javon Jackson•Once Upon A Melody•Palmetto Records•2008','\
Weldon Irvine•Weldon & The Kats•Nodlew Music•1989','\
Oliver Jones (5)•Speak Low Swing Hard•Justin Time•1987','\
Herb Alpert•Passion Dance•Almo Sounds•1997','\
The Chico Hamilton Quintet•Chico Hamilton Quintet•Pacific Jazz•1957','\
Steve Khan•Borrowed Time•ESC Records•2007'),'\
\
Mr. Lucky\
':('\
Artie Kane•Mr. Lucky•RCA Victor•0','\
Sarah Vaughan•Fever•Mercury•1964','\
Henry Mancini And His Orchestra•Mr. Lucky / Floating Pad•RCA Victor•1960','\
Miles Davis•World Of Jazz•Manhattan Records (3)•1980','\
The Sensational Guitars Of Dan & Dale•Henry Mancini Favorites•Diplomat Records•0','\
Miles Davis•1960/61•Newsound 2000•2002','\
Von Freeman•Have No Fear•Nessa Records•1975','\
Paul Serrano Quintet•Blues Holiday•Riverside Records•1961','\
Brother Jack McDuff•The Honeydripper•Original Jazz Classics•1986','\
Brother Jack McDuff•The Honeydripper•Prestige•1961','\
Pepper Adams Donald Byrd Quintet•Out Of This World•Warwick•1961','\
Earl Grant•Midnight Sun•Decca•1962','\
Jimmy McPartland•Play TV Themes•Design Records (2)•1960','\
Buddy DeFranco•Born To Swing!•Star Satelite Records•1988'),'\
\
Mr. Magic\
':('\
Nat King Cole•Thank You Pretty Baby•Capitol Records•1967','\
Grover Washington Jr.•Greatest Performances•Motown•1983','\
Charles Earland•Slammin\' & Jammin\'•Savant•1997','\
Nathan Davis•If•Tomorrow International Inc.•1976','\
Carmen McRae•I\'m Coming Home Again•Buddah Records•1980','\
Fly (24)•Fly•Savoy Jazz•2004','\
Rusty Bryant•Jazz Horizons: Rusty Bryant Plays Jazz•Dot Records•1958','\
Carmen McRae•Ms. Magic•Accord (2)•1982','\
Christoph Spendel•Spendel•L+R Records•1989','\
T-Square•Light Up (Best Selection)•CBS/Sony•1983','\
Noriko Miyamoto•Vivid•Trio Records•1979'),'\
\
Mr. P.C.\
':('\
John Coltrane•Coltranology Volume Two•Affinity•1978','\
The John Coltrane Quartet•The Complete 1963 Copenhagen Concert  •Gambit Records•2006','\
David Murray•Deep River•DIW•1989','\
John Coltrane•The European Tour•Pablo Live•1980','\
Jean Toussaint•Impressions Of Coltrane•Century•1988','\
John Coltrane•Giant Steps•Atlantic•1960','\
The John Coltrane Quartet•The Copenhagen Concerts•Ingo•0','\
McCoy Tyner•Guitars•Half Note (2)•2008','\
Lambert Hendricks & Ross•High Flying•Columbia•1962'),'\
\
Mrs. Miniver\
':('\
Dexter Gordon•The Panther!•Prestige•1970','\
Dexter Gordon•The Complete Prestige Recordings•Prestige•2004'),'\
\
Muezzin\'\
':('\
Pepper Adams•Pepper Adams 5•Interlude (2)•1959','\
Pepper Adams Quintet•Pepper Adams Quintet•Mode Records•1957','\
Anima Sound System•Aquanistan•EMI•2003','\
Fred Kaz•Eastern Exposure•Atlantic•1960','\
Keith Jarrett•Keith Jarrett At The Blue Note - Saturday June 4th 1994 1st Set•ECM Records•1995','\
Keith Jarrett•Keith Jarrett At The Blue Note (The Complete Recordings)•ECM Records•1995'),'\
\
My Attorney Bernie\
':('\
Blossom Dearie•Songs Of Chelsea•Daffodil Records (2)•1987','\
Dave Frishberg•Can\'t Take You Nowhere•Fantasy•1987','\
Blossom Dearie•Me And Phil - Blossom Dearie Live In Australia•ABC Music•1994'),'\
\
My Favorite Things\
':('\
John Coltrane•Live At The Village Vanguard Again!•Impulse!•1966','\
John Coltrane•My Favorite Things•Atlantic•1961','\
John Coltrane•European Tour 1961•Le Chant Du Monde•2017','\
Mickey Tucker•Doublet•Dan•1977','\
John Coltrane•My Favorite Things•Jazz Masterworks•1985','\
John Coltrane•Two Giants Together - Rare Live Performance 1962•Musidisc•0','\
John Coltrane•My Favorite Things: Coltrane At Newport•Impulse!•2007'),'\
\
My Foolish Heart\
':('\
Timeless All Stars•At Onkel Pö\'s Carnegie Hall Hamburg 1982•Jazzline•2019','\
Mara Lynn Brown•My Foolish Heart•Decca•0','\
Paul Weston And His Music From Hollywood•My Foolish Heart /  Infatuation•Columbia•1955','\
Billy Eckstine•My Foolish Heart / (We\'ve Got A) Sure Thing•MGM Records•1949','\
Steve Conway (2)•My Thanks To You•Columbia•0','\
John Lindberg•Team Work•CECMA Records•1982','\
Earl Grant•My Foolish Heart / One Note Samba•Decca•1968','\
Woody Herman And His Orchestra•My Foolish Heart And I / I\'d Love You Again•Decca•1941','\
Nancy Wilson•My Foolish Heart / The Seventh Son•Capitol Records•1961','\
Ryo Fukui•Mellow Dream•Trio Records•1977'),'\
\
My Funny Valentine\
':('\
Mari Wilson•My Funny Valentine•Dino Entertainment•1991','\
Miles Davis•My Funny Valentine / Smooch•Prestige•0','\
Bill Clinton•Two Presidents\' Jam Session - Praha 94•Český Rozhlas•1994','\
Eddie Chamblee•My Funny Valentine / Lucky Old Sun•Val•0','\
The Milt Jackson Quartet•Vol. 1•Metronome•1955','\
The Jazztet•My Funny Valentine / Blues On Down•Argo (6)•1961','\
Gerry Mulligan Quartet•My Funny Valentine / Bark For Barksdale•Fantasy•1953','\
Sammy Davis Jr.•Hey There / My Funny Valentine •Brunswick•1955','\
Jimmy Smith•Groovin\' At Smalls\' Paradise (Volume 1)•Blue Note•1958','\
Fumio Itabashi Trio•Rise and Shine - Live at the Aketa\'s •ALM Records•1977','\
Gareth Davis•Jazz Standards Volume 1•Brian Records•2011','\
Gerry Mulligan•Jazz Gallery•Philips•1959'),'\
\
My Girl\
':('\
Ron Goodwin And His Orchestra•Tracey\'s Theme•Parlophone•1960','\
Nat King Cole•Too Young / That\'s My Girl•Capitol Records•1951','\
The Georgia Washboard Stompers•Sophisticated Lady / My Pretty Girl•Bluebird (3)•1933','\
Willie Creager And His Entertainers•Blue Skies / My Regular Girl•Pathé Actuelle•1927','\
Jerry Jerome & His Cats & Jammers•Girl Of My Dreams / Rainbow Blues•Asch Records•0','\
Jimmy McGriff•All About My Girl / M.G. Blues•Sue Records Inc.•1962','\
Jimmy McGriff•All About My Girl•Sue Records Inc.•1962','\
Frank Sinatra•My Kind Of Girl•Reprise Records•1962','\
Illinois Jacquet And His All Stars•Don\'t Blame Me / Girl Of My Dreams•Savoy Records•1946','\
Jean Goldkette And His Orchestra•My Pretty Girl / Clementine•no label•1936','\
Ray Peterson•I Forgot What It Was Like•Dunes Records•1963','\
Dude Skiles And His Vine Street Boys•My Girl / I Can\'t Give You Anything But Love•Variety (6)•1937','\
Herb Alpert & The Tijuana Brass•All My Lovin\'•A&M Records•0','\
Jimmy McGriff•All About My Girl•Sue Records Inc.•1962','\
Bix Beiderbecke•Bixology / Since My Best Girl Turned Me Down•Parlophone•1935','\
Bix Beiderbecke And His Gang•Sorry / Since My Best Girl Turned Me Down•Parlophone•1928','\
Sharkey And His Kings Of Dixieland•Somebody Stole My Gal / With A Pack On My Back•Capitol Records•1950','\
Dizzy Gillespie•Dizzy Gillespie Jam•Gruppo Editoriale Fabbri•1981'),'\
\
My Heart Stood Still\
':('\
Erroll Garner•Honeysuckle Rose / My Heart Stood Still •Columbia•0','\
Shorty Rogers And His Giants•The Swinging Mr. Rogers•Atlantic•0','\
Artie Shaw And His Orchestra•The Donkey Serenade / My Heart Stood Still•Bluebird (3)•1939','\
Dave Brubeck•My Heart Stood Still / The Trolley Song•Fantasy•1952','\
Ray McKinley And His Famous Orchestra•My Heart Stood Still•RCA Victor•0','\
Paul Smith (5)•Liquid Sounds By Paul Smith•Capitol Records•1954','\
Stan Getz•Previously Unreleased Recordings•Verve Records•1973','\
Art Blakey & The Jazz Messengers•Hard Bop•Columbia•1957','\
The Four Freshmen•Voices In Modern (Part 1)•Capitol Records•0','\
The Four Freshmen•Voices In Modern (Part 1)•Capitol Records•0','\
Ella Fitzgerald•Sings The Rodgers And Hart Song Book •Verve Records•1956'),'\
\
My Little Boat\
':('\
Red Nichols And His Five Pennies•Jazz Time With Red Nichols•Capitol Records•0','\
Emily Yancy•Yancy•Mainstream Records•1965','\
Milton Rogers And His Orchestra•The Ultimate In Percussion•Dot Records•1960','\
Claudio Meranda•Brazilian New Wave•Rhapsody (2)•1969','\
Don Burrows•Burrows\' Jazz Brothers - A Retrospective•ABC Records (3)•1982','\
Herb Ellis•Rhythm Willie•Concord Jazz•1975','\
Cal Tjader•Soña Libré•Verve Records•1963','\
Larry Adler•Harmonica Virtuoso With Piano Trumpet Bass Guitar And Drums•Audio Fidelity•1959','\
Joe Darensbourg And His Dixie Flyers•On A Lark - In Dixieland•Lark Records (2)•0','\
Art Van Damme Ensemble•Art And Four Brothers•MPS Records•1969','\
Antonio Pedro Hatch•The Cool Latin Sound•Pye Records•1968','\
Harry Belafonte•The Harry Belafonte Collection - 20 Golden Greats•Deja Vu•1984','\
Lorez Alexandria•How Will I Remember You?•Discovery Records•1978'),'\
\
My Little Suede Shoes\
':('\
Herbie Mann•My Little Suede Shoes•Bethlehem Records•1954','\
Charlie Parker•La Cucuracha / My Little Suede Shoes•Mercury•1952','\
Dave Pike•La Bamba•Prestige•1962','\
Charlie Parker•South Of The Border•Clef Records•0','\
Grant Green•The Latin Bit•Blue Note•1963','\
Red Rodney Quintet•One For Bird•SteepleChase•1988','\
Naoki Nishi•My Little Suede Shoes•Trio Records•1980','\
Shorty Rogers And His Giants•Shorty Rogers & His Giants•RCA Victor•1955','\
Roland Hanna•Bird Watching•Progressive Records (2)•1978','\
Charlie Parker•Bird At The Hi-Hat•Blue Note•1993','\
Art Farmer Quartet•Interaction•Atlantic•1963','\
Grant Green•Jazz Profile: Grant Green•Blue Note•1997','\
Walter Bishop Jr.•Hot House•Muse Records•1979','\
Steve Grossman Trio• Bouncing With Mr. A.T.•Dreyfus Jazz•1996','\
29th Street Saxophone Quartet•Live•Red Record•1989','\
Sonny Stitt•Stitt Plays Bird•Atlantic•1964','\
J.J. Johnson•J.J.!•RCA Victor•1965'),'\
\
My Man\'s Gone Now\
':('\
Clare Fischer•Jazz•RCA Victor•0','\
Clark Terry•George Gershwin\'s Porgy & Bess•A440 Music Group•2004','\
Miles Davis•Porgy And Bess•Columbia•1959'),'\
\
My Old Flame\
':('\
Miles Davis And His Band•My Old Flame•Prestige•1952','\
The Modern Jazz Group Freiburg•Weekend - Saturday•Fono-Ring•0','\
Peggy Lee•My Old Flame•Capitol Records•1970','\
The Flip Phillips-Howard McGhee Boptet•Znarg Blues / My Old Flame•Mercury•1947','\
Stan Getz Quartet•My Old Flame / The Lady In Red•Prestige•1950','\
Jackie McLean•Consequence•Blue Note•1979','\
Billie Holiday•I\'m Yours / My Old Flame•Commodore•1947','\
Ira Sullivan Quintet•The Ira Sullivan Quintet•Delmar Records•1960','\
Ira Sullivan Quintet•The Ira Sullivan Quintet•Delmar Records•1960','\
Count Basie Orchestra•My Old Flame / Tom Thumb•Okeh•1942','\
no artist•The Touch Of Tony Scott (Walkin\' On Air)•RCA•1956','\
Miles Davis•The New Sounds•Prestige•1951','\
Charlie Parker•Charlie Parker Plays•Music•0','\
Doug Raney Trio•Guitar Guitar Guitar•SteepleChase•1985','\
Mal Waldron•Piano Duo Live At Pit Inn •CBS/Sony•1986','\
Sal Nistico•Heavyweights•Jazzland•1961','\
J. R. Monterose Quartet•Welcome Back J.R. !•Progressive Records (2)•1979','\
Bobby Jaspar•Tenor And Flute•Riverside Records•1957'),'\
\
My One and Only Love\
':('\
John Coltrane•My One And Only Love / Lush Life•Impulse!•1963','\
Joe Harnell•Our Day Will Come / My One And Only Love•Kapp Records•1963','\
Sonny Rollins•Is\'nt She Lovely•Milestone (4)•1978','\
Ella Fitzgerald•My One And Only Love / (Love Is) The Tender Trap•Decca•1955','\
Billy Taylor Trio•Who Can I Turn To / My One And Only Love•Prestige•1954','\
The Elvin Jones Jazz Machine•Live At Pit Inn•Polydor•1985','\
Сергей Гурбелошвили•Classical Jazz Ballades•Мелодия•1990','\
Thad Jones Quartet•Three And One•Steeplechase•1984','\
Pallarols Duo•Pallarols Duo•Not On Label (Pallarols Duo Self-released)•2018','\
no artist•My One And Only Love•Red Record•1983','\
Pepper Adams•Pepper Adams 5•Interlude (2)•1959','\
Pepper Adams Quintet•Pepper Adams Quintet•Mode Records•1957','\
Kapstad-Johansen Quartet•Friends•Kal Productions•1980','\
McCoy Tyner•Atlantis•Milestone (4)•1975','\
Larry Coryell•The Larry Coryell / Michael Urbaniak Duo•Keytone•1982','\
Michel Perez Quartet•Toujours•Aimera Production•1992','\
Ahmad Jamal•Steppin Out With A Dream•20th Century Records•1976','\
Jimmy Smith•Plain Talk•Blue Note•1968','\
Triosence•Away For A While•Mons Records•2005','\
Takeshi Shibuya•Shibuyan•no label•1983','\
The Richie Kamuca Quartet•Richie Kamuca Quartet•Mode Records•1957','\
Joe Henderson•Relaxin\' At Camarillo•Contemporary Records•1981'),'\
\
My Romance\
':('\
Dave Brubeck•My Romance / Just One Of Those Things•Fantasy•1952','\
Martin Denny•Romantica•Liberty•1961','\
Miss Lee Morse And Her Blue Grass Boys•Yes Sir That\'s My Baby / An Old Fashioned Romance•Perfect (3)•1925','\
no artist•Romance Romance / Me And My Shadow•Columbia•1965','\
Houston Person•Wild Flower•Muse Records•1978','\
Archie Shepp•California Meeting - Live "On Broadway"•Soul Note•1987','\
Elvin Jones Quartet•Mr. Thunder•Eastwest Records (2)•1974'),'\
\
My Shining Hour\
':('\
John Coltrane•Coltrane Jazz•Atlantic•1961','\
Dakota Staton•Live And Swinging•United Artists Records•1964','\
Pallarols Duo•Pallarols Duo•Not On Label (Pallarols Duo Self-released)•2018','\
Stanley Turrentine•Dearly Beloved•Blue Note•1961','\
Franco Ambrosetti•A Jazz Portrait Of Franco Ambrosetti•Durium•1965','\
Larry Coryell•Shining Hour•Muse Records•1990','\
Joe Puma•Shining Hour•Reservoir (2)•1987','\
Roy Hargrove•The Collected Roy Hargrove•BMG Classics•1998','\
Jimmy Gourley•Jimmy Gourley And The Paris Heavyweights•52e Rue Est•1984','\
Jimmy Gourley•Jimmy Gourley And The Paris Heavyweights•52e Rue Est•1984','\
Bob Mintzer Big Band•Swing Out•MCG Jazz•2008','\
Åke Johansson Trio•Live At Nefertiti•Dragon (8)•1983','\
Harold Mabern Trio•Don\'t Know Why•Venus Records (5)•2003','\
John Coltrane•Coltrane Jazz•Atlantic•1961','\
John Coltrane•Trane: The Atlantic Collection•Atlantic•2017','\
John Coltrane•The Very Best Of John Coltrane•Rhino Records (2)•2000','\
Wendell Harrison•Rush & Hustle•Wenha•1994'),'\
\
My Ship\
':('\
Hubert Laws•Storm Then The Calm•Jazz Heritage•1994','\
Kunio Ohta Quintet•My Back Pages •Three Blind Mice•1977','\
John Lewis (2)•The John Lewis Album For Nancy Harrow•Finesse Records (3)•1981','\
Stanley Turrentine•Jubilee Shouts•Blue Note•1978','\
The Herb Pilhofer Trio•Jazz•Argo (6)•1960','\
Scant (2)•At The Club Room•Confront•1996','\
Slide Hampton•Inclusion•Sound Hills Records•1999','\
Rudy Vallee And His Connecticut Yankees•When My Ship Comes In / An Earful Of Music•Victor•1934','\
Tiny Hill And His Orchestra•Back In Your Own Backyard / I\'ll Sail My Ship Alone•Mercury•0','\
Ron Carter•Peg Leg•Milestone (4)•1978','\
Art Blakey & The Jazz Messengers•Live At The Village Vanguard Club New York 1982•Quantum Leap•2004','\
George Freeman•Birth Sign•Delmark Records•1972','\
Cedar Walton Trio•Cedar!•Prestige•1967','\
Herbie Hancock•Directions In Music - Live At Massey Hall•Verve Records•2002','\
Wallace Roney•A Place In Time•HighNote Records Inc.•2016'),'\
\
Mystic Touch\
':('\
Joanne Brackeen•Special Identity•Antilles•1982','\
Roy Ayers•Virgin Ubiquity Remixed•Rapster Records•2006','\
Divine Styler•Spiral Walls Containing Autumns Of Light•Giant Records•1992'),'\
\
Naima\
':('\
John Coltrane•Live In Paris Part 1•BYG Records•1972','\
Joe McPhee•Glasses•Hat Hut Records•1979','\
The Blue Train•Live On Mount Meru (Volume Two)•Historic Performances Records•0','\
Hannibal Marvin Peterson•Naima•Eastworld•1978','\
Toshiyuki Miyama & The New Herd•Orchestrane New Herd Plays John Coltrane•Denon Jazz•1977','\
John Coltrane•Live In Paris Volume One•Affinity•1980','\
The Great Jazz Trio•At The Village Vanguard•East Wind•1978','\
John Coltrane•John Coltrane•Fabbri Editori•1979','\
George Otsuka Quintet•Physical Structure•Three Blind Mice•1976','\
Eric Dolphy•Naima•West Wind•1991','\
John Coltrane•Spiritual•Drive (3)•1989','\
John Coltrane•Coltranology•BYG Records•1973','\
John Coltrane•Portraits•Portraits (2)•2018','\
The Visitors (10)•Neptune•Cobblestone•1972','\
John Coltrane•Live In Antibes 1965•no label•1988','\
John Coltrane•Offering: Live At Temple University•Impulse!•2014'),'\
\
Nancy (With The Laughing Face)\
':('\
The John Coltrane Quartet•Nancy (With The Laughing Face) / Up \'Gainst The Wall•Impulse!•1962','\
Frank Sinatra•A Friend Of Yours•Columbia•1945','\
Brew Moore•Brew Moore•Original Jazz Classics•1983','\
Hazel Scott Trio•After Hours•Tioch Digital Records•1983','\
Cannonball Adderley•Know What I Mean?•Riverside Records•1961','\
The Oscar Peterson Trio•Nigerian Marketplace•Pablo Live•1982','\
Cannonball Adderley•The Best Of Cannonball Adderley•Riverside Records•1968','\
Shirley Scott•Blue Seven•Prestige•1965','\
Woody Herman•Presents A Concord Jam Volume 1•Concord Jazz•1981','\
Pete Petersen & The Collection Jazz Orchestra•Straight Ahead•Chase Music Group•1989','\
Herbie Mann•Flute Fraternity•Mode Records•1957','\
Hal Singer•Milt And Hal•Barclay•1968','\
Grant Green•Ballads•Blue Note•2002','\
Rufus Harley•From Philadelphia To Paris•Carrere•1988'),'\
\
Nancy Joe\
':('\
Gerald Wilson Orchestra•Moment Of Truth•Pacific Jazz•1962','\
Geri Allen•Grand River Crossings (Motown & Motor City Inspirations)•Motéma•2013','\
Frank Sinatra•American Legend•K-Tel•2002','\
Frank Sinatra•Portrait Of Sinatra (Columbia Classics)•Columbia•1997','\
Frank Sinatra•The Best Of The Columbia Years 1943-1952•Columbia•1998','\
Bob Wills & His Texas Playboys•Take Me Back To Tulsa•Proper Records (2)•2001','\
Frank Sinatra•The Columbia Years 1943-1952: The Complete Recordings•Columbia•1993','\
Frank Sinatra•The Complete Reprise Studio Recordings•Reprise Records•1995'),'\
\
Napanoch\
':('\
Quest (13)•Quest•Trio Records•1982','\
David Liebman•Sweet Hands•Horizon (3)•1975','\
David Liebman•Trio + One•Owl Records (4)•1988'),'\
\
Nardis\
':('\
Richard Beirach•Eon•ECM Records•1975','\
The Great Jazz Trio•At The Village Vanguard Vol.2•East Wind•1977','\
Sphinx (24)•Sphinx•Acba•1979','\
Philipp Van Endert•Trio•JazzSick Records•2004','\
Various•Ginparis Session - June 26','1963•Three Blind Mice•1971','\
Masahiko Satoh•As If ...•Interface (3)•1985','\
Intensive Jazz Sextet•Today\'s Sound•Schema•1997','\
Bobby Hutcherson•Live At The Festival•Enja Records•1973'),'\
\
Natives are Restless Tonight\
':('\
The Horace Silver Quintet•Song For My Father (Cantiga Para Meu Pai)•Blue Note•1964','\
Horace Silver•The Natives Are Restless Tonight•Emerald Records•1990','\
The Jazz City Workshop•The Jazz City Workshop•Bethlehem Records•1955'),'\
\
Natural Selection\
':('\
The Philippe Lapointe Group•Natural Selection•Progress Records (13)•1987','\
Quest (13)•Natural Selection•Pathfinder Records•1988','\
Dave Samuels•Natural Selection•GRP•1991','\
Alexander von Mehren•Aéropop•Aéropop Records•2013','\
Miles Goodman•Getting Even With Dad (Original MGM Motion Picture Score)•Private Music•1994'),'\
\
Nature Boy\
':('\
Miles Davis•Blue Moods Vol. 1•Debut Records (3)•0','\
Ahmad Jamal•Nature Boy / Little Ditty•Cadet•1967','\
Richard Barbary•What\'s Your Name?•A&M Records•0','\
Nat King Cole•Nature Boy / Lost April•Capitol Records•1948','\
Various•The New Wave In Jazz•Impulse!•1966','\
George Benson•Turn Your Love Around•Warner Bros. Records•1981','\
Miles Davis•Blue Moods•Debut Records•1955'),'\
\
Nearness Of You\
':('\
Sarah Vaughan•You\'re Mine You / The Nearness Of You•Columbia•1950','\
George Shearing Trio•The Fourth Deuce•London Records•0','\
Tab Smith•Because Of You•Checker•1959','\
Sonny Stitt•Sonny Stitt Plus Four•Sonet•0','\
Stan Getz Quintet•The Nearness Of You / Pot Luck•Norgran Records•0','\
Lou Donaldson•Mack The Knife / The Nearness Of You•Blue Note•1959','\
Gerry Mulligan Quartet•The Nearness Of You / Tea For Two•Swing (3)•1953','\
Bill Doggett•Honey / The Nearness Of You•King Records (3)•1954','\
Dinah Shore•The Nearness Of You / Maybe•Bluebird (3)•1940','\
Aldemaro Romero And His Orchestra•Keep It Gay•RCA Victor•1953','\
Lionel Hampton And His Quartet•The Lionel Hampton Quartet•Clef Records•1953','\
Glenn Miller And His Orchestra•The Nearness Of You•RCA Victor•1954','\
Oscar Peterson•Oscar Peterson Plays Pretty No. 2•Clef Records•0','\
no artist•The Nearness Of You / Begin The Beguine•Gone (3)•1951','\
Auriel Carnell•The English Jazz Scene Vol 1•Aral Records•1962'),'\
\
Necessary Blonde\
':('\
Scott Henderson (2)•Tribal Tech•Relativity•1991','\
Tribal Tech (2)•Primal Tracks•Bluemoon Recordings•1994'),'\
\
Nefertiti\
':('\
Chick Corea Quartet•Live In New York 1974•Oxford•1976','\
Miles Davis•Nefertiti•Columbia•1968','\
The Cecil Taylor Unit•Nefertiti The Beautiful One Has Come•Debut Records (3)•1965','\
Miles Davis•Sextet & Quintet •CBS•1989','\
Wayne Shorter•Wayne Shorter •Agora SA•2010','\
Andrew Hill•Nefertiti•East Wind•1976','\
Cecil Taylor•Nefertiti The Beautiful One Has Come•Arista•1976','\
Cecil Taylor•What\'s New•Freedom•1974'),'\
\
Never Alone\
':('\
Louis Armstrong•Rosie / You\'ll Never Walk Alone•Brunswick•1967','\
Eddie Chamblee•The Honeydripper•Prestige•1964','\
Fred Waring & The Pennsylvanians•You\'ll Never Walk Alone•Decca•1952','\
no artist•I Never See Maggie Alone / He\'s The Last Word•Banner•1927','\
Art Farmer•Art Farmer Plays•Prestige•1955','\
Frank Sinatra•If I Loved You / You\'ll Never Walk Alone•Columbia•1950','\
Kim Cordell•We\'re Having A Gang Bang•Look Records (3)•1976','\
Al Allen & Co.•Bali Hai•Fantasy•1975','\
Nina Simone•You\'ll Never Walk Alone / Plain Gold Ring•Bethlehem Records•1960','\
Irving Aaronson and his Commanders•Crazy Words-Crazy Tune / I Never See Maggie Alone•Victor•1927','\
Frank Sinatra•The Concert Sinatra•Reprise Records•1963','\
Larry Carlton•Alone/But Never Alone•MCA Records•1986','\
Perry Como•You\'ll Never Walk Alone•RCA•1958','\
Judy Garland•Have Yourself A Merry Little Christmas•Decca•1954','\
Blue Haze (2)•You\'ll Never Walk Alone•A&M Records•1973','\
Art Farmer•Early Art•New Jazz•1961','\
Ahmad Jamal•Jamal At The Penthouse•Argo (6)•1959'),'\
\
Never Givin\' Up\
':('\
Patrice Rushen•Haven\'t You Heard: The Best Of Patrice Rushen•Rhino Records (2)•0','\
Al Jarreau•This Time•Warner Bros. Records•1980','\
Patrice Rushen•Remind Me (The Classic Elektra Recordings 1978-1984)•Strut•2019','\
Al Jarreau•Best Of Al Jarreau•Warner Bros. Records•1996','\
Al Jarreau•The Very Best Of: An Excellent Adventure•Rhino Records (2)•2009','\
Incognito•The Best (2004-2017)•Ear Music•2017'),'\
\
Never Make Your Move Too Soon\
':('\
The Airmen Of Note•Blues & Beyond•The United States Air Force Band•2009','\
Ernestine Anderson•Never Make Your Move Too Soon•Concord Jazz•1981','\
The Capp/Pierce Juggernaut•Live At The Alley Cat•Concord Jazz•1987','\
B.B. King•Midnight Believer•ABC Records•1978','\
Chuck Brown•Timeless•Raw Venture Records & Tapes•1998','\
Ernestine Anderson•Great Moments With Ernestine Anderson•Concord Jazz•1993','\
The Crusaders•Royal Jam•MCA Records•1982'),'\
\
Never Will I Marry\
':('\
Jimmy Witherspoon•I Never Will Marry•Prestige•1964','\
Caterina Valente•Never Will I Marry•London Records•1963','\
Patty Andrews•Daybreak Blues / I Never Will Marry•Capitol Records•1956','\
Nancy Wilson•Save Your Love For Me / Never Will I Marry•Capitol Records•1962','\
Jimmy Witherspoon•I Never Will Marry•Stateside•1964','\
Cannonball Adderley•Cannonball Adderley And The Poll-Winners Featuring Ray Brown And Wes Montgomery•Riverside Records•1960','\
Bob Berg•Virtual Reality•Denon•1993','\
Nancy Wilson•Nancy Wilson / Cannonball Adderley•Capitol Records•1961','\
Nancy Wilson•The Swinging\'s Mutual•Capitol Records•0','\
Caterina Valente•Strictly U.S.A.•London Records•1963','\
Silvia Droste•Seize The Day•Bell Records (5)•1994'),'\
\
New Boots\
':('\
MVP (5)•Truth In Shredding•Tone Center•1990','\
Joachim Kühn•Nightline New York•Sandra Music Productions•1981','\
Don Menza•Morning Song•SABA•1966','\
Gabe Baltazar•Stan Kenton Presents Gabe Baltazar•Creative World•1979','\
no artist•Burnin\'•M & K Realtime Records•1981','\
Various•The Best Of Luv N\' Haight Volume One•no label•1993','\
Lee Castle•Jimmy Dorsey On Tour•Columbia Special Products•1959','\
sPacemoNkey (2)•The Karman Line•Hubro•2014','\
Al Cohn•The Birdland Stars On Tour•RCA•1983','\
Gene Ammons•Dig Him!•Argo (6)•1962','\
Galliano•A Joyful Noise Unto The Creator•no label•1992','\
no artist•The Great Bob Scobey And His Frisco Band Volume II•Jansco•1966','\
Charlie Byrd Quintet•Du Hot Club De Concord•Concord Records•1995','\
Bootstrappers•Bootstrappers•New Alliance Records•1989','\
Terry Edwards & The Scapegoats•Terry Edwards Presents... Birth Of The Scapegoats•Hux Records•1998','\
Tommy Dorsey And His Orchestra•The Complete Tommy Dorsey And His Orchestra 1928-1935•Charly Records•1990','\
Eugene Chadbourne•Corpses Of Foreign War•Fundamental•1986'),'\
\
New Thing\
':('\
Count Basie Orchestra•New Basie Blues / Sure Thing•Mercury•1952','\
Lloyd Wallace Trio•New Thing•Duo Records (2)•0','\
Count Basie Orchestra•Count Basie And His Orchestra•Barclay•1953','\
Jack Wilkins•You Can\'t Live Without It•Chiaroscuro Records•1977','\
Linc Chamberland•A Place Within•Muse Records•1977','\
Dexter Gordon•A Day In Copenhagen•MPS Records•1969','\
Gold Washboard•Gold Washboard•Pronit•0','\
Count Basie Orchestra•New Basie Blues•Karusell•1954','\
Dinah Washington•Memorial Dinah Washington•PGP RTB•1964','\
The Master Trio•The Master Trio•Baybridge Records•1983','\
Bunny Brunel•For You To Play•Média 7•1994','\
Various•Great Jazz Brass•RCA Camden•1957','\
The Awakening (4)•Hear Sense And Feel•Black Jazz Records•1972'),'\
\
Next Future\
':('\
Eddie Gomez•Next Future•Stretch Records•1993','\
Tijuana Mon Amour Broadcasting Inc.•Cold Jubilee (Of The Snowqueen)•Tijuanamusic•2006','\
Sue Raney•Happiness Is A Warm Sue Raney•Philips•1964','\
Frank Sinatra•Trilogy: Past Present & Future•Reprise Records•1980','\
Various•American Popular Song: Six Decades Of Songwriters And Singers•Smithsonian Collection•1984','\
Frank Sinatra•The Complete Reprise Studio Recordings•Reprise Records•1995'),'\
\
Nice Work If You Can Get It\
':('\
The Benny Goodman Quartet•B. G. Jazz Concert•Philips•0','\
Paul Weston And His Orchestra•Nice Work If You Can Get It / A Chance At Love•Columbia•1955','\
The Andrews Sisters•Nice Work If You Can Get It / Bei Mir Bist Du Schon•Decca•1937','\
Billy Taylor Trio•Nice Work If You Can Get It / It\'s The Little Things That Mean So Much•Prestige•1954','\
Fats Navarro•Modern Jazz Trumpets•Prestige•1951','\
Bing Crosby•Bing Sings Whilst Bregman Swings (Volume 3)•Verve Records•0','\
Thelonious Monk•Something In Blue•Polydor•1972','\
Thelonious Monk•It\'s Monk\'s Time•Columbia•1964'),'\
\
Nigerian Marketplace\
':('\
Oscar Peterson•A Summer Night In Munich•Telarc Jazz•1999','\
The Oscar Peterson Trio•Nigerian Marketplace•Pablo Live•1982','\
Ramsey Lewis•We Meet Again•CBS•1989','\
The Oscar Peterson Big 4•Freedom Song (The Oscar Peterson Big 4 In Japan \'82)•Pablo Records•1983'),'\
\
Night And Day\
':('\
Quintette Du Hot Club De France•Undecided / Night And Day•Brunswick•1941','\
Artie Shaw And His Orchestra•Nightmare / Night And Day•Columbia•0','\
Erik Van Dam•Duo•Not On Label (Erik Van Dam Self-released)•2017','\
Coleman Hawkins Quartet•Night And Day / Flamethrower •Keynote Recordings (2)•1944','\
Joe Sullivan•Night And Day / Heavy Laden•Sunset Recordings (3)•1944','\
Diana Miller•Begin The Beguine / Night And Day•Sonora (2)•1940','\
Zoot Sims Quartet•Night And Day / Slingin\' Hasch•Vogue Productions•1950','\
Stan Getz Quartet•Prelude To A Kiss / Night And Day•Metronome•1951','\
Billie Holiday•Night And Day / The Man I Love•Vocalion (2)•1939','\
no artist•Night And Day / Some Of These Days•Odeon•0','\
Freddy Martin And His Orchestra•Grieg Piano Concerto / Night And Day •RCA Victor•1947','\
David Rose & His Orchestra•Night And Day / Easy To Love•RCA Victor•1946','\
Django Reinhardt Et Ses Rythmes•Nuages•Blue Star•1955','\
Benny Goodman And His Orchestra•Shake Down The Stars / Night And Day•Parlophone•1940','\
Frank Minion•Night And Day / Watermelon•Bethlehem Records•1960','\
Nina Simone•Do I Move You? / Day And Night•RCA Victor•1967','\
Billie Holiday•Night And Day / The Man I Love•Okeh•1940','\
Sonny Rollins•Live In London Volume 2•Harkit Records•2005','\
Jan August•Dancing In The Dark / Night And Day•Brunswick•1948','\
Stan Getz Quartet•I Only Have Eyes For You / Night And Day•Elite Special•0'),'\
\
Night Dreamer\
':('\
Erik Van Dam•Duo•Not On Label (Erik Van Dam Self-released)•2017','\
Terumasa Hino•Swing Journal Jazz Workshop 1 - Terumasa Hino Concert•Takt Jazz Series•1969','\
Wayne Shorter•Night Dreamer•Blue Note•1964','\
Al Di Meola•Scenario•Columbia•1983','\
Pixel (9)•We Are All Small Pixels•Cuneiform Records•2013','\
Charles Bobo Shaw•Junk Trap•Black Saint•1978','\
John Coltrane•Bahia•Prestige•1965'),'\
\
Night Has a Thousand Eyes\
':('\
Gloria Lynne•The Night Has A Thousand Eyes•Everest•1965','\
John Coltrane•Coltrane\'s Sound•Atlantic•1964','\
McCoy Tyner•Song For My Lady•Milestone (4)•1973','\
Toshiko Akiyoshi•Toshiko Meets Her Old Pals•King Records•1974'),'\
\
Night In Tunisia A\
':('\
Art Blakey & The Jazz Messengers•A Night In Tunisia•Blue Note•1960','\
The Miles Davis Quartet•A Night In Tunisia•Prestige•1958','\
Dizzy Gillespie•Jazz At Massey Hall Volume 4•Debut Records (3)•1958','\
The Charlie Parker Septet•A Night In Tunisia / Ornithology•Dial Records (3)•1946','\
The Miles Davis Quartet•The Musings Of Miles Vol. 3•Metronome•1956','\
Art Blakey Quintet•A Night At Birdland Vol. 2•Blue Note•1954','\
Art Blakey & The Jazz Messengers•A Night In Tunisia - Direct Session•Philips•1979','\
Art Blakey & The Jazz Messengers•Night In Tunisia - Digital Session•Philips•1979','\
Tony Fruscella•Tony Fruscella-Phil Woods Quintet•Stateside•0','\
The Quintet•Jazz At Massey Hall Volume Three•Debut Records•1953','\
Art Blakey Quintet•A Night At Birdland Volume 1•Blue Note•1956','\
Jimmy Forrest•Live At The Barrel•Prestige•1983'),'\
\
Nightlake\
':('\
John Abercrombie Quartet•Arcade•ECM Records•1979','\
John Abercrombie•Works•ECM Records•1988','\
Kenny Barron•Wanton Spirit•Gitanes Jazz Productions•1994','\
John Abercrombie•The First Quartet•ECM Records•2015','\
Richard Beirach•Ballads•CBS/Sony•1986','\
Paolo Fresu Quintet•Songlines / Night & Blue•Tǔk Music•2010'),'\
\
Nightmood (Lembra)\
':('\
Mark Murphy•Night Mood•Milestone (4)•1987'),'\
\
Nimbus\
':('\
Ralph Towner•Solstice•ECM Records•1975','\
Laurie Holloway•Cumulus•Hobo (2)•1979','\
Chick Corea•Antidote•Concord Jazz•2019','\
Chick Corea•Touchstone•Warner Bros. Records•1982','\
Forty Seven Times Its Own Weight•Cumulo Nimbus•Fable Records•1975','\
Metro (12)•Big Band Boom•Jazzline•2015','\
Samuel Rohrer•Range Of Regularity•Arjunamusic•2017','\
Aki Takase Trio•Aki•Seven Seas•1978','\
Ralph Towner•Works•ECM Records•1984'),'\
\
No Me Esqueca\
':('\
Joe Henderson•In Pursuit Of Blackness•Milestone (4)•1971','\
Tom Grant (2)•Mystified•Timeless Records (3)•1978','\
Charles Earland•Leaving This Planet•Prestige•1974','\
Joe Henderson•In Pursuit Of Blackness / Black Is The Color•Milestone (4)•1998','\
Quinteto Onze E Meia•Quinteto Onze E Meia•CID•1992','\
The Articles•Flip F\'real•Moon Ska•1997','\
Joe Henderson•The Milestone Years•Milestone (4)•1994'),'\
\
No Moe\
':('\
Sonny Rollins•Sonny Rollins With Modern Jazz Quartet•Prestige•1954','\
Bob Berg•Enter The Spirit•GRP•1993','\
Bud Shank Quartet•That Old Feeling•Contemporary Records•1986','\
Bill Frisell•Live•Gramavision•1995','\
Straight Ahead (2)•Body & Soul•Atlantic Jazz•1993','\
Sonny Rollins•Sonny Rollins•Prestige•1972','\
Sonny Rollins•Jazz Showcase•Original Jazz Classics•2006'),'\
\
No Moon At All\
':('\
The George Shearing Quintet•Velvet Carpet (Part 1)•Capitol Records•1956','\
Kellie Greene•Move On•20th Century Fox Records•1966','\
Les Brown And His Band Of Renown•Do Nothin\' Till You Hear From Me / No Moon At All•Coral•1953','\
The Conte Candoli Quartet•Conte Candoli Quartet•Mode Records•1957','\
Elsie Bianchi Trio•Trio Elsie Bianchi•Atlantis Basel•1962','\
Mari Wilson•I\'m Coming Home•Dino Entertainment•1992','\
Mary Ann McCall•Detour To The Moon •Jubilee•1958','\
Mary Ann McCall•Detour To The Moon •Jubilee•1958','\
Phineas Newborn Trio•Fabulous Phineas•RCA Victor•1958','\
The Jonah Jones Quartet•Jumpin\' With Jonah Part 1•Capitol Records•0','\
Siril Malmedal Hauge•Last Things•Oslo Session Recordings•2017','\
Phineas Newborn Jr.•Back Home•Contemporary Records•1985','\
Mel Tormé•Swingin\' On The Moon•Verve Records•1960'),'\
\
No Splice\
':('\
Lee Konitz•In Harvard Square•Storyville (3)•1955'),'\
\
No Way Out\
':('\
Sonny Rollins•Way Out West•Contemporary Records•1957','\
Sonny Rollins•Way Out West•Contemporary Records•1957','\
Professor Psygrooves•Foreign Pulses & Borderlines Dubs•Jarring Effects•2008','\
Bill Evans (3)•The Other Side Of Something•Intuition Records•2007','\
Gianfranco Continenza•Face The Truth•ESC Records•2011'),'\
\
Nonsequence\
':('\
Gary Burton•The New Quartet•ECM Records•1973'),'\
\
North Atlantic Run\
':('\
Gerry Mulligan•Mulligan•Lester Radio Corporation•1985','\
no artist•Idol Gossip•Chiaroscuro Records•1976','\
Lester Young•I Giganti Del Jazz Vol. 99•Curcio•1981','\
Gerry Mulligan•Paraiso Jazz Brazil•Telarc Jazz•1993'),'\
\
Nostalgia In Times Square\
':('\
Jemeel Moondoc Quintet•Nostalgia In Times Square•Soul Note•1986','\
Charles Mingus•Shadows•Doxy•2015','\
Trio HLP•Volume 1•Disques Dreyfus•1991','\
Teddy Charles Quartet•Live At The Verona Jazz Festival 1988•Soul Note•1989','\
Charles Mingus•Jazz Portraits•United Artists Records•1959','\
Medeski Martin & Wood•Free Magic•Indirecto Records•2013','\
Trio HLP•Humair Louiss Ponty•Disques Dreyfus•1997','\
Dannie Richmond•Plays Charles Mingus•Timeless Records (3)•1981','\
No BS Brass Band•Fight Song: A Tribute to Charles Mingus•Not On Label•2013','\
Orange Then Blue•Music For Jazz Orchestra•GM Recordings•1987'),'\
\
Not Ethiopia\
':('\
MVP (5)•Truth In Shredding•Tone Center•1990','\
The Brecker Brothers•Straphangin\'•Arista•1981','\
Steps (3)•Smokin\' In The Pit•Better Days (2)•1981','\
The Brecker Brothers•Collection / Volume Two•BMG•1991'),'\
\
Not Like This\
':('\
Peter Brötzmann•Noise Of Wings•Slask Records•1999','\
The Chris Ibenez Trio•Jumpin\' At The Executive Suite•Brunswick•1962','\
The Chris Ibenez Trio•The Swingin\' Chris Ibenez Trio Likes Garner•Brunswick•0','\
Mose Allison•The Word From Mose•Atlantic•1964','\
Janis Siegel•Slow Hot Wind•Varèse Sarabande•1995','\
Helen Merrill•Clear Out Of This World•EmArcy•1992','\
Till Brönner•Chattin With Chet•Verve Records•2000','\
Perry Como•Perry Como•RCA•1980','\
Al Jarreau•Jarreau•Warner Bros. Records•1983','\
Helen Carr•...Down In The Depths On The 90th Floor•Bethlehem Records•1955','\
TobyMac•This Is Not A Test•ForeFront Records•2015'),'\
\
Nothing Personal\
':('\
The Michael Brecker Band•The Michael Brecker Band Live•Jazz Door•1993','\
The Michael Brecker Band•The Cost Of Living•Jazz Door•1994','\
Michael Brecker•Michael Brecker•MCA Impulse!•1987','\
Karizma (3)•Document•Hudson Music•2000','\
Don Grolnick•Weaver Of Dreams•Blue Note•1990','\
Stefon Harris & Blackout•Evolution•Blue Note•2004','\
Dave Weckl Acoustic Band•Of The Same Mind•Universal•2015','\
Trio Acoustic•Autumn Leaves•Pannon Jazz•1995','\
Gilad Hekselman•This Just In•Jazz Village•2013','\
Annette Peacock•I Have No Feelings•Ironic Records•1986','\
Kristoffer Eikrem•Duets•Mutual Intentions•2018','\
Don Grolnick•The Complete Blue Note Recordings•Blue Note•1997','\
Billy Mayerl•The Versatility Of Billy Mayerl•Flapper•1982'),'\
\
Nowhere To Run\
':('\
The Gilmour Players•Norwegian Wood•Philips•1966','\
Jacky Vincent•Life Imitating Art•Not On Label•2018','\
Santana•Very Best Of Volume 2•Arcade•1986','\
Ruby Turner•The Motown Song Book•Jive•1988','\
Michael Bolton•Ain\'t No Mountain High Enough (A Tribute To Hitsville U.S.A.)•EMI Label Services•2012','\
Various•Dramatic Funk Themes Vol. 3 - Roaring Rare Grooves Action & Detective Breaks 1972-1983•ShowUp Records•2011','\
The Detroit Sound•Big Band Soul•Contour•1971','\
Gregory Porter•Issues Of Life - Features And Remixes•Membran•2014','\
The Style Council•Altered States•Not On Label (The Style Council)•1984','\
Various•Superbad•Warner Dance•2004','\
Various•Woman To Woman•Universal Music Group International•2008'),'\
\
Now\'s the Time\
':('\
Archie Shepp Quintet•Bird Fire•Impro•1979','\
Jack DeJohnette•The Jack DeJohnette Piano Album•Landmark Records (3)•1985','\
Ken McIntyre Sextet•Introducing The Vibrations•SteepleChase•1977','\
Karyn Kydd•The Bridge•Not On Label•1994','\
Dick Griffin•Now Is The Time•Trident (3)•1979','\
Eddie "Cleanhead" Vinson•Jamming The Blues•Black Lion Records•1975','\
Eddie "Cleanhead" Vinson•Jamming The Blues•Black Lion Records•1975','\
Grant Green•Slick! - Live at Oil Can Harry’s•Resonance Records•2018','\
Archie Shepp Quartet•I Didn\'t Know About You•Timeless Records (3)•1991','\
Takeshi Itoh•El Seven•CBS/Sony•1985','\
Bill Evans•Jazz \'Round Midnight•Verve Records•1993','\
Karl Berger•All Kinds Of Time•Sackville Recordings•1976','\
Ray Bryant•Ray Bryant Plays•Signature (4)•1960','\
Various•Voices Of Love 2•Evosound•2014','\
Cannonball Adderley Sextet•Jazz Workshop Revisited•Riverside Records•1963','\
Joe Albany•Bird Lives!•Interplay Records•1979'),'\
\
Nutville\
':('\
Angel "Cachete" Maldonado•Afro Caribbean Jazz•Montuno Records•1987','\
Hank Mobley•Another Monday Night At Birdland•Roulette•1959','\
The Horace Silver Quintet•The Cape Verdean Blues•Blue Note•1965','\
Tina Brooks•Minor Move•Blue Note•1980','\
Квартет Игоря Бутмана•Живая Коллекция (Live)•Moroz Records•2001','\
Charly Antolini•Wow!!!•Verve Records•1987','\
Buddy Rich Big Band•Buddy Rich Big Band•Europa Jazz•1981','\
Jamey Aebersold•Horace Silver - Eight Jazz Classics:  Volume 17•JA Records•1978','\
Michael Brecker•Live in Helsinki 1995•Random Act Records•2015','\
Jazzlife Sextet•Tall Stories•Dejavu•2009'),'\
\
Ode to the Doo Da Day\
':('\
Michael Brecker•Now You See It... (Now You Don\'t)•GRP•1990','\
Various•GRP 10th Anniversary Collection•GRP•1992'),'\
\
Of Thee I Sing\
':('\
Stan Getz•The Best of West Coast Sessions•Verve Records•1997','\
Stan Getz•And The "Cool" Sounds•Verve Records•1957','\
Cleo Laine•The Unbelievable•Fontana•1968','\
no artist•And All That Jazz•Columbia•1958','\
Lou Levy Trio•The Hymn•Philips•1963','\
Frankie Carle And His Orchestra•The Piano Style Of Frankie Carle•RCA Camden•1959','\
Jane Froman•Gems From Gershwin•RCA Victor•1954','\
The Andrews Sisters•Fresh And Fancy Free•Capitol Records•0','\
Kitty White•Sweet Talk•Roulette•1958','\
The National Jazz Trio Of Scotland•Standards Vol. V•Karaoke Kalk•2019','\
Music Minus One•Gershwin Anyone?•Music Minus One•0','\
George Gershwin•A Portrait Of George (Gershwin On Broadway & In Hollywood)•Turnabout•1979','\
George Gershwin•A Portrait Of George (Gershwin On Broadway & In Hollywood)•Turnabout•1979','\
Arthur Fiedler•I Got Rhythm: Fiedler Conducts Gershwin•London Records•1979','\
Red Callender•The Lowest•MetroJazz•1958'),'\
\
Off Flow\
':('\
Michel Herr•Perspective (Musique Contemporaine~Pop~Jazz)•Selection Records•1978','\
All That•The Whop Boom Bam•Upstart Records (3)•1999','\
Prince•Purple Palace•Red Hot (4)•1992','\
Madlib•Madlib Medicine Show: The Brick•Madlib Invazion•2012'),'\
\
Off Minor\
':('\
Thelonious Monk•Nutty - Monk And Trane•Riverside Records•1961','\
The Bud Powell Trio•Off Minor / I\'ll Remember April•Jazz Selection•0','\
The Barry Harris Sextet•Bull\'s Eye!•Prestige•1968','\
Tim Warfield•Dedicated To Thelonious Sphere Monk•Criss Cross Jazz•2015','\
Thelonious Monk•Hackensack•Drive (3)•1989','\
Thelonious Monk•Live In Paris Part 2•BYG Records•1975','\
Thelonious Monk•Monk\'s Music•Cinevox•1981'),'\
\
Oh Lady Be Good!\
':('\
no artist•Oh Lady Be Good / Liza•Decca•0','\
Benny Goodman Trio•China Boy / Oh Lady Be Good•Victor•1936','\
The Oscar Peterson Quartet•Album #2•Clef Records•1955','\
Artie Shaw And His Orchestra•Oh Lady Be Good / I Surrender Dear•Bluebird (3)•1939','\
Count Basie Orchestra•Blue And Sentimental / Oh Lady Be Good•Decca•1938','\
Teddy Wilson And His Orchestra•But Not For Me / Oh Lady Be Good•Columbia•1941','\
Count Basie Sextet•Oh Lady Be Good / I Want A Little Girl •Mercury•1952','\
Ella Fitzgerald•At The Opera House•Verve Records•1958','\
Count Basie Orchestra•Oh Lady Be Good / You Can Depend On Me•Decca•1939','\
The Dave Brubeck Trio•Give A Little Whistle / Tea For Two•Fantasy•0','\
Erroll Garner•Honeysuckle Rose / How High The Moon•Columbia•1954','\
Ella Fitzgerald•Smooth Sailing with Ella Fitzgerald•Decca•1953','\
Lester Young•With Count Basie And His Orchestra•Philips•0','\
Benny Goodman•Stompin\' At The Savoy•RCA•0','\
Benny Goodman Trio•Benny Goodman Trio-Quartet-Quintet•RCA Victor•0'),'\
\
Oh Lady Be Good\
':('\
no artist•Oh Lady Be Good / Liza•Decca•0','\
Benny Goodman Trio•China Boy / Oh Lady Be Good•Victor•1936','\
The Oscar Peterson Quartet•Album #2•Clef Records•1955','\
Artie Shaw And His Orchestra•Oh Lady Be Good / I Surrender Dear•Bluebird (3)•1939','\
Count Basie Orchestra•Blue And Sentimental / Oh Lady Be Good•Decca•1938','\
Ella Fitzgerald•At The Opera House•Verve Records•1958','\
Teddy Wilson And His Orchestra•But Not For Me / Oh Lady Be Good•Columbia•1941','\
Count Basie Sextet•Oh Lady Be Good / I Want A Little Girl •Mercury•1952','\
Count Basie Orchestra•Oh Lady Be Good / You Can Depend On Me•Decca•1939','\
The Dave Brubeck Trio•Give A Little Whistle / Tea For Two•Fantasy•0','\
Erroll Garner•Honeysuckle Rose / How High The Moon•Columbia•1954','\
Ella Fitzgerald•Smooth Sailing with Ella Fitzgerald•Decca•1953','\
Lester Young•With Count Basie And His Orchestra•Philips•0','\
Benny Goodman•Stompin\' At The Savoy•RCA•0'),'\
\
Old Country The\
':('\
Julie Kelly•Some Other Time•Chase Music Group•1989','\
Akira Ohmori•Back To The Wood•Denon•1987','\
Rick Margitza•Hope•Blue Note•1991','\
Nat Adderley And The Big Sax Section•That\'s Right!•Riverside Records•1960','\
Nat Adderley•Autobiography•Atlantic•1965','\
George Adams - Don Pullen Quartet•Breakthrough•Blue Note•1986','\
Ray Bryant•Trio Today•EmArcy•1987','\
Ryo Fukui•A Letter from Slowboat•Sapporo City Jazz•2016','\
David Murray Quartet•Shakill\'s Warrior•DIW•1991','\
Shirley Horn Trio•The Garden Of The Blues•SteepleChase•1985','\
Keith Jarrett Trio•Standards Live•ECM Records•1986','\
Charles Williams (15)•Trees And Grass And Things•Mainstream Records•1971','\
Gerry Mulligan Quartet•Recorded In Boston At Storyville•Pacific Jazz•1957','\
Sam Jones•The Soul Society•Riverside Records•1960','\
Shirley Horn Trio•The Garden Of The Blues•SteepleChase•1985'),'\
\
Old Devil Moon\
':('\
Sarah Vaughan•Old Devil Moon•Mercury•1957','\
Scott Hamilton•Who Cares?•Fonè•2015','\
Ella Fitzgerald•Old Devil Moon / Lover Come Back To Me•Brunswick•1955','\
Jackie Jocko•Please Believe Me / Old Devil Moon•Cabin Records (7)•1953','\
Milt Jackson•Goodbye•CTI Records•1974','\
Clifford Jordan And The Magic Triangle•On Stage Vol. 1•Steeplechase•1977','\
Miles Davis•That Old Devil Moon / You Don\'t Know What Love Is•Prestige•1964','\
Nancy Sinatra•Good Time Girl / Old Devil Moon•Reprise Records•1969','\
Joanne Brackeen•Snooze•Choice (7)•1975','\
Margaret Whiting•Ask Anyone Who Knows / Old Devil Moon•Capitol Records•0','\
George Benson•Benson & Farrell•CTI Records•1976'),'\
\
Old Folks\
':('\
Lee Morse•My Old Kentucky Home / The Old Folks At Home•Pathé Actuelle•1926','\
Miles Davis•Someday My Prince Will Come•CBS•1962','\
Seiichi Nakamura Quintet•The Boss - Live In "5 Days In Jazz" 1974•Three Blind Mice•2014','\
Charlie Parker And His Orchestra•In The Still Of The Night / Old Folks•Clef Records•1953','\
Jimmy Smith•Open House•Blue Note•1968','\
Louis Armstrong•In The Shade Of The Old Apple Tree / The Old Folks At Home•Decca•1937','\
The Modern Jazz Sextet•The Modern Jazz Sextet•Verve Records•0','\
Grant Green•Grantstand•Blue Note•1962','\
James Williams (2)•James Williams Meets The Saxophone Masters•Columbia•1992'),'\
\
Ole\
':('\
John Coltrane•Olé Coltrane•Atlantic•1961'),'\
\
Oleo\
':('\
The Miles Davis Quintet•Airegin / Oleo•Metronome•1959','\
Sonny Rollins Quintet•In Europe•Unique Jazz•0','\
Joe McPhee Po Music•Oleo•hat MUSICS•1983','\
Nat Adderley Quartet•Naturally!•JAZZLAND•1962','\
Sonny Rollins•Our Man In Jazz•RCA Victor•1963','\
Vic Lewis West Coast All-Stars•Plays Bill Holman•Candid•1993','\
Miles Davis•Saturday Night At The Blackhawk•CBS•1962','\
George Benson•Oleo•Music Mirror•1993','\
George Benson•Jazz On A Sunday Afternoon Vol. II•Accord (2)•1981','\
The Jeremy Steig Quartet•Oleo / Dark As A Dungeon•Columbia•1964','\
Teddy Edwards Quartet•Good Gravy•Timeless Records (3)•1984','\
Urbie Green•Oleo•Pausa Records•1978'),'\
\
Olhos De Gato\
':('\
Jazztrack•Listen!•Happy Bird•1977','\
Paul Bley•Paul Bley / NHØP•SteepleChase•1973','\
Paul Bley•Homage To Carla•Owl Records (4)•1993','\
Gary Burton•Works•ECM Records•1984','\
Gary Burton•The New Quartet•ECM Records•1973','\
Enrico Rava Quartet•Il Giro Del Giorno In 80 Mondi•Fonit Cetra International•1972','\
Gary Burton•Quartet Live•Concord Jazz•2009','\
Rudolf Dašek•Mezipřistání / Inter-Landing•Supraphon•1984'),'\
\
Oliloqui Valley\
':('\
Herbie Hancock•The Egg•Music Mirror•1993','\
Herbie Hancock•Empyrean Isles•Blue Note•1964','\
Herbie Hancock•Great Sessions•Blue Note•2006','\
Herbie Hancock•The Best Of Herbie Hancock•Blue Note•1971','\
Eddie Henderson•Inspiration•Milestone (4)•1995','\
Christian McBride•Fingerpainting (The Music Of Herbie Hancock)•Verve Records•1997'),'\
\
On A Clear Day\
':('\
Wynton Kelly•In Concert•VJ International•1977','\
The Oscar Peterson Trio•The Good Life•Pablo Live•1984','\
Frank Sinatra•Strangers In The Night•Reprise Records•1966','\
Ted Taylor Music•Waltzes & Quicksteps•IDTA•1971','\
Elias Haslanger•Church On Monday•Cherrywood Records•2012','\
The Peddlers•On A Clear Day You Can See Forever / Comin\' Home Baby•Epic•1969','\
Bill Evans•Alone•Verve Records•1968','\
Vocal Jazz Incorporated•High Clouds•Grapevine (4)•1977','\
David Liebman Group•Conversation•Sunnyside•2003','\
Trio Karel Boehlee•Switch•Timeless Records (3)•1984','\
Mari Nakamoto•Mari•Three Blind Mice•1977','\
Jimmy Powell•The Shadow Of Your Smile•Jubilee•0','\
Oscar Peterson•Oscar Peterson In Paris•Joker (2)•1977','\
Sonny Criss•Portrait Of Sonny Criss•Prestige•1967','\
Dee Dee Bridgewater•Live In Paris•Affinity•1987','\
Mieko Hirota•Miko Live•Columbia•1971'),'\
\
On A Misty Night\
':('\
Tadd Dameron•Mating Call•Prestige•1957','\
Pharoah Sanders•Heart Is A Melody•Theresa Records•1983','\
The Chet Baker Quintet•Boppin\' With The Chet Baker Quintet•Prestige•1967','\
Tubby Hayes•The Jazz Couriers•Tempo Records (5)•1957','\
Tubby Hayes•The Jazz Couriers•Tempo Records (5)•1957','\
The Jazz Couriers•The First And Last Words•Jasmine Records•2001','\
Sonny Stitt•Sonny Stitt & The Top Brass•Atlantic•1962','\
Howard McGhee•Young At Heart•Storyville•1983','\
Eric Alexander Quartet•Chim Chim Cheree•Venus Records (5)•2010','\
Jesse Davis (3)•High Standards•Concord Jazz•1994','\
Gary Bartz•There Goes The Neighborhood!•Candid•1991'),'\
\
One Finger Snap\
':('\
Herbie Hancock•The Egg•Music Mirror•1993','\
Herbie Hancock•Empyrean Isles•Blue Note•1964','\
Nate Morgan•Retribution Reparation•Nimbus West Records•1984','\
Mel Lewis•Live In Montreux•MPS Records•1981','\
Kirk Lightsey Quartet•First Affairs•Lime Tree•1987','\
Larry Willis Trio•Just In Time•SteepleChase Productions ApS•1989','\
Rufus Reid Trio•Perpetual Stroll•Theresa Records•1981','\
The Toon Roos Quartet•Attitudes•Timeless Records (3)•1988'),'\
\
On for Daddy-o\
':('\
Clark Terry•Out On A Limb•Argo (6)•1957','\
Cannonball Adderley•Somethin\' Else•Not Now Music•2010','\
Miles Davis•Miles \'58•Not Now Music•2009','\
Louis Jordan And His Tympany Five•Five Guys Named Moe•Bandstand•1992','\
Louis Armstrong•West End Blues •DeAgostini•1990','\
Charlie Christian•The Genius Of The Electric Guitar•Columbia•2002','\
Benny Goodman•Jazz Milestones•The Franklin Mint Record Society•1984','\
Various•Fabulous Memories Of The Fabulous \'40s•no label•1981','\
Freddy Martin And His Orchestra•C\'mon Let\'s Dance!•Capitol Records•1961','\
Lawrence Welk And His Champagne Music•Listening And Dancing•no label•1968','\
Roger Williams (2)•America\'s Best Selling Pianist: 4 Original Albums 1957-1961•Jasmine Records•2012','\
Ralph Marterie And His Orchestra•51 Country Club Dance Favorites•Musicor Records•0','\
Various•The Big Horn (The History Of Honkin\' & Screamin\' Saxophone)•Proper Records (2)•2003','\
Miles Davis•Twenty Classic Albums•Real Gone•2011'),'\
\
On the Stairs\
':('\
Pat Martino•Consciousness•Muse Records•1974','\
Dave Matthews (3)•Big Band Recorded Live At The "Five Spot"•Muse Records•1975','\
Commuters•Commuters•Amphibious Records (2)•1982','\
Various•GRP Digital Sampler  Vol.1•GRP•1984','\
Alan Barnes•Manhattan•Concord Jazz•2001','\
Jim Self•Tricky Lix•Concord Jazz•1991','\
Various•One Night With Blue Note Volume 2•Blue Note•1985','\
no artist•What\'s New?•Atlantic•1971','\
Pat Martino•Formidable•HighNote Records Inc.•2017','\
Nicky Holland•Nicky Holland•Epic Associated•1992','\
Andy Sheppard•Trio Libero•ECM Records•2012','\
Tito Rodriguez•Motion Picture Themes Cha Cha Cha•United Artists Ultra Audio•0','\
Gerry Mulligan•Symphonic Dreams•PAR (4)•1987'),'\
\
On the Sunny Side of the Street\
':('\
Louis Armstrong And His Orchestra•On The Sunny Side Of The Street•Brunswick•0','\
Tommy Dorsey And His Orchestra•Who?•RCA Victor•1955','\
Tommy Dorsey And His Orchestra•Boogie Woogie / On The Sunny Side Of The Street•RCA Victor•1946','\
Tommy Dorsey And His Orchestra•Boogie Woogie / On The Sunny Side Of The Street•RCA Victor•1946','\
Lionel Hampton And His Orchestra•On The Sunny Side Of The Street / Rhythm Rhythm•no label•0','\
Lionel Hampton And His Orchestra•Ring Them Bells / On The Sunny Side Of The Street•no label•1952','\
Louis Armstrong And His All-Stars•New Orleans Function / On The Sunny Side Of The Street•Brunswick•1955','\
Chick Webb And His Orchestra•On The Sunny Side Of The Street / Blue Minor•Decca•1934','\
Duke Ellington And His Orchestra•Good Woman Blues / On The Sunny Side Of The Street •Columbia•1949','\
Tab Smith•On The Sunny Side Of The Street / Tab\'s Purple Heart•King Records (3)•1952','\
Tommy Dorsey And His Orchestra•On The Sunny Side Of The Street / There\'s No You•no label•0','\
Rex Stewart & His Sydney Six•On The Sunny Side Of The Street / Boog It Jack•Wilco Records (2)•1949','\
Tommy Dorsey And His Orchestra•Hawaiian War Chant / On The Sunny Side Of The Street•RCA Victor•0','\
Johnny Hodges And His Orchestra•On The Sunny Side Of The Street / All Of Me•Norgran Records•1955','\
Benny Goodman Sextet•On The Sunny Side Of The Street / The Wang Wang Blues•Parlophone•1942','\
Coleman Hawkins•I Ain\'t Got Nobody / On The Sunny Side Of The Street•Parlophone•1934','\
The Lester Young Sextet•Sax-O-Be-Bop / On The Sunny Side Of The Street•Aladdin (6)•1947','\
Bing Crosby•On The Sunny Side Of The Street / Pinetop\'s Boogie Woogie •Decca•1947','\
Ted Lewis And His Band•On The Sunny Side Of The Street / Singing A Vagabond Song•Columbia•1930','\
Lionel Hampton Quintet•The Lionel Hampton Quintet•Karusell•1955','\
Erroll Garner•On The Sunny Side Of The Street•Savoy Records•0','\
Louis Armstrong And His Orchestra•Once In A While / On The Sunny Side Of The Street•Decca•1937','\
Billie Holiday•I Love My Man / On The Sunny Side Of The Street•Commodore•1948','\
Louis Armstrong•Mahogany Hall Blues Stomp / On The Sunny Side Of The Street•Philips•1960'),'\
\
On the Trail\
':('\
101 Strings•Ferde Grofe\'s Grand Canyon Suite•Somerset•1958','\
Al Cohn•Silver Blue•Xanadu Records•1977','\
Earl Backus•Guitar In The Night•Epic•0','\
Ray Anthony & His Orchestra•Ray Anthony Concert•Capitol Records•1953','\
Kenny Barron•In Tandem•Muse Records•1980','\
Various•Jazz For A Sunday Afternoon Volume 2•Solid State Records (2)•1968','\
Paul Whiteman & His Concert Orchestra•On The Trail•Victor•1943','\
Richard Davis (2)•Dealin\' (Live At Sweet Basil)•Sweet Basil (2)•1991','\
no artist•On The Trail•Buena Vista Records•1959','\
Jackie McLean•The Meeting Vol.1•SteepleChase•1974','\
Wynton Kelly•In Concert•VJ International•1977','\
Isao Suzuki & His Fellows•Touch•Three Blind Mice•1976','\
Pepper Adams•Village Vanguard Live Sessions 2•Lester Recording Catalog•1990','\
George Gershwin•Rhapsody In Blue Complete And Grand Canyon Suite Excerpts•RCA Victor•1957'),'\
\
Once I Loved\
':('\
Mel Lewis Quintet•The New Mel Lewis Quintet Live•Sandra Music Productions•1979','\
Gene Ammons•Brasswind•Prestige•1974','\
Bill Hardman•Home•Muse Records•1978','\
Lee Konitz•Brazilian Serenade•Venus Records (5)•1996','\
Chet Baker•Chet Baker - Steve Houben•Not On Label•1980','\
Ronnie Mathews•Song For Leslie•Red Record•1980','\
Horace Parlan Trio•Hi-Fly•SteepleChase•1978','\
McCoy Tyner•Trident•Milestone (4)•1975','\
Shelly Manne•Plays Richard Rodgers•Discovery Records•1977','\
Cedar Walton•The Trio 3•Red Record•1986','\
The Monty Alexander Trio•Full Steam Ahead•Concord Records•1985','\
Hal Galper•Dreamsville•Enja Records•1987','\
Shigeharu Mukai•Hip Cruiser•Better Days (2)•1979','\
Pat Martino•El Hombre•Prestige•1967','\
Rita Reys•Sings Antonio Carlos Jobim•Philips•1981'),'\
\
Once In A While\
':('\
Art Blakey•Quicksilver•Blue Note•1956','\
Felix King And His Orchestra•Bewitched•Decca•1950','\
Ulf Linde Quintet•Dinah / Once In A While•Metronome•1950','\
Earl Bostic And His Orchestra•Gondola / Once In A While•King Records (3)•1958','\
Erroll Garner•Gone Garner Gonest - Vol. 2•Columbia•0','\
Art Blakey Quintet•A Night At Birdland Volume 1•Blue Note•1954','\
Wilbur Harden•Tanganyika Strut•Savoy Records•1958','\
Sarah Vaughan•The Man I Love•MGM Records•1949','\
Louis Armstrong And His Orchestra•Once In A While / Confessin\' (That I Love You)•Decca•1952','\
Art Blakey Quintet•A Night At Birdland Volume 1•Blue Note•1956','\
Tommy Dorsey And His Orchestra•Once In A While / Not So Quiet Please•RCA Victor•0'),'\
\
One Bird One Stone\
':('\
Don Grolnick Group•Complete London Concert•Fuzzy Memories Music Archives•2014','\
Don Grolnick•The Complete Blue Note Recordings•Blue Note•1997','\
The London Big Sound•Reg Tilsley\'s Band Grooves Of The 60\'s•De Wolfe Music•1996','\
Bob Dylan•Radio Radio: Theme Time Radio Hour Volume Three•Mischief Music•2010','\
Various•Jazz Masters•Tandem Verlag Audio Line•0','\
Various•For Lee Jackson In Space•Not On Label•2012','\
Various•Les Triomphes Du Jazz•Habana•2000','\
Various•Les Triomphes Du Blues•Habana•2001','\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014','\
Various•Sony Music 100 Years: Soundtrack For A Century•Sony Music•1999'),'\
\
One By One\
':('\
The Jazz Messengers•The Legacy Of Art Blakey - Live At The Iridium•Telarc•1998','\
Art Blakey & The Jazz Messengers•Dr.Jeckyle•Paddle Wheel•1987','\
Art Blakey & The Jazz Messengers•Oh-By The Way•Timeless Records (3)•1982','\
Billy Vaughn And His Orchestra•Chapel By The Sea / One Love One Heartache•Dot Records•1962','\
no artist•One By One•Island Records•1974','\
Ted Lewis And His Band•All By Myself / One Kiss•Columbia•1921','\
Gray Matter (6)•Footsteps•Not On Label (Gray Matter (6) Self-released)•2015','\
Wynton Marsalis•The All American Hero•no label•1985','\
Wynton Marsalis•The All American Hero•TIM The International Music Company AG•2000','\
Borgmann / Morris / Charles Trio•Live In Poland•Sagittarius A-Star•2010','\
Wynton Marsalis•The All American Hero•no label•1985','\
Borgmann / Morris / Charles Trio•Live In Poland•Sagittarius A-Star•2010','\
Wynton Marsalis•The All American Hero•TIM The International Music Company AG•2000','\
Ramsey Lewis•One Two Three / Down By The Riverside•Cadet•1967','\
Teddy Edwards•The Inimitable•Xanadu Records•1976','\
Wynton Marsalis•Vol.1 - Time Will Tell•Jazz Hour•1992','\
Mal Waldron•Mal/2•Prestige•1957','\
Wynton Marsalis•The Jazz Masters - 100 Años De Swing•Folio Collection•1996','\
The Jeff Hamilton Quintet•Indiana•Concord Jazz•1982'),'\
\
One Family\
':('\
Jan Akkerman•Oil In The Family•CNR•1981','\
Yellowjackets•Shades•MCA Records•1986','\
Mark Guiliana Jazz Quartet•Family First•Beat Music Productions•2015','\
Larry Carlton•Singing / Playing•Blue Thumb Records•1973','\
David Murray•Fo Deuk Revue•Enja Records•1997','\
The RH Factor•Distractions•Verve Records•2006','\
Roy Ayers•Drive•Ichiban Records•1988','\
Roy Ayers•Lots Of Love•Uno Melodic Records•1983','\
Various•Drum Nation (Volume Two)•Magna Carta•2005','\
Walter Murphy And His Orchestra•Family Guy Live In Vegas•Geffen Records•2005','\
Warne Marsh Quartet•Berlin 1980•Gambit Records•2006','\
Jack Trombey•Topsy Turvy•Rouge Music Ltd.•1985','\
Jaki Byard•Live At Maybeck Recital Hall Volume Seventeen•Concord Jazz•1992','\
Kamasi Washington•Heaven And Earth•Young Turks•2018'),'\
\
One Foot In the Gutter\
':('\
Curtis Fuller•Poll Winners Jazz•Fontana•1960','\
The Dave Bailey Sextet•One Foot In The Gutter: A Treasury Of Soul•Epic•1960','\
Clark Terry•The Globetrotter•Vanguard•1977','\
Clark Terry•In Orbit•Riverside Records•1958','\
Clark Terry•The Second Set - Recorded Live At The Village Gate•Chesky Records•1995','\
The Dave Bailey Quintet•The Complete 1 & 2 Feet In The Gutter Sessions•Lone Hill Jazz•2005','\
Willie Rodriguez Jazz Quartet•Flatjacks•Riverside Records•1963','\
Clark Terry•Cruising•Milestone (4)•1975','\
Oscar Brown Jr.•Tells It Like It Is!•Columbia•1963','\
Jackie Washington (2)•Blues & Sentimental•Knight II Records•1976','\
Louis Armstrong•His Greatest Years 1925-1928•Odeon•1972','\
Louis Armstrong•The Essential Recordings 1925-1940•Charly Records•1995'),'\
\
One For My Baby\
':('\
Della Reese•One For My Baby / My Melancholy Baby•Jubilee•1956','\
Frank Sinatra•One For My Baby / Willow Weep For Me•Capitol Records•1956','\
Frank Sinatra•I\'ve Got You Under My Skin / One For My Baby (And One More For The Road)•Capitol Records•0','\
Joe Guy•Trumpet Battle At Minton\'s•Xanadu Records•1975','\
Fran Warren•I Gotta Right To Sing The Blues•RCA Victor•1951','\
Frank Sinatra•I\'ve Got A Crush On You •Capitol Records•1994','\
Lena Horne•I Didn\'t Know About You / One For My Baby•Victor•1945','\
Helge Schneider•Heart Attack No.1•Polydor•2017','\
David "Fathead" Newman•Still Hard Times•Muse Records•1982','\
Al Saxon•Al Saxon Sings Sinatra•Forest Records (2)•1971','\
Tal Farlow•Chromatic Palette•Concord Jazz•1981','\
Billie Holiday•Songs For Distingué Lovers•Verve Records•1958','\
Don Shirley•Drown In My Own Tears•Cadence (2)•1962'),'\
\
One Hundred Ways\
':('\
Quincy Jones•One Hundred Ways•A&M Records•1981','\
David Sanborn•Straight To The Heart•Warner Bros. Records•1984','\
Quincy Jones•One Hundred Ways / The Dude•A&M Records•1982','\
Brother Jack McDuff•The Reentry•Muse Records•1988','\
Richard "Groove" Holmes•Swedish Lullaby•Sison•1984','\
David Sanborn•Straight To The Heart•Warner Bros. Records•1984'),'\
\
One Note Samba\
':('\
The Modern Jazz Quartet•One Note Samba•Atlantic•1964','\
Enoch Light Big Band Bossa Nova•Desafinado / One Note Samba•Command•1962','\
Pat Thomas (5)•Desafinado / One Note Samba•Verve Records•1962','\
Earl Grant•My Foolish Heart / One Note Samba•Decca•1968','\
Betty Carter•One Note Samba - Bossa Nova•ATCO Records•1962','\
Antonio Carlos Jobim•Corcovado / One Note Samba•Verve Records•1964','\
Antonio Carlos Jobim•The Girl From Ipanema•Verve Records•0','\
The Howard Roberts Quartet•H.R. Is A Dirty Guitar Player•Capitol Records•0','\
Herbie Mann•Brazil Bossa Nova & Blues•United Artists Jazz•1962','\
Leroy Holmes•Bossa Nova•United Artists Records•1962','\
Various•Jazz Super Hits•Atlantic•1969','\
Herbie Mann•Sugarloaf - Jazz Impressions Of Brazil•Solid State Records (2)•1968'),'\
\
OOO Baby Baby\
':('\
Ella Fitzgerald•OOO Baby Baby•Reprise Records•0','\
Mats/Morgan•Trends And Other Diseases•Ultimate Audio Entertainment•1996','\
Dave Stahl Band•Miranda•Abee Cake Records•1988','\
Hugh Masekela•Uptownship•Novus•1989','\
Ella Fitzgerald•Star-Collection•Midi•0','\
Ella Fitzgerald•Ella•Reprise Records•1969','\
Stu Phillips•Feels Like Lovin\'•Capitol Records•1965','\
Ruby Turner•The Motown Song Book•Jive•1988','\
Various•Movements 4•Tramp Records•2012','\
Marlena Shaw•Dangerous•Concord Jazz•1996','\
Ella Fitzgerald•Ella / Things Ain\'t What They Used To Be (And You Better Believe It)•Reprise Records•1989'),'\
\
Open Your Eyes You Can Fly\
':('\
Flora Purim•Open Your Eyes You Can Fly•Omega International•1976','\
Gary Burton•The New Quartet•ECM Records•1973','\
Flora Purim•Milestone Memories•BGP Records•1988','\
Flora Purim•Love Reborn•Milestone (4)•1980','\
Lizz Wright•Salt•Verve Records•2003','\
Flora Purim•Open Your Eyes You Can Fly•Milestone (4)•1976','\
Nat King Cole•Nat King Cole•Capitol Records•1992'),'\
\
Opus De Funk\
':('\
Milt Jackson•Opus De Jazz•Savoy Records•1955','\
Woody Herman And His Third Herd•Road Band!•Capitol Records•1956','\
Milt Jackson Quintet•Milt Jackson Quintet•Prestige•1954','\
Milt Jackson•Goodbye•CTI Records•1974','\
Tal Farlow•Fuerst Set•Xanadu Records•1975','\
Milt Jackson•From Opus De Jazz To Jazz Skyline•Savoy Jazz•1986','\
Horace Silver•The Best Of Horace Silver Vol. I•Blue Note•1988'),'\
\
Orbits\
':('\
The Miles Davis Quintet•Miles Smiles•Columbia•1967','\
Medeski Martin & Wood•Notes From The Underground•Accurate Records•1992','\
Medeski Martin & Wood•Notes From The Underground•Accurate Records•1992','\
Miles Davis•Orbits•Columbia Musical Treasuries•1968','\
Wayne Shorter•Alegría•Verve Records•2003'),'\
\
Ornithology\
':('\
Barry Harris (2)•Tokyo: 1976•Xanadu Records•1980','\
Charlie Parker•Le Jazz Cool Historical Recordings Vol. 1•Le Jazz Cool•1960','\
Charlie Parker•Charlie Parker On Dial Volume 1•Spotlite Records•1970','\
The Charlie Parker Septet•A Night In Tunisia / Ornithology•Dial Records (3)•1946','\
Charlie Parker•1949 Concert•Alamac•0','\
Charlie Parker•Yardbird In Lotus Land•Spotlite Records•1976','\
The Bud Powell Trio•You Go To My Head / Ornithology•Blue Note•1949','\
Charlie Parker•Bird At The Hi-Hat•Blue Note•1993','\
Charlie Parker•Memories Of Bird•Esquire•0','\
The Charlie Parker All-Stars•Night In Tunisia•Sonet•0','\
Dave Pike•Bluebird•Timeless Records (3)•1991','\
Charlie Parker•Charlie Parker Septet•Jazztone (2)•1956','\
Charlie Parker•Be Bop•United Audio Entertainment•1995','\
Anthony Braxton•In The Tradition•SteepleChase•1974'),'\
\
Our Delight\
':('\
Fats Navarro•At The Royal Roost 1948 (Volume 2)•Beppo Records•0','\
The Eddie "Lockjaw" Davis Quintet•Jaws In Orbit•Metronome•1960','\
The Tadd Dameron Sextet•Our Delight / The Squirrel•Blue Note•1948','\
Dizzy Gillespie And His Orchestra•Our Delight / Good Dues Blues•Musicraft•1946','\
Fats Navarro•The Fabulous Fats Navarro Volume 1•Blue Note•1957','\
Roy Haynes•We Three•New Jazz•1959','\
Eddie "Lockjaw" Davis•Live! The Midnight Show•Prestige•1964','\
George Wallington Quintet•Jazz For The Carriage Trade•Prestige•1956','\
Miles Davis•Lady Bird•Jazz Showcase•1975','\
Shelly Manne & His Men•At The Black Hawk Vol. 1•Contemporary Records•1960'),'\
\
Our Love Is Here To Stay\
':('\
Maynard Ferguson•Jam Session Featuring Maynard Ferguson•Emarcy•1955','\
Lionel Hampton And His Orchestra•Hamp\'s Session•Vergara•1965','\
Bob Tracy His Strings And His Big Band•Dancing To Gershwin•Concert Hall•1969','\
Harry Arnold & His Swedish Radio Studio Orchestra•This Is Harry•Metronome•1958','\
Roland Kirk•Introducing Roland Kirk•Argo (6)•1960','\
Maynard Ferguson•Hollywood Jam Sessions•Fresh Sound Records•2005','\
Ivo Robić•Ivo Robić Sings In Two Moods•Supraphon•0','\
George Wallington Quintet•Jazz For The Carriage Trade•Prestige•1956','\
Romano Mussolini Trio•Romano Mussolini Trio•RCA Italiana•1957','\
Romano Mussolini Trio•Romano Mussolini Trio•RCA Italiana•1957'),'\
\
Out A Day\
':('\
Jackie McLean Quintet•Lights Out!•Prestige•1956','\
Lennie Niehaus•Vol.1 The Quintet•Contemporary Records•1954','\
Stuart McKay (2)•Take Me Out To The Ball Game•RCA Victor•0','\
Dinah Washington•After Hours With Miss D•Emarcy•1955','\
Stan Kenton And His Orchestra•Road Show Volume 1•Creative World•1975','\
Frank Sinatra•Songs For Young Lovers (Part 2)•Capitol Records•1954','\
Various•New York Stories•Blue Note•1992','\
Bill Watrous•Bone-ified•GNP Crescendo•1992','\
Pepper Adams Donald Byrd Quintet•Out Of This World•Warwick•1961','\
Ab Und Zu•Ab Und Zu•EMI•1989','\
Billie Holiday•Songs For Distingué Lovers•Verve Records•1958','\
Grady Martin And The Slew Foot Five•Slew Foot Style•Festival Records•1956','\
The Caravan Orchestra•Cole Porter Dance Album•Caravan (4)•1949','\
George Cables Trio•Some Of My Favorite Things•Atlas Record (2)•1980'),'\
\
Out Back of the Barn\
':('\
Gerry Mulligan•Mulligan•Lester Radio Corporation•1985','\
no artist•Idol Gossip•Chiaroscuro Records•1976','\
Lester Young•I Giganti Del Jazz Vol. 99•Curcio•1981','\
Various•Soho Scene \'62 - Jazz Goes Mod•Rhythm & Blues Records•2016','\
The John Wilson Orchestra•That\'s Entertainment: A Celebration Of The MGM Film Musical•EMI Classics•2011'),'\
\
Out of Nowhere\
':('\
Stan Getz Quartet•Live In Düsseldorf 1960•Jazzline•2014','\
Paul Smith Quartet•Out Of Nowhere / S\'wonderful•Modern Music (7)•0','\
Erroll Garner•Out Of Nowhere / Music Maestro Please•Columbia•0','\
Sidney Bechet•Out Of Nowhere / Mon Homme•Vogue Productions•1949','\
Charlie Parker•Charlie Parker On Dial Volume 5•Spotlite Records•1970','\
Coleman Hawkins And His All Star Jam Band•Sweet Georgia Brown / Out Of Nowhere•no label•0','\
Ella Fitzgerald•Stairway To The Stars / Out Of Nowhere•Decca•1947','\
Artie Shaw And His Orchestra•Out Of Nowhere / I\'m Coming Virginia•Bluebird (3)•0','\
James Moody And His Band•Lester Leaps In / Out Of Nowhere•Prestige•1950','\
The Dick Hyman Trio•Unforgettable / Out Of Nowhere•MGM Records•1954','\
The Dave Brubeck Quartet•Take The "A" Train•Philips•1962','\
The Dick Hyman Trio•Unforgettable / Out Of Nowhere•MGM Records•1954','\
Tony Fruscella•The Unique - Tony\'s Blues•Cool & Blue Records•1992','\
Bob & Phil And The Orchestra•Pussyfoot / Out Of Nowhere•Project 3 Records•0','\
Charlie Parker With Strings•You Came Along From Out Of Nowhere / East Of The Sun•Mercury•1950','\
Jazz Superstars•A Live Jam Session Recorded at "Trade Winds"•Jam Session Records (2)•0','\
Tommy Dorsey And His Orchestra•Hong Kong Blues / You Came Along•Victor•1945'),'\
\
Out of the World\
':('\
Frank Comstock•Music From Outer Space•Warner Bros. Records•1962','\
The John Coltrane Quartet•Coltrane•Impulse!•1962','\
The Three Sounds•Out Of This World•Blue Note•1966','\
Stan Kenton•Back To Balboa•Capitol Records•1958','\
Lew Tabackin•Dual Nature•Inner City Records•1978','\
Bill Holman / Mel Lewis Quintet•Jive For Five•Andex•1959','\
Hal McKusick Quartet•Jazz At The Academy•Coral•1957','\
Stan Kenton•Back To Balboa•Capitol Records•1958'),'\
\
Over The Rainbow Somewhere\
':('\
Shorty Rogers And His Giants•Modern Sounds Part 1•Capitol Records•0','\
Dizzy Gillespie And His Orchestra•Over The Rainbow / Joogie Boogie•Verve Records•1957','\
Zoot Sims•Stella By Starlight / Over The Rainbow•Impulse!•1967','\
Erroll Garner•More Than You Know•Regent•1950','\
no artist•Over The Rainbow / Cole Heat Warm Feet•National Records (2)•1945','\
Larry Clinton And His Orchestra•Over The Rainbow / The Jitterbug•Victor•1939','\
Glenn Miller And His Orchestra•Over The Rainbow / Ding-Dong! The Witch Is Dead•Bluebird (3)•1939','\
Art Pepper•Neon Art: Volume Two•Omnivore Recordings•2012','\
Stan Getz•Cool Stan In Cool Sweden Vol. 3•Karusell•1956','\
Paola Orlandi•L\'Arcobaleno (Over The Rainbow) / Voglio L\'Amore•RCA Camden•1959','\
Art Pepper•Landscape - Art Pepper Live In Tokyo \'79•JVC•1979','\
Various•Wildflowers 1 (The New York Loft Jazz Sessions)•Douglas•1977','\
Cedar Walton Quintet•Cedar\'s Blues: Cedar Walton Quintet Live•Red Record•1985','\
Frank Sinatra•All The Things You Are / Over The Rainbow•Columbia•1948','\
Shorty Rogers And His Giants•Modern Sounds•Capitol Records•1952'),'\
\
Oye Como Va\
':('\
Kora Jazz Band•Kora Jazz Band And Guests•Celluloid•2011','\
The Latin Percussion Jazz Ensemble•Live At The Montreux Jazz Festival 1980•Latin Percussion Ventures Inc.•1980','\
Bobby Hutcherson•Montara•Blue Note•1975','\
Tito Puente•The Latin World Of Tito Puente (El Mundo De Latino Tito Puente•Tico Records•1964','\
no artist•Tito Puente\'s Golden Latin Jazz•Bat Discos•1993','\
Cheo Feliciano•Para Enamorados Solamente•Seeco•1975','\
Tito Puente•No Hay Mejor - There Is No Better•Tico Records•1975','\
Tito Puente & His Latin Ensemble•El Rey•Concord Jazz Picante•1984','\
Michel Camilo•Thru My Eyes•TropiJazz•1997'),'\
\
Oz\
':('\
Janne Schaffer•Traffic•Earmeal•1985','\
Yellowjackets•Politics•GRP•1988','\
Kenny Clarke•Kenny Clarke & Ernie Wilkins•Savoy Records•1955','\
Andy Narell•Stickman•Hip Pocket Records•1981','\
Mike Nock Quartet•Dark & Curious•ABC Records (3)•1990','\
Yellowjackets•Collection•GRP•1995','\
Grupo Oz•Grupo Oz•Diresa•1973','\
Makoto Ozone The Trio•Real•Verve Records•2005','\
Marcin Wasilewski Trio•Faithful•ECM Records•2011'),'\
\
Palo-Alto\
':('\
Richie Cole•Return To Alto Acres•Palo Alto Records•1982','\
Lee Konitz•Parallels•Chesky Records•2001','\
"Jojo" Takayanagi Second Concept•Cool Jojo•Three Blind Mice•1980','\
Lee Konitz•Subconscious-Lee•Prestige•1955','\
Ken Peplowski•Encore•Concord Jazz•1995','\
Lee Konitz•The New Sounds•Prestige•1951','\
Lee Konitz•Lee Konitz Meets Jimmy Giuffre•Verve Records•1959','\
Lee Konitz•Live At The Half Note•Verve Records•1994','\
Various•Fantasy Presents Cool Jazz•Fantasy•2000'),'\
\
Pannonica\
':('\
Roswell Rudd•Roswell Rudd•America Records•1971','\
Quintet  René Urtreger•En Direct D\'Antibes•Carlyne Music•1980','\
Louis Hayes•Ichi-Ban•Timeless Records (3)•1976','\
Thelonious Monk•Les Liaisons Dangereuses 1960•Sam Records (8)•2017','\
Tommy Flanagan•Thelonica•Enja Records•1983','\
Joey Alexander•Joey.Monk.Live!•Motéma•2017','\
Clark Terry And His Orchestra•Clark Terry And His Orchestra•Jazz Heritage Society•2001','\
Horace Parlan Trio•Pannonica•Enja Records•1984','\
Thelonious Monk•Brilliant Corners•Riverside Records•1976','\
Steve Lacy•Only Monk•Soul Note•1987'),'\
\
Papa Lips\
':('\
Bob Mintzer Big Band•Papa Lips•CBS/Sony•1984','\
The Memphis Nighthawks•Jazz Lips•Delmark Records•1977','\
Bob Mintzer•Urban Contours•DMP•1989','\
Bourbon Street Jazzband (2)•I Must Have It•Elite Special•1985','\
Yank Lawson•Big Yank Is Here!•ABC-Paramount•0','\
Louis Armstrong & His Hot Five•Irish Black Bottom 1926•Joker (2)•1975','\
Louis Armstrong•V.S.O.P. (Very Special Old Phonography)  Vol. 2•Odeon•1961','\
Louis Armstrong•The Hot Fives & Hot Sevens Volume II•Columbia•1988','\
Louis Armstrong•The Louis Armstrong Legend 1926-27•World Records (6)•1981','\
Louis Armstrong•His Greatest Years - Volume 2•Odeon•1974','\
Louis Armstrong•V.S.O.P. Vol. 1/2•CBS•1974','\
Clarence Williams•Dreaming The Hours Away. Clarence Williams: The Columbia Recordings: Volume 1•Frog (7)•1997','\
Louis Armstrong•His Greatest Years 1925-1928•Odeon•1972'),'\
\
Partido Alto\
':('\
Airto Moreira•Amajour•Warner Bros. Records•1979','\
Airto Moreira•The Colours Of Life•In+Out Records•1988','\
Ignacio Berroa•Codes•Blue Note•2006','\
Azymuth•Live At The Copacabana Palace•SBA•1985','\
José Roberto Bertrami•Blue Wave•Milestone (4)•1983','\
Azymuth•Aurora•Far Out Recordings•2011','\
Robertinho Silva•Bodas De Prata•Discos CBS•1989','\
Azymuth•Jazz Carnival: The Best Of Azymuth•BGP Records•1988','\
Azymuth•Jazz Carnival•Brook•2006','\
Azymuth•Light As A Feather•Milestone (4)•1979','\
Various•Samba Do Brasil•Philips•1977'),'\
\
Part-time Lover\
':('\
Nanette Frank•Can\'t Be Your Part Time Lover•Total Control Records (4)•1986','\
Julie Kelly•Some Other Time•Chase Music Group•1989','\
The Stan Tracey Quartet•With Love From Jazz•Columbia•1968','\
Steve Williamson• Journey To Truth•Verve Records•1994','\
Ben Williams (5)•State Of Art•Universal•2011','\
The Lost Fingers•Lost In The 80\'s•Tandem.mu•2008','\
Paul Mauriat•Windy•Philips•1986','\
The Columbia Ballroom Orchestra•Let\'s Dance - Samba Jive & Pasodoble Collection•Denon•1986','\
Fausto Papetti•Magic Sax•CBS•1987','\
Light Of The World•Inner Voices•Arts Records•1999','\
PBUG•Stand Up•Jazzline•2016','\
Various•Seven Heven - Perfect Little Slices Of Soul Funk And Funky Jazz From The 21st Century - New Music From The Original Compact Disc-otheque•BBE•2011','\
The George Shearing Quintet•September In The Rain•MGM Records•1978','\
Fausto Papetti•Oggi•CBS•1985','\
Fausto Papetti•Grand Collection•Квадро-Диск•0'),'\
\
Passion Dance\
':('\
Six Brown Brothers (2)•Rigoletto Quartet / Passion Dance•Victor•1917','\
Chick Corea•Chick Corea (Featuring Lionel Hampton)•Chiaroscuro Records•1980','\
The Sun Ra Arkestra•Dance Of Innocent Passion•El Saturn Records•1981','\
Kenny Barron•Spiral•Eastwind•1984','\
Kenny Barron•Spirit Song•Verve Records•2000','\
Doug Carn•Infant Eyes•Black Jazz Records•1971','\
McCoy Tyner•The Real McCoy•Blue Note•1967','\
McCoy Tyner•Passion Dance•Milestone (4)•1979'),'\
\
Patterns\
':('\
Noah Howard•Patterns•Altsax•1973','\
Man Forever•Live At The Pilot Light•Stoned To Death•2014','\
Bobby Hutcherson•Patterns•Blue Note•1980','\
Gerald Wilson Orchestra•Moment Of Truth•Pacific Jazz•1962','\
Antonio Sanchez (2)•The Meridian Suite•C.A.M. Jazz•2015','\
The Gary McFarland Orchestra•The Gary McFarland Orchestra•Verve Records•1963','\
Ahmad Jamal Trio•The Awakening•Impulse!•1970','\
Steve Kuhn•The October Suite•Impulse!•1967'),'\
\
Peace\
':('\
The Two Of Us (3)•Looking Glass•Louton Records•1973','\
Walt Dickerson Trio•Peace•SteepleChase•1976','\
Frank Perry•Deep Peace•Quartz Publications•1981','\
Dave Burrell•Echo•BYG Records•1969','\
John Coltrane•Live In Japan•GRP•1991','\
Tordenskjolds Soldater (2)•Peace•Spectator Records•1970','\
Zara McFarlane•Peace Begins Within•Brownswood Recordings•2017','\
Terumasa Hino Quintet•Peace And Love•Canyon•1971','\
Bill Evans•How Deep Is The Ocean?•Heart Note Records•1988','\
Bobby Bryant•Swahili Strut•Cadet•1971','\
Palle Mikkelborg•Ashoka Suite / Guadiana / Concert (Dedicated To Torolf Mølgaard)•Metronome•1970','\
Randy Crawford•Give Peace A Chance•Warner Bros. Records•1982','\
Randy Crawford•no title•Warner Bros. Records•no year','\
Marky Mark & The Funky Bunch•Peace•Interscope Records•1992','\
Jean Carn•Peace•Black Jazz Records•1971','\
The Archie Shepp-Bill Dixon Quartet•The Archie Shepp-Bill Dixon Quartet•Savoy Records•1962','\
The Bill Evans Trio•Peace Piece•Riverside Records•0','\
All Stars After Hours•Night Jam Session In Warsaw 1973•Polskie Nagrania Muza•1973','\
Okay Temiz•Dervish Service•Ton Son Ton•1989','\
Norah Jones•Don\'t Know Why•Parlophone•2002','\
The Crusaders•Love And Peace •Pacific Jazz•1969'),'\
\
Peaches En Regalia\
':('\
Frank Zappa•Hot Rats•Bizarre Records•1969'),'\
\
Pearlie\'s Swine\
':('\
Monica Zetterlund•Chicken Feathers•SR Records•1972'),'\
\
Pee Wee\
':('\
Art Blakey Quintet•A Night At Birdland Volume One•Blue Note•2001','\
Kirk Lightsey Trio•Isotope•Criss Cross Jazz•1983','\
Miles Davis•Sorcerer•Columbia•1967','\
Pee Wee Hunt•Classics Ala Dixie•Capitol Records•1960','\
Pee Wee Hunt•The Classics Ala Dixie•Capitol Records•1958','\
Art Blakey & The Jazz Messengers•Meet You At The Jazz Corner Of The World•Blue Note•2002'),'\
\
Peep\
':('\
Joya Sherrill•Little Bo Peep / Desdemona\'s Lament•Columbia•1960','\
Barbara Dennerlein•Take Off!•Verve Records•1995','\
Barbara Dennerlein•Bebab•BEBAB Records•1987','\
Allan Holdsworth•Flat Tire (Music For A Non-Existing Movie)•Megazoidal Records•2001','\
Sonny Truitt•Drummer Delights. Jazz Band Music Minus One Drummer •Music Minus One•1961','\
Michael Brecker•Now You See It... (Now You Don\'t)•GRP•1990','\
Barbara Dennerlein•The Best Of Barbara Dennerlein•Verve Records•2006','\
Ill Treats•Classic Material •HHV.DE•2016','\
Joya Sherrill•Sugar & Spice•Columbia•1962','\
Pierre Bastien•Machinations•Rephlex•2012','\
Bing Crosby•Kraft Music Hall April 16 1942•Spokane Records (3)•0','\
A Small Good Thing•The Pink And Purple World Of Dishonesty•Soleilmoon Recordings•1997','\
Kermit Ruffins•The Barbecue Swingers Live•Basin Street Records•1998'),'\
\
Peggy\'s Blue Skylight\
':('\
no artist•no title•no label•no year','\
Joe Lovano•Rush Hour•Blue Note•1995'),'\
\
Pendulum\
':('\
Jean Robitaille•Pendulum•Paroles & Musique•1984','\
The David Liebman Quintet•Pendulum•Artists House•1979','\
Jan Garbarek Group•Wayfarer•ECM Records•1983','\
Richard Beirach•Elm•ECM Records•1979','\
Quest (13)•Quest II•Storyville•1986','\
Keizo Inoue•Intimate•Better Days (2)•1979','\
The New Oscar Pettiford Sextet•The New Oscar Pettiford Sextet•Debut Records•1953','\
Mike Taylor Quartet•Pendulum•Columbia•1966','\
Philip Catherine•The String Project - Live In Brussels•ACT (4)•2015','\
Zs•Buck•Folding Cassettes•2006','\
David Laborier•NE:X:T•WPR Jazz•2019'),'\
\
Pennies From Heaven\
':('\
The Pasadena Roof Orchestra•Pennies From Heaven / Back In Your Own Backyard•CBS•1978','\
The Big Three (3)•The Big Three•Hi-Life Records (2)•0','\
Ben Webster And His Orchestra•Pennies From Heaven / Tenderly•Norgran Records•1954','\
The Alice Hall Trio•Pennies From Heaven / Caravan•Capitol Records•1949','\
James Moody With Strings•Pennies From Heaven / Cherokee•Prestige•1952','\
Heinz Schönberger Quintett•Pennies From Heaven - Ohio Blues•Brunswick•1955','\
Louis Prima•Buona Sera / Pennies From Heaven•Capitol Records•0','\
Don Byas All Stars•Pennies From Heaven / Jamboree-Jump•Jamboree Records (2)•1945','\
no artist•Jammin\' In Hi Fi With Gene Ammons•Prestige•1957','\
Louis Armstrong And His All-Stars•Pennies From Heaven / Save It Pretty Mama•no label•0','\
Dave Brubeck•Jazz Gallery•Philips•1954','\
Art Pepper Quartet•Straight Ahead Jazz Vol. Two•Straight Ahead Jazz•0','\
Frank Sinatra•Pennies From Heaven / Please Be Kind•Reprise Records•1963','\
Count Basie Orchestra•Pennies From Heaven / Swinging At The Daisy Chain•Decca•1937','\
Gene Ammons And His Orchestra•Pennies From Heaven / The Last Mile•The Aristocrat Of Records•1950'),'\
\
Penny Arcade\
':('\
Al Hirt•Penny Arcade / If•RCA Victor•1969','\
Sammy Kaye•At A Sidewalk Penny Arcade / Spring Came•RCA Victor•1948','\
Joe Farrell•Penny Arcade•CTI Records•1974','\
Woody Herman And His Orchestra•20:30•Pronit•0','\
UZEB•Fast Emotion•Paroles & Musique•1982','\
Dave Matthews (3)•Big Band Recorded Live At The "Five Spot"•Muse Records•1975','\
Pram•Dark Island•Domino•2003','\
The Magic Organ•Penny Arcade•Ranwood•1972','\
Frank Hubbell (2)•The Night They Raided Minsky\'s And Other Show Stoppers•Philips•1969','\
Maurice Mulcahy Orchestra•The Sound Of Maurice Mulcahy•Release Records (2)•1970','\
Lalo Schifrin•Rollercoaster (Music From The Original Motion Picture Soundtrack)•MCA Records•1977','\
Lalo Schifrin•Rollercoaster (Music From The Original Motion Picture Soundtrack)•MCA Records•1977','\
Woody Herman & The New Thundering Herd•The 40th Anniversary Carnegie Hall Concert•RCA Victor•1977','\
The Magic Organ•22 Original Hits•GRT•1975','\
The Magic Organ•22 Great Organ Favorites•Ranwood•1978','\
Various•The Night They Raided Minsky\'s•United Artists Records•1968'),'\
\
Pensativa\
':('\
Freddie Hubbard•The Night Of The Cookers - Live At Club La Marchal Volume 1•Blue Note•1965','\
Freddie Hubbard•The Night Of The Cookers (Live At Club La Marchal)•Blue Note•1994','\
Freddie Hubbard•Hot Horn•Imagem•1984','\
Art Blakey & The Jazz Messengers•Free For All•Blue Note•1965','\
Freddie Hubbard•Fastball "Live" At The Left Bank•Label M•2001','\
Hubert Laws•Wild Flower•Atlantic•1972','\
The Bill Evans Trio•Crosscurrents•Fantasy•1978','\
Cedar Walton•Soul Cycle•Prestige•1970','\
The Essence All Stars•Hub Art - A Celebration Of The Music Of Freddie Hubbard•Hip Bop Essence•1995'),'\
\
Pent Up House\
':('\
Ted Curson•Fireball•Trio Records•1979','\
The Super Jazz Trio•The Super Jazz Trio•Jazz Line•1982','\
Jamey Aebersold•Sonny Rollins Nine Classic Jazz Originals•JA Records•1976','\
Bobby Jaspar Quartet•The Bobby Jaspar Quartet At Ronnie Scott\'s 1962•Mole Jazz•1986','\
Morten Halle•Blow!•Odin•1990','\
Pepper Adams•Urban Dreams•Palo Alto Jazz•1981','\
Chet Baker•Sextet & Quartet•Music•1960','\
Chet Baker•Sextet & Quartet•Music•1960','\
Sonny Rollins•Plus 4•Prestige•1956','\
Christoph Spendel Trio•Back To Basics•Blue Flame•1987','\
Claudio Roditi•Milestones•Candid•1992','\
Hank Jones Trio•Hank Jones Trio With Mads Vinding & Al Foster•Storyville•1991'),'\
\
People Make The World Go Round\
':('\
Johnny Lytle•People & Love•Milestone (4)•1973','\
Bobby Hutcherson•Linger Lane•Blue Note•1975','\
Milt Jackson•Sunflower•CTI Records•1973','\
CTI All-Stars•CTI Summer Jazz At The Hollywood Bowl Live Two•CTI Records•1977','\
Ramon Morris•Sweet Sister Funk•Groove Merchant•1973','\
Freddie Hubbard•Polar AC•CTI Records•1975','\
Herb Alpert•Main Event Live•A&M Records•1978','\
Marcus Miller•Live & More•Dreyfus Jazz•1997'),'\
\
People Will Say We\'re In Love\
':('\
Lou Donaldson•Cole Slaw•Argo (6)•1965','\
Donald Lambert•Giant Stride - Donald Lambert At The Piano•Solo Art Records•1962','\
Stacey Kent•The Boy Next Door•Candid•2003','\
Carmen Cavallaro•The King And I And Other Richard Rodgers An Oscar Hammerstein II Songs•Decca•0','\
Lester Lanin And His Orchestra•For Dancing: 23 Richard Rodgers Hits •Epic•1967','\
Bill Evans•The Complete Fantasy Recordings•Fantasy•1989','\
David Bowie•MP3 Collection•Digital Records (6)•2016','\
Various•Sony Music 100 Years: Soundtrack For A Century•Sony Music•1999'),'\
\
Perdido\
':('\
Jazz At The Philharmonic•Norman Granz\' Jazz At The Philharmonic Vol. 8•Mercury•1953','\
Jazz At The Philharmonic•Norman Granz\' Jazz At The Philharmonic Volume Eight•Mercury•1947','\
Jazz At The Philharmonic•Perdido•Karusell•1953','\
Jazz At The Cavalcade•Perdido•Cavalcade (3)•1954','\
Stuff Smith Trio•Perdido•Selmer•0','\
Jazz At The Philharmonic•Perdido•VSP•1966','\
The Charles Mingus Quintet•Mingus Quintet Meets Cat Anderson•Unique Jazz•0','\
Duke Ellington And His Orchestra•Perdido / Raincheck•Victor•1942','\
The Dave Brubeck Quartet•Perdido / Stardust•Fantasy•1953','\
Woody Herman And His Third Herd•Perdido / Baby Clementine•London Records•1953','\
Tony Crombie And His Orchestra•All Of Me / Perdido•London Records•1954'),'\
\
Perdido Line\
':('\
The Stargazers (2)•Watch This Space•Epic•1982','\
Various•The Rare Tunes Collection "From Latin... To Jazz Dance" - Vol. 2•Rare Groove Recordings•2003','\
Various•Jazz Lounge ²•Ayia Napa•2001','\
no artist•Echoes Of Ellington•Black Lion Records•1978','\
Dave Brubeck•Eight Classic Albums•Real Gone•0','\
Dinah Washington•The Complete Dinah Washington On Mercury Vol.5 1956-1958•Mercury•1989','\
Various•Atlantic Jazz•Atlantic•1986','\
Various•The Complete Vinyl Collection•Bellevue Publishing Uk Ltd•2016'),'\
\
Petite Fleur\
':('\
Bob Crosby And The Bob Cats•Petite Fleur / South•Dot Records•1965','\
Paul Schröder•Petite Fleur / Blumen-Mädi•AMIGA•1967','\
Sidney Bechet•Petite Fleur / Stormy Weather•Disques Vogue•0','\
Michel Attenoux Et Son Orchestre•Les Succès Du Mois•Panorama (4)•1958'),'\
\
Petits Machins\
':('\
Johnny Coles•Katumbo (Dance)•Mainstream Records•1972','\
Miles Davis•Filles De Kilimanjaro•Columbia•1969','\
Serge Gainsbourg•Gainsbourg Percussions•Philips•1964'),'\
\
Pfrancing (No Blues)\
':('\
Joe Henderson•So Near So Far (Musings For Miles)•Verve Records•1993','\
Kyle Eastwood•Time Pieces•Jazz Village•2015','\
Miles Davis•The Box Set Series•Sony Music•2014','\
Miles Davis•The Original Mono Recordings•Columbia•2013'),'\
\
Phase Dance\
':('\
Pat Metheny Group•Pat Metheny Group•ECM Records•1978','\
Pat Metheny Group•Clouds•Paradise (12)•1991','\
Pat Metheny•Selected Recordings•ECM Records•0'),'\
\
Piano In The Dark\
':('\
Alex Bugnon•Piano In The Dark•Orpheus Records•1988','\
Alex Bugnon•Going Out•Orpheus Records•1989','\
Alex Bugnon•Love Season•Orpheus Records•1988','\
Ben Sidran•Old Songs For The New Depression•Antilles•1982','\
Freddy Martin And His Orchestra•Freddy Martin At The Cocoanut Grove•RCA•1957','\
George Howard•Personal•MCA Records•1990','\
Ramsey Lewis•Meant To Be•Narada Jazz•2002','\
Le Valedon•Sensuous Sax The Night•Compose•1995','\
Brenda Russell (2)•In Concert•BMG•2001','\
The John Tesh Project•Sax On The Beach•GTS Records•1995','\
Various•Colors Of Jazz: From Dusk Till Dawn•Sony Masterworks•1991','\
Shirley Scott Trio•For Members Only / Great Scott!!•Impulse!•1989','\
Bunny Berigan•Jazz Me Blues•Past Perfect Silver Line•2000','\
Kenny Werner•The Piano Music Of Bix Beiderbecke - Duke Ellington - George Gershwin - James P. Johnson•Finnadar Records•1978','\
Various•Soft & Romantic•PolyTel•1988','\
Richard M. Jones•Volume 1 1923-1927•Rst Records•1995'),'\
\
Pick Up The Pieces\
':('\
Buddy Rich Big Band•A Tribute To The Music Of Buddy Rich•Atlantic•1994','\
Ekseption•Mindmirror•Philips•1975','\
The Atlantic Family•Live At Montreux•Atlantic•1978','\
Ponga•Ponga•Loosegroove Records•1999','\
Tom Scott•Them Changes•GRP•1990','\
The Saturday Night Live Band•Jupiter•Electric Bird•1987','\
Henry Mancini And His Orchestra•Symphonic Soul•RCA Victor•1975','\
Herbie Mann•Herbie Mania•Atlantic•1976','\
Willis Jackson•The Way We Were•Atlantic•1975','\
Various•Jazz Around The Funk Part 1•Follow Me Records•2000','\
The New Orleans Nightcrawlers•Funknicity•Rounder Records•1997','\
Candy Dulfer•The Best Of Candy Dulfer•N2K Encoded Music•1998'),'\
\
Pick Yourself Up\
':('\
The Favourite Soloists 1951•Summertime / Pick Yourself Up•Cupol•1951','\
Benny Carter Quintet•Street Scene / Pick Yourself Up•Mercury•1952','\
The George Shearing Quintet•Roses Of Picardy•MGM Records•1950','\
The George Shearing Quintet•Little White Lies / Pick Yourself Up•MGM Records•0','\
Benny Goodman And His Orchestra•Pick Yourself Up / Down South Camp Meeting•Victor•1936','\
Ted Heath And His Music•Ted Heath At The London Palladium Vol. 2•London Records•0','\
Fred Astaire•The Way You Look To-night / Pick Yourself Up•Brunswick•1936','\
no artist•Pick Yourself Up With Anita O\'Day •Artone•1959','\
Larry Nozero•Kaleidoscopin\'•Dominic Records•1988','\
Buddy DeFranco•Buddy De Franco And The Oscar Peterson Quartet•Verve Records•1958','\
Tito Puente & His Latin Ensemble•Mambo Diablo•Concord Jazz Picante•1985','\
Paul Smith (5)•Heavy Jazz•Outstanding Records (2)•1977','\
Herbie Harper Quintet•Herbie Harper Quintet•Tampa Records•1955','\
Five Brothers•Five Brothers•Tampa Records•1956','\
Jazz Renaissance Quintet•Movin\' Easy•Mercury•1961','\
Louis Stewart•Super Session•Livia Records•1986'),'\
\
Pinocchio\
':('\
Miles Davis•Nefertiti•Columbia•1968','\
Mikio Masuda•Trace•East Wind•1974','\
Clifford Jordan And The Magic Triangle•On Stage Vol. 1•Steeplechase•1977','\
Sapporo•Sapporo Featuring Ryo Kawasaki•America Sound•0','\
Jack Wilkins•Windows•Mainstream Records•1973','\
Jonas Burgwinkel•Source Direct•Traumton Records•2011'),'\
\
Pithycanthropus Erectus\
':('\
Charles Mingus•Pithycanthropus Erectus•America Records•1971','\
Charles Mingus•Pithecanthropus Erectus•Atlantic•1960'),'\
\
Plain Jane\
':('\
Sonny Rollins•Sonny Rollins Volume 1•Blue Note•1957','\
Sonny Rollins•Jazz Profile: Sonny Rollins•Blue Note•1998','\
Bobby Darin•The Bobby Darin Story•ATCO Records•1961','\
Sonny Rollins•Sonny Rollins•Blue Note•1975','\
Ambrose & His Orchestra•Champagne Cocktail•Ace Of Clubs•1968','\
Catch Up•Birth Of The Second Life•Calig•1976'),'\
\
Played Twice\
':('\
Steve Lacy•The Straight Horn Of Steve Lacy•Candid•1960','\
Thelonious Monk•Brilliance•Milestone (4)•1975','\
Anthony Braxton•Six Monk\'s Compositions (1987)•Black Saint•1988','\
The Thelonious Monk Quintet•5 By Monk By 5•Riverside Records•1959','\
Sphere (16)•Flight Path•Elektra Musician•1983','\
Gary Bartz•Reflections On Monk - The Final Fronteer•SteepleChase•1989','\
Peter Leitch•Exhilaration  •Uptown Records (2)•1985','\
Thelonious Monk•Big Band And Quartet In Concert•Columbia•1964'),'\
\
Plaza Real\
':('\
Weather Report•Procession•Columbia•1983','\
Weather Report•Weather Report•CBS•1991','\
Chris Cramer•Memories Of A Spanish City•Caracalla Media•2001','\
Wayne Shorter Quartet•Without A Net•Blue Note•2013','\
Marcin Wasilewski•Trio•ECM Records•2005','\
Paco De Lucía•The Spanish Guitar•Philips•1976','\
Weather Report•Live In Cologne 1983•Art Of Groove•2011','\
Weather Report•Live & Unreleased•Columbia•2002','\
Paco De Lucía•Paco De Lucía•Philips•0','\
Weather Report•Forecast: Tomorrow•Legacy•2006','\
People (12)•People•I And Ear•2005'),'\
\
Please Don\'t Talk About Me When I\'m Gone\
':('\
Cybill Shepherd•Mad About The Boy•Inner City Records•1980','\
Billie Holiday•A Day In The Life Of Billie Holiday•Differant Drummer Records•2007','\
The Art Van Damme Quintet•The Gentle Art Of Art•SABA•1967','\
Don Byas•"Ambiances Et Slows"•Barclay•1975','\
Georgie Fame•The Whole World’s Shaking (Complete Recordings 1963-1966)•Polydor•2015','\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014'),'\
\
Polka Dots and Moonbeams\
':('\
Tommy Dorsey And His Orchestra•Polka Dots and Moonbeams / Liebestraum•RCA Victor•0','\
Gerry Mulligan•California Concerts•Pacific Jazz•1955','\
Lorez Alexandria•Polka Dots And Moonbeams•Federal (5)•1957','\
Sarah Vaughan•Shulie A Bop / Polka Dots And Moonbeams•Emarcy•1954','\
Lester Young Quartet•Polka Dots And Moonbeams / Up \'N Adam•Mercury•1952','\
Chet Baker•The Improviser•Cadence Jazz Records•1984','\
Frank Sinatra•There Are Such Things•Reprise Records•1961','\
Chet Baker Trio•Live From The Moonlight•Philology•1988','\
Elmo Hope Sextet•Informal Jazz•Prestige•1956','\
Isao Suzuki•Now\'s The Time•Three Blind Mice•1974','\
Tatsuya Takahashi 3•Impression•Audio Lab. Record•1980','\
Frank Sinatra•There Are Such Things•Reprise Records•1961','\
"Philly" Joe Jones•Philly Mignon•Galaxy•1978','\
Sarah Vaughan•Vol 1•Metronome•1954','\
Chivo Borraro•El Nuevo Sonido Del "Chivo Borraro"•Microfon•1966','\
Sarah Vaughan•Images•Emarcy•1954','\
Lester Young Quartet•Too Marvelous For Words•Clef Records•0'),'\
\
Portrait of Jennie\
':('\
Nat King Cole•Portrait Of Jennie / Jet•Capitol Records•1972','\
Jack Fina And His Orchestra•Portrait Of Jennie / Josephine•MGM Records•1949','\
Freddy Martin And His Orchestra•Portrait Of Jennie / If You Could Care•RCA Victor•1949','\
Various•Lusty Moods (Played By America\'s Greatest Jazzmen)•Moodsville•1963','\
Donald Byrd•At The Half Note Cafe (Volume 1)•Blue Note•1961','\
Nat King Cole•Unforgettable Part 1•Capitol Records•1954','\
Staffan William-Olsson Sextet•Oak Road Boogaloo•Real Records (3)•2000','\
Wes Montgomery•Willow Weep For Me•Verve Records•1969','\
Ron Carter•Panamanhattan•Dreyfus Jazz•1991','\
Johnny Hammond•Talk That Talk•New Jazz•1960'),'\
\
Portrait of Tracy\
':('\
Weather Report•Live At Montreux 1976•Eagle Eye Media•2007','\
Charged Particles•Charged Particles•no label•1994','\
Bass Extremes•Just Add Water•Tone Center•2001','\
Brian Bromberg•Jaco•A440 Music Group•2002','\
Jaco Pastorius•Jaco Pastorius•Epic•1976','\
Kadhja Bonet•The Visitor EP •Headcount Records•2016','\
Sashird Lao•Watsdis•E-motive records•2007'),'\
\
Portsmouth Figurations\
':('\
Bob Moses Quintet•Family•Sutra Records•1980','\
Gary Burton Quartet•Live In Tokyo•Atlantic•2013','\
Gary Burton Quartet•Live In Tokyo•Atlantic•1971','\
Gary Burton Quartet•Green Apple•Moon Records (4)•1989','\
Gary Burton Quartet•Duster•RCA Victor•1967'),'\
\
Power Play\
':('\
Eddie Gomez•Power Play•Columbia•1988','\
Jan Kaspersen Quintet•Bizarre Ballet•Storyville•1983','\
Wayman Tisdale•The Very Best Of•Verve Records (2)•2007','\
Buddy Rich And The Big Band Machine•Speak No Evil•RCA Victor•1976','\
Prince•Crystal Ball•Three Cool Cats•1991','\
no artist•We\'re All The Same•SDT Recordings Dept. - A Division Of SDT Freedom Lovers Inc.•2016','\
Maurice Pop•Power Pop•Motor Music•1998','\
Thomas Dolby•12x12 Original Remixes•EMI•1999','\
Alan Hawkshaw•Non Stop Hammond Hits•Polydor•1974','\
Various•Music For The Movies Of Clint Eastwood•Warner Sunset Records•2001'),'\
\
Preacher\
':('\
Horace Silver•The Preacher•Blue Note•1955','\
The Cannonball Adderley Quintet•Hummin\' / Country Preacher•Capitol Records•1969','\
Jimmy Smith•The Preacher / Hobo Flats•Verve Records•1963','\
Arthur Collins•The Preacher And The Bear•Victor•0','\
Jimmy Smith•Plays "Walk On The Wild Side" And "The Preacher"•Verve Records•1963','\
Eddie Jefferson•Come Along With Me•Prestige•1969','\
Eddie Smith (4)•The Preacher And The Bear / Snow Deer•King Records (3)•1952','\
Rosko•Rosko - The Preacher•Langdon•1963','\
Gene Ammons•Son Of A Preacher Man•Prestige•1970','\
Arthur Collins•The Preacher And The Bear / Bake Dat Chicken Pie•Victor•1916','\
Pee Wee Hunt And His Orchestra•I Got Rhythm / The Preacher And The Bear•Mirror (8)•1946','\
The Horace Silver Quintet•Horace Silver Quintet Vol. 4•Blue Note•1955','\
The Golden Gate Quartet•Jonah In The Whale / Preacher And The Bear•Victor•0','\
Jimmy Smith•At Club "Baby Grand" Wilmington Delaware Volume 1•Blue Note•1956','\
Kenny Burrell•The Preacher / Burning Spear•Verve Records•1968','\
Shirley Scott•Plays Horace Silver•Prestige•1962','\
Les McCann•Que Rico (The Swinging Preacher) / It Had Better Be Tonight•World Pacific Records•1964','\
Arthur Collins•The Preacher And The Bear / Is Your Mother In Molly Malone?•Columbia•1906','\
Prince George•The Swinging Preacher / 5/4 Time •Epic•1963','\
Bing Crosby•Bing & Satchmo•MGM Records•1960'),'\
\
Prelude To A Kiss\
':('\
Duke Ellington And His Orchestra•Prelude To A Kiss / Cotton Tail•RCA•0','\
Stan Getz Quartet•Prelude To A Kiss / Night And Day•Metronome•1951','\
Johnny Hodges And His Orchestra•Prelude To A Kiss / The Jeep Is Jumpin\'•Vocalion (2)•1938','\
Duke Ellington•The Duke Plays Ellington Part 2•Capitol Records•1955','\
Sadayasu Fujii•Prelude To A Kiss•Nadja•1976','\
Les Brown And His Orchestra•Prelude To A Kiss / On My Way Out•V Disc•1944','\
Oscar Peterson•Oscar Peterson Plays Duke Ellington•Mercury•1953','\
Marion Brown•Passion Flower•Baystate•1978','\
Billy Butler (3)•Night Life•Prestige•1971','\
Ahmad Jamal•Steppin Out With A Dream•20th Century Records•1976','\
Michel Petrucciani•Note \'n Notes•Owl Records (4)•1984','\
The Horace Silver Trio•New Faces - New Sounds•Blue Note•1952','\
McCoy Tyner•Counterpoints - Live In Tokyo•Milestone (4)•0','\
Ronnie Mathews•Doin\' The Thang!•Prestige•1964','\
Kenny Burrell•The Best Of Kenny Burrell•Prestige•1966','\
Bobby Timmons•Live At The Connecticut Jazz Party•Chiaroscuro Records•1981','\
The Horace Silver Trio•Horace Silver Trio•Vogue•0'),'\
\
Prince of Darkness\
':('\
Miles Davis•Sorcerer•Columbia•1967','\
Eddie Henderson•So What•no label•2002','\
Erik Escobar•New Samba Jazz•Altrisuoni•2006'),'\
\
Promenade\
':('\
Herb Alpert•Promenade•A&M Records•1976','\
Freddie Brocksieper Quintett•Caravan / Cymbal Promenade •Brunswick•0','\
Altaïs•Altaïs•Not On Label (Altaïs Self-released)•1986','\
Jack Mimram•jack mimram plays•Firework (2)•1978','\
Miles Davis•At Last!•Contemporary Records•1985','\
The Art Ensemble Of Chicago•Urban Bushmen•ECM Records•1982','\
Brian Hughes•Under One Sky•Justin Time Records•1992','\
Nelly Pouget•Le Dire•Minuit Regards•1991'),'\
\
Promise\
':('\
The Cinematic Orchestra•A Promise•Ninja Tune•2019','\
Vaughn Monroe And His Orchestra•Oh Promise Me / Because•RCA Victor•1948','\
Sammy Kaye•Kaye\'s Melody•RCA Victor•1949','\
John Coltrane•Africa & India•Jazz Masterworks•1985','\
Liberace•Oh Promise Me•Philips•0','\
The Quartet (4)•The Quartet•Poljazz•1979','\
Tommy Dorsey And His Orchestra•Oh Promise Me / Shine On Harvest Moon•no label•1938','\
The Quartet (4)•Loaded•Leo Records (2)•1980','\
McCoy Tyner•Echoes Of A Friend•Victor•1972','\
Thurston Moore•The Promise•Materiali Sonori•1999','\
SwerveMobile•We Promise•New Squad Records•2015','\
SwerveMobile•We Promise•New Squad Records•2015','\
Louis Jordan And His Tympany Five•You Broke Your Promise / Safe Sane and Single•Decca•1949','\
Ralph Simon•As•Sound Hills Records•1994','\
no artist•Primal Roots•A&M Records•1972','\
Muriel Grossmann•Golden Rule•RR GEMS•2018'),'\
\
Punjab\
':('\
Joe Henderson•Punjab•ARCO•1990','\
Joe Henderson•In \'N Out•Blue Note•1964','\
Pepper Adams•Encounter•Prestige•1969','\
The Indian Core•The Indian Core•Grappa•2007','\
Benny Green•These Are Soulful Days •Blue Note•1999','\
Ralph Moore (2)•Images•Landmark Records (3)•1988','\
Renee Rosnes•Renee Rosnes•Blue Note•1990','\
Ryan Kisor•On The One•Columbia•1993','\
Lourenço Rebetez•O Corpo de Dentro•Suburbia Records•2017','\
Bobby Watson & Horizon•Post-Motown Bop•Blue Note•1991'),'\
\
Pursuance\
':('\
The Mattson 2•Play "A Love Supreme"•Spiritual Pajamas•2018','\
Kenny Garrett•Pursuance: The Music Of John Coltrane•Warner Bros. Records•1996','\
Frank Catalano•Love Supreme Collective•Ropeadope Records•2014','\
Dominic Duval•Music Of John Coltrane•NoBusiness Records•2010','\
Katharina Maschmeyer Quartet•A Love Supreme/Universal Tone•Neuklang•2016','\
Branford Marsalis Quartet•Footsteps Of Our Fathers•Rounder Records•2002','\
Elvin Jones Quartet•Tribute To John Coltrane "A Love Supreme"•Sony Records•1994','\
John Coltrane•A Love Supreme•Impulse!•1965'),'\
\
Pussy Cat Dues\
':('\
Kevin Mahogany•Pussy Cat Dues "The Music Of Charles Mingus"•Enja Records•2000'),'\
\
Put It Where You Want It\
':('\
The Crusaders•Put It Where You Want It•Blue Thumb Records•1972','\
Larry Carlton•Deep Into It•Warner Bros. Records•2001','\
Sharon Redd•Ain\'t No Man Worth It•Columbia•1978','\
The Crusaders•Soul Shadows•MCA Records•1980','\
George Shaw•Skywalkers•TBA Records & Tapes•1986','\
The Crusaders•Ongaku Kai Live In Japan•Crusaders Records•1981','\
Paul Brown•One Way Back•Woodward Avenue Records(2)•2016','\
Jiro Inagaki & Soul Media•Funk Party•Columbia•1975','\
Average White Band•Show Your Hand•MCA Records•1973','\
Wolfgang Schmid•Wolfgang Schmid\'s Jubilee Concert "Live"•Global Satellite•1989','\
Everette Harp•For The Love•Blue Note•2000','\
Various•Jazz Panorama III•Балкантон•1976','\
The Crusaders•Live In Japan 2003•P.R.A. Records•2004','\
The Crusaders•The Crusaders\' Finest Hour•Verve Records•2000'),'\
\
Put On A Happy Face\
':('\
Tony Bennett•Put On A Happy Face•Columbia•1962','\
Jay Hoggard•Overview•Muse Records•1989','\
Oscar Peterson•Put On A Happy Face•Verve Records•1966','\
Norman Vaughan•Swinging In The Rain (Singin\' In The Rain)•Pye Records•0','\
J.J. Johnson•J.J.\'s Broadway•Verve Records•1963','\
Oscar Peterson•A Portrait Of Oscar Peterson•Polydor•1966','\
Stevie Wonder•With A Song In My Heart•Tamla•1963','\
Steve Wilson Quintet•New York Summit•Criss Cross Jazz•1992','\
Brother Jack McDuff•Prelude•Prestige•1964','\
Vikki Carr•Anatomy Of Love•Liberty•1965','\
Brother Jack McDuff•The Heatin\' System•Concord Jazz•1995','\
Dave Catney•First Flight•Justice Records (2)•1990','\
Tal Farlow•A Sign Of The Times•Concord Jazz•1977','\
Dick Williams (4)•Two Sides Of Love•Capitol Records•1961','\
Bill Potts And His Orchestra•Bye Bye Birdie•Colpix Records•1963'),'\
\
Pyramid\
':('\
Buddy DeFranco And His Orchestra•Gold Nugget Sam / Pyramid•Clef Records•1954','\
Johnny Hodges And His Orchestra•Pyramid / Empty Ballroom Blues•Parlophone•0','\
John Graas Septet•French Horn Jazz Volume 1•London Records•0','\
The Modern Jazz Quartet•The Best Of•Atlantic•1970','\
Erland Dahlen•Rolling Bomber•Hubro•2012','\
Duke Ellington And His Orchestra•Pyramid / When My Sugar Walks Down The Street•Brunswick•1938','\
White Blacula•Pyramid Twist•Not On Label (White Blacula Self-released)•2013','\
Charles Lloyd•Waves•A&M Records•0'),'\
\
Question Mark\
':('\
Ray Anderson•You Be•Minor Music•1986','\
Ray Anderson•You Be•Minor Music•1986','\
Juan Garcia Esquivel•Mucha Muchacha•Bar/None Records•1996','\
Emmanuel Cremer•Sonora Manuchello Septet•Alambik Musik•2015','\
Janusz Muniak Quintet•Question Mark•Polskie Nagrania Muza•1978','\
Milt Buckner•Rockin\' Again•Black And Blue•0','\
Roland Batik Trio•Roots•Gramola•1992','\
Esquivel And His Orchestra•Actual•RCA Victor•1966','\
Juan Garcia Esquivel•Music From A Sparkling Planet•Bar/None Records•1994','\
Juan Garcia Esquivel•Cabaret Mañana•RCA•1995','\
Brook Benton•Ain\'t It Good•Trip•0','\
Elvis Presley•20 Original Albums•RCA•2012'),'\
\
Quicksilver\
':('\
Art Blakey•Quicksilver•Blue Note•1956','\
Art Blakey Quintet•A Night At Birdland Volume 1•Blue Note•1954','\
The Horace Silver Trio•New Faces - New Sounds•Blue Note•1952','\
Jamey Aebersold•For You To Play... Horace Silver Eight Jazz Classics•JA Records•1978','\
Nick Brignola Quintet•L.A. Bound•Sea Breeze•1979','\
Art Blakey Quintet•A Night At Birdland Volume 1•Blue Note•1956','\
Fourplay (3)•Silver•Heads Up International•2015','\
Art Blakey Quintet•A Night At Birdland Volume 2•Blue Note•1982','\
no artist•Double Or Nothin\'•Liberty•1957','\
The Horace Silver Trio•Horace Silver Trio•Vogue•0','\
Art Blakey Quintet•A Night At Birdland Volume 2•Blue Note•1966','\
Art Blakey Quintet•A Night At Birdland Volume 2•Blue Note•1956'),'\
\
Quiet Girl\
':('\
Phil Upchurch•Feeling Blue•Milestone (4)•1968','\
Paul Smith (5)•Brazilian Detour•Warner Bros. Records•1966','\
Art Of Movement Studio•Listen And Move (Percussion And Music)•MacDonald & Evans (Educational Recordings) Ltd.•0','\
Kenny G (2)•Brazilian Nights•Concord Records•2014','\
Quartet Sensitive•Afternoon With Jobim•Dallas Records•2001','\
Billy Childs•Take For Example This•Windham Hill Jazz•1988','\
Frank Sinatra•Francis Albert Sinatra & Antonio Carlos Jobim•Reprise Records•1967'),'\
\
Quiet Now\
':('\
Teus Nobel•Legacy•no label•2015','\
Bill Evans•The Romantic Jazzman•Editions Atlas•1991','\
The Bill Evans Trio•Quiet Now•Affinity•1981','\
Jack DeJohnette•The Jack DeJohnette Piano Album•Landmark Records (3)•1985','\
The Bill Evans Trio•Quiet Now•Affinity•1986','\
Bob James Trio•Straight Up•Warner Bros. Records•1996','\
Bill Evans•Jazz \'Round Midnight•Verve Records•1993','\
Denny Zeitlin•Homecoming•Living Music•1986','\
Bill Evans•Further Conversations With Myself•Verve Records•1967','\
Bill Evans•From The 70\'s•Fantasy•1983','\
Bill Evans•Live In Paris 1972 Vol. 2•no label•1988','\
The Bill Evans Trio•Live In Europe Vol. II•EPM Musique•1989','\
Helge Lien Trio•Spiral Circle•DIW•2002'),'\
\
Quintessence\
':('\
The George Shearing Quintet•I\'ll Be Around / Quintessence•MGM Records•1951','\
Quincy Jones•The Quintessence / For Lena And Lennie•Impulse!•1962','\
Coleman Hawkins•Supreme•Enja Records•1995','\
Warne Marsh•Jazz Of Two Cities•Imperial•1957','\
Billy Larkin And The Delegates•Blue Lights•Aura Records (4)•1965','\
Quincy Jones And His Orchestra•The Quintessence•Impulse!•1962'),'\
\
Rain Waltz\
':('\
Triosence•One Summer Night•Mons Records•2013','\
Vince Guaraldi•Oh Good Grief!•Warner Bros. - Seven Arts Records•1968','\
Bobby Christian•Vibe-brations•Ovation Records•1970','\
Gary Burton•Gary Burton•International Polydor Production•0','\
no artist•Why Not!•Columbia•1984','\
Larry Bunker Quartette•Live At Shelly\'s Manne-Hole•Vault•1966','\
Stan Getz•The Chick Corea / Bill Evans Sessions•Verve Records•1976','\
John Abercrombie•Tactics•ECM Records•1997','\
Various•Windham Hill Records Sampler \'82•Windham Hill Records•0','\
The Fred Hersch Trio•Heartsongs•Sunnyside•1990'),'\
\
Rainland\
':('\
Paul McCandless•Premonition•Windham Hill Records•1992','\
Mokave•Volume 1•AudioQuest Music•1991','\
Various•Köln Sampler 91•Electrola•1991','\
Various•The Great Stupa•Sound & Silence•2001'),'\
\
Ramblin\'\
':('\
no artist•Jazz-Liisa 3•Svart Records•2016','\
Ray Garnett•Patches / Ramblin\' Rose•RCA•0','\
Frankie Laine•Answer Me / Ramblin\' Man•Philips•1953','\
Radiojazzgruppen•Rainbow Sketches•CAM•1974','\
Woody Herman•What Kind Of Fool Am I? / Ramblin\' Rose•Philips•0','\
The Joe Daley Trio•At Newport \'63•RCA Victor•1963','\
Frankie Laine•I Let Her Go / Ramblin\' Man•Columbia•1953','\
Ornette Coleman•The Best Of Ornette Coleman•Atlantic•1970','\
Laurindo Almeida & The Bossa Nova Allstars•Lazy River Bossa Nova•Capitol Records•1962','\
Jukka Tolonen•Tolonen!•Love Records (4)•1971'),'\
\
Rapture\
':('\
Sam Rivers•Paragon•Fluid Records (4)•1977','\
Count Basie Orchestra•Jumpin\' At The Woodside•Decca•1939','\
Sam Rivers Quartet•"Crosscurrent" - Live At Jazz Unité•Blue Marge•1982','\
Stan Kenton And His Orchestra•Concerto For Doghouse (A Setting In Motion) / Reed Rapture•Decca•1947','\
The Harold Land / Blue Mitchell Quintet•Mapenzi•Concord Jazz•1977','\
Sadao Watanabe•Autumn Blow•Flying Disk•1977','\
Tom Harrell•Stories•Contemporary Records•1988','\
Tom Harrell Quintet•Moon Alley•Criss Cross Jazz•1986','\
Anita Baker•Talk To Me•Elektra•1990','\
Latin All Stars (2)•Jazz Heat Bongo Beat•Crown Records (2)•1960','\
Sal Rachele•Infinite Peace•Living Awareness Productions•1987','\
Steve Tavaglione•Blue Tav•Sohbi•1990','\
"Philly" Joe Jones•Philly Joe\'s Beat•Atlantic•1960','\
James Gurley•It\'s Big Huge•Qbico•2010'),'\
\
Raven\
':('\
David Grubbs•Thirty Minute Raven•Rectangle•2001','\
Woody Herman•Fat Mama / The Raven Speaks•Fantasy•1973','\
Richard Davis (2)•Cauldron•Corvo Records (2)•1979','\
Oregon•Violin•Vanguard•1978','\
Albert Mangelsdorff•Moon At Noon•Musikant•1987','\
Jackie Orszaczky•Beramiada•Real Records (11)•1975','\
String Connection•Workoholic•PolJazz•1982','\
Gary Burton•Gary Burton & Keith Jarrett•Atlantic•1971','\
The Wow•Come Here•Hermit Records•2003','\
Various•Protos Orofos - 3•Protos Orofos•2011','\
GoGo Penguin•A Humdrum Star•Blue Note•2018'),'\
\
Re : Person I Knew\
':('\
Bill Evans•The Paris Concert (Edition Two)•Elektra Musician•1984','\
Bill Evans•Peace Pieces•Riverside Records•1969','\
Coe Oxley & Co.•Nutty On Willisau•hat ART•1984','\
Bill Evans•Re: Person I Knew•Fantasy•1981','\
Bill Evans•The Bill Evans Album•Columbia•1971'),'\
\
Reach Out I\'ll Be There\
':('\
Kevin Mahogany•Pride & Joy•Telarc•2002'),'\
\
Real Guitarist\
':('\
Steve Kuhn•Steve Kuhn Live In New York•Cobblestone•1972','\
Irene Sjögren Quintet•Sweet Surprise•Dragon (8)•1986','\
Monica Zetterlund•Chicken Feathers•SR Records•1972'),'\
\
Real Life\
':('\
Brenda Russell (2)•This Is Real Life•Arcana Sound•2009','\
Roy Ayers•Let\'s Do It•Polydor•1978','\
Ray Obiedo•Sticks & Stones•Windham Hill Jazz•1993','\
Antonio Sanchez (2)•New Life•C.A.M. Jazz•2013','\
Paolo Radoni•Vento•KBL•1978','\
Gary Burton Quartet•Real Life Hits•ECM Records•1985','\
Terri Lyne Carrington•Real Life Story•Verve Forecast•1989','\
Robbie Dupree•David Dupree With David Sancious•Not On Label•2003','\
Carla Bley•Songs With Legs•WATT Works•1996','\
André Ceccarelli•Ceccarelli•Carla•1977','\
Antonio Sanchez (2)•Channels Of Energy•C.A.M. Jazz•2018','\
Isotope 217•Utonian_Automatic•Thrill Jockey•1999','\
Carla Bley•Live!•WATT Works•1982','\
Bernie Worrell•Funk Of Ages•Gramavision•1990','\
no artist•Sergio Mendes And The New Brasil \'77•Elektra•1977','\
no artist•Sergio Mendes And The New Brasil \'77•Elektra•1977'),'\
\
Real Love\
':('\
Al Jarreau•Closer To Your Love•Warner Bros. Records•1981','\
The Oscar Peterson Trio•Until The Real Thing Comes Along/Love For Sale•Mercury•0','\
Hampton Hawes•For Real!•Contemporary Records•1961','\
Gary Burton Quartet•Picture This•ECM Records•1982','\
Spyro Gyra•Three Wishes•GRP•1992','\
Nellie Lutcher And Her Rhythm•He\'s A Real Gone Guy / Let Me Love You Tonight•Capitol Records•1947','\
no artist•Canadian Sunset•RCA Victor•1956','\
Leonard Cohen•The Future•Columbia•1993','\
Alan Braufman•Valley Of Search•India Navigation•1975','\
The Harper Brothers•The Harper Brothers•Verve Digital•1988','\
Tony Di Bart•Falling For You•Cleveland City Blues•1996','\
Alexander Zonjic•When Is It Real•Optimism Incorporated•1987'),'\
\
Recado Bossa Nova\
':('\
Les Elgart•Recado Bossa Nova / All Alone Am I•Columbia•1962','\
Zoot Sims And His Orchestra•New Beat Bossa Nova Means The Samba Swings•Colpix Records•1962','\
Manhattan Jazz Quintet•Autumn Leaves•Paddle Wheel•1985','\
Klaus Doldinger Quartett•Bossa Nova •Philips•1962','\
Vi Velasco•Recado Bossa Nova / Zing Went The Strings Of My Heart•Colpix Records•0','\
Lee Konitz•Brazilian Serenade•Venus Records (5)•1996','\
Roy Eldridge•What It\'s All About•Pablo Records•1976','\
Manhattan Jazz Quintet•Live At Pit Inn•Paddle Wheel•1986','\
Various•Blue Bossa 2•Blue Note•1987','\
Dusko Goykovich•Celebration•Hot House Records (2)•1987'),'\
\
Recorda-me\
':('\
Red Rodney•Alive In New York •Muse Records•1986','\
Joe Henderson•Page One•Blue Note•1963','\
Billy Mitchell•The Colossus Of Detroit•Xanadu Records•1978','\
Ron Carter•Town Hall Concert•Blue Note•1998','\
Trio Karel Boehlee•Switch•Timeless Records (3)•1984','\
Various•One Night With Blue Note Volume 1•Blue Note•1985','\
Bobby Hutcherson•Color Schemes•Landmark Records (3)•1986'),'\
\
Red Clay\
':('\
Various•California Concert - The Hollywood Palladium•CTI Records•1972','\
Freddie Hubbard•Classics•Fantasy•1984','\
Rare Silk•Red Clay •Polydor•1983'),'\
\
Red Cross\
':('\
Charlie Parker•Red Cross / Tiny\'s Tempo•Savoy Records•1945','\
Sunny Murray•Sunshine•BYG Records•1969','\
Charlie Parker•New Sounds In Modern Music Vol. 1•Savoy Records•1950','\
Jackie McLean•Ode To Super•SteepleChase•1973','\
Dexter Gordon Quartet•Stable Mable•Steeplechase•1975','\
Stu Williamson•Stu Williamson•Bethlehem Records•0','\
Sunny Murray•Sunshine / Hommage To Africa•BYG Records•1971','\
Harold Danko•Mirth Song•Sunnyside•1982','\
Shivananda•Cross Now•Gnome Records (3)•1977','\
Charlie Parker•Congo Blues•Pilz•1993','\
Sphere (16)•Bird Songs•Verve Records•1988','\
Charlie Parker•The World Of Charlie Parker / Bird\'s Nest•Trace (2)•1992','\
Charlie Parker•New Sounds In Modern Music Volume 1•Savoy Records•1950','\
Lionel Hampton And His Orchestra•All American Award Concert•Brunswick•1955','\
Art Farmer Quartet•A Work Of Art•Concord Jazz•1982'),'\
\
Red\'s Blues\
':('\
The Washingtonians•Stack O\'Lee Blues / Red Head Blues•Harmony (4)•1928','\
Johnny Dodds And His Orchestra•Red Onion Blues / Gravier Street Blues•Brunswick•0','\
Red Garland•Red\'s Blues•Prestige•1998','\
Bucky Crawford•Red White And The Blues•Mount Vernon Music•0','\
The New Orleans Black Birds•Red Head / Playing The Blues•Victor•1929','\
Count Basie•Dupree Blues / Red Wagon•Decca•1941','\
Miles Davis•Maiysha / Red China Blues•Columbia•1974','\
Count Basie•Basie Jam•Pablo Records•1975','\
Johnny Dodds•New Orleans Clarinets•Brunswick•1956','\
Count Basie Orchestra•Red Bank Boogie / Jimmy\'s Blues•Parlophone•1946','\
Firehouse Five Plus Two•Red Hot River Valley / Riverside Blues•Good Time Jazz•0','\
Red Rodney•The Red Tornado•Muse Records•1976','\
Red Foley•Rockin\' Chair / Blues In My Red Wagon Blues•Decca•1960','\
Merrill Moore•Red Light / Bartender\'s Blues•Capitol Records•1953'),'\
\
Reflections\
':('\
Vienna Art Orchestra•The Minimalism Of Erik Satie•Hat Hut Records•1984','\
Peter Kowald•Mirrors - Broken But No Dust•Balance Point Acoustics•2001','\
Takagi Et Kako Quartet•Jazz A Maison De Japon Paris•Nadja•1974','\
Giorgio Gaslini•Schumann Reflections•Soul Note•1984','\
Stan Getz•Reflections / Blowin\' In The Wind•Verve Records•1963','\
Jan Garbarek•Places•ECM Records•1978','\
The Visitors (10)•Neptune•Cobblestone•1972','\
Jack Carroll•More And More / Reflections•World Pacific Records•1967','\
Ahmad Jamal•Freeflight•Impulse!•1971','\
Jim Hall•Textures•Telarc Jazz•1997','\
FM (3)•Direct To Disc•Labyrinth Records (3)•1978','\
Billy Hart•Rah•Gramavision•1988','\
FM (3)•Direct To Disc•Labyrinth Records (3)•1978','\
Thelonious Monk Trio•Bemsha Swing•Barclay•1960'),'\
\
Reincarnation of a Lovebird\
':('\
Charles Mingus•Pithecanthropus Erectus•Atlantic•1960','\
Charles Mingus•The Clown•Atlantic•1957','\
Charles Mingus•Charles Mingus In Paris: The Complete America Session•Universal Music Jazz France•2006','\
Pietro Ciancaglini•Reincarnation Of A Lovebird - Homage To Charles Mingus•Rearward•2009','\
Lew Soloff•But Beautiful•Bellaphon•1987','\
Gil Evans•Paris Blues•Owl Records (4)•1988','\
Gérard Marais•Poisson Nageur•Bleu Citron•1992','\
Charles Mingus•The Very Best Of Charles Mingus: The Atlantic Years•Rhino Records (2)•2001'),'\
\
Relentless\
':('\
The Vitamin B12•Kiki\'s Island•Not On Label•2006','\
Steve Grossman•Terra Firma•PM•1977','\
Oregon•1000 Kilometers•C.A.M. Jazz•2007','\
Gary Bartz•The Red And Orange Poems•Atlantic•1994','\
Bob Mintzer•I Remember Jaco•Novus•1991','\
Kenny Barron•Swamp Sally•Verve Records•1996','\
Victor Lewis•Family Portrait•AudioQuest Music•1992','\
Orbert C. Davis•Priority•3sixteen Records•2001','\
Bazooka (13)•Cigars Oysters & Booze•SST Records•1995','\
Gregg Karukas•Looking Up•no label•2005','\
Julian Coryell•Jazzbo•Venus Records (5)•1995'),'\
\
Remark You Made\
':('\
Weather Report•Birdland•CBS•1977','\
Weather Report•Birdland•CBS•1977','\
Weather Report•Heavy Weather•Columbia•1977'),'\
\
Remember Hymn\
':('\
John Abercrombie•Getting There•ECM Records•1988','\
Various•The Blue Note Years Vol. 2: The Jazz Message 1955 - 1960•Blue Note•1998','\
The Oscar Peterson Trio•In Tokyo 1964•Pablo Records•1975','\
Charlie Parker•Quartet Quintet & Sextet•Giants Of Jazz•1986','\
Jack Teagarden And His Orchestra•It\'s Time For Teagarden•Sounds Of Swing•0','\
no artist•Stradivari Champagne•MGM Records•1957','\
Jan Garbarek•Mnemosyne•ECM Records•1999','\
Various•Oscar With Love•Two Lions•2015','\
Brenda Lee•Live In Japan•MCA Records•1975','\
Oscar Peterson•Easy Does It•Book-Of-The-Month Records•1984','\
Charlie Parker•Kind Of Parker•Foreign Media Music•2007','\
Lawrence Welk•200 Years Of American Music•Ranwood•1975','\
Various•100 Hits Jazz•100 Hits•2013'),'\
\
Remember Rockefeller At Attica\
':('\
Charles Mingus•Keystone Korner•Jazz Door•1992','\
Charles Mingus•Changes One•Atlantic•1975','\
Mark Shim•Mind Over Matter•Blue Note•1998','\
Charles Mingus•Changes One & Two•Atlantic•1975','\
Andy Summers•Peggy\'s Blue Skylight•BMG Classics•2000','\
Various•Classic Jazz: The Seventies•Time Life Music•2002'),'\
\
Resolution\
':('\
The Mattson 2•Play "A Love Supreme"•Spiritual Pajamas•2018','\
Indigo Jam Unit•Independent•Basis Records (2)•2011','\
Frank Catalano•Love Supreme Collective•Ropeadope Records•2014','\
Alan Skidmore Quartet•Tribute To \'Trane•Miles Music•1988','\
Elio  Villafranca•Dynamic Resolution•16 Eyes•2011','\
Jukka Tolonen•Cool Train -Tolonen Plays Coltrane!•Akbazar•2005','\
Alvin Queen•Jammin\' Uptown•Nilva Records•1985','\
John Coltrane•A Love Supreme•Jazz Masterworks•1985','\
Katharina Maschmeyer Quartet•A Love Supreme/Universal Tone•Neuklang•2016'),'\
\
Respect\
':('\
Jimmy Smith•Respect / The Cat•Verve Records•1972','\
Jimmy Smith•Funky Broadway•Verve Records•1967','\
Helmut Zacharias•Respect•Capitol Records•0','\
Herbie Mann•Respect Yourself / Mississippi Gambler•Atlantic•1972','\
Cecil McBee Sextet•Music From The Source•Enja Records•1978','\
Dick Hyman and The Group•In The Heat Of The Night•Command•1968','\
Guru•Watch What You Say•Chrysalis•1995','\
Tabou Combo•8th Sacrement•RCA Victor•1975','\
Andy Narell•Behind The Bridge•Heads Up International•1998','\
Herbie Mann•Mississippi Gambler•Atlantic•1972','\
Larry Carlton•Singing / Playing•Blue Thumb Records•1973'),'\
\
Revelation\
':('\
Eddie Henderson•Realization•Capricorn Records•1973','\
Teddy Charles New Directions Quartet•Teddy Charles Featuring Bobby Brookmeyer•Prestige•1954','\
Birdland (3)•Darkness Of Light•PGP RTB•1980','\
Art Blakey & The Jazz Messengers•At The Jazz Corner Of The World Vol. 2•Blue Note•1960','\
Clark Terry•Mother•••! Mother •••••-!! A Jazz Symphony•Pablo Today•1980','\
Tarika Blue•The Blue Path•Chiaroscuro Records•1976','\
Hannibal Marvin Peterson•Hannibal•BASF•1975','\
Bob Brookmeyer•The Dual Role Of Bob Brookmeyer•Prestige•1956','\
Neokarma Jooklo Trio•Time\'s Vibes•Conspiracy Records (2)•2009','\
Gerry Mulligan And The Sax Section•The Gerry Mulligan Songbook Volume 1•World Pacific Records•1958','\
Sonny Fortune•Waves Of Dreams•Horizon (3)•1976','\
Yellowjackets•Live Wires•GRP•1992'),'\
\
Rhythm-a-Ning\
':('\
Art Taylor•Taylor\'s Tenors•Metronome•1959','\
Art Blakey & The Jazz Messengers•Art Blakey\'s Jazz Messengers With Thelonious Monk•Metronome•1958','\
Art Blakey & The Jazz Messengers•Art Blakey\'s Jazz Messengers With Thelonious Monk•Metronome•1959','\
Gil Evans And His Orchestra•Synthetic Evans•PolJazz•0','\
Dexter Gordon•XXL - Live At The Left Bank•Prestige•2002','\
Dexter Gordon Quartet•Swiss Nights Vol. 3•Steeplechase•1979','\
Thelonious Monk•Hackensack•Drive (3)•1989','\
Clark Terry•VARA Radio - 1965•Varajazz•1988','\
SaxEmble•SaxEmble•Qwest Records•1996','\
Gil Evans•Rhythm A Ning•EmArcy•1988','\
Michael Garrick Trio•You\'ve Changed•HEP Records (3)•1981','\
Rory Stuart Quartet•Hurricane•Sunnyside•1987','\
Sam Jones•The Bassist!•Interplay Records•1980','\
Dexter Gordon•At Montreux•Prestige•1985','\
Art Taylor•Taylor\'s Tenors•New Jazz•1959','\
Joey Alexander•Joey.Monk.Live!•Motéma•2017','\
Cedar Walton Quartet•Third Set•SteepleChase•1983','\
Dexter Gordon•Live At The Amsterdam Paradiso Volume Two•Affinity•1980'),'\
\
Riddles\
':('\
John Abercrombie Quartet•Abercrombie Quartet•ECM Records•1980','\
Richard Beirach•Convergence•Triloka Records•1990','\
Laurent De Wilde•Riddles•Gazebo•2016','\
John Abercrombie•The First Quartet•ECM Records•2015','\
Art Tatum•Art!•Fontana•1966','\
Nelson Riddle•Batman (Exclusive Original Television Soundtrack Album)•20th Century Fox Records•1966'),'\
\
Ritual\
':('\
Fire! Orchestra•Ritual•Rune Grammofon•2016','\
Tatsuya Nakatani•Ritual Inscription•Epigraph Records•2012','\
Black Renaissance•Body Mind And Spirit •Baystate•1977','\
Václav Zahradník And His East All Stars Band•Interjazz•Supraphon•1971','\
Miles Davis•Backyard Ritual•Warner Bros. Records•1986','\
Lee Morgan•Caramba•Blue Note•1968','\
Reg Owen And His Orchestra•Manhattan Spiritual / Ritual Blues•Palette•1958','\
Golden Jooklo Age•Ritual•Troglosound•2009','\
Jimmy Smith•And I Love You So•Verve Records•1973','\
The Victor Feldman All-Stars•Soviet Jazz Themes•Ava•1963'),'\
\
River People\
':('\
Weather Report•River People / Birdland•CBS•1978','\
Weather Report•Birdland•CBS•1977','\
Sammy Kaye•The Rich People Of Brooklyn / Dreamy River•Columbia•0','\
Weather Report•River People / The Pursuit Of The Woman With The Feathered Hat•ARC (3)•1978','\
The Jimmy Giuffre Trio•River Chant•Choice (7)•1975','\
Joe LoCascio•Sleeping City•Optimism Incorporated•1989','\
Sandro Albert•Soulful People•Meridian Music Inc.•2000','\
Will Sessions•Kindred Live•Sessions Sounds•2017','\
Lucky Thompson•Happy Days Are Here Again•Prestige•1965','\
Weather Report•Mr. Gone•ARC (3)•1978','\
Tommy Bolin•Come Taste The Man•Tommy Bolin Archives Inc.•1999','\
John Porter (2)•China Disco•Pronit•1982','\
Abbey Lincoln•Talking To The Sun•Enja Records•1984'),'\
\
Road Song\
':('\
Earl Wrightson•Ballads Of A Soldier Of Fortune•Columbia•1962','\
Sadao Watanabe•Open Road•CBS/Sony•1973','\
Sabenza•Sabenza•Mountain Records (2)•1987','\
Pat Martino•We\'ll Be Together Again•Muse Records•1976','\
Lee Oskar•My Road Our Road•Elektra•1981','\
T-Square•Midnight Lover•CBS/Sony•1979','\
Gary Meek•Live At Ronnie Scott\'s•Bootleg.Net•1996','\
Pat Martino•The Visit!•Cobblestone•1972','\
SMaLL Trio•Road Trip•Meifumado•2012','\
no artist•Brian Auger\'s Oblivion Express•RCA Victor•1971','\
Oriental Wind•Life Road•JA&RO records•1983'),'\
\
Robbin\'s Nest\
':('\
Ella Fitzgerald•All My Life•Le Chant Du Monde•2010','\
Various•Jazz Musica Del Nostro Tempo•RCA•1969'),'\
\
Rockin\' Chair\
':('\
Louis Armstrong And His All-Stars•Rockin\' Chair / Sugar•no label•0','\
Roy Eldridge And His Orchestra•Rockin\' Chair / Yard Dog•Decca•1946','\
Duke Ellington And His Orchestra•Runnin\' Wild / Rockin\' Chair•Brunswick•1931','\
Louis Armstrong And His All-Stars•St. James Infirmary / Rockin\' Chair•RCA Victor•1955','\
Louis Armstrong And His All-Stars•Jack-Armstrong Blues / Rockin\' Chair•RCA Victor•1947','\
Kay Starr•Rockin\' Chair•RCA Victor•1958','\
Mildred Bailey•Rockin\' Chair / Georgia On My Mind•Bluebird (3)•1937','\
The Mills Brothers•Moanin\' For You / Rockin\' Chair•Brunswick•0','\
Duke Ellington And His Orchestra•East St. Louis Toodle-Oo / Rockin\' Chair•Decca•0','\
Bing Crosby•Havin\' Fun!•Jasmine Records•1983','\
Mildred Bailey•Rockin\' Chair / Georgia On My Mind•Bluebird (3)•1937','\
Casani Club Orchestra•Red Sails In The Sunset / Georgia Rockin\' Chair•Perfect (3)•1935','\
Mildred Bailey•Rockin\' Chair / Sometimes I\'m Happy•Decca•1941','\
Roy Eldridge•Roy "Little Jazz" Eldridge•Philips•0'),'\
\
Rockin\' In Rhythm\
':('\
Weather Report•Rockin\' In Rhythm•ARC (3)•1980','\
Duke Ellington And His Orchestra•No Papa No / Rockin\' In Rhythm•no label•1942','\
The Harlem Footwarmers•Rockin\' In Rhythm / Old Man Blues•Okeh•1931','\
The Harlem Footwarmers•Big House Blues / Rockin\' In Rhythm•Parlophone•1933','\
Ella Fitzgerald•Ella Fitzgerald Chante Les Succès De: Duke Ellington•Barclay-Verve•1960','\
Duke Ellington And His Orchestra•Ellington \'55 (Part 1)•Capitol Records•1955','\
Duke Ellington And His Orchestra•1930-1931•Classics (11)•1991','\
no artist•Adrian Bentzons Jazzband•Storyville•1958','\
Duke Ellington And His Orchestra•Piano In The Background•Philips•1960','\
Duke Ellington•I Giganti Del Jazz Vol. 64•Curcio•0','\
Duke Ellington•Such Sweet Thunder•Jazz Life•1988','\
Steve Lacy•Soprano Sax•Prestige•1958','\
Sonny Criss•Rockin\' In Rhythm•Prestige•1969'),'\
\
Rosetta\
':('\
Jazz At The Philharmonic•Jazz At The Philharmonic Vol. 5 Rosetta•Asch Recordings•0','\
Fred Böhler And His Band•Fred\'s Jump•Columbia•1940','\
Henry "Red" Allen And His Orchestra•Dinah Lou / Rosetta•Parlophone•1943','\
Earl Hines•Rosetta / \'Deed I Do•Columbia•1951','\
Quintet Johnny Meyer•Rosetta / Re-Bop Continental•Decca•1948','\
Ray Charles•Hard Hearted Hannah•ABC-Paramount•0','\
Earl Hines•Rosetta / Glad Rag Doll•Bluebird (3)•1940','\
Brother Bones•Rosetta / Bubber\'s Boogie•Tempo (7)•1949','\
Jimmy Smith•At Club "Baby Grand" Wilmington Delaware Volume 1•Blue Note•1956','\
Nat King Cole•Nat Cole At JATP•VSP•1966'),'\
\
Round Midnight\
':('\
Various•\'Round Midnight•Milestone (4)•1986','\
Barney Wilen Quartet•Newport \'59•Fresh Sound Records•1991','\
Milt Jackson Orchestra•\'Round Midnight / Namesake•Riverside Records•1962','\
The Charlie Parker All-Stars•1950•Alamac•1974','\
The Miles Davis Quintet•\'Round Midnight / Solea•Columbia•0','\
Wes Montgomery•Round About Midnight•Riverside Records•0','\
Terumasa Hino•Wheel Stone - Live In Nemuro Vol. 2•East Wind•1981','\
Miles Davis•The Winners Of Down Beat\'s Readers Poll 1960 "Horns "•Philips•1960','\
George Wallington•In Sweden•Prestige•0','\
Miles Davis•The Winners Of Down Beat\'s Readers Poll 1960 "Horns "•Philips•1960','\
George Wallington•In Sweden•Prestige•0','\
Max Roach Quartet•Live In Tokyo Vol.1•Denon Jazz•1977','\
Charles Tolliver•Live In Tokyo•Strata-East•1974','\
Kenny Baker And His Band•Round About Midnight / Afternoon In Paris•Parlophone•1953','\
Thelonious Monk•\'Round Midnight•Milestone (4)•1982','\
Jimmy Raney Quintet•Jimmy Raney Plays•Prestige•1953','\
Miles Davis•Miles Davis And The Modern Jazz Giants•Metronome•0','\
Lee Konitz•Creative Music Studio - Woodstock Jazz Festival 1•Douglas Music•1997','\
Dizzy Gillespie•Unissued In Europe 1971 (Live In Warsaw Böblingen & Milan)•Gambit Records•2008'),'\
\
Round Trip\
':('\
The 360 Degree Music Experience•From Rag Time To No Time•360 Records (2)•1975','\
Sadao Watanabe•Round Trip•CBS/Sony•1970','\
Ralph Moore (2)•Round Trip•Reservoir (2)•1987','\
Yoshiaki Masuo•24•CBS/Sony•1970','\
Sadao Watanabe•At Montreux Jazz Festival•CBS/Sony•1971','\
Nataniel Edelman Trio•Humedad•Kuai Music•2015','\
John Abercrombie•The Third Quartet•ECM Records•2007','\
John Abercrombie•The Third Quartet•ECM Records•2007','\
Teo Macero•Impressions Of Virus•Columbia•1980','\
Ornette Coleman•The Best Of Ornette Coleman•Blue Note•1997','\
Rita Marcotulli Trio•Oslo Party•A Témpo•1989','\
Scalino Scaleno•Scalino Scaleno•Cobra Records (3)•1988','\
Sadao Watanabe•Birds Of Passage•Elektra•1987','\
Ornette Coleman•New York Is Now!•Blue Note•1968','\
Tiziana Ghiglioni•Yet Time•Splasc(h) Records•1988'),'\
\
Rubberneck\
':('\
Stan Getz•Getz The Great•Jazztone (2)•1955','\
Stan Getz•At Storyville - Vol. 2•Roost•1957','\
Stan Getz•The Greatest Of Stan Getz•Roost•1963','\
Stan Getz•Stan Getz•Jazztone (2)•1956','\
Max Bennett•Max Bennett•London Records•1955','\
Max Bennett•Max Bennett Plays•Bethlehem Records•1957','\
Stan Getz•The Stan Getz Years•Royal Roost•1964','\
Stan Getz•At Storyville•Roulette•1973','\
Stan Getz•Jazz Summit•Disques Vogue•1972','\
Curtis Fuller•The Trombone Album•Savoy Records•1980','\
Stan Getz•The Best Of Stan Getz•Roulette•1972','\
Various•Swing... Not Spring!•Savoy Records•1956'),'\
\
Ruby\
':('\
Bob James•Live At Montreux•Koch Records•2005','\
Bob James•Bob James Live: From The Queen Mary Jazz Festival•V.I.E.W. Video•1988','\
Bob James•12•Tappan Zee Records•1984','\
Harry James And His Orchestra•Palladium Party / Ruby•Columbia•1953','\
Les Brown And His Band Of Renown•Ruby / Midnight Sun •Coral•1953','\
Les Brown And His Band Of Renown•Ruby / Midnight Sun•Coral•1953','\
Orchestr Spoutaného Divadla•Potopa / Svět Na Ruby•Ultraphon•0','\
European Jazz Quintet•III•Fusion (3)•1982','\
The Les Morgan Orchestra•Ruby / Limelight (Terry\'s Theme)•Tops Records•0','\
Thelonious Monk Trio•Ruby My Dear / Evidence•Blue Note•1949','\
Milt Jackson Sextet•Invitation•Riverside Records•1962','\
Thelonious Monk•Ruby My Dear - Monk And Trane•Riverside Records•1961'),'\
\
Ruby My Dear\
':('\
Thelonious Monk Trio•Ruby My Dear / Evidence•Blue Note•1949','\
Thelonious Monk•Ruby My Dear - Monk And Trane•Riverside Records•1961','\
The Thelonious Monk Quartet•In Europe•Unique Jazz•0','\
The Kenny Drew Trio•Ruby My Dear•SteepleChase•1980','\
Thelonious Monk•Monk\'s Music•Cinevox•1981','\
Thelonious Monk•Monk\'s Mood - Live In Paris 1967 - Vol. 1•Jazz & Jazz•1990','\
Thelonious Monk•Thelonious Monk With John Coltrane•Jazzland•1961'),'\
\
Rush Hour\
':('\
Chieli Minucci•Sweet Surrender•Shanachie•2007','\
Don Friedman Trio•A Day In The City : Six Variations On A Theme•Riverside Records•1961','\
Rüdiger Carl Inc.•King Alcohol (New Version)•FMP•1973','\
Yellowjackets•Matinee Idol•Warner Bros. Records•1981','\
Ivo Perelman Quartet•Sieiro•Leo Records•1999','\
Stagg•Stagg•Long Hair•2018','\
Bob James•Lucky Seven•Tappan Zee Records•1979','\
Frank Strazzeri•After The Rain•Catalyst Records (3)•1976','\
Seventh Avenue (4)•Heads Up•ITI Records•1984','\
The David Chesky Band•Rush Hour•Columbia•1980','\
Ray Pizzi•Conception•Pablo Records•1977','\
Shivananda•Cross Now•Gnome Records (3)•1977','\
George Robert Quartet•Looking Ahead•TCB Records (2)•1989','\
Bob James•Mr. New York•Tappan Zee Records•1980'),'\
\
S Wonderful\
':('\
Lionel Hampton And His Quartet•The Lionel Hampton Quartet•Clef Records•1954','\
Buddy DeFranco•Buddy DeFranco And Oscar Peterson Play George Gershwin•Karusell•1955','\
Harold Baker•\'S Wonderful / Cherry•King Records (3)•1960','\
Ray Conniff And His Orchestra & Chorus•\'S Wonderful•CBS•1962','\
The John Dankworth Orchestra•\'S Wonderful / Younger Every Day•Parlophone•1953','\
Thelonious Monk•Thelonious Monk And Herbie Nichols•Savoy Jazz•1986','\
Artie Shaw And His Orchestra•I\'ll Never Be The Same / \'S Wonderful•Victor•1945','\
Coleman Hawkins Quintet•\'S Wonderful / I Only Have Eyes For You•Keynote Recordings (2)•1944','\
Lionel Hampton And His Quartet•The Lionel Hampton Quartet•Clef Records•1954','\
Various•Quickstep•Philips•0','\
Art Tatum•The Tatum-Carter-Bellson Trio Album #2•Clef Records•1955','\
The Dave Brubeck Trio•The Dave Brubeck Trio•Fantasy•1953','\
McGuire Sisters•Somebody Loves Me / Mississippi Mud / \'S Wonderful / All By Myself•Coral•0','\
Sid Phillips Band•Dixie Beat•no label•1959','\
Harry Edison All-Stars•\'S Wonderful - Live At Club House 33•Pablo Live•1983'),'\
\
Sabia\
':('\
Frank Sinatra•Lady Day•Reprise Records•1971','\
The Cedar Walton / Hank Mobley Quintet•Breakthrough•Cobblestone•1972','\
Pat Patrick•Sound Advice•El Saturn Records•1977','\
Cedar Walton•The Maestro•Muse Records•1981','\
John McLaughlin•Black Light•Abstract Logix•2015','\
Sambrasa Trio•Em Som Maior•Som Maior•1965'),'\
\
Safari\
':('\
Bert Kaempfert•A Swinging Safari•Polydor•1977','\
Sabu Martinez•Safari With Sabu•Vik•1958','\
Billy Vaughn And His Orchestra•A Swingin\' Safari / Blue Hawaii•Dot Records•1962','\
The Puppets (5)•Theme From "Funeral In Berlin" / Manhattan Safari•RCA Victor•1967','\
Prince Lasha•Inside Story•Enja Records•1981','\
Afric Simone•Barracuda / Hey Safari•BASF•1972','\
Ded Gerval Et Son Orchestre•Mon Pays C\'est L\'ete•Philips•0','\
Al Hirt•Keep The Ball Rollin\' / Manhattan Safari•RCA Victor•1968'),'\
\
Saga of Harrison Crabfeathers\
':('\
Steve Kuhn•Ecstasy•ECM Records•1975','\
Pétur Östlund•Power Flower•Jazzís•1997','\
Steve Kuhn•Steve Kuhn Live In New York•Cobblestone•1972','\
Monica Zetterlund•Chicken Feathers•SR Records•1972','\
Brian Bromberg•Wood•Seven Seas•2001','\
Come Shine•Do Do That Voodoo•Curling Legs•2002','\
Sheila Jordan•Sheila•SteepleChase•1978'),'\
\
Sail Away\
':('\
The Jack Daugherty Band•Save Your Self•A&M Records•1972','\
Storyville (3)•The Blues Ain\'t News•Granite Music Corp.•1977','\
Richard Elliot•Initial Approach•ITI Records•1984','\
Tom Harrell•Sail Away•Contemporary Records•1989','\
The Melton Brothers Band•Livin\' In The City•MDM Communications•1979','\
Joe Lovano•Quartets: Live At The Village Vanguard Volume 1•Blue Note•2014','\
Kenny Barron•Wanton Spirit•Gitanes Jazz Productions•1994','\
no artist•Call Of The Wild•TBA Records•1984','\
Eric Alexander Quartet•Extra Innings•Alfa Jazz•2000','\
Francesco Cafiso•Portrait In Black And White•Venus Records (5)•2008','\
Ace Cannon•Golden Classics•Gusto Records (2)•1980','\
Don Friedman•Hot House•Chiaroscuro Records•2004'),'\
\
Sailing at Night\
':('\
Dave Grusin•Sticks And Stones•GRP•1988','\
Najee•Rising Sun•Heads Up International•2007','\
Diferenz•Jazz Workshop•Loose Ends Records•1994','\
James Last•Cap\'n James•no label•0','\
Various•California Dreamin\': Smooth Jazz On A West Coast Trip•Metro Doubles•2002','\
Edmond Hall•The Complete Edmond Hall / James P. Johnson / Sidney De Paris / Vic Dickenson Blue Note Sessions•Mosaic Records (2)•1985','\
Tommy Dorsey•The Complete Tommy Dorsey Volume VII 1938•Bluebird (3)•1981','\
Various•BeBop Spoken Here•Proper Records (2)•2000','\
Various•Today\'s Favourites Tomorrow\'s Evergreens•no label•2006','\
Various•Jazz 3: The Family Of Singing Ladies•CBS•1977','\
Various•The Big Horn (The History Of Honkin\' & Screamin\' Saxophone)•Proper Records (2)•2003','\
James Last•The Best Of James Last•Polydor•1979','\
John Lee Hooker•Portrait•Past Perfect 24 Carat Gold Edition•2001','\
Various•TV Music Spectacular•no label•1978'),'\
\
Saint James Infirmary\
':('\
Les Gipsy Sanders•Nobody Knows•Belfort Disques•1964','\
Louis Armstrong•West-End Blues•Odeon•0','\
Stan Rubin And His Tigertown Five•Stan Rubin And His Tigertown Five•Jubilee•0','\
Hank Jones•Bluesette•Black And Blue•1979','\
Kid Ory And His Creole Jazz Band•1953•Good Time Jazz•1954','\
Louis Armstrong & His Hot Five•Louis Armstrong And His Hot Five With Earl Hines (1928)•Odeon•1952','\
Bill Ramsey•Jazz Festival Sopot•Disco-Club•1957','\
Doc Cheatham•Hey Doc!•Black And Blue•1975','\
Pete Fountain•Down On Rampart Street•Intermedia Records Inc.•1982','\
Glenn Ferris "Pentessence" Quintet•Skin Me!•Naïve•2004','\
The Dixie Rebels•Holidays In Dixieland•Bea Ton•0','\
Space Cadets (4)•Dixieland Jazz•Promenade•0','\
Various•History Of Jazz Vol.4 - New Orleans Revival•BYG Records•1970'),'\
\
Salt Peanuts\
':('\
Donald Byrd Quintet•Parisian Thoroughfare•Brunswick•1958','\
Charlie Parker•Le Jazz Cool Historical Recordings Vol. 2•Le Jazz Cool•1960','\
Dizzy Gillespie•Jazz At Massey Hall Volume 1•Debut Records (3)•1958','\
The Quintet Of The Year•Jazz At Massey Hall•Vogue•1956','\
Dizzy Gillespie And His All Star Quintet•Shaw\' Nuff / Salt Peanuts / Lover Man / Stupendous•Pathé•0','\
Dizzy Gillespie Quintet•An Electrifying Evening With The Dizzy Gillespie Quintet•Verve Records•1961','\
Dizzy Gillespie Quintet•An Electrifying Evening With The Dizzy Gillespie Quintet•Verve Records•1961','\
Dizzy Gillespie And His Orchestra•Salt Peanuts / I Waited For You / Emanon / A Hand Full Of Gimme•A•R•C Records•0','\
Charlie Parker•Bird & Diz•Charlie Parker Records•1983','\
The Quintet•Jazz At Massey Hall Volume One•Debut Records•1953'),'\
\
Samba Du Bois\
':('\
Phil Woods•Back In New York•Vedette Records•1977','\
Phil Woods•Musique Du Bois•Muse Records•1974','\
Claude Nougaro•L\'amour Sorcier•Mercury•2014'),'\
\
Same Shame\
':('\
Bobby Hutcherson•Total Eclipse•Blue Note•1968','\
Chico Freeman•Destiny\'s Dance•Contemporary Records•1982','\
Bobby Hutcherson•The View From The Inside•Blue Note•1977','\
Bobby Hutcherson•The Best Of The Blue Note Years•Blue Note•2001','\
Various•Lord Have Mercy (The Soulful Gospel Of Checker Records)•Play Back•2017','\
Bob Wills & His Texas Playboys•The Golden Era•Columbia•1987'),'\
\
Sandu\
':('\
Clifford Brown And Max Roach•Study In Brown Vol.3•EmArcy•1957','\
The George Russell Sextet•George Russell Sextet In K.C.•Decca•1961','\
The Dave Bailey Sextet•One Foot In The Gutter: A Treasury Of Soul•Epic•1960','\
Manhattan Jazz Orchestra•Moritat•Sweet Basil (2)•1990','\
no artist•no title•no label•no year','\
Don Patterson•Four Dimensions•Prestige•1968','\
James Carter Quartet•Jurassic Classics•DIW•1994','\
Art Farmer•Something You Got•CTI Records•1977','\
Ryan Kisor•Kisor •Videoarts Music•2000','\
Freddie Hubbard•Double Take•Blue Note•1985'),'\
\
Satin Doll\
':('\
Claude McLin•Misty / Satin Doll•Allegro (12)•1960','\
Franco Cerri•2 Bacchette Per 1 Chitarra•GTA Records•1966','\
Bob Creed•Satin Doll•Jar-Bal Records•0','\
Duke Ellington•Satin Doll / Sophisticated Lady•RCA Victor•0','\
Duke Ellington And His Orchestra•Satin Doll / Without A Song•Capitol Records•1953','\
Various•Jazz For A Sunday Afternoon Volume 3•Solid State Records (2)•1968','\
Shirley Scott•Satin Doll•Prestige•1963','\
Billy Maxted•Satin Doll•Liberty•1967','\
The Chico Hamilton Quintet•Satin Doll•Pacific Jazz•0','\
Duke Ellington And His Orchestra•Take The "A" Train / Satin Doll•Columbia•0','\
Earl Grant•Just One More Time •Decca•1965','\
Ella Fitzgerald•Ella Fitzgerald Chante Les Succès De: Duke Ellington•Barclay-Verve•1960','\
Coleman Hawkins•Hawkins! Eldridge! Hodges! Alive! At The Village Gate!•Verve Records•1962','\
Vicki Gillespie•We Love You Madley (A Tribute To Duke Ellington)•Pye Records•1974','\
Kenny Clarke•Kenny "To Day"•Night And Day (2)•1980','\
Kenny Clarke•Kenny "To Day"•Night And Day (2)•1980','\
Duke Ellington And His Orchestra•Band Call•Capitol Records•1956'),'\
\
Save You Love for Me\
':('\
Jackie Verdeel•Exactly Like You•New Sound Recording Co.•0','\
Watson T. Browne•Will You Love Me Tomorrow / Save The Last Dance For Me•Bell Records•1970','\
Vince Jones•One Day Spent•EMI•1990','\
Eric Alexander•Chicago Fire•HighNote Records Inc.•2014','\
Scott Hamilton•Across The Tracks•Concord Jazz•2008','\
Eddie Drennon & The B.B.S. Unlimited•Would You Dance To My Music•Casablanca•1977','\
Jimmy Ponder•So Many Stars•Milestone (4)•1985','\
David "Fathead" Newman•Back To Basics•Milestone (4)•1991','\
The Great Jazz Trio•Aurex Jazz Festival\' 81 / The Great Jazz Trio & Friends With Nancy Wilson•Eastworld•1981','\
Theo Croker•Afro Physicist•DDB Records (2)•2014','\
Harry Connick Jr.•Only You•Columbia•2004','\
Rebecca Parris•Spring•MusicMasters Jazz•1993','\
The Kenny Davern Trio•The Last Reunion•Upbeat Jazz•1998','\
Freddy Cole•In The Name Of Love•Telarc•2003','\
José James•Blackmagic•Brownswood Recordings•2010','\
Alex Chilton•Songs From Robin Hood Lane•Bar/None Records•2019','\
Nancy Wilson•Save Your Love For Me: Nancy Wilson Sings The Great Blues Ballads•Capitol Jazz•2005','\
Ann Hampton Callaway•At Last•Telarc•2009','\
The Soul Explosion•Soul Fire•Center•1968','\
Claire Martin•Devil May Care•Linn Records•1993','\
Si Zentner And His Orchestra•Big Band Plays The Big Hits•Liberty•1961'),'\
\
Saving All My Love For You\
':('\
Erik Norström•Before Breakfast•Not On Label (Sävedalen Big Band Self-released)•0','\
Dave Stahl Band•Anaconda•Abee Cake Records•1987','\
Ottottrio•Super Guitar Session: Red Live•CBS/Sony•1988','\
no artist•Avant Pop•ECM Records•1986','\
Akiko Tsuruga•Sweet And Funky•18th & Vine•2007','\
Hank Crawford•Groove Master•Milestone (4)•1990','\
Paul Mauriat•Windy•Philips•1986','\
Don Braden•Organic•Epicure•1995','\
no artist•The Fire This Time•In+Out Records•1992','\
Susan Wong•511•Evosound•2009','\
Russell Malone•All About Melody•HighNote Records Inc.•2016','\
Fausto Papetti•Oggi 2•CBS•1986','\
Yasuko Agawa•Jazz Ballad•Invitation•1993','\
David McAlmont•Set One - You Go To My Head•Blue Port Recordings•2005','\
Various•14 Faðmlög•Skífan•1985','\
Keiko Lee•A Letter From Rome•SME Records•2000'),'\
\
Scene Is Clean\
':('\
Zoot Sims•You Go To My Head / The Scene Is Clean•Prestige•1950','\
Tadd Dameron•Fontainebleau•Prestige•1956','\
Archie Shepp Quartet•Parisian Concert Volume 1•Impro•1977','\
Continuum (5)•Mad About Tadd•Quicksilver•1982','\
Ronnie Cuber•The Scene Is Clean•Milestone (4)•1994','\
Archie Shepp•On Green Dolphin Street•Denon•1978','\
Clifford Brown And Max Roach•At Basin Street•EmArcy•1956','\
Jack Wilson•The Two Sides Of Jack Wilson•Atlantic•1964','\
Clifford Brown•Clifford Brown\'s Finest Hour•Verve Records•2000'),'\
\
Scrapple From the Apple\
':('\
The Charlie Parker Quintet•Scrapple From The Apple / Don\'t Blame Me•Dial Records (3)•1948','\
Cecil Payne•A Night At The Five Spot•Signal (3)•1957','\
Cecil Payne•The Music Of Charlie Parker -Bird\'s Night•Savoy Record Co.•1985','\
Paul Motian•Paul Motian And The Electric Bebop Band•JMT•1993','\
The Modern Jazz Group Freiburg•Weekend - Friday•Fono-Ring•0','\
Curtis Fuller•Jazz Conference Abroad•Smash Records (4)•1962','\
Yoshio Otomo/Hidefumi Toki Alto-Madness•Lover Man•Three Blind Mice•1975','\
Tony Fruscella•Tony Fruscella-Phil Woods Quintet•Stateside•0','\
no artist•no title•no label•no year','\
Charlie Parker•Bird At The Roost•Savoy Records•1977','\
Charlie Parker•The \'Bird\' Returns•Savoy Records•1962','\
Tsuyoshi Yamamoto•Live At Misty \'77 Vol. Two•Flying Disk•1978','\
Sonny Stitt & His West Coast Friends•Groovin\' High•Atlas Record (2)•1980','\
Charlie Parker•International Jam Sessions•Xanadu Records•1976','\
Charlie Parker•Charlie Parker On Dial Volume 5•Spotlite Records•1970'),'\
\
Sea Journey\
':('\
Maria Schneider Orchestra•Allégresse•ArtistShare•2000','\
Stanley Clarke•Children Of Forever•Polydor•1973','\
Gary Burton Quartet•Passengers•ECM Records•1977','\
Stanley Clarke•Children Of Forever•Polydor•1976','\
Debbie Fier•In Your Hands•no label•1982','\
Sergio Salvatore•Tune Up•GRP•1994','\
Brian Bennett•Nature Watch•Bruton Music•1982','\
Dylan Ryan•Circa•Cuneiform Records•2014','\
Gary Burton•Quartet Live•Concord Jazz•2009'),'\
\
Search for Peace\
':('\
Flora Purim•Casa Forte•Milestone (4)•1974','\
Kosuke Mine Quartet•Solid•East Wind•1976','\
McCoy Tyner•13th House•Milestone (4)•1982','\
McCoy Tyner•The Real McCoy•Blue Note•1967','\
Joanne Brackeen•New True Illusion•Timeless Records (3)•1976','\
McCoy Tyner•Passion Dance•Milestone (4)•1979','\
Ravi Coltrane•Moving Pictures•BMG France•1998','\
Tim Garland•Return To The Fire•Edition Records•2015'),'\
\
Second Time Around The\
':('\
Frank Sinatra•Hit Parade Vol.1•Reprise Records•1962','\
Shirley Scott•Out Of It / The Second Time Around•Prestige•1963','\
Jane Morgan•Theme From Carnival (Love Makes The World Go \'Round)•London Records•1963','\
Shirley Scott•Drag \'Em Out•Prestige•1963','\
The Chico Hamilton Quintet•Passin\' Thru•Impulse!•1963','\
Tony Bennett•The Very Thought Of You•Columbia Special Products•0','\
Hank Crawford•Soul Survivors•Milestone (4)•1986','\
Shirley Bassey•Let\'s Face The Music•Columbia•1962','\
Wayne Horvitz•Upper Egypt•Knitting Factory Records•2000','\
The George Duke Quartet•The George Duke Quartet Presented By The Jazz Workshop 1966 Of San Francisco•SABA•1966','\
George Duke•The Primal George Duke•MPS Records•1978','\
Monica Zetterlund•It Only Happens Every Time•EMI•1978','\
Teddy Wilson•Air Mail Special•Polydor•0','\
Hank Crawford•Soul Brothers•Milestone (4)•1989','\
Count Basie Orchestra•Basie•Verve Records•0'),'\
\
Secret Love\
':('\
Willis Jackson•Secret Love Pt. 1 / Secret Love Pt. 2•Prestige•1963','\
Bing Crosby•Secret Love / My Love My Love•Decca•0','\
Count Basie Orchestra•Secret Love•Command•1967','\
Eddie Heywood•Secret Love•Mercury•1956','\
Ahmad Jamal Trio•Secret Love / Taking A Chance At Love•Argo (6)•1958','\
Richard "Groove" Holmes•Secret Love / Hallelujah I Love Her So•Pacific Jazz•0','\
Jerry Betters•Caravan / Secret Love•Gateway Records•1963','\
The Jonah Jones Quartet•Swingin\' AT The Cinema - Hit Songs From Hollywood Films•Capitol Records•0','\
Phil Tate And His Orchestra•Secret Love•Oriole•1963','\
Ahmad Jamal Trio•At The Spotlight Club Vol.2•Argo (6)•1958','\
Tony DeSimone•Secret Love•Epic•1954','\
Tete Montoliu Trio•Secret Love•Timeless Records (3)•1978','\
Jim Hall Trio•Jim Hall Live In Tokyo•A&M Records•1976','\
Ahmad Jamal Trio•At The Spotlight Club Vol.2•Argo (6)•1958','\
John & Jerry Case•Sextet Sessions•Priority Records (7)•1972','\
The Oscar Peterson Trio•The Trio•Pablo Records•1974','\
Oscar Peterson•The Trio•Pablo Records•1977','\
Lynn Collins (3)•Anyone Who Had A Heart•Variety (2)•1964','\
Cliff Smalls•Cliff Smalls•Black And Blue•1978','\
Charles Mingus•Mingus (Charlie Mingus) 1968•Rhapsody Films•1988','\
The Brass Ring•Guantanamera•RCA Victor•1966','\
Jimmy Owens•Jimmy Owens•Horizon (3)•1976','\
Dexter Gordon•Blues A La Suisse•Prestige•1974','\
Ted Heath And His Music•Hits I Missed•Decca•1958','\
Teddy Edwards•Heart & Soul•Contemporary Records•1962','\
Oscar Peterson•The Trio•Pablo Records•1977'),'\
\
Self Portrait in Three Colors\
':('\
Ahmed Abdullah•Abdullah Live At Ali\'s Alley•Cadence Jazz Records•1980','\
Marion Brown Quintet•Offering•Venus Records (5)•1993','\
Ravi Coltrane•Mad 6•no label•2002','\
Greg Osby•Inner Circle•Blue Note•2002','\
Charles Mingus•Mingus Ah Um•Columbia•1959'),'\
\
Semblence\
':('\
Gary Burton•Times Square•ECM Records•1978','\
Keith Jarrett•Facing You•ECM Records•1972','\
Gary Burton•Gary Burton•Supraphon•1981'),'\
\
Senor Blues\
':('\
Chris Connor•Senor Blues•Atlantic•1960','\
The Horace Silver Quintet•Señor Blues•Blue Note•1956','\
The Rhythmakers•Yellow Dog Blues / Yes Suh!•Parlophone•1941','\
Joe Harriott Quintet•Blue Harriott•Columbia•1959','\
Horace Silver•Sterling Silver•Blue Note•1979','\
Horace Silver•The Best Of Horace Silver•Blue Note•1969','\
The Horace Silver Quintet•6 Pieces Of Silver•Blue Note•1956','\
Shirley Scott•Plays Horace Silver•Prestige•1962','\
Horace Silver•14 Février 1959•Frémeaux & Associés•2016'),'\
\
Senor Mouse\
':('\
Duo Fenix•Karai-Eté•In+Out Records•1992','\
Al Di Meola•Flesh On Flesh•Telarc•2002','\
Martin Taylor•Triple Libra•Wave (4)•1981','\
Chick Corea•Chick Corea•Polydor•1987','\
Chick Corea•Forever•Concord Records•2011','\
Herb Alpert & The Tijuana Brass•Coney Island•A&M Records•1975','\
Return To Forever•Hymn Of The Seventh Galaxy•Polydor•1973'),'\
\
September In The Rain\
':('\
Dinah Washington•September In The Rain•Mercury•1992','\
Julie London•Lonely Girl•Liberty•1956','\
Lester Young And His Orchestra•September In The Rain / Pete\'s Cafe•Clef Records•1953','\
Lionel Hampton Trio•Always / September In The Rain•Jazz Selection•1956','\
Los Angeles City College Orchestra•Cream Puff / September In The Rain•Capitol Records•1953','\
Tommy Dorsey And His Orchestra•Black Strap Molasses / September In The Rain •Decca•1951','\
The George Shearing Quintet•September In The Rain / Bop Look And Listen•MGM Records•1949','\
The Dave Brubeck Octet•What Is This Thing Called Love / September In The Rain•Fantasy•1950','\
Dinah Washington•September In The Rain•Mercury•1961','\
Milt Buckner•Midnight Slows Vol 6•Black And Blue•1977','\
The George Shearing Quintet•September In The Rain / East Of The Sun (West Of The Moon)•MGM Records•0'),'\
\
September Song\
':('\
Chet Baker Trio•September Song•Marshmallow (3)•1986','\
Artie Shaw And His Orchestra•Frenesi•RCA Victor•0','\
Sidney Bechet & His Circle Seven•September Song / Who•Esquire•0','\
Sidney Bechet•September Song / Summertime•Vogue Productions•1952','\
Sidney Bechet•Les Oignons / September Song•Vogue Productions•0','\
Hal McIntyre And His Orchestra•Summer Night / September Song •Cosmo•1946','\
Gene Krupa Trio•Harmonica-Shu-Boogie / September Song•Blue Star•0','\
John Lewis (2)•Improvised Meditations & Excursions•Atlantic•0','\
Artie Shaw And His Orchestra•September Song / Little Jazz•Victor•1945','\
Jo Stafford•September Song / Yesterdays•Capitol Records•1950','\
The Slew Foot Five•Sioux City Sue / September Song•Decca•0','\
Sarah Vaughan•Lullaby Of Birdland / September Song•EmArcy•0','\
Stan Kenton And His Orchestra•Laura•Capitol Records•1951','\
Al Hirt•September Song / Up Above My Head (I Hear Music In The Air)•RCA Victor•1964','\
Earl Bostic And His Orchestra•September Song / Sleep•King Records (3)•0','\
Sil Austin•Gone Again•Mercury•1959','\
Harry James And His Orchestra•Ab-Mur / September Song•Columbia•1948'),'\
\
Serenade In Blue\
':('\
Glenn Miller And His Orchestra•Serenade In Blue / Blue Evening•RCA Victor•1948','\
Ray Anthony & His Orchestra•Serenade In Blue / Moonlight Serenade •Capitol Records•0','\
Kenyon Hopkins And His Orchestra•Swingin\' Serenades•Capitol Records•1960','\
no artist•I Love You•Mercury•1960','\
The Oscar Peterson Trio•Serenade In Blue•Clef Records•1955','\
The Oscar Peterson Trio•Serenade In Blue•Clef Records•1955','\
The Glenn Miller Orchestra•Serenade In Blue / Pennsylvania 6-5000•Epic•0','\
Erroll Garner Trio•The Greatest Garner•Atlantic•0','\
Glenn Miller And His Orchestra•Moonlight Cocktail•RCA Victor•1954','\
Ralph Marterie•Serenade In Blue / Sentimental Journey•United Artists Records•1973','\
Benny Goodman And His Orchestra•I\'ve Got A Gal In Kalamazoo / Serenade In Blue•Columbia•1942','\
Max Greger•In The Mood For Dancing•Karussell•0','\
Glenn Miller•Hommage à Glenn Miller Vol 1•Les Tréteaux•0','\
David Rose & His Orchestra•Serenades•MGM Records•1950'),'\
\
Serenade to a Cuckoo\
':('\
Roland Kirk•A Quote From Clifford Brown / Serenade To A Cuckoo•Limelight•1965','\
Roland Kirk•(I Eye Aye) - Live At The Montreux Jazz Festival Switzerland 1972•Rhino Records (2)•1996','\
Cargo (16)•Simple Things•Ringside•1970','\
Steve Turre•The Music Of Rahsaan Roland Kirk•Stash Records Inc.•1986','\
Chihiro Yamanaka•Lach Doch Mal•Verve Records•2006','\
Steve Turre•The Spirits Up Above•HighNote Records Inc.•2004','\
Jane Bunnett•The Water Is Wide•Evidence (5)•1994','\
Roland Kirk•Kirkatron•Warner Bros. Records•1977','\
Roland Kirk•Roland Kirk\'s Finest Hour•Verve Records•2001','\
Roland Kirk•I Talk With The Spirits•Limelight•1965','\
Roland Kirk•Simmer Reduce Garnish And Serve / The Warner Bros. Recordings•Warner Archives•1995','\
T.J. Kirk•T.J. Kirk•Warner Bros. Records•1995','\
Glenn Miller And His Orchestra•The Legendary Glenn Miller Vol.1•RCA•1976','\
Glenn Miller•The Complete Glenn Miller Vol. 1 1938-1939•RCA•1975'),'\
\
Serenade to a Soul Sister\
':('\
Horace Silver•Psychedelic Sally / Serenade To A Soul Sister•Blue Note•1968','\
The Horace Silver Quintet•Serenade To A Soul Sister•Blue Note•1968','\
Horace Silver•The Best Of Horace Silver Vol. II•Blue Note•1989','\
Missus Beastly•SWF-Session 1974•Long Hair•2012','\
Horace Silver•Horace Silver•Blue Note•1975','\
DJ Maestro•Blue Note Trip - Birds / Beats•Blue Note•2008','\
Coleman Hawkins•The Complete Recordings: 1929-1941•Affinity•1992','\
Various•Jazz Masters•Tandem Verlag Audio Line•0','\
Various•Jazz Musica Del Nostro Tempo•RCA•1969'),'\
\
Serenata\
':('\
Marina Occhiena•Serenata•Recordasterix•1982','\
Sarah Vaughan•Serenata / Let\'s•Roulette•1960','\
The Jazztet•Easy Living / Serenata•Argo (6)•0','\
Pete Jolly•Serenata•A&M Records•1968','\
Dinah Washington•Where Are You / Serenata•Roulette•0','\
Reggie Goff•Serenata / One Two Three A-Lairah•Decca•1950','\
Peter Kreuder•Ständchen / Serenata•Telestar•1939','\
Wayne King And His Orchestra•Evening Star•Victor•1940','\
The Ames Brothers•Stay / Piccolissima Serenata•RCA•1958','\
Harry James (2)•O Mein Papa (Oh! My Papa) / Serenata•Columbia•0','\
Tony Cucchiara•Annalisa•Sprint•1962','\
Winifred Atwell•Plink Plank Plunk / Serenata•Decca•1952'),'\
\
Serene\
':('\
Eric Dolphy•Unrealized Tapes•West Wind•1988','\
Eric Dolphy•Dash One•Prestige•1982','\
no artist•ONJQ - Live In Lisbon•Clean Feed•2006','\
Eric Dolphy•Naima•Jazzway•1987','\
Eric Dolphy•Out There•New Jazz•1961','\
Robert W. Brown (2)•Waterfall - Piano Solos•Nova Records (3)•1985','\
James Clay•A Double Dose Of Soul•Riverside Records•1960'),'\
\
Serenity\
':('\
John Coltrane•First Meditations (For Quartet)•ABC Records•1977','\
Steve Marcus•Something•Columbia•1971','\
Joe Henderson•An Evening With•Red Record•1987','\
Sam Rivers Quartet•"Crosscurrent" - Live At Jazz Unité•Blue Marge•1982','\
Joe Henderson•In \'N Out•Blue Note•1964','\
The Jazz Corps•The Jazz Corps•Pacific Jazz•1967','\
William Aura•Dreamer•Aura Communications•1984','\
David Liebman Ensemble•John Coltrane\'s Meditations•Arkadia Jazz•1997','\
Gambheera•Hidden Harmony•Nightingale Records•1991','\
Ernie Wilkins Almost Big Band•Ernie Wilkins\' Almost Bigband Live!  At Slukefter Jazz Club In Tivoli Gardens Copenhagen•Matrix Records (3)•1982'),'\
\
Seven Come Eleven\
':('\
Terry Gibbs•Seven Come Eleven / Imagination - Vol. 1•EmArcy•1957','\
Benny Goodman Sextet•Seven Come Eleven / Shivers•Columbia•1940','\
The Chateaus (2)•Moanin\' / Seven Come Eleven•Sound Stage 7•1964','\
Isao Suzuki Sextet•Ako\'s Dream•Three Blind Mice•1976','\
Tony Rand•Seven Come Eleven / Can\'t Be True - Or Can It•Columbia•0','\
Richard "Groove" Holmes•"Groove"•Pacific Jazz•1961','\
Barrett Deems Hottet•Deemus•Claremont•1978','\
The Oscar Peterson Trio•At JATP•Verve Records•1960','\
The Wilson-Norvo All Stars•Improvisations•Mercury•0','\
Gebhard Ullmann•Per-Dee-Doo•NABEL•1990','\
Louis Bellson•Don\'t Stop Now•Bosco•1984','\
Henry "Red" Allen And His Band•Battle Of Jazz Volume 6•Brunswick•1953','\
Barney Kessel•Live At The Jazz Mill 1954•Modern Harmonic•2016','\
Terry Gibbs•Terry Gibbs•EmArcy•1955','\
Various•The Concord Sound Volume One•Concord Jazz•1985','\
Herb Ellis•Seven Come Eleven (From Their Live Performance At The Concord Summer Festival)•Concord Jazz•1974','\
Lionel Hampton•Who\'s Who In Jazz Presents: Lionel Hampton With Dexter Gordon•no label•1977'),'\
\
Seven Steps to Heaven\
':('\
Miles Davis•Seven Steps To Heaven / Devil May Care•Columbia•0','\
Larry Young•Of Love And Peace•Blue Note•1966','\
Chet Baker•Four•Paddle Wheel•1989','\
The Miles Davis Quintet•Miles In St. Louis•VGM Records•1981','\
Peter King (2)•Hi Fly•Spotlite Records•1988','\
Miles Davis•Orbits•Columbia Musical Treasuries•1968','\
The Lynne Arriale Trio•Live•Motéma Music•2005','\
Miles Davis•No (More) Blues•Jazz Door•1991','\
no artist•Night Flight•Muse Records•1977','\
Francesco Cafiso Quartet•Seven Steps To Heaven•Venus Records (5)•2008','\
Lonnie Smith•Drives•Blue Note•1970','\
Victor Feldman•Your Smile•Choice (7)•1974'),'\
\
Shades of Light\
':('\
McCoy Tyner•Together•Milestone (4)•1979','\
Hubert Laws•My Time Will Come•MusicMasters Jazz•1993','\
Hubert Laws•Laws\' Cause•Atlantic•1969','\
Karyn Kydd•The Bridge•Not On Label•1994','\
The Jimmy Bruno Group•Midnight Blue•Concord Jazz•2001','\
Joni Mitchell•The Hissing Of Summer Lawns•Asylum Records•1975'),'\
\
Shadow Of Your Smile\
':('\
Eric Kloss•All Blues•Prestige•1966','\
Terumasa Hino•Swing Journal Jazz Workshop 1 - Terumasa Hino Concert•Takt Jazz Series•1969','\
The Glenn Miller Orchestra•The Shadow Of Your Smile / Hot Line•Epic•0','\
The Jet Set (10)•The Shadow Of Your Smile / Enchiladas•Amy•1966','\
Morris Nanton•Troubles Of The World / The Shadow Of Your Smile•Prestige•0','\
Boots Randolph•Yakety Sax / The Shadow Of Your Smile•Monument•1972','\
Kj Denhert•Album No. 9•MAT (2)•2010','\
Dexter Gordon•Jive Fernando•Chiaroscuro Records•1981','\
Pieces Of A Dream•Fo-Fi-Fo•Elektra•1983','\
Nancy Sinatra•Bang Bang / The Shadow Of Your Smile•Reprise Records•1966','\
Henry Jerome•Uptight (Everything\'s Alright) / The Shadow Of Your Smile•United Artists Records•1970','\
Hiroshi Fukumura•Live: First Flight•Trio Records•1973','\
J.R. Monterose•Live In Albany•Uptown Records (2)•1980','\
Wes Montgomery•Love Theme From "The Sandpiper" (The Shadow Of Your Smile) / Bumpin\' (Part II)•Verve Records•1965','\
Dexter Gordon•Have No Fear Dex Is Here•Mellotronen•2018','\
Boots Randolph•The Shadow Of Your Smile (Love Theme From "The Sandpiper")•Monument•1966'),'\
\
Shaker Song\
':('\
Spyro Gyra•Jubilee / Shaker Song•Infinity Records (2)•1979','\
Spyro Gyra•Shaker Song•Infinity Records (2)•1979','\
Spyro Gyra•Shaker Song / Paw Prints•Amherst Records•1978','\
Spyro Gyra•Live Concert Series•Infinity Records (2)•1979','\
Spyro Gyra•Spyro Gyra•Crosseyed Bear Productions•1977','\
Spyro Gyra•Access All Areas•MCA Records•1984'),'\
\
Shaw \'Nuff\
':('\
Dizzy Gillespie And His All Star Quintet•Shaw \'Nuff / Stupendous•Parlophon•1948','\
Dizzy Gillespie•Lover Man / Shaw \'Nuff•Guild Records (2)•1945','\
Freddie Hubbard•Back To Birdland•M & K Realtime Records•1981','\
Greg Osby•Public•Blue Note•2004','\
Al Haig•Reminiscence•Progressive Records (2)•1977','\
Charles McPherson•The Quintet/Live! (Recorded Live At The Five Spot)•Prestige•1967','\
Red Rodney•Red Rodney Returns•Argo (6)•1959','\
Curtis Lundy•Just Be Yourself•New Note•1987','\
Toshiyuki Miyama & The New Herd•Beat Generation•Paddle Wheel•1994'),'\
\
Shiny Stockings\
':('\
Billy Maxted•Satin Doll•Liberty•1967','\
Count Basie Orchestra•Count Basie And His Orchestra•Karusell•1957','\
Harry James And His Orchestra•Bess You Is My Woman / Shiny Stockings•MGM Records•1959','\
The Frank Foster Quintet•Chiquito Loco•Bingow Records•1979','\
Ella Fitzgerald•Into Each Life Some Rain Must Fall / Shiny Stockings•Verve Records•1964','\
Frank Foster And The Loud Minority•Shiny Stockings•Denon•1979','\
Elvin Jones•Heavy Sounds•Impulse!•1968','\
The Dave Bailey Quintet•2 Feet In The Gutter•Epic•1961','\
Dexter Gordon•Gettin\' Around•Blue Note•1966'),'\
\
Short Riff\
':('\
Charlie Parker•The Charlie Parker Story•Savoy Records•1956','\
Charlie Parker•Charlie Parker On Savoy Vol.1•Arista•1977','\
Karl Jenkins•Rubber Riff•Music De Wolfe•1976','\
Charlie Parker•Charlie Parker Memorial Vol. 2•Savoy Records•1955','\
Michael William Gilbert•I Can See From Here•Gibex•2010','\
Various•The Library Archive (Funk Jazz Beats And Soundtracks From The Vaults Of Cavendish Music)•BBE•2017','\
Various•Les Triomphes Du Blues•Habana•2001'),'\
\
Short Stop\
':('\
Various•The RCA Victor Encyclopedia Of Recorded Jazz: Album 10 - Ori To Rus•RCA Victor•1956','\
Shorty Rogers And His Orchestra•Cool And Crazy•RCA Victor•1953','\
Gene Ammons•Sock!•Prestige•1965','\
Shorty Rogers And His Giants•Re-Entry•Atlas Record (2)•1983','\
Adam Lane•4 Corners•Clean Feed•2007','\
Jens Fischer•Mad Material•Erdenklang•1989','\
Shorty Rogers And His Giants•The Big Shorty Rogers Express•RCA Victor•1956','\
Arve Henriksen•Composograph: A Synthesis Of Wood Metal And Electronics•Arve Music•2018','\
Gene Ammons•A Stranger In Town•Prestige•2002','\
Quite Sane•Child Of Troubled Times•CoolHunter Music•2002','\
TRPTS•Transforming Traditions•BlackHawk Records•1986','\
Ted Heath And His Orchestra•Ted Heath At The London Palladium Vol. 4•London Records•1955'),'\
\
Short Story\
':('\
Joe Henderson•In \'N Out•Blue Note•1964','\
Jerome Harris•In Passing•Muse Records•0','\
Googie Rene Combo•Wild Bird / The Chiller (A Very Short Story)•Class•1966','\
Kenny Dorham•Short Story•SteepleChase•1979','\
Francisco Aguabella•H2O•CuBop•1999','\
Canoneo•Desperately Seeking Fusion•Passport Jazz•1986','\
Buddy Collette And His Swinging Shepherds•Buddy Collette\'s Swinging Shepherds•EmArcy•1958','\
General Music Project•General Music Project•Evidence (5)•1997','\
Mikhail Alperin•Wave Of Sorrow•ECM Records•1990'),'\
\
Shutter Bug\
':('\
The J.J. Johnson Sextet•J.J. Inc.•Columbia•1961'),'\
\
Sidewinder\
':('\
Lee Morgan•The Sidewinder•Blue Note•1964','\
Bud Shank•Sidewinder•Pacific Jazz•1966','\
Kai Winding•The Sidewinder / Something You Got•Verve Records (2)•0','\
Lee Morgan•Blue Breakbeats•Blue Note•1998','\
Ray Charles And His Orchestra•Booty Butt / Sidewinder•Tangerine Records•1971','\
Lee Morgan•Lee Morgan•The Blue Note Label Group•2007','\
Woody Herman•Sidewinder / Greasy Sack Blues•Columbia•0','\
Shawn Elliott•Hello Heartache Goodbye Love / The Sidewinder•Roulette•1966','\
Lee Morgan•Jazz Profile: Lee Morgan•Blue Note•1997','\
Tamiko Jones•A Man And A Woman / Sidewinder•Atlantic•1966'),'\
\
Silver\'s Serenade\
':('\
Siegfried Kessler Trio•Invitation•Impro•1979','\
NY5•Music For Violin & Jazz Quartet•Jam (15)•1981','\
Louis Hayes•Serenade For Horace•Blue Note•2017','\
Ted Heath And His Music•Tequila•Decca•1958','\
David Hazeltine Trio•Senor Blues•Venus Records (5)•2000','\
Lawrence Welk And His Sparkling Strings•To Mother •Dot Records•0','\
Lonnie Smith•Too Damn Hot•Palmetto Records•2004','\
Tex Beneke And His Orchestra•Moonlight Serenade•RCA Camden•1959','\
Orchestra Werner Drexler•Don\'t Stop Now•Happy Records (6)•1976','\
Le Grand Orchestre De Paul Mauriat•Vole Vole Farandole•Philips•0','\
Lawrence Welk•75 Years Of Great American Music•Dot Records•1961','\
Paul Mauriat And His Orchestra•L.O.V.E.•Philips•1969','\
The Statler Dance Orchestra•For Your Party - Popular Dance Rythms•Stereo-Fidelity•1962','\
Horace Silver•The Hardbop Grandpop•Impulse!•1996','\
Orchester Frank Valdor•Moonlight - 12 Hits Im Original Glenn Miller Sound•Hippo Records (2)•0'),'\
\
Simone\
':('\
Elvin Jones•Live•PM•1975','\
Jutta Hipp And Her German Jazzmen•Jutta Hipp And Her German Jazzmen•MGM Records•0','\
Elvin Jones•Coalition•Blue Note•1971','\
Nobuo Hara and His Sharps & Flats•Giant Steps•King Records•1978','\
Emil De Waal•Ombud•Artiscope Music•2008','\
Sylvie Courvoisier Trio•D\'Agala•Intakt Records•2018','\
Léon Francioli•Chateauvallon 76•no label•1979','\
Bobby Few•More Or Less Few•Center Of The World•1973','\
ETC (10)•ETC•Red Record•1990','\
Frank Foster•Shiny Stockings•Sony•1998','\
Roland Kirk•Other Folks\' Music•Atlantic•1976','\
James Williams (2)•I Remember Clifford•DIW•1990','\
Lonnie Smith•Jungle Soul•Palmetto Records•2006','\
Haejin & Wouter•Wrong Distance•Dancing Butterfly Records•2016'),'\
\
Simple Samba\
':('\
George Robert Quartet•Live At The Q-4 Rheinfelden•TCB Records (2)•1991','\
Les Maniboulas•Tempo•Manibelle•0','\
Jim Hall•...Where Would I Be?•Milestone (4)•1972','\
Abraham Laboriel•Dear Friends•Bluemoon Recordings•1993','\
Marvin "Smitty" Smith•Keeper Of The Drums•Concord Jazz•1987','\
Buddy Montgomery•The Two-Sided Album•Milestone (4)•1968','\
Manfred Burzlaff Quartet•Jazz For Dancing•Elite Special•1965','\
Count Basie Orchestra•The Complete Roulette Studio Recordings Of Count Basie And His Orchestra•Mosaic Records (2)•1993','\
Bill Evans•The Complete Bill Evans On Verve•Verve Records•1997','\
Barbra Streisand•The Television Specials•Warner Music Vision•2005'),'\
\
Since I Fell For You\
':('\
Al Jarreau•Since I Fell For You•MCA Records•1986','\
Tommy Wills•Lost Dreams•Airtown Records•1968','\
The Ramsey Lewis Trio•The "In" Crowd•Argo (6)•1965','\
Louis Armstrong•Bostoner All Star Session•Brunswick•1952','\
Lee Morgan•Candy•Blue Note•1958','\
Brad Mehldau Trio•Blues and Ballads•Nonesuch•2016','\
Gene Ammons•Gene Ammons And Friends At Montreux•Prestige•1973','\
The Prestige Blues-Swingers•Stasch•Prestige Swingville•1960','\
Louis Armstrong And His All-Stars•Satchmo At Symphony Hall•Ace Of Hearts•0','\
Johnny Griffin•Bush Dance•Galaxy•1979','\
Louis Armstrong And His All-Stars•Satchmo At Symphony Hall (Volume 5)•Brunswick•1955','\
Stanley Turrentine•Blue Hour•Blue Note•1961'),'\
\
Since We Met\
':('\
The Bill Evans Trio•Since We Met•Fantasy•1976','\
Ken Peplowski•Encore•Concord Jazz•1995','\
Bill Evans•Eloquence•Fantasy•1982','\
Jean-Yves Thibaudet•Conversations With Bill Evans•Decca•1997','\
Tommy Emmanuel•Only•Original Works•2000','\
Chris Botti•A Thousand Kisses Deep•Columbia•2003','\
Bjarne "Liller" Pedersen•Til Enhver Tid•Storyville•1979','\
Various•Café Après-Midi ~ Vert•P-Vine Non Stop•2003','\
Tommy Emmanuel•The Great•Rajon Music Group•2004','\
Bill Evans•The Complete Fantasy Recordings•Fantasy•1989','\
Trijntje Oosterhuis•Collected•Universal Music•2015'),'\
\
Sing Me Softly of the Blues\
':('\
Karin Krog•Hi-Fly•Compendium Records•1976','\
Jean-Charles Capon•J.C. Capon R. Galliano G. Perrin•Productions Patrice Caratini•1982','\
Art Farmer Quartet•Sing Me Softly Of The Blues•Atlantic•1965','\
Swing Strings System•Swing Strings System•Uniteledis•1978','\
John McLaughlin•After The Rain•Verve Records•1995','\
Steve Kuhn Trio•Sing Me Softly Of The Blues•Venus Records (5)•1997','\
Volker Kriegel & Mild Maniac Orchestra•Elastic Menu•MPS Records•1978','\
Gary Burton Quartet•Duster•RCA Victor•1967','\
Carla Bley•Dinner Music•WATT Works•1977','\
Volker Kriegel & Mild Maniac Orchestra•Elastic Menu•MPS Records•1978','\
The Mike Gibbs Band•Just Ahead•Polydor•1972','\
Morrissey Mullen•Up•Embryo Records•1977'),'\
\
Sippin\' at Bell\'s\
':('\
Roy Haynes Group•When It\'s Haynes It Roars!•Disques Dreyfus•1992','\
Miles Davis•My Old Flame•Le Monde•2009'),'\
\
Sister Sadie\
':('\
Shirley Scott•Sister Sadie•Prestige•1962','\
The Lou Bennett Quartet•Amen•RCA Victor•1965','\
The Horace Silver Quintet•Sister Sadie / Break City•Blue Note•1959','\
Buddy Rich•Uptight (Everything\'s Alright) / Sister Sadie•Pacific Jazz•1966','\
Shirley Scott•Plays Horace Silver•Prestige•1962','\
The Lou Bennett Quartet•Amen•RCA•1960','\
Dieter Reith•Open Drive•Center•1968','\
Horace Silver•The Best Of Horace Silver•Blue Note•1969','\
Larry Coryell•The Larry Coryell / Michael Urbaniak Duo•Keytone•1982','\
Various•The Compositions Of Horace Silver•Riverside Records•1962','\
The Red Bahnik Trio•Goes To Santander•Sonorama•2016','\
Various•This Is Blue Note Jazz•Blue Note•1969','\
Hank Crawford•More Soul•Atlantic•1961','\
Woody Herman•I Giganti Del Jazz Vol. 49•Curcio•0','\
Manhattan Jazz Quintet•Funky Strut•Sweet Basil (2)•1991'),'\
\
Skating In Central Park\
':('\
The Modern Jazz Quartet•Skating In Central Park / Cue No. 9•United Artists Records•1961','\
Francis Lai•Theme From Love Story•Paramount Records•1971','\
Francis Lai And His Orchestra•Theme From Love Story•Paramount Records•1971','\
Vibes Summit•Vibes Summit•MPS Records•1979','\
Joe Carter Quartet•My Foolish Heart•Empathy Records•1985','\
Bill Evans•Undercurrent•United Artists Records•1962','\
Kjell Öhman•Organ Jazz With Kjell Öhman•Discofon (2)•1968'),'\
\
Skippy-ing\
':('\
no artist•Locomotive•Soul Note•1988','\
Miles Okazaki•Work Volumes 1-6  (The Complete Compositions Of Thelonious Monk)•Not On Label (Miles Okazaki Self-released)•2018','\
Alexander von Schlippenbach•Monk\'s Casino•Intakt Records•2005','\
Frank Kimbrough•Monk\'s Dreams: The Complete Compositions Of Thelonious Sphere Monk•Sunnyside•2018'),'\
\
Skylark\
':('\
Earl Hines And His Orchestra•Water Boy / Skylark•RCA Victor•1948','\
Harry James And His Orchestra•Skylark / The Clipper•Columbia•1942','\
Franco Ambrosetti•Franco Ambrosetti & Don Sebesky•Dire (2)•1980','\
Dexter Gordon Quartet•Biting The Apple•SteepleChase•1977','\
Jim Hall•Youkali•CTI Records•1992','\
Glenn Miller And His Orchestra•The Story Of A Starry Night / Skylark•Bluebird (3)•1942','\
David "Fathead" Newman•Straight Ahead •Atlantic•1961','\
The Urbie Green Septet•New Faces - New Sounds•Blue Note•1953'),'\
\
Sleeping Bee\
':('\
The Bill Evans Trio•Quiet Now•Affinity•1986','\
Bill Evans•Autumn Leaves•International Joker Production•1977','\
Art Farmer•A Sleeping Bee•Grammofonverket•1974','\
Oscar Peterson•Oscar Peterson & Nelson Riddle•Verve Records•1963','\
Various•The Progressive Records All Star Trumpet Spectacular•Progressive Records (2)•1979','\
Billy Taylor Trio•Sleeping Bee•MPS Records•1969','\
George Cables Trio•Sleeping Bee•Atlas Record (2)•1983','\
J.J. Johnson•J.J.\'s Broadway•Verve Records•1963','\
Bill Evans•Trio 64•Verve Records•1964','\
Harold Mabern Trio•Somewhere Over The Rainbow - Harold Plays Arlen•Venus Records (5)•2007','\
Bill Evans•At The Montreux Jazz Festival•Verve Records•1968'),'\
\
Slipped Disc\
':('\
The Benny Goodman Quintet•Liza•Philips•0','\
Benny Goodman Sextet•Slipped Disc / I Got Rhythm•Parlophone•1946','\
Benny Goodman Sextet•Slipped Disc / Oomph Fah Fah•Columbia•1945','\
Benny Goodman•The Benny Goodman Story•Brunswick•1962','\
Benny Goodman And His Orchestra•The Benny Goodman Story Volume 1 Part 3•Brunswick•1956','\
Benny Goodman Combos•Famous Goodman Dates No.1•Philips•0','\
Swing Kvartet•Mini Jazz Klub 12•Panton•1977','\
Benny Goodman•Yale Archives•PolyGram Nederland B.V.•1993','\
Benny Goodman•The Benny Goodman Story Part 2•Decca•1956','\
Benny Goodman Septet•Stompin\' At The Savoy•Mercury•0','\
EM Swingin Oil Drops•Like A Drop Of Oil•CBS•1966','\
Benny Goodman•1945•CBS•1972','\
Benny Goodman•The Benny Goodman Yale Archives Volume 1•Musicmasters•1988','\
Roy Lanham•Sizzling Strings•National Recording Corporation•2005','\
Benny Goodman•Benny Goodman Combos•Columbia•1951','\
Eddie Daniels•Benny Rides Again•GRP•1992','\
Benny Goodman•Basel 1959•TCB Records (2)•1996','\
Benny Goodman•Benny Goodman\'s Greatest Hits•Columbia•1966'),'\
\
Sliver\'s Serenade\
':('\
Various•WCBS-FM 101.1 The Ultimate Christmas Album•Collectables•1994'),'\
\
Slow Hot Wind\
':('\
no artist•Constant Rain (Chove Chuva)•A&M Records•1966','\
Gerry Niewood•The Gerry Niewood Album•Sagoma•1975','\
Gerry Niewood•The Gerry Niewood Album•Sagoma•1975','\
Gerry Niewood•Slow Hot Wind•A&M Records•1975','\
Henry Mancini And His Orchestra•Symphonic Soul•RCA Victor•1975','\
Lucia Cadotsch•Speak Low•Yellowbird•2016','\
Benjamin Herman•Trouble•Music On Vinyl•2014','\
Eri Ohno•Eri My Dear•Better Days (2)•1982','\
Steve Kuhn Trio•Live At Birdland•Blue Note•2007','\
Eric Kloss•Grits & Gravy•Prestige•1967','\
Marc Hunter•Night & Day•ABC Records (3)•1990','\
James Moody•Moody Plays Mancini•Warner Bros. Records•1997'),'\
\
Small Day Tomorrow\
':('\
Janis Siegel•Small Day Tomorrow•Atlantic•1987','\
Jamie Cullum•Devil May Care!•Candid•2010','\
Paul Winter And Friends•Collection II•Living Music•1987','\
Irene Kral•Kral Space•Catalyst Records (3)•1977','\
Janis Siegel•At Home•Atlantic•1987','\
Nellie McKay•Sister Orchid•Palmetto Records•2018','\
Bob Dorough•Beginning To See The Light•Laissez-Faire (2)•1976','\
Lee Aaron•Slick Chick•Barking Dog Music•2000','\
no artist•Another Time•Sunnyside•1981','\
Sting•Greatest Hits•Star Mark•2008','\
Larry Elgart And His Manhattan Swing Orchestra•Hooked On Swing•RCA•1982'),'\
\
Smile Please\
':('\
Jake Mason Trio•The Stranger In The Mirror•no label•2018','\
Sammy Davis Jr.•Featuring Sammy Davis Jr.•Capitol Records•1954','\
Mike Mainieri•Love Play•Arista•1977','\
Trudy Pitts•A Bucketful Of Soul•Prestige•1968','\
Ted Heath And His Music•Ted Heath Recalls The Fabulous Dorseys•Decca Eclipse•1957','\
Alex Welsh & His Band•At Home With...Alex Welsh And His Band•Columbia•1968','\
The Bay Big Band•The Brussels World\'s Fair Salutes Tommy Dorsey Orchestra•Omega Records (13)•0','\
Maximilian Geller Quartet•Smile•Edition Collage•1993','\
Members Of the Tommy Dorsey Orchestra•A Salute ToTommy Dorsey•Crown Records (2)•1960','\
Zacharias-Swingtett•Swing Is In•HÖR ZU•1976','\
Members Of The Tommy Dorsey Orchestra•The Stereophonic Sound Of Tommy Dorsey•Bright Orange•0','\
Shakatak•Perfect Smile•Verve Forecast•1990','\
The Great Jazz Trio•Flowers For Lady Day•Evidence (5)•1996'),'\
\
Smoke Gets In Your Eyes\
':('\
Patti Austin•Smoke Gets In Your Eyes•Qwest Records•1988','\
Earl Bostic And His Orchestra•Moonglow / Smoke Gets\' In Your Eyes•King Records (3)•0','\
Teddy Wilson•Smoke Gets In Your Eyes / Them There Eyes•Columbia•0','\
Don Byas Quartet•Smoke Gets In Your Eyes / Slamboree•Arista (3)•0','\
Earl Bostic And His Orchestra•Smoke Gets In Your Eyes•Parlophone•1955','\
Freddy Gardner•Smoke Gets In Your Eyes / Stardust•Regal Zonophone•1940','\
Frank Foster•We See•Metronome•1957','\
Jeri Southern•Smoke Gets In Your Eyes / Fire Down Below•Brunswick•1957','\
Earl Bostic And His Orchestra•Smoke Gets In Your Eyes / For You•King Records (3)•1952','\
Al Smith•Smoke Gets In Your Eyes / Slow Mood•Chance Records (3)•1952','\
Tommy Dorsey And His Orchestra•Night And Day / Smoke Gets In Your Eyes•Victor•0','\
The Thelonious Monk Quintet•Thelonious Monk Quintet•Prestige•1954','\
The Platters•The Great Pretender•Musicor Records•1973','\
Leo Parker•The Late Great King Of The Baritone Sax•Chess•1971','\
"Philly" Joe Jones•Advance!•Galaxy•1979','\
Paul Whiteman And His Orchestra•Smoke Gets In Your Eyes / Something Had To Happen•Victor•1933'),'\
\
So In Love\
':('\
Harry James And His Orchestra•Ciribiribin (They\'re So In Love) / Avalon•Columbia•1939','\
Dick Jurgens And His Orchestra•You’d Be So Nice To Come Home To / I’m So So So So So In Love•Columbia•1943','\
Illinois Jacquet•So In Love•Argo (6)•1965','\
Harry James And His Orchestra•Ciribiribin (They\'re So In Love) / Concerto For Trumpet•Columbia•1954','\
New York Trio•Begin The Beguine•Venus Records (5)•2006','\
Harry James And His Orchestra•Ciribiribin (They\'re So In Love) / The Mole•Columbia•0','\
Søren Kjærgaard Trio•Amfebia•ILK Music•2005','\
Bob Rockwell Trio•The Bob Rockwell Trio•SteepleChase•1989','\
Georgia Gibbs•So Madly In Love / Kiss Of Fire•Metronome•1952','\
The International Pop Orchestra•Cole Porter Favorites•Wyncote•1964','\
Jan Garber And His Orchestra•So Madly In Love / Some Day•Capitol Records•0','\
Keith Jarrett•Standards Vol. 2•ECM Records•1985','\
Tethered Moon•Tethered Moon•King Records•1992','\
Ella Fitzgerald•Hotta Chocholata / So In Love•Barclay•0','\
Harold Land•Eastward Ho! Harold Land In New York•JAZZLAND•1960','\
Art Pepper•So In Love•Artists House•1980','\
Corky Hale•So Much In Love / Roof Garden•Affinity•1986','\
George Siravo And His Orchestra•Everything Goes! The Music Of Cole Porter•Epic•1961','\
Herb Alpert•Yo Soy Ese Amor (This Guy\'s In Love With You) / Love So Fine•A&M Records•1968','\
George Benson•Inside Love (So Personal)•Warner Bros. Records•1983'),'\
\
So Many Stars\
':('\
no artist•The Fool On The Hill / So Many Stars•A&M Records•1968','\
Jackie & Roy•Star Sounds•Concord Jazz•1980','\
Jimmy Ponder•So Many Stars•Milestone (4)•1985','\
Jane Monheit•Surrender•Concord Records•2007','\
Manhattan Trinity•Love Letters•M & I•2001','\
Helen Merrill•Casa Forte•Trio Records•1980','\
no artist•Night And Day•A&M Records•1971','\
Sarah Vaughan•Brazilian Romance•CBS•1987','\
Roelof Stalknecht•Zoals Altijd ...•Nova Zembla Records•1987','\
Joanne Brackeen•Breath Of Brazil•Concord Picante•1991'),'\
\
So Near So Far\
':('\
Oscar Peterson•Oscar Peterson Plays Cole Porter•Mercury•1953','\
Joe Henderson•So Near So Far (Musings For Miles)•Verve Records•1993','\
Air Craft•So Near So Far•Fantasy Records•1985','\
Miles Davis•Jazz Moods - Cool•Columbia•2004','\
Marilyn Crispell Trio•Storyteller•ECM Records•2004','\
Michael Sagmeister•So Near So Far•L+R Records•1987','\
Miles Davis•Playlist: The Very Best Of Miles Davis•Columbia•2008','\
Miles Davis•Seven Steps To Heaven•Columbia•1963'),'\
\
So Nice (Summer Samba)\
':('\
Walter Wanderley•Summer Samba (So Nice) / Call Me•Verve Records•1966','\
Bud Shank•Summer Samba / Monday Monday•World Pacific Records•1966','\
Bebel Gilberto•Tanto Tempo•EastWest•2003','\
Bebel Gilberto•Tanto Tempo•Ziriguiboom•2000','\
Caiola Combo•All Strung Out•United Artists Records•1966','\
The Don Scaletta Trio•Sunday Afternoon At The Trident•Verve Records•1967','\
Yasuko Agawa•Meu Romance•Victor•2008','\
Trombones Unlimited•You\'re Gonna Hear From Me (Us!)•Liberty•1966','\
Bud Shank•Brazil! Brazil! Brazil!•World Pacific Records•1966','\
Kazuo Yashiro•Love Is Here To Stay•Takt Jazz Series•1968'),'\
\
So What\
':('\
Miles Davis•So What•DOL•2013','\
The Miles Davis Quintet•The Legendary 1960 European Tour•Jazz Plot Records•2011','\
Miles Davis•On Green Dolphin Street•Jazz Door•1992','\
The Monday Night Orchestra•Playing The Music Of Gil Evans Live At Sweet Basi•Apollon•1993','\
Various•Newport In New York \'72 - The Jam Sessions Vol 4•Atlantic•1972','\
All Stars After Hours•Night Jam Session In Warsaw 1973•Polskie Nagrania Muza•1973','\
Miles Davis•Miles In Berlin•CBS•1967','\
no artist•It Ain\'t Necessarily So / Guess What•Mercury•1952','\
Miles Davis•The Final Tour (The Bootleg Series Vol. 6)•Columbia•2018','\
Miles Davis•Heard \'Round The World•CBS•1983','\
George Russell•So What•Blue Note•1986','\
Takashi Mizuhashi Quartet•Live In "5 Days In Jazz 1974" - When A Man Loves A Woman•Three Blind Mice•1974'),'\
\
Softly as a Morning Sunrise\
':('\
Artie Shaw And His Orchestra•Softly As In A Morning Sunrise / Rosalie•RCA Victor•0','\
The Modern Jazz Quartet•Softly As In A Morning Sunrise•Music•0','\
Artie Shaw And His Orchestra•Softly As In A Morning Sunrise / Copenhagen•Bluebird (3)•1938','\
Takeo Moriyama Quartet•Flush Up•Teichiku Records•1977','\
Al Goodman And His Orchestra•Tico Tico / Softly As In A Morning Sunrise•Victor•1946','\
no artist•Beyond Standard•Telarc•2008','\
John Coltrane•"Live" At The Village Vanguard•Impulse!•1962'),'\
\
Softly As In A Morning Sunrise\
':('\
Artie Shaw And His Orchestra•Softly As In A Morning Sunrise / Rosalie•RCA Victor•0','\
The Modern Jazz Quartet•Softly As In A Morning Sunrise•Music•0','\
Artie Shaw And His Orchestra•Softly As In A Morning Sunrise / Copenhagen•Bluebird (3)•1938','\
Takeo Moriyama Quartet•Flush Up•Teichiku Records•1977','\
Al Goodman And His Orchestra•Tico Tico / Softly As In A Morning Sunrise•Victor•1946','\
no artist•Beyond Standard•Telarc•2008','\
John Coltrane•"Live" At The Village Vanguard•Impulse!•1962','\
John Scofield•Live•ENJA Records•1978'),'\
\
Solar\
':('\
The Sun Ra Arkestra•Secrets Of The Sun•El Saturn Records•1965','\
Chet Baker•Star Eyes•Marshmallow (3)•1990','\
Slide Hampton Quintet•Roots•Criss Cross Jazz•1985','\
All Stars After Hours•Night Jam Session In Warsaw 1973•Polskie Nagrania Muza•1973','\
Quintet  René Urtreger•En Direct D\'Antibes•Carlyne Music•1980','\
Ex-Wise Heads•Celestial Disclosure•Tonefloat•2007','\
Martial Solal•Duo In Paris•Musica Records•1975','\
Ray Manzarek•Solar Boat•Mercury•1974','\
Charlie Haden•The Montréal Tapes•Verve Records•1998','\
Johnny Almond Music Machine•Solar Level•Deram•1969','\
The J.J. Johnson Quintet•Jazz Gallery•Philips•0','\
Keith Jarrett / Gary Peacock / Jack DeJohnette•Somewhere•ECM Records•2013','\
Clare Fischer & Salsa Picante•Crazy Bird•Discovery Records•1985','\
Ben Wendel•What We Bring•Motéma•2016'),'\
\
Solitude\
':('\
Meade "Lux" Lewis•Melancholy / Solitude•Blue Note•1939','\
Duke Ellington And His Orchestra•Caravan / Solitude•RCA•0','\
Jimmie Lunceford And His Orchestra•Stratosphere / Solitude•Decca•1934','\
Duke Ellington And His Orchestra•Solitude / Moon Glow•Brunswick•1934','\
Duke Ellington And His Cotton Club Orchestra•Black Beauty / Solitude•La Voix De Son Maître•0','\
Duke Ellington And His Orchestra•Mood Indigo / Solitude•Columbia•0','\
Duke Ellington And His Orchestra•Solitude / Black Beauty•no label•1951','\
Duke Ellington And His Orchestra•Solitude / Delta Serenade•Victor•1934','\
Duke Ellington And His Orchestra•Solitude / Troubled Waters•no label•1936','\
Duke Ellington And His Orchestra•Solitude / Mood Indigo•Columbia•1940','\
Jimmie Lunceford And His Orchestra•Black And Tan Fantasy / Solitude•Brunswick•0'),'\
\
Some Other Blues\
':('\
Tony Coe•With Brian Lemon Trio•77 Records•1971','\
Dexter Gordon•Blues A La Suisse•Prestige•1974','\
OYEZ (2)•I Mean You•Timeless Records (3)•1988','\
Various•Jazz Na Koncertnom Podiju Vol. 1•Jugoton•1977','\
Akira Toyoda•Benkei•Sound Design Records•1984','\
Tete Montoliu Trio•Tootie\'s Tempo•SteepleChase•1979','\
Teruo Nakamura•Unicorn•Three Blind Mice•1973','\
Space Jazz Trio•Meridies•Gala Records (4)•1988','\
Eraldo Volonté•My Point Of View•Durium•1963','\
John Coltrane•Coltrane Jazz•Atlantic•1961','\
Dave Hubbard•Dave Hubbard•Mainstream Records•1971'),'\
\
Some Other Time\
':('\
John Hicks•In Concert•Theresa Records•1986','\
Richard Beirach•Continuum•Eastwind•1984','\
Jackie McLean & The Cosmic Brotherhood•New York Calling•SteepleChase•1975','\
Floyd Morris•Some Other Time / So Nice \'N So Easy•Philips•0','\
Art Farmer•Homecoming•Mainstream Records•1971','\
Bill Evans•How Deep Is The Ocean?•Heart Note Records•1988','\
Houston Person•Basics•Muse Records•1989','\
Space Jazz Trio•Meridies•Gala Records (4)•1988','\
David Liebman / Richard Beirach•Double Edge•Storyville•1985','\
The Bill Evans Trio•Waltz For Debby•Riverside Records•1962','\
Larry Coryell•Quartet - Dedicated To Bill Evans And Scott La Faro•Jazzpoint Records•1987'),'\
\
Some Skunk Funk\
':('\
Yoichi Murata Solid Brass•Tribute To The Brecker Brothers•Platinum (5)•2008','\
The Brecker Brothers•East River•Arista•1978','\
The Brecker Brothers•Live•Jazz Door•1994','\
The Brecker Brothers•Heavy Metal Be-Bop•Arista•1978','\
The Brecker Brothers•Return Of The Brecker Brothers – Live In Barcelona•GRP Video•1992','\
The Brecker Brothers•The Brecker Bros.•Arista•1975','\
Randy Brecker•Some Skunk Funk - Live At Leverkusener Jazztage•BHM Productions•2006','\
Randy Brecker•Some Skunk Funk - Live At Leverkusener Jazztage•Telarc•2005','\
Yoichi Murata Solid Brass•Double Edge•JVC•1996'),'\
\
Somebody Love Me\
':('\
Frankie Carle•Frankie Carle Encores•Columbia•0','\
Don Byas And His Orchestra•3•Barclay•0','\
Bob Tracy His Strings And His Big Band•Dancing To Gershwin•Concert Hall•1969','\
Jack Teagarden•Jazz Makers•Mercury•0','\
Michael Dunn And His Orchestra•Dancing To Gershwin•Varieton•1954','\
Maynard Ferguson•Hollywood Jam Sessions•Fresh Sound Records•2005','\
Elmo Hope•Last Sessions Vol. 2•Inner City Records•1977','\
Khani Cole•Places•Fahrenheit Records•1998','\
Wayne Newton•Showstoppers•CEMA Special Markets•1991','\
Frankie Lymon•Frankie Lymon At The London Palladium•Roulette•1958','\
Charles Pasi•Bricks•Blue Note•2017','\
Zoot Sims•Cookin\'!•Fontana•1965','\
Joe "Fingers" Carr•Class Of \'25•Capitol Records•0','\
Eddy Duchin•Chopin Nocturne In E-Flat•Columbia•0','\
George Gershwin•The Music Of George Gershwin (Summertime)•Spectrum•1975','\
Earl Hines•Earl Meets Harry•Black And Blue•1978','\
Frank Sinatra•El Mundo De Frank Sinatra•Caudal•0','\
Danuta Błażejczyk•Gershwin: Summertime•Agencja Artystyczna MTJ•2005'),'\
\
Someday My Prince Will Come\
':('\
Oscar Peterson•Come Sunday•Verve Records•1963','\
Etta Jones•Someday My Prince Will Come•Prestige•0','\
Herbie Hancock•Herbie Hancock And Chick Corea•CBS/Sony•1981','\
Pallarols Duo•Pallarols Duo•Not On Label (Pallarols Duo Self-released)•2018','\
Miles Davis•The Essence Of Miles Davis•Legacy•1991','\
Herbie Hancock•An Evening With Herbie Hancock & Chick Corea In Concert•CBS•1978','\
Chet Baker Trio•Someday My Prince Will Come•SteepleChase•1983','\
Miles Davis•Someday My Prince Will Come•Columbia•1990'),'\
\
Someone to Light Up My Life\
':('\
Kenny Burrell•Groovin\' High•Muse Records•1984','\
Mark Murphy•Brazil Song - Cancoes Do Brasil•Muse Records•1984','\
Ray Warleigh•Ray Warleigh\'s First Album•Philips•1969','\
Shirley Horn•Loving You•Verve Records•1997','\
Chicago Jazz Exhange•Chicago Jazz Exchange With Elaine Hamilton•Siege Records (2)•1982','\
Eddie Higgins•Portrait In Black And White•Sunnyside•1996','\
The Singers Unlimited•A Capella III•MPS Records•0','\
Simone Kopmajer•Romance•Venus Records (5)•2004','\
Nancy Ames•Spiced With Brasil•Epic•1967','\
Scott Walker•Scott - Scott Walker Sings Songs From His T.V. Series•Philips•1969','\
Various•Patterns In Sound•Project 3 Total Sound•1966','\
Enoch Light And The Light Brigade•Spanish Strings•Project 3 Total Sound•1966'),'\
\
Someone To Watch Over Me\
':('\
Erroll Garner•Tenderly / Someone To Watch Over Me•Modern Records (2)•1949','\
Frank Sinatra•Someone To Watch Over Me / Paradise•Columbia•1946','\
Tab Smith Orchestra•Soft Breeze / Someone To Watch Over Me•United (2)•1957','\
Buddy DeFranco•Buddy De Franco And Oscar Peterson Play George Gershwin•Karusell•1955','\
John W. Bubbles•Bubbles Blues / Someone To Watch Over Me•Vee Jay Records•1964','\
Art Tatum•Sounds Of Jazz No. 1•Fontana•0','\
Tete Montoliu•Volumen 1 •Saef•1958','\
Art Tatum•Sounds Of Jazz No. 1•Fontana•0','\
Donald Byrd•Timeless•Savoy Jazz•2002','\
Ray Conniff•Spielt Für Verliebte S\'Wonderful•Philips•0','\
John Dennis (2)•New Piano Expressions•Debut Records•1955','\
Ella Fitzgerald•Ella Fitzgerald Sings Gershwin No.2•Verve Records•1962','\
Donald Byrd•Byrd\'s Word•Savoy Records•1956','\
Knud Jörgensen•I Got Rhythm•Metronome•0','\
Ella Fitzgerald•Ella Sings Gershwin - Volume 1•Brunswick•1955'),'\
\
Something To Talk About\
':('\
Blossom Dearie•My Gentleman Friend•Verve Records•1959','\
John Coltrane•Plays Ballads•Midnight Records (11)•2010','\
Burt Bacharach•Plays His Hits•Kapp Records•1966','\
Burt Bacharach•The Best Of Burt Bacharach•MCA Records•1972','\
Ann Margret•Let Me Entertain You•RCA•1996','\
Various•Sunny Side Up 2•EMI Austria•2002','\
Joe "Mr Piano" Henderson•Joe "Mr Piano" Henderson With Geoff Love & His Orchestra And The Williams Singers•Parlophone•1961','\
Various•Russ Meyer\'s Original Motion Picture Soundtracks: Mudhoney Finders Keepers Lovers Weepers MotorPsycho•Q.D.K. Media•1995','\
Louis Armstrong And His All-Stars•Louis Armstrong And His All-Stars•Joker (2)•1976','\
Various•Flappers Vamps And Sweet Young Things•ASV•1982','\
John Coltrane•Coltrane \'58: The Prestige Recordings•Craft Recordings•2019'),'\
\
Sometime Ago\
':('\
Giorgio Azzolini•Tribute To Someone•Ciao! Ragazzi•1964','\
Gerry Mulligan•Something Borrowed - Something Blue•Limelight•1966','\
Lee Konitz•Satori•Milestone (4)•1975'),'\
\
Sometimes I\'m Happy\
':('\
Kimiko Itoh•Jazzdaga? Jazzdaja!•PM Music (7)•2007','\
Lee Konitz Nonet•Lee Konitz Nonet•Chiaroscuro Records•1977','\
Teddy Wilson•The Touch Of Teddy Wilson•Verve Records•1957','\
Sarah Vaughan•Sarah Vaughan•Mercury•1987','\
Patrice Munsel•Unpredictable•Philips•1962','\
Sun Ra•Singles (The Definitive 45\'s Collection 1952–1991)•Strut•2016','\
Sun Ra•Singles (The Definitive 45\'s Collection 1952–1991)•Strut•2016','\
Joe Loss & His Orchestra•Party Dance Time No. 2•no label•1961','\
Oliver Nelson•The Argo Verve And Impulse Big Band Studio Sessions•Mosaic Records (2)•2006'),'\
\
Son of Mr. Green Genes\
':('\
Frank Zappa•Brooklyn & Elsewhere•Rubber Dubber Records (2)•2012','\
Frank Zappa•"Instrumental & Improvisations"•NQ•2006','\
Frank Zappa•Hot Rats•Bizarre Records•1969'),'\
\
Song\
':('\
Muhal Richard Abrams•Spiral: Live At Montreux 1978•Novus•1978','\
Byard Lancaster Trio•Byard Lancaster Trio•Soutrane Recording Company•2000','\
Paul Horn•Inside Russia•Attic•1984','\
Jim Black Trio•The Constant•Intakt Records•2016','\
Trygve Seim•Helsinki Songs•ECM Records•2018','\
Graham Collier Music•Songs For My Father•Fontana•1970','\
Tethered Moon•Play Kurt Weill•JMT•1995','\
The Australian Jazz Quintet•Modern Jazz Performance Of Kurt Weill\'s Three Penny Opera•Bethlehem Records•1958','\
Gary Burton / Chick Corea•Live In Tokyo•Pioneer Artists•1981','\
Gary Burton / Chick Corea•Duet•ECM Records•1979','\
Tethered Moon•Play Kurt Weill•JMT•1995','\
Joseph Jarman•Poem Song (Joy In The Universe)•Bopbuda Music•0','\
The Dave Brubeck Quartet•The Trolley Song•Fantasy•1954','\
Kenneth McKellar•Lewis Bridal Song / Skye Boat Song•Decca•0'),'\
\
Song for Bilbao\
':('\
Michael Brecker•Tales From The Hudson•Impulse!•1996','\
Various•Back To The Basics•Impulse!•1996','\
Pat Metheny Group•Travels•ECM Records•1983','\
Pat Metheny Group•Speaking Of Now Live•Eagle Vision•2003','\
Vincent Lopez And His Orchestra•Dance Along With Lopez•MGM Records•1961'),'\
\
Song for Lorraine\
':('\
Spyro Gyra•Morning Dance•Infinity Records (2)•1979','\
Spyro Gyra•Shaker Song•Infinity Records (2)•1979','\
Spyro Gyra•Morning Dance•Infinity Records (2)•1979'),'\
\
Song For My Father\
':('\
The Horace Silver Quintet•Song For My Father•Blue Note•1965','\
The Horace Silver Quintet•Song For My Father•Blue Note•1965','\
Richard "Groove" Holmes•Soul Message•Prestige•1965','\
Joe Lee Wilson•Shout For Trane•Trio Records•1976','\
The Seven•Tell Her No•Thunderbird Records•1970','\
Larry Coryell•The Larry Coryell / Michael Urbaniak Duo•Keytone•1982','\
Richard "Groove" Holmes•Onsaya Joy•Flying Dutchman•1975','\
The Claude Williamson Trio•Song For My Father•Venus Records (5)•2009','\
Fitz Gore & The Talismen•Fitz Gore & The Talismen•Plastic Strip•2009','\
Cindy Horstman & Friends•Out Of The Blue•North Star Music•1997','\
Horace Silver•Jazz Profile: Horace Silver•Blue Note•1997','\
Don "Sugarcane" Harris•Sugar Cane\'s Got The Blues•MPS Records•1972','\
Richard "Groove" Holmes•Soul Message•Prestige•1965','\
The Horace Silver Quintet•Song For My Father (Cantiga Para Meu Pai)•Blue Note•1964','\
Jamey Aebersold•Horace Silver - Eight Jazz Classics:  Volume 17•JA Records•1978'),'\
\
Song for My Lady\
':('\
Bernie McGann Quartet•Kindred Spirits•Emanem•1987','\
Joe Lee Wilson•Shout For Trane•Trio Records•1976','\
McCoy Tyner•Song For My Lady•Milestone (4)•1973','\
Coalition (4)•Birth•Kenya Records•1978','\
McCoy Tyner•The Best Of McCoy Tyner•Blue Note•1996','\
Λάκης Ζώης•Esoteric•Eros Music•1992','\
Kim Waters•Sax Appeal•Warlock Records•1991','\
Grażyna Auguścik•Sunrise Sunset•Polskie Nagrania Muza•1988','\
Erik Söderlind•Happening•Prophone•2011','\
James Morrison•A Night In Tunisia•ABC Records (3)•1984','\
Freddie Hubbard•MMTC: (Monk Miles Trane & Cannon)•MusicMasters Jazz•1995','\
Wayne Johnson Trio•Spirit Of The Dancer•Zebra Records•1988','\
Phil Woods•Here\'s To My Lady•Chesky Records•1989','\
The Charles Lloyd Quartet•Of Course Of Course•Columbia•1966','\
Various•Jazz aus dem Grand Hotel•The Fab Records•0'),'\
\
Song Is You\
':('\
Lee Konitz•Lone-Lee•SteepleChase•1975','\
Yoshiaki Masuo•The Song Is You And Me•Electric Bird•1980','\
Keely Smith•S\'posin\'•Capitol Records•1965','\
Joe Holiday Quartet•I Told You So / The Song Is You•Federal (5)•1951','\
Cynara (2)•Cynara•Capitol Records•1970','\
James Williams (2)•James Williams Meets The Saxophone Masters•Columbia•1992','\
Stan Getz•It Might As Well Be Spring / The Song Is You•Royal Roost•1951','\
Anthony Braxton•Trio And Duet•Sackville Recordings•1974','\
Lee Konitz•Alone Together•Blue Note•1997','\
Stan Getz Quintet•Jazz At Storyville•Royal Roost•1952','\
Joanne Grauer Trio•Joanne Grauer Trio•Mode Records•1957','\
Mike Campbell (2)•Secret Fantasy•Palo Alto Records•1982','\
Frank Sinatra•Frank Sings Jerome Kern•Columbia•1953','\
Tommy Dorsey And His Orchestra•(I Wanna Go Where You Go) Then I\'ll Be Happy / The Song Is You•RCA Victor•1946','\
Paul Robertson (14)•The Song Is You•Palo Alto Jazz Records•1980','\
Steve Nelson Quintet•Live Session Two•Red Record•1990','\
Warne Marsh Quartet•The Unissued 1975 Copenhagen Studio Recordings•Storyville•1997','\
Sonny Stitt•In Style•Muse Records•1982','\
Oscar Peterson•Oscar Peterson Plays Jerome Kern•no label•1960','\
Chet Baker•Peace•Enja Records•1982','\
Buddy DeFranco•The Song From Moulin Rouge / I\'m Gettin\' Sentimental Over You•MGM Records•1953'),'\
\
Sophisticated Lady\
':('\
Duke Ellington And His Orchestra•Sophisticated Lady / Stormy Weather•Columbia•0','\
Bill Jennings Quartet•633-Knock!•King Records (3)•1955','\
Duke Ellington•Satin Doll / Sophisticated Lady•RCA Victor•0','\
Earl Harlan And His Orchestra•Sophisticated Lady / Smoke Rings•Perfect (3)•1933','\
Rosemary Clooney•Grievin\' / Sophisticated Lady•Columbia•1956','\
The Georgia Washboard Stompers•Sophisticated Lady / My Pretty Girl•Bluebird (3)•1933','\
Jimmie Lunceford And His Orchestra•Sophisticated Lady / Mood Indigo•Brunswick•0','\
Duke Ellington•Sophisticated Lady / Pitter Panther Patter•no label•0','\
Erroll Garner•Sophisticated Lady / Fine and Dandy•Columbia•1951','\
Dinah Shore•Sophisticated Lady / Star Dust•no label•1943','\
Jimmie Lunceford And His Orchestra•Sophisticated Lady / Unsophisticated Sue•Decca•1934','\
Billy Eckstine And His Orchestra•Jitney Man / Sophisticated Lady•National Records (2)•1945','\
The Royale Dance Orchestra•Duke Ellington\'s Famous Hits•Royale•0','\
Duke Ellington•Caravan•RCA Victor•1958','\
Vicki Gillespie•We Love You Madley (A Tribute To Duke Ellington)•Pye Records•1974'),'\
\
Sorcerer The\
':('\
Steve Spiegl Big Band•Perspectives•Sorcerer Records•1982','\
Miles Davis•Sorcerer•Columbia•1967','\
Franco Ambrosetti•The Jazz Live Situation•Dire (2)•1973','\
Herbie Hancock•Directions In Music - Live At Massey Hall•Verve Records•2002','\
Larry Coryell•Shining Hour•Muse Records•1990','\
Herbie Hancock•Speak Like A Child•Blue Note•1968'),'\
\
Soul Eyes\
':('\
Billie Holiday•Them There Eyes / Body And Soul•Columbia•1947','\
David Newton (3)•Eye Witness•Linn Records•1991','\
Idrees Sulieman•Interplay For 2 Trumpets And 2 Tenors•Prestige•1957','\
Marion Brown•Soul Eyes•Baystate•1979','\
no artist•Mood For Tenor•Coral•1955','\
Hilton Ruiz•Island Eyes•BMG Ricordi S.p.A.•1997','\
The Bob Brookmeyer Quartet•The Bob Brookmeyer Quartet•Vogue•1955','\
Benny Bailey Sextett•Soul Eyes: Jazz Live At The Domicile Munich•SABA•1968','\
Yosuke Yamashita Trio•A Tribute To Mal Waldron•Enja Records•1980','\
Mal Waldron•Space•Vent Du Sud•1986','\
Gene Krupa Jazz Trio•Gene Krupa Jazz Trio•Columbia•1952','\
Karin Krog•Hi-Fly•Compendium Records•1976','\
Gene Krupa Trio•At Jazz At The Philharmonic•Mercury•1952'),'\
\
Soul Man\
':('\
Ramsey Lewis•Soul Man / Struttin\' Lightly•Cadet•1968','\
Ramsey Lewis•Soul Man / Struttin\' Lightly•Chess•1967','\
Harold Alexander•Mama Soul / Sunshine Man•Flying Dutchman•1971','\
Lonnie Sattin•Watermelon Man / Soul Bossa Nova•Scepter Records•1963','\
Cal Tjader•Cuchy Frito Man / Soul Burst•Verve Records•1966','\
Johnny Griffin•Jazz Jamboree 63 Vol. 2•Polskie Nagrania Muza•1963','\
Jimmy Smith•Groovin\' At Smalls\' Paradise (Volume 2)•Blue Note•1958','\
Herbie Mann•Memphis Two-Step / Soul Man•Embryo Records•1971','\
Monk Higgins•Extra Soul Perception / Watermelon Man•Solid State Records (2)•1968','\
The Johnny Griffin Quartet•Body And Soul•Moon Records (4)•1989','\
Dizzy Gillespie•Azure Blue•Hallmark Jazz•2000','\
Sarah Vaughan•Vol 1•Metronome•1954','\
Rotary Connection•Ruby Tuesday / Soul Man•Cadet Concept•1968','\
Sarah Vaughan•Images•Emarcy•1954','\
Gene Krupa Trio•At Jazz At The Philharmonic•Mercury•1952','\
Art Blakey & The Jazz Messengers•Sängerhalle Untertürkheim July 15 1978•SWR Music•2011','\
John Patton•Understanding•Blue Note•1968','\
Various•Organ Jazz•Fantasy•2000'),'\
\
Soul Sauce (Wachi Wara)\
':('\
Cal Tjader•Cal Tjader\'s Greatest Hits•Fantasy•1966','\
Cal Tjader•Cal Tjader\'s Greatest Hits•Fantasy•1995','\
Various•Rare Tunes Chapter Two "From Latin... To Jazz Dance"•Rare Groove Recordings•1995','\
Xavier Cugat And His Orchestra•Dance Party•Decca•1966','\
Various•The Rare Tunes Collection "From Latin... To Jazz Dance" - Vol. 2•Rare Groove Recordings•2003','\
Xavier Cugat•The Best Of Xavier Cugat•MCA Records•1975'),'\
\
Soultrane\
':('\
Tadd Dameron•Mating Call•Prestige•1957','\
Sasaki Hideto - Sekine Toshiyuki Quartet + 1•Stop Over•SMILE•1976','\
Chet Baker•The Most Important Jazz Album Of 1964/65•Colpix Records•1964','\
Steve Grossman•Katonah•DIW•1986','\
Elvin Jones•Mr. Jones•Blue Note•1973','\
John Coltrane•Jazz Showcase•Original Jazz Classics•2008','\
Steve Grossman•Way Out East - Vol. 2•Red Record•1984','\
Barry Harris (2)•Barry Harris Plays Tadd Dameron•Xanadu Records•1975','\
Steve Grossman Trio• Bouncing With Mr. A.T.•Dreyfus Jazz•1996'),'\
\
Sound Lee\
':('\
Lee Konitz•At Storyville•Storyville (3)•1954','\
Lee Konitz Quintet•Lee Konitz Quintet / Lennie Tristano Quintet•New Jazz•1951','\
Lee Konitz•Lee Konitz Quintet With Warne Marsh•Prestige•1954','\
Lee Konitz•At Storyville•Black Lion Records•1988','\
Lee Konitz•Subconscious-Lee•Prestige•1955','\
Lennie Tristano Quintet•Live In Toronto 1952•Jazz Records•1982','\
Lee Konitz•Jazz At Storyville•Storyville (3)•1956','\
Lee Konitz•Lee Konitz Meets Warne Marsh Again•Epic•1978'),'\
\
Space Circus Part 1\
':('\
André Ceccarelli•Ceccarelli•Carla•1977','\
Various•LAFMS: The Lowest Form Of Music•Cortical Foundation•1996'),'\
\
Space Circus Part 2\
':('\
André Ceccarelli•Ceccarelli•Carla•1977','\
Various•LAFMS: The Lowest Form Of Music•Cortical Foundation•1996'),'\
\
Spain\
':('\
Wolfgang Gerhard•Nena•Polydor•0','\
Bob Crosby And The Bob Cats•All By Myself / Spain•Decca•1942','\
Ted Daniel•Ted Daniel Sextet•Ujamaa Records•1970','\
Victor Silvester And His Silver Strings•Panama•Columbia•1956','\
Sammy Kaye•Spain / That Daffodil Feelin\'•Columbia•0','\
Dick Contino•Lady Of Spain•Horace Heidt Presents•1952','\
RSL•The Magic Of Spain•Players•2005','\
Charles Dornberger & His Orchestra•My Castle In Spain / Drifting Apart•Victor•1926','\
Feb September•The Old Piano Roll Blues / Spain•Mercury•1950','\
Masayuki Takayanagi•Live Independence•P.S.F. Records•1995','\
Jabbo Smith And His Orchestra•Rhythm In Spain / More Rain More Rest•Decca•1938','\
Vlady Bas•Old Spain / Italian Style  •Acción•1972','\
Ray Martin And His Concert Orchestra•Exotica•Columbia•0','\
Chick Corea•Spain•Polydor•1973'),'\
\
Speak Like A Child\
':('\
Herbie Hancock Trio•The Herbie Hancock Trio•CBS/Sony•1977','\
Herbie Hancock•Speak Like A Child•Blue Note•1968','\
Alan Simon (2)•Rainsplash•Cadence Jazz Records•1985','\
Mel Lewis•Live In Montreux•MPS Records•1981','\
Red Rodney And Ira Sullivan Quintet•Sprint•Elektra Musician•1983','\
Herbie Hancock•The Best Of Herbie Hancock•Blue Note•0','\
Tatsuya Takahashi & Tokyo Union•Black Pearl•Zen (3)•1980','\
Various•Chesky Records•Ήχος & Hi-Fi•1998','\
George Kawaguchi•George Kawaguchi Plays Herbie Hancock•Paddle Wheel•1987','\
Kevin Eubanks•Live At Bradley\'s•Blue Note•1994','\
Herbie Hancock•Ken Burns Jazz•Columbia•2000'),'\
\
Speak Low\
':('\
Guy Lombardo And His Royal Canadians•Speak Low / Take It Easy•Decca•1943','\
Gerry Mulligan Quartet•Gene Norman Presents The Gerry Mulligan Quartet•Gene Norman Presents•1954','\
Eddie "Lockjaw" Davis•Days Of Wine And Roses / Speak Low•RCA Victor•1966','\
Booker Ervin•That\'s It!•Candid•1961','\
Booker Ervin•The Trance•Prestige•1967','\
Pilita•Speak Low / Come Closer To Me•Astor•1959','\
Richard Davis (2)•As One•Muse Records•1976','\
Dan Nimmer Trio•Yours Is My Heart Alone•Venus Records (5)•2008'),'\
\
Speak No Evil\
':('\
Dadisi Komolafe•Hassan\'s Walk•Nimbus West Records•1983','\
Buddy Rich And The Big Band Machine•Speak No Evil•RCA•1976','\
Wayne Shorter•The Best Of Wayne Shorter•Blue Note•1988','\
Wayne Shorter•Speak No Evil•Blue Note•1966','\
Peter Leitch•Red Zone•Reservoir (2)•1987','\
Vaughan Hawthorne•Emanon•Intouch•1987','\
Helge Lien Trio•Spiral Circle•DIW•2002','\
Don Redman All Stars•Don Redman And His All-Stars•Jazz Kings•0','\
Don Redman•Dance Dance Dance With Don Redman•Urania Records (3)•0'),'\
\
Spiral\
':('\
Paul Bley Trio•Emerald Blue•Venus Records (5)•1994','\
John Coltrane•Giant Steps•Atlantic•1960','\
Sam Rivers Winds Of Manhattan•Colours•Black Saint•1983','\
no artist•Live In An American Time Spiral•Soul Note•1983','\
Elsie Jo•Live•Maya Recordings•1992','\
Andrew Hill•Spiral•Arista•1975','\
George Russell•So What•Blue Note•1986','\
Ill Considered•5•Ill Considered Music•2018','\
Creative Construction Company•Creative Construction Company•Muse Records•1975','\
Menagerie•The Arrow Of Time•Freestyle Records (2)•2017','\
Bobby Hutcherson•Spiral•Blue Note•1979','\
Hutcherson-Land Quintet•Blow Up•Jazz Music Yesterday•1990','\
Kenny Barron•Spiral•Eastwind•1984','\
Elements (6)•Forward Motion•Antilles•1984','\
Hervé Provini•Digital Music Landscape For Drum And Computer•Audioactivity•2011'),'\
\
Sprial Dance\
':('\
Jan Garbarek•Belonging•ECM Records•1974'),'\
\
Spring can Really Hang You Up the Most\
':('\
Phil Woods•Phil Woods & The Japanese Rhythm Machine•RCA•1976','\
Stanley Turrentine•A Chip Off The Old Block•Blue Note•1964','\
Billy Wallace•Coming Home•MDM Productions•1979','\
Stan Getz•Poetry•Elektra Musician•1984','\
Walter Norris•Drifting•Enja Records•1974','\
Kenny Burrell•Groovin\' High•Muse Records•1984','\
Eddie Green (3)•This One\'s For You•M & I•1995','\
Brad Mehldau•New York-Barcelona Crossing•Fresh Sound New Talent•1997','\
Nathan Davis•Happy Girl•SABA•1965','\
Blue Mitchell•Booty•Mainstream Records•1974','\
Soesja Citroen•Shall We Dance - Or Keep On Moping•Timeless Sunny•1987','\
Joe Diorio•Bonita•Zdenek Records•1980'),'\
\
Spring Is Here\
':('\
Ralph Burns And His Ensemble•Spring Sequence•Period Records•1955','\
Kenny Dorham Septet•Blue Spring•Riverside Records•1959','\
Stan Getz Quintet•Interpretations By Stan Getz Quintet•Karusell•1955','\
John Coltrane•While My Lady Sleeps•Fontana•1964','\
Paul Smith (5)•Liquid Sounds Part 2•Capitol Records•1954','\
Ralph Burns And His Ensemble•Bijou•Bethlehem Records•1957','\
Toshiko Akiyoshi Trio•Four Seasons•Ninety-One•1990','\
Anthony Braxton•Seven Standards 1985 Volume I•Magenta (2)•1985','\
The Dave Brubeck Trio•The Dave Brubeck Trio•Fantasy•1953','\
The Ramsey Lewis Trio•The Sound Of Spring•Argo (6)•1962','\
Horace Parlan•The Maestro•SteepleChase•1982','\
Tutti Camarata•Spring•Disneyland•1958','\
Stan Getz•Stan Getz \'57•Verve Records•1957','\
John Coltrane•Standard Coltrane•Prestige•1962'),'\
\
St. Louis Blues\
':('\
Various•14 Blue Roads To St. Louis•RCA Victor•1958','\
Various•St. Louis Blues•Philips•1957','\
Billy Eckstine•St. Louis Blues•MGM Records•1953','\
no artist•The Birth Of The Blues (An Album Of W. C. Handy Music)•Victor•0','\
no artist•St. Louis Blues / Memphis Blues•Victor•1941','\
Clyde McCoy•Sugar Blues•Mercury•1957','\
Louis Armstrong•St Louis Blues / Basin Street Blues•Odeon•1959','\
Teddy Stauffer Und Seine Original Teddies•St. Louis Blues / Meditation•Telefunken•1938'),'\
\
St. Thomas\
':('\
Sonny Rollins Quartet•St. Thomas•Prestige•1957','\
Sonny Rollins•Sonny Rollins In Japan•Victor•1973','\
Clifford Jordan And The Magic Triangle•On Stage Vol. 3•Steeplechase•1979','\
Sonny Rollins•Saxophone Colossus•Metronome•1957','\
Stuff Combe•Stuff Combe 5 + Percussion•M Records (3)•1974','\
Jim Hall Trio•Jim Hall Live In Tokyo•A&M Records•1976','\
Sonny Rollins•Alternatives•Bluebird (3)•1992','\
LA4•The L.A.4•Concord Jazz•1976','\
Hampton Hawes•Live At The Jazz Showcase In Chicago Volume One•Enja Records•1981','\
Kunio Ohta Quintet•My Back Pages •Three Blind Mice•1977'),'\
\
Stablemates\
':('\
Pat Patrick•Sound Advice•El Saturn Records•1977','\
Barney Wilen•Barney•RCA•1960','\
Mal Waldron Quintet•Mal-1•Prestige•1957','\
Roger Guérin•Roger Guérin - Benny Golson•Columbia•1959','\
Benny Golson Quartet•Benny Golson Quartet•LRC Ltd.•1990','\
Milt Jackson•Bags Meets Wes!•Riverside Records•1962','\
Sam Jones•Changes & Things•Xanadu Records•1978','\
Paul Chambers (3)•Chambers\' Music: A Jazz Delegation From The East•Jazz: West•1956','\
Herbie Hancock Trio•Herbie Hancock Trio With Ron Carter + Tony Williams•CBS/Sony•1981','\
no artist•Double Or Nothin\'•Liberty•1957'),'\
\
Stairway To The Stars\
':('\
Serge Chaloff•Blue Serge•Capitol Records•1956','\
Sammy Kaye•Stairway To The Stars / White Sails•Victor•1939','\
Milt Jackson•S. K. J. / Stairway To The Stars•Riverside Records•1962','\
Ella Fitzgerald•Stairway To The Stars / Out Of Nowhere•Decca•1947','\
Jack Weigand•Shangri-La•Cameo•1960','\
Vic Dana•Garden In The Rain  / Stairway To The Stars•Dolton Records•1964','\
Erroll Garner•I Can\'t Escape From You / Stairway To The Stars•RCA Victor•1952','\
The Urbie Green Septet•New Faces - New Sounds•Blue Note•1953','\
Milt Jackson•Bags Meets Wes!•Riverside Records•1962','\
Buddy Baker And His Orchestra•Beyond The Stars•Exclusive (2)•0','\
John Coltrane•The Coltrane Legacy•Atlantic•1970'),'\
\
Star Eyes\
':('\
Charlie Parker And His Orchestra•Au Privave / Star Eyes •Mercury•1951','\
Kitty Kallen•Star Eyes•RCA Victor•1963','\
Bill Snyder•Star Eyes / Swinging On A Star•Decca•1953','\
Chet Baker•Star Eyes•Marshmallow (3)•1990','\
Bill Snyder•The Starlit Hour•Decca•0','\
John Jenkins (2)•Jazz Eyes•Regent•1957','\
Sonny Stitt•Who Can I Turn To?•Prestige•1965','\
Teddy Charles New Directions Quartet•Teddy Charles Featuring Bobby Brookmeyer•Prestige•1954','\
Sonny Stitt•Sonny\'s Blues•UpFront Records (3)•1977','\
Charlie Parker•The Magnificent Charlie Parker (Album #1)•Clef Records•0','\
Carmen McRae•Tonight He\'s Out To Break Another Heart / Star Eyes•Decca•1956','\
Ted Curson•The New Thing & The Blue Thing•Atlantic•1965','\
The Cannonball Adderley Quintet•Plus•Riverside Records•1961','\
Carmen McRae•Star Eyes / I\'m A Dreamer (Aren\'t We All)•Brunswick•1956','\
Xanadu•Xanadu At Montreux Volume Three•Xanadu Records•1979','\
Bennie Wallace•The Free Will•Enja Records•1980'),'\
\
Star-Crossed Lovers\
':('\
Tommy Flanagan•The Best Of•Pablo Records•1980','\
Pepper Adams•Encounter•Prestige•1969','\
Wojciech Karolak•Kalisz. X-Lecie Międzynarodowych Festiwali Pianistów Jazzowych•PolJazz•1983','\
James Newton (2)•Water Mystery•Gramavision•1986','\
Randy Weston•Live At The Fivespot•United Artists Records•1960','\
Kenny Barron•At The Piano•Xanadu Records•1982','\
Dave Liebman Quartet•The Opal Heart•Enja Records•1979','\
Kenny Drew•Moonlit Desert•Baystate•1982','\
Aaron Heick•Europe•Venus Records (5)•2009','\
The Pete Malinverni Trio•Don\'t Be Shy•Sea Breeze Jazz•1988','\
Tommy Flanagan Trio•Montreux \'77•Pablo Live•1977','\
The Claude Williamson Trio•South Of The Border - West Of The Sun•Venus Records (5)•2009','\
Tommy Flanagan Trio•Norman Granz\' Jazz In Montreux Presents Tommy Flanagan Trio \'77•Eagle Vision•2005','\
The Fred Hersch Trio•Horizons•Concord Jazz•1985'),'\
\
Stardust\
':('\
Various•The Stardust Road•RCA Victor•1960','\
Lionel Hampton All Stars•Stardust•Decca•0','\
Sonny Stitt•Stardust•Roulette•1966','\
The Dave Brubeck Quartet•Perdido / Stardust•Fantasy•1953','\
Billy Butterfield And His Orchestra•Stardust / Jalousie•Capitol Records•1948','\
Benny Goodman And His Orchestra•Stardust / Caravan•Philips•0','\
Billy Butterfield And His Orchestra•Stardust / Steamroller•Telefunken Capitol•0','\
Billy Eckstine•Stardust•Polydor•0','\
Dizzy Gillespie Quintet•Umbrella Man / Stardust•Dee Gee•1953','\
J.J. Johnson•Debut Records\' Jazz Workshop Volume One: Trombone Rapport•Debut Records•1953','\
Johnny Otis And His Orchestra•Oopy-Doo / Stardust•Mercury•1952','\
Larry Clinton And His Orchestra•Stardust / Tammy•Bell Records•1957','\
Jimmie Lunceford And His Orchestra•Unsophisticated Sue / Stardust•Decca•0','\
Jerry Murad•Stardust•Mercury•1953','\
Lester Young•Pres Is Blue•Charlie Parker Records•1963'),'\
\
Stargazer\
':('\
Frank Sinatra•Stargazer / The Best I Ever Had•Reprise Records•1976','\
Golden Dawn Arkestra•Stargazer•Modern Imperial Records•2016','\
Les DeMerle•On Fire•Palo Alto Records•1982','\
Armen Donelian•A Reverie - Solo Piano•Sunnyside•1986','\
David S. Ware Quartet•Live In The World•Thirsty Ear•2005','\
Ray Barretto•Can You Feel It•Atlantic•1978','\
Polyrhythmics•Caldera•Polyrhythmics•2017','\
Down To The Bone•Crazy Vibes And Things•GRP•2002','\
Frank Sinatra•The Singles•Reprise Records•1978','\
Hugo Strasser Und Sein Tanzorchester•Die Tanzplatte Des Jahres 78•EMI•1977','\
Dexter Wansel•Life On Mars•Philadelphia International Records•1976','\
Groove Collective•Live: Brooklyn NY 04.20.02•Kufala Recordings•2002','\
Shirley Bassey•You Take My Heart Away•United Artists Records•1977','\
Shirley Bassey•Onvergetelijke Hits•Liberty•0'),'\
\
Stars Fell On Alabama\
':('\
Vincent Rose And His Orchestra•Stars Fell On Alabama / Learning•Perfect (3)•1934','\
Cannonball Adderley•Limehouse Blues / Stars Fell On Alabama•Limelight•1964','\
Woody Herman And His Orchestra•Sidewalks Of Cuba / Stars Fell On Alabama•Columbia•0','\
Frankie Laine•Jazz Spectacular•Columbia•1956','\
Jonah Jones•Wrap Your Troubles In Dreams / Stars Fell On Alabama•Bethlehem Records•1958','\
Stan Getz Quintet•The Way You Look Tonight / Stars Fell On Alabama•Mercury•1952','\
Ella Fitzgerald•Can\'t We Be Friends? / Stars Fell On Alabama•Verve Records•1956','\
Bengt Hallberg Trio•Opus One•Metronome•1954','\
Johnny Guarnieri•Jazz Piano By..EP•Royale•0','\
Frank Sinatra•A Swingin\' Affair Part 4•Capitol Records•1957','\
Louis Armstrong And His All-Stars•Satchmo At Symphony Hall Volume 3•Brunswick•1957','\
The Cannonball Adderley Quintet•In Chicago•Mercury•1959','\
The Cannonball Adderley Quintet•In Chicago•Mercury•1959'),'\
\
Steepian Faith\
':('\
Various•I Love A Piano•GRP•1993','\
Kenny Kirkland•Kenny Kirkland•GRP•1991','\
Various•GRP 10th Anniversary Collection•GRP•1992'),'\
\
Stella By Starlight\
':('\
The Chico Hamilton Quintet•Satin Doll•Pacific Jazz•0','\
Charlie Parker With Strings•Stella By Starlight•Mercury•1952','\
Arthur Prysock•Stella By Starlight / My Wish•Old Town Records•0','\
Stan Kenton And His Orchestra•Contemporary Concepts (No. 1)•Capitol Records•0','\
Frank Sinatra•Mam\'selle / Stella By Starlight•Columbia•1947','\
Various•Jazz For A Sunday Afternoon Volume 4•Solid State Records (2)•1969','\
Teddy Wilson•Air Mail Special•Polydor•0','\
Miles Davis•Poll Winners Jazz•Fontana•1958','\
Zoot Sims•Stella By Starlight / Over The Rainbow•Impulse!•1967','\
Lee Konitz•Creative Music Studio - Woodstock Jazz Festival 1•Douglas Music•1997','\
Teddy Wilson•Air Mail Special•Polydor•0','\
Harry James And His Orchestra•Mona Lisa / Stella By Starlight•Columbia•0'),'\
\
Step Lightly\
':('\
Shelly Manne & His Men•At The Black Hawk Vol. 2•Contemporary Records•1960','\
Blue Mitchell•The Thing To Do•Blue Note•1965','\
Blue Mitchell•Step Lightly•Blue Note•1980','\
Bobby Hutcherson•The Kicker•Blue Note•1999','\
Benny Golson•Benny Golson\'s New York Scene•Contemporary Records•1958','\
Ferit Odman•Autumn In New York•Equinox Music & Entertainment•2011','\
Joe Henderson•Big Band•Verve Records•1996','\
The Grassella Oliphant Quartet•The Grass Roots•Atlantic•1965'),'\
\
Steps\
':('\
Electric Circus (3)•Live At The Quartier Latin•Vinyl Records•1979','\
Woody Herman And His Woodchoppers•Fan It / Steps•Columbia•0','\
Anthony Braxton•Duo (Verona) 1989•Braxton Bootleg•2011','\
John Coltrane•Giant Steps•Atlantic•1960','\
Earl Hines And His Orchestra•Piano Man / Father Steps In•Bluebird (3)•1939','\
Edgar Hayes And His Orchestra•Caravan / Edgar Steps Out•Decca•1937','\
Duke Ellington And His Orchestra•The Duke Steps Out / Haunted Nights•no label•0','\
Barney Bigard•Barney Bigard•Liberty•1955','\
Nostalgia 77•Everything Under The Sun•Tru Thoughts•2007','\
John Coltrane•John Coltrane•Fabbri Editori•1979','\
Toshiyuki Miyama & The New Herd•Orchestrane New Herd Plays John Coltrane•Denon Jazz•1977'),'\
\
Sticky Wicket\
':('\
Dexter Gordon•More Power!•Prestige•1969','\
Dexter Gordon Quartet•Swiss Nights Vol. 2•Steeplechase•1978','\
Dexter Gordon Quartet•Espace Cardin 1977•Elemental Music•2018','\
Dexter Gordon•American Classic•Elektra Musician•1982','\
no artist•Spaceball•Arista•1976','\
Dexter Gordon•Power!•Prestige•1978','\
Dexter Gordon•Power!•Prestige•1978','\
Billy Larkin And The Delegates•The Best Of•World Pacific Records•0','\
Billy Larkin And The Delegates•Blue Lights•Aura Records (4)•1965','\
Peter Banks•Instinct•HTD Records•1993'),'\
\
Still\
':('\
Engine•Still Standing•Bagatelle Records•2004','\
Sadao Watanabe•If I\'m Still Around Tomorrow•Elektra•1984','\
Keith Jarrett•Fort Yawuh•Impulse!•1973','\
Al Morgan (3)•So Long Sally•London Records•1950','\
DWH•Still Here EP•Counterpoint Records•2004','\
Silje Nergaard•Be Still My Heart•EmArcy•2001','\
Anthony Davis (2)•Undine•Gramavision•1987','\
Arnett Cobb & His Orchestra•Cobb\'s Idea / Still Flyin\'•Apollo Records (2)•1947','\
John Raymond (4)•Real Feels Live Vol. 2•Sunnyside•2019','\
Courtney Pine•I\'m Still Waiting•Island Records•1990','\
Louis Armstrong And His All-Stars•I Still Get Jealous / Someday•Kapp Records•1964','\
Emiel Van Egdom•This Is For You•Optimism Incorporated•1989','\
The Three Sounds•Still I\'m Sad•Blue Note•1967','\
Frantz Loriot Systematic Distortion Orchestra•The Assembly•OutNow Recordings•2016','\
Ahmad Jamal Trio•Ahmad\'s Blues / Will You Still Be Mine•Okeh•1951'),'\
\
Stolen Moments\
':('\
Phil Woods And His European Rhythm Machine•Woods-Notes•International Joker Production•1977','\
Herbie Mann•Standing Ovation At Newport•Atlantic•1965'),'\
\
Stompin\' At The Savoy\
':('\
Harry James And His Orchestra•Stompin\' At The Savoy•Columbia•1954','\
Various•Norman Granz\' Jam Session #6•Clef Records•1954','\
Benny Goodman•Stompin\' At The Savoy•RCA•0','\
Jazz Club Mystery Hot Band•Stompin At The "Savoy" / S\'Wonderful•Disques ABC Paris•1945','\
Harry James And His Orchestra•Stompin\' At The Savoy / Flash•Philips•0','\
Clifford Brown•Sweet Clifford•Mercury Emarcy Jazz•1956','\
Duke Ellington And His Orchestra•Ellington \'55 Part 2•Capitol Records•1955','\
Erroll Garner•September Song / Stompin\' At The Savoy•Savoy Records•1949','\
Hub Atwood•Stompin\' At The Savoy•Capitol Records•0','\
Gene Krupa/Charlie Ventura Trio•Stompin\' At The Savoy / Body And Soul•Disc Records•0','\
The Benny Goodman Quartet•Stompin\' At The Savoy / Dizzy Spells•Philips•1955','\
The Benny Goodman Quartet•Stompin\' At The Savoy / Let\'s Dance•Columbia•0','\
Jack Teter Trio•Stompin\' At The Savoy•Sharp•1951','\
The Oscar Peterson Quartet•The Oscar Peterson Quartet•Mercury•1952'),'\
\
Stormy Weather\
':('\
Erroll Garner•Stormy Weather•Savoy Records•1950','\
Luis Arcaraz Y Su Orquesta•Caravan•RCA Victor•1951','\
Duke Ellington And His Orchestra•Sophisticated Lady / Stormy Weather•Columbia•0','\
Sidney Bechet•Petite Fleur / Stormy Weather•Disques Vogue•0','\
Tex Beneke•Body and Soul / Stormy Weather•RCA Victor•1947','\
Elisabeth Welch•Stormy Weather•Industrial Records•1980','\
Dinah Washington•Make Believe Dreams / Stormy Weather•Mercury•1952','\
Charles Mingus•Mingus•Candid•1961','\
Leo Mathisens Band•Stormy Weather / Pardon Me Pretty Baby•Odeon•1941','\
Earl Grant•I Miss You So•Decca•1967','\
Junior Mance•Stormy Weather / Down On The Floor•Riverside Records•1962'),'\
\
Story Line\
':('\
KAOS Protokoll•Everyone Nowhere•Prolog•2018','\
Casiopea•Bitter Sweet•Pioneer (3)•2000','\
The Bill Evans Trio•At Town Hall Volume One•Verve Records•1966','\
Mantovani And His Orchestra•Annunzio Paolo Mantovani•London Records•1972','\
Various•Family Portrait•A&M Records•0','\
Marco Benevento•The Story of Fred Short•The Royal Potato Family•2016','\
Geoff Love & His Orchestra•Your Top TV Themes•Music For Pleasure•1972','\
Leon Redbone•No Regrets•Sugar Hill Records (2)•1988','\
Julia Migenes•More Live At The Olympia•Milan•1989','\
Various•Hithaus: Goldene Evergreens - 20 Instrumental Welterfolge•Polystar (3)•0','\
Nick Nicholas•TV Piano Time With Nick Nicholas•Contour•1973','\
The Grateful Dead•Dick\'s Picks Volume Eleven 9/27/72•Grateful Dead Records•1998'),'\
\
Straight Life\
':('\
Boillat Therace Quintet•The Best Selection•KS Music•2001','\
Freddie Hubbard•Straight Life•CTI Records•1971','\
Art Pepper•Landscape - Art Pepper Live In Tokyo \'79•JVC•1979','\
Art Pepper•Renascence•Galaxy•2000','\
Art Pepper•Straight Life•Galaxy•1979','\
Art Pepper•Tokyo Encore•Dreyfus Jazz•1991','\
Art Pepper•Laurie\'s Choice•Fresh Sound Records•1992','\
Andy LaVerne Trio•Another World•SteepleChase•1978','\
John Coltrane•Jazz Showcase•Original Jazz Classics•2008','\
Sandy Mosse•Chicago Scene •Argo (6)•1957','\
Willie Pickens•It\'s About Time•Southport Records•1998','\
The Cannonball Adderley Quintet•Portrait Of Cannonball•Riverside Records•1958','\
Ayumi Koketsu•Art•M & I•2016'),'\
\
Straight No Chaser\
':('\
Miles Davis•Straight-No Chaser!•Fontana•1958','\
Norio Maeda•Pianic Pianism = スーパー・ソロ・ピアノの世界•Denon Jazz•1977','\
Clark Terry / Bob Brookmeyer Quintet•Blindman Blindman / Straight No Chaser•Mainstream Records•0','\
Various•Jazz For A Sunday Afternoon Volume 3•Solid State Records (2)•1968','\
Miles Davis•Poll Winners Jazz•Fontana•1958','\
Mal Waldron•Left Alone - Mal Waldron Live 1•Fontana•1974','\
The Ben Webster Quintet•Blow Ben Blow!•Catfish•1969','\
Juan Carlos Calderón•Bloque 6•Hispavox•1968','\
The North Texas State University Lab Band•Lab \'73•NTSU Jazz•1973','\
Louis Van Dyke Trio•Loosdrecht Jazz Concours•Philips•1961','\
Bud Powell•Hot House•Fontana•1966','\
Clark Terry•VARA Radio - 1965•Varajazz•1988','\
Sebastian Gramss•knoM.T•Jazz Haus Musik•2000','\
Grant Green•I Giganti Del Jazz Vol. 55•Curcio•0','\
Dizzy Gillespie•To Diz With Love (Live At The Blue Note)•Telarc•1992','\
Art Taylor•Taylor\'s Tenors•New Jazz•1959','\
Al Haig•Be Bop Live•Spotlite Records•1983','\
Art Pepper•So In Love•Artists House•1980'),'\
\
Strayhorn 2\
':('\
no artist•Idol Gossip•Chiaroscuro Records•1976','\
Gerry Mulligan•Symphonic Dreams•PAR (4)•1987','\
Ran Blake•Duke Dreams "The Legacy Of Strayhorn-Ellington"•Soul Note•1981'),'\
\
Street Life\
':('\
Herb Alpert•Rotation•A&M Records•0','\
The Crusaders•Street Life•MCA Records•1979','\
Stan Getz Quartet•Portrait•Joker (2)•1977','\
The Crusaders•Soul Shadows•Warner-Pioneer Corporation•1985','\
The Crusaders•Soul Shadows / Street Life•MCA Records•1980','\
no artist•Life Is Just A Bowl Of Cherries / Basin Street Blues•Columbia•1957','\
Matumoto Hiroshi • Ichikawa Hideo Quartet•Megalopolis•VICTOR WORLD GROUP•1969','\
John Coltrane•Jazz Showcase•Original Jazz Classics•2008','\
Rhoda Scott•Rhoda Scott + Kenny Clarke•Barclay•1977','\
Harold Alexander•Raw Root•Atlantic•1974','\
Gil Mellé Quintet•5 Impressions of Color•Blue Note•1955','\
Maynard Ferguson•Live From San Francisco - From The Great American Music Hall•Palo Alto Records•1985'),'\
\
Street Of Dreams\
':('\
Felix Slatkin•Street Scene•Liberty•1961','\
Dotts Johnson•Street Of Dreams / Paradise•Metro Records•1958','\
Stan Kenton And His Orchestra•Street Of Dreams / Daddy•Capitol Records•1951','\
Gene Ammons And His Orchestra•Street Of Dreams / The Beat•United (2)•1952','\
Jan Garber And His Orchestra•Street Of Dreams•Decca•1961','\
no artist•The Siren\'s Song•Liberty•1966','\
Ralph Flanagan• Ralph Flanagan In Hi-Fi 1•RCA•0','\
The Ernie Felice Quartet•Woo-Ca-Ma-Choo-Ga / Street Of Dreams•Capitol Records•1948','\
Norman Connors•Slew Foot•Buddah Records•1974','\
Billy May And His Orchestra•Street Of Dreams•Capitol Records•1955','\
Tommy Dorsey And His Orchestra•Just As Though You Were Here / Street Of Dreams•Victor•1942','\
Cedar Walton Trio•Song Of Delilah•Venus Records (5)•2010','\
James Carter (3)•Heaven On Earth•Half Note Records•2009','\
Sarah Vaughan•Street Of Dreams / Time To Go•Columbia•1952','\
Sonny Stitt Quartet•The Hard Swing•Verve Records•1960','\
Grant Green•Street Of Dreams•Blue Note•1967'),'\
\
Strike Up The Band\
':('\
Tombee•Strike Up The Band•Jack To Phono Records•2011','\
Art Pepper•Inglewood Jam 1952•Absord Music Japan•2009','\
Herb Alpert & The Tijuana Brass•Jerusalem / Strike Up The Band•A&M Records•1970','\
Ted Heath And His Music•Strike Up The Band / Hot Toddy•Decca•1953','\
Marian McPartland•Strike Up The Band / Love Is Here To Stay•Savoy Records•1952','\
Buddy DeFranco•Buddy De Franco And Oscar Peterson Play George Gershwin•Karusell•1955','\
Sidney Bechet•September Song•Vogue Productions•0','\
Jazz Superstars•A Live Jam Session Recorded at "Trade Winds"•Jam Session Records (2)•0','\
Herbie Mann Quartet•St.Louis Blues•Verve Records•0','\
Art Farmer•New Jazz Stars•Vogue Records•0','\
Tal Farlow•The Artistry Of Tal Farlow•Norgran Records•0','\
The Red Norvo Trio•Lover Come Back To Me•Brunswick•1955','\
Oscar Peterson•Plays George Gershwin•Clef Records•0','\
Unknown Artist•Marking Time•Hoctor Records•0','\
Gene Krupa•The Jazz Rhythms Of Gene Krupa•Columbia•1955','\
The Bud Powell Trio•Memorial Oscar Pettiford•Disques Vogue•1960','\
Art Pepper•Straight-Ahead Jazz Volume One•Straight Ahead Jazz•0','\
Toshiko And Her International Jazz Sextet•United Notions•MetroJazz•1958'),'\
\
Strode Rode\
':('\
Sonny Rollins•Saxophone Colossus•Prestige•1957'),'\
\
Strollin\'\
':('\
Phil Woods•Phil Woods•Fabbri Editori•1989','\
Charlie Barnet And His Orchestra•Strollin\' / Sittin\' At Home Waitin\' For You•Decca•1944','\
Lou Donaldson•Lou Takes Off•Blue Note•1958','\
Jean-Louis Rassinfosse•Crystal Bells•LDH Records•1983','\
The Phil Woods Quartet•\'More\' Live•Adelphi Records Inc.•1981','\
King Curtis And The Noble Knights•Strollin\' Home / Mess Around•Capitol Records•0','\
Chet Baker•Strollin\'•Enja Records•1986','\
Dexter Gordon Quartet•The Apartment•SteepleChase•1975'),'\
\
Stuck On You\
':('\
Bobby Caldwell•Stuck On You•Sin-Drome Records Ltd.•1991','\
Bobby Caldwell•Blue Condition•Sin-Drome Records•1996','\
Salena Jones•Feelings Change•JVC•1984','\
The Dry Throat Fellows•Do Something•Stomp Off Records•1991','\
Natalie Williams•My Oh My•East Side Records (2)•2010','\
Acker Bilk•Memory•Success•1993','\
Various•Voices Of Love•Evosound•2011','\
Wim T. Schippers•Hark!•CBS•1980','\
Ren & Stimpy (2)•Ren & Stimpy - Radio Daze•Sony Wonder•1995','\
Acker Bilk•Magic Serenade•Quality•1986','\
Various•Action Line - Argo Cadet Grooves•Charly Records•1994','\
Acker Bilk•20 Golden Greats•Starburst Music World•1994','\
Caro Emerald•Deleted Scenes From The Cutting Room Floor•Grandmono•2010'),'\
\
Stuff\
':('\
Jimmie Lunceford And His Orchestra•Back Door Stuff•Decca•0','\
Adrian Rollini And His Orchestra•Swing Low / Stuff Etc.•Decca•1936','\
Nino Tempo & 5th Ave. Sax•(Hooked On) Young Stuff•A&M Disco•1979','\
Donald Lindley (2)•Trumpet Blues / Sweet Stuff•Columbia•1926','\
New York Art Quartet•Old Stuff•Cuneiform Records•2010','\
Herbie Haymer Quintet•Black Market Stuff / Laguna Leap•Sunset Recordings (3)•1945','\
Hazy Osterwald Quintett•Stuff And Sonny / Hazy Boogie•Elite Special•1946','\
Tommy Dorsey And His Orchestra•Until / After Hour Stuff•RCA Victor•1948','\
Bug•Symphony Del Ritmo No 2•MAMA Records•1997','\
Miles Davis•Miles In The Sky•Columbia•1968','\
The Sunset All Stars•Kicks!•Fontana•0','\
Tom Scott•Strut Your Stuff / Sneakin\' In The Back•Ode Records (2)•1974'),'\
\
Sub Aqua\
':('\
Scott Henderson (2)•Tribal Tech•Relativity•1991','\
Tribal Tech (2)•Primal Tracks•Bluemoon Recordings•1994'),'\
\
Sub-Conscious-Lee\
':('\
Bill Frisell•History Mystery•Nonesuch•2008'),'\
\
Sudden Samba\
':('\
Full Moon (5)•Live Featuring Buzz Feiten Neil Larsen Lenny Castro Art Rodriquez & Vernon Porter•Dreamsville Records•2002','\
Neil Larsen•Jungle Fever•Horizon (3)•1978','\
Orbit (11)•Neil Larsen Featuring Robben Ford•Straight Ahead Records•2007','\
Neil Larsen•Orbit•Straight Ahead Records•2007','\
S.U.M.O.•The Danceband•HEYA HIFI•2006','\
Various•Fusion Phew•Elevate•1993','\
The Tim Weisberg Band•Rotations•United Artists Records•1978','\
Various•Copenhagen Dancefloor Classics II•Murena Records•2002','\
Various•Cha-Cha De Amor•Capitol Records•1996'),'\
\
Sugar\
':('\
Cultured Pearls•Sugar Sugar Honey•WEA•1997','\
Stanley Turrentine•Sugar•CTI Records•0','\
no artist•Liza / Sugar•Parlophone•0','\
The Temperance Seven•Pasadena•Parlophone•1961','\
Jimmy McGriff•Sugar Sugar / Fat Cakes•Capitol Records•1970','\
Alice Babs•Sugar / Blue Prelude•Cupol•1949','\
Adrian Rollini And His Orchestra•Sugar / Riverboat Shuffle•Decca•1934','\
Sidney Bechet And His Orchestra•Festival Blues / Sugar•Swing (3)•1949','\
Soul Coughing•Sugar Free Jazz•Slash•1995','\
Julia And Company•Breakin\' Down (Sugar Samba)•District Of Columbia•1983','\
Alice Babs•Sugar / Blue Prelude•Cupol•1949','\
Adrian Rollini And His Orchestra•Sugar / Riverboat Shuffle•Decca•1934','\
no artist•Cocktails For Two / Sugar•Guild Records (2)•1945','\
no artist•Sugar / China Boy•Parlophone•1928','\
Louis Armstrong And His All-Stars•Rockin\' Chair / Sugar•no label•0','\
Babs Gonzales•Sugar Ray / Cool Whalin\'•Babs Records•1953','\
Clyde McCoy And His Orchestra•Sugar Blues / Hot lips•Conqueror•1931','\
Count Basie His Instrumentalists And Rhythm•Sugar / Swingin\' The Blues•RCA Victor•1947','\
Teddy Wilson And His Orchestra•More Than You Know / Sugar•Columbia•1941','\
George Wein & The Newport All-Stars•George Wein\'s Newport Jazz Festival All Stars•Smash Records (4)•1963'),'\
\
Suite: Judy Blue Eyes\
':('\
Lincoln Mayorga•Suite: Judy Blue Eyes•White Whale•1970','\
Stephen Stills•Just Roll Tape April 26 1968•Rhino Records (2)•2008','\
Bola Sete•Workin\' On A Groovy Thing•Paramount Records•1971'),'\
\
Summer In Central Park\
':('\
Jamey Aebersold•For You To Play... Horace Silver Eight Jazz Classics•JA Records•1978','\
Richard Davis (2)•Persia My Dear•DIW•1987','\
Adam Makowicz•Moonray•RCA•1986','\
Ron Carter•Panamanhattan•Dreyfus Jazz•1991','\
Horace Silver•In Pursuit Of The 27th Man•Blue Note•1973','\
Louis Hayes•Serenade For Horace•Blue Note•2017','\
Chick Corea•Music Forever & Beyond: The Selected Works Of Chick Corea 1964-1996•GRP•1996'),'\
\
Summer Knows The\
':('\
Freddie Hubbard•Skagly•Columbia•1980','\
Freddie Hubbard•Skagly•CBS•1980','\
Phil Woods•Musique Du Bois•Muse Records•1974','\
Phil Woods•Back In New York•Vedette Records•1977','\
Idrees Sulieman Quintet•Bird\'s Grass•SteepleChase•1985','\
Art Pepper•The Trip•Contemporary Records•1977','\
Art Farmer•The Summer Knows•East Wind•1977','\
Freddie Hubbard•The Best Of Freddie Hubbard Live And In Studio•Pablo Records•1983','\
Bill Evans•Montreux III•Fantasy•1976','\
Ali Ryerson•Portraits In Silver•Concord Jazz•1995','\
Nicole Croisille•Jazzille•CY Records•1987','\
Kenny Burrell•Special Requests (And Other Favorites) Live At Catalina\'s•HighNote Records Inc.•2013','\
Nicki Parrott•Summertime•Venus Records (5)•2012','\
George Roessler•The Jazz Guitar And Compositions Of George Roessler•Coincidence Records (2)•1982'),'\
\
Summer Night\
':('\
Hal McIntyre And His Orchestra•Summer Night / September Song •Cosmo•1946','\
Manhattan Trio•Manhattan Score•Egg•1970','\
Stan Getz•The Master•CBS•1982','\
101 Strings•Play Songs For Lovers On A Summer Night•Alshire•1969','\
St-Clair Pinckney•Private Stock•Ichiban Records•1989','\
Rich Perry•Time Was•SteepleChase•2012','\
The Phil Woods Quartet•Birds Of A Feather•Antilles•1982','\
Chick Corea•Trio Music Live In Europe•ECM Records•1986','\
Dizzy Gillespie Quintet•In Europe•Unique Jazz•0','\
Nicki Parrott•Summertime•Venus Records (5)•2012','\
no artist•Volume 4•Contemporary Records•1954','\
Katsutoshi Morizono•4:17 p.m.•JVC•1985'),'\
\
Summer Samba\
':('\
Walter Wanderley•Summer Samba (So Nice) / Call Me•Verve Records•1966','\
Combustible Edison•Blue Light•Domino•1993','\
Bud Shank•Summer Samba / Monday Monday•World Pacific Records•1966','\
Caiola Combo•All Strung Out•United Artists Records•1966','\
Woody Herman And His Orchestra•Moody Woody•Everest•1958','\
Bebel Gilberto•Tanto Tempo•EastWest•2003','\
Percy Faith & His Orchestra•Percy Faith Themes•CBS•0','\
The 50 Guitars Of Tommy Garrett•In A Brazilian Mood•Liberty•1967','\
Charlie Byrd•The Byrd & The Herd•Pickwick/33 Records•1966'),'\
\
Summer Time\
':('\
Toshiko Akiyoshi Trio•Four Seasons•Ninety-One•1990','\
no artist•The Band Played On•Capitol Records•1954','\
Herbie Harper Quintet•Jazz In Hollywood Series•Nocturne Records•1954','\
Rich Perry•Time Was•SteepleChase•2012','\
Gabor Szabo•Mizrab•CTI Records•1973','\
Wayne Newton•Summer Wind•Capitol Records•1965','\
Yuri Tashiro Piano Trio•Digital Explosion•Eastworld•1980','\
James Carter (3)•Gold Sounds•Brown Brothers Recordings•2005','\
Peter Brötzmann•Sparrow Nights•Trost Records•2018','\
Miles Davis•Blue Moods•Legacy•2001','\
Milt Buckner•Midnight Slows Vol. 4•Black And Blue•1974','\
Wild Bill Davis•Wild Wild Wild Wild Wild Wild Wild Wild Wild Wild •Imperial•1963','\
Gene Harris•Astralsignal•Blue Note•1974','\
Yellowjackets•Dreamland•Warner Bros. Records•1995','\
Don Rendell Quintet•Space Walk•Columbia•1972'),'\
\
Summertime\
':('\
Various•A Collection Of Various Interpretations Of Summertime•Trocadero Records•2003','\
George Benson•Summertime•CTI Records•1982','\
Jason Rebello•Summertime•RCA•1994','\
The Wes Montgomery Quartet•Summertime / Fingerpickin\'•Pacific Jazz•1960','\
Candy Dulfer•Summertime•Heads Up International•2007','\
Candy Dulfer•Summertime•Heads Up International•2007','\
Billy Longstreet Sextet•Summer Set / Summertime•Artone•0','\
Sidney Bechet•September Song / Summertime•Vogue Productions•1952','\
Port Of Harlem Seven•Pounding Heart Blues / Summertime•Blue Note•1943','\
Helen Merrill•Dream Of You / Summertime•Not On Label•0','\
Mary Lou Gauthier•In The Summertime•Polydor•0','\
Sidney Bechet And His Blue Note Jazz Men•Blues For Tommy / Summertime•Jazz Selection•0','\
The George Benson Quartet•Summertime / Ain\'t That Peculiar•Columbia•1966','\
Victor Silvester And His Ballroom Orchestra•Whisper•Columbia•1956','\
Sidney Bechet•Summertime•Blue Note•0','\
Monk Montgomery•Montgomeryland Volume One•Pacific Jazz•0','\
Bob Crosby And His Orchestra•Summertime / What\'s New•Decca•1938'),'\
\
Sunny (Sonny)\
':('\
Didier Lockwood•The Kid•MPS Records•1983','\
Toots Thielemans•Just Friends•Jazzline•1986','\
Helmut Zacharias Und Seine Verzauberten Geigen•Golden Award Songs•Polydor•0','\
Count Basie Orchestra•High Voltage•MPS Records•1970','\
Count Basie Orchestra•Basie\'s Timing•MPS Records•1976','\
Various•Remember The 40\'s•BR Music•1985','\
Sonny Stitt•Eight Classic Albums•Real Gone•2012','\
Toots Thielemans•Toots Thielemans•no label•2001','\
June Christy•The Ultimate Jazz Archive – Vocalists•Membran•2005'),'\
\
Sunshine Express\
':('\
The Bud Shank Quintet•Bud Shank\'s Sunshine Express•Concord Jazz•1976','\
Deborah Brown•Double Trouble•PolJazz•1989','\
Vince Benedetti•Heartdrops•TCB Records (2)•2002','\
Malta (3)•Summer Dreamin\'•JVC•1985','\
Isabelle Antena•French Riviera•Gate Records•2006','\
Kim & Buran•Flight B•Solnze Records•2008','\
DJ Spinbad•Needle To The Groove•Tape Kingz•0','\
Various•Goosebumps (25 Years Of Marina Records)•Marina Records•2018','\
Various•Happiness Is ... Up Up And Away With The Happy Hits Of Today•no label•1970','\
Mario 3D World Big Band•Super Mario 3D World Original Soundtrack•Nintendo•2014','\
James Last•James Last In Gold•Polydor•1975'),'\
\
Super Blue\
':('\
Freddie Hubbard•Super Blue•Columbia•1978','\
Eumir Deodato•Rhapsody In Blue / Super Strut•CTI Records•1973','\
Ray Brown•SuperBass•Telarc•1997','\
Ashley Alexander (2)•And His Alumni Band•Mark Records•1980','\
Richard "Groove" Holmes•The Best Of Richard "Groove" Holmes•Prestige•1972','\
Freddie Hubbard•The Best Of Freddie Hubbard•Columbia•1980','\
Eumir Deodato•Deodato 2•CTI Records•1973','\
Native Son•Wind Surfing•JVC•1983'),'\
\
Sure Enough\
':('\
Tom Scott•Sure Enough / The Only One•Elektra Musician•1982','\
Cedar Walton•Eastern Rebellion 4•Timeless Records (3)•1984','\
Various•Casino Lights•Warner Bros. Records•1982','\
Tom Scott•Desire•Elektra Musician•1982','\
Various•Bestseller 1•Clearaudio•1990','\
Peggy Hogan•To Lie With•Not On Label (Peggy Hogan Self-released)•2012','\
DJ Maestro•Blue Note Trip -  Heat Up / Simmer Down•Blue Note•2011','\
Various•Montreux Jazz Festival - 25th Anniversary•Montreux Jazz Festival•1991','\
Quincy Jones•In The Heat Of The Night / They Call Me Mister Tibbs! Soundtrack•Rykodisc•0'),'\
\
Swedish Pastry\
':('\
Stan Hasselgard•Swedish Pastry•Dragon (8)•1978','\
Stan Hasselgard And His All Star Six•Swedish Pastry / Who Sleeps•Capitol Records•1948','\
The Bud Powell Trio•At The Golden Circle Volume 3•SteepleChase•1979','\
Stan Hasselgard•Classics In Jazz•Capitol Records•0','\
Stan Hasselgard•Jammin\' At Jubilee•Dragon (8)•1981','\
Bud Powell•De Face ... Et De Profil•RCA•1960','\
The George Shearing Quintet•A Jazz Date With•MGM Records•1961','\
The Red Norvo Trio•Red Norvo Trio Volume Two•Discovery Records•1953','\
Duke Jordan•Midnight Moonlight•SteepleChase•1980','\
Bud Powell•Swingin\' With Bud•RCA Victor•1958','\
The Bill Evans Trio•At Shelly\'s Manne-Hole Hollywood California•Riverside Records•1965','\
Sarah Vaughan•Sassy Meets Shearing•Camay Records•1962','\
Paul Horn•Sessions Live•Calliope (3)•1976'),'\
\
Sweeping Up\
':('\
Gary Burton•Hotel Hello•ECM Records•1975','\
Lizz Wright•Fellowship•Verve Forecast•2010','\
Mel Tormé•Live At The Maisonette•Atlantic•1975','\
George Gershwin•Music From The Woody Allen Film "Manhattan"•Columbia Masterworks•1979','\
Chris Connor•Chris Connor Sings The George Gershwin Almanac Of Song•Atlantic•1957','\
Ella Fitzgerald•Sings The George And Ira Gershwin Song Book•Verve Records•1959','\
Al Bowlly•Time On My Hands•Saville Records•1987','\
Lena Ericsson•Gershwin - Evergreen! (28 George Gershwin Songs)•Phontastic•1980','\
Various•Classic Gershwin!•CBS Records•1987'),'\
\
Sweet and Loverly\
':('\
Billy Eckstine•The Modern Sound Of Mr. B.•Mercury•1964','\
Ben Cutler And His Orchestra•Debutante Party•MGM Records•0'),'\
\
Sweet Georgia Bright\
':('\
David S. Ware•Surrendered•Columbia•2000','\
Charles Lloyd•In The Soviet Union: Recorded At The Tallinn Jazz Festival•Atlantic•1970','\
Charles Lloyd•Acoustic Masters 1•Atlantic•1994','\
Charles Lloyd•Manhattan Stories•Resonance Records•2014','\
The Charles Lloyd Quartet•Rabo De Nube•ECM Records•2008','\
Cannonball Adderley•Cannonball Adderley-Live!•Capitol Records•1965','\
Charles Lloyd•Jumping The Creek•ECM Records•2005','\
Erik Andresen Quartet•GIP•Flower (2)•1971','\
Jarosław Śmietana•Extra Cream•Jazz Forum Records•1999','\
Charles Lloyd•Discovery!•Columbia•1964','\
Vincent Herring•American Experience•Musicmasters•1992','\
Russell Malone•Sweet Georgia Peach•Impulse!•1998'),'\
\
Sweet Georgia Brown\
':('\
Jazz At The Philharmonic•Norman Granz\' Jazz At The Philharmonic Vol. 3•Mercury•1946','\
Bob Stewart - First Line Band•Goin\' Home•JMT•1989','\
Brother Bones•Sweet Georgia Brown•Harlem Globetrotters•0','\
no artist•M.B.B / Sweet Georgia Brown•Skylark Records (2)•0','\
Johnny Maddox (2)•Sweet Georgia Brown / Dill Pickles•Dot Records•1951','\
Frank Assunto•Whispering / Sweet Georgia Brown•Imperial•0','\
Johnny Maddox (2)•Sweet Georgia Brown / Dill Pickles•Dot Records•1951','\
John Norris (3)•Sweet Georgia Brown / Mexican Hat Dance•Eric Records•1992','\
The Benny Goodman Quartet•Sweet Georgia Brown / Opus ½•no label•0','\
Graeme Bell & His Skiffle Gang•Sweet Georgia Brown / Freight Train•Columbia•1957','\
Harry James And His Orchestra•Ciribiribin / Sweet Georgia Brown•Brunswick•1939','\
The Oscar Peterson Trio•Sweet Georgia Brown / Poor Butterfly•no label•0','\
Jazz At The Philharmonic•Jazz At The Philharmonic•Opera•0'),'\
\
Sweet Henry\
':('\
The Gene Estes Band•Westful - Jazz In Hollywood•Nocturne (3)•1976','\
Gary Burton•Hotel Hello•ECM Records•1975','\
Yoichi Murata Solid Brass•Double Edge•JVC•1996','\
The Ray Charles Singers•Take Me Along!•Command•1968','\
Ralph Marterie And His Orchestra•Young America Dances•Mercury•1957','\
Ted Heath And His Music•Ted Heath At The London Palladium Volume 3•London Records•1955','\
Arthur Lyman•Percussion Spectacular!•HiFi Records•1961','\
Arthur Lyman•Percussion Spectacular!•HiFi Records•1961','\
Various•Perfect For Dancing  Jitterbug Or Lindy•RCA Victor•1955','\
Various•The Soul Of Jazz Volume 3•Verve Records•1995','\
Various•Eight - Hand Sets And Holy Steps•Crossroads Music•1978','\
Sissle & Blake•Vol. 1 Early Rare Recordings•Eubie Blake Music•1973','\
Buddy Greco•From The Wrists Down•Epic•1965','\
Nat King Cole•The Collection•The Red Box•2006','\
Les Brown And His Band Of Renown•Session #55•Doc Hollywood•2000'),'\
\
Sweet Lorraine\
':('\
Artie Shaw And His Strings•Streamline / Sweet Lorraine•Brunswick•1936','\
Lionel Hampton All Stars•Mister Fedor•EmArcy•0','\
The Benny Goodman Quartet•Dizzy Spells / Sweet Lorraine•Victor•1938','\
Art Tatum•Sweet Lorraine / Get Happy•Decca•0','\
Kenny Kersey Trio•JATP Boogie / Sweet Lorraine•Mercury•1951','\
Erroll Garner•Gone With Garner•Brunswick•1953','\
Coleman Hawkins Swing Four•The Man I Love / Sweet Lorraine•Signature (4)•1944','\
Freddie Brocksieper Quintett•Sweet Lorraine / Open The Door Richard •Brunswick•0','\
The Nat King Cole Trio•Sweet Lorraine / Embraceable You•Capitol Records•0','\
Dizzy Gillespie•Always•Disques Vogue•1966','\
Art Tatum•Sweet Lorraine / Lullaby Of The Leaves•Brunswick•0','\
Metronome All Stars•Sweet Lorraine / Nat Meets June•Columbia•1947','\
Dizzy Gillespie•Sweet Lorraine / Dizzy Does It•Jazz Selection•1954'),'\
\
Sweet Love\
':('\
Mark Whitfield•Sweet Sweet Love•Warner Bros. Records•1993','\
Billy Vaughn And His Orchestra•Creole Love Call / Sweet Leilani•Dot Records•1956','\
Coleman Hawkins Swing Four•The Man I Love / Sweet Lorraine•Signature (4)•1944','\
Jimmie Lunceford And His Orchestra•I Love You / Ain\'t She Sweet•Columbia•1948','\
Denise Rich•Sweet Pain Of Love•Foundry Records•1987','\
Stéphane Grappelli•And His American All Stars 1978•Black And Blue•1978','\
Stuff Smith•Black Violin•SABA•1967','\
Bob Crosby And His Orchestra•Pagan Love Song / Come Back Sweet Papa•Decca•1936','\
Steve Khan•Darlin\' Darlin\' Baby (Sweet Tender Love)•Tappan Zee Records•1978','\
Coleman Hawkins•"Inventor" of the Tenor Sax•Coral•1956','\
Paris Reunion Band•French Cooking•Gazell (2)•1985','\
Paul Whiteman And His Orchestra•I\'m In Love With You That\'s Why / Sweet Southern Breeze•Victor•1926','\
Candy Dulfer•For The Love Of You•Ariola•1997','\
Benny Goodman•The Benny Goodman Combo•Victor•0','\
The Camarata Strings•Lost In A Fog / Toot Sweet (It\'s Really Love)•Buena Vista Records•1960','\
Roger Williams (2)•Sweet Pea / Love Me Forever•Kapp Records•1967','\
Lenny Dee (2)•Goodnight Sweet Love / Stormy Weather•Decca•1957','\
Fats Waller & His Rhythm•I\'ve Got A New Lease On Love / Sweet Heartache•Disque Gramophone•1937','\
Terumasa Hino•Live In Warsaw•Century•1991','\
Guy Lombardo And His Royal Canadians•Cannon Ball•Capitol Records•1956'),'\
\
Sweet Rain\
':('\
Stan Getz•Sweet Rain•Verve Records•1967','\
Dee Dee Bridgewater•Sweet Rain•Elektra•1978','\
Dee Dee Bridgewater•Just Family•Elektra•1978','\
no artist•Sweet L\'il / Ain\'t She Sweet / Mississippi Mud / I Left My Sugar Standing In The Rain•Victor•1927','\
Stan Getz Quartet•Portrait•Joker (2)•1977','\
Toshiyuki Miyama & The New Herd•Sunday Thing•Three Blind Mice•1976','\
Duke Pearson•Sweet Honey Bee•Blue Note•1967','\
Cuong Vu 4-tet•Ballet - The Music Of Michael Gibbs•RareNoise Records•2017','\
Robert Greenidge•Heat•MCA Records•1988','\
The Herb Pomeroy Orchestra•Pramlatta\'s Hips (Live At The El Morocco!)•Shiah Records•1980','\
Louis Armstrong And His All-Stars•Swing Low Sweet Satchmo Vol. 1•Brunswick•1959','\
Count Basie Orchestra•Warm Breeze•Pablo Today•1981'),'\
\
Sweetest Sounds\
':('\
Earl Grant•Blue Velvet / The Sweetest Sounds•Decca•1966','\
Ella Fitzgerald•Can\'t Buy Me Love•Verve Records•1964','\
Peggy Lee•The Sweetest Sounds•Capitol Records•1962','\
Billy May And His Orchestra•Love Makes The World Go •Capitol Records•1969','\
Ella Fitzgerald•Hello Dolly•Verve Records•1963','\
Ella Fitzgerald•Hello Dolly•Verve Records•1963','\
Ray Bryant•Groove House•Sue Records Inc.•1963','\
Gildo Mahones•I\'m Shooting High•Prestige•1963','\
Various•No Strings - Original Broadway Cast•Capitol Records•1962','\
Art Farmer•Listen To Art Farmer And The Orchestra•Mercury•1963','\
J.J. Johnson•J.J.\'s Broadway•Verve Records•1963','\
Art Pepper•Goin\' Home•Galaxy•1982','\
Coleman Hawkins Quartet•The Coleman Hawkins Quartet Play The Jazz Version Of No Strings•Moodsville•1962','\
The Lee Evans Trio•The Lee Evans Trio•Capitol Records•1963','\
The George Shearing Quintet•Rare Form!•Capitol Records•1966'),'\
\
Swingin\' Shepherd Blues\
':('\
Ted Heath And His Music•Swingin\' Shepherd Blues•Decca•1958','\
Xavier Cugat And His Orchestra•Swingin\' Shepherd Blues / Watermelon Man•Mercury•1963','\
Jimmy McGriff•The Swingin\' Shepherd Blues•Solid State Records (2)•1967','\
Moe Koffman Quartette•The Swingin\' Shepherd Blues / Hambourg Bound•Jubilee•1958','\
Moe Koffman Quartette•Swingin\' Shepherd Blues / Hambourg Bound•London Records•1958','\
Ella Fitzgerald•The Swingin\' Shepherd Blues / Midnight Sun•no label•1957','\
Ken Mackintosh And His Orchestra•The Stroll / The Swingin\' Shepherd Blues•Electrola•1958','\
Ted Heath And His Music•No.5•Decca•0','\
Ella Fitzgerald•Teach Me How To Cry•Verve Records•1958','\
Moe Koffman•Swingin\' Shepherd Blues Twist / Train Whistle Twist•Ascot Records•1962','\
Ella Fitzgerald•Hotta Chocholata / So In Love•Barclay•0','\
Jimmy Smith•Six Views Of The Blues•Blue Note•1999'),'\
\
T.B.C.\
':('\
The Victor Feldman Trio•To Chopin With Love•Hindsight Records•1997','\
Anton Eger•Æ•Edition Records Ltd.•2019','\
Tomasz Stańko•Balladyna•GOWI Records•1994','\
Anthony Braxton•Anthony Braxton · Robert Schumann String Quartet•Sound Aspects Records•1986','\
FLOOR BABA•Gamewave•DESKPOP•2015','\
Frankie Jaxon•Complete Recorded Works In Chronological Order Volume 1 (14 May 1926 to 22 July 1929)•Document Records (2)•1994','\
Art Blakey & The Jazz Messengers•The History Of Art Blakey And The Jazz Messengers•Blue Note•1991','\
Hatfield And The North•The Rotters\' Club•Virgin•1975','\
Karlheinz Kästel•Lieben Sie Gitarre?•Hit-Ton Schallplatten•1966','\
Helen Shapiro•Simply Shapiro•Katalyst Records•2000'),'\
\
Tadd\'s Delight\
':('\
Fats Navarro•At The Royal Roost 1948 (Volume 2)•Beppo Records•0','\
Fats Navarro•Fats Navarro Featured With The Tadd Dameron Quintet•JAZZLAND•1961','\
Fats Navarro•Blowing At The Royal Roost•Ediciones Del Prado•1996','\
Philly Joe Jones Octet•Filet De Sole•Marge•1992','\
Barry Harris (2)•Barry Harris Plays Tadd Dameron•Xanadu Records•1975','\
Fats Navarro•Fats Navarro•Giants Of Jazz•1986','\
Fats Navarro•Fats Blows•Past Perfect Silver Line•2000','\
Fats Navarro•Modern Giants Of Jazz•Ozone (4)•0','\
Fats Navarro•Royal Roost Sessions 1948•Fresh Sound Records•1991','\
Fats Navarro•Featured With The Tadd Dameron Band•Milestone (4)•1977','\
Various•Dazzling Jazz - Modern•Philips•0','\
Miles Davis•The Original Mono Recordings•Columbia•2013','\
Miles Davis•Just Squeeze Me•Documents•2006'),'\
\
Take Five\
':('\
Various•A Collection Of Various Interpretations Of Take Five•Roof Music•2003','\
Reggae Clinic 65•Take Five / Caravan / Wheels•International Bestseller Company•1979','\
Aura Urziceanu•Take Five•Electrecord•1973','\
The Mol Percussion Band•Percussion-Polka / Take Five•Monopole•1979','\
Fausto Papetti•Take Five / Always•Durium•1968','\
Carmen McRae•Take Five / Dat Dere•Jazzman•2004','\
The Dave Brubeck Quartet•Take Five / Unsquare Dance•CBS•1969','\
Jacky Terrasson•Take This•Impulse!•2015','\
Dave Brubeck•Take Five•Atlantic•0','\
The Dave Brubeck Quartet•Experiments In Time - Vol. 2•Fontana•0','\
Dave Brubeck•Take Five / It\'s A Raggy Waltz•CBS•1976','\
Carmen McRae•Take Five•Columbia•1962','\
Dave Lee (7)•Take Four / Five To Four On•Decca•1963','\
Lloyd Trotman & His Orchestra•Take Five / Trottin\' In•Brunswick•1959','\
Al Jarreau•Take Five / Loving You•Warner Bros. Records•1977','\
The Dave Brubeck Quartet•Time Out Volume 1•CBS•0','\
Dave Brubeck•Dave Brubeck In Berlin•CBS•1964','\
Dave Brubeck•Take Five / Three To Get Ready•Atlantic•0','\
Sachal Studios Orchestra•Take Five•Sachal Music•2008','\
The Dave Brubeck Quartet•Take Five / Blue Rondo A La Turk•Columbia•1959'),'\
\
Take the "A" Train\
':('\
Aura Urziceanu•Take Five•Electrecord•1973','\
Duke Ellington And His Orchestra•Take The "A" Train / The Mooche•Philips•0','\
The Duke Ellington Orchestra•Perdido•GRP•1987','\
Duke Ellington And His Orchestra•Take The "A" Train / Satin Doll•Columbia•0','\
Clifford Brown And Max Roach•Study In Brown Vol.1•EmArcy•1957','\
Duke Ellington And His Orchestra•Perdido / Take The "A" Train•Columbia•1952','\
Johnny Lytle Trio•Lela / Take The "A" Train•JAZZLAND•1961','\
Sonny Stitt•In A Sentimental Mood / Take The "A" Train•Catalyst Records (3)•1977','\
The Pud Brown Trio•Take The "A" Train / Memories Of You•Capitol Records•1953','\
The Dave Brubeck Quartet•Take The "A" Train•Philips•1962','\
The Oscar Pettiford Quartet•Take The "A" Train / Blues For Blanton•Mercer Records•1950','\
Ernst Höllerhagen Quartett•Take The "A" Train / Sentimental Journey•Elite Special•1945','\
Dave Brubeck•Dave Brubeck In Berlin•CBS•1964','\
no artist•Chattanooga Choo Choo / Take The "A" Train•Capitol Records•1975','\
Glenn Miller And His Orchestra•Take The "A” Train / Slip Horn Jive	•no label•1944','\
Duke Ellington And His Orchestra•Ellingtonia - Vol. 5 “New Recordings Of Great Standards”•Philips•1961','\
World Saxophone Quartet•Plays Duke Ellington•Nonesuch•1986','\
Jimmy Forrest•Heart Of The Forrest•Palo Alto Records•1982'),'\
\
Takin\' It To The Streets\
':('\
Take 6•Takin\' It To The Streets•Warner Bros. Records•2002','\
Jay Hoggard•Days Like These•GRP•1979','\
Eric Marienthal•Turn Up The Heat•Peak Records (5)•2001','\
Take 6•Beautiful World•Warner Bros. Records•2002','\
Quincy Jones•Sounds ... And Stuff Like That!!•A&M Records•1978','\
Donald Fagen•Live At Lincoln Center - The Dukes Of September•429 Records•2014'),'\
\
Taking A Chance On Love\
':('\
Eddie Calvert•Taking A Chance On Love / Serenade•Capitol Records•1956','\
Ella Fitzgerald•Moanin\' Low•Decca•1955','\
The Four Lads•Side By Side / Taking A Chance On Love•Philips•0','\
Gerry Mulligan Tentette•Gerry Mulligan And His Ten-Tette Part 1•Capitol Records•1954','\
Eydie Gormé•Taking A Chance On Love•ABC-Paramount•1959','\
Nellie Lutcher•Taking A Chance On Love / The St. Louis Blues•Philips•0','\
Ella Fitzgerald And Her Famous Orchestra•Cabin In The Sky / Taking A Chance On Love•Decca•1940','\
Billy Eckstine•Taking A Chance On Love / You\'re Driving Me Crazy!•MGM Records•1951','\
Ray Anthony•Golden Horn (EP Pt.3)•Capitol Records•1955','\
Benny Goodman And His Orchestra•Cabin In The Sky / Taking A Chance On Love•Columbia•1943','\
Paul Smith Quartet•Softly Baby - Part 2•Capitol Records•1958','\
Frank Sinatra•Swing Easy! Part 2•Capitol Records•1954','\
Bobby Short•Let There Be Love•Kapp Records•0','\
Teddy Wilson Trio•Teddy Wilson Trio•Metronome•1953','\
The George Shearing Quintet•Taking A Chance On Love•MGM Records•1958','\
Tony Bennett•I Left My Heart In San Francisco•CBS•1964','\
Ella Fitzgerald•Sweet And Hot (Part 3)•Brunswick•1956'),'\
\
Tangerine\
':('\
Tommy Dorsey And His Orchestra•Tangerine / Who•Bell Records•1954','\
Ahmad Jamal•Seleritus•Argo (6)•1959','\
Tommy Dorsey And His Orchestra•Tangerine / Silk Stockings•Bell Records•1957','\
Stan Getz Quintet•Interpretations By The Stan Getz Quintet #2•Norgran Records•1954','\
Jimmy Dorsey And His Orchestra•Tangerine / Ev\'rything I Love•Decca•1942','\
Cal Tjader•Love Me Or Leave Me•Savoy Records•0','\
Jimmy Dorsey And His Orchestra•It Happened In Hawaii / Tangerine •Decca•1947','\
Zoot Sims All-Stars•Contemporary Music•Prestige•1953','\
Oliver Nelson•Main Stem•Prestige•1962','\
Benny Goodman And His Orchestra•Love Walked In / Ramona / Soft As Spring / Tangerine•Philips•0','\
Willy Girard•Jazz Violin•Radio Canada International•1970','\
Dexter Gordon•Tangerine•Prestige•1975','\
Vaughn Monroe And His Orchestra•Tangerine / Tica Ti-Tica Ta•Bluebird (3)•1942','\
Buddy Tate•Live At Sandy\'s•Muse Records•1980','\
Cal Tjader•Love Me Or Leave Me•Savoy Records•1953','\
Stan Getz Quintet•Interpretations By The Stan Getz Quintet #2•Norgran Records•1954'),'\
\
Tautology\
':('\
Lee Konitz•Lee Konitz Quintet With Warne Marsh•Prestige•1954','\
Lee Konitz Quintet•Lee Konitz Quintet / Lennie Tristano Quintet•New Jazz•1951','\
Various•First Sessions 1949/50•Prestige•1978','\
Lee Konitz•Subconscious-Lee•Prestige•1955','\
Meinrad Kneer Quintet•Oneirology•Jazz Haus Musik•2015','\
Lennie Tristano•1947-1951•Classics (11)•2003','\
Anthony Braxton•Quintet (Tristano) 1997•New Braxton House•2012'),'\
\
Tea For Two\
':('\
Jazz At The Philharmonic•Norman Granz\' Jazz At The Philharmonic Volume Seven •Mercury•1947','\
Tommy Dorsey And His Orchestra•Tea For Two Cha Cha•MCA Records•0','\
Norrie Paramor And His Orchestra•Tête à Tête•Columbia•1958','\
Earl Hines Quintet•Chicago / Tea For Two•Royal Jazz (2)•1949','\
Ingelise Rune Med Soft-bar-kvintet•Stardust / Tea For Two•Tono•0','\
The Bud Powell Trio•Hallelujah / Tea For Two•Mercury•0','\
Johnny Hodges And His Orchestra•Tea For Two / Rosanne•Blue Star•0','\
The Dave Brubeck Trio•Blue Moon / Tea For Two•Coronet (5)•1949','\
Svend Asmussens Skandia Trio•Tea For Two / Melancholy Baby•Odeon•0','\
Unknown Artist•La Borrachita•Hoctor Records•0','\
Charlie Ventura And His Orchestra•Tea For Two•RCA Victor•1950','\
The Benny Goodman Quartet•Runnin\' Wild / Tea For Two•Victor•1937','\
The Benny Goodman Quartet•Vibraphone Blues / Tea For Two•no label•0','\
Art Tatum•Deep Purple / Tea For Two•Decca•1939','\
Bob Crosby And His Orchestra•Louise Louise / Tea ForTwo•Brunswick•0','\
Cecil Young Quartet•Monsieur Le Duc / Tea For Two•King Records (3)•0','\
The Oscar Peterson Trio•Serenade In Blue•Clef Records•1955','\
Hans Koller New Jazz Stars•I\'ll Remember April / Tea For Two•Harmona 3D•1955'),'\
\
Teach Me Tonight\
':('\
Count Basie Orchestra•My Baby Upsets Me / Teach Me Tonight•Verve Records•1956','\
Bop-A-Loos•South Park Way Mambo / Teach Me Tonight•Oldies 45 (4)•0','\
The Modernaires•Mood Indigo / Teach Me Tonight•Coral•0','\
Sarah Vaughan•The Big Three•Roulette•0','\
Dinah Washington•Teach Me Tonight  / Wishing Well•Mercury•1954','\
Al Jarreau•Teach Me Tonight / Easy•Warner Bros. Records•1981','\
Marian Montgomery•When Sunny Gets Blue•Capitol Records•0','\
Phil Tate & His Music•The Sound Of Dancing•IDTA•1969','\
Phil Tate & His Music•Cha Cha Chas / Tangos•IDTA•1969','\
Bop-A-Loos•South Parkway Mambo / Teach Me Tonight•Mercury•0','\
Ralph Sharon Quartet And Friend•2:38 a.m.•Argo (6)•1958','\
Erroll Garner•Erroll Garner•Columbia•0','\
Jaki Byard•The Jaki Byard Experience•Prestige•1969','\
Jimmy McGriff•City Lights•Jam (15)•1981','\
Gene Ludwig Trio•Organ Out Loud•Mainstream Records•1965','\
Joey DeFrancesco•Plays Sinatra His Way•HighNote Records Inc.•2004','\
Nat King Cole•Nat "King" Cole Sings•Capitol Records•1954','\
Jo Stafford•Jo Stafford Con Paul Weston E La Sua Orchestra•Philips•0'),'\
\
Teenie\' Blues\
':('\
Sam Butera And The Witnesses•Apache•Dot Records•1961','\
Hazy Osterwald Sextett•Latin Trumpet•Polydor•1965','\
Sam Butera And The Witnesses•The Wildest Clan/Apache!•Jasmine Records•1998','\
Marty Wilson And His Orchestra•Young America Dances To The Golden Goodies•20th Century Fox Records•0'),'\
\
Tell Me a Bedtime Story\
':('\
Mark Whitfield•Raw•Transparent Music•2000','\
KUDU (2)•Kudu•Velour Recordings•2001','\
Herbie Hancock•Treasure Chest•Warner Bros. Records•1974','\
Herbie Hancock•Fat Albert Rotunda•Warner Bros. - Seven Arts Records•1969','\
Herbie Hancock•Ken Burns Jazz•Columbia•2000','\
Billy Childs Trio•Bedtime Stories (A Tribute To Herbie Hancock)•32 Jazz•2000','\
Kimiko Kasai•Butterfly•CBS/Sony•1979'),'\
\
Tenderly\
':('\
The Oscar Peterson Trio•Tenderly•Verve Records•0','\
Oscar Peterson•Debut / Tenderly•Mercury•1952','\
Ray Anthony & His Orchestra•Tenderly / Autumn Nocturne•Capitol Records•0','\
Nat King Cole•Tenderly / Why•Capitol Records•1953','\
Gene Norman•In Concert 1•Vogue Records•1955','\
Georgie Auld•Harlem Nocturne / Tenderly•Coral•0','\
Randy Brooks And His Orchestra•Lamplight / Tenderly•Decca•1947','\
Norman Luboff Choir•Laura / Tenderly•Philips•0','\
Stan Kenton And His Orchestra•The Creep / Tenderly•Capitol Records•1954','\
Paul Quinichette•Jazz Studio 1•Decca•1954','\
Eddie "Lockjaw" Davis Trio•Tenderly / Dizzy Atmosphere•King Records (3)•0','\
Ben Webster And His Orchestra•Pennies From Heaven / Tenderly•Norgran Records•1954'),'\
\
Tenor Madness\
':('\
Bo Wärmell•Blue Train/Rue Chaptal•Jazz Records (2)•1962','\
Dexter Gordon Quartet•Swiss Nights Vol. 1•SteepleChase•1976','\
Sonny Rollins•Road Shows Vol 1•Doxy Records•2008','\
Jamey Aebersold•Sonny Rollins Nine Classic Jazz Originals•JA Records•1976'),'\
\
That Certain Feeling\
':('\
Pearl Bailey•Hit The Road To Dreamland / That Certain Feeling •London Records•1956','\
Les Brown And His Band Of Renown•Hit The Road To Dreamland•Capitol Records•0','\
Pearl Bailey•Zing Went The Strings Of My Heart•Sunset Records (12)•1956','\
Pearl Bailey•Travelling With Pearl Bailey•Egmont Viking•0','\
Karin Krog•As You Are (The Malmö Sessions)•RCA Victor•1977','\
Ran Blake•That Certain Feeling (George Gershwin Songbook)•hat ART•1991','\
George Gershwin•George Gershwin At The Piano•Ember Records International Ltd•1958','\
Pearl Bailey•Around The World With Me•Guest Star•0','\
George Gershwin•George Gershwin At The Piano•Ember Records International Ltd•1958','\
George Gershwin•Plays The Rhapsody In Blue•20th Fox•1958','\
Cleo Laine•Portrait•Philips•1971','\
Jack Trombey•Sliced Orange•Music De Wolfe•1975','\
Monica Borrfors•A Certain Sadness•Arietta Discs•2002','\
Ella Fitzgerald•Ella Fitzgerald Sings The George And Ira Gershwin Song Book (Volume Two)•Verve Records•1959','\
Newton Wayland Denver Symphony Pops•George Gershwin Plays Rhapsody In Blue•K-Tel•1988','\
Pearl Bailey•Singing & Swinging•Coronet Records•1960'),'\
\
That Girl\
':('\
Mark Whitfield•That Girl•Warner Bros. Records•1993','\
no artist•That Girl•Mercury•1954','\
Irving Fields Trio•That Wonderful Girl Of Mine•RCA Victor•1949','\
Tony Ray•Bossa Nova Baby / Here Comes That Girl Again•Imperial•0','\
Ziggy Elman & His Orchestra•Cheek To Cheek / That Wonderful Girl Of Mine•MGM Records•1949','\
Esthero•That Girl•Work•1999','\
Benny Goodman And His Orchestra•The Huckle-Buck / That Wonderful Girl Of Mine•Capitol Records•1949','\
Benny Strong And His Orchestra•That Certain Party / My Best Girl•Tower (7)•1948','\
Paul Whiteman And His Orchestra•Why Did I Kiss That Girl? / California Here I Come•Victor•1924','\
Elvis Costello•I Still Have That Other Girl b/w The Sweetest Punch•Decca•1999','\
Eddy Howard And His Orchestra•Brother Bill / The Girl That I Marry•Mercury•1950','\
Benny Strong And His Orchestra•That Certain Party / My Best Girl•Tower (7)•1948','\
Skitch Henderson & His Orchestra•The Girl That I Marry•Columbia•1968','\
Skitch Henderson & His Orchestra•The Girl That I Marry•Columbia•1968','\
Nat Shilkret And The Victor Orchestra•My Varsity Girl I\'ll Cling To You / Blossoms That Bloom In The Moonlight•Victor•1928','\
Frank Sinatra•They Say It\'s Wonderful / The Girl That I Marry•Columbia•1946','\
The Duke Pearson Nonet•Honeybuns•Atlantic•1966','\
Tanzorchester Horst Wende•Im Strickten Tanz-Rhythmus Charleston•Polydor•1966'),'\
\
That Old Feeling\
':('\
The King Sisters•Easy To Love•Capitol Records•1957','\
Lena Horne•That Old Feeling / Sweet Thing•RCA Victor•1957','\
Artie Shaw And His Gramercy Five•Besame Mucho•Bell Records•1952','\
Chet Baker•That Old Feeling / My Buddy•Pacific Jazz•1956','\
Side Effect•Keep That Same Old Feeling•Fantasy•1977','\
The Crusaders•Keep That Same Old Feeling•ABC Records•1976','\
Louis Armstrong•Nobody Knows The Trouble I\'ve Seen •Verve Records•1960','\
Connie Boswell•Whispers In The Dark / That Old Feeling•Decca•1937','\
Frank Sinatra•Nice \'n Easy (Part 1)•Capitol Records•1960','\
Albert Dailey Trio•That Old Feeling•SteepleChase•1979','\
Frank Sinatra•Nice \'n Easy (Part 1)•Capitol Records•1960','\
Ella Fitzgerald•That Old Feeling / A Guy Is A Guy•Decca•0','\
Artie Shaw And His Gramercy Five•Artie Shaw And His Gramercy Five•Jazztone (2)•0','\
Lee Richardson (4)•As Time Goes By / That Old Feeling•DeLuxe (2)•1955','\
Joe Loss And His Band•That Old Feeling / You Can\'t Stop Me From Dreaming•Regal Zonophone•1938'),'\
\
That Sunday That Summer\
':('\
Nat King Cole•Those Lazy-Hazy-Crazy Days Of Summer / That Sunday That Summer•Capitol Records•0','\
Betty Carter•Look What I Got•Verve Records•1988','\
Diana Panton•Solstice / Equinox•Diana Panton•2017','\
Nicki Parrott•Summertime•Venus Records (5)•2012','\
The George Shearing Quintet•Back to Birdland•Telarc Jazz•2001','\
Ernestine Anderson•Boogie Down•Concord Jazz•1990','\
Nat King Cole•An Evening With Nat King Cole•HG Associates•1995','\
Joe Sherman And His Orchestra•The Seventh Dawn•World Artists (4)•0','\
The Bernie Lowe Orchestra•Encore•Cameo•0','\
Sam Fletcher•Sings I Believe In You•Vee Jay Records•1964','\
Dinah Washington•In Tribute•Roulette•1964','\
Bobby Martin And His Orchestra•Great Smash Hits•Columbia•0','\
Various•The Five Songbirds: A Reference Collection of Female Voices•First Impression Music•2005','\
Various•Best Of The Jazz Vocalists•Compact Jazz•1992','\
Kathie Lee Gifford•Sentimental•Warner Bros. Records•1993'),'\
\
That\'s All\
':('\
Etta Jones•That\'s All There Is To That / Canadian Sunset•Prestige•1961','\
Louis Armstrong And His All-Stars•Long Gone / All That Meat And No Potatoes•Philips•0','\
Catherine Zeta Jones•Music From The Miramax Motion Picture Chicago •Epic•2003','\
Mal Waldron•Spanish Bitch•Globe (9)•1970','\
Dinah Shore•Two Silhouettes / All That Glitters\' Is Not Gold•Columbia•0','\
Fats Waller & His Rhythm•All That Meat And No Potatoes•no label•1954','\
Ralph Marterie And His Orchestra•All That Oil In Texas / The Love For Three Oranges•Mercury•1954','\
Dean Martin•Love Is All That Matters / Simpatico•Capitol Records•1955','\
Benny Carter•A Man Called Adam•Reprise Records•1966','\
Roy Eldridge And His Orchestra•All The Cats Join In / Ain\'t That A Shame•Decca•1946','\
Jimmy Sacca•Alone / You\'re All That I Need•Dot Records•0','\
Mel Tormé•All That Jazz•Columbia•0','\
Louis Armstrong•Blueberry Hill / That Lucky Old Sun•Decca•1949','\
Pat Martino•The Return•Muse Records•1987','\
The Red Garland Quintet•All Mornin\' Long•Prestige•1958','\
Skitch Henderson & His Orchestra•The Girl That I Marry•Columbia•1968','\
Vario 34•Vario-34•Blue Tower Records•1995'),'\
\
That\'s What Friends Are For The Aerie\
':('\
Carl Doy•Moonlight Piano•Columbia•1991','\
Billie Holiday•The Gold Collection: 40 Classic Performances •Retro (2)•1995','\
Billie Holiday•The Legendary Masters Unissued Or Rare 1935-58•Recording Arts Reference Edition•0','\
Dizzy Gillespie•Bebop Legends•The Franklin Mint Record Society•1984','\
Trijntje Oosterhuis•Collected•Universal Music•2015','\
Burt Bacharach•The Look Of Love - The Burt Bacharach Collection•Warner Strategic Marketing•2001','\
Ella Fitzgerald•30 By Ella•Capitol Records•1968','\
Chet Baker Quartet•The Complete Pacific Jazz Studio Recordings Of The Chet Baker Quartet With Russ Freeman•Mosaic Records (2)•1987'),'\
\
The Double Up\
':('\
Lee Morgan•Charisma•Blue Note•1969','\
Tony Lakatos•The News•Jazzline•1995','\
André Previn•Double Play!•Contemporary Records•1957','\
Si Zentner And His Orchestra•Right Here! Right Now! The Big Mod Sound Of•Liberty•1967','\
Stacey Kent•I Know I Dream: The Orchestral Sessions•Okeh•2017','\
Freddie Green•Mr. Rhythm•RCA Victor•1956','\
Daniel Smith (7)•Blue Bassoon•Summit Records (3)•2009','\
Hate Fuck Trio•You Know For Kids•Shaky Records•1997','\
Vic Godard•What\'s The Matter Boy?•MCA Records•1980','\
The Midnite Follies Orchestra•Hotter Than Hades•Odeon•1978','\
Various•Jazz: For Absolute Beginners•RCA Victor•1986','\
The Midnite Follies Orchestra•Hotter Than Hades•Odeon•1978'),'\
\
Them There Eyes\
':('\
Don Byas Quintet•Deep Purple / Them There Eyes•Jamboree Records (2)•1945','\
Teddy Wilson•Smoke Gets In Your Eyes / Them There Eyes•Columbia•0','\
Billie Holiday•My Man - Them There Eyes•United Artists Records•0','\
The Hollywood Hucksters•Them There Eyes / Happy Blues•Telefunken Capitol•0','\
Billie Holiday•Them There Eyes / Body And Soul•Columbia•1947','\
Varetta Dillard•Them There Eyes / You Are Gone•Savoy Records•1952','\
The Dutch Swing College Band•Them There Eyes / Cake Walkin\' Babies Back Home•Philips•1952','\
Milt Buckner•I Giganti Del Jazz Vol. 13•Curcio•1980','\
Earl Hines•In Paris•America Records•1971','\
The Rob McConnell Jive 5•The Rob McConnell Jive 5•Concord Jazz•1990','\
Milt Buckner•Them Their Eyes•Black And Blue•0','\
Dave Pell Octet•A Pell Of A Time•RCA Victor•1957','\
Teddy Wilson•Teddy Wilson And His Piano•Columbia•1950','\
Bill Coleman & His Orchestra•Metro Jazz•Columbia•0','\
Quintette Du Hot Club De France•The Quintet Of The Hot Club Of France - Volume 2•Decca•1943'),'\
\
Theme for Ernie\
':('\
The Frank Foster Quintet•Chiquito Loco•Bingow Records•1979','\
Cedar Walton•The Trio 2•Red Record•1986','\
Tete Montoliu Trio•Tete!•SteepleChase•1975','\
Doug Raney Quintet•Lazy Bird•SteepleChase•1985','\
Ricard Roda•Nits De Jazz Al Jamboree•Edigsa•1968','\
Frank Foster•Shiny Stockings•Sony•1998','\
John Coltrane•Soultrane•Prestige•1958'),'\
\
Theme From Mr. Broadway\
':('\
The Dave Brubeck Quartet•Jazz Impressions Of New York•Columbia•1965','\
Oliver Nelson•More Blues And The Abstract Truth•Impulse!•1964','\
Bill Evans•"Theme From The V.I.P.s" And Other Great Songs•MGM Records•1963','\
The Crusaders•Heat Wave•Pacific Jazz•1963','\
Dave Brubeck•Dave Brubeck•Supraphon•1971','\
Dave Brubeck•Dave Brubeck•Europa•0'),'\
\
Then I\'ll Be Tired Of You\
':('\
Various•Slow Dancing Through The Years•Sony Music Special Products•1994','\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014'),'\
\
There is No Greater Love\
':('\
Billy May And His Orchestra•There Is No Greater Love / Always•Capitol Records•1952','\
Billie Holiday•There Is No Greater Love / Solitude•Decca•1947','\
Jimmy Dorsey And His Orchestra•Heartaches / There Is No Greater Love•MGM Records•1947','\
Billy May And His Orchestra•There Is No Greater Love / Always•Capitol Records•0','\
The Miles Davis Quintet•Miles\' Theme•Esquire•1960','\
Duke Ellington And His Orchestra•Isn\'t Love The Strangest Thing / (There Is) No Greater Love•Brunswick•1936','\
Eddie Lockjaw Davis Quartet•All Of Me•Steeplechase•1994','\
Booker Ervin•The Space Book•Prestige•1965','\
Circle (5)•Circle-1 Live In German Concert•CBS/Sony•1971','\
Stan Kenton And His Orchestra•There Is No Greater Love / Across The Alley From The Alamo•Capitol Records•1947','\
no artist•Sacred Love•Sound Aspects Records•1988','\
Eddie Daniels•Brief Encounter•Muse Records•1980','\
McCoy Tyner Trio•Inception•Impulse!•1962','\
Frank Rosolino And His Quartet•Frank Talks!•Storyville•1998'),'\
\
There Will Never Be Another You\
':('\
Louis Smith (2)•Smithville•Blue Note•1958','\
Lionel Hampton Quintet•Where Or When / There Will Never Be Another You•Decca•0','\
Jesse Morrison•Tell Me Can You Feel It / There Will Never Be Another You•Abet•1975','\
Cal Tjader•Sessions Live•Calliope (3)•1976','\
Chet Baker•The Rising Sun Collection•Just A Memory•1996','\
Hank Mobley•Monday Night At Birdland•Roulette•1959','\
Teddy Powell And His Orchestra•A Boy In Khaki-A Girl In Lace / There Will Never Be Another You•Bluebird (3)•1942','\
Mathilde Santing•Too Much•Megadisc•1985','\
Chris Montez•There Will Never Be Another You•A&M Records•1966','\
Sonny Rollins•On The Outside•Bluebird (3)•1990','\
The Four Freshmen•4 Freshmen And 5 Trumpets Part 3•Capitol Records•0','\
Dexter Gordon•Blues Walk! The Montmartre Collection Vol. II•Black Lion Records•1974','\
Gerry Mulligan•Carnegie Hall Concert Volume 2•CTI Records•1979','\
The George Benson Quartet•Live At "Casa Caribe" Volume 1•Jazz View•0','\
George Benson•Witchcraft•Jazz Hour•1999'),'\
\
There\'s A Lull In My Life\
':('\
Nat King Cole•Nat King Cole Sings / George Shearing Plays•Capitol Records•1962','\
Nat King Cole•Nat King Cole Sings / George Shearing Plays•Capitol Records•1962','\
Nat King Cole•A Many Splendored Thing•Longines Symphonette Society•1965','\
Chet Baker•Embraceable You•Pacific Jazz•1995','\
Kay Starr•The Uncollected 1949 Vol. 2•Hindsight Records (2)•1986','\
Chet Baker•Chet Baker Sextet / Embraceable You•Pacific Jazz•2004','\
Natalie Cole•Stardust•Elektra•1996'),'\
\
There\'s A Small Hotel\
':('\
Hal Singer•Milt And Hal•Barclay•1968','\
Billy Taylor Trio•The New Billy Taylor Trio•ABC-Paramount•1958','\
Abe Most•Mister Clarinet•Liberty•1955','\
Teddy Sommer•The Dancing 30\'s In Percussion•Grand Prix Series•0','\
Ted Mazio Percussion Group•Dancing Percussion Music Of The 30\'s•International Award Series•1961','\
Charlie Applewhite•Our Love Affair•Design Records (2)•1958','\
Various•Rodgers & Hart Gems•Pacific Jazz•1992','\
Chet Baker•Plays And Sings•World Pacific Jazz•1968','\
Sachal Vasandani•We Move•Mack Avenue•2009','\
Claude Williamson•In Italy•Broadway International•0','\
Chet Baker•Verve Jazz Masters 32•Verve Records•1994','\
Various•The Big Band Era: Volume 10: The Passing Of The 40\'s•Omega (6)•1978','\
Stéphane Grappelli•Just One Of Those Things•EMI•1984','\
Stan Getz•Intoit•Past Perfect Silver Line•0','\
Bill Snyder•Sweet And Lovely•Brunswick•1958'),'\
\
There\'s No You\
':('\
Miles Davis•Blue Moods•Debut Records (3)•1959','\
Frank Sinatra•Where Are You? Part 4•Capitol Records•1956','\
Oscar Peterson•Live At The Northsea Jazz Festival The Hague Holland 1980•Pablo Live•1981','\
Frank Rosolino And His Quartet•Frank Talks!•Storyville•1998','\
Whispering Jack Smith•There Ain\'t No Maybe In My Baby\'s Eyes / No One But You Knows How To Love•Victor•1927','\
Johnny Griffin•The Congregation•Blue Note•1958','\
Eddie Lockjaw Davis Quartet•All Of Me•Steeplechase•1994','\
Earl Hines•I Giganti Del Jazz Vol. 95•Curcio•0','\
Chet Baker•Out Of Nowhere•Milestone (4)•1991','\
David John Pratt•Samba Fusion Flight No. 064•Philips•1985','\
Rita Reys•There Is No Greater•Philips•0','\
Lee Konitz•Lee Konitz Chet Baker Keith Jarret Quintet•Jazz Connoisseur•0','\
Claude Williams Quintet•Call For The Fiddler•SteepleChase•1976','\
Frank Rosolino•Just Friends•MPS Records•1977'),'\
\
These Foolish Things\
':('\
Red Callender Sextet•These Foolish Things / Get Happy•Sunset Recordings (3)•1945','\
Rod Stewart•These Foolish Things•BMG•2002','\
Art Pepper Quartet•These Foolish Things / Brown Gold•Discovery Records•1952','\
Benny Goodman Sextet•Six Appeal / These Foolish Things•Odeon•0','\
Earl Bostic And His Orchestra•Mambostic / These Foolish Things•Parlophone•1954','\
Thelonious Monk Trio•Trinkle Tinkle / These Foolish Things•Prestige•1953','\
Lester Young And His Band•These Foolish Things / Jumpin\' At Mesners\'•Philo Recordings•1946','\
Lester Young And His Band•These Foolish Things / Lester\'s Be-Bop Boogie•Esquire•0','\
Thelonious Monk Trio•Bemsha Swing•Barclay•1960','\
The Harry Edison Quartet•"Sweets" At The Haig•Pacific Jazz•1953','\
Harry James And His Orchestra•More Harry James In Hi-fi (Part 4)•Capitol Records•1956'),'\
\
They All Laughed\
':('\
Carmen McRae•Keep Me In Mind•Decca•0','\
Ella Fitzgerald•Ella And Louis Again Part 2•Verve Records•0','\
Ken McIntyre•Looking Ahead•Prestige•1961','\
Bing Crosby•Bing Sings Whilst Bregman Swings•Verve Records•1956','\
Dakota Staton•Dynamic! Part 3•Capitol Records•0','\
Manny Albam And His Jazz Greats•Jazz Horizons: Jazz New York•Dot Records•1959','\
The Nick Travis Quintet•The Panic Is On•RCA Victor•1954','\
Eric Dolphy•Fire Waltz•Prestige•1978','\
The George Shearing Quintet•Rare Form!•Capitol Records•1966','\
George Shearing•Masters Of Jazz 2•Capitol Records•1976'),'\
\
They Can\'t Take That Away From Me\
':('\
Ada Rovatti•Under The Hat•Apria Records•2003','\
Charlie Byrd•1961-1962•Sarpe•1990','\
Tony Bennett•Love Is Here To Stay•Verve Records•2018','\
Dizzy Gillespie•Dizzy In Paris / 1952-1953•Barclay•1980','\
Stacey Kent•Dreamer In Concert•Blue Note•2012','\
Billie Holiday•Greatest Hits•Columbia•1995','\
Polly Bergen•Act One Sing Too•Philips•1963','\
Charlie Parker•Charlie Parker•Nocturne•2003','\
Various•Slow Dancing Through The Years•Sony Music Special Products•1994'),'\
\
Things Ain\'t What They Used To Be\
':('\
Elsie Bianchi Trio•At Chateau Fleur De Lis•Sonorama•2017','\
Duke Ellington•Duke Ellington\'s Greatest Hits•Harmony (4)•1971','\
Duke Ellington And His Orchestra•Harlem•Pablo Live•1985','\
Kansas City Stompers•Giants Of Swing•Storkophon•1981','\
Steve Allen (3)•At The Piano•Fresh Sound Records•1987','\
The Clark Terry Five•Memories Of Duke•Pablo Today•1980','\
Cootie Williams And His Orchestra•Cootie Williams And His Orchestra•Storyville•0','\
Earl Hines•Fatha & His Flock On Tour•MPS Records•0','\
Various•Une Histoire Des Maitres Du Jazz / A Story Of Jazz Masters•CBS•1975','\
Duke Ellington And His Orchestra•S.R.O.•Lester Recording Catalog•1985'),'\
\
Things to Come\
':('\
Dizzy Gillespie And His Orchestra•Things To Come / Emanon•Musicraft•1947','\
Dizzy Gillespie And His Orchestra•One Bass Hit / Things To Come•Parlophone•1946','\
George Benson•Shape Of Things To Come•A&M Records•1968','\
The Dizzy Gillespie Reunion Big Band•20th And 30th Anniversary•MPS Records•1969','\
Dizzy Gillespie And His Orchestra•Things To Come•MGM Records•1953','\
Sarah Vaughan•I Giganti Del Jazz Vol. 2•Curcio•1980','\
Dizzy Gillespie•Dizzy Gillespie Plays•Allegro (2)•0','\
George Benson•Shape Of Things To Come•A&M Records•1968','\
Passport (2)•Looking Thru•Atlantic•1973','\
Earl Anderza•Outa Sight•Pacific Jazz•1963','\
Manhattan Jazz Quintet•My Favorite Things - Live In Tokyo •Paddle Wheel•1987'),'\
\
Think On Me\
':('\
Dean Martin•Lay Some Happiness On Me / Think About Me•Reprise Records•1966','\
Woody Shaw•Blackstone Legacy•Contemporary Records•1971','\
Joan Armatrading•Starlight•Hypertension•2012','\
Giovanni Hidalgo•Worldwide•Sony Discos Inc.•1993','\
Tommy Tedesco•When Do We Start•Discovery Records•1978','\
Ralph Burns And His Orchestra•Illya Darling•United Artists Records•1967','\
Various•Swingin\' Stereo!•Capitol Records•1959','\
Pousette-Dart Band•Amnesia•Capitol Records•1978','\
Woody Herman•Giant Steps•Fantasy•1973','\
Blossom Dearie•Sweet Blossom Dearie•Fontana•1967','\
Frank Nimsgern•Frank Nimsgern Featuring Chaka Khan & Billy Cobham•Lipstick Records (3)•1991','\
Jazzie Redd•The Colors Of Jazz EP•Pump Records•1991','\
Leslie Letven•Make It Right•Sin-Drome Records Ltd.•1991','\
Curtis Stigers•I Think It\'s Going To Rain Today•Concord Jazz•2005'),'\
\
This Heart Of Mine\
':('\
Jimmy Witherspoon•Love Me Right / Make This Heart Of Mine Smile Again•Prestige•1965','\
Blue Barron And His Orchestra•Blue Baron And His Orchestra Play•Royale•1954','\
Sonny Rollins Quartet•Sonny Rollins Quartet•Prestige•1952','\
Fred Hersch•Sarabande•SunnySide•1987','\
Maxine Sullivan•Maxine Sullivan Featuring Phil Moore With The Blue Notes•Sutton•0','\
Jane Fielding•Introducing Jane Fielding•Jazz: West•1955','\
Boyd Raeburn And His Orchestra•Experiments In Big Band Jazz - 1945•Musicraft•1980','\
Jackie Ryan•This Heart of Mine•OpenArt Records•2003','\
Pamela Luss•There\'s Something About You Don\'t Know•Savant•2006','\
Francis Scott And His Orchestra•Moods For Firelight•Capitol Records•0','\
Larry Elgart & His Orchestra•Sophisticated Sixties•MGM Records•1960','\
Buddy Clark (3)•The Early Years 1935-1937•Take Two Records•1980','\
André Previn•Love Walked In•RCA Camden•0','\
Sonny Rollins•Shadrack•Soldore•2003'),'\
\
This I Dig of You\
':('\
Hank Mobley•Soul Station•Blue Note•1960','\
The Rafael Jerjen Concept•Soul Station Return•Laika Records•2015','\
Various•Blue Notables Vol. 3 : Blue Note\'s Blue Bloods - Modern Jazz Aristocrats•Blue Note•1996','\
Vincent Herring•Folklore - Live At The Village Vanguard•Limelight•1992','\
Grand Central (10)•Tenor Conclave - Featuring Ravi Coltrane & Craig Handy•Alfa Jazz•1995','\
Ralph Moore (2)•Images•Landmark Records (3)•1988','\
Greg Abate Quintet•bop lives!•Blue Chip Jazz•1996','\
Στράτος Βουγάς Quartet•A Tribute To Hank Mobley•Legend Recordings•1999','\
Rickey Woodard•California Cooking!•Candid•1991'),'\
\
This Is Always\
':('\
Harry James And His Orchestra•This Is Always / And Then It\'s Heaven•Columbia•1946','\
Charlie Parker•Charlie Parker On Dial Volume 2•Spotlite Records•1972','\
Earl Coleman•This Is Always / I\'ve Had My Last Affair•Prestige•1955','\
The Chet Baker Quintet•Cool Blues [Vol. Two]•Replica Records (5)•0','\
Harry James And His Orchestra•This Is Always / I\'ve Never Forgotten•Columbia•1946','\
Chet Baker Trio•This Is Always•SteepleChase•1982','\
Chet Baker•Live In Europe 1956•Musidisc•1982','\
Harry James And His Orchestra•This Is Always / I\'ve Never Forgotten•Columbia•1946','\
Chet Baker Quartet•Live At Nick\'s•Criss Cross Jazz•1987','\
Dave McKenna•My Friend The Piano•Concord Jazz•1987','\
Don Byas And His Orchestra•3•Barclay•0','\
Willis Jackson•The Gator Horn•Muse Records•1979','\
Chet Baker•Chet Baker - Steve Houben•Not On Label•1980','\
Chet Baker•Sings And Plays With Bud Shank Russ Freeman And Strings•Pacific Jazz•1955','\
Chet Baker•Two A Day•All Life•1979','\
The Anita Kerr Quartet•For You For Me Forevermore•Decca•1960','\
Lee Konitz•Lullaby Of Birdland•Candid•1994','\
Christopher Hollyday•Christopher Hollyday•Novus•1989'),'\
\
This Is New\
':('\
Jack Wilkins•You Can\'t Live Without It•Chiaroscuro Records•1977','\
Chick Corea•Tones For Joan\'s Bones•Vortex Records (2)•1968','\
Chick Corea•Tones For Joan\'s Bones•Vortex Records (2)•1968','\
The Walter Norris Quartet•Sunburst•Concord Jazz•1991','\
Jimmy Raney Quartet•Raney\'81•Criss Cross Jazz•1981','\
Bob Thompson (11)•Say What You Want•Intima Records•1988','\
Bob Manning (2)•This Is All Very New To Me / What A Wonderful Way To Die•Capitol Records•1955','\
no artist•Never Pat a Burning Dog•no label•1991','\
Eddie Daniels•This Is New•Takt Jazz Series•1968','\
Freddie Redd Trio•San Francisco Suite•Riverside Records•1958','\
Tom Rainey Obbligato•Float Upstream•Intakt Records•2017','\
Al Cohn•Nonpareil•Concord Jazz•1981','\
Art Resnick Trio•A Gift•Capri Records (6)•1989','\
Chick Corea•Chick Corea Herbie Hancock Keith Jarrett McCoy Tyner•Atlantic•1976'),'\
\
This Masquerade\
':('\
George Benson•This Masquerade•Warner Bros. Records•1976','\
George Benson•This Masquerade / Breezin\'•Warner Bros. Records•1976','\
George Benson•This Masquerade•Warner Bros. Records•1976','\
George Benson•This Masquerade•Warner Bros. Records•1976','\
Avrey Sharron•Oasis•Krypton•1977','\
Bob Berg•New Birth•Xanadu Records•1978','\
Xanadu•Xanadu At Montreux Volume Three•Xanadu Records•1979'),'\
\
Those Eyes\
':('\
Donna Hightower•Brush Those Tears From Your Eyes•Valentine Records (4)•0','\
Golden Gate Orchestra•Where\'d You Get Those Eyes? / Longing•Perfect (3)•1926','\
Fred Waring & The Pennsylvanians•Collegiate / Look At Those Eyes•Victor•1925','\
Donna Hightower•Get T\'stepping •Marfer•1973','\
Evelyn Knight And The Stardusters•A Little Bird Told Me / Brush Those Tears From Your Eyes•Decca•1949','\
Evelyn Knight And The Stardusters•A Little Bird Told Me / Brush Those Tears From Your Eyes•Decca•1949','\
no artist•Hi-Diddle-Diddle / Where\'d You Get Those Eyes•Victor•1926','\
June Christy•Look Out Up There / I Never Wanna Look Into Those Eyes Again•Capitol Records•1958','\
Shep Fields And His New Music•Better Not Roll Those Blue Blue Eyes / When The Lights Go On Again (All Over The World)•Bluebird (3)•1942','\
George Wallington Trio•Jazz Time Paris Vol. 9•Vogue Productions•0','\
Michael Deep•Thru The Harp•Higher Octave Music•1989','\
Cannonball Adderley•The Best Of Cannonball Adderley•Riverside Records•1968','\
Benny Carter•New Jazz Sounds•Norgran Records•1955','\
Kat Edmonson•Take To The Sky•Convivium•2009','\
Dexter Gordon•The Ballad Album•Prestige•1981'),'\
\
Thou Swell\
':('\
Art Tatum Trio•Footnotes To Jazz Vol. 2: Rehearsal•Folkways Records•1952','\
Hampton Hawes•I Just Love Jazz Piano!•Savoy Records•1955','\
Art Tatum Trio•The Complete Trio Sessions With Tiny Grimes & Slam Stewart Vol. 2•Official (3)•1988','\
Sonny Stitt•Jazz At The Hi-Hat•Roost•1954','\
Kai Winding•K + J.J.•Bethlehem Records•0','\
Stan Getz Quintet•Jazz At Storyville•Royal Roost•1952','\
Paul Smith (5)•Liquid Sounds By Paul Smith•Capitol Records•1954','\
Maynard Ferguson•Dimensions Vol. 1 Feat. Maynard Ferguson•EmArcy•0','\
The Horace Silver Trio•Horace Silver Trio•Vogue•0','\
Lester Young And His Orchestra•A Foggy Day•Columbia•1955','\
The Horace Silver Trio•New Faces - New Sounds•Blue Note•1952','\
The Pete Jolly Trio•When Lights Are Low•RCA Victor•1957'),'\
\
Three Base Hit\
':('\
Pat Martino•Exit•Muse Records•1977','\
Teddy Edwards•Mississippi Lad•Verve Records•1991','\
Teddy Edwards•Central Avenue Breakdown Volume 2•Onyx Records (3)•1974'),'\
\
Three Flowers\
':('\
McCoy Tyner Big Band•Uptown/Downtown•Milestone (4)•1989','\
McCoy Tyner•Today And Tomorrow•Impulse!•1964','\
Richard Davis (2)•Harvest•Muse Records•1979','\
Frank Morgan•Easy Living•Contemporary Records•1985','\
McCoy Tyner•The Impulse Story•Impulse!•2006','\
London Experimental Ensemble•Child Ballads•Split Rock Records•2019','\
Gilles Peterson•Pure Fire! A Gilles Peterson Impulse! Collection•Impulse!•2006','\
Derek Bailey•Drops•Ictus Records•1977','\
William Salter•It Is So Beautiful To Be•Marlin•1977','\
McCoy Tyner•Soliloquy•Blue Note•1992','\
Freddie Gambrell•Mikado•World Pacific Records•1959'),'\
\
Three Hearts Dancing\
':('\
Barbara Dennerlein•That\'s Me•Enja Records•1992','\
The Three Suns•The Happy-Go-Lucky Sound•RCA Camden•1958','\
The Three Suns•Dancing On A Cloud•RCA Victor•1961','\
The Romantic Strings•The Romantic Strings Play Your 101 Favorite Melodies•no label•1977','\
Various•Mood Music For Every Moment•no label•1981'),'\
\
Three Little Words\
':('\
Kansas City Six•Prez And Friends (A Complete Session)•Commodore•1980','\
Lester Young And His Orchestra•Three Little Words / Neenah•Mercury•0','\
The Flip Phillips-Buddy Rich Trio•Carioca/Three Little Words•Mercury•0','\
Quintette Du Hot Club De France•Three Little Words / Appel Indirect•Decca•1938','\
Cal Tjader Trio•Lullaby Of Leaves / Three Little Words•Galaxy•0','\
Milt Jackson•Bags & Trane•Atlantic•0','\
Duke Ellington And His Orchestra•Three Little Words / Ring Dem Bells•Victor•1930','\
Tommy Dorsey And His Orchestra•Nobody\'s Baby / Three Little Words / Jungle Drums•V Disc•1945','\
Nat King Cole•Three Little Words / I\'ll Never Be The Same•Capitol Records•1949','\
Les Paul & Mary Ford•Moon Of Manakoora / Three Little Words•Capitol Records•1951','\
Ziggy Elman & His Orchestra•And The Angels Sing / Three Little Words•MGM Records•1948','\
Ron Carter Quartet•Piccolo•Milestone (4)•1977','\
The Benny Carter Group•Wonderland•Pablo Records•1986','\
Sarah Vaughan•After Hours At The London House•Mercury•1958'),'\
\
Three Marias\
':('\
Wayne Shorter•Emanon•Blue Note•2018','\
Wayne Shorter•This Is Jazz Vol. 19•Columbia•1996','\
Rachel Z Trio•On The Milky Way Express•Tone Center•2000','\
Wayne Shorter•Atlantis•Columbia•1985','\
Andy Summers•The X-Tracks•CNR Records International•2004','\
Philip Aaberg•High Plains•Windham Hill Records•1985','\
Wayne Shorter•Footprints The Life And Music Of Wayne Shorter•Columbia•2004','\
Various•Bistro - Erotica Italia•Arista•1997'),'\
\
Thriving On a Riff\
':('\
The Be Bop Boys•Thriving On A Riff / Wee Dot•Savoy Records•1946','\
Charlie Parker•New Sounds In Modern Music Volume 2•Savoy Records•1951','\
Charlie Parker•The Original Bird The Best Of Charlie Parker 1944-1949•Savoy Jazz•1988','\
Akira Miyazawa•On Green Dolphin Street•Union Jazz•1982','\
Charlie Parker•Bird / The Savoy Recordings (Master Takes) Vol. 1•Savoy Jazz•0','\
Charlie Parker•A Night In Tunisia•Sunflower Records (5)•2002','\
Charlie Parker•Charlie Parker On Savoy Vol.1•Arista•1977','\
Charlie Parker•Original Bird: The Best Of Bird On Savoy•Savoy Jazz•1988','\
Charlie Parker•Encores•Savoy Records•1977','\
Miles Davis•Miles Davis•Weton-Wesgram•2005','\
Charlie Parker•Bird / The Savoy Recordings (Master Takes)•Savoy Records•1976'),'\
\
Through The Fire\
':('\
Heikki Sarmanto•Suomi - A Symphonic Poem For Orchestra•Finlandia Records•1984','\
Eliane Elias•Illusions•Denon•1987','\
Kirk Whalum•And You Know That!•Columbia•1988','\
Jeff Linsky•Passport To The Heart•Concord Vista•1997','\
Eric Marienthal•One Touch•GRP•1993','\
Eric Marienthal•Collection•GRP•1997','\
Riccardo Del Fra•Moving People•Parco Della Musica Records•2019','\
Kirk Whalum•The Best Of Kirk Whalum•Columbia•2002','\
no artist•no title•no label•no year','\
no artist•no title•no label•no year','\
Various•Magical Duos•GRP•1993','\
Eliane Elias•The Best of Eliane Elias on Denon•Denon•1995','\
Sven Libaek•Inner Space (The Lost Film Music Of Sven Libaek)•Trunk Records•2006','\
David Foster•The Best Of Me: A Collection Of David Foster\'s Greatest Works•Warner Strategic Marketing•2002','\
James Holden•The Animal Spirits•Border Community•2017','\
Werkha•Colours  Of A Red Brick Raft•Tru Thoughts•2015','\
Happy Sax•Soft Sounds•Sunnyvale Records•1977','\
Oscar Lopez•Flashback: The Best Of Oscar Lopez•Narada World•2002'),'\
\
Thumper\
':('\
Barone - Burghardt Orchestra•Organic•Ex Libris•1977','\
Eric Gale•Multiplication•Columbia•1977','\
The Paul Winter Sextet•Jazz Premiere: Washington•Columbia•1963','\
Jimmy Heath Sextet•The Thumper•Riverside Records•1960','\
Hieroglyphic Being•We Are Not The First•Rvng Intl.•2015','\
Dickie Harrell•Drums And More Drums•Capitol Records•1961','\
Eric Gale•Ginseng Woman / Multiplication•Columbia•1991','\
Various•Diggin\' Deeper 6 - The Roots Of Acid Jazz•Sony Music Catalog•2001','\
Jimmy Heath•Fast Company•Milestone (4)•1975','\
John Barry•Diamonds Are Forever (Original Motion Picture Soundtrack)•United Artists Records•1971'),'\
\
Tickle-Toe\
':('\
Art Pepper Quartet•Suzy The Poodle / Tickle Toe•Discovery Records•1952','\
The Zoot Sims Quintet•All The Things You Are / Tickle Toe•Gazell•0','\
Count Basie Orchestra•The Count And Prez•Philips•0','\
The Eddie Davis-Johnny Griffin Quintet•Tough Tenors Again N Again•MPS Records•1970','\
The Eddie Davis-Johnny Griffin Quintet•Tough Tenors•Jazzland•1960','\
The Quincy Jones Big Band•Q Live In Paris Circa 1960•Qwest Records•1996','\
Lew Tabackin•Vintage Tenor•RCA•1978','\
Scott Hamilton•Live!•Gac Records (2)•2016','\
Cy Touff•Tickle Toe•Delmark Records•2008','\
Les Double Six•Swingin\' Singin\'!•Philips•1962','\
Buddy Tate•Kansas City Joys•Sonet•1976','\
Art Pepper Quartet•Art Pepper Quartet•Discovery Records•1952','\
Art Pepper•Discoveries•Savoy Records•1977','\
Charly Antolini•Cookin\'•L+R Records•1990'),'\
\
Til There was You\
':('\
Pete Petersen & The Collection Jazz Orchestra•Straight Ahead•Chase Music Group•1989','\
Eddie Fisher•Starring Eddie Fisher Also Starring Eddie Maynard And His Orchestra•Premier (7)•0','\
Lance Hayward•Killing Me Softly•Island Records•1987','\
Jacques Darieux And His Orchestra•The Music Man And Gilbert And Sullivan\'s The Mikado•Palace (2)•1961','\
101 Strings•Broadway Cocktail Party•Somerset•1960','\
Herb Alpert•I Feel You•Concord Jazz•2011','\
Mel Lewis Sextet•The Lost Art•Musicmasters•1989','\
Steve Race•Late Race•World Record Club•1965','\
Tyree Glenn•Tyree Glenn At The London House In Chicago•Roulette•1961','\
Cassandra Wilson•Loverly•Blue Note•2008','\
Nils Landgren•The Moon The Stars And You•ACT (4)•2011','\
Terry Snyder•Footlight Percussion (Hit Selections Of The Great White Way With A Bongo Beat)•United Artists Ultra Audio•1967','\
John Gary•Sings Especially For You•RCA Victor•1967','\
Ethel Smith•On Broadway•Decca•1960','\
Vera Lynn•Among My Souvenirs•no label•1964'),'\
\
Till There Was You\
':('\
Billy Eckstine•Till There Was You•Mercury•1962','\
The Jonah Jones Quartet•Mack The Knife•Capitol Records•0','\
Valjean•Till There Was You / The Eighteenth Variation•Carlton•1962','\
Peggy Lee•Till There Was You•Capitol Records•1961','\
Sonny Rollins•Freedom Suite•Riverside Records•1958','\
Sonny Rollins•The Freedom Suite Plus•Milestone (4)•1973','\
Howard Blake•That Hammond Sound•Studio 2 Stereo•1966','\
Martes 8.30•Villa Sebucan•Lyric (2)•1994','\
Ray Charles•Come Live With Me•Crossover Records (3)•1974','\
Steve Grossman•Time To Smile•Dreyfus Jazz•1994'),'\
\
Time After Time\
':('\
Miles Davis•Time After Time•Columbia•1984','\
Lou Donaldson•Signifyin\'•Argo (6)•1963','\
Frank Sinatra•Time After Time / French Foreign Legion•Capitol Records•0','\
Von Freeman•Serenade & Blues•Nessa Records•1979','\
The Three Sounds•Goin\' Home•Blue Note•1958','\
The Sun Ra Arkestra•The Invisible Shield•Saturn Research•1974','\
Vito Price & Company•Time After Time•Argo (6)•1958','\
The American Patrol•Time After Time•Warner Bros. Records•0','\
Tuck & Patti•Time After Time•Windham Hill Records•1988','\
Billie Poole•Rocks In My Bed / Time After Time•Riverside Records•1962','\
The Curtis Counce Group•The Curtis Counce Group•Contemporary Records•1957','\
Ruth Brown•Secret Love•Noslen•1963','\
Billie Poole•Rocks In My Bed / Time After Time•Riverside Records•1962','\
Joe Morello•It\'s About Time•RCA•1962','\
Frank Sinatra•I Believe / Time After Time•Columbia•1947','\
Isao Suzuki Quartet•All Right!•Three Blind Mice•1974','\
Ben Webster•Ben Webster And Associates•Verve Records•1959','\
Jimmy Ponder•Mean Streets - No Bridges•Muse Records•1987','\
Milt Jackson Quintet•\'Live\' At The Village Gate•Riverside Records•1967'),'\
\
Time Marches On\
':('\
Louis Jordan And His Tympany Five•Time Marches On / Run Joe•Decca•1957','\
John Scofield•Blue Matter•Gramavision•1987','\
Freddie Redd•Everybody Loves A Winner•Milestone (4)•1991','\
Eddie Daniels•First Prize!•Prestige•1967','\
Wynton Marsalis•Fathers & Sons•Columbia•1982','\
John Scofield•Slo Sco: Best Of The Ballads•Gramavision•1990','\
Jelly Roll Morton•The Complete Library Of Congress Recordings By Alan Lomax•Rounder Records•2005'),'\
\
Time On My Hands\
':('\
Benny Goodman And His Orchestra•Time On My Hands / Scarecrow•Columbia•1941','\
Benny Goodman Trio•Time On My Hands / Sweet Leilani •Philips•0','\
Earl Bostic•Ubangi Stomp / Time On My Hands•King Records (3)•1954','\
Count Basie Orchestra•Time On My Hands / For The Good Of Your Country•Columbia•1943','\
Johnny Hodges•On The Sunny Side Of The Street•Vogue•0','\
Erroll Garner•Erroll Garner-No. 3•Philips•0','\
Stan Getz Quintet•The Stan Getz Quintet•Clef Records•1953','\
Teddy Wilson Trio•Teddy Wilson Trio•Metronome•1953','\
Henri René And His Orchestra•Time On My Hands•RCA Victor•1956','\
Benny Goodman•That\'s Good...man!•Philips•0','\
Lee Konitz•In Harvard Square•Storyville (3)•1955','\
Oscar Pettiford•Basically Duke•Bethlehem Records•1955','\
Joe Morello•It\'s About Time•RCA•1962','\
Glenn Miller•Glenn Miller•Epic•1954'),'\
\
Time Remembered\
':('\
Kenny Werner•Form and Fantasy•Double-Time Records•2001','\
The Bill Evans Trio•Köln Concert 1976•Gambit Records•2005','\
Barney Kessel•Let\'s Cook!•Contemporary Records•1963','\
Keith Jarrett•Europa Jazz•Europa Jazz•1981','\
The Bill Evans Trio•Bill Evans Trio With Symphony Orchestra•Verve Records•1966','\
Bill Evans•How Deep Is The Ocean?•Heart Note Records•1988','\
Oregon•Friends•Vanguard•1977','\
Joey Calderazzo•Joey Calderazzo•Columbia•2000','\
Bill Evans•Unknown Session•Riverside Records•1983','\
Phil Woods•Crazy Horse•Atlas Record (2)•1980','\
Bill Evans•Autumn Leaves•Jazz Masterworks•1985','\
The Bill Evans Trio•Since We Met•Fantasy•1976','\
The Bill Evans Trio•Camp Fortune 1974•Radio Canada International•1976'),'\
\
Time Remembers One Time Once\
':('\
Denny Zeitlin•Time Remembers One Time Once•ECM Records•1983','\
Enya•MP3 Collection•Digital Records (6)•2007'),'\
\
Time Tracks\
':('\
Charles Mills•Tracks In The Sand•Access (3)•1991','\
Jack Fascinato•Music From A Surplus Store•Capitol Records•1959','\
Terry Evans•Puttin\' It Down•AudioQuest Music•1995','\
Mongo Santamaria•Feelin\' Alright•Atlantic•1970','\
Swing Out Sister•Beautiful Mess•Avex Trax•2008','\
The Grateful Dead•Dick\'s Picks Volume Sixteen: Fillmore Auditorium - 11/8/69•Grateful Dead Records•2000','\
Frankie Randall•A Swingin\' Touch!•RCA•1985','\
Glenn Weston•On Stage•Ivanhoe Associates Limited•0','\
Tino•Tino\'s Breaks Volume 3: Christmas•Tino Corp.•1999','\
Various•Your Guide To Fønix Musik•Fønix Musik•1991','\
The Flashbulb•Soundtrack To A Vacant Life•Alphabasic•2008','\
Various•Rykodisc The Anthology•Rykodisc•2004','\
Sarah Vaughan•The Complete Sarah Vaughan On Mercury Vol. 4 (Part 2) - Sassy Swings Again; 1964-1967•Mercury•1987'),'\
\
Tiny Capers\
':('\
The Flippers (2)•Jada / Tiny Capers•RCA•1961','\
Clifford Brown Ensemble•Clifford Brown Ensemble Featuring Zoot Sims•Vogue•1956','\
Stanley Turrentine•Look Out!•Blue Note•1960','\
Clifford Brown Ensemble•Clifford Brown Ensemble Featuring Zoot Sims•Pacific Jazz•1955','\
Clifford Brown•Jazz Immortal•Pacific Jazz•1960','\
The Louie Bellson Quintet•S*A*L*U*T*E•Chiaroscuro Records•1995','\
Jack Montrose•Arranged By Montrose•Pacific Jazz•1956'),'\
\
Tippin\'\
':('\
Erskine Hawkins And His Orchestra•Tippin\' In / After Hours•RCA Victor•0','\
Erskine Hawkins And His Orchestra•Remember / Tippin\' In•RCA Victor•1945','\
Pete Fountain•Hello Dolly / Tippin\' In•Coral•0','\
Shirley Scott•Roll \'Em•Impulse!•1966','\
Roy Eldridge And His Orchestra•Tippin\' Out / Hi Ho Trailus Boot Whip•Decca•1946','\
Ralph Flanagan And His Orchestra•Tippin\' In / I Should Care•RCA Victor•0','\
Georgie Auld•Tippin\' In / Love Is Just Around The Corner•Mercury•1956','\
Georgie Auld•Tippin\' In / Love Is Just Around The Corner•Mercury•1956','\
The Jazz Couriers•Tippin\' - The Jazz Couriers Live In Morecambe 1959•Gearbox Records•2012','\
Freddie Hubbard•Face To Face•Pablo Records•1982','\
Art Blakey Combo•Untitled•Odeon•1957','\
Horace Silver•Live At Newport \'58•Blue Note•2008','\
Erskine Hawkins And His Orchestra•After Hours•RCA•0','\
Erroll Garner•Garnering•EmArcy•1954','\
Brother Jack McDuff•Tough \'Duff•Prestige•1960'),'\
\
Tis Autumn\
':('\
Geraldo And His Orchestra•Soft Shoe Shuffle / \'Tis Autumn•Columbia•0','\
Stan Getz Quintet•Lover Come Back To Me / Tis Autumn•Mercury•1953','\
Nicki Parrott•Autumn Leaves•Venus Records (5)•2012','\
David Rose & His Orchestra•Autumn Leaves•MGM Records•1957','\
Zoot Sims•In A Sentimental Mood•Sonet•1985','\
Nicki Parrott•Autumn Leaves•Venus Records (5)•2012','\
Red Garland•All Kinds Of Weather•Prestige•1958','\
Stan Getz Quintet•The Stan Getz Quintet•Clef Records•1953','\
The Boys From Rochester•The Boys From Rochester•Feels So Good Records•1989','\
The Malcolm Lockyer Orchestra•The Seasons Of Love•Mercury•1957','\
Anthony Ortega•New Dance!•hat ART•1990','\
The Nat King Cole Trio•Volume 4•Capitol Records•1950','\
Bunny Berigan•Bunny Berigan\'s Last Recordings•Sparton•1954'),'\
\
Togetherness\
':('\
Don Cherry•Togetherness•Durium•1966','\
Jimmy Heath•New Picture•Landmark Records (3)•1985','\
Trummor & Orgel•Indivisibility•Introspection•2018','\
Ray Charles•Jazz Number II•Tangerine Records•1972','\
Albert Mangelsdorff•Lanaya•Plainisphare•1994','\
Don Cherry•Orient•BYG Records•1973','\
Walt Dickerson•A Sense Of Direction•New Jazz•1961','\
Outernational Meltdown•Healer\'s Brew•B&W Music•1995','\
Joachim Fuchs-Charrier•Drum Symphony•Pläne•1979','\
Horace Silver•Silver \'N Voices•Blue Note•1977','\
Blue Mitchell•Heads Up!•Blue Note•1968','\
Escalators•The Escalators EP•Typhoon Records (4)•1994'),'\
\
Tokyo Blues\
':('\
The Horace Silver Quintet•The Tokyo Blues•Blue Note•1962','\
Horace Silver•The Best Of Horace Silver•Blue Note•1969','\
Either/Orchestra•Dial E•Accurate Records•1986','\
Various•Soho Blue - Welcome To The Blue Note Club•Blue Note•1986','\
John Hicks•Sketches Of Tokyo•DIW•1985','\
Horace Silver•Paris Blues•Pablo Records•2002','\
James Morrison And The Hot Horn Happening•Live In Paris•EastWest•1994','\
Chartbusters!•Volume 1•NYC Records•1995','\
Kankawa•B-III•Victor•1997','\
The Benny Green Trio•Blue Notes•Something Else Records (2)•1993','\
Red Holloway & Company•Red Holloway & Company •Concord Jazz•1987','\
Helmut Zacharias And His Orchestra•Tea Time In Tokyo•Polydor•1964'),'\
\
Tokyo Dream\
':('\
The Glad Singers•Tokyo-Melody•Columbia•1964','\
Rob Mullins•Tokyo Nights•Nova Records (3)•1990','\
Clifford Jordan•Four Play•DIW Records•1990','\
Leon Parker•Awakening•Columbia•1998','\
Eric Alexander•Nightlife In Tokyo•Milestone (4)•2003','\
Allan Holdsworth•Road Games•Warner Bros. Records•1983','\
Anthony Wilson Nonet•Power Of Nine•Groove Note•2006','\
Claire Martin•Believin\' It•Linn Records•2019','\
Horace Silver•Essential Blue -The Classic Of Horace Silver•-Blue Note•2007','\
Karizma (3)•Lost And Found•Creatchy•2001','\
Dee Dee Bridgewater•Love And Peace - A Tribute To Horace Silver•Verve Records•1995','\
Keith Jarrett•Barber / Bartók / Jarrett•ECM Records•2015','\
King Crimson•The Collectable King Crimson Volume Five (Live In Japan 1995 - The Official Edition)•WHD Entertainment Inc.•2010'),'\
\
Tomorrow\'s Destiny\
':('\
Sun Ra•Monorails & Satellites (Works For Solo Piano Vols. 1 2 3)•Cosmic Myth Records•2019'),'\
\
Too High\
':('\
Norman Brown•Too High•MoJazz•1992','\
Paul Horn•Too High •Epic•1974','\
Earl Hines•Just Too Soon / Chicago High Life•H. R. S.•1946','\
Joe Farrell•Penny Arcade•CTI Records•1974','\
Freddie Hubbard•High Energy•Columbia•1974','\
Paul Horn•Visions•Epic•1974','\
The Dave Brubeck Trio•The Dave Brubeck Trio•Fantasy•1953','\
Pharoah Sanders•Shukuru•Theresa Records•1985','\
Dr. Music•Doctor Music•Radio Canada International•1977','\
Edmundo Ros & His Orchestra•Ros Album Of Latin Melodies•Decca•1956','\
The Medieval Jazz Quartet•Medieval Jazz Quartet Plus Three•Classic Editions•1961','\
Freddie Hubbard•Gleam•CBS/Sony•1975'),'\
\
Too Marvelous For Words\
':('\
Stan Getz Quartet•Too Marvelous For Words / Michelle•Prestige•0','\
Lester Young Quartet•Too Marvelous For Words / Encore•Mercury•1950','\
Stan Getz•What\'s New / Too Marvelous For Words•Prestige•0','\
Joe Loco And His Quintet•You\'re Too Marvelous For Words  / Flamingo•Tico Records•1954','\
Harry James And His Orchestra•Too Marvelous For Words / My Future Just Passed•Columbia•1947','\
Billy Daniels•I Get A Kick Out Of You / Too Marvelous For Words•Mercury•0','\
Glenn Miller•Bye Bye Blues / Wang Wang Blues / Too Marvelous For Words•V Disc•0','\
Lester Young Quartet•Too Marvelous For Words•Clef Records•0','\
Frank Sinatra•Songs For Swingin\' Lovers! (Part 3)•Capitol Records•1956','\
The Dave Brubeck Trio•The Dave Brubeck Trio•Fantasy•1953','\
Lee Konitz•Lee Konitz Plays With The Gerry Mulligan Quartet•Pacific Jazz•1954','\
Paul Desmond•Paul Desmond•Artists House•1978','\
Stan Getz Quartet•Vol.2•Prestige•1953','\
J.J. Johnson•The Eminent Jay Jay Johnson Vol. 2•Blue Note•1955'),'\
\
Too Much Sake\
':('\
The Horace Silver Quintet•The Tokyo Blues•Blue Note•1962','\
Various•Influencia Do Jazz•Latin Jazz•1995','\
Montego Joe•¡Arriba! Con Montego Joe•Prestige•1994','\
The Castilians•Now Is The Hour To Tango•Decca•1960','\
Various•Classic Mellow Mastercuts Volume 3•Mastercuts•1994','\
Various•1913: "Come And See The Big Parade"•Archeophone Records•2006','\
Billy Vaughn And His Orchestra•The Big 100•Dot Records•0'),'\
\
Tough Talk\
':('\
The Crusaders•Tough Talk / The Thing•World Pacific Records•1965','\
The Crusaders•No Name Samba (Bossa Nova) / Tough Talk•World Pacific Records•1963','\
The Crusaders•Tough Talk•Pacific Jazz•1963','\
The Crusaders•Chile Con Soul•Pacific Jazz•1965','\
Freddie McCoy•Funk Drops•Prestige•1966','\
Panama Francis•Tough Talk•20th Century Fox Records•0','\
The Crusaders•The Best Of The Jazz Crusaders•World Pacific Jazz•1970','\
Hawk On Flight•Bermuda Triangle•Public Road Records•1989','\
King Curtis•Live At Small\'s Paradise•ATCO Records•1966','\
The Crusaders•The Young Rabbits•Blue Note•1975'),'\
\
Toy Tune\
':('\
Wayne Shorter•Etcetera•Blue Note•1980','\
The Wooden O•A Handeful Of Pleasant Delites•Middle Earth•1969','\
The Klaus Suonsaari Quintet•Reflecting times•Storyville•1985','\
David Kikoski•Persistent Dreams•Triloka Records•1992','\
Michael Flügel Quartet•Plays The Music Of Wayne Shorter•Jazz4Ever Records•2004','\
The Big Ben Banjo Band•Sing Along With Us•Columbia•1964','\
Bill Evans•Riverside Recordings•Analogue Productions•2010','\
Bill Evans•The Complete Riverside Recordings•Riverside Records•1984','\
Various•Sony Music 100 Years: Soundtrack For A Century•Sony Music•1999'),'\
\
Tracks Of My Tears The\
':('\
Dennis Coffey•Motor City Magic•TSR Records•1986','\
Carmel (2)•The Drum Is Everything•London Records•1984','\
Various•A Twist Of Motown•GRP•2003','\
Mongo Santamaria•Feelin\' Alright•Atlantic•1970','\
Spirit Traveler•Playing The Hits From The Motor City•JVC•1993','\
Various•Blue Note Salutes Motown•Blue Note•1998','\
Various•Alta Classe•WEA•1992','\
Michael Bolton•Ain\'t No Mountain High Enough (A Tribute To Hitsville U.S.A.)•EMI Label Services•2012'),'\
\
Train Samba\
':('\
Sadao Watanabe•Music Break•Takt Jazz Series•1969','\
Sadao Watanabe•Plays•Polydor•1978','\
Orbit (11)•Neil Larsen Featuring Robben Ford•Straight Ahead Records•2007','\
J.J. Johnson•J.J.!•RCA Victor•1965','\
Neil Larsen•Orbit•Straight Ahead Records•2007','\
Antonio Carlos Jobim•Antonio Brasileiro•Columbia•1995','\
Paul Smith (5)•Heavy Jazz - Vol. 2•Outstanding Records (2)•1977','\
Benny Carter•More Cookin\'•Jazz Heritage•1988','\
Per Nyhaug Studioband•Groovin\' High•Gemini Records (7)•1987','\
The Diamond Five•Something Old Something New Something Pink Something Blue•EMI•1975','\
Junko Kimura Trio•But Beautiful •Audio Lab. Record•1987','\
Various•The Very Best Of Latin Jazz•Global Television•1998'),'\
\
Trance\
':('\
Cecil Taylor•Innovations•Freedom•1972','\
Kenny Cox•Introducing Kenny Cox And The Contemporary Jazz Quintet•Blue Note•1968','\
Trio Porteleki-Tärn-Pärnoja•Trio Porteleki-Tärn-Pärnoja •MIB Label Services•2015','\
Booker Ervin•The Trance•Prestige•1967','\
Jah Wobble•Maghrebi Jazz•Jah Wobble Records•2018','\
The Crusaders•The Festival Album•Pacific Jazz•1967','\
Hely (4)•Borderland•Ronin Rhythm Records•2018','\
no artist•no title•no label•no year'),'\
\
Trane\'s Blues\
':('\
Mankunku Quartet•Yakhal\' Inkomo•World Record Co.•1968','\
Sam Jones•Changes & Things•Xanadu Records•1978','\
Hank Jones•Interface•Serious Productions•1989','\
Royce Campbell•Elegy To A Friend•Raised Eyebrow Records•1993','\
The Lonnie Smith = John Abercrombie Trio•Afro Blue•Venus Records (5)•1994','\
Nathan Davis Quartet•Rules Of Freedom•Polydor•1969','\
Naosuke Miyamoto Sextet•Step!•Three Blind Mice•1973'),'\
\
Triste\
':('\
Antonio Carlos Jobim•Wave / Triste•A&M Records•0','\
no artist•Scarborough Fair / Canto Triste•A&M Records•1968','\
Gene Krupa And His Orchestra•Opus No. 1 / Valse Triste•Columbia•1947','\
Lee Konitz & The Brazilian Band•Brazilian Rhapsody•Venus Records (5)•1995','\
Gato Barbieri•El Gato•Flying Dutchman•1975','\
Jorge Autuori Trio•Jorge Autuori Trio - Vol.1 •Rozenblit•1967','\
Jair Rodrigues•Triste Madrugada / Camará... Ê•Philips•1967','\
Art Pepper Quartet•The Maiden Voyage Sessions Vol. 3•Galaxy•1984','\
Various•Hungarian Noir. A Tribute To The Gloomy Sunday•Piranha•2016'),'\
\
Tristeza\
':('\
no artist•Roda / Tristeza •A&M Records•1968','\
Mount/Ant•Sorg•POxVO Crew•2014','\
Astrud Gilberto•Goodbye Sadness (Tristeza) / Nega Do Cabelo Duro•Seven Up Records•2001','\
Roberto Roena•Looking Out For "Numero Uno"•Fania Records•1980','\
Wanda Sá•Wanda Vagamente•RGE•1964','\
The Eddie Higgins Trio•Amor•Venus Records (5)•2006','\
Sebastião Tapajós•Guitarra & Amigos•RCA•1978','\
Birgit Lystager•Christina•RCA Victor•1971','\
Putte Wickman•Putte Wickman & Sivuca•Four Leaf Clover Records•1982'),'\
\
Trouble Is A Man\
':('\
Milt Jackson & Strings•Feelings•Pablo Records•1976','\
Sarah Vaughan•It\'s A Man\'s World•Mercury•1967','\
Marvin Gaye•Trouble Man•Tamla•1972','\
Larry Sonn Orchestra•Jazzband Having A Ball•Dot Records•1958','\
Mary Ann McCall•Melancholy Baby•Coral•1959','\
Coleman Hawkins•At Ease With Coleman Hawkins•Moodsville•1960'),'\
\
Truth\
':('\
Les McCann Ltd.•The Truth•Pacific Jazz•1960','\
Kamasi Washington•Truth•Young Turks•2017','\
Emmanuel Abdul-Rahim•Total Submission•Cobblestone•1972','\
Freddie Hubbard•Super Blue•Columbia•1978','\
Charles Tolliver•New Tolliver•Baystate•1978','\
Charles Tolliver•Live In Tokyo•Strata-East•1974','\
The Pete Jolly Trio•Sweet September•Ava•1964','\
Gerry Mulligan And His Sextet•Mainstream Of Jazz•EmArcy•1957','\
Count Basie Orchestra•Basie Blues / Ain\'t It The Truth•Parlophone•1946','\
Music Inc•Impact•Enja Records•1972','\
Albert Ayler Quintet•Truth Is Marching In•Magic Music•1990','\
Les McCann•The Truth•Pacific Jazz•1969','\
Kamasi Washington•Harmony Of Difference•Young Turks•2017','\
Jackie McLean•It\'s Time!•Blue Note•1965','\
Marc Ribot•Spiritual Unity•Pi Recordings (2)•2005'),'\
\
Tune Up\
':('\
Albert Ayler•Something Different!!!!!!•Bird Notes•1963','\
Jackie McLean Quartet•Tune Up•SteepleChase•1987','\
Miles Davis•The Winners Of Down Beat\'s Readers Poll 1960 "Horns "•Philips•1960','\
Miles Davis•The Fabulous \'Fifties•Bandstand•1993','\
Miles Davis•Laurasia•Seymour Records (2)•2007','\
Miles Davis•Miles Davis Transcribed Solos•JA Records•1980','\
The George Russell Sextet•George Russell Sextet In K.C.•Decca•1961','\
Don Patterson•Tune Up!•Prestige•1971','\
The Miles Davis Quartet•When Lights Are Low•Prestige•1953','\
The Miles Davis Quartet•When Lights Are Low•Prestige•1953','\
Philly Joe Jones Sextet•Blues For Dracula•Riverside Records•1958','\
Max Roach Quintet•Max Roach + 4 At Newport•EmArcy•1958'),'\
\
Tunji\
':('\
Roland Brival•Créole Gypsy•FM Productions•1980','\
John Coltrane•Spiritual•Impulse!•0','\
The John Coltrane Quartet•Coltrane•Impulse!•1962','\
John Coltrane•The Impulse Story•Impulse!•2006'),'\
\
Tunnel Vision\
':('\
Scott Henderson (2)•Nomad•L+R Records•1990','\
Fire Merchants•Fire Merchants•Medusa Records (2)•1989','\
McCormack & Yarde Duo•My Duo•Joy And Ears•2009','\
Brian Bromberg•Brian Bromberg•Nova Records (3)•1993'),'\
\
Turn Around\
':('\
George Benson•Turn Your Love Around•Warner Bros. Records•1981','\
Sonny & Cher•Living For You / Turn Around•Atlantic•1966','\
Michel Petrucciani•100 Hearts•The George Wein Collection•1984','\
Matana Roberts•Live In London•Central Control International•2011','\
Lenny Dee (2)•Folsom Prison Blues•Decca•0','\
Clinton Ford•Turn Around Go Back Home•Pye Records•1970','\
Keely Smith•The Wedding (La Novia)•Reprise Records•1965','\
Jérôme Sabbagh•The Turn•Bee Jazz•2014','\
Burton Greene•Presenting Burton Greene•Columbia•1968','\
Irene Reid•I\'m Too Far Gone To Turn Around•Verve Records•1967','\
Burton Greene•Presenting Burton Greene•Columbia•1968','\
Walter Bishop Jr.•Coral Keys•Black Jazz Records•1971','\
George Benson•Turn Your Love Around / Never Give Up On A Good Thing•Warner Bros. Records•0','\
Phil Broadhurst•Iris•Ode Records•1985','\
David Liebman Group•Turn It Around•Owl Records (4)•1992','\
Tony Di Bart•Falling For You•Cleveland City Blues•1996'),'\
\
Turn Out the Stars\
':('\
The Bill Evans Trio•Quiet Now•Affinity•1986','\
The Bill Evans Trio•Quiet Now•Affinity•1981','\
Gordon Beck•Seven Steps To Evans - A Tribute To The Compositions Of Bill Evans•MPS Records•1980','\
The Bill Evans Trio•Since We Met•Fantasy•1976','\
Bill Evans•In His Own Way•West Wind•1989','\
The Bill Evans Trio•Live At Hilversum 1968•Fondamenta•2016','\
The Bill Evans Trio•Turn Out The Stars•Dreyfus Jazz•1992','\
The Bill Evans Trio•Consecration II•Timeless Records (3)•1990','\
Herbie Mann•Peace Pieces - The Music Of Bill Evans•Kokopelli Records•1995','\
David Hazeltine Trio•Waltz For Debby•Venus Records (5)•1999','\
Don Friedman Trio•Timeless•441 Records•2004','\
Paul Motian•Bill Evans•JMT•1990'),'\
\
Turn Your Love Around\
':('\
George Benson•Turn Your Love Around•Warner Bros. Records•1981','\
George Benson•Turn Your Love Around / Never Give Up On A Good Thing•Warner Bros. Records•0','\
Tony Di Bart•Falling For You•Cleveland City Blues•1996','\
Keiko Lee•The Wonder Of Love•Columbia•2001','\
Various•T.K. Jazz Sampler•T.K. Records•1978','\
George Benson•Best Of George Benson Live•GRP•2005','\
Orchestra Werner Drexler•My Favourite Instruments•Happy Records (6)•1975','\
George Benson•The Best Of George Benson•Warner Bros. Records•1995','\
George Benson• I Grandi Successi •Fonit Cetra•1991','\
George Benson•Classic Love Songs•Rhino Records (2)•2010','\
George Benson•The George Benson Collection•Warner Bros. Records•1981','\
George Benson•Live At Montreux 1986•Eagle Vision•2005'),'\
\
Twilight World\
':('\
Tony Bennett•Twilight World / Easy Come Easy Go•Columbia•1972','\
Tommy Dorsey And His Clambake Seven•Chinatown My Chinatown•RCA Victor•0','\
The Sun Ra Arkestra•My Brother The Wind Vol II•El Saturn Records•1971','\
Don Johnson (4)•King Of Organ With A Beat! Volume 1•Kandy Records•0','\
The Three Suns•Twilight Time•Rondo-Lette•1958','\
Marian McPartland•Interplay•Halcyon Records•1989','\
Average White Band•Show Your Hand•MCA Records•1973','\
Tony Bennett•With Love•Columbia•1972','\
Jun Fukamachi•エイリアン魔獣鏡•Columbia•1985','\
Marian McPartland•Silent Pool•Concord Jazz•1997','\
Mel Powell•Dixieland Classics•Jazztone (2)•0','\
Bert Kaempfert•Die Großen Orchester Der Welt•Polydor•0','\
Orchester Addy Flor•Twilight Mood•MPS Records•1967'),'\
\
Twisted\
':('\
Wardell Gray Quartet•Twisted / Easy Living•Gazell•1952','\
Annie Ross•Annie Ross Sings•Prestige•1953','\
Dan Siegel•The Hot Shot / The Twisted•Inner City Records•1980','\
Wes Montgomery•Live In Paris 1965•no label•1988','\
Lambert Hendricks & Ross•The Hottest New Group In Jazz•Columbia•1959','\
Richard Henshall•The Cocoon•Not On Label (Richard Henshall Self-released)•2019','\
Lambert Hendricks & Ross•The Best Of Lambert Hendricks & Ross•Columbia•1974','\
Ilmiliekki Quartet•Land Of Real Men•We Jazz•2019','\
Wes Montgomery•Twisted Blues•Ediciones Del Prado•1996'),'\
\
Two For The Road\
':('\
Henry Mancini•Two For The Road•RCA Victor•1967','\
Evan Parker / Barry Guy / Paul Lytton•Atlăn′tă•Impetus Records•1990','\
Dudley Moore Trio•Today•Atlantic•1972','\
Henry Mancini•Tema Dal Film "Nicola E Alessandra" / Two For The Road•RCA Victor•1972','\
Brazilia 70•South Of The Border•Deacon Records•1970','\
Arnett Cobb•Party Time•Prestige•1959','\
Lex Jasper Trio•Lexpression•Limetree Records•1986','\
Rick Kiefer•Lush Life•Omega International•1975','\
Dudley Moore•At The Wavendon Festival•Black Lion Records•1976','\
Steve Kuhn Trio•Easy To Love•Venus Records (5)•2004','\
Shoji Suzuki And His Rhythm Aces•Live In Nemu Vol.1•JVC•1972','\
Steve Kuhn•Mostly Ballads•New World Records•1987','\
Living Strings•Living Strings Play Music From Gone With The Wind And Other Motion Pictures•RCA Camden•1967','\
Gene Bertoncini•Acoustic Romance•Sons Of Sound Recorded Music•2003','\
Patricia Barber•Split•Floyd Records•1989'),'\
\
Two Not One\
':('\
Lee Konitz•Vol. 2•Music•0','\
Anat Fort•A Long Story•ECM Records•2007','\
Lee Konitz•Spirits•Milestone (4)•1972','\
Warne Marsh Quintet•Live At The Montmartre Club - Jazz Exchange Vol. 2•Storyville•1977','\
Jimmy Hamilton•It\'s About Time•Prestige Swingville•1961','\
Lee Konitz•Lee Konitz Meets Warne Marsh Again•Epic•1978','\
Ayumi Koketsu•Rainbow Tales•M & I•2012','\
Lee Konitz•Lee Konitz With Warne Marsh•Atlantic•1955','\
Warne Marsh Quartet•Back Home•Criss Cross Jazz•1986','\
Junior Cook•Pressure Cooker•Catalyst Records (3)•1977','\
George Duke•Face The Music•BPM Records (14)•2003','\
Count Basie•Kansas City Style•Giants Of Jazz Records•1977','\
Ken Peplowski•Ken Peplowski & Howard Alden•Concord Jazz•1993','\
Frank Gambale•Thunder From Down Under•JVC•1990'),'\
\
Underdog The\
':('\
James Moody•Too Heavy For Words•MPS Records•1973','\
Turk Mauro•The Underdog•Jazzcraft Records•1978','\
Kim Parker•"Havin\' Myself A Time"•Soul Note•1982','\
Buddy Childers Big Band•Just Buddy\'s•Trend (3)•1985','\
Dave Frishberg•You\'re A Lucky Guy•Concord Jazz•1978','\
Dave McKenna•Giant Strides•Concord Jazz•0','\
Irene Kral•Gentle Rain•Choice (7)•1978','\
Branford Marsalis Quartet•Music From Mo\' Better Blues•Columbia•1990','\
Nellie McKay•Home Sweet Mobile Home•Verve Forecast•2010','\
Dave Frishberg•Let\'s Eat Home•Concord Jazz•1990','\
Donna Byrne•Licensed To Thrill•A-Records•2004'),'\
\
Unforgettable\
':('\
Nat King Cole•Unforgettable•Capitol Records•0','\
Nat King Cole•Smile•Capitol Records•0','\
Nat King Cole•Unforgettable / Mona Lisa•Capitol Records•0','\
Natalie Cole•Unforgettable•Elektra•1991','\
Billy May And His Orchestra•Unforgettable / Silver And Gold•Capitol Records•1952','\
Natalie Cole•Unforgettable•Elektra•1991','\
Ray Martin And His Concert Orchestra•Blue Tango / Unforgettable•Columbia•1952','\
Dinah Washington•Unforgettable / Love Walked In•Mercury•0','\
Nat King Cole•Unforgettable•Capitol Records•1960','\
The Dick Hyman Trio•Unforgettable / Out Of Nowhere•MGM Records•1954','\
Prism (9)•Live Alive Vol. 2 (In \'85)•SMS Records•1987','\
Jackie Gleason•Music Martinis And Memories (Part 2)•Capitol Records•1954','\
Dinah Washington•Unforgettable / What A Diff\'rence A Day Makes •Mercury•1973','\
Pepper Adams•Pepper Adams 5•Interlude (2)•1959'),'\
\
Unit Seven\
':('\
Sam Jones 12 Piece Band•Something New•Interplay Records•1979','\
The Cannonball Adderley Quintet•Live In Paris April 23rd 1966•Ulysse Musique•1986','\
Cannonball Adderley Sextet•Lugano 1963•TCB Records (2)•1995','\
ETC (10)•ETC•Red Record•1990','\
The Frank Vignola Trio•Let It Happen•Concord Jazz•1994','\
Eddie Green (3)•This One\'s For You•M & I•1995','\
Dusko Goykovich•5ive Horns & Rhythm•Enja Records•2010','\
Hilton Ruiz•Island Eyes•BMG Ricordi S.p.A.•1997','\
Billy Larkin And The Delegates•Don\'t Stop!•World Pacific Records•1967','\
Jimmy Bruno•Like That•Concord Records•1996','\
Cannonball Adderley• Radio Nights•Night Records•1991','\
Nat Adderley•Nat Adderley Live At The 1994 Floating Jazz Festival•Chiaroscuro Records•1996','\
Blood Sweat And Tears•In Concert•CBS•1979','\
Various•Soho Scene \'62 - Jazz Goes Mod•Rhythm & Blues Records•2016'),'\
\
Unless It\'s You (Orbit)\
':('\
Bill Evans•The Complete Bill Evans On Verve•Verve Records•1997'),'\
\
Unquity Road\
':('\
Pat Metheny•Works II•ECM Records•1988','\
Pat Metheny•Bright Size Life•ECM Records•1976'),'\
\
Until It\'s Time For You To Go\
':('\
Houston Person•The Real Thing•Eastbound Records•1973','\
New Birth•Birth Day•RCA Victor•1972','\
Peggy Lee•2 Shows Nightly•Capitol Records•1968','\
Roberta Flack•Chapter Two•Atlantic•1970','\
New Birth•Golden Classics•Collectables•1988','\
Vikki Carr•From The Heart•Pair Records•1992','\
Karen Wyman•Karen Wyman•Decca•1970','\
Ray Bryant•Somewhere In France•Label M•2000','\
Jane Morgan•A Jane Morgan Happening•ABC Records•1968','\
Vikki Carr•The Best Of The Liberty Years•Liberty•1989','\
Jim Nabors•The World Of Jim Nabors•Columbia•1973'),'\
\
Until The Real Thing Comes Along\
':('\
The Oscar Peterson Trio•Until The Real Thing Comes Along/Love For Sale•Mercury•0','\
Frank Sinatra•L.A. Is My Lady•Qwest Records•1984','\
Ella Fitzgerald•Songs In A Mellow Mood•Decca•0','\
Fats Waller•"Fats" Waller•RCA Victor•1957','\
Erroll Garner•Garner In Hollywood•Président•0','\
Nat King Cole•Tell Me All About Yourself•Capitol Records•1960','\
Coleman Hawkins•Soul•Prestige•1958','\
Sonny Criss•Saturday Morning•Xanadu Records•1975','\
Dexter Gordon•A Swingin\' Affair•Blue Note•1962'),'\
\
Up Jumped Spring\
':('\
Freddie Hubbard And His Orchestra•Born To Be Blue•Pablo Records•1982','\
Freddie Hubbard•Feel The Wind•Timeless Records (3)•1989','\
The Essence All Stars•Hub Art - A Celebration Of The Music Of Freddie Hubbard•Hip Bop Essence•1995','\
George Coleman•George Coleman At Yoshi\'s•Theresa Records•1989','\
Freddie Hubbard•Rollin\'•MPS Records•1982','\
Art Blakey & The Jazz Messengers•3 Blind Mice•United Artists Jazz•1962','\
Freddie Hubbard•The Artist Selects•Blue Note•2005','\
Freddie Hubbard•On The Real Side•Four Quarters Entertainment Inc.•2008','\
McCoy Tyner•Double Exposure•LRC Ltd.•1991','\
Trio Transition•Trio Transition•DIW•1988','\
Freddie Hubbard•Backlash•Atlantic•1967'),'\
\
Up With the Lark\
':('\
Bill Evans•Bill Evans•Fabbri Editori•1980','\
Bill Evans•From The 70\'s•Fantasy•1983','\
The Bill Evans Trio•Consecration II - Last•Alfa Jazz•1989','\
Bill Evans•Bill Evans Live In Tokyo•CBS/Sony•1973','\
The Bill Evans Trio•On A Monday Evening•Fantasy•2017','\
Lex Jasper Trio•Lexpression•Limetree Records•1986','\
The Bill Evans Trio•Live At Lulu White\'s•DOL•2016','\
The Bill Evans Trio•Live In Europe Vol. II•EPM Musique•1989','\
The Bill Evans Trio•Live In Europe Vol. II•EPM Musique•1989','\
The Bill Evans Trio•Switzerland 1975•Jazz Helvet•1990','\
The Bill Evans Trio•In Buenos Aires - Vol. 1•Jazz Lab Records•1991','\
Bill Evans•Yesterday I Heard The Rain•Bandstand•1992','\
Bill Evans•The Paris Concert (Edition One)•Elektra Musician•1983'),'\
\
Upper Manhattan Medical Group\
':('\
Art Farmer•Something To Live For (The Music Of Billy Strayhorn)•Contemporary Records•1987','\
The Mitchell-Ruff Duo•Strayhorn: A Mitchell-Ruff Interpretation•Mainstream Records•1971','\
Art Farmer Quartet•Warm Valley•Concord Jazz•1983','\
Bob Wilber•New Clarinet In Town•Classic Editions•1960','\
Clare Fischer Big Band•Thesaurus•Atlantic•1969','\
Tommy Flanagan Trio•The Tommy Flanagan Tokyo Recital•Pablo Records•1975','\
Malte Dürrschnabel Quartet•Strayhorn•Laika Records•2014','\
John Hicks•I Remember You•HighNote Records Inc.•2009','\
Ben Aronov•Shadow Box•Choice (7)•1979'),'\
\
Used To Be A Cha-Cha\
':('\
Michel Camilo•In Trio•Electric Bird•1986','\
Jaco Pastorius•Jaco Pastorius•Epic•1976','\
Various•Jazz Rocks•CBS•1977','\
Jaco Pastorius Big Band•Word Of Mouth Revisited•Heads Up International•2003','\
Snowboy•The Return Of The Hi-Hat (Essential Cuban Brazilian Hard Bop + Fusion)•Ocho•2001','\
Jaco Pastorius•The Essential Jaco Pastorius•Epic•2007','\
Frank Sinatra•The Reprise Collection•Reprise Records•1990'),'\
\
Valdez In The Country\
':('\
Donny Hathaway•You Were Meant For Me / Valdez In The Country•ATCO Records•1978','\
Dan Siegel•Oasis•Baybridge Records•1984','\
George Benson•Gonna Love You More•Warner Bros. Records•1977','\
Peter King (2)•Crusade•Blanco Y Negro•1989','\
Candy Dulfer•Let Me Show You•Victor•2003','\
Terrace Martin•Velvet Portraits•Ropeadope•2016','\
Gerald Veasley•Love Letters•Inak•1999','\
George Benson•Best Of George Benson: The Instrumentals•Warner Bros. Records•1997','\
George Benson•Best Of George Benson: The Instrumentals•Warner Bros. Records•1997'),'\
\
Valse Hot\
':('\
Sonny Rollins•Valse Hot•Esquire•0','\
Ryan Kisor•Kisor •Videoarts Music•2000','\
Clifford Brown and Max Roach•Live At Basin Street April 1956•Ingo•0','\
Jamey Aebersold•Sonny Rollins Nine Classic Jazz Originals•JA Records•1976','\
Sonny Rollins•Live Mid 60\'s•Landscape•1992','\
John Heard & Co.•The Jazz Composer\'s Song Book•Straight Ahead Records•2005','\
Sonny Rollins•Plus 4•Prestige•1956','\
Max Roach•Jazz In 3/4 Time•EmArcy•1957'),'\
\
Vashkar\
':('\
The Tony Williams Lifetime•Emergency! Volume One•Polydor•1969','\
The Tony Williams Lifetime•Emergency! Volume One•Polydor•1969','\
Jaco Pastorius•Pastorius / Metheny / Ditmas / Bley•Improvising Artists Inc.•1976','\
The Tony Williams Lifetime•Lifetime•Polydor•1975','\
Paul Bley•Live•SteepleChase•1986','\
Spectrum Road•Spectrum Road•Palmetto Records•2012','\
The Tony Williams Lifetime•Emergency!•Polydor•1969','\
Gary Burton•Hotel Hello•ECM Records•1975','\
Paul Bley•Syndrome•Savoy Jazz•1986','\
Paul Bley•Floater Syndrome•Vogue•1989','\
Various•Way In To The 70\'s•Polydor•1970'),'\
\
Veils\
':('\
Dinah Shore•Let Me Know•RCA Victor•0','\
John Abercrombie Quartet•M•ECM Records•1981','\
Philly Joe Jones Big Band Sounds•Drums Around The World•Riverside Records•1959','\
Les Baxter His Chorus And Orchestra•Ports Of Pleasure (Part 3)•Capitol Records•1957','\
Rad.•Higher Plane•7 Bridges Recordings•1997','\
John Abercrombie•The First Quartet•ECM Records•2015','\
Unknown Artist•The Music Of Cleopatra On The Nile•Mount Vernon Music•1962','\
Marcel Duchamp Memorial Players•MDMP•Not On Label•1985','\
Richie Beirach Trio•Manhattan Reverie•Venus Records (5)•2006','\
Willie & Lobo•Siete•Narada World•2000','\
Swing (5)•In Full Swing•Cypress Records•1987'),'\
\
Velho Piano\
':('\
Nana Caymmi•Falando De Amor (Famílias Caymmi E Jobim Cantam Antonio Carlos Jobim)•RCA•2005'),'\
\
Very Early\
':('\
Jazz Parasites•Very Early•Phonector•2006','\
The Bill Evans Trio•Quiet Now•Affinity•1986','\
The Phil Woods Quartet•Live From New York•Palo Alto Records•1985','\
The Bill Evans Trio•Quiet Now•Affinity•1981','\
The Michel Petrucciani Trio•Estate•Riviera Records (2)•1982','\
Bill Evans•Montreux II•CTI Records•1970','\
Bill Evans•Autumn Leaves•International Joker Production•1977','\
The Charles Lloyd Quartet•Montreux 82•Elektra Musician•1983','\
Ali Ryerson•Portraits In Silver•Concord Jazz•1995','\
Bobo Stenson Trio•Very Early•Dragon (8)•1987'),'\
\
Virago\
':('\
Billy Joe Walker Jr.•Painting Music•MCA Records•1989','\
Anthony-Cédric Vuagniaux•La Virago•Plombage Records•2012'),'\
\
Vonetta\
':('\
Miles Davis•Sorcerer•Columbia•1967','\
Reggie Moore (2)•Wishbone•Mainstream Records•1971','\
The Tony Rice Unit•Still Inside•Rounder Records•1981','\
Earl Klugh•Earl Klugh•Blue Note•1976','\
The Baron Von Ohlen Quartet•The Baron•Creative World•1973'),'\
\
Voyage\
':('\
The Art Ensemble Of Chicago•Live Part 2•BYG Records•1975','\
The Art Ensemble Of Chicago•Live•Affinity•1980','\
David Arkenstone•In The Wake Of The Wind•Narada Artist Series•1991','\
Charles Tyler•Live In Europe: Jazz Festival Umea•AK-BA Records•1977','\
Frank Chacksfield & His Orchestra•Catalan Sunshine•London Records•1957','\
Marc Moulin•Le Grand Voyage•Blue Note•2006','\
Herbie Hancock•Spider•Columbia•1977','\
Herbie Hancock•Dedication•CBS/Sony•1974'),'\
\
Wabash III\
':('\
John Scofield•Live 3 Ways•Pioneer Artists•1990','\
John Scofield•Time On My Hands•Blue Note•1990','\
The Famous Choraliers•The Famous Choraliers And The Longines Symphonette In The World\'s Most Honored Family Singing And Listening Songs•Longines Symphonette Society•0'),'\
\
Wait Till You See Her\
':('\
Ella Fitzgerald•Ella Fitzgerald Sings The Rodgers  And Hart Song Book•Verve Records•1957','\
Bonnie Prudden•Keep Fit And Be Happy•Warner Bros. Records•0','\
John Abercrombie Quartet•Wait Till You See Her•ECM Records•2009','\
Charles Lloyd•Autumn In New York•Destiny Records•1979','\
Miles Davis•Quiet Nights•Columbia•1964','\
Johnny Smith Quartet•The Johnny Smith Quartet•Roost•1955','\
Jimmy Raney•Solo•Xanadu Records•1978','\
Joe Pass•Montreux \'77•Pablo Live•1977','\
The Phil Woods Quartet•Warm Woods•Epic•1958'),'\
\
Walk Of The Negress\
':('\
Robert Hurst•Robert Hurst Presents: Robert Hurst•DIW•1993'),'\
\
Walk On By\
':('\
The Afro Blues Quintet Plus One•Liberation•Mira Records•1966','\
Sandy Lynn•Quelli Che Hanno Un Cuore (Anyone Who Had A Heart) / Walk On By•Vedette Records•1964','\
The Afro Blues Quintet Plus One•Introducing The Afro Blues Quintet Plus One•Mira Records•1965','\
Leroy Vinnegar Sextet•Leroy Walks!•Contemporary Records•1958','\
Dionne Warwick•Walk On By•Old Gold (2)•0','\
Dionne Warwick•Walk On By•Scepter Records•1964','\
The Wildare Express•A River\'s Invitation•Brunswick•1968','\
Dionne Warwick•Anyone Who Had A Heart / Walk On By•Universum Music•0','\
The Dells•Walk On By•Cadet•1972','\
George Benson•Giblet Gravy•Verve Records•1968','\
Brother Jack McDuff•Too Many Fish In The Sea•Prestige•1966','\
Stanley Turrentine•Rough \'N Tumble•Blue Note•1966'),'\
\
Walk Tall\
':('\
Mark Soskin•Walk Tall / Colossus•Prestige•1980','\
Hiroshi Suzuki (2)•Cat•Columbia•1975','\
The Cannonball Adderley Quintet•Kronika Dzwiękowa JJ 72 / Laboratorium I Zbigniew Seifert•PSJ Klub Płytowy•1972','\
Cannonball Adderley•Alto Giant•International Joker Production•1977','\
The Cannonball Adderley Quintet•Walk Tall (Baby That\'s What I Need) / Do Do Do (What Now Is Next)•Capitol Records•1967','\
Mark Soskin•Rhythm Vision•Prestige•1980','\
The Cannonball Adderley Quintet•Music You All•Capitol Records•1976','\
The Cannonball Adderley Quintet•74 Miles Away / Walk Tall•Capitol Records•1967','\
The Cannonball Adderley Quintet•Liederhalle Stuttgart March 20 1969•Jazzhaus•2012','\
The Cannonball Adderley Quintet•Country Preacher•Capitol Records•1970','\
Cannonball Adderley•Greatest Hits•CEMA Special Markets•1992'),'\
\
Walkin\'\
':('\
Herbie Mann & His Afro Jazz•Walkin\'•Atlantic•1961','\
Freddie Hubbard•The Night Of The Cookers - Live At Club La Marchal Volume 1•Blue Note•1965','\
Pee Wee Hunt And His Orchestra•Walkin\' Along / Help•Capitol Records•1954','\
Al Hirt•Cotton Candy•RCA Victor•1964','\
Chet Baker•Star Eyes•Marshmallow (3)•1990','\
The Miles Davis Sextet•Miles Davis All Star Sextet•Prestige•1954'),'\
\
Walkin\' Shoes\
':('\
Gerry Mulligan Quartet•Bernie\'s Tune / Walkin\' Shoes•Vogue Productions•1956','\
Gerry Mulligan Quartet•Lullaby Of The Leaves / Walkin\' Shoes•Swing (3)•1953','\
Gerry Mulligan Quartet•Paris Concert•Vogue•1957','\
Gerry Mulligan Quartet•Paris Concerrt•Pacific Jazz•1956','\
Gerry Mulligan Quartet•Gerry Mulligan Quartet•Pacific Jazz•1952','\
Art Pepper•Art Pepper + Eleven (Modern Jazz Classics)•Contemporary Records•1959','\
Gerry Mulligan Quartet•Vol. 3•Vogue Productions•1955','\
Gerry Mulligan Quartet•Concert In Paris (Vol. 1)•Barben Records•0','\
Gerry Mulligan Quartet•A Night In Rome Vol. 1•Fini Jazz•1990'),'\
\
Walk\'in Thing\
':('\
Charlie Johnson & His Paradise Band•The Boy In The Boat / Walk That Thing•Victor•1929','\
Gerry Mulligan•The Complete Gerry Mulligan Meets Ben Webster Sessions•Verve Records•1997','\
Various•Justice Records Sampler - The First Year•Justice Records (2)•1992','\
Various•Mood Music Sampler•Trans-World•0','\
Dick Wellstood•This Is The One...Dig!•Solo Art•1994','\
Preservation Hall Jazz Band•Shake That Thing•Preservation Hall Recordings•2004','\
Horace Silver•A Prescription For The Blues•Impulse!•1997','\
Jim Collier (3)•Three O\'Clock In The Morning - A Walk In The Black Forest•Wyncote•1964','\
Various•Home Cookin’ (Infectious Grooves Steamed By Blue Note)•Blue Note•2002','\
Devil Doll (2)•Queen Of Pain•Lucky Bluebird Records•2001','\
Artie Shaw•Artie Shaw•Everest Records Archive Of Folk & Jazz Music•1972','\
Various•Ez Jazz Vol. 2•EMI•2002','\
Gene Bianco•Your All-Time Favorite Songs (As Chosen By Members Of The RCA Victor Record Club)•RCA•1964'),'\
\
Walkin\' Thing\
':('\
The Cecil Payne Quartet•Casbah•Empathy Records•1986','\
Stanley Turrentine•West Side Highway•Fantasy•1978','\
The J.J. Johnson Quintet•J. J. In Person!•Columbia•1958','\
Phineas Newborn Trio•The Newborn Touch•Contemporary Records•1966','\
Benny Carter•Jazz Giant•Contemporary Records•1958','\
Benny Carter•The King•Pablo Records•1976','\
Ray Conniff•Die Ganze Welt Tanzt Mit Ray Conniff•Philips•1961'),'\
\
Wall Street\
':('\
The Jungle Band (2)•Wall Street Wail / Cotton Club Stomp•Brunswick•1930','\
Herb Alpert & The Tijuana Brass•Casino Royale•A&M Records•1967','\
Duke Ellington And His Orchestra•Ellingtonia Volume 1•Brunswick•1943','\
Duke Ellington And His Orchestra•Early Ellington•Brunswick•1954','\
Scott Joplin•Ragtime 1868-1917•Jugoton•1987','\
Jackie Mittoo•Showcase•Studio One•1980','\
Daniel Zimmermann•Bone Machine•Gaya Music Production•2013','\
Scott Joplin•Palm Leaf Rag•Angel Records•1974','\
Various•Boogie Woogie Rarities 1927-1932•Milestone (4)•1978','\
Duke Ellington•Duke Ellington "Rockin\' In Rhythm" Vol. 3 (1929-1931)•Decca•1970','\
Jacob Fred Jazz Odyssey•The Race Riot Suite•Kinnara Records•2011','\
Scott Joplin•16 Classic Rags•RCA Gold Seal•1976'),'\
\
Walter L.\
':('\
Gary Burton Quartet•In Concert•RCA Victor•1968','\
Gary Burton Quartet•Green Apple•Moon Records (4)•1989','\
Jimmy Gordon And His Jazznpops Band•Hog Fat•Flying Dutchman•1969','\
Frank Ricotti Quartet•Our Point Of View•CBS•1969','\
Gary Burton•Quartet Live•Concord Jazz•2009','\
Various•Dusty Fingers Volume Seven•Strictly Breaks Records•1999','\
Keith Emerson•Off The Shelf•Castle Music•2006','\
Gary Burton & Friends•Tennessee Firebird•RCA Victor•1967','\
Various•The Illmatic Collection•Strictly Breaks Records•2002'),'\
\
Waltse for Dave\
':('\
Chick Corea•Friends•Polydor•1978'),'\
\
Waltz\
':('\
Guy Lombardo And His Royal Canadians•Waltzland•Decca•0','\
Various•A Group Of Old Time Waltzes•Decca•0','\
"Deadly" Headley Bennett•Deadly Headly Bennett Meets The Magnificent Ossie Scott•Gorgon Records•0','\
Wayne King And His Orchestra•Wine Woman And Song / That Naughty Waltz•Victor•1940','\
Rawicz & Landauer•The Great Waltzes•Decca•1966','\
Ashley Miller•The Famous Radio City Music Hall Organ•Columbia•0','\
Mantovani And His Orchestra•The Skaters Waltz / The Midnight Waltz•Decca•1953','\
Guy Lombardo And His Royal Canadians•The River Seine / Waltz Waltz Waltz•Decca•1953','\
The Magic Organ•Waltz Time•Ranwood•1975','\
Victor Military Band•Cecile - Waltz Hesitation / Millicent - Waltz Hesitation•Victor•1915','\
The Three Suns•The Three Suns In Three Quarter Time•RCA Victor•1951','\
Ken Griffin (2)•Waltz Favorites•Sony Music Special Products•1993','\
Marden Abadi•Classic Rags: Scott Joplin•Sine Qua Non•1983'),'\
\
Waltz for a Lovely Wife\
':('\
Stan Getz•Nobody Else But Me•Verve Records•1994','\
Gary Burton•Gary Burton•International Polydor Production•0','\
Larry Bunker Quartette•Live At Shelly\'s Manne-Hole•Vault•1966','\
Stan Getz Quartet•The "Brilliant" Canadian Concert Of Stan Getz•Can-Am Records•0','\
The Phil Woods Quartet•Warm Woods•Epic•1958','\
Stan Getz•Anthology•il Sole 24 Ore•2011','\
Stan Getz•Live At Newport 1964•Solitude Records (2)•2014','\
Frank Sinatra•The Complete Reprise Studio Recordings•Reprise Records•1995'),'\
\
Waltz for Debby\
':('\
Cannonball Adderley•Waltz For Debby / Who Cares?•Riverside Records•1963','\
Giuseppe Emmanuele Quintet•A Waltz For Debby•Splasc(h) Records•1990','\
Cannonball Adderley•Greatest Hits (The Riverside Years)•Milestone (4)•2006'),'\
\
Waltz New\
':('\
Guy Lombardo And His Royal Canadians•Waltzland•Decca•0','\
Mary Lou Williams•Don Byas - Mary Lou Williams Quartet•Vogue•0','\
George Coleman•Amsterdam After Dark•Timeless Records (3)•1979','\
The Michel Petrucciani Trio•Live At The Village Vanguard Volume 2•Video Artists International•1982','\
Ron Carter Quartet•Parfait•Milestone (4)•1982','\
101 Strings•Play Hit American Waltzes•Somerset•1958','\
Michel Petrucciani•Power Of Three – Live At Montreux•Pioneer LDCE Ltd.•1990','\
Peter Leitch•Jump Street•Pausa Records•1982','\
Communication (4)•Live At Fat Tuesday\'s New York Vol.2•Paddle Wheel•1981','\
Jim Hall•Jim Hall / Red Mitchell•Artists House•1978','\
Bill Mays•Two Of A Mind•ITI Records•1983','\
Tullio De Piscopo•Live•Carosello•1981','\
Sebastian Spanache Trio•Humanized•Fiver House Records•2013','\
Dog Life•Dog Life•Omlott•2014'),'\
\
Waltzin\'\
':('\
Johnny Keating And The Z-men•Getaway•Piccadilly•1963','\
Freddie Redd•Straight Ahead!•Interplay Records•1977','\
The Mike Mainieri Quartet•Blues On The Other Side•Argo (6)•1962','\
Hélio Delmiro•Emotiva•EMI•1980','\
Allen Mezquida•A Good Thing•Trouser Down•1993','\
Bud Shank•Bud Shank In Africa•Pacific Jazz•1958','\
Freddie Redd•Live At The Studio Grill•Triloka Records•1990','\
Adrian Legg•Wine Women & Waltz•Relativity•1993','\
Benny Carter And His Orchestra•Swingin\' At Maida Vale•Decca•1958','\
The Dick Hyman Trio•A Waltz Dressed In Blue•Grapevine (4)•1977','\
Jack Hansen And His Orchestra•Discotheque•Dance Along Records•0','\
Bud Shank•The Pacific Jazz Bud Shank Studio Sessions•Mosaic Records (2)•1998'),'\
\
Warm Valley\
':('\
Duke Ellington And His Orchestra•Warm Valley•V Disc•0','\
Duke Ellington And His Orchestra•Bluejean Beguine / Warm Valley•Capitol Records•1953','\
Duke Ellington And His Orchestra•Warm Valley / The Flaming Sword•Victor•1940','\
Duke Ellington And His Orchestra•Band Call•Capitol Records•1956','\
Elvin Jones•Heart To Heart•Denon•1981','\
Robin Kenyatta•Nomusa•Muse Records•1975','\
Mel Lewis Quintet•Mellifluous•Gatemouth•1981','\
Louis Scherr•Warm Valley•no label•1993','\
Jerome Richardson•Roamin\' With Richardson•New Jazz•1959','\
Duke Ellington•Money Jungle•United Artists Jazz•1962'),'\
\
Watch What Happens\
':('\
Wes Montgomery•Windy / Watch What Happens•A&M Records•1967','\
no artist•The Frog•A&M Records•1968','\
no artist•The Frog•A&M Records•1967','\
The Moonlighters (9)•Watch What Happens / Watermelon Man•Thunderbird Records•0','\
Lena Horne•Rocky Raccoon / Watch What Happens•Skye Records•1969','\
Shamek Farrah•First Impressions•Strata-East•1974','\
Chris Montez•Watch What Happens•A&M Records•1968','\
Stanley Turrentine•Ain\'t No Way•Blue Note•1981','\
LA4•Watch What Happens•Concord Jazz•1978','\
Billy Butler (3)•Night Life•Prestige•1971','\
Art Farmer•What Happens ?...•Campi-Editore Recording•1968','\
Billy Butler (3)•Night Life•Prestige•1971','\
Milt Jackson•Jackson Johnson Brown & Company•Pablo Records•1983'),'\
\
Water Colors\
':('\
Ralph Peterson Trio•Triangular•Blue Note•1989','\
Liz Story•Solid Colors•Windham Hill Records•1983','\
Chuck Loeb•Life Colors•DMP•1990','\
David Murray•Lovers•DIW•1988','\
Dotsero•Jubillee•Not On Label (Dotsero Self-released)•1991','\
Shai Maestro Trio•The Stone Skipper•Sound Surveyor Music•2016','\
Josee Koning•Dois Mundos•VIA Jazz•1998','\
Ladies Of Soul•Live At The Ziggodome 2017•Not On Label•2017','\
Frank Sinatra•The Complete Reprise Studio Recordings•Reprise Records•1995'),'\
\
Waterwings\
':('\
Friendship (3)•Friendship•Elektra•1979'),'\
\
Wave\
':('\
Antonio Carlos Jobim•Wave / Triste•A&M Records•0','\
no artist•Nature•Nwog Records•2015','\
Fletcher Henderson And His Orchestra•Tidal Wave / Memphis Blues•Brunswick•0','\
The Crusaders•On Broadway / Heat Wave•World Pacific Records•1964','\
Marilyn Monroe•Heat Wave•Maybellene•1987','\
George Shearing•Don\'t Blame Me/Brain Wave•MGM Records•0','\
Біокорд•High Skies•Караван CD•1995','\
Bengt Hallberg•Jazz From Sweden VIII•Philips•1956','\
Junior Mance•Live At Sweet Basil•Flying Disk•1977','\
Yosuke Yamashita•Inner Space•Enja Records•1977','\
The Sandpipers•Wave / Temptation•A&M Records•1969','\
Alex Malheiros•The Wave•Far Out Recordings•2009'),'\
\
Way You Look Tonight The\
':('\
Lionel Hampton Quintet•The Way You Look Tonight•Clef Records•0','\
Zoot Sims/Dick Nash Octet•Nash-Ville•Zim Records•1977','\
Erroll Garner•Turquoise / The Way You Look Tonight•Atlantic•1949','\
Maroon 5•The Way You Look Tonight•A&M Octone Records•2009','\
Lynn Hope & Orchestra•Tenderly / Jet And The Way You Look Tonight•Aladdin (6)•1953','\
Erroll Garner•One World Concert - Vol. 1•Philips•0','\
The Dave Brubeck Octet•The Way You Look Tonight / Love Walked In•Fantasy•1950','\
The Dave Brubeck Quartet•Jazz At Oberlin•Fantasy•1953','\
Stan Getz Quintet•The Way You Look Tonight / Stars Fell On Alabama•Mercury•1952','\
Maynard Ferguson•Dimensions Vol. 1 Feat. Maynard Ferguson•EmArcy•0','\
Sonny Stitt Quartet•The Hard Swing•Verve Records•1960','\
Eric Dolphy•In Europe Vol. 2•Prestige•1965','\
Johnny Griffin•A Blowing Session•Blue Note•1957','\
Art Blakey Quintet•A Night At Birdland Vol. 3•Blue Note•1984'),'\
\
Weaver of Dreams A\
':('\
Monty Alexander•Threesome•Soul Note•1986','\
Eraldo Volonté•My Point Of View•Durium•1963','\
Cedar Walton Trio•Song Of Delilah•Venus Records (5)•2010','\
The Cannonball Adderley Quintet•In Chicago•Mercury•1960','\
The Lee Konitz Trio•Oleo•Sonet•1975','\
Henryk Miśkiewicz•No More Love•Polonia Records•2000','\
Don Grolnick•Weaver Of Dreams•Blue Note•1990','\
Various•Foundations Of Modern Jazz•Dunhill Compact Classics•1986'),'\
\
Webb City\
':('\
Art Blakey & The Jazz Messengers•Art Blakey In Sweden•Amigo•1982','\
The New Phil Woods Quintet•Integrity The New Phil Woods Quintet Live•Red Record•1985','\
The Barry Harris Sextet•Luminescence!•Prestige•1967','\
Sonny Stitt•Constellation•Cobblestone•1972','\
The Phil Woods Quartet•Live From New York•Palo Alto Records•1985','\
Art Pepper Quartet•The Art Of Pepper•Omegatape•1957','\
Art Blakey & The Jazz Messengers•Straight Ahead•Concord Jazz•1981','\
Tommy Turrentine•Tommy Turrentine•Time Records (3)•1960','\
Art Pepper•Omega Alpha•Blue Note•1981','\
The Phil Woods Quartet•The Phil Woods Quartet/Quintet 20th Anniversary Set•Mosaic Records (2)•1995','\
Sonny Stitt•Endgame Brilliance: Tune-Up! - Constellation•32 Jazz•1997'),'\
\
Wee\
':('\
Duke Henderson•Oo\' Wee Baby Oo\' Wee / Wiggle Wiggle Woogie•Apollo Records (2)•1945','\
Art Blakey Quintet•A Night At Birdland Volume One•Blue Note•2001','\
Jacques Leroy And His Orchestra•Wee Tom / Petite Fleur•Embassy•1959','\
Lionel Hampton And His Orchestra•Beulah\'s Sister\'s Boogie / Wee Albert•Decca•0','\
Gerry Mulligan•Night Lights•Philips•1963','\
The Be Bop Boys•Thriving On A Riff / Wee Dot•Savoy Records•1946','\
Dizzy Gillespie•Jazz At Massey Hall Volume 2•Debut Records (3)•0','\
Mal Waldron•Mal Waldron With The Steve Lacy Quintet•America Records•1972','\
Jimmy Lyons Quintet•Wee Sneezawee•Black Saint•1984','\
Art Blakey Quintet•A Night At Birdland Vol. 2•Blue Note•1954','\
Hank Mobley•Another Monday Night At Birdland•Roulette•1959','\
Johnny Griffin•Live In Tokyo•Philips•1976','\
The Quintet•Jazz At Massey Hall Volume Three•Debut Records•1953'),'\
\
Weekend Blues\
':('\
Duke Ellington•Duke Ellington Meets Leonard Feather•Sutton•0','\
Gramine•Gramine•Polskie Nagrania Muza•1974','\
Dave Lambert (3)•Sing/Swing Along With Dave Lambert•United Artists Records•1960','\
George Chisholm Sextet•"Chis" (The Art Of George Chisholm)•Decca•1956','\
Robert W. Baldwin•Jazz Loon•NorthSound•1995','\
Franco Chiari E Il Suo Complesso•Franco Chiari E Il Suo Complesso Volume II•Duse Record•1974','\
The Don Lusher Big Band•Pays Tribute To The Great Bands: Volume Two•Horatio Nelson Records•0','\
The Eddie Higgins Trio•If Dreams Come True•Venus Records (5)•2004','\
Various•The 1940\'s - The Small Groups: New Directions•CBS•1988','\
Ted Heath•The Very Best Of Ted Heath Volume One•Horatio Nelson Records•1995','\
Blossom Dearie•Positively Volume VII•Daffodil Records (2)•1983','\
Mr. Confuse & The Confusers•Feel The Fire - LIVE•Confunktion Records•2014','\
Jean Martyn•Puttin\' On The Style•Grosvenor•2003','\
Mabel Mercer•The Art Of Mabel Mercer•Atlantic•1959'),'\
\
We\'ll Be Together Again\
':('\
Paul Bley Trio•The Nearness Of You•SteepleChase•1989','\
Derek Smith•To Love Again•Venus Records (5)•2009','\
Joe Pass•Virtuoso In New York•Pablo Records•2004','\
Vi Redd•Lady Soul•Atco Records•1963','\
Louis Armstrong•Jazz History Vol. 9•Verve Records•1973','\
Eugene Chadbourne•Jungle Cookies•Old Gold•1998','\
Various•Fabulous Memories Of The Fabulous \'40s•no label•1981','\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014'),'\
\
Well You Needn\'t\
':('\
Thelonious Monk Septet•Well You Needn\'t•Riverside Records•1957','\
MAST (4)•Thelonious Sphere Monk•World Galaxy Records•2018','\
Frank Rosolino And His Quartet•Jazz Scene USA•Shanachie•2001','\
Thelonious Monk•Thelonious Monk•GNP Crescendo•1972','\
Thelonious Monk•Thelonious Monk•GNP Crescendo•1972','\
Sonny Simmons•Jazz Tempo Latin Accents!•Audio Fidelity•1965','\
Various•Dazzling Jazz - Modern•Philips•0','\
Chet Baker Sextet•Chet Is Back!•RCA Victor•1962','\
Klaus Doldinger•Doldinger In New York [Street Of Dreams]•WEA•1994','\
Jamie Cullum•Devil May Care!•Candid•2010','\
Johnny Griffin•The Toughest Tenors•Milestone (4)•1976'),'\
\
Wendy\
':('\
Orchester Friedel Berlipp•Downtown•Vogue Schallplatten•1965','\
Hal Singer•Blue Stompin\'•Prestige•1959','\
Jim Hall•By Arrangement•Telarc•1998','\
Michel Sardaby•Blue Sunset•Disques Debs•1967','\
Sounds Orchestral•Cast Your Fate To The Wind•Parkway•1965','\
Rob McConnell & The Boss Brass•Tribute•Pausa Records•1981','\
Sounds Orchestral•To Wendy With Love•Piccadilly•1965','\
Leo Diamond And His Orchestra•Skin Diver Suite And Other Selections•RCA Victor•1956','\
Spheroe•Spheroe•Cobra•1977','\
The Paul Desmond Quartet•Live•Horizon (3)•1976','\
John Neel•Blue Martini•Ava•1963','\
Gian Piero Reverberi•Stairway To Heaven•Pausa Records•1977','\
Sounds Orchestral•Cast Your Fate To The Wind•Disques Vogue•1965','\
Phyllis Emert•Focus On The Feeling•Essence Music (3)•1985'),'\
\
We\'re In This Love Together\
':('\
Al Jarreau•Al Jarreau And The Metropole Orkest Live•Concord Records•2012','\
Lester Lanin And His Orchestra•Everybody Dance•CBS•1968','\
Lester Lanin And His Orchestra•High Society (Volume 11)•Epic•0','\
Bill Evans•The Complete Fantasy Recordings•Fantasy•1989','\
Various•The Rise And Fall Of Paramount Records 1928-1932 Volume 2•Third Man Records•2014'),'\
\
West Coast Blues\
':('\
Wes Montgomery•Live In Paris 1965•no label•1988','\
Harold Land•West Coast Blues!•JAZZLAND•1960','\
Cannonball Adderley•The Uptown•Riverside Records•0','\
Various•Jazzland - The Stars Of Jazz•Jazzland•1961','\
Charles Mingus•East Coasting•Bethlehem Records•1957','\
Horace Parlan Trio•Hi-Fly•SteepleChase•1978','\
Tommy Flanagan•Something Borrowed Something Blue•Galaxy•1978','\
René Thomas•Meeting Mister Thomas•Barclay•1963','\
Pat Martino•Remember: A Tribute To Wes Montgomery•Blue Note•2006'),'\
\
What a Difference a Day Made\
':('\
Coleman Hawkins•Blue Moon / What A Difference A Day Made•no label•1935','\
Coleman Hawkins And His Orchestra•I\'ll See You Later / What A Difference A Day Made•Parrot (2)•1953','\
Sarah Vaughan•I Can\'t Get Started•MGM Records•1950','\
Lurlean Hunter•Night Life Vol. II•Vik•1957','\
Mulgrew Miller Trio•From Day To Day•Landmark Records (3)•1990','\
The Wilson Lewes Trio•The In Crowd•Diplomat Records•0','\
The Gipsy Jazz Violin Summit•The Gipsy Jazz Violin Summit•MPS Records•1979','\
Gipsy Jazz Violin Summit The•The Gipsy Jazz Violin Summit•MPS Records•1979','\
Roland Hanna•Impressions•Ahead (2)•1979','\
Sonny Rollins•+3•Milestone (4)•1996','\
Bill Doggett•The Doggett Beat For Happy Feet•King Records (3)•1959','\
Yoshiko Goto•Day Dream•Three Blind Mice•1975','\
Bobby Hackett•Jazz Session•Columbia•1950','\
Edmundo Ros & His Orchestra•The Latin World Of Edmundo Ros Vol. 2•Decca•1970','\
Albert Mangelsdorff•The Jazz Sextet•Moosicus•2017'),'\
\
What A Fool Believes\
':('\
Matt Bianco•What A Fool Believes•EastWest•1991','\
Piet Noordijk•Just When I Needed You Most•GIP•1979','\
Dee Daniels•Jazzinit•Three x D•2007','\
Kuh Ledesma•Precious•KZK Entertainment•1997','\
Matt Bianco•Sunshine Day - Summer Best Collection•Victor•2004','\
Donald Fagen•Live At Lincoln Center - The Dukes Of September•429 Records•2014','\
Sammy Davis Jr.•Greatest Hits•Garland•1988','\
Various•California Dreamin\': Smooth Jazz On A West Coast Trip•Metro Doubles•2002','\
Various•The Best Seventies Album In The World...Ever! Volume One•EMI 100•1997','\
Various•15 Χρόνια Ποπ + Ροκ 1978-1993•BMG•1993','\
Hot Chip•A Bugged Out Mix•New State Recordings•2009','\
Various•Revolutions In Sound: Warner Bros. Records The First Fifty Years•Warner Bros. Records•2008'),'\
\
What a Little Moonlight Can Do\
':('\
Bing Crosby•What A Little Moonlight Can Do / Down By The Riverside•Columbia•1953','\
Benny Goodman And His Orchestra•What A Little Moonlight Can Do / I\'ll Never Say "Never Again" Again•Columbia•1953','\
Eiji Kitamura•Swing Sessions•RCA•1978','\
Earl Hines•Giants Of Jazz - Earl Hines Remembers...•Time Life Records•1977','\
The Lew Tabackin Quartet•What A Little Moonlight Can Do•Concord Jazz•1994','\
Billie Holiday•Billie Holiday\'s Greatest Hits•Columbia•1967','\
The Lew Tabackin Quartet•What A Little Moonlight Can Do•Concord Jazz•1994','\
Miriam Klein•Lady Like (Miriam Klein Sings Billie Holiday)•MPS Records•1973','\
Various•Columbia Jazz Masterpieces Sampler Volume II•Columbia•1987','\
Miriam Klein•Honeysuckle Rose•Supraphon•1964','\
Jackie King•Moon Magic•Indigo Moon Records•1999','\
Dee Dee Bridgewater•Live At Yoshi\'s•Verve Records•2000','\
Billie Holiday•Easy To Remember•Society•1966','\
Billie Holiday•Billie Holiday Volume 1•SagaPan•1972','\
Betty Carter•Whatever Happened To Love?•Bet-Car Records•1982'),'\
\
What Am I Here For\
':('\
Duke Ellington And His Orchestra•I Don\'t Mind / What Am I Here For?•Victor•1944','\
Clifford Brown And Max Roach•Clifford Brown And Max Roach•EmArcy•1955','\
Clifford Brown And Max Roach•Clifford Brown And Max Roach•EmArcy•2005','\
Illinois Jacquet•Illinois Jacquet With Wild Bill Davis vol. 2•Black And Blue•1973','\
Shelly Manne•Essence•Galaxy•1977','\
Art Farmer•On The Road•Contemporary Records•1976','\
Duke Ellington•Jungle Triangle•Black Lion Records•1983','\
Ray Bryant•Golden Earrings•EmArcy•1988','\
Milt Jackson•Ain\'t But A Few Of Us Left•Pablo Records•1982','\
Cy Touff•His Octet & Quintet•Pacific Jazz•1956','\
Kenny Burrell•Togethering•Blue Note•1985','\
Billy Higgins•The Essence•DMP•1991'),'\
\
What Am I Here For?\
':('\
Duke Ellington And His Orchestra•I Don\'t Mind / What Am I Here For?•Victor•1944','\
Clifford Brown And Max Roach•Clifford Brown And Max Roach•EmArcy•2005','\
Clifford Brown And Max Roach•Clifford Brown And Max Roach•EmArcy•1955','\
Illinois Jacquet•Illinois Jacquet With Wild Bill Davis vol. 2•Black And Blue•1973','\
Shelly Manne•Essence•Galaxy•1977','\
Art Farmer•On The Road•Contemporary Records•1976','\
Duke Ellington•Jungle Triangle•Black Lion Records•1983','\
Ray Bryant•Golden Earrings•EmArcy•1988','\
Milt Jackson•Ain\'t But A Few Of Us Left•Pablo Records•1982','\
Cy Touff•His Octet & Quintet•Pacific Jazz•1956','\
Kenny Burrell•Togethering•Blue Note•1985','\
Billy Higgins•The Essence•DMP•1991'),'\
\
What Are You Doing The Rest Of Your Life\
':('\
Stan Kenton And His Orchestra•Intermission Riff•London Records•1972','\
Gene Ammons•Free Again•Prestige•1972','\
Pat Martino•The Visit!•Cobblestone•1972','\
Art Farmer•Yesterday\'s Thoughts•East Wind•1976','\
Reggie Moore (2)•Wishbone•Mainstream Records•1971','\
Kunio Ohta Quartet•Free And Lovely•Three Blind Mice•1976','\
Charlie Byrd Trio•Brazilville•Concord Jazz Picante•1982','\
Phil Woods•Cool Woods•no label•1999','\
Barney Kessel•Solo•Concord Records•1983'),'\
\
What Is This Thing Called Love?\
':('\
Various•Jam Session•EmArcy•1954','\
Artie Shaw And His Orchestra•What Is This Thing Called Love? / The Glider•MGM Records•1950','\
The Pasadena Roof Orchestra•Skokiaan•Transatlantic Records•1977','\
Various•Norman Granz\' Jam Session #2•Mercury•1953','\
Erroll Garner•Lover Man / What Is This Thing Called Love•Vogue Productions•1948','\
Sauter-Finegan Orchestra•Honey Babe•RCA Victor•0','\
Billie Holiday•What Is This Thing Called Love? / Don\'t Explain•Decca•1946','\
Jimmy Smith•Confirmation•Blue Note•1979','\
Artie Shaw And His Orchestra•Yesterday / What Is This Thing Called Love ?•no label•1939','\
The Dave Brubeck Octet•What Is This Thing Called Love / September In The Rain•Fantasy•1950','\
Ray Anthony & His Orchestra•Harlem Nocturne / What Is This Thing Called Love•Capitol Records•1951','\
Jack Wilkins•You Can\'t Live Without It•Chiaroscuro Records•1977'),'\
\
What The World Needs Now Is Love\
':('\
Tom Clay•What The World Needs Now Is Love•MoWest•1971','\
Mulgrew Miller•The Countdown•Landmark Records (3)•1989','\
Al Hirt•The Happy Trumpet•RCA Victor•1966','\
Houston Person•Underground Soul!•Prestige•1967','\
The Capp/Pierce Juggernaut•Live At The Century Plaza•Concord Jazz•1978','\
Ray Anthony•Hit Songs To Remember•Capitol Records•1966','\
Stanley Turrentine•Easy Walker•Blue Note•1967','\
Dwight Trible•Inspirations•Gondwana Records•2017','\
Freedom Sounds•Soul Sound System•Atlantic•1968','\
Art Blakey & The Jazz Messengers•Jazz Messengers \'70•Victor World Group•1972','\
Wes Montgomery•Plays The Hits•Verve Records•2010','\
Wes Montgomery•Tequila•Verve Records•1966'),'\
\
What Was\
':('\
Kenny Gill•What Was What Is What Will Be•Warner Bros. Records•1971','\
Charlie Parker With Strings•I Didn\'t Know What Time It Was / Summertime •Karusell•0','\
Artie Shaw And His Orchestra•Shadows / I Didn\'t Know What Time It Was•Bluebird (3)•1939','\
Benny Golson•Groovin\' With Golson•Metronome•0','\
Ray Peterson•I Forgot What It Was Like•Dunes Records•1963','\
Billy Eckstine•Till There Was You•Mercury•1962','\
The Dave Brubeck Trio•The Dave Brubeck Trio•Fantasy•1953','\
Dexter Gordon•Tangerine•Prestige•1975','\
Don Pullen•The Magic Triangle•Black Saint•1979','\
Stan Getz Quintet•Interpretations By The Stan Getz Quintet #2•Norgran Records•1954','\
Louis Jordan•I Didn\'t Know What Time It Was•Decca•1954','\
Joanne Brackeen•New True Illusion•Timeless Records (3)•1976','\
Benny Golson•Groovin\' With Golson•New Jazz•1959','\
Cedar Walton Quartet•Second Set•SteepleChase•1979','\
Charlie Parker•Bird At St. Nick\'s - Volume 1•Debut Records (3)•1957','\
Paul Smith Quartet•Softly Baby - Part 3•Capitol Records•1958','\
Peggy Lee•What More Can A Woman Do? / You Was Right Baby•Capitol Records•1945'),'\
\
What\'s Going On?\
':('\
John Fischer•6 x 1 = 10 Duos For A New Decade•ReEntry Records•1980','\
Hiroko Kokubu•Diary•JVC•1998','\
Les McCann•Live At Montreux•Atlantic•1973','\
Cal Collins•Cal Collins In San Francisco•Concord Jazz•1978','\
Al Cohn•Al Cohn\'s Tones•Savoy Records•1956','\
Acker Bilk•Some Of My Favourite Things•PYE Records•1973','\
Ella Fitzgerald•Ella Sings Gershwin•Decca•1951','\
Ray Charles•Ray Sings - Basie Swings•Hear Music•2006','\
Bill Easley•First Call•Milestone (4)•1991','\
John Lewis (2)•John Lewis / Helen Merrill•Mercury•1977','\
Ray Charles•True To Life•Atlantic•1977'),'\
\
What\'s Love Got To Do With It\
':('\
Ella Fitzgerald•I\'ve Got You Under My Skin•Success•1989','\
Ray Conniff•Say You Say Me•Columbia•1986','\
Steve Tyrell•This Guy\'s In Love•Columbia•2003','\
Artie Shaw And His Orchestra•Artie Shaw Hour•Royale•1952','\
Ella Fitzgerald•The Unique•The Entertainers•1987','\
Ella Fitzgerald•The First Lady Of Swing•The Entertainers•1987','\
Stéphane Grappelli•Live At The Blue Note•Telarc Jazz•1996','\
Various•Now - That\'s Love!•Capitol Records•1988','\
Billie Holiday•Billie Holiday•Art Of Music (2)•2014','\
Various•Dr. Breaks / The Chronicles•Not On Label•2003','\
Various•Ladies Of Burlesque•Sandy Hook Records•1979','\
Various•Anything Goes - Capitol Sings Cole Porter•Capitol Records•1992','\
Cole Porter•The Musical World Of Cole Porter•MGM Records•0'),'\
\
What\'s New?\
':('\
Johnny Lytle•Good Vibes•Muse Records•1982','\
Jamey Aebersold•The Magic Of Miles Davis•JA Records•1991','\
Jack Wilkins•You Can\'t Live Without It•Chiaroscuro Records•1977','\
Miles Davis•The Sound Of Miles Davis•Vap•1990','\
Sonny Stitt•Sonny\'s Last Recordings•Kingdom Jazz•1983','\
Louis Armstrong And His Dixieland Seven•Do You Know What It Means To Miss New Orleans / Endie•RCA Victor•1946','\
Dexter Gordon•A Day In Copenhagen•MPS Records•1969','\
Harry James (2)•Swing Session With Harry James•Capitol Special Markets•1982','\
Joanne Brackeen•New True Illusion•Timeless Records (3)•1976','\
Louis Armstrong•Do You Know What It Means To Miss New Orleans / Jack-Armstrong Blues•RCA•0','\
Miles Davis All Stars•Miles Davis All Stars And Gil Evans•Beppo Records•0','\
Raoul Björkenheim•Ritual•Not On Label•1988','\
Pete Fountain•A Closer Walk•Coral•1959'),'\
\
Wheelers And Dealers\
':('\
Jackie & Roy•Star Sounds•Concord Jazz•1980','\
Maria Muldaur•Transblucency•Uptown Records (2)•1986','\
Malcolm McNeill•Songdance•EMI•1986','\
Irene Kral•Kral Space•Catalyst Records (3)•1977','\
Dave Frishberg•Where You At?•Bloomdido•1991','\
Claire Martin•Old Boyfriends•Linn Records•1994','\
no artist•Another Time•Sunnyside•1981','\
Blossom Dearie•Volume IV Winchester In Apple Blossom Time •Daffodil Records (2)•1977'),'\
\
When A Man Loves A Woman\
':('\
Eddie Harris•When A Man Loves A Woman•Atlantic•1967','\
Takashi Mizuhashi Quartet•Live In "5 Days In Jazz 1974" - When A Man Loves A Woman•Three Blind Mice•1974','\
Raymond Lefèvre Et Son Grand Orchestre•Soul Coaxing (Ame Caline)•Major Minor•1968','\
Beryl Booker•Why Do I Love You / When A Woman Loves A Man•Mercury•1953','\
Grant Green Jr.•Jungle Strut•Venus Records (5)•1998','\
Buck Clayton•Buck & Buddy•Prestige Swingville•1961','\
Shirley Scott•Soul Song•Atlantic•1969','\
Raymond Lefèvre Et Son Grand Orchestre•Love Me Please Love Me•4 Corners Of The World•1967','\
Abbey Lincoln•That\'s Him!•Riverside Records•1957','\
Kenji Omura•Guitar Work Shop•Flying Dog•1977','\
Bobby Hackett And His Orchestra•Battle Of Jazz Volume 5•Brunswick•1953','\
Mel Powell•Mel Powell On Piano•Capitol Records•0','\
Wes Montgomery•Plays The Hits•Verve Records•2010','\
Kullrusk•Kullrusk•Moserobie Music Production•2004','\
Peter Moffitt•Riverdance•Novus•1989','\
Hank Crawford•Down On The Deuce•Milestone (4)•1984','\
Ruby Braff•2 Part Inventions In Jazz Vol. 2•Vanguard•1955'),'\
\
When All is Said and Done\
':('\
Billy Childs•Twilight Is Upon Us•Windham Hill Records•1989','\
Ric Flauding•Refuge•Spindletop Records•1988','\
Paul Mauriat•Tout Pour La Musique•Philips•1982','\
Inger Marie Gundersen•Feels Like Home•Stunt Records•2018','\
East Of Eden (2)•Here We Go Again…•EMI•1976','\
Nils Landgren Funk Unit•Funky ABBA•ACT (4)•2004','\
The Idea Of North•Live At The Powerhouse•ABC Jazz•2007','\
Shirley Bassey•Four Decades Of Song•Music For Pleasure•1996','\
Shirley Bassey•The Collection•EMI Gold•2008','\
The Dave Brubeck Quartet•The Columbia Studio Albums Collection 1955-1966•Columbia•2012','\
Louis Armstrong•Hotter Than That•Membran Music Ltd.•0','\
Ella Fitzgerald•Portrait•Past Perfect 24 Carat Gold Edition•2003','\
The Nat King Cole Trio•The Complete Capitol Recordings Of The Nat King Cole Trio•Mosaic Records (2)•1991','\
Various•Famous Jazz Singers: The Greatest Tracks (\'You Go To My Head\')•The Intense Media•0'),'\
\
When I Fall In Love\
':('\
Michael Bublé•When I Fall In Love•Reprise Records•2018','\
Etta Jones•People Will Say We\'re In Love / When I Fall In Love•King Records (3)•1960','\
Nat King Cole•When I Fall In Love / Stardust•Capitol Records•1973','\
Mehldau & Rossy Trio•When I Fall In Love•Fresh Sound New Talent•1994','\
Miles Davis•When I Fall In Love•Prestige•1961','\
Sandra Dee (3)•Dear Johnny / When I Fall In Love•Decca•1960','\
Nat King Cole•When I Fall In Love•Capitol Records•0','\
Blue Mitchell•Giants Meeting•Riverside Records•1964','\
Nat King Cole•Let There Be Love•Capitol Records•1992','\
Arthur Prysock•When I Fall In Love / April In Paris•Old Town Records•1961','\
Marilyn Monroe•When I Fall In Love•Zuma (2)•1987','\
Nat King Cole•When I Fall In Love / China Gate•Capitol Records•1957','\
Nat King Cole•When I Fall In Love•Capitol Records•1957','\
Jackie McLean•4 5 And 6•Prestige•1956','\
Westlife•Smile•RCA•2004','\
Phil Upchurch•When And If I Fall In Love•Physical Records (4)•1983','\
The John Young Trio•The John Young Trio•Delmark Records•1964','\
Linda Ronstadt•When I Fall In Love•Asylum Records•1985'),'\
\
When I Look In Your Eyes\
':('\
Andy Williams•When I Look In Your Eyes / Holly•Columbia•1967','\
Les & Larry Elgart•The Sound Of Silence•Columbia•1968','\
Lainie Kazan•Sunny / When I Look In Your Eyes•MGM Records•1967','\
Jeff Tyzik•New York Woman•Polydor•1984','\
Lainie Kazan•They Don\'t Give Medals (To Yesterday\'s Heroes) •MGM Records•1969','\
Laurindo Almeida•The Look Of Love And The Sounds Of Laurindo Almeida•Capitol Records•1968','\
Ahmad Jamal•Tranquility•Abc Records•1968','\
Cavril Payne•Cavril Sings•Ruval Records•1971','\
Ahmad Jamal•Tranquility / Outertimeinnerspace•Impulse!•2015','\
Günter Kallmann Chor•In Hollywood•4 Corners Of The World•1968','\
Jeff Tyzik•Jammin\' In Manhattan•Polydor•1984','\
Andy Williams•Love Andy•Columbia•1967','\
Sandy Nassan•Just Guitar•Embryo Records•1970','\
Gordon Beck + Two•Dr Dolittle Loves Jazz•Major Minor•1967','\
Ann Dee•Free Again•Capitol Records•1967'),'\
\
When Lights Are Low\
':('\
The Miles Davis Quartet•When Lights Are Low / Miles Ahead•Prestige•1955','\
Lionel Hampton And His Orchestra•Hot Mallets / When Lights Are Low•RCA Victor•0','\
Lionel Hampton And His Orchestra•Central Avenue Breakdown / When Lights Are Low •no label•1949','\
The George Shearing Quintet• When Lights Are Low / Lullaby Of Birdland•MGM Records•1952','\
The Miles Davis Quartet•When Lights Are Low•Prestige•1953','\
The King Sisters•In Hamburg / While The Lights Are Low•Capitol Records•1957','\
Oscar Peterson•Travelin\' On•MPS Records•1969','\
Eric Dolphy•In Europe / Volume 3.•Prestige•1965','\
The Pete Jolly Trio•When Lights Are Low•RCA Victor•1957'),'\
\
When Sunny Gets Blue\
':('\
Carmen McRae•When Sunny Gets Blue / Cutie Pants•Focus (8)•1964','\
Kenny Rankin•When Sunny Gets Blue•Little David Records•1977','\
Marian Montgomery•When Sunny Gets Blue•Capitol Records•0','\
Dakota Staton•Dynamic! Part 2•Capitol Records•1958','\
Johnny Mathis•Call Me•Fontana•1961','\
Hidefumi Toki Quartet•Toki•Three Blind Mice•1975','\
Jaki Byard•Out Front!•Prestige•1965','\
Ronnie Mathews•Trip To The Orient•East Wind•1975','\
Dexter Gordon Quartet•Something Different•SteepleChase•1980','\
Sonny Stitt•The Best Of Sonny Stitt With Brother Jack McDuff/For Lovers•Prestige•1972','\
Paul Desmond•Paul Desmond•Artists House•1978','\
Masaru Imada•Poppy•Three Blind Mice•1973','\
Johnny Hammond•Black Feeling!•Prestige•1970','\
McCoy Tyner•Today And Tomorrow•Impulse!•1964','\
Ira Sullivan Quintet•Nicky\'s Tune•Delmark Records•1970'),'\
\
When The World Was Young\
':('\
Pearl Bailey•Applause / When The World Was Young•Project 3 Total Sound•0','\
Mel Tormé•The London Sessions•MMS CLASSIX•0','\
Mel Tormé•A New Album•Gryphon•1980','\
Stan Getz•In Paris Live•Verve Records•1967','\
Ray Bryant•Slow Freight•Cadet•1967','\
Stan Getz Quartet•The "Brilliant" Canadian Concert Of Stan Getz•Can-Am Records•0','\
Nancy Wilson•Lush Life•Capitol Records•1967','\
Blossom Dearie•Blossom Time•Fontana•1966','\
Blossom Dearie•Blossom Time At Ronnie Scott\'s•Fontana•1966','\
Dick Johnson (3)•Dick Johnson Plays Alto Sax & Flute & Soprano Sax & Clarinet•Concord Jazz•1980','\
Morgana King•With A Taste Of Honey•Mainstream Records•1964','\
Peggy Lee•Black Coffee With Peggy Lee•Decca•1953','\
Eddie Heywood•Eddie Heywood At The Piano•Mercury•1960'),'\
\
When Your Lover Has Gone\
':('\
Stan Getz•Jazz Giants \'59•Verve Records•1959','\
The George Shearing Quintet•When Your Lover Has Gone / Carnegie Horizons•MGM Records•1950','\
Earl Bostic And His Orchestra•Cocktails For Two / When Your Lover Has Gone•Odeon•0','\
Maxine Sullivan•When Your Lover Has Gone / My Ideal•Decca•1943','\
The Roy Eldridge Quintet•When Your Lover Has Gone / I Can\'t Get Started•Clef Records•1954','\
Buddy DeFranco Quartet•The Music Of Buddy DeFranco•Norgran Records•1954','\
Sarah Vaughan•Serenata•Roulette•1960','\
Teuvo Suojärvi Quartet•Suomalaista Jazzia •Scandia•0','\
Art Farmer•2 Trumpets•Prestige•1956','\
Harry James And His Orchestra•When Your Lover Has Gone / I\'m Confessin\' (That I Love You)•Columbia•1945','\
Johnny Sparrow & His Bows And Arrows•When Your Lover Has Gone / Sparrow In The Barrel•Gotham•1952','\
Jimmy Forrest•Forrest Fire•New Jazz•1960','\
Gerry Mulligan•Gerry\'s Time•VSP•1966','\
Eddie Condon And His Orchestra•When Your Lover Has Gone / Wherever There\'s Love (There\'s You And I)•Decca•1945','\
Peggy Lord•When Your Lover Has Gone Astray•Stereoddities•0','\
Roy Eldridge•The Strolling Mr. Eldridge•Clef Records•1954'),'\
\
Whenever Your Heart Wants to Sing\
':('\
Kevyn Lettau•Kevyn Lettau•JVC•1991','\
Marion Meadows•Forbidden Fruit•Novus•1994'),'\
\
Where Are You\
':('\
Dinah Washington•Where Are You / Serenata•Roulette•0','\
Raymond Scott And His New Orchestra•Where You Are / Keep Cool Fool•Columbia•1941','\
Frank Sinatra•Where Are You? Part 1•Capitol Records•1956','\
Dinah Washington•Where Are You / You\'re Nobody \'Til Somebody Loves You•Roulette•1962','\
Russ Morgan And His Orchestra•Johnson Rag / Where Are You Blue Eyes?•Decca•1949','\
Jure Pukl•Hybrid•Whirlwind Recordings•2017','\
Andy Williams•Can\'t Take My Eyes Off You•CBS•1967','\
Oscar Brown Jr.•Brother Where Are You / Burning Fire•Fontana•1965','\
Tony Bennett•Anywhere I Wander•Columbia•1952','\
Ahmad Jamal•In Search Of Momentum•Birdology•2003','\
Sonny Rollins•Vol 1: "The Bridge" / Vol 2: With Coleman Hawkins "Sonny Meets Hawk!"•RCA•0','\
no artist•Chelsea Morning / Where Are You Coming From•A&M Records•1970','\
Eve Boswell•Where You Are / Pickin\' A Chicken•Capitol Records•1955','\
Les Brown And His Band Of Renown•Where You Are•Coral•1952','\
Claude Ciari•Where Are You My Only Love•Pathé•1970','\
Homer Rodeheaver•Brighten The Corner Where You Are / I Walk With The King•Victor•1915','\
Illinois Jacquet And His Orchestra•Blues In The Night•Blue Star•0','\
Zbigniew Seifert•Kilimanjaro•Studio Szlak Sound•1990'),'\
\
Where Are You?\
':('\
Dinah Washington•Where Are You / Serenata•Roulette•0','\
Raymond Scott And His New Orchestra•Where You Are / Keep Cool Fool•Columbia•1941','\
Frank Sinatra•Where Are You? Part 1•Capitol Records•1956','\
Dinah Washington•Where Are You / You\'re Nobody \'Til Somebody Loves You•Roulette•1962','\
Russ Morgan And His Orchestra•Johnson Rag / Where Are You Blue Eyes?•Decca•1949','\
Jure Pukl•Hybrid•Whirlwind Recordings•2017','\
Andy Williams•Can\'t Take My Eyes Off You•CBS•1967','\
Oscar Brown Jr.•Brother Where Are You / Burning Fire•Fontana•1965','\
Ahmad Jamal•In Search Of Momentum•Birdology•2003','\
Tony Bennett•Anywhere I Wander•Columbia•1952','\
Sonny Rollins•Vol 1: "The Bridge" / Vol 2: With Coleman Hawkins "Sonny Meets Hawk!"•RCA•0','\
no artist•Chelsea Morning / Where Are You Coming From•A&M Records•1970','\
Eve Boswell•Where You Are / Pickin\' A Chicken•Capitol Records•1955','\
Les Brown And His Band Of Renown•Where You Are•Coral•1952','\
Claude Ciari•Where Are You My Only Love•Pathé•1970','\
Homer Rodeheaver•Brighten The Corner Where You Are / I Walk With The King•Victor•1915','\
Vince Hill•This Song\'s For You•CBS•1977','\
Illinois Jacquet And His Orchestra•Blues In The Night•Blue Star•0','\
Zbigniew Seifert•Kilimanjaro•Studio Szlak Sound•1990'),'\
\
Where Is Love?\
':('\
no artist•Where Is The Love•Bell Records•1973','\
Frank Sinatra•Sinatra Sings Rodgers and Hart •Columbia•1954','\
Jackie McLean•A Ghetto Lullaby•SteepleChase•1974','\
Reel People•Seven Ways To Wonder (Especial Records Unreleased Remixes EP)•Especial Distribution•2008','\
Gato Barbieri•Tropico•A&M Records•1978','\
Sonny Stitt•Black Vibrations•Prestige•1972','\
Snowboy•The Soul Of Snowboy•Acid Jazz•1999','\
Phineas Newborn Jr.•Solo Piano•Atlantic•1975','\
Cal Tjader•Guarabe•Fantasy•1977','\
Dave Pike•As Long As He Needs Me•Prestige•1963','\
Houston Person•Why Not!•Muse Records•1991','\
Rita Reys•There Is No Greater•Philips•0'),'\
\
Where Or When\
':('\
Dave Mitchell Group•Temptation / Where Or When•Crystal (4)•0','\
Ralph Flanagan And His Orchestra•Where Or When •RCA Victor•1958','\
Oscar Peterson•Where Or When / Oscar\'s Blues•Mercury•0','\
Artie Shaw And His Orchestra•Two Blind Loves / Where Or When•no label•1940','\
Claude Thornhill And His Orchestra•Where Or When / Snowfall•Columbia•1941','\
Ray Conniff•Brazil / Where Or When•Philips•1959','\
Benny Goodman Sextet•Blues In The Night / Where Or When•Okeh•1942','\
Benny Goodman Trio•Where Or When? / I Cried For You•Bluebird (3)•1942','\
Erroll Garner•Concert By The Sea•Philips•0','\
Earl Bostic And His Orchestra•Roses Of Picardy / Where Or When•King Records (3)•1956','\
Oscar Brown Jr.•Work Song•CBS/Sony•1988','\
Lionel Hampton Quintet•Where Or When / There Will Never Be Another You•Decca•0','\
Jimmy Smith•At Club "Baby Grand" Wilmington Delaware Volume 1•Blue Note•1956','\
Benny Goodman Trio•Where Or When? / I\'m A Ding Dong Daddy•Victor•1937','\
Richard "Groove" Holmes•Shippin\' Out•Muse Records•1978','\
Marti Pellow•Take A Letter Miss Jones•Rhino Records (2)•2008'),'\
\
While We\'re Young\
':('\
Bill Evans•The Complete Fantasy Recordings•Fantasy•1989','\
Various•We Remember Them Well•no label•1986','\
Wes Montgomery•The Complete Riverside Recordings•Riverside Records•1992'),'\
\
Whisper Not\
':('\
Art Blakey & The Jazz Messengers•Blues March•Fontana•1959','\
Milt Jackson•Blues For Diahann / Whisper Not•United Artists Records•0','\
Art Blakey & The Jazz Messengers•Art\'s Break!•Lotus•1978','\
Art Blakey & The Jazz Messengers•Aurex Jazz Festival \'83•Eastworld•1983','\
Shelly Manne & His Men•At The Black Hawk Vol. 3•Contemporary Records•1960','\
Art Blakey & The Jazz Messengers•Au Club St. Germain Vol. 1•RCA•1959','\
Cedar Walton Sextet•The Art Blakey Legacy•Evidence (5)•1997','\
Ahmad Jamal•Extensions•Argo (6)•1965','\
Art Farmer•Big Blues•CTI Records•1979','\
Lee Morgan•Volume 2 - Sextet•Blue Note•1957','\
The Jazztet•The Jazztet - Real Time•Contemporary Records•1988','\
Art Blakey & The Jazz Messengers•Live in Holland 1958•Bandstand•1991'),'\
\
Who Can I Turn To\
':('\
Sonny Stitt•Who Can I Turn To?•Prestige•1965','\
Astrud Gilberto•Funny World•Verve Records•1965','\
Billy Taylor Trio•Who Can I Turn To / My One And Only Love•Prestige•1954','\
Hank Crawford•Who Can I Turn To (When Nobody Needs Me) / Soul Shoutin\'•Atlantic•1966','\
Willis Jackson•Goose Pimples / Who Can I Turn To (When Nobody Needs Me)•Cadet•1965','\
Frank Rosolino•Thinking About You•Sackville Recordings•1984','\
Shirley Bassey•The Dynamic Shirley Bassey•Columbia•1964','\
Al Serafini•Who Can I Turn To •Rozan Records•0','\
Isao Suzuki Trio•Black Orpheus•Three Blind Mice•1976','\
Kimiko Itoh•Jazzdaga? Jazzdaja!•PM Music (7)•2007','\
Dexter Gordon•Gettin\' Around•Blue Note•1966','\
Bill Evans•Autumn Leaves•International Joker Production•1977','\
Maynard Ferguson Sextet•Maynard Ferguson Sextet•CBC Radio Canada•1967','\
Richard "Groove" Holmes•American Pie•Groove Merchant•1972','\
Oscar Peterson•Mellow Mood•MPS Records•1969','\
Willie Smith (2)•The Best Of Willie Smith•GNP Crescendo•0','\
Sonny Stitt•Night Crawler•Prestige•1966'),'\
\
Who Can I Turn To?\
':('\
Sonny Stitt•Who Can I Turn To?•Prestige•1965','\
Astrud Gilberto•Funny World•Verve Records•1965','\
Billy Taylor Trio•Who Can I Turn To / My One And Only Love•Prestige•1954','\
Hank Crawford•Who Can I Turn To (When Nobody Needs Me) / Soul Shoutin\'•Atlantic•1966','\
Willis Jackson•Goose Pimples / Who Can I Turn To (When Nobody Needs Me)•Cadet•1965','\
Frank Rosolino•Thinking About You•Sackville Recordings•1984','\
Shirley Bassey•The Dynamic Shirley Bassey•Columbia•1964','\
Al Serafini•Who Can I Turn To •Rozan Records•0','\
Isao Suzuki Trio•Black Orpheus•Three Blind Mice•1976','\
Kimiko Itoh•Jazzdaga? Jazzdaja!•PM Music (7)•2007','\
Dexter Gordon•Gettin\' Around•Blue Note•1966','\
Bill Evans•Autumn Leaves•International Joker Production•1977','\
Maynard Ferguson Sextet•Maynard Ferguson Sextet•CBC Radio Canada•1967','\
Dexter Gordon•Gettin\' Around•Blue Note•1966','\
Kimiko Itoh•Jazzdaga? Jazzdaja!•PM Music (7)•2007','\
Richard "Groove" Holmes•American Pie•Groove Merchant•1972','\
Oscar Peterson•Mellow Mood•MPS Records•1969','\
Willie Smith (2)•The Best Of Willie Smith•GNP Crescendo•0','\
Sonny Stitt•Night Crawler•Prestige•1966'),'\
\
Who Cares?\
':('\
Cannonball Adderley•Waltz For Debby / Who Cares?•Riverside Records•1963','\
Lionel Hampton And His Orchestra•Oh Babe! / Who Cares•Decca•0','\
Fran Warren•I Almost Lost My Mind•RCA Victor•1952','\
André Previn•By Request•RCA Victor•0','\
Horace Parlan Trio•Pannonica•Enja Records•1984','\
The John Bunch Quintet•John\'s Bunch•Famous Door•1975','\
The Bob Brookmeyer Quartet•Old Friends •Storyville•1998','\
Kenny Dorham•\'Round About Midnight At The Cafe Bohemia Vol. 3•Blue Note•1984','\
Lionel Hampton•Cobb\'s Idea•Happy Bird•0','\
Karin Krog•Jazz Jamboree 75 Vol. 2•Polskie Nagrania Muza•0','\
Kenny Dorham•\'Round About Midnight At The Cafe Bohemia Vol. 2•Blue Note•1984','\
Horace Parlan Trio•Hi-Fly•SteepleChase•1978','\
Kenny Dorham•The Complete \'Round About Midnight At The Cafe Bohemia•Blue Note•1995','\
Vladimir Shafranov Trio•Live At Groovy•Kompass Records•1981'),'\
\
Whopper\
':('\
Willie Colón•El Malo•Fania Records•1968','\
Gary Burton Quartet•Passengers•ECM Records•1977','\
Eberhard Weber•Selected Recordings•ECM Records•2004','\
Sam Kininger•Sam Kininger•Velour Music Group•2004'),'\
\
Why Try To Change Me Now?\
':('\
Frank Sinatra•No One Cares (Part 3)•Capitol Records•1959','\
Elvin Jones•Brother John•Quicksilver•1982','\
Honi Gordon•Honi Gordon Sings•Prestige•1962','\
Frank Foster•Basie Is Our Boss•Argo (6)•1963','\
Arnett Cobb•Ballads By Cobb•Prestige•1960','\
Helen Humes•Helen•Muse Records•1981','\
Mathilde Santing•Out Of This Dream: A Third Side•Megadisc•1987','\
Cy Coleman Jazz Trio•Why Try To Change Me Now•Westminster•1959','\
no artist•On The Montreal Scene•Justin Time•1996','\
Norman Simmons Quintet•I\'m... The Blues•Milljac Pub Co.•1981','\
Russell Malone•Heartstrings•Verve Records•2001','\
Cy Coleman•If My Friends Could See Me Now•Columbia•1966','\
Paul Kuhn And The Best•Young At Heart•In+Out Records•2003','\
Nancy Steele•Nitey Nite•Chatam•1958','\
Sammy Davis Jr.•Our Shining Hour•Verve Records•1965','\
Sammy Davis Jr.•Our Shining Hour•Verve Records•1965','\
Deno Kannes•The Kid From Salt Lake City•Coral•1958'),'\
\
Wildflower\
':('\
Houston Person•Preachin\' And Teachin\'•Muse Records•1977','\
no artist•Bambalina / Wildflower•Brunswick•1923','\
Hank Crawford•Wildflower•Kudu•1974','\
Houston Person•Wild Flower•Muse Records•1978','\
Enrico Pieranunzi Trio•Infant Eyes•Challenge Records (3)•2000','\
Hank Crawford•Wildflower•Kudu•1973','\
Miho Hazama•Time River•Verve Records•2015','\
Herbie Nichols Trio•Herbie Nichols Trio•Blue Note•1956','\
Keiko Matsui•Wildflower•Narada Jazz•2003','\
Nostalgia 77•Everything Under The Sun•Tru Thoughts•2007','\
Vijay Iyer Trio•Accelerando•ACT (4)•2012','\
Tuck & Patti•Chocolat Moment•T&P RECORDS•2002'),'\
\
Will You Say You Will\
':('\
Eddie Henderson•Say You Will / Connie•Capitol Records•1977','\
Eddie Henderson•Say You Will / The Funk Surgeon•Capitol Records•1977','\
Eddie Henderson•Prance On / Say You Will•Capitol Records•1978','\
Gary Burton•Reunion•GRP•1990','\
Mitch Watkins•Curves•Enja Records•1990','\
Various•Planet London•Tongue And Groove Records•1993','\
The Lee Konitz Quartet•Tranquility•Verve Records•1957','\
Sylvia Syms•For Once In My Life•Prestige•1967','\
The Keith Emerson Trio•The Keith Emerson Trio•Record Collector Magazine•2015','\
Eddie Henderson•Comin\' Through•Capitol Records•1977','\
Bob Brookmeyer•Plays Bob Brookmeyer And Some Others•Clef Records•1955','\
The Red Garland Trio•Groovy•Prestige•1957','\
Freddy Martin And His Orchestra•Shall We Dance?•RCA Victor•1956'),'\
\
Will You Still Be Mine\
':('\
Ahmad Jamal Trio•Ahmad\'s Blues / Will You Still Be Mine•Okeh•1951','\
Lem Winchester•Winchester Special•Metronome•0','\
The Miles Davis Quartet•Miles•Esquire•1955','\
Jerry Duane•Will You Still Be Mine / London In July•Trend (3)•0','\
Art Farmer Quintet•At Boomers•East Wind•1976','\
Ron Carter•All Blues•CTI Records•1974','\
Sonny Rollins•Freedom Suite•Riverside Records•1958','\
Art Farmer•On The Road•Contemporary Records•1976','\
Sonny Rollins•Oleo•Ediciones Del Prado•1996'),'\
\
Willow\
':('\
The Riverside Jazz Stars•A Jazz Version Of Kean•Riverside Records•1961','\
Mildred Bailey And Her Alley Cats•Willow Tree / Honeysuckle Rose•Parlophone•1936','\
Jonas Howden Sjøvaag•West Wind Drift•Shipwreckords•2017','\
Roberta Linn•Willow In The Wind / Jump For Joy•Keen (2)•0','\
Stan Kenton And His Orchestra•Willow Weep For Me / Fantasy•Telefunken Capitol•1946','\
Tommy Dorsey And His Orchestra•Pussy Willow / Dream Of You•RCA Victor•0','\
Stan Kenton And His Orchestra•Willow Weep For Me / Fantasy•Telefunken Capitol•1946','\
Tommy Dorsey And His Orchestra•Pussy Willow / Dream Of You•RCA Victor•0','\
Mantovani And His Orchestra•Theme From "Villa Rides" / Willow Tree•Decca•1968','\
Lee Morgan•Speedball•Trip Jazz•1974','\
Red Prysock•Willow Weep For Me / Billie\'s Blues•Mercury•1958','\
Frances Faye•Comin Home Baby•Audio Fidelity Records Inc.•0'),'\
\
Willow Weep for Me\
':('\
Stan Kenton And His Orchestra•Willow Weep For Me / Fantasy•Telefunken Capitol•1946','\
Red Prysock•Willow Weep For Me / Billie\'s Blues•Mercury•1958','\
Lee Morgan•Speedball•Trip Jazz•1974','\
Frances Faye•Comin Home Baby•Audio Fidelity Records Inc.•0','\
The Modern Jazz Quartet•Versailles / Angel Eyes / Willow Weep For Me•Metronome•1956','\
Lee Morgan•Live Sessions•Trip Jazz•1975','\
Cab Calloway And His Orchestra•Willow Weep For Me / Jonah Joins The Cab•Okeh•1941','\
Cozy Cole All Stars•Take It On Back / Willow Weep For Me•Continental (6)•1945','\
Stan Kenton And His Orchestra•Willow Weep For Me / How High The Moon•Capitol Records•1950','\
Freddie McCoy•Belly Full Of Greens / Willow Weep For Me•Prestige•1965','\
Frank Sinatra•One For My Baby / Willow Weep For Me•Capitol Records•1956','\
Bill Jennings Quintet•Glide On / Willow Weep For Me•King Records (3)•1955','\
Sidney Bechet•Dardanella•Disques Vogue•0','\
John Coates Jr•Tokyo Concert•Omnisound (2)•1980','\
The Oscar Peterson Quartet•Just One Of Those Things / Willow Weep For Me•Karusell•0'),'\
\
Wind Sprint\
':('\
John Patitucci•John Patitucci•GRP•1988'),'\
\
Windows\
':('\
The Modern Jazz Quartet•One Never Knows•London Records•1959','\
Hubert Laws•Carnegie Hall•CTI Records•1973','\
The Knightsbridge Strings•Cry•Top Rank International•1960','\
Tony Osborne And His Orchestra•Summer Star •no label•1959','\
Stan Getz•Sweet Rain•Verve Records•1967','\
Jan Garbarek Group•Photo With Blue Sky White Cloud Wires Windows And A Red Roof•ECM Records•1979'),'\
\
Wings of Karma\
':('\
Mahavishnu Orchestra•Apocalypse•Columbia•1974','\
no artist•no title•no label•no year','\
Mahavishnu Orchestra•The Best Of The Mahavishnu Orchestra•Columbia•1980','\
Various•Contemporary Jazz Masters Sampler Volume 1•Columbia•1990','\
Mahavishnu Orchestra•Live At Montreux 1984 / 1974•Eagle Vision•2007','\
John McLaughlin•The Essential John McLaughlin•Columbia•2007','\
Mahavishnu Orchestra•Original Album Classics•Columbia•2007'),'\
\
Wise One\
':('\
The John Coltrane Quartet•Crescent•Impulse!•1964','\
Jazz Parasites•Very Early•Phonector•2006','\
Fumio Karashima Trio•Round Midnight•Full House (3)•1983','\
Dwight Trible•Living Water•no label•2004'),'\
\
Witch Hunt\
':('\
Donald Byrd•Witch Hunt / Woman Of The World•Blue Note•1973','\
no artist•Play For You•JA Records•1975','\
Kirk Lightsey Trio•Isotope•Criss Cross Jazz•1983','\
Art Blakey & The Jazz Messengers•Hard Champion•Paddle Wheel•1987','\
Wayne Shorter•Speak No Evil•Blue Note•1966','\
Donald Byrd•Street Lady•Blue Note•1973','\
Art Blakey & The Jazz Messengers•Album Of The Year•Timeless Records (3)•1981'),'\
\
Witchcraft\
':('\
Gabor Szabo•Witchcraft•Impulse!•1966','\
Frank Sinatra•Witchcraft•Capitol Records•0','\
Frank Sinatra•Chicago / Witchcraft•Capitol Records•0','\
Frank Sinatra•Come Fly With Me•Capitol Records•1978','\
George Benson•Jazz On A Sunday Afternoon Vol. II•Accord (2)•1981','\
Frank Sinatra•Witchcraft•Capitol Records•1957','\
Gerry Niewood•The Gerry Niewood Album•Sagoma•1975','\
Donald Byrd•Byrd In Hand•Blue Note•1959','\
Gerry Niewood•The Gerry Niewood Album•Sagoma•1975'),'\
\
With A Song In My Heart\
':('\
Ella Fitzgerald•All Of You•no label•0','\
Hal Singer•Blue Stompin\'•Prestige•1959','\
Ella Fitzgerald•With A Song In My Heart•no label•1959','\
Jack Reilly Trio•November•Progressive (3)•2003','\
Ella Fitzgerald•Ella Fitzgerald Sings The Rodgers And Hart Song Book Vol. 2•Karusell•1957','\
Dick Berk & The Jazz Adoption Agency•Music Of Rodgers & Hart•Trend Records (5)•1993','\
Sonny Clark•Sonny\'s Crib•Blue Note•1958','\
Chick Corea Akoustic Band•Live From The Blue Note Tokyo•Stretch Records•1996','\
Shelly Manne•Shelly Manne & Russ Freeman•Contemporary Records•1955','\
Sonny Rollins Quartet•Sonny Rollins Quartet•Prestige•1952'),'\
\
Without a Song\
':('\
Duke Ellington And His Orchestra•Satin Doll / Without A Song•Capitol Records•1953','\
John Abercrombie Quartet•Within A Song•ECM Records•2012','\
Tommy Dorsey And His Orchestra•Without A Song / Deep River •Victor•1941','\
Dick Stabile And His Orchestra•Poor Butterfly / Without A Song•Bethlehem Records•1958','\
Rex Stewart And His Orchestra•My Sunday Gal / Without A Song•Bluebird (3)•1940','\
Frank Sinatra•Forget Domani / Without A Song•Reprise Records•0','\
Ray McKinley And His Orchestra•Manhattan Serenade / Without A Song•Capitol Records•1942','\
Sonny Rollins Quartet•"Live" In Europe•Unique Jazz•0','\
Earl Grant•Without A Song•Decca•1967','\
Perry Como•Without A Song / More Than You Know•RCA Victor•1951','\
Abi Zeider•For The First Time•Mezhdunarodnaya Kniga•0','\
Willis Jackson•That Twistin\' Train•Tru-Sound•1962','\
Lee Konitz Nonet•Live At Laren•Soul Note•1984','\
Gloria Lynne•Serenade In Blue / Without A Song•Everest•1964','\
Sonny Rollins Quartet•In Europe 1963 - Vol. II•Jazz Up•1989','\
John Hicks•Two Of A Kind•Theresa Records•1989','\
Sonny Rollins•Soneymoon•Get Back•2007','\
Rolf Ericson•Stockholm Sweetnin\'•Dragon (8)•1985','\
Putte Wickman•Songs Without Words•Zenith (7)•1985','\
Vladimir Shafranov Trio•Live At Groovy•Kompass Records•1981'),'\
\
Woody \'n You\
':('\
Grant Green•First Session•Blue Note•2001','\
Yusef Lateef•Lateef At Cranbrook•Argo (6)•1958','\
The Red Garland Quintet•Soul Junction•Prestige•1960','\
The Kenny Dorham Quintet•Scandia Skies•SteepleChase•1980','\
The Giants Of Jazz (2)•Live•Jazz Door•1994','\
Miles Davis•Miles Plays Jazz Classics•Prestige•1965','\
Dizzy Gillespie•Tour De Force•Moon Records (4)•1989','\
Donald Byrd•Byrd Jazz•Transition•1956','\
Miles Davis•Volume 1•Blue Note•1988'),'\
\
Work Song\
':('\
Monk Higgins•Work Song•United Artists Records•1973','\
The Oscar Peterson Trio•Reunion Blues / Work Song•Verve Records•1962','\
Nat Adderley•Work Song!•Riverside Records•1960','\
The Oscar Peterson Trio•Very Tall•Verve Records•1963','\
Herb Alpert & The Tijuana Brass•The Work Song•A&M Records•1966','\
Oscar Brown Jr.•Work Song•CBS•1964','\
Oscar Brown Jr.•Work Song•Columbia•1961','\
Nina Simone•Work Song / Memphis In June•Colpix Records•1961','\
Oscar Brown Jr.•Work Song•CBS/Sony•1988','\
Manhattan Jazz Quintet•Face To Face Edition de Luxe•Paddle Wheel•1989'),'\
\
Wow\
':('\
Lennie Tristano Sextet•Wow / Crosscurrent•Capitol Records•1949','\
Wolfgang Schalk•From Here To There•Frame Up Music•2016','\
Grant Green•Windjammer•Blue Note•1972','\
Frank Motley•Frank Motley•Krazy Kat•1986','\
Eddie Smith (4)•Bow Wow Boogie / San Antonio Rose•King Records (3)•1951','\
Norman Connors•Betcha By Golly Wow /  Kwasi•Buddah Records•1976','\
Giuseppe Emmanuele Quintet•A Waltz For Debby•Splasc(h) Records•1990','\
Jimmy Giuffre•Western Suite•Atlantic•1960','\
Roy Porter Sound Machine•Jessica•Chelan Records•1971','\
Lifeforce (4)•Fearless Warriors•Numu Numu Records•1981','\
Ayumi Koketsu•Aquarelle•M & I•2017','\
Jason Stein Quartet•Lucille!•Delmark Records•2017'),'\
\
Wrap Your Troubles in Dreams\
':('\
Charles Mingus•The Eldridge Session•Doxy•2017','\
Sidney Bechet And His New Orleans Feetwarmers•Margie / Wrap Your Troubles In Dreams•Blue Star•0','\
Earl Bostic And His Orchestra•Wrap Your Troubles In Dreams / Serenade•King Records (3)•1950','\
Louis Armstrong And His Orchestra•Wrap Your Troubles In Dreams / A Monday Date•Parlophone•0','\
Jonah Jones•Wrap Your Troubles In Dreams / Stars Fell On Alabama•Bethlehem Records•1958','\
Sarah Vaughan•Serenata•Roulette•1960','\
no artist•Gatemouth•Storyville•1957','\
Hampton Hawes•For Real!•Contemporary Records•1961','\
Buddy Rich•Sing And Swing With Buddy Rich•Columbia•1956','\
Louis Armstrong And His Orchestra•Star Dust / Wrap Your Troubles In Dreams (And Dream Your Troubles Away)•OKeh•1931','\
Jonah Jones Sextette•Jonah Jones Part 2•Bethlehem Records•1956'),'\
\
Wrong Is Right\
':('\
Pat Metheny Group•Phase Dancer... Live \'77•Hi Hat•2015','\
Pat Metheny Group•Live In Concert•ECM Records•1977','\
Larry Coryell•Spaces•Vanguard Apostolic•1970','\
Gary Burton Quartet•In Concert•RCA Victor•1968','\
Pat Metheny Group•Offramp/Blue Asphalt•Grammy•2001','\
Various•Casino Lights•Warner Bros. Records•1982','\
Peter Beets•New York Trio - Page 3•Criss Cross Jazz•2005'),'\
\
Yardbird Suite\
':('\
The Modern Jazz Quartet•The Modern Jazz Quartet At Music Inn / Volume 2•Atlantic•0','\
The Charlie Parker Septet•Yardbird Suite / Moose The Mooche•Dial Records (3)•1946','\
California State University Fresno Jazz Band A•Hot Big Band Jazz Live At The Satellite•Accurate Analog Recordings•1984','\
The Charlie Parker All-Stars•Night In Tunisia•Sonet•0','\
Jimmy Smith•Jimmy Smith At The Organ Volume 1•Blue Note•1957','\
Miles Davis•World Of Jazz•Manhattan Records (3)•1980','\
Ron Carter•Birdology - Live At The TBB Jazzz Festival•Verve Records•1989','\
Charlie Parker•Charlie Parker On Dial Volume 1•Spotlite Records•1970','\
Max Roach Quartet•The Max Roach 4 Plays Charlie Parker•Mercury•1959','\
Howard McGhee•Here Comes Freddy•Pick (2)•1978'),'\
\
Yes and No\
':('\
The Wilder Brothers (2)•Timber / Yes And No•"X"•1955','\
no artist•Uptown Express•Palo Alto Jazz•1985','\
Franco Ambrosetti•Tentets•Enja Records•1985','\
Frank Morgan•Easy Living•Contemporary Records•1985','\
Thad Jones / Pepper Adams Quintet•Mean What You Say•Milestone (4)•1966','\
Franco Ambrosetti•Gin And Pentatonic•Enja Records•1992','\
Marcus Printup•Unveiled•Blue Note•1996','\
Branford Marsalis•Random Abstract•CBS•1988','\
Slavko Benić Orkestr•Weniger Ist Nicht Immer Mehr•STARPATROL•2012','\
Robert Glasper•Double Booked•Blue Note•2009','\
Misha Tsiganov•Spring Feelings•Criss Cross Jazz•2016','\
Harold Mabern•The Leading Man•Columbia•1993','\
David Goldblatt•Facing North•99 Records•1996'),'\
\
Yes or No\
':('\
Ricky Ford•Shorter Ideas•Muse Records•1985','\
Wayne Shorter•Juju•Blue Note•1964','\
Franco Ambrosetti•Tentets•Enja Records•1985','\
Franco Ambrosetti•Gin And Pentatonic•Enja Records•1992'),'\
\
Yesterday\
':('\
Johnny Hammond•Yesterday Was Cool•Salvation (4)•1974','\
Al De Lory•Yesterday / Traffic Jam•Phi-Dan Records•1965','\
David "Fathead" Newman•The Thirteenth Floor•Atlantic•1968','\
Freddie Hubbard•Hot Horn•Imagem•1984','\
Billie Holiday And Her Orchestra•Ghost Of Yesterday / Chitlin\' Switch Blues•Parlophone•0','\
Shirley Scott•Sent For You Yesterday•Impulse!•0','\
Al Hirt•Yesterday•RCA Victor•1965','\
Louis Armstrong & His Hot Seven•I Want A Little Girl / Blues For Yesterday•Swing (3)•1947','\
Artie Shaw And His Orchestra•Yesterday / What Is This Thing Called Love ?•no label•1939','\
Tony Bennett•Until Yesterday / Please Driver•Columbia•1954','\
Charles Earland•Greatest Hits•Prestige•2000','\
Eddy Howard And His Orchestra•Seems Like Yesterday•Mercury•1950','\
Mitch Miller And His Orchestra And Chorus•Bluebell / It Seems Like Only Yesterday•Columbia•1958'),'\
\
Yesterdays\
':('\
Lennie Tristano Sextet•Intuition / Yesterdays•Capitol Records•0','\
Benny Golson Quintet•Yesterdays / Drumboogie•New Jazz•1959','\
Maynard Ferguson & His Orchestra•Indiscreet/Yesterdays•Roulette•1958','\
Stan Getz Quartet•Yesterdays / Sweetie Pie•Roost•1950','\
Stan Kenton•Contemporary Concepts Part 2•Capitol Records•0','\
J.J. Johnson•Debut Records\' Jazz Workshop Volume One: Trombone Rapport•Debut Records•1953','\
The Miles Davis Sextet•Chance It / Yesterdays•Blue Note•1952','\
Freddie Hubbard•First Light•CTI Records•1972','\
Garry Moore•My Kind Of Music•Columbia•1956','\
Coleman Hawkins And His Orchestra•Bu-Dee-Daht / Yesterdays•Apollo Records (2)•1944','\
Eddie Miller And His Orchestra•Yesterdays / Stomp Mr. Henry Lee•Capitol Records•1944','\
Erroll Garner•Just You Just Me / Yesterdays•Selmer•0','\
The Milt Jackson Quartet•Yesterdays / D And E•Dee Gee•0','\
Cal Tjader Quintet•Yesterdays / Bei Mir Bist Du Schoen•Fantasy•1954','\
Jo Stafford•September Song / Yesterdays•Capitol Records•1950','\
Helen Merrill•Yesterdays / Falling In Love With Love•Mercury•0'),'\
\
You And The Night And The Music\
':('\
Nelson Riddle And His Orchestra•Hey... Let Yourself Go! (Part 1)•Capitol Records•0','\
Stan Getz•Live In Belgium 1974•Novadisc•0','\
Kasper Villaume Quartet•Outrun•Stunt Records•0','\
Phil Broadhurst•Live At The London Bar•Ode Records•1993','\
Judy Bailey•You & The Night & The Music•CBS•1964','\
Shelly Manne & His Men•Shelly Manne And His Men•Contemporary Records•1953','\
Art Blakey & The Jazz Messengers•Live At Kimball\'s•Concord Jazz•1986','\
Janusz Muniak•You Know These Songs?•GOWI Records•1994','\
Omri Mor•It\'s about time•Naïve•2018','\
Francesco Cafiso•Portrait In Black And White•Venus Records (5)•2008','\
Vic Lewis West Coast All-Stars•Me & You!•Candid•1997','\
Manhattan Jazz Quintet•Caravan•Paddle Wheel•1989','\
Jon Ballantyne Trio•Skydance•Justin Time Records Inc.•1989','\
Joe Haider Trio•Grandfather\'s Garden•Sound Hills Records•2003','\
Cms Trío•Andando •Contrabaix•2009','\
Woody Shaw Quintet•Time Is Right - Live In Europe•Red Record•1983','\
Nueva Manteca•Bluesongo•Lucho•1992','\
John Abercrombie•Tactics•ECM Records•1997','\
Kenny Burrell•Handcrafted•Muse Records•1978','\
The Marty Paich Quartet•Marty Paich Quartet•Tampa Records•1956','\
The Marty Paich Quartet•Marty Paich Quartet•Tampa Records•1957','\
Vladimir Shafranov Trio•Whisper Not•Venus Records (5)•2012','\
Grant Green•Remembering•Blue Note•1980','\
Herman Sandy•Jazz For Moderns•Fiesta Records (2)•1956','\
Jeff "Tain" Watts•Megawatts•Sunnyside•1991'),'\
\
You Are So Beautiful\
':('\
Bob James•Night Crawler / You Are So Beautiful•Tappan Zee Records•1977','\
Urbie Green•Señor  Blues•CTI Records•1977','\
Bob James•Heads•Tappan Zee Records•1977','\
Glenn Ferris "Pentessence" Quintet•X Actimo !•Naïve•2006','\
Morgana King•Everything Must Change•Muse Records•1979','\
Boney James•Ride•Warner Bros. Records•2001','\
Various•Nubian Blue•Blue Note•2005','\
Nino Tempo•Tenor Saxophone•Atlantic•1990'),'\
\
You are the Sunshine of My Life\
':('\
Elephant9•Silver Mountain•Rune Grammofon•2015','\
Lou Donaldson•The Long Goodbye / You Are The Sunshine Of My Life•Blue Note•0','\
Morgana King•Song For You / You Are The Sunshine Of My LIfe•Paramount Records•1973','\
Sandy Nelson•Dance With The Devil•United Artists Records•1974','\
Gene Russell•Me And Mrs. Jones / You Are The Sunshine Of My Life•Black Jazz Records•1973','\
Willis Jackson•Single Action•Muse Records•1980','\
Barney Kessel•Solo•Concord Records•1983','\
Peter Yellin•It\'s The Right Thing•Mainstream Records•1973','\
Grover Washington Jr.•Plays The Hits•Verve Records•2010','\
Marlena Shaw•Live At Montreux•Blue Note•1974','\
Carmen McRae•Ms. Jazz•Quintessence Jazz Series•1978','\
Manuel And His Music Of The Mountains•Shangri-La•EMI•1973','\
Tyrone Washington•Roots•Perception Records (5)•1973','\
Cedar Walton•Firm Roots•Muse Records•1976','\
Gerald Wiggins•Wig Is Here•Black And Blue•1974','\
Leon Thomas•Full Circle•Flying Dutchman•1973','\
Bobbi Humphrey•Satin Doll•Blue Note•1974','\
Steve Turre•Fire And Ice•Stash Records•1988','\
Grover Washington Jr.•Soul Box Vol. 2•Kudu•1973','\
Rhoda Scott•Live At The Club Saint-Germain•Barclay•1974'),'\
\
You Are There\
':('\
Varetta Dillard•Them There Eyes / You Are Gone•Savoy Records•1952','\
Mike Sammes Singers•Because You Are There•Columbia•1968','\
Burt Bacharach•Are You There (With Another Girl)•A&M Records•1967','\
Acker Bilk•When You Are There / La Playa•Atco Records•1966','\
Tommy Dorsey And His Orchestra•Tommy Dorsey Originals•RCA Victor•1961','\
Hank Mobley•Monday Night At Birdland•Roulette•1959','\
Paul Robertson (14)•The Song Is You•Palo Alto Jazz Records•1980','\
Earl Hines•I Giganti Del Jazz Vol. 95•Curcio•0','\
Earl Hines•Hines\' 74•Black And Blue•1974','\
Rita Reys•There Is No Greater•Philips•0','\
The Bruce Forman Quartet•There Are Times•Concord Jazz•1987','\
Mike Melvoin•Keys To Your Mind•Liberty•1966','\
Chet Baker•Out Of Nowhere•Milestone (4)•1991','\
Doc Severinsen•Doc Severinsen And Xebron•Passport Jazz•1985'),'\
\
You Are Too Beautiful\
':('\
Frank Sinatra•Day By Day / You Are Too Beautiful•Columbia•1946','\
The George Shearing Quintet•Good To The Last Bop / You Are Too Beautiful•MGM Records•0','\
Victor Feldman•In London Vol. 1 The Quartet•Tempo Records (5)•1957','\
Sonny Rollins•Tenor Titan•VSP•1966','\
Eddie "Lockjaw" Davis Big Band•Trane Whistle•Prestige•1961','\
Dollar Brand + 3•Dollar Brand + 3•Soultown (2)•1973','\
Ben Webster•Rare Live Performance 1962•Musidisc•1975','\
Eddie Graham Trio•S\'Wonderful Jazz•Wilson Audiophile•1984','\
Paul Robertson (14)•The Song Is You•Palo Alto Jazz Records•1980','\
Thelonious Monk•The Unique Thelonious Monk•Riverside Records•1956','\
Victor Feldman•In London Vol. 1 The Quartet•Jasmine Records•2001','\
Hank Jones Trio•Arigato•Progressive Records (2)•1977','\
Elvin Jones•Elvin!•Riverside Records•1962','\
Red Mitchell•Scairport Blues•Yupiteru Records•1978','\
John Coltrane•John Coltrane And Johnny Hartman•Impulse!•1963','\
James Williams (2)•Magical Trio 2•EmArcy•1988'),'\
\
You Better Leave It Alone\
':('\
Clifford Jordan Quartet•Bearcat•JAZZLAND•1962','\
Various•Kansas City Blues 1944-49•Capitol Records•1996','\
Nina Simone•Seven Classic Albums Plus Bonus Tracks•Real Gone•2013','\
Ray Charles•Eighteen Classic Albums•Real Gone•2018','\
Nina Simone•MP3 Collection•Digital Records (6)•0'),'\
\
You Do Something To Me\
':('\
Benny Goodman And His Orchestra•Mission To Moscow•Chess•1959','\
Lena Horne•It\'s Love•RCA•1955','\
Erroll Garner•You Do Something To Me•Philips•1961','\
Frank Sinatra•Bye Baby!•Fontana•1958','\
Erroll Garner•Closeup In Swing - Vol. 1•Philips•1961','\
Ray Anthony•Ray Anthony Plays For Dancers In Love Part 1•Capitol Records•0','\
Ray Conniff And His Orchestra & Chorus•\'S Awful Nice•Philips•1960','\
Hidehiko Matsumoto•Four Wings•Trio Records•1980','\
Ella Fitzgerald•Sings The Cole Porter Song Book 1•Verve Records•1957','\
Sammy Davis Jr.•Just For Lovers Part 1•Decca•1955','\
Frank Sinatra•Sinatra\'s Swingin\' Session Part 3•Capitol Records•1961','\
Adam Makowicz•The Name Is Makowicz (Ma-kó-vitch)•Sheffield Lab•1983','\
Larry Goldings•Awareness•Warner Bros. Records•1997','\
Sonny Rollins•The Bridge•RCA Victor•1962','\
Shirley Scott•Like Cozy•Moodsville•1961'),'\
\
You Don\'t Know What Love Is\
':('\
The Miles Davis Quintet•Miles Davis Quintet•Prestige•1954','\
Roland Keijser•Back Home Blues•SITTEL•1997','\
Gary Thomas•Till We Have Faces•JMT•1992','\
Kathryn Williams•Resonator•One Little Indian•2016','\
Various•Best Audiophile Voices IV•Premium Records (2)•2012','\
Various•Concord Jazz Guitar Collection - Volumes 1 And 2•Concord Jazz•1987','\
Shirley Bassey•O Talento de Shirley Bassey•EMI•1988','\
Magni Wentzel•My Wonderful One•Gemini Records (7)•1988'),'\
\
You Fascinate Me So\
':('\
Cy Coleman•Playboy\'s Theme•Playboy Records•1964','\
Blossom Dearie•My Gentleman Friend•Verve Records•1959','\
Ann Burton•It Might As Well Be Love•Turning Point Records•1984','\
Nelson Riddle And His Orchestra•Witchcraft!•Pickwick/33 Records•1965','\
Mark Murphy•Midnight Mood•SABA•1968','\
Cy Coleman•Piano Witchcraft•Capitol Records•1963','\
Peggy Lee•Pretty Eyes•Capitol Records•1960','\
Cy Coleman•Cool Coleman•Westminster•1958','\
Mabel Mercer•Merely Marvelous•Atlantic•1960','\
Blossom Dearie•Songs Of Chelsea•Daffodil Records (2)•1987','\
Morgana King•Wild Is Love•Reprise Records•1966'),'\
\
You Go To My Head\
':('\
Cassandra Wilson•You Go To My Head / The Mood That I\'m In•Legacy•2015','\
The John Young Trio•You Go To My Head / Memories Of You•Chance Records (3)•1953','\
Ted Heath And His Music•Dark Eyes / You Go To My Head•Decca•0','\
Max Roach•Best Coast Jazz•Mercury•1956','\
The Bud Powell Trio•You Go To My Head / Ornithology•Blue Note•1949','\
Buddy DeFranco•The Artistry Of Buddy DeFranco•Norgran Records•0','\
Teddy Wilson And His Orchestra•You Go To My Head / I\'ll Dream Tonight•Brunswick•1938','\
Art Pepper•Saturday Night At The Village Vanguard•Contemporary Records•1979','\
Billie Holiday And Her Orchestra•Blue Moon / You Go To My Head•Mercury•1952','\
Zoot Sims•You Go To My Head / The Scene Is Clean•Prestige•1950'),'\
\
You Make Me Feel Brand New\
':('\
Everette Harp•Strutt•Blue Note Contemporary•1994','\
Ron English•Fish Feet•P-Vine Records•2009','\
Richard Elliot•Ricochet•GRP•2003','\
Ernest Ranglin•Ranglypso•MPS Records•1976','\
Hubert Laws•The Chicago Theme•CTI Records•1975','\
The Lyman Woodard Organization•Live At J.J.\'s Lounge 1974•Uuquipleu Records•2008','\
Norman Brown•Celebration•Warner Bros. Records•1999','\
Asako Toki•Standards Gift•LD&K•2005','\
Jerald Daemyon•Thinking About You•GRP•1995','\
Dolf De Vries Trio•Where\'s That Rainy Day•Limetree Records•1986','\
Sonia Rosa•Spiced With Brazil•CBS/Sony•1974','\
Yoshiko Kishino•Fairy Tale•GRP•1996','\
Phil Perry (2)•Classic Love Songs•Shanachie•2006','\
"Stix" Hooper•Lay It On The Line•Artful Balance•1989'),'\
\
You Make Me Feel So Young\
':('\
Rosemary Clooney•You Make Me Feel So Young•Philips•0','\
Ella Fitzgerald•But Not For Me / You Make Me Feel So Young•Verve Records•1959','\
Frank Sinatra•Summer Wind / You Make Me Feel So Young•Reprise Records•1966','\
Frank Sinatra•Songs For Swingin\' Lovers (Part 1)•Capitol Records•1956','\
Sonny Phillips•My Black Flower•Muse Records•1977','\
Chris Connor•Chris Connor•Atlantic•1956','\
Frank Sinatra•Frank Sinatra\'s Greatest Hits•Reprise Records•1966','\
The Oscar Peterson Trio•A Jazz Portrait Of Frank Sinatra•Verve Records•1966','\
Jazz Renaissance Quintet•Movin\' Easy•Mercury•1961','\
The Claude Williamson Trio•The Fabulous Claude Williamson Trio•Contract Records•1961','\
Frank Sinatra•Sinatra At The Sands•Reprise Records•1966','\
Perry Como•For The Young At Heart•RCA Victor•1961','\
Ella Fitzgerald•Get Happy!•Verve Records•0'),'\
\
You Must Believe In Spring\
':('\
Marlena Shaw•Somewhere / You Must Believe In Spring•Blue Note•1972','\
Dave McKenna•You Must Believe in Swing•Concord Jazz•1997','\
Kenny Werner•The Space•Pirouet•2018','\
Hakuei Kim•Trisonique•area azzurra•2011','\
Nicki Parrott•Sakura Sakura•Venus Records (5)•2012','\
Michel Legrand•Recorded Live At Jimmy\'s•RCA•1975','\
Stefan Nilsson (3)•Music For Music Lovers•Sonet•1983','\
Michel Legrand•Legrand "Live" Jazz•Novus•1991','\
Karin Krog•You Must Believe In Spring (Songs By Michel Legrand)•Polydor•1974','\
Richard Galliano•French Touch•Dreyfus Jazz•1998','\
Alan Pasqua•My New Old Friend•Cryptogramophone•2005'),'\
\
You Say You Care\
':('\
The John Coltrane Quartet•You Say You Care / Russian Lullaby•Barclay•1959','\
Sarah Vaughan•You Say You Care•Columbia•1949','\
John Coltrane•Soultrane•Prestige•1958'),'\
\
You Stepped Out Of A Dream\
':('\
Pete Rugolo Orchestra• California Melodies / You Stepped Out Of A Dream•Philips•0','\
The Dave Brubeck Trio•You Stepped Out Of A Dream / Lullaby In Rhythm•Fantasy•1950','\
Clyde Otis•High On A Cloud•Liberty•1961','\
Tommy Whittle Quintet•A Touch Of Latin•Saga (5)•1958','\
Mantovani And His Orchestra•You Stepped Out Of A Dream / Lonely Ballerina•London Records•1954','\
Don Friedman Quartet•Dreams And Explorations•Riverside Records•1965','\
Cedar Walton•The Electric Boogaloo Song•Prestige•1969','\
Teddy Edwards•Together Again!•Contemporary Records•1961','\
The Oscar Peterson Trio•The Oscar Peterson Trio Plays•Verve Records•1964','\
Attila Zoller•デュオローグ Duologue•Express•1971','\
Sonny Rollins•Volume 2•Blue Note•1957'),'\
\
You Taught My Heart To Sing\
':('\
Janusz Muniak Quartet•Crazy Girl•PolJazz•1986','\
McCoy Tyner Big Band•Journey•Verve Records•1993','\
McCoy Tyner•It\'s About Time•Blue Note•1986','\
McCoy Tyner•Live At The Musicians Exchange Cafe•no label•1988','\
McCoy Tyner•It\'s About Time•Blue Note•1985','\
McCoy Tyner•The Best Of McCoy Tyner•Blue Note•1996','\
Various•Ballads In Blue (Big Sounds For The Small Hours)•Blue Note•1991','\
Cheryl Bentyne•The Book Of Love•Telarc•2006','\
McCoy Tyner•Warsaw Concert 1991•Fresh Sound Records•1992','\
Various•Blue Piano Volume Two•Blue Note•1992','\
Dianne Reeves•The Best Of Dianne Reeves•Blue Note•2002','\
Kirsten Gustafson•You Taught My Heart To Sing•Atlantic Jazz•1992'),'\
\
You Took Advantage Of Me\
':('\
June Christy•You Took Advantage Of Me / Intrigue•Capitol Records•1956','\
no artist•I Apologize / You Took Advantage Of Me •London Records•1951','\
Bunny Berigan And His Blue Boys•You Took Advantage Of Me / Chicken And Waffles •Parlophone•0','\
Tommy Dorsey•Just A Simple Melody / You Took Advantage Of Me•RCA Victor•1953','\
Chuck Hedges•Clarinet Climax•Jazzology•1983','\
Erskine Butterfield•Just For Kicks•Livingston Electronic Corporation•1955','\
Bob Brookmeyer•Bob Brookmeyer Plays Bob Brookmeyer And Some Others•Clef Records•1955','\
Tatum - Eldridge - Stoller - Simmons Quartet•The Moon Is Low•Clef Records•0','\
Tatum - Eldridge - Stoller - Simmons Quartet•The Moon Is Low•Clef Records•0','\
Mel Lewis Sextet•Mel Lewis Sextet•Mode Records•1957','\
Wolfgang Lackerschmid•Live Conversation•in-akustik•0','\
Ann Gilbert•Makin\' Whoopee•Vik•1957','\
Bobby Jaspar•New Jazz Vol. 2•Swing (3)•1955'),'\
\
You\'d Be So Nice To Come Home To Home To\
':('\
Cecil Taylor Trio•Jazz Advance•Fresh Sound Records•2008','\
Hall Overton•Jazz Laboratory Series Vol. 2•Signal (3)•1955','\
Dick Jurgens And His Orchestra•You’d Be So Nice To Come Home To / I’m So So So So So In Love•Columbia•1943','\
Manhattan Jazz Quintet•My Favorite Things - Live In Tokyo •Paddle Wheel•1987','\
Fred Nardin Trio•Opening•Jazz Family•2017','\
Dudley Moore•At The Wavendon Festival•Black Lion Records•1976','\
Chet Baker•Love Song•Baystate•1987','\
Nina Simone•Nina At Newport•Colpix Records•1960','\
Al Cohn - Zoot Sims Quintet•You \'N Me•Mercury•1960','\
Sheila Jordan•The Crossing•BlackHawk Records•1986','\
The Eddie Higgins Trio•The Ed Higgins Trio•Replica Records (3)•1957','\
Fred Waring & The Pennsylvanians•Fred Waring Music-Cole Porter Songs•Decca•1949','\
The Douglas Randle Orchestra & Chorus•Doug Crosley & Elan Stuart Vocalists •CBC Radio Canada•0'),'\
\
You\'ll Never Know\
':('\
Georgie Auld•Sax In Satin•Coral•1968','\
Lillian Roth•Lillian Roth Sings•Tops Records•1957','\
The Eddie Higgins Trio•Ballad Higgins•Venus Records (5)•2005','\
Various•In The Mood / Greatest Hits Of The Big Band Era•RCA Special Products•1988','\
Nina Simone•Mood Indigo: The Complete Bethlehem Singles•Bethlehem Records•2018','\
Shirley Bassey•O Talento de Shirley Bassey•EMI•1988','\
Benny Goodman•Small Group Recordings•Intense Rarities•2001','\
Miles Davis•Just Squeeze Me•Documents•2006','\
George Duke•George Duke Часть 1-2•Домашняя Коллекция•0'),'\
\
Young Rabbits\
':('\
The Crusaders•The Festival Album•Pacific Jazz•1967','\
The Crusaders•The Best Of...•Pacific Jazz•1993','\
The Crusaders•Lookin\' Ahead•Fontana•1962','\
The Crusaders•The Best Of The Jazz Crusaders•World Pacific Jazz•1970','\
The Crusaders•The Young Rabbits•Blue Note•1975','\
The Crusaders•At Their Best•Motown•1973','\
The Crusaders•Freedom Sound / Lookin\' Ahead •Vinyl Passion•2015','\
The Crusaders•Happy Again•Sin-Drome Records•1995','\
The Crusaders•Pass The Plate•Chisa Records•1971','\
Gilles Peterson•The Kings Of Jazz•Rapster Records•2006','\
The Crusaders•The Golden Years•GRP•1992','\
The Crusaders•Gold•Hip-O Records•2007'),'\
\
Your Is My Heart Alone\
':('\
Dan Nimmer Trio•Yours Is My Heart Alone•Venus Records (5)•2008','\
Guy Lombardo And His Royal Canadians•Snuggled On Your Shoulder•Decca•1962','\
Jack Hylton And His Orchestra•England\'s Favorite Of The 1930s•Capitol Records•0','\
Dave McKenna•The Key Man •Concord Jazz•1985','\
The George Shearing Quintet•Latin Rendezvous•Capitol Records•1963','\
The Three Sounds•Groovin\' Hard (Live At The Penthouse 1964-1968)•Resonance Records•2016','\
Oscar Peterson•The Jazz Soul Of Oscar Peterson / Affinity•Verve Records•1996','\
Charlie Mariano•Deep In A Dream•Enja Records•2002','\
George Shearing•The Many Facets Of George Shearing•MPS Records•1978','\
Benny Goodman•Best Of Big Bands•Columbia•1992','\
Vincent Lopez And His Orchestra•Nola And Other Piano Instrumentals•Carlton•1959','\
Mel Davis•Trumpet With a Soul•Epic•1956','\
Ken Griffin (2)•Love Letters In The Sand•Columbia•1957','\
Ken Griffin (2)•Love Letters In The Sand•Columbia•1957','\
Various•The 80\'s Collection 1988•Time Life Music•1994','\
Connie Francis•Mala Femmena (Evil Woman) & Connie\'s Big Hits From Italy•MGM Records•1963'),'\
\
Your Mind Is On Vacation\
':('\
Mose Allison•Your Mind Is On Vacation •Atlantic•1962','\
Mose Allison•Lessons In Living•Elektra Musician•1983','\
Paulinho Da Costa•Happy People•Pablo Today•1979','\
New Guitar Summit•Shivers•Stony Plain Records•2008','\
Various•Atlantic Jazz Legends: Vol. 1•Rhino Records (2)•1993','\
Mose Allison•Mose Allison•Atlantic•1976','\
Marlena Shaw•Elemental Soul•Concord Jazz•1997','\
Mose Allison•I Don\'t Worry About A Thing•Atlantic•1962','\
Mose Allison•Pure Mose•Village•1994','\
Mose Allison•The Best Of Mose Allison•Atlantic•0','\
Vassar Clements•Hillbilly Jazz Rides Again•Flying Fish (2)•1986','\
Mose Allison•Your Mind Is On Vacation•Atlantic•1976'),'\
\
You\'re Everything\
':('\
Various•Blue Bossa•Blue Note•1986','\
Roy Hargrove Quintet•Of Kindred Souls•Novus•1993','\
Kenny Ball•A Friend To You•Pye Records•1974','\
Chick Corea Akoustic Band•Live•Stretch Records•2018','\
Chick Corea Trio•Trilogy•Stretch Records•2013','\
Jamie Cullum•Momentum•Island Records•2013','\
Georgie Fame•A Portrait Of Chet•Four Leaf Clover Records•1989','\
Ella Fitzgerald•Portrait Of Ella Fitzgerald•Capitol Records•1974','\
Buddy Johnson And His Orchestra•Walkin\'•Mercury•1957','\
Gary Lawrence And His Sizzling Syncopators•Gary Lawrence And His Sizzling Syncopators•Blue Goose Records•1976','\
Various•The Wire Tapper 13•Wire Magazine•2005','\
Sacha Rubin•No Balaio•London Records•1967','\
Various•Chillenundgrillen / Zwei•Universal Marketing Group GmbH•2003'),'\
\
You\'re My Everything\
':('\
Roy Hargrove Quintet•Of Kindred Souls•Novus•1993','\
Chick Corea Trio•Trilogy•Stretch Records•2013','\
Kenny Ball•A Friend To You•Pye Records•1974','\
Ella Fitzgerald•Portrait Of Ella Fitzgerald•Capitol Records•1974','\
Buddy Johnson And His Orchestra•Walkin\'•Mercury•1957','\
Gary Lawrence And His Sizzling Syncopators•Gary Lawrence And His Sizzling Syncopators•Blue Goose Records•1976','\
Sacha Rubin•No Balaio•London Records•1967','\
Bill Evans•The Complete Riverside Recordings•Riverside Records•1984','\
Miles Davis•Just Squeeze Me•Documents•2006','\
Bill Evans•Riverside Recordings•Analogue Productions•2010','\
Bill Evans•The Complete Bill Evans On Verve•Verve Records•1997'),'\
\
You\'re The Top\
':('\
Duke Robillard•After Hours Swing Session•Rounder Records•1992','\
Lionel Hampton•Lionel Hampton•Brunswick•1953','\
Fats Waller•Vol. 4 •RCA Victor•1965','\
Stacey Kent•The Boy Next Door•Candid•2003','\
Various•The Legendary Big Band Singers•MCA Records•1994','\
Lionel Hampton•Hamp:  The Legendary Decca Recordings•Decca Jazz•2002','\
Lester Lanin And His Orchestra•For Dancing: 23 Richard Rodgers Hits •Epic•1967','\
Lionel Hampton•Classic Jazz Archive - Lionel Hampton•Documents•2004','\
Miles Davis•Just Squeeze Me•Documents•2006','\
Lionel Hampton•The Lionel Hampton Story•Proper Records (2)•2000','\
Django Reinhardt• Djangologie Volume 1-20•EMI•1981'),'\
\
You\'ve Changed\
':('\
The Don Weller Spring Quartet•Commit No Nuisance•Affinity•1979','\
Miriam Klein•Lady Like (Miriam Klein Sings Billie Holiday)•MPS Records•1973','\
Chet Baker•The Best Thing For You•A&M Records•1989','\
Benjamin Herman•Cafe Solo•Dox Records•2013','\
Irv Williams•Keep The Music Playing•Ding Dong Music•1994','\
The Herman Foster Trio•Ready And Willing•Argo (6)•1964','\
Laila Dalseth•Time For Love•Gemini Records (7)•1986','\
Spider Burks•Direct From The Blue Note Club•L. G. Records•1960','\
Various•In The Wee Small Hours•Columbia House•1974','\
Various•Fifty Years Of Radio: A Celebration Of CBC Radio 1936-1986•CBC Enterprises•1986')\
}

class versions_search:

	def init_versionsDB(self):
		versions_search.DB = []
		versions_search.DB = versions_dict
		return versions_search.DB



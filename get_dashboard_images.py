import os
import requests

# List of company URLs
company_images = {
    "AMD (Advanced Micro Devices, Inc.)": "https://www.amd.com",
    "Nvidia": "https://www.nvidia.com",
    "ACS Powersports": "https://www.acspowersports.ca",
    "AES Engineering": "https://www.aesengr.com",
    "Acciona Infrastructure Canada Inc.": "https://www.acciona.ca",
    "Air Canada": "https://www.aircanada.com",
    "Alberici Constructors": "https://www.alberici.com",
    "AlphaWave SEMI": "https://www.awavesemi.com",
    "AltaLink LP": "https://www.altalink.ca",
    "Altera, An Intel Company": "https://www.intel.com",
    "Analog Devices Inc.": "https://www.analog.com",
    "Arcadis IBI Group": "https://www.ibigroup.com",
    "Arla Foods Inc.": "https://www.arlafoods.ca",
    "Aviva Canada Inc": "https://www.aviva.ca",
    "BA Consulting Group Ltd.": "https://www.bagroup.com",
    "Bank of America Merrill Lynch": "https://www.ml.com",
    "Baylis Medical Technologies": "https://www.baylismedtech.com",
    "Bibliocommons Inc.": "https://www.bibliocommons.com",
    "Birch Hill Equity Partners": "https://www.birchhillequity.com",
    "Brigham & Women's Hospital, Harvard Medical School": "https://www.brighamandwomens.org",
    "Briza": "https://www.briza.com",
    "Cadence Design Systems Inc": "https://www.cadence.com",
    "Cadillac Fairview": "https://www.cadillacfairview.com",
    "Canadensys Aerospace": "https://www.canadensys.com",
    "Canadian Natural Resources Limited": "https://www.cnrl.com",
    "Castleton Commodities International": "https://www.cci.com/",
    "Cenovus Energy, Inc.": "https://www.cenovus.com/",
    "CentML Inc": "https://www.centml.ai/",
    "Cerebras Systems": "https://www.cerebras.ai/",
    "Change Connect Inc.": "https://www.changeconnect.ca/",
    "DHL Supply Chain": "https://www.dhl.com",
    "Defence R&D Canada (DRDC) - Ottawa": "https://www.canada.ca",
    "E11 Bio": "https://www.e11.bio/",
    "Ecobee": "https://www.ecobee.com",
    "Edgewood Health Network Inc": "https://www.edgewoodhealthnetwork.com/",
    "Elevate Construction Management": "https://www.elevatecm.com/",
    "Enerlife Consulting Inc.": "https://www.enerlife.com/",
    "Environment and Climate Change Canada": "https://www.canada.ca",
    "Epson": "https://www.epson.ca",
    "Evertz Microsystems Ltd": "https://www.evertz.com",
    "Geomechanica Inc.": "https://www.geomechanica.com/",
    "Geotab": "https://www.geotab.com/",
    "Groq Inc.": "https://www.groq.com/",
    "HDR Corporation": "https://www.hdrinc.com",
    "HF Sinclair": "https://www.hfsinclair.com",
    "HOOPP Healthcare of Ontario Pension Plan": "https://www.hoopp.com/",
    "HTS Engineering": "https://www.hts.com/",
    "Harmonic Fund Services": "https://www.harmonicfundservices.com/",
    "Honda Canada Inc.": "https://www.honda.ca",
    "Huawei Technologies Canada Co. Ltd.": "https://www.huawei.com",
    "Husky Injection Molding Systems Ltd.": "https://www.husky.co/",
    "Hydro One Limited": "https://www.hydroone.com/",
    "Intact Financial Corporation": "https://www.intact.ca/",
    "Invictus Analytics and Strategy Inc.": "https://www.invictusas.com/",
    "JMA Consulting": "https://www.jmaconsulting.biz",
    "Kijiji": "https://www.kijiji.ca",
    "Kinaxis": "https://www.kinaxis.com",
    "Kinectrics Inc.": "https://www.kinectrics.com/",
    "Kortex Enterprises LLC": "https://www.kortex.co/",
    "Labworks International Inc.": "https://www.labworksinternational.com/",
    "Ledcor": "https://www.ledcor.com",
    "Left Turn Right Turn (LTRT)": "https://www.ltrt.ca",
    "MHI RJ Aviation Group": "https://www.mhirj.com/",
    "Marvell Technology Group (US)": "https://www.marvell.com",
    "Massachusetts Institute of Technology (MIT)": "https://www.mit.edu",
    "Mattamy Homes Limited": "https://www.mattamyhomes.com/",
    "MedMe Health": "https://www.medmehealth.com/",
    "Memme Infrastructure Contractors": "https://www.memme.com/",
    "Metrolinx": "https://www.metrolinx.com",
    "Microchip Technology Inc.": "https://www.microchip.com/",
    "Monday Girl": "https://www.joinmondaygirl.com/",
    "Moody's Analytics": "https://www.moodys.com/",
    "Movellus": "https://www.movellus.com/",
    "Nest Wealth Solutions Inc.": "https://www.nestwealth.com/",
    "New School Foods Inc.": "https://www.newschoolfoods.co/",
    "OMERS": "https://www.omers.com/",
    "Ontario Ministry of Transportation": "https://www.ontario.ca",
    "Ontario Teachers Pension Plan": "https://www.otpp.com",
    "Pason Systems Corp.": "https://www.pason.com/",
    "Periscope Capital Inc": "https://www.periscopecap.com/",
    "Picovoice": "https://www.picovoice.ai/",
    "PolicyMe": "https://www.policyme.com",
    "Pomerleau, Inc": "https://www.pomerleau.ca",
    "Posterity Group": "https://www.posteritygroup.ca/",
    "Power Advisory": "https://www.poweradvisoryllc.com/",
    "Procter & Gamble Inc.": "https://www.pg.com",
    "Purpose Building Inc.": "https://www.purposebuilding.ca/",
    "Quanta Technology": "https://www.quanta-technology.com/",
    "Quantim Intelligence": "https://www.qic.ai/",
    "Read Jones Christoffersen (RJC Engineers)": "https://www.rjc.ca/",
    "Regional Municipality of York": "york.ca",
    "RocMar Engineering Inc.": "https://rocmar.ca/",
    "Royal Bank of Canada (RBC)": "https://www.rbcroyalbank.com/",
    "Royal Canadian Mounted Police": "https://www.rcmp-grc.gc.ca/",
    "SAFRAN Landing Systems (Messier-Dowty Inc.)": "https://www.safran-group.com",
    "Safety Power Inc": "https://www.safetypower.ca/",
    "Scotiabank": "https://www.scotiabank.com",
    "Select Equity Group, L.P.": "https://www.selectequity.com/",
    "Semtech": "https://www.semtech.com/",
    "Smith + Andersen": "https://smithandandersen.com/",
    "Snowflake, Inc.": "https://www.snowflake.com",
    "StoneX Group Inc.": "https://www.stonex.com/en/",
    "Structura Biotechnology Inc.": "https://structura.bio/",
    "Sun Life Financial": "https://www.sunlife.ca",
    "Synopsys, Inc.": "https://www.synopsys.com/",
    "TC Energy Corp.": "https://www.tcenergy.com/",
    "TD Securities": "https://www.tdsecurities.com/",
    "Taalas Inc.": "https://taalas.com/",
    "Technical University of Munich (TUM)": "https://www.tum.de/",
    "Tenstorrent Inc": "https://tenstorrent.com/",
    "Tesla": "https://www.tesla.com/",
    "Tetra Trust": "https://tetratrust.com/",
    "The Independent Electricity System Operator (IESO)": "https://www.ieso.ca/",
    "The Mosaic Company": "https://mosaicco.com/",
    "The Six Semiconductor": "https://www.thesixsemi.com/",
    "Town of Oakville": "https://www.oakville.ca/",
    "Uken Games": "https://uken.com/",
    "University Health Network": "https://www.uhn.ca/",
    "University of Toronto - Facilities & Services": "https://www.fs.utoronto.ca/",
    "Untether AI": "https://www.untether.ai/",
    "Vale Canada": "https://www.vale.com",
    "Veeva Systems": "https://www.veeva.com/",
    "Vena Solutions": "https://www.venasolutions.com/",
    "Xpan Inc.": "https://xpanmedical.com/",
    "YuJa Canada Inc.": "https://www.yuja.com/",
    "ZS Associates": "https://www.zs.com/",
    "Zynga Inc.": "https://www.zynga.com/",
    "ePIC Blockchain Technologies": "https://www.epicblockchain.io/",
    "t0.technology": "https://www.t0.technology/"
  }

# Directory to save images
output_dir = "assets/img/data/uoft-pey-coop-job-2024/"

# Create directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Function to download and save image
def download_image(company_name, company_url):
    # Construct the image URL
    image_url = f"https://logo.clearbit.com/{company_url.replace('https://', '').replace('www.', '')}"

    # Get the image content
    response = requests.get(image_url)

    if response.status_code == 200:
        # Save the image
        image_path = os.path.join(output_dir, f"{company_name.replace(' ', '_').replace(',', '').replace('.', '').replace('(', '').replace(')', '').replace('&', 'and')}.png")
        with open(image_path, 'wb') as file:
            file.write(response.content)
        print(f"Saved {company_name} logo to {image_path}")
    else:
        print(f"Failed to download image for {company_name} from {image_url}")

# Download images for all companies
for company_name, company_url in company_images.items():
    download_image(company_name, company_url)
# %%
import torch


label2num = {'1161364': 0, '116570': 1, '1176823': 2, '1595929': 3, '209233': 4, '22930': 5, '22956': 6, '22961': 7, '22967': 8, '22973': 9, '22983': 10, '22985': 11, '23150': 12, '23154': 13, '23158': 14, '23176': 15, '23724': 16, '24279': 17, '24285': 18, '24287': 19, '24321': 20, '244024': 21, '25092': 22, '25214': 23, '326272': 24, '41970': 25, '43435': 26, '47144': 27, '476521': 28, '516975': 29, '555123': 30, '555145': 31, '555146': 32, '64898': 33, '65377': 34, '65380': 35, '66971': 36, '67107': 37, '67252': 38, '70711': 39, '738183': 40, '74113': 41, '74580': 42, '760266': 43, 'ashgre1': 44, 'astcra1': 45, 'bafcur1': 46, 'baffal1': 47, 'banana': 48, 'barant1': 49, 'batbel1': 50, 'baymac': 51, 'bbwduc': 52, 'bcwfin2': 53, 'bkcdon': 54, 'bkhpar': 55, 'blchaw1': 56, 'blheag1': 57, 'blttit1': 58, 'bncfly': 59, 'bobfly1': 60, 'brcmar1': 61, 'brnowl': 62, 'bucmot4': 63, 'bucpar': 64, 'bufpar': 65, 'bunibi1': 66, 'burowl': 67, 'camfli1': 68, 'chacha1': 69, 'chbmoc1': 70, 'chobla1': 71, 'chvcon1': 72, 'cibspi1': 73, 'coffal1': 74, 'compau': 75, 'compot1': 76, 'crbthr1': 77, 'crebec1': 78, 'dwatin1': 79, 'epaori4': 80, 'eulfly1': 81, 'fabwre1': 82, 'fepowl': 83, 'ficman1': 84, 'flawar1': 85, 'fotfly': 86, 'fusfly1': 87, 'gilhum1': 88, 'giwrai1': 89, 'glteme1': 90, 'grasal3': 91, 'greani1': 92, 'greant1': 93, 'greela': 94, 'grekis': 95, 'grepot1': 96, 'gretho2': 97, 'greyel': 98, 'grfdov1': 99, 'grhtan1': 100, 'gycwor1': 101, 'horscr1': 102, 'houspa': 103, 'hyamac1': 104, 'larela1': 105, 'lesela1': 106, 'lesgrf1': 107, 'limpki': 108, 'linwoo1': 109, 'litcuc2': 110, 'litnig1': 111, 'mabpar': 112, 'magant1': 113, 'magtan2': 114, 'masgna1': 115, 'nacnig1': 116, 'ocecra1': 117, 'oliwoo1': 118, 'orbtro3': 119, 'orwpar': 120, 'osprey': 121, 'pabspi1': 122, 'palhor3': 123, 'paltan1': 124, 'phecuc1': 125, 'picpig2': 126, 'pirfly1': 127, 'plasla1': 128, 'platyr1': 129, 'plcjay1': 130, 'pluibi1': 131, 'purjay1': 132, 'pvttyr1': 133, 'ragmac1': 134, 'rebscy1': 135, 'recfin1': 136, 'redjun': 137, 'relser1': 138, 'rinkin1': 139, 'rivwar1': 140, 'roahaw': 141, 'rubthr1': 142, 'rufcac2': 143, 'rufcas2': 144, 'rufgna3': 145, 'rufhor2': 146, 'rufnig1': 147, 'ruftho1': 148, 'ruftof1': 149, 'rumfly1': 150, 'ruther1': 151, 'rutjac1': 152, 'sabspa1': 153, 'saffin': 154, 'saytan1': 155, 'scadov1': 156, 'schpar1': 157, 'scther1': 158, 'shcfly1': 159, 'shshaw': 160, 'shtnig1': 161, 'sibtan2': 162, 'smbani': 163, 'smbtin1': 164, 'sobcac1': 165, 'sobtyr1': 166, 'socfly1': 167, 'sofspi1': 168, 'souant1': 169, 'soulap1': 170, 'souscr1': 171, 'spbant3': 172, 'spispi1': 173, 'sptnig1': 174, 'squcuc1': 175, 'stbwoo2': 176, 'strcuc1': 177, 'strher2': 178, 'strowl1': 179, 'swthum1': 180, 'swtman1': 181, 'tattin1': 182, 'thlwre1': 183, 'toctou1': 184, 'trokin': 185, 'trsowl': 186, 'undtin1': 187, 'varant1': 188, 'watjac1': 189, 'wesfie1': 190, 'wfwduc1': 191, 'whbant2': 192, 'whbwar2': 193, 'whiwoo1': 194, 'whlspi1': 195, 'whnjay1': 196, 'whtdov': 197, 'whwpic1': 198, 'y00678': 199, 'yebcar': 200, 'yebela1': 201, 'yecmac': 202, 'yecpar': 203, 'yehcar1': 204, 'yeofly1': 205, '1491113': 206, '25073': 207, '47158son01': 208, '47158son02': 209, '47158son03': 210, '47158son04': 211, '47158son05': 212, '47158son06': 213, '47158son07': 214, '47158son08': 215, '47158son09': 216, '47158son10': 217, '47158son11': 218, '47158son12': 219, '47158son13': 220, '47158son14': 221, '47158son15': 222, '47158son16': 223, '47158son17': 224, '47158son18': 225, '47158son19': 226, '47158son20': 227, '47158son21': 228, '47158son22': 229, '47158son23': 230, '47158son24': 231, '47158son25': 232, '517063': 233}
label2num["nocall"] = 234
class_idx_mapping = {'Insecta': [0, 21, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 43], 'Reptilia': [1], 'Amphibia': [2, 206, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 207, 22, 23, 24, 28, 233, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], 'Mammalia': [4, 25, 26, 27, 29, 40, 41, 42], 'Aves': [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205]}

class Config:
    calculate_duration = True
    data_dir = "/home/salman/Documents/data/birdclef-2026/"

    seed = 3545
    
    sample_rate = 32_000
    train_duration = 20

    mixup_prob_dict = {}

    n_folds = 5
    fold = 0

    add_nocall = True
    overlap = False

    dataset_params = {
        "sample_rate" : sample_rate,
        "num_classes" : len(label2num.keys()),
        "bird2id" : label2num,
        "normalize_wave" : True,
        "sampling_type" : "random",
        "duration" : train_duration
    }

    #448 x 626
    melspec_parameters = {
        "n_mels" : 448,
        "n_fft" : 4096, 
        "hop_length" : 1001,
        "win_length" : 4096,
        "f_min" : 0,
        "f_max" : 16000,
        "sample_rate" : sample_rate,
        "normalized" : True,
        "aug" : {
            "apply" : True,
            "freq_mask_param" : 30, 
            "time_mask_param" : 20, 
            "num_masks" : 2
        }
    }

    model_parameters = {
        "n_mels" : melspec_parameters.get("n_mels"),
        "smoothings" : [1, 3], #1 means main input
        "backbone": "tf_efficientnet_b1_ns",
        "pretrained": True,
        "in_chans" : 3,
        "num_classes" : len(label2num),
        "drop_rate" : 0.4,
        "drop_path_rate" : 0.15,
        "forward_drop_rate" : 0.5,
        "attn_heads" : {
            "insecta" : len(class_idx_mapping['Insecta'])+1,
            "amph" : len(class_idx_mapping['Amphibia'])+2,
            "mam" : len(class_idx_mapping['Mammalia'])+2,
            "aves" : len(class_idx_mapping['Aves'])+1,
        }
    }
    
    training_params = {
    
        "debug": False,
        "amp" : True,

        "criterion" : torch.nn.CrossEntropyLoss(),
        "device" : "cuda",
        "accumulation_steps" : 1,
        "gradient_clip" : -9999,

        "batch_size" : 32,
        "num_workers" : 16,
        
        "n_epochs" : 50,
        "warmup_epochs": 4,
        
        "lr": 3.5e-4,
        "wd": 1e-4,
        "min_lr": 1e-6,
    }

    experiment_params = {
        "output_dir" : "outputs",
        "experiment_name" : "stage2_b1ns_v2",
        "fold" : 0,
        "save_epochs" : [24, 34, 44, 48]
    }


# %%
_FILE_MAP = {'stbwoo2/XC467895.ogg': 'stbwoo2-XC467895.mp3', '1161364/iNat1264238.ogg': '1161364-iNat1264238.mp3', '209233/iNat1545859.ogg': '209233-iNat1545859.m4a', '22956/iNat1693371.ogg': '22956-iNat1693371.m4a', '22973/iNat781822.ogg': '22973-iNat781822.m4a', '22973/iNat1353836.ogg': '22973-iNat1353836.mp3', '22973/iNat1460521.ogg': '22973-iNat1460521.mpga', '22973/iNat1645288.ogg': '22973-iNat1645288.mp3', '23158/iNat1322093.ogg': '23158-iNat1322093.m4a', '24279/iNat1306335.ogg': '24279-iNat1306335.m4a', '24279/iNat1435402.ogg': '24279-iNat1435402.mp3', '244024/iNat1219059.ogg': '244024-iNat1219059.m4a', '244024/iNat1583846.ogg': '244024-iNat1583846.m4a', '244024/iNat1573678.ogg': '244024-iNat1573678.m4a', '25092/iNat1645314.ogg': '25092-iNat1645314.m4a', '326272/iNat1299066.ogg': '326272-iNat1299066.m4a', '326272/iNat1303382.ogg': '326272-iNat1303382.m4a', '43435/iNat1054872.ogg': '43435-iNat1054872.mp3', '43435/iNat1243480.ogg': '43435-iNat1243480.mpga', '47144/iNat1717935.ogg': '47144-iNat1717935.m4a', '47144/iNat1346356.ogg': '47144-iNat1346356.m4a', '47144/iNat1346365.ogg': '47144-iNat1346365.m4a', '47144/iNat1317366.ogg': '47144-iNat1317366.m4a', '47144/iNat1559514.ogg': '47144-iNat1559514.m4a', '47144/iNat1191939.ogg': '47144-iNat1191939.mpga', '476521/iNat1648597.ogg': '476521-iNat1648597.m4a', '555146/iNat1375734.ogg': '555146-iNat1375734.m4a', '555146/iNat1375753.ogg': '555146-iNat1375753.m4a', '65377/iNat1372639.ogg': '65377-iNat1372639.m4a', '65377/iNat924044.ogg': '65377-iNat924044.mp3', '65377/iNat924035.ogg': '65377-iNat924035.mp3', '65377/iNat1676955.ogg': '65377-iNat1676955.m4a', '67107/iNat1635719.ogg': '67107-iNat1635719.m4a', 'ashgre1/iNat963674.ogg': 'ashgre1-iNat963674.m4a', 'ashgre1/iNat1400791.ogg': 'ashgre1-iNat1400791.m4a', 'baffal1/iNat1672327.ogg': 'baffal1-iNat1672327.m4a', 'baffal1/iNat1711622.ogg': 'baffal1-iNat1711622.m4a', 'banana/iNat1638891.ogg': 'banana-iNat1638891.m4a', 'banana/iNat1302882.ogg': 'banana-iNat1302882.m4a', 'banana/iNat1371833.ogg': 'banana-iNat1371833.m4a', 'banana/iNat335243.ogg': 'banana-iNat335243.m4a', 'banana/iNat1631602.ogg': 'banana-iNat1631602.m4a', 'banana/iNat1496209.ogg': 'banana-iNat1496209.m4a', 'banana/iNat1630115.ogg': 'banana-iNat1630115.m4a', 'barant1/iNat1654575.ogg': 'barant1-iNat1654575.m4a', 'barant1/iNat1418545.ogg': 'barant1-iNat1418545.m4a', 'barant1/iNat1738725.ogg': 'barant1-iNat1738725.m4a', 'barant1/iNat76423.ogg': 'barant1-iNat76423.mpga', 'batbel1/iNat851301.ogg': 'batbel1-iNat851301.mp3', 'batbel1/iNat851302.ogg': 'batbel1-iNat851302.mp3', 'batbel1/iNat851299.ogg': 'batbel1-iNat851299.mp3', 'batbel1/iNat1275000.ogg': 'batbel1-iNat1275000.m4a', 'batbel1/iNat1517987.ogg': 'batbel1-iNat1517987.m4a', 'batbel1/iNat1710152.ogg': 'batbel1-iNat1710152.m4a', 'baymac/iNat1304419.ogg': 'baymac-iNat1304419.m4a', 'baymac/iNat976078.ogg': 'baymac-iNat976078.m4a', 'bbwduc/iNat1318531.ogg': 'bbwduc-iNat1318531.m4a', 'bbwduc/iNat942901.ogg': 'bbwduc-iNat942901.m4a', 'bbwduc/iNat1294916.ogg': 'bbwduc-iNat1294916.m4a', 'bbwduc/iNat1338852.ogg': 'bbwduc-iNat1338852.m4a', 'bbwduc/iNat1499546.ogg': 'bbwduc-iNat1499546.m4a', 'bbwduc/iNat1352566.ogg': 'bbwduc-iNat1352566.m4a', 'bbwduc/iNat1543298.ogg': 'bbwduc-iNat1543298.m4a', 'bbwduc/iNat1683874.ogg': 'bbwduc-iNat1683874.m4a', 'bbwduc/iNat1580446.ogg': 'bbwduc-iNat1580446.m4a', 'bbwduc/iNat418728.ogg': 'bbwduc-iNat418728.m4a', 'bbwduc/iNat797291.ogg': 'bbwduc-iNat797291.m4a', 'bbwduc/iNat950353.ogg': 'bbwduc-iNat950353.m4a', 'bbwduc/iNat1333153.ogg': 'bbwduc-iNat1333153.m4a', 'bbwduc/iNat594163.ogg': 'bbwduc-iNat594163.m4a', 'bbwduc/iNat1520789.ogg': 'bbwduc-iNat1520789.m4a', 'bbwduc/iNat1705504.ogg': 'bbwduc-iNat1705504.m4a', 'bkcdon/iNat1637377.ogg': 'bkcdon-iNat1637377.m4a', 'bkcdon/iNat1396398.ogg': 'bkcdon-iNat1396398.m4a', 'bkhpar/iNat1637590.ogg': 'bkhpar-iNat1637590.m4a', 'bkhpar/iNat1029272.ogg': 'bkhpar-iNat1029272.m4a', 'blheag1/iNat1675853.ogg': 'blheag1-iNat1675853.mp3', 'blheag1/iNat953708.ogg': 'blheag1-iNat953708.m4a', 'bncfly/iNat1422961.ogg': 'bncfly-iNat1422961.m4a', 'bncfly/iNat1406256.ogg': 'bncfly-iNat1406256.m4a', 'bncfly/iNat1457501.ogg': 'bncfly-iNat1457501.m4a', 'bncfly/iNat1554596.ogg': 'bncfly-iNat1554596.mp3', 'bobfly1/iNat1691483.ogg': 'bobfly1-iNat1691483.m4a', 'bobfly1/iNat1200017.ogg': 'bobfly1-iNat1200017.mpga', 'bobfly1/iNat1556528.ogg': 'bobfly1-iNat1556528.m4a', 'bobfly1/iNat1487398.ogg': 'bobfly1-iNat1487398.m4a', 'brcmar1/iNat1730049.ogg': 'brcmar1-iNat1730049.m4a', 'brcmar1/iNat1658256.ogg': 'brcmar1-iNat1658256.m4a', 'brcmar1/iNat1737157.ogg': 'brcmar1-iNat1737157.m4a', 'brnowl/iNat1480534.ogg': 'brnowl-iNat1480534.m4a', 'brnowl/iNat1706506.ogg': 'brnowl-iNat1706506.mp3', 'brnowl/iNat1610861.ogg': 'brnowl-iNat1610861.m4a', 'brnowl/iNat514729.ogg': 'brnowl-iNat514729.m4a', 'brnowl/iNat1491227.ogg': 'brnowl-iNat1491227.m4a', 'brnowl/iNat1659173.ogg': 'brnowl-iNat1659173.m4a', 'brnowl/iNat1309637.ogg': 'brnowl-iNat1309637.m4a', 'brnowl/iNat1548013.ogg': 'brnowl-iNat1548013.m4a', 'brnowl/iNat1050844.ogg': 'brnowl-iNat1050844.m4a', 'brnowl/iNat1491232.ogg': 'brnowl-iNat1491232.m4a', 'bufpar/iNat1295642.ogg': 'bufpar-iNat1295642.mp3', 'bufpar/iNat1299514.ogg': 'bufpar-iNat1299514.m4a', 'burowl/iNat1589934.ogg': 'burowl-iNat1589934.m4a', 'camfli1/iNat1336230.ogg': 'camfli1-iNat1336230.m4a', 'chobla1/iNat228765.ogg': 'chobla1-iNat228765.m4a', 'chobla1/iNat1428711.ogg': 'chobla1-iNat1428711.m4a', 'chobla1/iNat1424302.ogg': 'chobla1-iNat1424302.m4a', 'chobla1/iNat1540294.ogg': 'chobla1-iNat1540294.m4a', 'coffal1/iNat1710475.ogg': 'coffal1-iNat1710475.m4a', 'coffal1/iNat782270.ogg': 'coffal1-iNat782270.m4a', 'coffal1/iNat905814.ogg': 'coffal1-iNat905814.m4a', 'coffal1/iNat826415.ogg': 'coffal1-iNat826415.m4a', 'coffal1/iNat1167591.ogg': 'coffal1-iNat1167591.m4a', 'coffal1/iNat1637929.ogg': 'coffal1-iNat1637929.m4a', 'coffal1/iNat782291.ogg': 'coffal1-iNat782291.m4a', 'coffal1/iNat395438.ogg': 'coffal1-iNat395438.m4a', 'compau/iNat1591339.ogg': 'compau-iNat1591339.m4a', 'compau/iNat946279.ogg': 'compau-iNat946279.m4a', 'compau/iNat1599244.ogg': 'compau-iNat1599244.m4a', 'compau/iNat1672503.ogg': 'compau-iNat1672503.m4a', 'compau/iNat1268738.ogg': 'compau-iNat1268738.m4a', 'compau/iNat1623767.ogg': 'compau-iNat1623767.m4a', 'compau/iNat1321681.ogg': 'compau-iNat1321681.m4a', 'compau/iNat1294212.ogg': 'compau-iNat1294212.m4a', 'compot1/iNat1668960.ogg': 'compot1-iNat1668960.m4a', 'compot1/iNat1660624.ogg': 'compot1-iNat1660624.m4a', 'crbthr1/iNat1693777.ogg': 'crbthr1-iNat1693777.m4a', 'crbthr1/iNat1684518.ogg': 'crbthr1-iNat1684518.m4a', 'crbthr1/iNat1678524.ogg': 'crbthr1-iNat1678524.m4a', 'crbthr1/iNat1277382.ogg': 'crbthr1-iNat1277382.m4a', 'epaori4/iNat1592245.ogg': 'epaori4-iNat1592245.m4a', 'epaori4/iNat649978.ogg': 'epaori4-iNat649978.m4a', 'eulfly1/iNat1738901.ogg': 'eulfly1-iNat1738901.m4a', 'fepowl/iNat1711295.ogg': 'fepowl-iNat1711295.m4a', 'fepowl/iNat1664968.ogg': 'fepowl-iNat1664968.m4a', 'fepowl/iNat1308138.ogg': 'fepowl-iNat1308138.m4a', 'fepowl/iNat1738605.ogg': 'fepowl-iNat1738605.m4a', 'fepowl/iNat1240485.ogg': 'fepowl-iNat1240485.mpga', 'fepowl/iNat1335628.ogg': 'fepowl-iNat1335628.m4a', 'fepowl/iNat1287848.ogg': 'fepowl-iNat1287848.mp3', 'fotfly/iNat1193130.ogg': 'fotfly-iNat1193130.m4a', 'fusfly1/iNat1518620.ogg': 'fusfly1-iNat1518620.m4a', 'giwrai1/iNat1673888.ogg': 'giwrai1-iNat1673888.m4a', 'giwrai1/iNat1349850.ogg': 'giwrai1-iNat1349850.m4a', 'grasal3/iNat1632581.ogg': 'grasal3-iNat1632581.mp3', 'grasal3/iNat1644284.ogg': 'grasal3-iNat1644284.m4a', 'grasal3/iNat1614411.ogg': 'grasal3-iNat1614411.m4a', 'greant1/iNat1635481.ogg': 'greant1-iNat1635481.m4a', 'greant1/iNat1508328.ogg': 'greant1-iNat1508328.m4a', 'greant1/iNat936816.ogg': 'greant1-iNat936816.mp3', 'greela/iNat1231355.ogg': 'greela-iNat1231355.m4a', 'grekis/iNat1690035.ogg': 'grekis-iNat1690035.m4a', 'grekis/iNat1572002.ogg': 'grekis-iNat1572002.m4a', 'grekis/iNat1209312.ogg': 'grekis-iNat1209312.mpga', 'grekis/iNat1663561.ogg': 'grekis-iNat1663561.m4a', 'grekis/iNat1400476.ogg': 'grekis-iNat1400476.m4a', 'grekis/iNat1623199.ogg': 'grekis-iNat1623199.mp3', 'grekis/iNat1391832.ogg': 'grekis-iNat1391832.m4a', 'grekis/iNat1667823.ogg': 'grekis-iNat1667823.mp3', 'greyel/iNat1381842.ogg': 'greyel-iNat1381842.m4a', 'greyel/iNat1375792.ogg': 'greyel-iNat1375792.m4a', 'greyel/iNat1375793.ogg': 'greyel-iNat1375793.m4a', 'greyel/iNat1350689.ogg': 'greyel-iNat1350689.m4a', 'greyel/iNat1370909.ogg': 'greyel-iNat1370909.m4a', 'greyel/iNat1638552.ogg': 'greyel-iNat1638552.m4a', 'greyel/iNat952416.ogg': 'greyel-iNat952416.m4a', 'greyel/iNat1350614.ogg': 'greyel-iNat1350614.m4a', 'greyel/iNat1303954.ogg': 'greyel-iNat1303954.m4a', 'grfdov1/iNat1395710.ogg': 'grfdov1-iNat1395710.m4a', 'grfdov1/iNat1400824.ogg': 'grfdov1-iNat1400824.m4a', 'gycwor1/iNat1537449.ogg': 'gycwor1-iNat1537449.m4a', 'gycwor1/iNat1288203.ogg': 'gycwor1-iNat1288203.m4a', 'gycwor1/iNat1596768.ogg': 'gycwor1-iNat1596768.m4a', 'gycwor1/iNat816375.ogg': 'gycwor1-iNat816375.mp3', 'gycwor1/iNat1255088.ogg': 'gycwor1-iNat1255088.m4a', 'gycwor1/iNat1594836.ogg': 'gycwor1-iNat1594836.m4a', 'gycwor1/iNat1378299.ogg': 'gycwor1-iNat1378299.mp3', 'gycwor1/iNat1346486.ogg': 'gycwor1-iNat1346486.m4a', 'gycwor1/iNat1620374.ogg': 'gycwor1-iNat1620374.m4a', 'gycwor1/iNat1569899.ogg': 'gycwor1-iNat1569899.m4a', 'gycwor1/iNat1624903.ogg': 'gycwor1-iNat1624903.m4a', 'gycwor1/iNat1577300.ogg': 'gycwor1-iNat1577300.m4a', 'gycwor1/iNat1724472.ogg': 'gycwor1-iNat1724472.m4a', 'gycwor1/iNat1683695.ogg': 'gycwor1-iNat1683695.m4a', 'houspa/iNat1666148.ogg': 'houspa-iNat1666148.m4a', 'houspa/iNat1409352.ogg': 'houspa-iNat1409352.m4a', 'houspa/iNat1364301.ogg': 'houspa-iNat1364301.mp3', 'houspa/iNat1551547.ogg': 'houspa-iNat1551547.m4a', 'houspa/iNat935753.ogg': 'houspa-iNat935753.m4a', 'houspa/iNat1397767.ogg': 'houspa-iNat1397767.m4a', 'houspa/iNat1512573.ogg': 'houspa-iNat1512573.m4a', 'houspa/iNat1362595.ogg': 'houspa-iNat1362595.m4a', 'houspa/iNat1417357.ogg': 'houspa-iNat1417357.m4a', 'houspa/iNat1321989.ogg': 'houspa-iNat1321989.m4a', 'houspa/iNat409684.ogg': 'houspa-iNat409684.m4a', 'houspa/iNat1304457.ogg': 'houspa-iNat1304457.m4a', 'houspa/iNat1569993.ogg': 'houspa-iNat1569993.m4a', 'houspa/iNat1731791.ogg': 'houspa-iNat1731791.m4a', 'houspa/iNat1316764.ogg': 'houspa-iNat1316764.m4a', 'houspa/iNat1358970.ogg': 'houspa-iNat1358970.m4a', 'limpki/iNat1319758.ogg': 'limpki-iNat1319758.m4a', 'limpki/iNat1320813.ogg': 'limpki-iNat1320813.m4a', 'limpki/iNat1072786.ogg': 'limpki-iNat1072786.m4a', 'linwoo1/iNat1302630.ogg': 'linwoo1-iNat1302630.m4a', 'linwoo1/iNat1535721.ogg': 'linwoo1-iNat1535721.m4a', 'linwoo1/iNat1371736.ogg': 'linwoo1-iNat1371736.m4a', 'mabpar/iNat1626097.ogg': 'mabpar-iNat1626097.m4a', 'masgna1/iNat1635487.ogg': 'masgna1-iNat1635487.m4a', 'oliwoo1/iNat1346713.ogg': 'oliwoo1-iNat1346713.m4a', 'orwpar/iNat1687083.ogg': 'orwpar-iNat1687083.m4a', 'orwpar/iNat1355177.ogg': 'orwpar-iNat1355177.m4a', 'orwpar/iNat1503877.ogg': 'orwpar-iNat1503877.m4a', 'orwpar/iNat1657675.ogg': 'orwpar-iNat1657675.mp3', 'orwpar/iNat1079708.ogg': 'orwpar-iNat1079708.m4a', 'osprey/iNat226664.ogg': 'osprey-iNat226664.m4a', 'osprey/iNat1398129.ogg': 'osprey-iNat1398129.m4a', 'osprey/iNat1595562.ogg': 'osprey-iNat1595562.m4a', 'osprey/iNat1370949.ogg': 'osprey-iNat1370949.m4a', 'osprey/iNat1692289.ogg': 'osprey-iNat1692289.m4a', 'osprey/iNat1556374.ogg': 'osprey-iNat1556374.m4a', 'osprey/iNat1004549.ogg': 'osprey-iNat1004549.m4a', 'osprey/iNat1670343.ogg': 'osprey-iNat1670343.m4a', 'osprey/iNat288776.ogg': 'osprey-iNat288776.m4a', 'osprey/iNat482127.ogg': 'osprey-iNat482127.m4a', 'osprey/iNat1135797.ogg': 'osprey-iNat1135797.m4a', 'osprey/iNat1697529.ogg': 'osprey-iNat1697529.m4a', 'osprey/iNat1359848.ogg': 'osprey-iNat1359848.m4a', 'osprey/iNat1361039.ogg': 'osprey-iNat1361039.m4a', 'paltan1/iNat1709147.ogg': 'paltan1-iNat1709147.m4a', 'paltan1/iNat1418628.ogg': 'paltan1-iNat1418628.m4a', 'paltan1/iNat1418634.ogg': 'paltan1-iNat1418634.m4a', 'paltan1/iNat1618415.ogg': 'paltan1-iNat1618415.m4a', 'picpig2/iNat1607749.ogg': 'picpig2-iNat1607749.m4a', 'pirfly1/iNat1635054.ogg': 'pirfly1-iNat1635054.m4a', 'pirfly1/iNat1677277.ogg': 'pirfly1-iNat1677277.m4a', 'plcjay1/iNat911601.ogg': 'plcjay1-iNat911601.mp3', 'plcjay1/iNat1612345.ogg': 'plcjay1-iNat1612345.m4a', 'plcjay1/iNat1435256.ogg': 'plcjay1-iNat1435256.m4a', 'plcjay1/iNat1435257.ogg': 'plcjay1-iNat1435257.m4a', 'rebscy1/iNat1324031.ogg': 'rebscy1-iNat1324031.m4a', 'redjun/iNat1661079.ogg': 'redjun-iNat1661079.m4a', 'redjun/iNat1681112.ogg': 'redjun-iNat1681112.m4a', 'redjun/iNat953958.ogg': 'redjun-iNat953958.m4a', 'relser1/iNat1557442.ogg': 'relser1-iNat1557442.m4a', 'relser1/iNat1370757.ogg': 'relser1-iNat1370757.m4a', 'relser1/iNat1344314.ogg': 'relser1-iNat1344314.mp3', 'roahaw/iNat1677378.ogg': 'roahaw-iNat1677378.m4a', 'roahaw/iNat1458636.ogg': 'roahaw-iNat1458636.mp3', 'rubthr1/iNat870811.ogg': 'rubthr1-iNat870811.mpga', 'rubthr1/iNat1684073.ogg': 'rubthr1-iNat1684073.m4a', 'rubthr1/iNat852442.ogg': 'rubthr1-iNat852442.mp3', 'rubthr1/iNat1682587.ogg': 'rubthr1-iNat1682587.mp3', 'rubthr1/iNat1672514.ogg': 'rubthr1-iNat1672514.m4a', 'rubthr1/iNat546228.ogg': 'rubthr1-iNat546228.m4a', 'rubthr1/iNat850316.ogg': 'rubthr1-iNat850316.mp3', 'rubthr1/iNat1707784.ogg': 'rubthr1-iNat1707784.mp3', 'rubthr1/iNat1615216.ogg': 'rubthr1-iNat1615216.mp3', 'rubthr1/iNat851551.ogg': 'rubthr1-iNat851551.mp3', 'rubthr1/iNat1691551.ogg': 'rubthr1-iNat1691551.m4a', 'rubthr1/iNat1691430.ogg': 'rubthr1-iNat1691430.m4a', 'rufnig1/iNat1657250.ogg': 'rufnig1-iNat1657250.m4a', 'rumfly1/iNat1734627.ogg': 'rumfly1-iNat1734627.m4a', 'ruther1/iNat1483642.ogg': 'ruther1-iNat1483642.mp3', 'saffin/iNat1692175.ogg': 'saffin-iNat1692175.m4a', 'saffin/iNat1313823.ogg': 'saffin-iNat1313823.m4a', 'saffin/iNat1300076.ogg': 'saffin-iNat1300076.m4a', 'saffin/iNat1300148.ogg': 'saffin-iNat1300148.m4a', 'saffin/iNat1667770.ogg': 'saffin-iNat1667770.mp3', 'saffin/iNat1449859.ogg': 'saffin-iNat1449859.m4a', 'saytan1/iNat1677185.ogg': 'saytan1-iNat1677185.m4a', 'scadov1/iNat1299298.ogg': 'scadov1-iNat1299298.m4a', 'scadov1/iNat1491465.ogg': 'scadov1-iNat1491465.m4a', 'scadov1/iNat1276971.ogg': 'scadov1-iNat1276971.m4a', 'schpar1/iNat1293642.ogg': 'schpar1-iNat1293642.m4a', 'shcfly1/iNat1321023.ogg': 'shcfly1-iNat1321023.m4a', 'shcfly1/iNat1532661.ogg': 'shcfly1-iNat1532661.m4a', 'shcfly1/iNat1345739.ogg': 'shcfly1-iNat1345739.m4a', 'shcfly1/iNat1471076.ogg': 'shcfly1-iNat1471076.m4a', 'shshaw/iNat1590156.ogg': 'shshaw-iNat1590156.m4a', 'shshaw/iNat1602640.ogg': 'shshaw-iNat1602640.m4a', 'shtnig1/iNat869228.ogg': 'shtnig1-iNat869228.mp3', 'shtnig1/iNat870997.ogg': 'shtnig1-iNat870997.mpga', 'shtnig1/iNat870998.ogg': 'shtnig1-iNat870998.mpga', 'shtnig1/iNat1696713.ogg': 'shtnig1-iNat1696713.m4a', 'sibtan2/iNat1402979.ogg': 'sibtan2-iNat1402979.m4a', 'smbani/iNat915724.ogg': 'smbani-iNat915724.m4a', 'smbani/iNat1594767.ogg': 'smbani-iNat1594767.m4a', 'smbtin1/iNat1734628.ogg': 'smbtin1-iNat1734628.m4a', 'smbtin1/iNat81751.ogg': 'smbtin1-iNat81751.mpga', 'sobcac1/iNat1387094.ogg': 'sobcac1-iNat1387094.m4a', 'sobcac1/iNat1432132.ogg': 'sobcac1-iNat1432132.m4a', 'sobtyr1/iNat1718955.ogg': 'sobtyr1-iNat1718955.m4a', 'sobtyr1/iNat1355327.ogg': 'sobtyr1-iNat1355327.m4a', 'socfly1/iNat1701203.ogg': 'socfly1-iNat1701203.m4a', 'socfly1/iNat1685298.ogg': 'socfly1-iNat1685298.m4a', 'socfly1/iNat1705430.ogg': 'socfly1-iNat1705430.m4a', 'socfly1/iNat1687317.ogg': 'socfly1-iNat1687317.m4a', 'socfly1/iNat1181651.ogg': 'socfly1-iNat1181651.m4a', 'socfly1/iNat671916.ogg': 'socfly1-iNat671916.m4a', 'socfly1/iNat797558.ogg': 'socfly1-iNat797558.mpga', 'sofspi1/iNat1664377.ogg': 'sofspi1-iNat1664377.mp3', 'sofspi1/iNat1510202.ogg': 'sofspi1-iNat1510202.m4a', 'soulap1/iNat1203529.ogg': 'soulap1-iNat1203529.mpga', 'soulap1/iNat1405995.ogg': 'soulap1-iNat1405995.m4a', 'soulap1/iNat1637171.ogg': 'soulap1-iNat1637171.m4a', 'soulap1/iNat1637169.ogg': 'soulap1-iNat1637169.m4a', 'soulap1/iNat1685486.ogg': 'soulap1-iNat1685486.m4a', 'soulap1/iNat1434604.ogg': 'soulap1-iNat1434604.mp3', 'souscr1/iNat1244955.ogg': 'souscr1-iNat1244955.m4a', 'spbant3/iNat1695874.ogg': 'spbant3-iNat1695874.m4a', 'spispi1/iNat1503058.ogg': 'spispi1-iNat1503058.mp3', 'spispi1/iNat1374076.ogg': 'spispi1-iNat1374076.m4a', 'spispi1/iNat1456192.ogg': 'spispi1-iNat1456192.m4a', 'squcuc1/iNat1358561.ogg': 'squcuc1-iNat1358561.m4a', 'squcuc1/iNat1358573.ogg': 'squcuc1-iNat1358573.m4a', 'squcuc1/iNat188319.ogg': 'squcuc1-iNat188319.m4a', 'strcuc1/iNat1691050.ogg': 'strcuc1-iNat1691050.m4a', 'strcuc1/iNat1675976.ogg': 'strcuc1-iNat1675976.m4a', 'strcuc1/iNat1665191.ogg': 'strcuc1-iNat1665191.m4a', 'strcuc1/iNat1670795.ogg': 'strcuc1-iNat1670795.m4a', 'strcuc1/iNat1165584.ogg': 'strcuc1-iNat1165584.m4a', 'strcuc1/iNat1490053.ogg': 'strcuc1-iNat1490053.m4a', 'strcuc1/iNat1465517.ogg': 'strcuc1-iNat1465517.m4a', 'strcuc1/iNat1367996.ogg': 'strcuc1-iNat1367996.m4a', 'strcuc1/iNat1347727.ogg': 'strcuc1-iNat1347727.m4a', 'strowl1/iNat1451619.ogg': 'strowl1-iNat1451619.m4a', 'strowl1/iNat1736437.ogg': 'strowl1-iNat1736437.m4a', 'strowl1/iNat1537360.ogg': 'strowl1-iNat1537360.m4a', 'swtman1/iNat1468159.ogg': 'swtman1-iNat1468159.m4a', 'swtman1/iNat841931.ogg': 'swtman1-iNat841931.mp3', 'swtman1/iNat980195.ogg': 'swtman1-iNat980195.mp3', 'swtman1/iNat1647280.ogg': 'swtman1-iNat1647280.m4a', 'swtman1/iNat1420444.ogg': 'swtman1-iNat1420444.m4a', 'swtman1/iNat1664402.ogg': 'swtman1-iNat1664402.m4a', 'swtman1/iNat1667664.ogg': 'swtman1-iNat1667664.mp3', 'tattin1/iNat1291008.ogg': 'tattin1-iNat1291008.m4a', 'thlwre1/iNat1446997.ogg': 'thlwre1-iNat1446997.m4a', 'thlwre1/iNat1540292.ogg': 'thlwre1-iNat1540292.m4a', 'toctou1/iNat1406213.ogg': 'toctou1-iNat1406213.m4a', 'trokin/iNat1543761.ogg': 'trokin-iNat1543761.m4a', 'trokin/iNat1088126.ogg': 'trokin-iNat1088126.m4a', 'trokin/iNat1631950.ogg': 'trokin-iNat1631950.m4a', 'trsowl/iNat1337876.ogg': 'trsowl-iNat1337876.m4a', 'trsowl/iNat1321621.ogg': 'trsowl-iNat1321621.m4a', 'trsowl/iNat1240859.ogg': 'trsowl-iNat1240859.mpga', 'trsowl/iNat1707373.ogg': 'trsowl-iNat1707373.m4a', 'trsowl/iNat1608858.ogg': 'trsowl-iNat1608858.m4a', 'varant1/iNat1227614.ogg': 'varant1-iNat1227614.m4a', 'wfwduc1/iNat1679287.ogg': 'wfwduc1-iNat1679287.m4a', 'wfwduc1/iNat1487538.ogg': 'wfwduc1-iNat1487538.m4a', 'whbwar2/iNat763637.ogg': 'whbwar2-iNat763637.m4a', 'whiwoo1/iNat1594296.ogg': 'whiwoo1-iNat1594296.m4a', 'whnjay1/iNat1404548.ogg': 'whnjay1-iNat1404548.m4a', 'whnjay1/iNat1199393.ogg': 'whnjay1-iNat1199393.mpga', 'whnjay1/iNat771603.ogg': 'whnjay1-iNat771603.mp3', 'whnjay1/iNat1636518.ogg': 'whnjay1-iNat1636518.m4a', 'whnjay1/iNat1651360.ogg': 'whnjay1-iNat1651360.m4a', 'whtdov/iNat1536547.ogg': 'whtdov-iNat1536547.m4a', 'whtdov/iNat1594270.ogg': 'whtdov-iNat1594270.m4a', 'whtdov/iNat1598157.ogg': 'whtdov-iNat1598157.m4a', 'y00678/iNat1461732.ogg': 'y00678-iNat1461732.mp3', 'y00678/iNat1593494.ogg': 'y00678-iNat1593494.m4a', 'y00678/iNat1397691.ogg': 'y00678-iNat1397691.m4a', 'yebela1/iNat1593008.ogg': 'yebela1-iNat1593008.m4a', 'yebela1/iNat1479050.ogg': 'yebela1-iNat1479050.mp3', 'yebela1/iNat1521944.ogg': 'yebela1-iNat1521944.m4a', 'yecpar/iNat1360878.ogg': 'yecpar-iNat1360878.m4a', 'yecpar/iNat1347445.ogg': 'yecpar-iNat1347445.mp3', 'yehcar1/iNat1268927.ogg': 'yehcar1-iNat1268927.m4a', 'yehcar1/iNat585409.ogg': 'yehcar1-iNat585409.m4a', 'yehcar1/iNat1701473.ogg': 'yehcar1-iNat1701473.m4a'}
_PATH_MAP = {'/home/salman/Documents/data/birdclef-2026/train_audio/stbwoo2/XC467895.ogg': '/home/salman/Documents/data/download_corrupt/stbwoo2-XC467895.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/1161364/iNat1264238.ogg': '/home/salman/Documents/data/download_corrupt/1161364-iNat1264238.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/209233/iNat1545859.ogg': '/home/salman/Documents/data/download_corrupt/209233-iNat1545859.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/22956/iNat1693371.ogg': '/home/salman/Documents/data/download_corrupt/22956-iNat1693371.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/22973/iNat781822.ogg': '/home/salman/Documents/data/download_corrupt/22973-iNat781822.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/22973/iNat1353836.ogg': '/home/salman/Documents/data/download_corrupt/22973-iNat1353836.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/22973/iNat1460521.ogg': '/home/salman/Documents/data/download_corrupt/22973-iNat1460521.mpga', '/home/salman/Documents/data/birdclef-2026/train_audio/22973/iNat1645288.ogg': '/home/salman/Documents/data/download_corrupt/22973-iNat1645288.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/23158/iNat1322093.ogg': '/home/salman/Documents/data/download_corrupt/23158-iNat1322093.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/24279/iNat1306335.ogg': '/home/salman/Documents/data/download_corrupt/24279-iNat1306335.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/24279/iNat1435402.ogg': '/home/salman/Documents/data/download_corrupt/24279-iNat1435402.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/244024/iNat1219059.ogg': '/home/salman/Documents/data/download_corrupt/244024-iNat1219059.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/244024/iNat1583846.ogg': '/home/salman/Documents/data/download_corrupt/244024-iNat1583846.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/244024/iNat1573678.ogg': '/home/salman/Documents/data/download_corrupt/244024-iNat1573678.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/25092/iNat1645314.ogg': '/home/salman/Documents/data/download_corrupt/25092-iNat1645314.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/326272/iNat1299066.ogg': '/home/salman/Documents/data/download_corrupt/326272-iNat1299066.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/326272/iNat1303382.ogg': '/home/salman/Documents/data/download_corrupt/326272-iNat1303382.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/43435/iNat1054872.ogg': '/home/salman/Documents/data/download_corrupt/43435-iNat1054872.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/43435/iNat1243480.ogg': '/home/salman/Documents/data/download_corrupt/43435-iNat1243480.mpga', '/home/salman/Documents/data/birdclef-2026/train_audio/47144/iNat1717935.ogg': '/home/salman/Documents/data/download_corrupt/47144-iNat1717935.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/47144/iNat1346356.ogg': '/home/salman/Documents/data/download_corrupt/47144-iNat1346356.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/47144/iNat1346365.ogg': '/home/salman/Documents/data/download_corrupt/47144-iNat1346365.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/47144/iNat1317366.ogg': '/home/salman/Documents/data/download_corrupt/47144-iNat1317366.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/47144/iNat1559514.ogg': '/home/salman/Documents/data/download_corrupt/47144-iNat1559514.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/47144/iNat1191939.ogg': '/home/salman/Documents/data/download_corrupt/47144-iNat1191939.mpga', '/home/salman/Documents/data/birdclef-2026/train_audio/476521/iNat1648597.ogg': '/home/salman/Documents/data/download_corrupt/476521-iNat1648597.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/555146/iNat1375734.ogg': '/home/salman/Documents/data/download_corrupt/555146-iNat1375734.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/555146/iNat1375753.ogg': '/home/salman/Documents/data/download_corrupt/555146-iNat1375753.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/65377/iNat1372639.ogg': '/home/salman/Documents/data/download_corrupt/65377-iNat1372639.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/65377/iNat924044.ogg': '/home/salman/Documents/data/download_corrupt/65377-iNat924044.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/65377/iNat924035.ogg': '/home/salman/Documents/data/download_corrupt/65377-iNat924035.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/65377/iNat1676955.ogg': '/home/salman/Documents/data/download_corrupt/65377-iNat1676955.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/67107/iNat1635719.ogg': '/home/salman/Documents/data/download_corrupt/67107-iNat1635719.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/ashgre1/iNat963674.ogg': '/home/salman/Documents/data/download_corrupt/ashgre1-iNat963674.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/ashgre1/iNat1400791.ogg': '/home/salman/Documents/data/download_corrupt/ashgre1-iNat1400791.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/baffal1/iNat1672327.ogg': '/home/salman/Documents/data/download_corrupt/baffal1-iNat1672327.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/baffal1/iNat1711622.ogg': '/home/salman/Documents/data/download_corrupt/baffal1-iNat1711622.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/banana/iNat1638891.ogg': '/home/salman/Documents/data/download_corrupt/banana-iNat1638891.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/banana/iNat1302882.ogg': '/home/salman/Documents/data/download_corrupt/banana-iNat1302882.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/banana/iNat1371833.ogg': '/home/salman/Documents/data/download_corrupt/banana-iNat1371833.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/banana/iNat335243.ogg': '/home/salman/Documents/data/download_corrupt/banana-iNat335243.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/banana/iNat1631602.ogg': '/home/salman/Documents/data/download_corrupt/banana-iNat1631602.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/banana/iNat1496209.ogg': '/home/salman/Documents/data/download_corrupt/banana-iNat1496209.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/banana/iNat1630115.ogg': '/home/salman/Documents/data/download_corrupt/banana-iNat1630115.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/barant1/iNat1654575.ogg': '/home/salman/Documents/data/download_corrupt/barant1-iNat1654575.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/barant1/iNat1418545.ogg': '/home/salman/Documents/data/download_corrupt/barant1-iNat1418545.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/barant1/iNat1738725.ogg': '/home/salman/Documents/data/download_corrupt/barant1-iNat1738725.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/barant1/iNat76423.ogg': '/home/salman/Documents/data/download_corrupt/barant1-iNat76423.mpga', '/home/salman/Documents/data/birdclef-2026/train_audio/batbel1/iNat851301.ogg': '/home/salman/Documents/data/download_corrupt/batbel1-iNat851301.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/batbel1/iNat851302.ogg': '/home/salman/Documents/data/download_corrupt/batbel1-iNat851302.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/batbel1/iNat851299.ogg': '/home/salman/Documents/data/download_corrupt/batbel1-iNat851299.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/batbel1/iNat1275000.ogg': '/home/salman/Documents/data/download_corrupt/batbel1-iNat1275000.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/batbel1/iNat1517987.ogg': '/home/salman/Documents/data/download_corrupt/batbel1-iNat1517987.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/batbel1/iNat1710152.ogg': '/home/salman/Documents/data/download_corrupt/batbel1-iNat1710152.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/baymac/iNat1304419.ogg': '/home/salman/Documents/data/download_corrupt/baymac-iNat1304419.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/baymac/iNat976078.ogg': '/home/salman/Documents/data/download_corrupt/baymac-iNat976078.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1318531.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1318531.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat942901.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat942901.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1294916.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1294916.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1338852.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1338852.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1499546.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1499546.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1352566.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1352566.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1543298.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1543298.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1683874.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1683874.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1580446.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1580446.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat418728.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat418728.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat797291.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat797291.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat950353.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat950353.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1333153.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1333153.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat594163.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat594163.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1520789.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1520789.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1705504.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1705504.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bkcdon/iNat1637377.ogg': '/home/salman/Documents/data/download_corrupt/bkcdon-iNat1637377.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bkcdon/iNat1396398.ogg': '/home/salman/Documents/data/download_corrupt/bkcdon-iNat1396398.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bkhpar/iNat1637590.ogg': '/home/salman/Documents/data/download_corrupt/bkhpar-iNat1637590.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bkhpar/iNat1029272.ogg': '/home/salman/Documents/data/download_corrupt/bkhpar-iNat1029272.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/blheag1/iNat1675853.ogg': '/home/salman/Documents/data/download_corrupt/blheag1-iNat1675853.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/blheag1/iNat953708.ogg': '/home/salman/Documents/data/download_corrupt/blheag1-iNat953708.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bncfly/iNat1422961.ogg': '/home/salman/Documents/data/download_corrupt/bncfly-iNat1422961.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bncfly/iNat1406256.ogg': '/home/salman/Documents/data/download_corrupt/bncfly-iNat1406256.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bncfly/iNat1457501.ogg': '/home/salman/Documents/data/download_corrupt/bncfly-iNat1457501.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bncfly/iNat1554596.ogg': '/home/salman/Documents/data/download_corrupt/bncfly-iNat1554596.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/bobfly1/iNat1691483.ogg': '/home/salman/Documents/data/download_corrupt/bobfly1-iNat1691483.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bobfly1/iNat1200017.ogg': '/home/salman/Documents/data/download_corrupt/bobfly1-iNat1200017.mpga', '/home/salman/Documents/data/birdclef-2026/train_audio/bobfly1/iNat1556528.ogg': '/home/salman/Documents/data/download_corrupt/bobfly1-iNat1556528.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bobfly1/iNat1487398.ogg': '/home/salman/Documents/data/download_corrupt/bobfly1-iNat1487398.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/brcmar1/iNat1730049.ogg': '/home/salman/Documents/data/download_corrupt/brcmar1-iNat1730049.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/brcmar1/iNat1658256.ogg': '/home/salman/Documents/data/download_corrupt/brcmar1-iNat1658256.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/brcmar1/iNat1737157.ogg': '/home/salman/Documents/data/download_corrupt/brcmar1-iNat1737157.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/brnowl/iNat1480534.ogg': '/home/salman/Documents/data/download_corrupt/brnowl-iNat1480534.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/brnowl/iNat1706506.ogg': '/home/salman/Documents/data/download_corrupt/brnowl-iNat1706506.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/brnowl/iNat1610861.ogg': '/home/salman/Documents/data/download_corrupt/brnowl-iNat1610861.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/brnowl/iNat514729.ogg': '/home/salman/Documents/data/download_corrupt/brnowl-iNat514729.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/brnowl/iNat1491227.ogg': '/home/salman/Documents/data/download_corrupt/brnowl-iNat1491227.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/brnowl/iNat1659173.ogg': '/home/salman/Documents/data/download_corrupt/brnowl-iNat1659173.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/brnowl/iNat1309637.ogg': '/home/salman/Documents/data/download_corrupt/brnowl-iNat1309637.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/brnowl/iNat1548013.ogg': '/home/salman/Documents/data/download_corrupt/brnowl-iNat1548013.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/brnowl/iNat1050844.ogg': '/home/salman/Documents/data/download_corrupt/brnowl-iNat1050844.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/brnowl/iNat1491232.ogg': '/home/salman/Documents/data/download_corrupt/brnowl-iNat1491232.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/bufpar/iNat1295642.ogg': '/home/salman/Documents/data/download_corrupt/bufpar-iNat1295642.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/bufpar/iNat1299514.ogg': '/home/salman/Documents/data/download_corrupt/bufpar-iNat1299514.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/burowl/iNat1589934.ogg': '/home/salman/Documents/data/download_corrupt/burowl-iNat1589934.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/camfli1/iNat1336230.ogg': '/home/salman/Documents/data/download_corrupt/camfli1-iNat1336230.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/chobla1/iNat228765.ogg': '/home/salman/Documents/data/download_corrupt/chobla1-iNat228765.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/chobla1/iNat1428711.ogg': '/home/salman/Documents/data/download_corrupt/chobla1-iNat1428711.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/chobla1/iNat1424302.ogg': '/home/salman/Documents/data/download_corrupt/chobla1-iNat1424302.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/chobla1/iNat1540294.ogg': '/home/salman/Documents/data/download_corrupt/chobla1-iNat1540294.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/coffal1/iNat1710475.ogg': '/home/salman/Documents/data/download_corrupt/coffal1-iNat1710475.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/coffal1/iNat782270.ogg': '/home/salman/Documents/data/download_corrupt/coffal1-iNat782270.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/coffal1/iNat905814.ogg': '/home/salman/Documents/data/download_corrupt/coffal1-iNat905814.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/coffal1/iNat826415.ogg': '/home/salman/Documents/data/download_corrupt/coffal1-iNat826415.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/coffal1/iNat1167591.ogg': '/home/salman/Documents/data/download_corrupt/coffal1-iNat1167591.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/coffal1/iNat1637929.ogg': '/home/salman/Documents/data/download_corrupt/coffal1-iNat1637929.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/coffal1/iNat782291.ogg': '/home/salman/Documents/data/download_corrupt/coffal1-iNat782291.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/coffal1/iNat395438.ogg': '/home/salman/Documents/data/download_corrupt/coffal1-iNat395438.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/compau/iNat1591339.ogg': '/home/salman/Documents/data/download_corrupt/compau-iNat1591339.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/compau/iNat946279.ogg': '/home/salman/Documents/data/download_corrupt/compau-iNat946279.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/compau/iNat1599244.ogg': '/home/salman/Documents/data/download_corrupt/compau-iNat1599244.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/compau/iNat1672503.ogg': '/home/salman/Documents/data/download_corrupt/compau-iNat1672503.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/compau/iNat1268738.ogg': '/home/salman/Documents/data/download_corrupt/compau-iNat1268738.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/compau/iNat1623767.ogg': '/home/salman/Documents/data/download_corrupt/compau-iNat1623767.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/compau/iNat1321681.ogg': '/home/salman/Documents/data/download_corrupt/compau-iNat1321681.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/compau/iNat1294212.ogg': '/home/salman/Documents/data/download_corrupt/compau-iNat1294212.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/compot1/iNat1668960.ogg': '/home/salman/Documents/data/download_corrupt/compot1-iNat1668960.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/compot1/iNat1660624.ogg': '/home/salman/Documents/data/download_corrupt/compot1-iNat1660624.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/crbthr1/iNat1693777.ogg': '/home/salman/Documents/data/download_corrupt/crbthr1-iNat1693777.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/crbthr1/iNat1684518.ogg': '/home/salman/Documents/data/download_corrupt/crbthr1-iNat1684518.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/crbthr1/iNat1678524.ogg': '/home/salman/Documents/data/download_corrupt/crbthr1-iNat1678524.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/crbthr1/iNat1277382.ogg': '/home/salman/Documents/data/download_corrupt/crbthr1-iNat1277382.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/epaori4/iNat1592245.ogg': '/home/salman/Documents/data/download_corrupt/epaori4-iNat1592245.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/epaori4/iNat649978.ogg': '/home/salman/Documents/data/download_corrupt/epaori4-iNat649978.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/eulfly1/iNat1738901.ogg': '/home/salman/Documents/data/download_corrupt/eulfly1-iNat1738901.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/fepowl/iNat1711295.ogg': '/home/salman/Documents/data/download_corrupt/fepowl-iNat1711295.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/fepowl/iNat1664968.ogg': '/home/salman/Documents/data/download_corrupt/fepowl-iNat1664968.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/fepowl/iNat1308138.ogg': '/home/salman/Documents/data/download_corrupt/fepowl-iNat1308138.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/fepowl/iNat1738605.ogg': '/home/salman/Documents/data/download_corrupt/fepowl-iNat1738605.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/fepowl/iNat1240485.ogg': '/home/salman/Documents/data/download_corrupt/fepowl-iNat1240485.mpga', '/home/salman/Documents/data/birdclef-2026/train_audio/fepowl/iNat1335628.ogg': '/home/salman/Documents/data/download_corrupt/fepowl-iNat1335628.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/fepowl/iNat1287848.ogg': '/home/salman/Documents/data/download_corrupt/fepowl-iNat1287848.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/fotfly/iNat1193130.ogg': '/home/salman/Documents/data/download_corrupt/fotfly-iNat1193130.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/fusfly1/iNat1518620.ogg': '/home/salman/Documents/data/download_corrupt/fusfly1-iNat1518620.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/giwrai1/iNat1673888.ogg': '/home/salman/Documents/data/download_corrupt/giwrai1-iNat1673888.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/giwrai1/iNat1349850.ogg': '/home/salman/Documents/data/download_corrupt/giwrai1-iNat1349850.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/grasal3/iNat1632581.ogg': '/home/salman/Documents/data/download_corrupt/grasal3-iNat1632581.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/grasal3/iNat1644284.ogg': '/home/salman/Documents/data/download_corrupt/grasal3-iNat1644284.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/grasal3/iNat1614411.ogg': '/home/salman/Documents/data/download_corrupt/grasal3-iNat1614411.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/greant1/iNat1635481.ogg': '/home/salman/Documents/data/download_corrupt/greant1-iNat1635481.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/greant1/iNat1508328.ogg': '/home/salman/Documents/data/download_corrupt/greant1-iNat1508328.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/greant1/iNat936816.ogg': '/home/salman/Documents/data/download_corrupt/greant1-iNat936816.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/greela/iNat1231355.ogg': '/home/salman/Documents/data/download_corrupt/greela-iNat1231355.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/grekis/iNat1690035.ogg': '/home/salman/Documents/data/download_corrupt/grekis-iNat1690035.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/grekis/iNat1572002.ogg': '/home/salman/Documents/data/download_corrupt/grekis-iNat1572002.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/grekis/iNat1209312.ogg': '/home/salman/Documents/data/download_corrupt/grekis-iNat1209312.mpga', '/home/salman/Documents/data/birdclef-2026/train_audio/grekis/iNat1663561.ogg': '/home/salman/Documents/data/download_corrupt/grekis-iNat1663561.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/grekis/iNat1400476.ogg': '/home/salman/Documents/data/download_corrupt/grekis-iNat1400476.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/grekis/iNat1623199.ogg': '/home/salman/Documents/data/download_corrupt/grekis-iNat1623199.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/grekis/iNat1391832.ogg': '/home/salman/Documents/data/download_corrupt/grekis-iNat1391832.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/grekis/iNat1667823.ogg': '/home/salman/Documents/data/download_corrupt/grekis-iNat1667823.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/greyel/iNat1381842.ogg': '/home/salman/Documents/data/download_corrupt/greyel-iNat1381842.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/greyel/iNat1375792.ogg': '/home/salman/Documents/data/download_corrupt/greyel-iNat1375792.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/greyel/iNat1375793.ogg': '/home/salman/Documents/data/download_corrupt/greyel-iNat1375793.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/greyel/iNat1350689.ogg': '/home/salman/Documents/data/download_corrupt/greyel-iNat1350689.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/greyel/iNat1370909.ogg': '/home/salman/Documents/data/download_corrupt/greyel-iNat1370909.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/greyel/iNat1638552.ogg': '/home/salman/Documents/data/download_corrupt/greyel-iNat1638552.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/greyel/iNat952416.ogg': '/home/salman/Documents/data/download_corrupt/greyel-iNat952416.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/greyel/iNat1350614.ogg': '/home/salman/Documents/data/download_corrupt/greyel-iNat1350614.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/greyel/iNat1303954.ogg': '/home/salman/Documents/data/download_corrupt/greyel-iNat1303954.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/grfdov1/iNat1395710.ogg': '/home/salman/Documents/data/download_corrupt/grfdov1-iNat1395710.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/grfdov1/iNat1400824.ogg': '/home/salman/Documents/data/download_corrupt/grfdov1-iNat1400824.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1537449.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1537449.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1288203.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1288203.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1596768.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1596768.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat816375.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat816375.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1255088.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1255088.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1594836.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1594836.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1378299.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1378299.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1346486.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1346486.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1620374.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1620374.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1569899.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1569899.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1624903.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1624903.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1577300.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1577300.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1724472.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1724472.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1683695.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1683695.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1666148.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1666148.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1409352.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1409352.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1364301.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1364301.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1551547.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1551547.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat935753.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat935753.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1397767.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1397767.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1512573.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1512573.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1362595.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1362595.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1417357.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1417357.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1321989.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1321989.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat409684.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat409684.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1304457.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1304457.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1569993.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1569993.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1731791.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1731791.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1316764.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1316764.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1358970.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1358970.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/limpki/iNat1319758.ogg': '/home/salman/Documents/data/download_corrupt/limpki-iNat1319758.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/limpki/iNat1320813.ogg': '/home/salman/Documents/data/download_corrupt/limpki-iNat1320813.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/limpki/iNat1072786.ogg': '/home/salman/Documents/data/download_corrupt/limpki-iNat1072786.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/linwoo1/iNat1302630.ogg': '/home/salman/Documents/data/download_corrupt/linwoo1-iNat1302630.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/linwoo1/iNat1535721.ogg': '/home/salman/Documents/data/download_corrupt/linwoo1-iNat1535721.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/linwoo1/iNat1371736.ogg': '/home/salman/Documents/data/download_corrupt/linwoo1-iNat1371736.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/mabpar/iNat1626097.ogg': '/home/salman/Documents/data/download_corrupt/mabpar-iNat1626097.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/masgna1/iNat1635487.ogg': '/home/salman/Documents/data/download_corrupt/masgna1-iNat1635487.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/oliwoo1/iNat1346713.ogg': '/home/salman/Documents/data/download_corrupt/oliwoo1-iNat1346713.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/orwpar/iNat1687083.ogg': '/home/salman/Documents/data/download_corrupt/orwpar-iNat1687083.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/orwpar/iNat1355177.ogg': '/home/salman/Documents/data/download_corrupt/orwpar-iNat1355177.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/orwpar/iNat1503877.ogg': '/home/salman/Documents/data/download_corrupt/orwpar-iNat1503877.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/orwpar/iNat1657675.ogg': '/home/salman/Documents/data/download_corrupt/orwpar-iNat1657675.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/orwpar/iNat1079708.ogg': '/home/salman/Documents/data/download_corrupt/orwpar-iNat1079708.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat226664.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat226664.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1398129.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1398129.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1595562.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1595562.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1370949.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1370949.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1692289.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1692289.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1556374.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1556374.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1004549.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1004549.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1670343.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1670343.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat288776.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat288776.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat482127.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat482127.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1135797.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1135797.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1697529.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1697529.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1359848.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1359848.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1361039.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1361039.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/paltan1/iNat1709147.ogg': '/home/salman/Documents/data/download_corrupt/paltan1-iNat1709147.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/paltan1/iNat1418628.ogg': '/home/salman/Documents/data/download_corrupt/paltan1-iNat1418628.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/paltan1/iNat1418634.ogg': '/home/salman/Documents/data/download_corrupt/paltan1-iNat1418634.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/paltan1/iNat1618415.ogg': '/home/salman/Documents/data/download_corrupt/paltan1-iNat1618415.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/picpig2/iNat1607749.ogg': '/home/salman/Documents/data/download_corrupt/picpig2-iNat1607749.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/pirfly1/iNat1635054.ogg': '/home/salman/Documents/data/download_corrupt/pirfly1-iNat1635054.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/pirfly1/iNat1677277.ogg': '/home/salman/Documents/data/download_corrupt/pirfly1-iNat1677277.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/plcjay1/iNat911601.ogg': '/home/salman/Documents/data/download_corrupt/plcjay1-iNat911601.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/plcjay1/iNat1612345.ogg': '/home/salman/Documents/data/download_corrupt/plcjay1-iNat1612345.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/plcjay1/iNat1435256.ogg': '/home/salman/Documents/data/download_corrupt/plcjay1-iNat1435256.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/plcjay1/iNat1435257.ogg': '/home/salman/Documents/data/download_corrupt/plcjay1-iNat1435257.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/rebscy1/iNat1324031.ogg': '/home/salman/Documents/data/download_corrupt/rebscy1-iNat1324031.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/redjun/iNat1661079.ogg': '/home/salman/Documents/data/download_corrupt/redjun-iNat1661079.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/redjun/iNat1681112.ogg': '/home/salman/Documents/data/download_corrupt/redjun-iNat1681112.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/redjun/iNat953958.ogg': '/home/salman/Documents/data/download_corrupt/redjun-iNat953958.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/relser1/iNat1557442.ogg': '/home/salman/Documents/data/download_corrupt/relser1-iNat1557442.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/relser1/iNat1370757.ogg': '/home/salman/Documents/data/download_corrupt/relser1-iNat1370757.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/relser1/iNat1344314.ogg': '/home/salman/Documents/data/download_corrupt/relser1-iNat1344314.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/roahaw/iNat1677378.ogg': '/home/salman/Documents/data/download_corrupt/roahaw-iNat1677378.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/roahaw/iNat1458636.ogg': '/home/salman/Documents/data/download_corrupt/roahaw-iNat1458636.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat870811.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat870811.mpga', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat1684073.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat1684073.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat852442.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat852442.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat1682587.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat1682587.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat1672514.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat1672514.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat546228.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat546228.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat850316.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat850316.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat1707784.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat1707784.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat1615216.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat1615216.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat851551.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat851551.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat1691551.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat1691551.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat1691430.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat1691430.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/rufnig1/iNat1657250.ogg': '/home/salman/Documents/data/download_corrupt/rufnig1-iNat1657250.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/rumfly1/iNat1734627.ogg': '/home/salman/Documents/data/download_corrupt/rumfly1-iNat1734627.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/ruther1/iNat1483642.ogg': '/home/salman/Documents/data/download_corrupt/ruther1-iNat1483642.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/saffin/iNat1692175.ogg': '/home/salman/Documents/data/download_corrupt/saffin-iNat1692175.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/saffin/iNat1313823.ogg': '/home/salman/Documents/data/download_corrupt/saffin-iNat1313823.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/saffin/iNat1300076.ogg': '/home/salman/Documents/data/download_corrupt/saffin-iNat1300076.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/saffin/iNat1300148.ogg': '/home/salman/Documents/data/download_corrupt/saffin-iNat1300148.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/saffin/iNat1667770.ogg': '/home/salman/Documents/data/download_corrupt/saffin-iNat1667770.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/saffin/iNat1449859.ogg': '/home/salman/Documents/data/download_corrupt/saffin-iNat1449859.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/saytan1/iNat1677185.ogg': '/home/salman/Documents/data/download_corrupt/saytan1-iNat1677185.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/scadov1/iNat1299298.ogg': '/home/salman/Documents/data/download_corrupt/scadov1-iNat1299298.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/scadov1/iNat1491465.ogg': '/home/salman/Documents/data/download_corrupt/scadov1-iNat1491465.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/scadov1/iNat1276971.ogg': '/home/salman/Documents/data/download_corrupt/scadov1-iNat1276971.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/schpar1/iNat1293642.ogg': '/home/salman/Documents/data/download_corrupt/schpar1-iNat1293642.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/shcfly1/iNat1321023.ogg': '/home/salman/Documents/data/download_corrupt/shcfly1-iNat1321023.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/shcfly1/iNat1532661.ogg': '/home/salman/Documents/data/download_corrupt/shcfly1-iNat1532661.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/shcfly1/iNat1345739.ogg': '/home/salman/Documents/data/download_corrupt/shcfly1-iNat1345739.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/shcfly1/iNat1471076.ogg': '/home/salman/Documents/data/download_corrupt/shcfly1-iNat1471076.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/shshaw/iNat1590156.ogg': '/home/salman/Documents/data/download_corrupt/shshaw-iNat1590156.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/shshaw/iNat1602640.ogg': '/home/salman/Documents/data/download_corrupt/shshaw-iNat1602640.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/shtnig1/iNat869228.ogg': '/home/salman/Documents/data/download_corrupt/shtnig1-iNat869228.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/shtnig1/iNat870997.ogg': '/home/salman/Documents/data/download_corrupt/shtnig1-iNat870997.mpga', '/home/salman/Documents/data/birdclef-2026/train_audio/shtnig1/iNat870998.ogg': '/home/salman/Documents/data/download_corrupt/shtnig1-iNat870998.mpga', '/home/salman/Documents/data/birdclef-2026/train_audio/shtnig1/iNat1696713.ogg': '/home/salman/Documents/data/download_corrupt/shtnig1-iNat1696713.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/sibtan2/iNat1402979.ogg': '/home/salman/Documents/data/download_corrupt/sibtan2-iNat1402979.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/smbani/iNat915724.ogg': '/home/salman/Documents/data/download_corrupt/smbani-iNat915724.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/smbani/iNat1594767.ogg': '/home/salman/Documents/data/download_corrupt/smbani-iNat1594767.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/smbtin1/iNat1734628.ogg': '/home/salman/Documents/data/download_corrupt/smbtin1-iNat1734628.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/smbtin1/iNat81751.ogg': '/home/salman/Documents/data/download_corrupt/smbtin1-iNat81751.mpga', '/home/salman/Documents/data/birdclef-2026/train_audio/sobcac1/iNat1387094.ogg': '/home/salman/Documents/data/download_corrupt/sobcac1-iNat1387094.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/sobcac1/iNat1432132.ogg': '/home/salman/Documents/data/download_corrupt/sobcac1-iNat1432132.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/sobtyr1/iNat1718955.ogg': '/home/salman/Documents/data/download_corrupt/sobtyr1-iNat1718955.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/sobtyr1/iNat1355327.ogg': '/home/salman/Documents/data/download_corrupt/sobtyr1-iNat1355327.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/socfly1/iNat1701203.ogg': '/home/salman/Documents/data/download_corrupt/socfly1-iNat1701203.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/socfly1/iNat1685298.ogg': '/home/salman/Documents/data/download_corrupt/socfly1-iNat1685298.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/socfly1/iNat1705430.ogg': '/home/salman/Documents/data/download_corrupt/socfly1-iNat1705430.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/socfly1/iNat1687317.ogg': '/home/salman/Documents/data/download_corrupt/socfly1-iNat1687317.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/socfly1/iNat1181651.ogg': '/home/salman/Documents/data/download_corrupt/socfly1-iNat1181651.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/socfly1/iNat671916.ogg': '/home/salman/Documents/data/download_corrupt/socfly1-iNat671916.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/socfly1/iNat797558.ogg': '/home/salman/Documents/data/download_corrupt/socfly1-iNat797558.mpga', '/home/salman/Documents/data/birdclef-2026/train_audio/sofspi1/iNat1664377.ogg': '/home/salman/Documents/data/download_corrupt/sofspi1-iNat1664377.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/sofspi1/iNat1510202.ogg': '/home/salman/Documents/data/download_corrupt/sofspi1-iNat1510202.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/soulap1/iNat1203529.ogg': '/home/salman/Documents/data/download_corrupt/soulap1-iNat1203529.mpga', '/home/salman/Documents/data/birdclef-2026/train_audio/soulap1/iNat1405995.ogg': '/home/salman/Documents/data/download_corrupt/soulap1-iNat1405995.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/soulap1/iNat1637171.ogg': '/home/salman/Documents/data/download_corrupt/soulap1-iNat1637171.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/soulap1/iNat1637169.ogg': '/home/salman/Documents/data/download_corrupt/soulap1-iNat1637169.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/soulap1/iNat1685486.ogg': '/home/salman/Documents/data/download_corrupt/soulap1-iNat1685486.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/soulap1/iNat1434604.ogg': '/home/salman/Documents/data/download_corrupt/soulap1-iNat1434604.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/souscr1/iNat1244955.ogg': '/home/salman/Documents/data/download_corrupt/souscr1-iNat1244955.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/spbant3/iNat1695874.ogg': '/home/salman/Documents/data/download_corrupt/spbant3-iNat1695874.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/spispi1/iNat1503058.ogg': '/home/salman/Documents/data/download_corrupt/spispi1-iNat1503058.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/spispi1/iNat1374076.ogg': '/home/salman/Documents/data/download_corrupt/spispi1-iNat1374076.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/spispi1/iNat1456192.ogg': '/home/salman/Documents/data/download_corrupt/spispi1-iNat1456192.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/squcuc1/iNat1358561.ogg': '/home/salman/Documents/data/download_corrupt/squcuc1-iNat1358561.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/squcuc1/iNat1358573.ogg': '/home/salman/Documents/data/download_corrupt/squcuc1-iNat1358573.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/squcuc1/iNat188319.ogg': '/home/salman/Documents/data/download_corrupt/squcuc1-iNat188319.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/strcuc1/iNat1691050.ogg': '/home/salman/Documents/data/download_corrupt/strcuc1-iNat1691050.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/strcuc1/iNat1675976.ogg': '/home/salman/Documents/data/download_corrupt/strcuc1-iNat1675976.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/strcuc1/iNat1665191.ogg': '/home/salman/Documents/data/download_corrupt/strcuc1-iNat1665191.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/strcuc1/iNat1670795.ogg': '/home/salman/Documents/data/download_corrupt/strcuc1-iNat1670795.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/strcuc1/iNat1165584.ogg': '/home/salman/Documents/data/download_corrupt/strcuc1-iNat1165584.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/strcuc1/iNat1490053.ogg': '/home/salman/Documents/data/download_corrupt/strcuc1-iNat1490053.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/strcuc1/iNat1465517.ogg': '/home/salman/Documents/data/download_corrupt/strcuc1-iNat1465517.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/strcuc1/iNat1367996.ogg': '/home/salman/Documents/data/download_corrupt/strcuc1-iNat1367996.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/strcuc1/iNat1347727.ogg': '/home/salman/Documents/data/download_corrupt/strcuc1-iNat1347727.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/strowl1/iNat1451619.ogg': '/home/salman/Documents/data/download_corrupt/strowl1-iNat1451619.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/strowl1/iNat1736437.ogg': '/home/salman/Documents/data/download_corrupt/strowl1-iNat1736437.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/strowl1/iNat1537360.ogg': '/home/salman/Documents/data/download_corrupt/strowl1-iNat1537360.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/swtman1/iNat1468159.ogg': '/home/salman/Documents/data/download_corrupt/swtman1-iNat1468159.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/swtman1/iNat841931.ogg': '/home/salman/Documents/data/download_corrupt/swtman1-iNat841931.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/swtman1/iNat980195.ogg': '/home/salman/Documents/data/download_corrupt/swtman1-iNat980195.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/swtman1/iNat1647280.ogg': '/home/salman/Documents/data/download_corrupt/swtman1-iNat1647280.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/swtman1/iNat1420444.ogg': '/home/salman/Documents/data/download_corrupt/swtman1-iNat1420444.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/swtman1/iNat1664402.ogg': '/home/salman/Documents/data/download_corrupt/swtman1-iNat1664402.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/swtman1/iNat1667664.ogg': '/home/salman/Documents/data/download_corrupt/swtman1-iNat1667664.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/tattin1/iNat1291008.ogg': '/home/salman/Documents/data/download_corrupt/tattin1-iNat1291008.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/thlwre1/iNat1446997.ogg': '/home/salman/Documents/data/download_corrupt/thlwre1-iNat1446997.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/thlwre1/iNat1540292.ogg': '/home/salman/Documents/data/download_corrupt/thlwre1-iNat1540292.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/toctou1/iNat1406213.ogg': '/home/salman/Documents/data/download_corrupt/toctou1-iNat1406213.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/trokin/iNat1543761.ogg': '/home/salman/Documents/data/download_corrupt/trokin-iNat1543761.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/trokin/iNat1088126.ogg': '/home/salman/Documents/data/download_corrupt/trokin-iNat1088126.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/trokin/iNat1631950.ogg': '/home/salman/Documents/data/download_corrupt/trokin-iNat1631950.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/trsowl/iNat1337876.ogg': '/home/salman/Documents/data/download_corrupt/trsowl-iNat1337876.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/trsowl/iNat1321621.ogg': '/home/salman/Documents/data/download_corrupt/trsowl-iNat1321621.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/trsowl/iNat1240859.ogg': '/home/salman/Documents/data/download_corrupt/trsowl-iNat1240859.mpga', '/home/salman/Documents/data/birdclef-2026/train_audio/trsowl/iNat1707373.ogg': '/home/salman/Documents/data/download_corrupt/trsowl-iNat1707373.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/trsowl/iNat1608858.ogg': '/home/salman/Documents/data/download_corrupt/trsowl-iNat1608858.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/varant1/iNat1227614.ogg': '/home/salman/Documents/data/download_corrupt/varant1-iNat1227614.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/wfwduc1/iNat1679287.ogg': '/home/salman/Documents/data/download_corrupt/wfwduc1-iNat1679287.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/wfwduc1/iNat1487538.ogg': '/home/salman/Documents/data/download_corrupt/wfwduc1-iNat1487538.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/whbwar2/iNat763637.ogg': '/home/salman/Documents/data/download_corrupt/whbwar2-iNat763637.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/whiwoo1/iNat1594296.ogg': '/home/salman/Documents/data/download_corrupt/whiwoo1-iNat1594296.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/whnjay1/iNat1404548.ogg': '/home/salman/Documents/data/download_corrupt/whnjay1-iNat1404548.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/whnjay1/iNat1199393.ogg': '/home/salman/Documents/data/download_corrupt/whnjay1-iNat1199393.mpga', '/home/salman/Documents/data/birdclef-2026/train_audio/whnjay1/iNat771603.ogg': '/home/salman/Documents/data/download_corrupt/whnjay1-iNat771603.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/whnjay1/iNat1636518.ogg': '/home/salman/Documents/data/download_corrupt/whnjay1-iNat1636518.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/whnjay1/iNat1651360.ogg': '/home/salman/Documents/data/download_corrupt/whnjay1-iNat1651360.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/whtdov/iNat1536547.ogg': '/home/salman/Documents/data/download_corrupt/whtdov-iNat1536547.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/whtdov/iNat1594270.ogg': '/home/salman/Documents/data/download_corrupt/whtdov-iNat1594270.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/whtdov/iNat1598157.ogg': '/home/salman/Documents/data/download_corrupt/whtdov-iNat1598157.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/y00678/iNat1461732.ogg': '/home/salman/Documents/data/download_corrupt/y00678-iNat1461732.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/y00678/iNat1593494.ogg': '/home/salman/Documents/data/download_corrupt/y00678-iNat1593494.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/y00678/iNat1397691.ogg': '/home/salman/Documents/data/download_corrupt/y00678-iNat1397691.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/yebela1/iNat1593008.ogg': '/home/salman/Documents/data/download_corrupt/yebela1-iNat1593008.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/yebela1/iNat1479050.ogg': '/home/salman/Documents/data/download_corrupt/yebela1-iNat1479050.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/yebela1/iNat1521944.ogg': '/home/salman/Documents/data/download_corrupt/yebela1-iNat1521944.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/yecpar/iNat1360878.ogg': '/home/salman/Documents/data/download_corrupt/yecpar-iNat1360878.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/yecpar/iNat1347445.ogg': '/home/salman/Documents/data/download_corrupt/yecpar-iNat1347445.mp3', '/home/salman/Documents/data/birdclef-2026/train_audio/yehcar1/iNat1268927.ogg': '/home/salman/Documents/data/download_corrupt/yehcar1-iNat1268927.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/yehcar1/iNat585409.ogg': '/home/salman/Documents/data/download_corrupt/yehcar1-iNat585409.m4a', '/home/salman/Documents/data/birdclef-2026/train_audio/yehcar1/iNat1701473.ogg': '/home/salman/Documents/data/download_corrupt/yehcar1-iNat1701473.m4a'}

FILE_MAP = {'stbwoo2/XC467895.ogg': 'stbwoo2-XC467895.ogg', '1161364/iNat1264238.ogg': '1161364-iNat1264238.ogg', '209233/iNat1545859.ogg': '209233-iNat1545859.ogg', '22956/iNat1693371.ogg': '22956-iNat1693371.ogg', '22973/iNat781822.ogg': '22973-iNat781822.ogg', '22973/iNat1353836.ogg': '22973-iNat1353836.ogg', '22973/iNat1460521.ogg': '22973-iNat1460521.ogg', '22973/iNat1645288.ogg': '22973-iNat1645288.ogg', '23158/iNat1322093.ogg': '23158-iNat1322093.ogg', '24279/iNat1306335.ogg': '24279-iNat1306335.ogg', '24279/iNat1435402.ogg': '24279-iNat1435402.ogg', '244024/iNat1219059.ogg': '244024-iNat1219059.ogg', '244024/iNat1583846.ogg': '244024-iNat1583846.ogg', '244024/iNat1573678.ogg': '244024-iNat1573678.ogg', '25092/iNat1645314.ogg': '25092-iNat1645314.ogg', '326272/iNat1299066.ogg': '326272-iNat1299066.ogg', '326272/iNat1303382.ogg': '326272-iNat1303382.ogg', '43435/iNat1054872.ogg': '43435-iNat1054872.ogg', '43435/iNat1243480.ogg': '43435-iNat1243480.ogg', '47144/iNat1717935.ogg': '47144-iNat1717935.ogg', '47144/iNat1346356.ogg': '47144-iNat1346356.ogg', '47144/iNat1346365.ogg': '47144-iNat1346365.ogg', '47144/iNat1317366.ogg': '47144-iNat1317366.ogg', '47144/iNat1559514.ogg': '47144-iNat1559514.ogg', '47144/iNat1191939.ogg': '47144-iNat1191939.ogg', '476521/iNat1648597.ogg': '476521-iNat1648597.ogg', '555146/iNat1375734.ogg': '555146-iNat1375734.ogg', '555146/iNat1375753.ogg': '555146-iNat1375753.ogg', '65377/iNat1372639.ogg': '65377-iNat1372639.ogg', '65377/iNat924044.ogg': '65377-iNat924044.ogg', '65377/iNat924035.ogg': '65377-iNat924035.ogg', '65377/iNat1676955.ogg': '65377-iNat1676955.ogg', '67107/iNat1635719.ogg': '67107-iNat1635719.ogg', 'ashgre1/iNat963674.ogg': 'ashgre1-iNat963674.ogg', 'ashgre1/iNat1400791.ogg': 'ashgre1-iNat1400791.ogg', 'baffal1/iNat1672327.ogg': 'baffal1-iNat1672327.ogg', 'baffal1/iNat1711622.ogg': 'baffal1-iNat1711622.ogg', 'banana/iNat1638891.ogg': 'banana-iNat1638891.ogg', 'banana/iNat1302882.ogg': 'banana-iNat1302882.ogg', 'banana/iNat1371833.ogg': 'banana-iNat1371833.ogg', 'banana/iNat335243.ogg': 'banana-iNat335243.ogg', 'banana/iNat1631602.ogg': 'banana-iNat1631602.ogg', 'banana/iNat1496209.ogg': 'banana-iNat1496209.ogg', 'banana/iNat1630115.ogg': 'banana-iNat1630115.ogg', 'barant1/iNat1654575.ogg': 'barant1-iNat1654575.ogg', 'barant1/iNat1418545.ogg': 'barant1-iNat1418545.ogg', 'barant1/iNat1738725.ogg': 'barant1-iNat1738725.ogg', 'barant1/iNat76423.ogg': 'barant1-iNat76423.ogg', 'batbel1/iNat851301.ogg': 'batbel1-iNat851301.ogg', 'batbel1/iNat851302.ogg': 'batbel1-iNat851302.ogg', 'batbel1/iNat851299.ogg': 'batbel1-iNat851299.ogg', 'batbel1/iNat1275000.ogg': 'batbel1-iNat1275000.ogg', 'batbel1/iNat1517987.ogg': 'batbel1-iNat1517987.ogg', 'batbel1/iNat1710152.ogg': 'batbel1-iNat1710152.ogg', 'baymac/iNat1304419.ogg': 'baymac-iNat1304419.ogg', 'baymac/iNat976078.ogg': 'baymac-iNat976078.ogg', 'bbwduc/iNat1318531.ogg': 'bbwduc-iNat1318531.ogg', 'bbwduc/iNat942901.ogg': 'bbwduc-iNat942901.ogg', 'bbwduc/iNat1294916.ogg': 'bbwduc-iNat1294916.ogg', 'bbwduc/iNat1338852.ogg': 'bbwduc-iNat1338852.ogg', 'bbwduc/iNat1499546.ogg': 'bbwduc-iNat1499546.ogg', 'bbwduc/iNat1352566.ogg': 'bbwduc-iNat1352566.ogg', 'bbwduc/iNat1543298.ogg': 'bbwduc-iNat1543298.ogg', 'bbwduc/iNat1683874.ogg': 'bbwduc-iNat1683874.ogg', 'bbwduc/iNat1580446.ogg': 'bbwduc-iNat1580446.ogg', 'bbwduc/iNat418728.ogg': 'bbwduc-iNat418728.ogg', 'bbwduc/iNat797291.ogg': 'bbwduc-iNat797291.ogg', 'bbwduc/iNat950353.ogg': 'bbwduc-iNat950353.ogg', 'bbwduc/iNat1333153.ogg': 'bbwduc-iNat1333153.ogg', 'bbwduc/iNat594163.ogg': 'bbwduc-iNat594163.ogg', 'bbwduc/iNat1520789.ogg': 'bbwduc-iNat1520789.ogg', 'bbwduc/iNat1705504.ogg': 'bbwduc-iNat1705504.ogg', 'bkcdon/iNat1637377.ogg': 'bkcdon-iNat1637377.ogg', 'bkcdon/iNat1396398.ogg': 'bkcdon-iNat1396398.ogg', 'bkhpar/iNat1637590.ogg': 'bkhpar-iNat1637590.ogg', 'bkhpar/iNat1029272.ogg': 'bkhpar-iNat1029272.ogg', 'blheag1/iNat1675853.ogg': 'blheag1-iNat1675853.ogg', 'blheag1/iNat953708.ogg': 'blheag1-iNat953708.ogg', 'bncfly/iNat1422961.ogg': 'bncfly-iNat1422961.ogg', 'bncfly/iNat1406256.ogg': 'bncfly-iNat1406256.ogg', 'bncfly/iNat1457501.ogg': 'bncfly-iNat1457501.ogg', 'bncfly/iNat1554596.ogg': 'bncfly-iNat1554596.ogg', 'bobfly1/iNat1691483.ogg': 'bobfly1-iNat1691483.ogg', 'bobfly1/iNat1200017.ogg': 'bobfly1-iNat1200017.ogg', 'bobfly1/iNat1556528.ogg': 'bobfly1-iNat1556528.ogg', 'bobfly1/iNat1487398.ogg': 'bobfly1-iNat1487398.ogg', 'brcmar1/iNat1730049.ogg': 'brcmar1-iNat1730049.ogg', 'brcmar1/iNat1658256.ogg': 'brcmar1-iNat1658256.ogg', 'brcmar1/iNat1737157.ogg': 'brcmar1-iNat1737157.ogg', 'brnowl/iNat1480534.ogg': 'brnowl-iNat1480534.ogg', 'brnowl/iNat1706506.ogg': 'brnowl-iNat1706506.ogg', 'brnowl/iNat1610861.ogg': 'brnowl-iNat1610861.ogg', 'brnowl/iNat514729.ogg': 'brnowl-iNat514729.ogg', 'brnowl/iNat1491227.ogg': 'brnowl-iNat1491227.ogg', 'brnowl/iNat1659173.ogg': 'brnowl-iNat1659173.ogg', 'brnowl/iNat1309637.ogg': 'brnowl-iNat1309637.ogg', 'brnowl/iNat1548013.ogg': 'brnowl-iNat1548013.ogg', 'brnowl/iNat1050844.ogg': 'brnowl-iNat1050844.ogg', 'brnowl/iNat1491232.ogg': 'brnowl-iNat1491232.ogg', 'bufpar/iNat1295642.ogg': 'bufpar-iNat1295642.ogg', 'bufpar/iNat1299514.ogg': 'bufpar-iNat1299514.ogg', 'burowl/iNat1589934.ogg': 'burowl-iNat1589934.ogg', 'camfli1/iNat1336230.ogg': 'camfli1-iNat1336230.ogg', 'chobla1/iNat228765.ogg': 'chobla1-iNat228765.ogg', 'chobla1/iNat1428711.ogg': 'chobla1-iNat1428711.ogg', 'chobla1/iNat1424302.ogg': 'chobla1-iNat1424302.ogg', 'chobla1/iNat1540294.ogg': 'chobla1-iNat1540294.ogg', 'coffal1/iNat1710475.ogg': 'coffal1-iNat1710475.ogg', 'coffal1/iNat782270.ogg': 'coffal1-iNat782270.ogg', 'coffal1/iNat905814.ogg': 'coffal1-iNat905814.ogg', 'coffal1/iNat826415.ogg': 'coffal1-iNat826415.ogg', 'coffal1/iNat1167591.ogg': 'coffal1-iNat1167591.ogg', 'coffal1/iNat1637929.ogg': 'coffal1-iNat1637929.ogg', 'coffal1/iNat782291.ogg': 'coffal1-iNat782291.ogg', 'coffal1/iNat395438.ogg': 'coffal1-iNat395438.ogg', 'compau/iNat1591339.ogg': 'compau-iNat1591339.ogg', 'compau/iNat946279.ogg': 'compau-iNat946279.ogg', 'compau/iNat1599244.ogg': 'compau-iNat1599244.ogg', 'compau/iNat1672503.ogg': 'compau-iNat1672503.ogg', 'compau/iNat1268738.ogg': 'compau-iNat1268738.ogg', 'compau/iNat1623767.ogg': 'compau-iNat1623767.ogg', 'compau/iNat1321681.ogg': 'compau-iNat1321681.ogg', 'compau/iNat1294212.ogg': 'compau-iNat1294212.ogg', 'compot1/iNat1668960.ogg': 'compot1-iNat1668960.ogg', 'compot1/iNat1660624.ogg': 'compot1-iNat1660624.ogg', 'crbthr1/iNat1693777.ogg': 'crbthr1-iNat1693777.ogg', 'crbthr1/iNat1684518.ogg': 'crbthr1-iNat1684518.ogg', 'crbthr1/iNat1678524.ogg': 'crbthr1-iNat1678524.ogg', 'crbthr1/iNat1277382.ogg': 'crbthr1-iNat1277382.ogg', 'epaori4/iNat1592245.ogg': 'epaori4-iNat1592245.ogg', 'epaori4/iNat649978.ogg': 'epaori4-iNat649978.ogg', 'eulfly1/iNat1738901.ogg': 'eulfly1-iNat1738901.ogg', 'fepowl/iNat1711295.ogg': 'fepowl-iNat1711295.ogg', 'fepowl/iNat1664968.ogg': 'fepowl-iNat1664968.ogg', 'fepowl/iNat1308138.ogg': 'fepowl-iNat1308138.ogg', 'fepowl/iNat1738605.ogg': 'fepowl-iNat1738605.ogg', 'fepowl/iNat1240485.ogg': 'fepowl-iNat1240485.ogg', 'fepowl/iNat1335628.ogg': 'fepowl-iNat1335628.ogg', 'fepowl/iNat1287848.ogg': 'fepowl-iNat1287848.ogg', 'fotfly/iNat1193130.ogg': 'fotfly-iNat1193130.ogg', 'fusfly1/iNat1518620.ogg': 'fusfly1-iNat1518620.ogg', 'giwrai1/iNat1673888.ogg': 'giwrai1-iNat1673888.ogg', 'giwrai1/iNat1349850.ogg': 'giwrai1-iNat1349850.ogg', 'grasal3/iNat1632581.ogg': 'grasal3-iNat1632581.ogg', 'grasal3/iNat1644284.ogg': 'grasal3-iNat1644284.ogg', 'grasal3/iNat1614411.ogg': 'grasal3-iNat1614411.ogg', 'greant1/iNat1635481.ogg': 'greant1-iNat1635481.ogg', 'greant1/iNat1508328.ogg': 'greant1-iNat1508328.ogg', 'greant1/iNat936816.ogg': 'greant1-iNat936816.ogg', 'greela/iNat1231355.ogg': 'greela-iNat1231355.ogg', 'grekis/iNat1690035.ogg': 'grekis-iNat1690035.ogg', 'grekis/iNat1572002.ogg': 'grekis-iNat1572002.ogg', 'grekis/iNat1209312.ogg': 'grekis-iNat1209312.ogg', 'grekis/iNat1663561.ogg': 'grekis-iNat1663561.ogg', 'grekis/iNat1400476.ogg': 'grekis-iNat1400476.ogg', 'grekis/iNat1623199.ogg': 'grekis-iNat1623199.ogg', 'grekis/iNat1391832.ogg': 'grekis-iNat1391832.ogg', 'grekis/iNat1667823.ogg': 'grekis-iNat1667823.ogg', 'greyel/iNat1381842.ogg': 'greyel-iNat1381842.ogg', 'greyel/iNat1375792.ogg': 'greyel-iNat1375792.ogg', 'greyel/iNat1375793.ogg': 'greyel-iNat1375793.ogg', 'greyel/iNat1350689.ogg': 'greyel-iNat1350689.ogg', 'greyel/iNat1370909.ogg': 'greyel-iNat1370909.ogg', 'greyel/iNat1638552.ogg': 'greyel-iNat1638552.ogg', 'greyel/iNat952416.ogg': 'greyel-iNat952416.ogg', 'greyel/iNat1350614.ogg': 'greyel-iNat1350614.ogg', 'greyel/iNat1303954.ogg': 'greyel-iNat1303954.ogg', 'grfdov1/iNat1395710.ogg': 'grfdov1-iNat1395710.ogg', 'grfdov1/iNat1400824.ogg': 'grfdov1-iNat1400824.ogg', 'gycwor1/iNat1537449.ogg': 'gycwor1-iNat1537449.ogg', 'gycwor1/iNat1288203.ogg': 'gycwor1-iNat1288203.ogg', 'gycwor1/iNat1596768.ogg': 'gycwor1-iNat1596768.ogg', 'gycwor1/iNat816375.ogg': 'gycwor1-iNat816375.ogg', 'gycwor1/iNat1255088.ogg': 'gycwor1-iNat1255088.ogg', 'gycwor1/iNat1594836.ogg': 'gycwor1-iNat1594836.ogg', 'gycwor1/iNat1378299.ogg': 'gycwor1-iNat1378299.ogg', 'gycwor1/iNat1346486.ogg': 'gycwor1-iNat1346486.ogg', 'gycwor1/iNat1620374.ogg': 'gycwor1-iNat1620374.ogg', 'gycwor1/iNat1569899.ogg': 'gycwor1-iNat1569899.ogg', 'gycwor1/iNat1624903.ogg': 'gycwor1-iNat1624903.ogg', 'gycwor1/iNat1577300.ogg': 'gycwor1-iNat1577300.ogg', 'gycwor1/iNat1724472.ogg': 'gycwor1-iNat1724472.ogg', 'gycwor1/iNat1683695.ogg': 'gycwor1-iNat1683695.ogg', 'houspa/iNat1666148.ogg': 'houspa-iNat1666148.ogg', 'houspa/iNat1409352.ogg': 'houspa-iNat1409352.ogg', 'houspa/iNat1364301.ogg': 'houspa-iNat1364301.ogg', 'houspa/iNat1551547.ogg': 'houspa-iNat1551547.ogg', 'houspa/iNat935753.ogg': 'houspa-iNat935753.ogg', 'houspa/iNat1397767.ogg': 'houspa-iNat1397767.ogg', 'houspa/iNat1512573.ogg': 'houspa-iNat1512573.ogg', 'houspa/iNat1362595.ogg': 'houspa-iNat1362595.ogg', 'houspa/iNat1417357.ogg': 'houspa-iNat1417357.ogg', 'houspa/iNat1321989.ogg': 'houspa-iNat1321989.ogg', 'houspa/iNat409684.ogg': 'houspa-iNat409684.ogg', 'houspa/iNat1304457.ogg': 'houspa-iNat1304457.ogg', 'houspa/iNat1569993.ogg': 'houspa-iNat1569993.ogg', 'houspa/iNat1731791.ogg': 'houspa-iNat1731791.ogg', 'houspa/iNat1316764.ogg': 'houspa-iNat1316764.ogg', 'houspa/iNat1358970.ogg': 'houspa-iNat1358970.ogg', 'limpki/iNat1319758.ogg': 'limpki-iNat1319758.ogg', 'limpki/iNat1320813.ogg': 'limpki-iNat1320813.ogg', 'limpki/iNat1072786.ogg': 'limpki-iNat1072786.ogg', 'linwoo1/iNat1302630.ogg': 'linwoo1-iNat1302630.ogg', 'linwoo1/iNat1535721.ogg': 'linwoo1-iNat1535721.ogg', 'linwoo1/iNat1371736.ogg': 'linwoo1-iNat1371736.ogg', 'mabpar/iNat1626097.ogg': 'mabpar-iNat1626097.ogg', 'masgna1/iNat1635487.ogg': 'masgna1-iNat1635487.ogg', 'oliwoo1/iNat1346713.ogg': 'oliwoo1-iNat1346713.ogg', 'orwpar/iNat1687083.ogg': 'orwpar-iNat1687083.ogg', 'orwpar/iNat1355177.ogg': 'orwpar-iNat1355177.ogg', 'orwpar/iNat1503877.ogg': 'orwpar-iNat1503877.ogg', 'orwpar/iNat1657675.ogg': 'orwpar-iNat1657675.ogg', 'orwpar/iNat1079708.ogg': 'orwpar-iNat1079708.ogg', 'osprey/iNat226664.ogg': 'osprey-iNat226664.ogg', 'osprey/iNat1398129.ogg': 'osprey-iNat1398129.ogg', 'osprey/iNat1595562.ogg': 'osprey-iNat1595562.ogg', 'osprey/iNat1370949.ogg': 'osprey-iNat1370949.ogg', 'osprey/iNat1692289.ogg': 'osprey-iNat1692289.ogg', 'osprey/iNat1556374.ogg': 'osprey-iNat1556374.ogg', 'osprey/iNat1004549.ogg': 'osprey-iNat1004549.ogg', 'osprey/iNat1670343.ogg': 'osprey-iNat1670343.ogg', 'osprey/iNat288776.ogg': 'osprey-iNat288776.ogg', 'osprey/iNat482127.ogg': 'osprey-iNat482127.ogg', 'osprey/iNat1135797.ogg': 'osprey-iNat1135797.ogg', 'osprey/iNat1697529.ogg': 'osprey-iNat1697529.ogg', 'osprey/iNat1359848.ogg': 'osprey-iNat1359848.ogg', 'osprey/iNat1361039.ogg': 'osprey-iNat1361039.ogg', 'paltan1/iNat1709147.ogg': 'paltan1-iNat1709147.ogg', 'paltan1/iNat1418628.ogg': 'paltan1-iNat1418628.ogg', 'paltan1/iNat1418634.ogg': 'paltan1-iNat1418634.ogg', 'paltan1/iNat1618415.ogg': 'paltan1-iNat1618415.ogg', 'picpig2/iNat1607749.ogg': 'picpig2-iNat1607749.ogg', 'pirfly1/iNat1635054.ogg': 'pirfly1-iNat1635054.ogg', 'pirfly1/iNat1677277.ogg': 'pirfly1-iNat1677277.ogg', 'plcjay1/iNat911601.ogg': 'plcjay1-iNat911601.ogg', 'plcjay1/iNat1612345.ogg': 'plcjay1-iNat1612345.ogg', 'plcjay1/iNat1435256.ogg': 'plcjay1-iNat1435256.ogg', 'plcjay1/iNat1435257.ogg': 'plcjay1-iNat1435257.ogg', 'rebscy1/iNat1324031.ogg': 'rebscy1-iNat1324031.ogg', 'redjun/iNat1661079.ogg': 'redjun-iNat1661079.ogg', 'redjun/iNat1681112.ogg': 'redjun-iNat1681112.ogg', 'redjun/iNat953958.ogg': 'redjun-iNat953958.ogg', 'relser1/iNat1557442.ogg': 'relser1-iNat1557442.ogg', 'relser1/iNat1370757.ogg': 'relser1-iNat1370757.ogg', 'relser1/iNat1344314.ogg': 'relser1-iNat1344314.ogg', 'roahaw/iNat1677378.ogg': 'roahaw-iNat1677378.ogg', 'roahaw/iNat1458636.ogg': 'roahaw-iNat1458636.ogg', 'rubthr1/iNat870811.ogg': 'rubthr1-iNat870811.ogg', 'rubthr1/iNat1684073.ogg': 'rubthr1-iNat1684073.ogg', 'rubthr1/iNat852442.ogg': 'rubthr1-iNat852442.ogg', 'rubthr1/iNat1682587.ogg': 'rubthr1-iNat1682587.ogg', 'rubthr1/iNat1672514.ogg': 'rubthr1-iNat1672514.ogg', 'rubthr1/iNat546228.ogg': 'rubthr1-iNat546228.ogg', 'rubthr1/iNat850316.ogg': 'rubthr1-iNat850316.ogg', 'rubthr1/iNat1707784.ogg': 'rubthr1-iNat1707784.ogg', 'rubthr1/iNat1615216.ogg': 'rubthr1-iNat1615216.ogg', 'rubthr1/iNat851551.ogg': 'rubthr1-iNat851551.ogg', 'rubthr1/iNat1691551.ogg': 'rubthr1-iNat1691551.ogg', 'rubthr1/iNat1691430.ogg': 'rubthr1-iNat1691430.ogg', 'rufnig1/iNat1657250.ogg': 'rufnig1-iNat1657250.ogg', 'rumfly1/iNat1734627.ogg': 'rumfly1-iNat1734627.ogg', 'ruther1/iNat1483642.ogg': 'ruther1-iNat1483642.ogg', 'saffin/iNat1692175.ogg': 'saffin-iNat1692175.ogg', 'saffin/iNat1313823.ogg': 'saffin-iNat1313823.ogg', 'saffin/iNat1300076.ogg': 'saffin-iNat1300076.ogg', 'saffin/iNat1300148.ogg': 'saffin-iNat1300148.ogg', 'saffin/iNat1667770.ogg': 'saffin-iNat1667770.ogg', 'saffin/iNat1449859.ogg': 'saffin-iNat1449859.ogg', 'saytan1/iNat1677185.ogg': 'saytan1-iNat1677185.ogg', 'scadov1/iNat1299298.ogg': 'scadov1-iNat1299298.ogg', 'scadov1/iNat1491465.ogg': 'scadov1-iNat1491465.ogg', 'scadov1/iNat1276971.ogg': 'scadov1-iNat1276971.ogg', 'schpar1/iNat1293642.ogg': 'schpar1-iNat1293642.ogg', 'shcfly1/iNat1321023.ogg': 'shcfly1-iNat1321023.ogg', 'shcfly1/iNat1532661.ogg': 'shcfly1-iNat1532661.ogg', 'shcfly1/iNat1345739.ogg': 'shcfly1-iNat1345739.ogg', 'shcfly1/iNat1471076.ogg': 'shcfly1-iNat1471076.ogg', 'shshaw/iNat1590156.ogg': 'shshaw-iNat1590156.ogg', 'shshaw/iNat1602640.ogg': 'shshaw-iNat1602640.ogg', 'shtnig1/iNat869228.ogg': 'shtnig1-iNat869228.ogg', 'shtnig1/iNat870997.ogg': 'shtnig1-iNat870997.ogg', 'shtnig1/iNat870998.ogg': 'shtnig1-iNat870998.ogg', 'shtnig1/iNat1696713.ogg': 'shtnig1-iNat1696713.ogg', 'sibtan2/iNat1402979.ogg': 'sibtan2-iNat1402979.ogg', 'smbani/iNat915724.ogg': 'smbani-iNat915724.ogg', 'smbani/iNat1594767.ogg': 'smbani-iNat1594767.ogg', 'smbtin1/iNat1734628.ogg': 'smbtin1-iNat1734628.ogg', 'smbtin1/iNat81751.ogg': 'smbtin1-iNat81751.ogg', 'sobcac1/iNat1387094.ogg': 'sobcac1-iNat1387094.ogg', 'sobcac1/iNat1432132.ogg': 'sobcac1-iNat1432132.ogg', 'sobtyr1/iNat1718955.ogg': 'sobtyr1-iNat1718955.ogg', 'sobtyr1/iNat1355327.ogg': 'sobtyr1-iNat1355327.ogg', 'socfly1/iNat1701203.ogg': 'socfly1-iNat1701203.ogg', 'socfly1/iNat1685298.ogg': 'socfly1-iNat1685298.ogg', 'socfly1/iNat1705430.ogg': 'socfly1-iNat1705430.ogg', 'socfly1/iNat1687317.ogg': 'socfly1-iNat1687317.ogg', 'socfly1/iNat1181651.ogg': 'socfly1-iNat1181651.ogg', 'socfly1/iNat671916.ogg': 'socfly1-iNat671916.ogg', 'socfly1/iNat797558.ogg': 'socfly1-iNat797558.ogg', 'sofspi1/iNat1664377.ogg': 'sofspi1-iNat1664377.ogg', 'sofspi1/iNat1510202.ogg': 'sofspi1-iNat1510202.ogg', 'soulap1/iNat1203529.ogg': 'soulap1-iNat1203529.ogg', 'soulap1/iNat1405995.ogg': 'soulap1-iNat1405995.ogg', 'soulap1/iNat1637171.ogg': 'soulap1-iNat1637171.ogg', 'soulap1/iNat1637169.ogg': 'soulap1-iNat1637169.ogg', 'soulap1/iNat1685486.ogg': 'soulap1-iNat1685486.ogg', 'soulap1/iNat1434604.ogg': 'soulap1-iNat1434604.ogg', 'souscr1/iNat1244955.ogg': 'souscr1-iNat1244955.ogg', 'spbant3/iNat1695874.ogg': 'spbant3-iNat1695874.ogg', 'spispi1/iNat1503058.ogg': 'spispi1-iNat1503058.ogg', 'spispi1/iNat1374076.ogg': 'spispi1-iNat1374076.ogg', 'spispi1/iNat1456192.ogg': 'spispi1-iNat1456192.ogg', 'squcuc1/iNat1358561.ogg': 'squcuc1-iNat1358561.ogg', 'squcuc1/iNat1358573.ogg': 'squcuc1-iNat1358573.ogg', 'squcuc1/iNat188319.ogg': 'squcuc1-iNat188319.ogg', 'strcuc1/iNat1691050.ogg': 'strcuc1-iNat1691050.ogg', 'strcuc1/iNat1675976.ogg': 'strcuc1-iNat1675976.ogg', 'strcuc1/iNat1665191.ogg': 'strcuc1-iNat1665191.ogg', 'strcuc1/iNat1670795.ogg': 'strcuc1-iNat1670795.ogg', 'strcuc1/iNat1165584.ogg': 'strcuc1-iNat1165584.ogg', 'strcuc1/iNat1490053.ogg': 'strcuc1-iNat1490053.ogg', 'strcuc1/iNat1465517.ogg': 'strcuc1-iNat1465517.ogg', 'strcuc1/iNat1367996.ogg': 'strcuc1-iNat1367996.ogg', 'strcuc1/iNat1347727.ogg': 'strcuc1-iNat1347727.ogg', 'strowl1/iNat1451619.ogg': 'strowl1-iNat1451619.ogg', 'strowl1/iNat1736437.ogg': 'strowl1-iNat1736437.ogg', 'strowl1/iNat1537360.ogg': 'strowl1-iNat1537360.ogg', 'swtman1/iNat1468159.ogg': 'swtman1-iNat1468159.ogg', 'swtman1/iNat841931.ogg': 'swtman1-iNat841931.ogg', 'swtman1/iNat980195.ogg': 'swtman1-iNat980195.ogg', 'swtman1/iNat1647280.ogg': 'swtman1-iNat1647280.ogg', 'swtman1/iNat1420444.ogg': 'swtman1-iNat1420444.ogg', 'swtman1/iNat1664402.ogg': 'swtman1-iNat1664402.ogg', 'swtman1/iNat1667664.ogg': 'swtman1-iNat1667664.ogg', 'tattin1/iNat1291008.ogg': 'tattin1-iNat1291008.ogg', 'thlwre1/iNat1446997.ogg': 'thlwre1-iNat1446997.ogg', 'thlwre1/iNat1540292.ogg': 'thlwre1-iNat1540292.ogg', 'toctou1/iNat1406213.ogg': 'toctou1-iNat1406213.ogg', 'trokin/iNat1543761.ogg': 'trokin-iNat1543761.ogg', 'trokin/iNat1088126.ogg': 'trokin-iNat1088126.ogg', 'trokin/iNat1631950.ogg': 'trokin-iNat1631950.ogg', 'trsowl/iNat1337876.ogg': 'trsowl-iNat1337876.ogg', 'trsowl/iNat1321621.ogg': 'trsowl-iNat1321621.ogg', 'trsowl/iNat1240859.ogg': 'trsowl-iNat1240859.ogg', 'trsowl/iNat1707373.ogg': 'trsowl-iNat1707373.ogg', 'trsowl/iNat1608858.ogg': 'trsowl-iNat1608858.ogg', 'varant1/iNat1227614.ogg': 'varant1-iNat1227614.ogg', 'wfwduc1/iNat1679287.ogg': 'wfwduc1-iNat1679287.ogg', 'wfwduc1/iNat1487538.ogg': 'wfwduc1-iNat1487538.ogg', 'whbwar2/iNat763637.ogg': 'whbwar2-iNat763637.ogg', 'whiwoo1/iNat1594296.ogg': 'whiwoo1-iNat1594296.ogg', 'whnjay1/iNat1404548.ogg': 'whnjay1-iNat1404548.ogg', 'whnjay1/iNat1199393.ogg': 'whnjay1-iNat1199393.ogg', 'whnjay1/iNat771603.ogg': 'whnjay1-iNat771603.ogg', 'whnjay1/iNat1636518.ogg': 'whnjay1-iNat1636518.ogg', 'whnjay1/iNat1651360.ogg': 'whnjay1-iNat1651360.ogg', 'whtdov/iNat1536547.ogg': 'whtdov-iNat1536547.ogg', 'whtdov/iNat1594270.ogg': 'whtdov-iNat1594270.ogg', 'whtdov/iNat1598157.ogg': 'whtdov-iNat1598157.ogg', 'y00678/iNat1461732.ogg': 'y00678-iNat1461732.ogg', 'y00678/iNat1593494.ogg': 'y00678-iNat1593494.ogg', 'y00678/iNat1397691.ogg': 'y00678-iNat1397691.ogg', 'yebela1/iNat1593008.ogg': 'yebela1-iNat1593008.ogg', 'yebela1/iNat1479050.ogg': 'yebela1-iNat1479050.ogg', 'yebela1/iNat1521944.ogg': 'yebela1-iNat1521944.ogg', 'yecpar/iNat1360878.ogg': 'yecpar-iNat1360878.ogg', 'yecpar/iNat1347445.ogg': 'yecpar-iNat1347445.ogg', 'yehcar1/iNat1268927.ogg': 'yehcar1-iNat1268927.ogg', 'yehcar1/iNat585409.ogg': 'yehcar1-iNat585409.ogg', 'yehcar1/iNat1701473.ogg': 'yehcar1-iNat1701473.ogg'}
PATH_MAP = {'/home/salman/Documents/data/birdclef-2026/train_audio/stbwoo2/XC467895.ogg': '/home/salman/Documents/data/download_corrupt/stbwoo2-XC467895.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/1161364/iNat1264238.ogg': '/home/salman/Documents/data/download_corrupt/1161364-iNat1264238.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/209233/iNat1545859.ogg': '/home/salman/Documents/data/download_corrupt/209233-iNat1545859.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/22956/iNat1693371.ogg': '/home/salman/Documents/data/download_corrupt/22956-iNat1693371.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/22973/iNat781822.ogg': '/home/salman/Documents/data/download_corrupt/22973-iNat781822.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/22973/iNat1353836.ogg': '/home/salman/Documents/data/download_corrupt/22973-iNat1353836.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/22973/iNat1460521.ogg': '/home/salman/Documents/data/download_corrupt/22973-iNat1460521.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/22973/iNat1645288.ogg': '/home/salman/Documents/data/download_corrupt/22973-iNat1645288.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/23158/iNat1322093.ogg': '/home/salman/Documents/data/download_corrupt/23158-iNat1322093.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/24279/iNat1306335.ogg': '/home/salman/Documents/data/download_corrupt/24279-iNat1306335.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/24279/iNat1435402.ogg': '/home/salman/Documents/data/download_corrupt/24279-iNat1435402.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/244024/iNat1219059.ogg': '/home/salman/Documents/data/download_corrupt/244024-iNat1219059.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/244024/iNat1583846.ogg': '/home/salman/Documents/data/download_corrupt/244024-iNat1583846.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/244024/iNat1573678.ogg': '/home/salman/Documents/data/download_corrupt/244024-iNat1573678.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/25092/iNat1645314.ogg': '/home/salman/Documents/data/download_corrupt/25092-iNat1645314.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/326272/iNat1299066.ogg': '/home/salman/Documents/data/download_corrupt/326272-iNat1299066.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/326272/iNat1303382.ogg': '/home/salman/Documents/data/download_corrupt/326272-iNat1303382.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/43435/iNat1054872.ogg': '/home/salman/Documents/data/download_corrupt/43435-iNat1054872.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/43435/iNat1243480.ogg': '/home/salman/Documents/data/download_corrupt/43435-iNat1243480.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/47144/iNat1717935.ogg': '/home/salman/Documents/data/download_corrupt/47144-iNat1717935.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/47144/iNat1346356.ogg': '/home/salman/Documents/data/download_corrupt/47144-iNat1346356.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/47144/iNat1346365.ogg': '/home/salman/Documents/data/download_corrupt/47144-iNat1346365.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/47144/iNat1317366.ogg': '/home/salman/Documents/data/download_corrupt/47144-iNat1317366.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/47144/iNat1559514.ogg': '/home/salman/Documents/data/download_corrupt/47144-iNat1559514.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/47144/iNat1191939.ogg': '/home/salman/Documents/data/download_corrupt/47144-iNat1191939.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/476521/iNat1648597.ogg': '/home/salman/Documents/data/download_corrupt/476521-iNat1648597.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/555146/iNat1375734.ogg': '/home/salman/Documents/data/download_corrupt/555146-iNat1375734.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/555146/iNat1375753.ogg': '/home/salman/Documents/data/download_corrupt/555146-iNat1375753.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/65377/iNat1372639.ogg': '/home/salman/Documents/data/download_corrupt/65377-iNat1372639.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/65377/iNat924044.ogg': '/home/salman/Documents/data/download_corrupt/65377-iNat924044.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/65377/iNat924035.ogg': '/home/salman/Documents/data/download_corrupt/65377-iNat924035.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/65377/iNat1676955.ogg': '/home/salman/Documents/data/download_corrupt/65377-iNat1676955.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/67107/iNat1635719.ogg': '/home/salman/Documents/data/download_corrupt/67107-iNat1635719.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/ashgre1/iNat963674.ogg': '/home/salman/Documents/data/download_corrupt/ashgre1-iNat963674.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/ashgre1/iNat1400791.ogg': '/home/salman/Documents/data/download_corrupt/ashgre1-iNat1400791.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/baffal1/iNat1672327.ogg': '/home/salman/Documents/data/download_corrupt/baffal1-iNat1672327.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/baffal1/iNat1711622.ogg': '/home/salman/Documents/data/download_corrupt/baffal1-iNat1711622.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/banana/iNat1638891.ogg': '/home/salman/Documents/data/download_corrupt/banana-iNat1638891.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/banana/iNat1302882.ogg': '/home/salman/Documents/data/download_corrupt/banana-iNat1302882.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/banana/iNat1371833.ogg': '/home/salman/Documents/data/download_corrupt/banana-iNat1371833.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/banana/iNat335243.ogg': '/home/salman/Documents/data/download_corrupt/banana-iNat335243.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/banana/iNat1631602.ogg': '/home/salman/Documents/data/download_corrupt/banana-iNat1631602.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/banana/iNat1496209.ogg': '/home/salman/Documents/data/download_corrupt/banana-iNat1496209.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/banana/iNat1630115.ogg': '/home/salman/Documents/data/download_corrupt/banana-iNat1630115.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/barant1/iNat1654575.ogg': '/home/salman/Documents/data/download_corrupt/barant1-iNat1654575.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/barant1/iNat1418545.ogg': '/home/salman/Documents/data/download_corrupt/barant1-iNat1418545.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/barant1/iNat1738725.ogg': '/home/salman/Documents/data/download_corrupt/barant1-iNat1738725.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/barant1/iNat76423.ogg': '/home/salman/Documents/data/download_corrupt/barant1-iNat76423.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/batbel1/iNat851301.ogg': '/home/salman/Documents/data/download_corrupt/batbel1-iNat851301.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/batbel1/iNat851302.ogg': '/home/salman/Documents/data/download_corrupt/batbel1-iNat851302.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/batbel1/iNat851299.ogg': '/home/salman/Documents/data/download_corrupt/batbel1-iNat851299.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/batbel1/iNat1275000.ogg': '/home/salman/Documents/data/download_corrupt/batbel1-iNat1275000.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/batbel1/iNat1517987.ogg': '/home/salman/Documents/data/download_corrupt/batbel1-iNat1517987.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/batbel1/iNat1710152.ogg': '/home/salman/Documents/data/download_corrupt/batbel1-iNat1710152.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/baymac/iNat1304419.ogg': '/home/salman/Documents/data/download_corrupt/baymac-iNat1304419.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/baymac/iNat976078.ogg': '/home/salman/Documents/data/download_corrupt/baymac-iNat976078.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1318531.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1318531.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat942901.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat942901.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1294916.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1294916.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1338852.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1338852.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1499546.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1499546.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1352566.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1352566.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1543298.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1543298.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1683874.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1683874.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1580446.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1580446.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat418728.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat418728.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat797291.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat797291.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat950353.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat950353.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1333153.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1333153.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat594163.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat594163.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1520789.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1520789.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bbwduc/iNat1705504.ogg': '/home/salman/Documents/data/download_corrupt/bbwduc-iNat1705504.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bkcdon/iNat1637377.ogg': '/home/salman/Documents/data/download_corrupt/bkcdon-iNat1637377.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bkcdon/iNat1396398.ogg': '/home/salman/Documents/data/download_corrupt/bkcdon-iNat1396398.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bkhpar/iNat1637590.ogg': '/home/salman/Documents/data/download_corrupt/bkhpar-iNat1637590.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bkhpar/iNat1029272.ogg': '/home/salman/Documents/data/download_corrupt/bkhpar-iNat1029272.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/blheag1/iNat1675853.ogg': '/home/salman/Documents/data/download_corrupt/blheag1-iNat1675853.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/blheag1/iNat953708.ogg': '/home/salman/Documents/data/download_corrupt/blheag1-iNat953708.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bncfly/iNat1422961.ogg': '/home/salman/Documents/data/download_corrupt/bncfly-iNat1422961.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bncfly/iNat1406256.ogg': '/home/salman/Documents/data/download_corrupt/bncfly-iNat1406256.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bncfly/iNat1457501.ogg': '/home/salman/Documents/data/download_corrupt/bncfly-iNat1457501.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bncfly/iNat1554596.ogg': '/home/salman/Documents/data/download_corrupt/bncfly-iNat1554596.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bobfly1/iNat1691483.ogg': '/home/salman/Documents/data/download_corrupt/bobfly1-iNat1691483.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bobfly1/iNat1200017.ogg': '/home/salman/Documents/data/download_corrupt/bobfly1-iNat1200017.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bobfly1/iNat1556528.ogg': '/home/salman/Documents/data/download_corrupt/bobfly1-iNat1556528.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bobfly1/iNat1487398.ogg': '/home/salman/Documents/data/download_corrupt/bobfly1-iNat1487398.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/brcmar1/iNat1730049.ogg': '/home/salman/Documents/data/download_corrupt/brcmar1-iNat1730049.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/brcmar1/iNat1658256.ogg': '/home/salman/Documents/data/download_corrupt/brcmar1-iNat1658256.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/brcmar1/iNat1737157.ogg': '/home/salman/Documents/data/download_corrupt/brcmar1-iNat1737157.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/brnowl/iNat1480534.ogg': '/home/salman/Documents/data/download_corrupt/brnowl-iNat1480534.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/brnowl/iNat1706506.ogg': '/home/salman/Documents/data/download_corrupt/brnowl-iNat1706506.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/brnowl/iNat1610861.ogg': '/home/salman/Documents/data/download_corrupt/brnowl-iNat1610861.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/brnowl/iNat514729.ogg': '/home/salman/Documents/data/download_corrupt/brnowl-iNat514729.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/brnowl/iNat1491227.ogg': '/home/salman/Documents/data/download_corrupt/brnowl-iNat1491227.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/brnowl/iNat1659173.ogg': '/home/salman/Documents/data/download_corrupt/brnowl-iNat1659173.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/brnowl/iNat1309637.ogg': '/home/salman/Documents/data/download_corrupt/brnowl-iNat1309637.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/brnowl/iNat1548013.ogg': '/home/salman/Documents/data/download_corrupt/brnowl-iNat1548013.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/brnowl/iNat1050844.ogg': '/home/salman/Documents/data/download_corrupt/brnowl-iNat1050844.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/brnowl/iNat1491232.ogg': '/home/salman/Documents/data/download_corrupt/brnowl-iNat1491232.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bufpar/iNat1295642.ogg': '/home/salman/Documents/data/download_corrupt/bufpar-iNat1295642.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/bufpar/iNat1299514.ogg': '/home/salman/Documents/data/download_corrupt/bufpar-iNat1299514.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/burowl/iNat1589934.ogg': '/home/salman/Documents/data/download_corrupt/burowl-iNat1589934.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/camfli1/iNat1336230.ogg': '/home/salman/Documents/data/download_corrupt/camfli1-iNat1336230.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/chobla1/iNat228765.ogg': '/home/salman/Documents/data/download_corrupt/chobla1-iNat228765.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/chobla1/iNat1428711.ogg': '/home/salman/Documents/data/download_corrupt/chobla1-iNat1428711.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/chobla1/iNat1424302.ogg': '/home/salman/Documents/data/download_corrupt/chobla1-iNat1424302.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/chobla1/iNat1540294.ogg': '/home/salman/Documents/data/download_corrupt/chobla1-iNat1540294.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/coffal1/iNat1710475.ogg': '/home/salman/Documents/data/download_corrupt/coffal1-iNat1710475.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/coffal1/iNat782270.ogg': '/home/salman/Documents/data/download_corrupt/coffal1-iNat782270.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/coffal1/iNat905814.ogg': '/home/salman/Documents/data/download_corrupt/coffal1-iNat905814.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/coffal1/iNat826415.ogg': '/home/salman/Documents/data/download_corrupt/coffal1-iNat826415.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/coffal1/iNat1167591.ogg': '/home/salman/Documents/data/download_corrupt/coffal1-iNat1167591.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/coffal1/iNat1637929.ogg': '/home/salman/Documents/data/download_corrupt/coffal1-iNat1637929.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/coffal1/iNat782291.ogg': '/home/salman/Documents/data/download_corrupt/coffal1-iNat782291.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/coffal1/iNat395438.ogg': '/home/salman/Documents/data/download_corrupt/coffal1-iNat395438.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/compau/iNat1591339.ogg': '/home/salman/Documents/data/download_corrupt/compau-iNat1591339.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/compau/iNat946279.ogg': '/home/salman/Documents/data/download_corrupt/compau-iNat946279.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/compau/iNat1599244.ogg': '/home/salman/Documents/data/download_corrupt/compau-iNat1599244.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/compau/iNat1672503.ogg': '/home/salman/Documents/data/download_corrupt/compau-iNat1672503.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/compau/iNat1268738.ogg': '/home/salman/Documents/data/download_corrupt/compau-iNat1268738.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/compau/iNat1623767.ogg': '/home/salman/Documents/data/download_corrupt/compau-iNat1623767.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/compau/iNat1321681.ogg': '/home/salman/Documents/data/download_corrupt/compau-iNat1321681.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/compau/iNat1294212.ogg': '/home/salman/Documents/data/download_corrupt/compau-iNat1294212.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/compot1/iNat1668960.ogg': '/home/salman/Documents/data/download_corrupt/compot1-iNat1668960.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/compot1/iNat1660624.ogg': '/home/salman/Documents/data/download_corrupt/compot1-iNat1660624.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/crbthr1/iNat1693777.ogg': '/home/salman/Documents/data/download_corrupt/crbthr1-iNat1693777.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/crbthr1/iNat1684518.ogg': '/home/salman/Documents/data/download_corrupt/crbthr1-iNat1684518.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/crbthr1/iNat1678524.ogg': '/home/salman/Documents/data/download_corrupt/crbthr1-iNat1678524.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/crbthr1/iNat1277382.ogg': '/home/salman/Documents/data/download_corrupt/crbthr1-iNat1277382.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/epaori4/iNat1592245.ogg': '/home/salman/Documents/data/download_corrupt/epaori4-iNat1592245.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/epaori4/iNat649978.ogg': '/home/salman/Documents/data/download_corrupt/epaori4-iNat649978.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/eulfly1/iNat1738901.ogg': '/home/salman/Documents/data/download_corrupt/eulfly1-iNat1738901.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/fepowl/iNat1711295.ogg': '/home/salman/Documents/data/download_corrupt/fepowl-iNat1711295.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/fepowl/iNat1664968.ogg': '/home/salman/Documents/data/download_corrupt/fepowl-iNat1664968.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/fepowl/iNat1308138.ogg': '/home/salman/Documents/data/download_corrupt/fepowl-iNat1308138.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/fepowl/iNat1738605.ogg': '/home/salman/Documents/data/download_corrupt/fepowl-iNat1738605.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/fepowl/iNat1240485.ogg': '/home/salman/Documents/data/download_corrupt/fepowl-iNat1240485.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/fepowl/iNat1335628.ogg': '/home/salman/Documents/data/download_corrupt/fepowl-iNat1335628.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/fepowl/iNat1287848.ogg': '/home/salman/Documents/data/download_corrupt/fepowl-iNat1287848.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/fotfly/iNat1193130.ogg': '/home/salman/Documents/data/download_corrupt/fotfly-iNat1193130.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/fusfly1/iNat1518620.ogg': '/home/salman/Documents/data/download_corrupt/fusfly1-iNat1518620.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/giwrai1/iNat1673888.ogg': '/home/salman/Documents/data/download_corrupt/giwrai1-iNat1673888.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/giwrai1/iNat1349850.ogg': '/home/salman/Documents/data/download_corrupt/giwrai1-iNat1349850.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/grasal3/iNat1632581.ogg': '/home/salman/Documents/data/download_corrupt/grasal3-iNat1632581.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/grasal3/iNat1644284.ogg': '/home/salman/Documents/data/download_corrupt/grasal3-iNat1644284.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/grasal3/iNat1614411.ogg': '/home/salman/Documents/data/download_corrupt/grasal3-iNat1614411.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/greant1/iNat1635481.ogg': '/home/salman/Documents/data/download_corrupt/greant1-iNat1635481.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/greant1/iNat1508328.ogg': '/home/salman/Documents/data/download_corrupt/greant1-iNat1508328.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/greant1/iNat936816.ogg': '/home/salman/Documents/data/download_corrupt/greant1-iNat936816.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/greela/iNat1231355.ogg': '/home/salman/Documents/data/download_corrupt/greela-iNat1231355.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/grekis/iNat1690035.ogg': '/home/salman/Documents/data/download_corrupt/grekis-iNat1690035.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/grekis/iNat1572002.ogg': '/home/salman/Documents/data/download_corrupt/grekis-iNat1572002.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/grekis/iNat1209312.ogg': '/home/salman/Documents/data/download_corrupt/grekis-iNat1209312.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/grekis/iNat1663561.ogg': '/home/salman/Documents/data/download_corrupt/grekis-iNat1663561.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/grekis/iNat1400476.ogg': '/home/salman/Documents/data/download_corrupt/grekis-iNat1400476.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/grekis/iNat1623199.ogg': '/home/salman/Documents/data/download_corrupt/grekis-iNat1623199.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/grekis/iNat1391832.ogg': '/home/salman/Documents/data/download_corrupt/grekis-iNat1391832.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/grekis/iNat1667823.ogg': '/home/salman/Documents/data/download_corrupt/grekis-iNat1667823.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/greyel/iNat1381842.ogg': '/home/salman/Documents/data/download_corrupt/greyel-iNat1381842.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/greyel/iNat1375792.ogg': '/home/salman/Documents/data/download_corrupt/greyel-iNat1375792.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/greyel/iNat1375793.ogg': '/home/salman/Documents/data/download_corrupt/greyel-iNat1375793.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/greyel/iNat1350689.ogg': '/home/salman/Documents/data/download_corrupt/greyel-iNat1350689.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/greyel/iNat1370909.ogg': '/home/salman/Documents/data/download_corrupt/greyel-iNat1370909.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/greyel/iNat1638552.ogg': '/home/salman/Documents/data/download_corrupt/greyel-iNat1638552.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/greyel/iNat952416.ogg': '/home/salman/Documents/data/download_corrupt/greyel-iNat952416.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/greyel/iNat1350614.ogg': '/home/salman/Documents/data/download_corrupt/greyel-iNat1350614.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/greyel/iNat1303954.ogg': '/home/salman/Documents/data/download_corrupt/greyel-iNat1303954.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/grfdov1/iNat1395710.ogg': '/home/salman/Documents/data/download_corrupt/grfdov1-iNat1395710.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/grfdov1/iNat1400824.ogg': '/home/salman/Documents/data/download_corrupt/grfdov1-iNat1400824.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1537449.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1537449.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1288203.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1288203.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1596768.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1596768.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat816375.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat816375.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1255088.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1255088.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1594836.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1594836.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1378299.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1378299.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1346486.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1346486.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1620374.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1620374.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1569899.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1569899.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1624903.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1624903.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1577300.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1577300.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1724472.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1724472.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/gycwor1/iNat1683695.ogg': '/home/salman/Documents/data/download_corrupt/gycwor1-iNat1683695.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1666148.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1666148.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1409352.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1409352.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1364301.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1364301.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1551547.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1551547.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat935753.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat935753.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1397767.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1397767.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1512573.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1512573.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1362595.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1362595.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1417357.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1417357.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1321989.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1321989.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat409684.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat409684.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1304457.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1304457.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1569993.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1569993.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1731791.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1731791.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1316764.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1316764.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/houspa/iNat1358970.ogg': '/home/salman/Documents/data/download_corrupt/houspa-iNat1358970.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/limpki/iNat1319758.ogg': '/home/salman/Documents/data/download_corrupt/limpki-iNat1319758.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/limpki/iNat1320813.ogg': '/home/salman/Documents/data/download_corrupt/limpki-iNat1320813.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/limpki/iNat1072786.ogg': '/home/salman/Documents/data/download_corrupt/limpki-iNat1072786.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/linwoo1/iNat1302630.ogg': '/home/salman/Documents/data/download_corrupt/linwoo1-iNat1302630.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/linwoo1/iNat1535721.ogg': '/home/salman/Documents/data/download_corrupt/linwoo1-iNat1535721.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/linwoo1/iNat1371736.ogg': '/home/salman/Documents/data/download_corrupt/linwoo1-iNat1371736.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/mabpar/iNat1626097.ogg': '/home/salman/Documents/data/download_corrupt/mabpar-iNat1626097.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/masgna1/iNat1635487.ogg': '/home/salman/Documents/data/download_corrupt/masgna1-iNat1635487.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/oliwoo1/iNat1346713.ogg': '/home/salman/Documents/data/download_corrupt/oliwoo1-iNat1346713.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/orwpar/iNat1687083.ogg': '/home/salman/Documents/data/download_corrupt/orwpar-iNat1687083.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/orwpar/iNat1355177.ogg': '/home/salman/Documents/data/download_corrupt/orwpar-iNat1355177.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/orwpar/iNat1503877.ogg': '/home/salman/Documents/data/download_corrupt/orwpar-iNat1503877.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/orwpar/iNat1657675.ogg': '/home/salman/Documents/data/download_corrupt/orwpar-iNat1657675.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/orwpar/iNat1079708.ogg': '/home/salman/Documents/data/download_corrupt/orwpar-iNat1079708.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat226664.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat226664.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1398129.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1398129.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1595562.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1595562.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1370949.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1370949.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1692289.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1692289.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1556374.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1556374.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1004549.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1004549.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1670343.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1670343.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat288776.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat288776.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat482127.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat482127.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1135797.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1135797.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1697529.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1697529.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1359848.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1359848.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/osprey/iNat1361039.ogg': '/home/salman/Documents/data/download_corrupt/osprey-iNat1361039.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/paltan1/iNat1709147.ogg': '/home/salman/Documents/data/download_corrupt/paltan1-iNat1709147.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/paltan1/iNat1418628.ogg': '/home/salman/Documents/data/download_corrupt/paltan1-iNat1418628.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/paltan1/iNat1418634.ogg': '/home/salman/Documents/data/download_corrupt/paltan1-iNat1418634.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/paltan1/iNat1618415.ogg': '/home/salman/Documents/data/download_corrupt/paltan1-iNat1618415.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/picpig2/iNat1607749.ogg': '/home/salman/Documents/data/download_corrupt/picpig2-iNat1607749.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/pirfly1/iNat1635054.ogg': '/home/salman/Documents/data/download_corrupt/pirfly1-iNat1635054.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/pirfly1/iNat1677277.ogg': '/home/salman/Documents/data/download_corrupt/pirfly1-iNat1677277.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/plcjay1/iNat911601.ogg': '/home/salman/Documents/data/download_corrupt/plcjay1-iNat911601.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/plcjay1/iNat1612345.ogg': '/home/salman/Documents/data/download_corrupt/plcjay1-iNat1612345.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/plcjay1/iNat1435256.ogg': '/home/salman/Documents/data/download_corrupt/plcjay1-iNat1435256.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/plcjay1/iNat1435257.ogg': '/home/salman/Documents/data/download_corrupt/plcjay1-iNat1435257.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/rebscy1/iNat1324031.ogg': '/home/salman/Documents/data/download_corrupt/rebscy1-iNat1324031.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/redjun/iNat1661079.ogg': '/home/salman/Documents/data/download_corrupt/redjun-iNat1661079.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/redjun/iNat1681112.ogg': '/home/salman/Documents/data/download_corrupt/redjun-iNat1681112.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/redjun/iNat953958.ogg': '/home/salman/Documents/data/download_corrupt/redjun-iNat953958.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/relser1/iNat1557442.ogg': '/home/salman/Documents/data/download_corrupt/relser1-iNat1557442.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/relser1/iNat1370757.ogg': '/home/salman/Documents/data/download_corrupt/relser1-iNat1370757.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/relser1/iNat1344314.ogg': '/home/salman/Documents/data/download_corrupt/relser1-iNat1344314.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/roahaw/iNat1677378.ogg': '/home/salman/Documents/data/download_corrupt/roahaw-iNat1677378.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/roahaw/iNat1458636.ogg': '/home/salman/Documents/data/download_corrupt/roahaw-iNat1458636.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat870811.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat870811.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat1684073.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat1684073.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat852442.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat852442.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat1682587.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat1682587.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat1672514.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat1672514.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat546228.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat546228.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat850316.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat850316.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat1707784.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat1707784.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat1615216.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat1615216.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat851551.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat851551.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat1691551.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat1691551.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/rubthr1/iNat1691430.ogg': '/home/salman/Documents/data/download_corrupt/rubthr1-iNat1691430.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/rufnig1/iNat1657250.ogg': '/home/salman/Documents/data/download_corrupt/rufnig1-iNat1657250.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/rumfly1/iNat1734627.ogg': '/home/salman/Documents/data/download_corrupt/rumfly1-iNat1734627.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/ruther1/iNat1483642.ogg': '/home/salman/Documents/data/download_corrupt/ruther1-iNat1483642.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/saffin/iNat1692175.ogg': '/home/salman/Documents/data/download_corrupt/saffin-iNat1692175.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/saffin/iNat1313823.ogg': '/home/salman/Documents/data/download_corrupt/saffin-iNat1313823.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/saffin/iNat1300076.ogg': '/home/salman/Documents/data/download_corrupt/saffin-iNat1300076.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/saffin/iNat1300148.ogg': '/home/salman/Documents/data/download_corrupt/saffin-iNat1300148.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/saffin/iNat1667770.ogg': '/home/salman/Documents/data/download_corrupt/saffin-iNat1667770.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/saffin/iNat1449859.ogg': '/home/salman/Documents/data/download_corrupt/saffin-iNat1449859.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/saytan1/iNat1677185.ogg': '/home/salman/Documents/data/download_corrupt/saytan1-iNat1677185.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/scadov1/iNat1299298.ogg': '/home/salman/Documents/data/download_corrupt/scadov1-iNat1299298.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/scadov1/iNat1491465.ogg': '/home/salman/Documents/data/download_corrupt/scadov1-iNat1491465.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/scadov1/iNat1276971.ogg': '/home/salman/Documents/data/download_corrupt/scadov1-iNat1276971.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/schpar1/iNat1293642.ogg': '/home/salman/Documents/data/download_corrupt/schpar1-iNat1293642.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/shcfly1/iNat1321023.ogg': '/home/salman/Documents/data/download_corrupt/shcfly1-iNat1321023.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/shcfly1/iNat1532661.ogg': '/home/salman/Documents/data/download_corrupt/shcfly1-iNat1532661.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/shcfly1/iNat1345739.ogg': '/home/salman/Documents/data/download_corrupt/shcfly1-iNat1345739.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/shcfly1/iNat1471076.ogg': '/home/salman/Documents/data/download_corrupt/shcfly1-iNat1471076.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/shshaw/iNat1590156.ogg': '/home/salman/Documents/data/download_corrupt/shshaw-iNat1590156.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/shshaw/iNat1602640.ogg': '/home/salman/Documents/data/download_corrupt/shshaw-iNat1602640.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/shtnig1/iNat869228.ogg': '/home/salman/Documents/data/download_corrupt/shtnig1-iNat869228.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/shtnig1/iNat870997.ogg': '/home/salman/Documents/data/download_corrupt/shtnig1-iNat870997.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/shtnig1/iNat870998.ogg': '/home/salman/Documents/data/download_corrupt/shtnig1-iNat870998.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/shtnig1/iNat1696713.ogg': '/home/salman/Documents/data/download_corrupt/shtnig1-iNat1696713.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/sibtan2/iNat1402979.ogg': '/home/salman/Documents/data/download_corrupt/sibtan2-iNat1402979.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/smbani/iNat915724.ogg': '/home/salman/Documents/data/download_corrupt/smbani-iNat915724.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/smbani/iNat1594767.ogg': '/home/salman/Documents/data/download_corrupt/smbani-iNat1594767.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/smbtin1/iNat1734628.ogg': '/home/salman/Documents/data/download_corrupt/smbtin1-iNat1734628.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/smbtin1/iNat81751.ogg': '/home/salman/Documents/data/download_corrupt/smbtin1-iNat81751.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/sobcac1/iNat1387094.ogg': '/home/salman/Documents/data/download_corrupt/sobcac1-iNat1387094.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/sobcac1/iNat1432132.ogg': '/home/salman/Documents/data/download_corrupt/sobcac1-iNat1432132.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/sobtyr1/iNat1718955.ogg': '/home/salman/Documents/data/download_corrupt/sobtyr1-iNat1718955.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/sobtyr1/iNat1355327.ogg': '/home/salman/Documents/data/download_corrupt/sobtyr1-iNat1355327.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/socfly1/iNat1701203.ogg': '/home/salman/Documents/data/download_corrupt/socfly1-iNat1701203.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/socfly1/iNat1685298.ogg': '/home/salman/Documents/data/download_corrupt/socfly1-iNat1685298.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/socfly1/iNat1705430.ogg': '/home/salman/Documents/data/download_corrupt/socfly1-iNat1705430.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/socfly1/iNat1687317.ogg': '/home/salman/Documents/data/download_corrupt/socfly1-iNat1687317.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/socfly1/iNat1181651.ogg': '/home/salman/Documents/data/download_corrupt/socfly1-iNat1181651.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/socfly1/iNat671916.ogg': '/home/salman/Documents/data/download_corrupt/socfly1-iNat671916.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/socfly1/iNat797558.ogg': '/home/salman/Documents/data/download_corrupt/socfly1-iNat797558.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/sofspi1/iNat1664377.ogg': '/home/salman/Documents/data/download_corrupt/sofspi1-iNat1664377.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/sofspi1/iNat1510202.ogg': '/home/salman/Documents/data/download_corrupt/sofspi1-iNat1510202.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/soulap1/iNat1203529.ogg': '/home/salman/Documents/data/download_corrupt/soulap1-iNat1203529.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/soulap1/iNat1405995.ogg': '/home/salman/Documents/data/download_corrupt/soulap1-iNat1405995.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/soulap1/iNat1637171.ogg': '/home/salman/Documents/data/download_corrupt/soulap1-iNat1637171.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/soulap1/iNat1637169.ogg': '/home/salman/Documents/data/download_corrupt/soulap1-iNat1637169.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/soulap1/iNat1685486.ogg': '/home/salman/Documents/data/download_corrupt/soulap1-iNat1685486.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/soulap1/iNat1434604.ogg': '/home/salman/Documents/data/download_corrupt/soulap1-iNat1434604.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/souscr1/iNat1244955.ogg': '/home/salman/Documents/data/download_corrupt/souscr1-iNat1244955.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/spbant3/iNat1695874.ogg': '/home/salman/Documents/data/download_corrupt/spbant3-iNat1695874.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/spispi1/iNat1503058.ogg': '/home/salman/Documents/data/download_corrupt/spispi1-iNat1503058.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/spispi1/iNat1374076.ogg': '/home/salman/Documents/data/download_corrupt/spispi1-iNat1374076.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/spispi1/iNat1456192.ogg': '/home/salman/Documents/data/download_corrupt/spispi1-iNat1456192.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/squcuc1/iNat1358561.ogg': '/home/salman/Documents/data/download_corrupt/squcuc1-iNat1358561.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/squcuc1/iNat1358573.ogg': '/home/salman/Documents/data/download_corrupt/squcuc1-iNat1358573.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/squcuc1/iNat188319.ogg': '/home/salman/Documents/data/download_corrupt/squcuc1-iNat188319.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/strcuc1/iNat1691050.ogg': '/home/salman/Documents/data/download_corrupt/strcuc1-iNat1691050.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/strcuc1/iNat1675976.ogg': '/home/salman/Documents/data/download_corrupt/strcuc1-iNat1675976.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/strcuc1/iNat1665191.ogg': '/home/salman/Documents/data/download_corrupt/strcuc1-iNat1665191.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/strcuc1/iNat1670795.ogg': '/home/salman/Documents/data/download_corrupt/strcuc1-iNat1670795.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/strcuc1/iNat1165584.ogg': '/home/salman/Documents/data/download_corrupt/strcuc1-iNat1165584.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/strcuc1/iNat1490053.ogg': '/home/salman/Documents/data/download_corrupt/strcuc1-iNat1490053.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/strcuc1/iNat1465517.ogg': '/home/salman/Documents/data/download_corrupt/strcuc1-iNat1465517.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/strcuc1/iNat1367996.ogg': '/home/salman/Documents/data/download_corrupt/strcuc1-iNat1367996.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/strcuc1/iNat1347727.ogg': '/home/salman/Documents/data/download_corrupt/strcuc1-iNat1347727.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/strowl1/iNat1451619.ogg': '/home/salman/Documents/data/download_corrupt/strowl1-iNat1451619.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/strowl1/iNat1736437.ogg': '/home/salman/Documents/data/download_corrupt/strowl1-iNat1736437.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/strowl1/iNat1537360.ogg': '/home/salman/Documents/data/download_corrupt/strowl1-iNat1537360.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/swtman1/iNat1468159.ogg': '/home/salman/Documents/data/download_corrupt/swtman1-iNat1468159.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/swtman1/iNat841931.ogg': '/home/salman/Documents/data/download_corrupt/swtman1-iNat841931.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/swtman1/iNat980195.ogg': '/home/salman/Documents/data/download_corrupt/swtman1-iNat980195.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/swtman1/iNat1647280.ogg': '/home/salman/Documents/data/download_corrupt/swtman1-iNat1647280.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/swtman1/iNat1420444.ogg': '/home/salman/Documents/data/download_corrupt/swtman1-iNat1420444.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/swtman1/iNat1664402.ogg': '/home/salman/Documents/data/download_corrupt/swtman1-iNat1664402.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/swtman1/iNat1667664.ogg': '/home/salman/Documents/data/download_corrupt/swtman1-iNat1667664.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/tattin1/iNat1291008.ogg': '/home/salman/Documents/data/download_corrupt/tattin1-iNat1291008.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/thlwre1/iNat1446997.ogg': '/home/salman/Documents/data/download_corrupt/thlwre1-iNat1446997.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/thlwre1/iNat1540292.ogg': '/home/salman/Documents/data/download_corrupt/thlwre1-iNat1540292.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/toctou1/iNat1406213.ogg': '/home/salman/Documents/data/download_corrupt/toctou1-iNat1406213.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/trokin/iNat1543761.ogg': '/home/salman/Documents/data/download_corrupt/trokin-iNat1543761.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/trokin/iNat1088126.ogg': '/home/salman/Documents/data/download_corrupt/trokin-iNat1088126.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/trokin/iNat1631950.ogg': '/home/salman/Documents/data/download_corrupt/trokin-iNat1631950.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/trsowl/iNat1337876.ogg': '/home/salman/Documents/data/download_corrupt/trsowl-iNat1337876.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/trsowl/iNat1321621.ogg': '/home/salman/Documents/data/download_corrupt/trsowl-iNat1321621.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/trsowl/iNat1240859.ogg': '/home/salman/Documents/data/download_corrupt/trsowl-iNat1240859.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/trsowl/iNat1707373.ogg': '/home/salman/Documents/data/download_corrupt/trsowl-iNat1707373.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/trsowl/iNat1608858.ogg': '/home/salman/Documents/data/download_corrupt/trsowl-iNat1608858.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/varant1/iNat1227614.ogg': '/home/salman/Documents/data/download_corrupt/varant1-iNat1227614.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/wfwduc1/iNat1679287.ogg': '/home/salman/Documents/data/download_corrupt/wfwduc1-iNat1679287.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/wfwduc1/iNat1487538.ogg': '/home/salman/Documents/data/download_corrupt/wfwduc1-iNat1487538.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/whbwar2/iNat763637.ogg': '/home/salman/Documents/data/download_corrupt/whbwar2-iNat763637.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/whiwoo1/iNat1594296.ogg': '/home/salman/Documents/data/download_corrupt/whiwoo1-iNat1594296.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/whnjay1/iNat1404548.ogg': '/home/salman/Documents/data/download_corrupt/whnjay1-iNat1404548.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/whnjay1/iNat1199393.ogg': '/home/salman/Documents/data/download_corrupt/whnjay1-iNat1199393.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/whnjay1/iNat771603.ogg': '/home/salman/Documents/data/download_corrupt/whnjay1-iNat771603.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/whnjay1/iNat1636518.ogg': '/home/salman/Documents/data/download_corrupt/whnjay1-iNat1636518.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/whnjay1/iNat1651360.ogg': '/home/salman/Documents/data/download_corrupt/whnjay1-iNat1651360.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/whtdov/iNat1536547.ogg': '/home/salman/Documents/data/download_corrupt/whtdov-iNat1536547.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/whtdov/iNat1594270.ogg': '/home/salman/Documents/data/download_corrupt/whtdov-iNat1594270.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/whtdov/iNat1598157.ogg': '/home/salman/Documents/data/download_corrupt/whtdov-iNat1598157.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/y00678/iNat1461732.ogg': '/home/salman/Documents/data/download_corrupt/y00678-iNat1461732.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/y00678/iNat1593494.ogg': '/home/salman/Documents/data/download_corrupt/y00678-iNat1593494.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/y00678/iNat1397691.ogg': '/home/salman/Documents/data/download_corrupt/y00678-iNat1397691.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/yebela1/iNat1593008.ogg': '/home/salman/Documents/data/download_corrupt/yebela1-iNat1593008.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/yebela1/iNat1479050.ogg': '/home/salman/Documents/data/download_corrupt/yebela1-iNat1479050.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/yebela1/iNat1521944.ogg': '/home/salman/Documents/data/download_corrupt/yebela1-iNat1521944.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/yecpar/iNat1360878.ogg': '/home/salman/Documents/data/download_corrupt/yecpar-iNat1360878.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/yecpar/iNat1347445.ogg': '/home/salman/Documents/data/download_corrupt/yecpar-iNat1347445.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/yehcar1/iNat1268927.ogg': '/home/salman/Documents/data/download_corrupt/yehcar1-iNat1268927.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/yehcar1/iNat585409.ogg': '/home/salman/Documents/data/download_corrupt/yehcar1-iNat585409.ogg', '/home/salman/Documents/data/birdclef-2026/train_audio/yehcar1/iNat1701473.ogg': '/home/salman/Documents/data/download_corrupt/yehcar1-iNat1701473.ogg'}


# %%
# =========================
# Standard Library
# =========================
import os
import gc
import json
import time
import random
import copy
import warnings

# =========================
# Core Libraries
# =========================
import numpy as np
import pandas as pd

# =========================
# PyTorch
# =========================
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torch.optim import AdamW
from torch.utils.data.sampler import WeightedRandomSampler
from torch.cuda.amp import GradScaler
from torch.optim.lr_scheduler import CosineAnnealingLR
from torchvision import transforms
from torchvision.transforms import v2

# =========================
# Audio Processing
# =========================
import torchaudio
import torchaudio.transforms as T
import librosa
import librosa.display
import soundfile as sf

# =========================
# Image Processing
# =========================
import cv2
from PIL import Image
import albumentations as A
import matplotlib.pyplot as plt

# =========================
# Augmentations
# =========================
import audiomentations as AA

# =========================
# ML / CV Utilities
# =========================
import timm
import sklearn
from sklearn.model_selection import StratifiedKFold, StratifiedGroupKFold
from sklearn import metrics

# =========================
# Training Utilities
# =========================
from tqdm import tqdm
from timm.scheduler import CosineLRScheduler
from IPython.display import Audio

import random

from torch.optim.swa_utils import AveragedModel

# %%

import pandas as pd
import numpy as np
import os
import torch
from tqdm import tqdm
import soundfile as sf
import json
import random
from sklearn import metrics

def set_seed(seed=42):
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.mps.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def metric(y_true, y_pred):
    # N x Classes
    non_missing_idx = np.sum(y_true, axis=0) != 0
    y_true = y_true[:, non_missing_idx]
    y_pred = y_pred[:, non_missing_idx]
    score = metrics.roc_auc_score(y_true, y_pred)
    return score

def seconds_to_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


# %%
# import utils

# %%
def df_prep(Config, calculate_duration = False):
    df = pd.read_csv(Config.data_dir + "train.csv")
    df["path"] = Config.data_dir + "train_audio/" + df['filename']
    df['filename'] = df['filename'].replace(FILE_MAP)
    df['path'] = df['path'].replace(PATH_MAP)
    
    if calculate_duration:
        total_duration = []
        for i, row in tqdm(df.iterrows(), total=df.shape[0]):
            with sf.SoundFile(row['path']) as sound_file:
                total_duration.append(sound_file.frames / sound_file.samplerate)
        df["total_duration"] = total_duration
        print ("Before Duration", df.shape)
        df = df[df["total_duration"] > 1].reset_index(drop=True)
        print ("After Duration Thresh", df.shape)
    else:
        df['total_duration'] = -1
    return df

# %%
def prepare_train_soundscape_dict(data_dir, seconds = [5, 10, 15, 20], overlap = False):
    train_soundscapes_df = pd.read_csv(os.path.join(data_dir, "train_soundscapes_labels.csv"))
    train_soundscapes_df = train_soundscapes_df.drop_duplicates().reset_index(drop=True)
    available_train_soundscapes = train_soundscapes_df['filename'].unique()
    print (len(available_train_soundscapes))
    soundscape_df_dict = {}
    for req_sec in seconds:
        over_all_soundscape_df = []
        for soundscape_fp in available_train_soundscapes:
            sub_df = train_soundscapes_df[train_soundscapes_df['filename'] == soundscape_fp]
            if sub_df.shape[0] != 12:
                continue
            chunk_label = []
            time_chunk_label = []
            for i in range(0, 60, 5):
                st = seconds_to_time(i)
                xdf = sub_df[sub_df['start'] == st]
                if xdf.shape[0] > 0:
                    primary_label = xdf['primary_label'].values[0]
                else:
                    primary_label = ""
                chunk_label.append(primary_label)
                time_chunk_label.append(i)
            small_df = pd.DataFrame()
            plabels = []
            start_time_sec = []
            if overlap:
                for i in range(0, len(chunk_label) - (req_sec//5) + 1):
                    plabel = chunk_label[i: i + (req_sec//5)]
                    plabel = ";".join(plabel)
                    plabels.append(plabel)
                    start_time_sec.append(time_chunk_label[i])
            else:
                for i in range(0, len(chunk_label), req_sec//5):
                    plabel = chunk_label[i: i + (req_sec//5)]
                    plabel = "#".join(plabel)
                    plabels.append(plabel)
                    start_time_sec.append(time_chunk_label[i])
            small_df['primary_label'] = plabels
            small_df['start_time'] = start_time_sec
            small_df["filename"] = soundscape_fp
            over_all_soundscape_df.append(small_df)
        over_all_soundscape_df = pd.concat(over_all_soundscape_df, ignore_index=True)
        print (req_sec, over_all_soundscape_df.shape)
        soundscape_df_dict[req_sec] = over_all_soundscape_df
    return soundscape_df_dict

# %%
print (Config.experiment_params.get("experiment_name"))

# %%
set_seed(Config.seed)

os.makedirs(Config.experiment_params.get("output_dir"), exist_ok=True)
os.makedirs(os.path.join(Config.experiment_params.get("output_dir"), Config.experiment_params.get("experiment_name")), exist_ok=True)


Config.train_soundscapes_dict = prepare_train_soundscape_dict(Config.data_dir, overlap=Config.overlap)
Config.perch_missings = ['116570', '1491113', '1595929', '25073', '47158son01', '47158son02', '47158son03', '47158son04', '47158son05', '47158son06', '47158son07', '47158son08', '47158son09', '47158son10', '47158son11', '47158son12', '47158son13', '47158son14', '47158son15', '47158son16', '47158son17', '47158son18', '47158son19', '47158son20', '47158son21', '47158son22', '47158son23', '47158son24', '47158son25', '516975', '74580']
Config.train_audio_missings = ['1491113', '25073', '47158son01', '47158son02', '47158son03', '47158son04', '47158son05', '47158son06', '47158son07', '47158son08', '47158son09', '47158son10', '47158son11', '47158son12', '47158son13', '47158son14', '47158son15', '47158son16', '47158son17', '47158son18', '47158son19', '47158son20', '47158son21', '47158son22', '47158son23', '47158son24', '47158son25', '517063']
Config.use_columns = ["filename", "primary_label", "secondary_labels", "path", "total_duration", "start_time", "training_candidate", "class_name", "is_soundscape"]


# %%
df = df_prep(Config, calculate_duration=Config.calculate_duration)
df["start_time"] = 0
df["training_candidate"] = True
df['is_soundscape'] = False
df = df[Config.use_columns]
df.head(2)

# %%
if Config.add_nocall:
    nocall_dir = os.path.join("/home/salman/Documents/data", "nocall")
    nocall_sub_dirs = os.listdir(nocall_dir)
    total_files = []
    for each in nocall_sub_dirs:
        files = os.listdir(os.path.join(nocall_dir, each))
        files = [os.path.join(nocall_dir, each, file) for file in files]
        np.random.shuffle(files)
        pick = len(files) // 2
        files = files[:pick]
        total_files.extend(files)
    nocall_df = pd.DataFrame()
    for each in Config.use_columns:
        nocall_df[each] = None
    nocall_df["path"] = total_files
    nocall_df["primary_label"] = "nocall"
    nocall_df["secondary_labels"] = "[]"
    nocall_df["is_soundscape"] = False
    print (nocall_df.shape)
    print (df.shape)
    df = pd.concat([df, nocall_df]).reset_index(drop=True)
    print (df.shape)

# %%
print (df.shape)
gkf = StratifiedKFold(n_splits=Config.n_folds, shuffle=True, random_state=Config.seed)
df['fold'] = -1
for ifold, (train_idx, val_idx) in enumerate(gkf.split(df, y=df['primary_label'])):
    df.loc[val_idx, 'fold'] = ifold
#Unseen Birds in Folds
bird_names = set(df.primary_label)
unseen_birds = []
for fold in range(Config.n_folds):
    bird_names_fold = set(df[df['fold']==fold].primary_label)
    unseen_bird = list(bird_names - bird_names_fold)
    print(f'fold{fold}: Unseen Birds - ', len(unseen_bird))
    unseen_birds.extend(unseen_bird)
unseen_birds = np.unique(unseen_birds)
print(f'Overall Unseen Birds - ', len(unseen_birds))
df.loc[df['primary_label'].isin(unseen_birds), 'fold'] = -1
train_df = df[df["fold"] != Config.fold]
val_df = df[df["fold"] == Config.fold].reset_index(drop=True)
train_df.shape, val_df.shape

# %%
# PICK_DURATION = Config.train_duration
PICK_DURATION = 10

train_soundscape_df = Config.train_soundscapes_dict[PICK_DURATION]
training_candidates = []
for i, row in train_soundscape_df.iterrows():
    plabels = row['primary_label'].split(";")
    include_training = False
    if len(plabels) > 0:
        plabels = np.unique(plabels).tolist()
    for label in plabels:
        if label in Config.train_audio_missings:
            include_training = True
    training_candidates.append(include_training)
train_soundscape_df["training_candidate"] = training_candidates
train_soundscape_df["secondary_labels"] = "[]"
train_soundscape_df["total_duration"] = 60
train_soundscape_df["class_name"] = ""
train_soundscape_df["is_soundscape"] = True
train_soundscape_df["path"] = Config.data_dir + "train_soundscapes/" + train_soundscape_df['filename']
train_soundscape_df = train_soundscape_df[Config.use_columns]
secondary_labels = []
for i, row in train_soundscape_df.iterrows():
    plabels = []
    for chunk_label in row['primary_label'].split("#"):
        _plabels = []
        for label in chunk_label.split(";"):
            if label != "":
                _plabels.append(label)
        _plabels = np.unique(_plabels).tolist()
        plabels.append(_plabels)
    secondary_labels.append(str(plabels))
train_soundscape_df["secondary_labels"] = secondary_labels
train_soundscape_df["primary_label"] = ""
train_soundscape_df["fold"] = -1

# %%
eval(train_soundscape_df['secondary_labels'].values[0])[0][0]

# %%
print (train_df.shape)
train_df = pd.concat([train_df, train_soundscape_df, val_df]).reset_index(drop=True)
print (train_df.shape)

# %%
print (train_soundscape_df.shape)

# %%
val_df = val_df[:1000]
 

class SSDataset(torch.utils.data.Dataset):
    def __init__(self):
        self.ss_df = pd.read_csv(os.path.join("../stage1/predictions_ss", "prediction_ss_ignored.csv"))
        print (self.ss_df.shape)
        print (self.ss_df.head()) 
        self.valid_soundscapes_weight = self.ss_df['sum_w']
        self.sample_rate = 32000
        self.duration = 20

    def max_norm_wave(self, wave):
        wave = np.array(wave)
        max_v = np.max(np.abs(wave))
        if max_v > 0:
            wave = wave/max_v
        return wave
    
    def __len__(self):
        return len(self.ss_df)
    
    def load_sample(self, filepath, sample_rate=32_000, res_type="kaiser_best"):
        wave, _ = librosa.load(filepath, sr=sample_rate, res_type=res_type, mono=True)
        return wave
    
    def load_ss_sample(self, idx):

        wave = self.load_sample(
                filepath=self.ss_df["ss_fp"].iloc[idx],
                sample_rate=self.sample_rate
            )
        wave_len = len(wave)

        duration_samples = int(self.duration * self.sample_rate)
        max_start = wave_len - duration_samples
        start = random.randint(0, max_start)
        wave = wave[start : start + duration_samples]
        wave = self.max_norm_wave(wave)


        start = start // self.sample_rate
        ps = np.load(os.path.join("../stage1/predictions_ss", self.ss_df["fp_w"].iloc[idx]))
        FRAME_WISE_PAD = 1
        start = start - FRAME_WISE_PAD
        if start < 0:
            start = 0
        end = start + self.duration
        end = end + FRAME_WISE_PAD
        ps = ps[start:end, :]
        ps = np.max(ps, axis=0)


        TEMPRATURE = (1 / 0.65)
        ps = ps ** TEMPRATURE

        aves = ps[0:162]
        insects = ps[162:162+28]
        amph = ps[162+28:162+28+36]
        mam = ps[162+28+36:162+28+36+9]

        rep = (amph[-1] + mam[-1]) / 2.0
        amph = amph[:-1]
        mam = mam[:-1]

        insects_idx = class_idx_mapping['Insecta'].copy()
        amph_idx = class_idx_mapping['Amphibia'].copy()
        mam_idx = class_idx_mapping['Mammalia'].copy()
        aves_idx = class_idx_mapping['Aves'].copy()

        target = np.zeros(235)
        target[insects_idx] = insects
        target[aves_idx] = aves
        target[amph_idx] = amph
        target[mam_idx] = mam
        target[1] = rep
        target[234] = 0

        wave = torch.tensor(wave, dtype=torch.float32)
        target = torch.tensor(target)

        return wave, target
    
    def __getitem__(self, idx):
        wave, target = self.load_ss_sample(idx)
        return {
            "wave": wave,
            "target": target
        }



# %%
class BirdClEF26Dataset(torch.utils.data.Dataset):
    """ 
    This class is used to load the raw signal data from the data directory.
    """
    def __init__(self,
                 df,
                 is_train,
                 params
                 ):
        self.df = df
        self.is_train = is_train
        self.params = params
        self.sample_rate = params.get('sample_rate')
        self.num_classes = params.get('num_classes')
        self.bird2id = params.get('bird2id')
        self.sampling_type = params.get("sampling_type")
        self.duration = params.get("duration")
        if self.is_train == False:
            self.sampling_type = "rms"
        self.PICK_DURATION = PICK_DURATION
        self.UNIQUE_N_SS = self.PICK_DURATION // 5
        self.insects_idx = class_idx_mapping['Insecta'].copy()
        self.amph_idx = class_idx_mapping['Amphibia'].copy()
        self.mam_idx = class_idx_mapping['Mammalia'].copy()
        self.aves_idx = class_idx_mapping['Aves'].copy()
        self.pad_type = "random"
        
    
    def __len__(self):
        return len(self.df)
    
    def load_sample(self, filepath, sample_rate=32_000, res_type="kaiser_best"):
        wave, _ = librosa.load(filepath, sr=sample_rate, res_type=res_type, mono=True)
        return wave

    def pad_if_needed(self, wave, expected_len, pad_type="random"):
        wave_init_len = wave.shape[0]

        if wave_init_len >= expected_len:
            return wave

        pad_len = expected_len - wave_init_len

        if pad_type == "random":
            padded_wave = np.zeros(expected_len, dtype=wave.dtype)
            insert_wave_start = np.random.randint(0, pad_len + 1)
            padded_wave[insert_wave_start: insert_wave_start + wave_init_len] = wave
            return padded_wave

        if pad_type == "left":
            return np.pad(wave, ((pad_len, 0)))

        elif pad_type == "right":
            return np.pad(wave, ((0, pad_len)))

        elif pad_type == "repeat":
            reps = int(np.ceil(expected_len / wave_init_len))
            repeated = np.tile(wave, reps)
            return repeated[:expected_len]

        else:
            raise ValueError(f"Unsupported pad_type: {pad_type}")

    def pick_random_sample(self, wave, duration_samples):
        wave_len = len(wave)
        if wave_len <= duration_samples:
            return wave, 0
        max_start = wave_len - duration_samples
        start = random.randint(0, max_start)
        return wave[start : start + duration_samples], start // self.sample_rate
        
    def pick_rms_sample(self, wave, duration_samples):
        stride = self.sample_rate
        max_rms = 0
        max_rms_start = 0
        for start in range(0, len(wave) - duration_samples + 1, stride):
            window = wave[start:start + duration_samples]
            rms = np.sqrt(np.mean(window ** 2))
            if rms > max_rms:
                max_rms = rms
                max_rms_start = start
        wave = wave[max_rms_start:max_rms_start + duration_samples]
        return wave
    
    def sample_wave(self, wave, duration, sampling_type):
        expected_len = int(duration * self.sample_rate)
        wave = self.pad_if_needed(wave, expected_len, pad_type=self.pad_type)
        if sampling_type == "rms":
            sample = self.pick_rms_sample(wave, expected_len)
        elif sampling_type == 'random':
            sample, start = self.pick_random_sample(wave, expected_len)
        else:
            raise ValueError(f"Unsupported sampling_type: {sampling_type}")
        if sample.shape[0] != expected_len:
            print (wave.shape)
        return sample, start

    def max_norm_wave(self, wave):
        wave = np.array(wave)
        max_v = np.max(np.abs(wave))
        if max_v > 0:
            wave = wave/max_v
        return wave

    def prepare_target(self, primary_label, secondary_labels):
        target = np.zeros(self.num_classes, dtype=np.float32)
        if primary_label != "":
            target[self.bird2id[primary_label]] = 1.0
        for label in secondary_labels:
            if label != "":
                target[self.bird2id[label]] = 1.0
        return target
    
    def prepare_wave(self, wave):
        sampling_type = self.sampling_type
        wave, start = self.sample_wave(
            wave=wave,
            duration=self.duration,
            sampling_type=sampling_type
        )
        wave = self.max_norm_wave(wave)
        return wave, start

        
    def __getitem__(self, idx):
        fp = self.df["path"].iloc[idx]
        primary_label = self.df["primary_label"].iloc[idx]
        secondary_labels = eval(self.df["secondary_labels"].iloc[idx])
        is_soundscape = self.df["is_soundscape"].iloc[idx]

        if is_soundscape:
            wave = self.load_sample(
                filepath=fp,
                sample_rate=self.sample_rate
            )
            if random.random() < 0.5:
                start_time = self.df["start_time"].iloc[idx]

                wave = wave[(start_time * self.sample_rate):((start_time + self.PICK_DURATION) * self.sample_rate)]
                expected_len = int(self.duration * self.sample_rate)
                wave = self.pad_if_needed(wave, expected_len, pad_type=self.pad_type)
                wave = self.max_norm_wave(wave)
                secondary_labels = np.concatenate(secondary_labels)
                secondary_labels = secondary_labels.flatten()
                secondary_labels = np.unique(secondary_labels).tolist()
                target = self.prepare_target(
                        primary_label=primary_label,
                        secondary_labels=secondary_labels
                    )
            else:
                start_time = self.df["start_time"].iloc[idx]
                random_chunk_idx = random.randint(0, self.UNIQUE_N_SS-1)
                start_time = start_time + (5 * random_chunk_idx)
                secondary_labels = secondary_labels[random_chunk_idx]
                wave = wave[(start_time * self.sample_rate):((start_time + 5) * self.sample_rate)]
                expected_len = int(self.duration * self.sample_rate)
                wave = self.pad_if_needed(wave, expected_len, pad_type=self.pad_type)
                wave = self.max_norm_wave(wave)
                target = self.prepare_target(
                        primary_label=primary_label,
                        secondary_labels=secondary_labels
                    )
                
        else:
            wave = self.load_sample(
                filepath=fp,
                sample_rate=self.sample_rate
            )
            wave = wave[:32000*60]
            wave, start = self.prepare_wave(wave)
        
            target = self.prepare_target(
                    primary_label=primary_label,
                    secondary_labels=secondary_labels
                )
            if target[234] < 0.5:
            
                np_name = ".".join(self.df["filename"].iloc[idx].replace("/", "-").split(".")[:-1]) + ".npy"
                ps = np.load(os.path.join("../stage0/predictions", np_name)) # SEQ_LEN x CLASSES
                if ps.shape[0] == 0:
                    print (idx)


                FRAME_WISE_PAD = 1
                start = start - FRAME_WISE_PAD
                if start < 0:
                    start = 0
                end = start + self.duration
                end = end + FRAME_WISE_PAD
                ps = ps[start:end, :]
                ps = np.max(ps, axis=0)

                TEMPRATURE = (1 / 0.6)

                ps = ps ** TEMPRATURE
                
                aves = ps[0:162]
                insects = ps[162:162+28]
                amph = ps[162+28:162+28+36]
                mam = ps[162+28+36:162+28+36+9]
                rep = (amph[-1] + mam[-1]) / 2.0
                amph = amph[:-1]
                mam = mam[:-1]


                mask = target[self.aves_idx] > 0.5
                p_mask = aves > 0.3
                mask = mask & p_mask #True where both True
                aves[mask] = (1 + aves[mask]) / 2.0

                mask = target[self.insects_idx] > 0.5
                p_mask = insects > 0.3
                mask = mask & p_mask #True where both True
                insects[mask] = (1 + insects[mask]) / 2.0


                mask = target[self.amph_idx] > 0.5
                p_mask = amph > 0.3
                mask = mask & p_mask #True where both True
                amph[mask] = (1 + amph[mask]) / 2.0


                mask = target[self.mam_idx] > 0.5
                p_mask = mam > 0.3
                mask = mask & p_mask #True where both True
                mam[mask] = (1 + mam[mask]) / 2.0

                target[1] = target[1] # rep # because recording is small and correct, so default label. ONly record exists.
                target[self.aves_idx] = aves
                target[self.insects_idx] = insects
                target[self.amph_idx] = amph
                target[self.mam_idx] = mam
            

        return {
            "wave": torch.tensor(wave, dtype=torch.float32),
            "target": torch.tensor(target)
        }



# %% [markdown]
# ### Spec

# %%
class MelSpectrogramTransform(nn.Module):
    def __init__(self, melspec_config, top_db, eps=1e-6,):
        super().__init__()

        aug = melspec_config.pop("aug")
        self.eps = eps
        self.top_db = top_db
        self.mel = T.MelSpectrogram(**melspec_config)
        self.db = T.AmplitudeToDB(stype="power", top_db=top_db)
        
        self.freq_mask = T.FrequencyMasking(freq_mask_param=aug["freq_mask_param"], iid_masks=True)
        self.time_mask = T.TimeMasking(time_mask_param=aug["time_mask_param"], iid_masks=True)
        self.num_masks = aug["num_masks"]

    @torch.no_grad()
    def forward(self, waveforms):
        X = self.db(self.mel(waveforms))
        mean = X.mean((1, 2), keepdim=True)
        std = X.std((1, 2), keepdim=True)
        Xstd = (X - mean) / (std + self.eps)
        norm_max = torch.amax(Xstd, dim=(1, 2), keepdim=True)
        norm_min = torch.amin(Xstd, dim=(1, 2), keepdim=True)
        X = (Xstd - norm_min) / (norm_max - norm_min + self.eps)

        if self.training:
            for _ in range(self.num_masks):
                X = self.freq_mask(X)
                X = self.time_mask(X)

        return X

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import timm


def init_layer(layer):
    nn.init.xavier_uniform_(layer.weight)
    if hasattr(layer, "bias"):
        if layer.bias is not None:
            layer.bias.data.fill_(0.)

def init_bn(bn):
    bn.bias.data.fill_(0.)
    bn.weight.data.fill_(1.0)

def init_weights(model):
    classname = model.__class__.__name__
    if classname.find("Conv2d") != -1:
        nn.init.xavier_uniform_(model.weight, gain=np.sqrt(2))
        model.bias.data.fill_(0)
    elif classname.find("BatchNorm") != -1:
        model.weight.data.normal_(1.0, 0.02)
        model.bias.data.fill_(0)
    elif classname.find("GRU") != -1:
        for weight in model.parameters():
            if len(weight.size()) > 1:
                nn.init.orthogonal_(weight.data)
    elif classname.find("Linear") != -1:
        model.weight.data.normal_(0, 0.01)
        model.bias.data.zero_()

def pad_framewise_output(framewise_output, frames_num):
    output = F.interpolate(
        framewise_output.unsqueeze(1),
        size=(frames_num, framewise_output.size(2)),
        align_corners=True,
        mode="bilinear").squeeze(1)

    return output

class AttBlock(nn.Module):
    def __init__(self,
                 in_features: int,
                 out_features: int,
                 activation="linear",
                 multiplier = 1,
                 temperature=1.0):
        super().__init__()


        self.fc1 = nn.Linear(in_features * multiplier, in_features, bias=True)
        self.activation = activation
        self.temperature = temperature
        self.att = nn.Conv1d(
            in_channels=in_features,
            out_channels=out_features,
            kernel_size=1,
            stride=1,
            padding=0,
            bias=True)
        self.cla = nn.Conv1d(
            in_channels=in_features,
            out_channels=out_features,
            kernel_size=1,
            stride=1,
            padding=0,
            bias=True)

        self.bn_att = nn.BatchNorm1d(out_features)
        self.init_weights()

    def init_weights(self):
        init_layer(self.att)
        init_layer(self.cla)
        init_bn(self.bn_att)
        init_layer(self.fc1)

    def forward(self, x, forward_drop_rate):
        x = F.relu_(self.fc1(x))
        x = x.transpose(1, 2)
        x = F.dropout(x, p=forward_drop_rate, training=self.training)
        # x: (n_samples, n_in, n_time)
        norm_att = torch.softmax(torch.clamp(self.att(x), -10, 10), dim=-1)
        cla = self.nonlinear_transform(self.cla(x))
        x = torch.sum(norm_att * cla, dim=2)
        return x, cla

    def nonlinear_transform(self, x):
        if self.activation == 'linear':
            return x
        elif self.activation == 'sigmoid':
            return torch.sigmoid(x)


def get_encoder(model_parameters):
    base_model = timm.create_model(
        model_parameters.get("backbone"),
        pretrained=model_parameters.get("pretrained"),
        in_chans=model_parameters.get("in_chans"),
        drop_rate=model_parameters.get("drop_rate"), #0.2
        drop_path_rate=model_parameters.get("drop_path_rate") #0.5
    )
    layers = list(base_model.children())[:-2]
    encoder = nn.Sequential(*layers)
    in_features = base_model.num_features
    return encoder, in_features


class BaseSEDModel(nn.Module):
    def __init__(self, model_parameters):
        super().__init__()
        self.forward_drop_rate = model_parameters.get("forward_drop_rate")
        self.bn0 = nn.BatchNorm2d(model_parameters.get("n_mels"))

        self.encoder, in_features = get_encoder(model_parameters)

        self.smoothings = model_parameters.get("smoothings")
        
        multiplier = len(self.smoothings)
        print ("Multiplier", multiplier)

        attn_heads = model_parameters.get("attn_heads")
        self.attn_head_names = list(attn_heads.keys())

        attn_head_layers = {}
        for each in self.attn_head_names:
            attn_head_layers[each] = AttBlock(in_features, attn_heads.get(each), activation="linear", multiplier=multiplier)
        self.attn_head_layers = nn.ModuleDict(attn_head_layers)

        self.init_weight()

    def init_weight(self):
        init_bn(self.bn0)

    def smooth_time(self, x, kernel_size):
        if kernel_size == 1:
            x = F.dropout(x, p=self.forward_drop_rate, training=self.training)
            x = x.transpose(1, 2)
        else:
            padding = (kernel_size - 1) // 2
            x1 = F.max_pool1d(x, kernel_size=kernel_size, stride=1, padding=padding)
            x2 = F.avg_pool1d(x, kernel_size=kernel_size, stride=1, padding=padding)
            x = x1 + x2
            x = F.dropout(x, p=self.forward_drop_rate, training=self.training)
            x = x.transpose(1, 2)
        return x

    def forward(self, x):
        x = x.transpose(1, 2)
        x = self.bn0(x)
        x = x.transpose(1, 2)

        x = self.encoder(x)
        
        x = torch.mean(x, dim=2) #BS X C X TIME

        if len(self.smoothings) == 1 and self.smoothings[0] == 1:
            features = self.smooth_time(x, 1)
        else:
            features = []
            for i in self.smoothings:
                features.append(self.smooth_time(x, i))
            features = torch.cat(features, dim=2)
        
        #BS X TIME X C*Multiplier
        outputs = {}
        for attn_head_name in self.attn_head_names:
            clip, frame = self.attn_head_layers[attn_head_name](features, self.forward_drop_rate)
            outputs[attn_head_name] = {
                "clip" : clip,
                "frame" : frame
            }

        return outputs

# %%
class SEDModel(nn.Module):
    def __init__(self, model_parameters, melspec_config):
        super().__init__()
        self.base_sed = BaseSEDModel(model_parameters)
        self.transform_ = MelSpectrogramTransform(melspec_config, top_db=80)

    
    @torch.no_grad()
    def transform(self, x):
        x = self.transform_(x).unsqueeze(1)
        x = torch.cat([x, x, x], dim=1)
        return x

    
    def forward(self, x):
        outputs = self.base_sed(x)
        return outputs


    def calculate_loss(self, output, insects_targets, amph_targets, mam_targets, aves_targets, criterion):

        clip_losses = [
            criterion(output["insecta"]["clip"], insects_targets),
            criterion(output["amph"]["clip"], amph_targets),
            criterion(output["mam"]["clip"], mam_targets),
            criterion(output["aves"]["clip"], aves_targets)
        ]

        frame_losses = [
            criterion(output["insecta"]["frame"].max(2)[0], insects_targets),
            criterion(output["amph"]["frame"].max(2)[0], amph_targets),
            criterion(output["mam"]["frame"].max(2)[0], mam_targets),
            criterion(output["aves"]["frame"].max(2)[0], aves_targets)
        ]

        loss1 = 0
        for i in range(4):
            loss1 += clip_losses[i]
        loss1 = 0.5 * loss1

        loss2 = 0
        for i in range(4):
            loss2 += frame_losses[i]
        loss2 = 0.5 * loss2

        loss = loss1 + loss2

        clip_losses_items = []
        frame_losses_items = []
        for i in range(4):
            clip_losses_items.append(round(clip_losses[i].detach().cpu().item(), 3))
            frame_losses_items.append(round(frame_losses[i].detach().cpu().item(), 3))


        return loss, clip_losses_items, frame_losses_items


def apply_mix(data, targets):
            # --- Mix 2 Samples (Original Logic) ---
    device = data.device
    lam = random.uniform(0.4, 0.6)
    indices = torch.randperm(data.size(0)).to(device)
    
    data2 = data[indices]
    targets2 = targets[indices]
    
    data = data * lam + data2 * (1 - lam)
    targets = torch.maximum(targets, targets2)
    return data, targets


def mixup(data, targets):
    
    data, targets = apply_mix(data, targets)
    # mask = targets[:, :234].sum(dim=1) > 0.5
    # targets[mask, 234] = 0

    TH = 0.25
    max_vals = targets[:, :234].max(dim=1).values
    mask = max_vals >= TH
    targets[mask, 234] = 0

    return data, targets



dataset = SSDataset()

ssdataloader = torch.utils.data.DataLoader(
    dataset,
    batch_size=Config.training_params['batch_size'],
    shuffle=True,
    num_workers=16,
    pin_memory=True,
    drop_last=True,
)

def infinite_loader(dataloader):
    while True:
        for batch in dataloader:
            yield batch

ssdataloader_inf = infinite_loader(ssdataloader)

def train_forward_pass(model, batch, scaler, criterion, device):
    mixed_precision = scaler is not None
    
    wave = batch['wave']
    target = batch['target']

    ss_batch = next(ssdataloader_inf)
    ss_wave = ss_batch['wave']
    ss_target = ss_batch['target']

    wave = torch.concat([wave, ss_wave], dim=0)
    target = torch.concat([target, ss_target], dim=0)

    wave, target = mixup(wave, target)

    insects_idx = class_idx_mapping['Insecta'].copy()
    amph_idx = class_idx_mapping['Amphibia'].copy()
    mam_idx = class_idx_mapping['Mammalia'].copy()
    aves_idx = class_idx_mapping['Aves'].copy()
    amph_idx.append(1)
    mam_idx.append(1)


    BS = len(target)
    insects_targets = torch.zeros(size=(BS, len(insects_idx)+1))
    amph_targets = torch.zeros(size=(BS, len(amph_idx)+1))
    mam_targets = torch.zeros(size=(BS, len(mam_idx)+1))
    aves_targets = torch.zeros(size=(BS, len(aves_idx)+1))


    insects_targets[:, :-1] = target[:, insects_idx]
    amph_targets[:, :-1] = target[:, amph_idx]
    mam_targets[:, :-1] = target[:, mam_idx]
    aves_targets[:, :-1] = target[:, aves_idx]

    # insects_targets[insects_targets[:, :-1].sum(dim=1) < 0.5, -1] = 1
    # amph_targets[amph_targets[:, :-1].sum(dim=1) < 0.5, -1] = 1
    # mam_targets[mam_targets[:, :-1].sum(dim=1) < 0.5, -1] = 1
    # aves_targets[aves_targets[:, :-1].sum(dim=1) < 0.5, -1] = 1


    TH = 0.25
    insects_targets[insects_targets[:, :-1].max(dim=1).values < TH, -1] = 1
    amph_targets[amph_targets[:, :-1].max(dim=1).values < TH, -1] = 1
    mam_targets[mam_targets[:, :-1].max(dim=1).values < TH, -1] = 1
    aves_targets[aves_targets[:, :-1].max(dim=1).values < TH, -1] = 1

    insects_targets = insects_targets.to(device)
    amph_targets = amph_targets.to(device)
    mam_targets = mam_targets.to(device)
    aves_targets = aves_targets.to(device)
    
    wave = wave.to(device)

    x = model.transform(wave)

    if mixed_precision:
        with torch.autocast(device_type=device):
            outputs = model(x)
            loss, clip_loss, frame_loss = model.calculate_loss(outputs, insects_targets, amph_targets, mam_targets, aves_targets, criterion)
    else:
        outputs = model(x)
        loss, clip_loss, frame_loss = model.calculate_loss(outputs, insects_targets, amph_targets, mam_targets, aves_targets, criterion)

    return loss, clip_loss, frame_loss



# %% [markdown]
# ## Training Loop

# %%
def train_epoch(model, loader, optimizer, scaler, params):

    criterion = params.get("criterion")
    accumulation_steps = params.get("accumulation_steps")
    gradient_clip = params.get("gradient_clip")
    device = params.get("device")
    
    model.train()
    train_loss = []
    optimizer.zero_grad()

    bar = tqdm(enumerate(loader), total=len(loader))
    for step, batch in bar:

        loss, clip_loss, frame_loss = train_forward_pass(
            model = model,
            batch=batch,
            scaler=scaler,
            criterion=criterion,
            device = device
        )
        
        loss_value = loss.detach().cpu().item()
        train_loss.append(loss_value)
        loss = loss / accumulation_steps

        if scaler is not None:
            scaler.scale(loss).backward()
            if ((step + 1) % accumulation_steps) == 0:
                scaler.unscale_(optimizer)
                if gradient_clip > 0:
                    nn.utils.clip_grad_norm_(model.parameters(), max_norm=gradient_clip, norm_type=2)
                scaler.step(optimizer)
                scaler.update()
                optimizer.zero_grad()
        else:
            loss.backward()
            if ((step + 1) % accumulation_steps) == 0:
                if gradient_clip > 0:
                    nn.utils.clip_grad_norm_(model.parameters(), max_norm=gradient_clip, norm_type=2)
                optimizer.step()
                optimizer.zero_grad()
        
        smooth_loss = sum(train_loss[-100:]) / min(len(train_loss), 100)
        bar.set_description(
    f'loss: {loss_value:.5f}, smth: {smooth_loss:.5f}, '
    f'cls: {[round(x, 5) for x in clip_loss]}, '
    f'seg: {[round(x, 5) for x in frame_loss]}'
)

    return np.mean(train_loss)

# %%

def worker_init_fn(worker_id):
    import cv2, torch
    cv2.setNumThreads(0)
    torch.set_num_threads(1)

    
def get_dataloaders(Config, train_df, val_df):
    if Config.training_params['debug']:
        train_df = train_df[:500]
        val_df = val_df[:500]
        
    batch_size = Config.training_params['batch_size']
    num_workers = Config.training_params['num_workers']
    
    
    train_dataset = BirdClEF26Dataset(train_df, is_train=True, params=Config.dataset_params)
    train_loader = torch.utils.data.DataLoader(train_dataset, shuffle=True, batch_size=batch_size, 
                                            drop_last=True, num_workers=num_workers, pin_memory=False,
                                            persistent_workers=True, prefetch_factor=2, worker_init_fn=worker_init_fn)

    return train_loader


def create_model_opt_sc(Config):
    model = SEDModel(Config.model_parameters, Config.melspec_parameters.copy())
    x = torch.randn((12, 32000*Config.dataset_params["duration"]))
    melspec = model.transform(x)
    y = model.base_sed.encoder(melspec)
    print(melspec.shape, y.shape)
    model = model.to(Config.training_params["device"])
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=Config.training_params['lr'],
        weight_decay=Config.training_params['wd']
    )

    warmup_epochs = Config.training_params['warmup_epochs']
    warmup_scheduler = torch.optim.lr_scheduler.LinearLR(
        optimizer,
        start_factor=0.01,
        end_factor=1.0,      # ramp up to full lr
        total_iters=warmup_epochs
    )
    cosine_scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
        optimizer,
        T_max=Config.training_params['n_epochs'] - warmup_epochs,
        eta_min=Config.training_params['min_lr']
    )
    scheduler = torch.optim.lr_scheduler.SequentialLR(
        optimizer,
        schedulers=[warmup_scheduler, cosine_scheduler],
        milestones=[warmup_epochs]
    )
    return model, optimizer, scheduler

# %%
train_loader = get_dataloaders(Config, train_df, val_df)
model, optimizer, scheduler = create_model_opt_sc(Config)

# %%
if Config.training_params["amp"]:
    scaler = torch.amp.GradScaler(Config.training_params['device'])
    print ("AMP Active")
else:
    scaler = None
    print ("AMP NOT Active")


exp_name = Config.experiment_params.get("experiment_name")
print (Config.experiment_params.get("save_epochs"))
best_map_score = 0
for epoch in range(0, Config.training_params['n_epochs']):
    train_loss = train_epoch(model, train_loader, optimizer, scaler, Config.training_params)
    val_loss = 0
    val_score = 0
    
    current_lr = optimizer.param_groups[0]['lr']
    log = time.ctime() + ' ' + f"Epoch {epoch}, LR: {current_lr:.6f}, Train Loss: {train_loss:.4f}, Val Loss: {val_loss:.4f}, Val Score: {val_score:.4f}\n"
    
    print (log)
    scheduler.step()

    if epoch in Config.experiment_params.get("save_epochs"):
        torch.save(model.state_dict(), os.path.join(Config.experiment_params.get("output_dir"), exp_name, f"{exp_name}_{epoch}.pt"))


# %%
torch.save(model.state_dict(), os.path.join(Config.experiment_params.get("output_dir"), exp_name, f"{exp_name}_final.pt"))

# %%


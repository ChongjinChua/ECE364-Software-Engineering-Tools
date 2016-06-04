import re
import numpy
import scipy
import zlib
import base64

class Payload:
    def __init__(self, img=None, compressionLevel=-1, xml=None):
        #Error handling
        val_error = self.valueCheck(img,compressionLevel,xml)
        type_error = self.typeCheck(img,xml)        

        if val_error:
            raise ValueError(val_error)
        elif type_error:
            raise TypeError(type_error)

        self.img = img
        self.xml = xml

        if img is not None:
            img_1D = self.generate_img(img,True)
            img_compressed = self.compress_img(img_1D,compressionLevel,True)
            xml_content = self.encode_img(img_compressed,True)

            self.xml = self.generate_xml(xml_content.decode("utf-8"),True)

        else:
            xml_content = self.generate_xml(xml,False)
            img_compressed = self.encode_img(xml_content.encode("utf-8"),False)
            img_decompressed = self.compress_img(img_compressed,-1,False)
            img_1D = numpy.fromstring(img_decompressed, dtype=numpy.uint8)

            self.img = self.generate_img(img_1D,False)


    def generate_xml(self,xml_data,img_flag):
        if img_flag:
            color_str = 'Gray'
            compress_str = 'False'
            if self.color_flag:
                color_str = 'Color'
            if self.compress_flag:
                compress_str = 'True'

            dim_row = self.xml_size[0]
            dim_col = self.xml_size[1]
            size_str = str(dim_row) + ',' + str(dim_col)

            return '<?xml version="1.0" encoding="UTF-8"?>\n<payload type="{0}" size="{1}" compressed="{2}">\n{3}\n</payload>'.format(color_str,size_str,compress_str,xml_data)

        else:
            #regex = r"(<red>^\d+(?= ))(<green>(?>= )\d+(?= ))(<blue>(?>= )\d+$)"
            regex = r'"(?P<group>[\w\d\,]+)"'
            regex_content = r'(?<=\n)\S+(?=\n</payload>)'
            img_data = re.findall(regex,xml_data)
            xml_content = re.search(regex_content,xml_data)

            if img_data:
                self.color_flag = False
                self.compress_flag = False
                if img_data[0] == 'Color':
                    self.color_flag = True
                if img_data[2] == 'True':
                    self.compress_flag = True

                dim = img_data[1].split(',')
                self.img_size = tuple([int(dim[0]),int(dim[1])])
                print(self.img_size)

            return xml_content.group()


    def encode_img(self,data,img_flag):
        if img_flag:
            return base64.b64encode(data)
        else:
            return base64.b64decode(data)

    def compress_img(self,data,compressionLevel,img_flag):
        if img_flag:
            self.compress_flag = False
            if compressionLevel != -1:
                self.compress_flag = True
                return zlib.compress(data.tostring(),compressionLevel)
            else:
                rtn_str = data.tostring()
                return rtn_str
        else:
            if self.compress_flag is True:
                return zlib.decompress(data)
            else:
                return data

    def generate_img(self,data,img_flag):
        if img_flag:
            #color image if color_flag is 1
            self.color_flag = self.detect_color(data)
            self.xml_size = data.shape

            if self.color_flag:
                red = data[:,:,0]
                green = data[:,:,1]
                blue = data[:,:,2]
                a = numpy.array([red,green,blue])
            else:
                a = numpy.array([data])

            img = a.flatten()

            return img

        else:
            if self.color_flag is True:
                data = data.reshape(3,-1)
                data = numpy.dstack(tuple(data))
                data = data.reshape(self.img_size[0],self.img_size[1],3)
            else:
                data = data.reshape(self.img_size[0],self.img_size[1])

            return data


    def detect_color(self,img):
        if type(img[0][0]) is numpy.ndarray:
            return True
        return False

    def valueCheck(self,img,compressionLevel,xml):
        if img is None and xml is None:
            return "img and xml are missing!"
        elif compressionLevel < -1 or compressionLevel > 9:
            return "invalid compressionLevel!"
        else:
            return None

    def typeCheck(self,img,xml):
        if img is not None and type(img) is not numpy.ndarray:
            return "invalid img type!"
        elif xml is not None and type(xml) is not str:
            return "invalid xml type!"
        else:
            return None

class Carrier:
    def __init__(self, img):
        #Error handling

        if type(img) is not numpy.ndarray:
            raise TypeError("input type is invalid!")

        self.img = img
        self.img_size = img.shape
        self.color_flag = self.detect_color(self.img)

    def detect_color(self,img):
        if type(img[0][0]) is numpy.ndarray:
            return True
        return False

    def embedPayload(self,payload,override=False):

        if type(payload) is not Payload:
            raise TypeError("input type is wrong!")

        comp_payload_size = self.calc_payloadSize(payload)
        comp_carrier_size = self.calc_carrierSize()

        if comp_payload_size > comp_carrier_size:
            raise ValueError("Payload size is smaller than Carrier")
        elif override is False and self.payloadExists():
            raise Exception("Payload exist, do not override!")

        rtn_img = self.img.copy()
        xml_array = numpy.ndarray(shape=(len(payload.xml),1),dtype=numpy.uint8)
        ind = 0
        for item in payload.xml:
            xml_array[ind][0] = ord(item)
            ind += 1
        xml_bin = numpy.unpackbits(xml_array)

        if self.color_flag:
            red = rtn_img[:,:,0]
            green = rtn_img[:,:,1]
            blue = rtn_img[:,:,2]
            a = numpy.array([red,green,blue])
        else:
            a = numpy.array([rtn_img])

        img_1d = a.flatten()
        target_img = img_1d[:len(xml_bin)]

        target_img = numpy.bitwise_and(target_img,numpy.uint(254))
        target_img = numpy.bitwise_or(target_img,xml_bin)
        target_img = numpy.concatenate((target_img,img_1d[len(xml_bin):]))

        if self.color_flag is True:
            data = target_img.reshape(3,-1)
            data = numpy.dstack(tuple(data))
            data = data.reshape(self.img_size[0],self.img_size[1],3)
        else:
            data = target_img.reshape(self.img_size[0],self.img_size[1])
        return data

    def calc_payloadSize(self,payload):
        self.payload_size = payload.img.shape
        if len(self.payload_size) == 3:
            self.payload_color_flag = True
            payload_color = 3
        else:
            self.payload_color_flag = False
            payload_color = 1

        return int(self.payload_size[0])*int(self.payload_size[1])*payload_color

    def calc_carrierSize(self):
        if self.color_flag:
            carrier_color = 3
        else:
            carrier_color = 1

        return int(int(self.img_size[0])*int(self.img_size[1])*carrier_color/8)

    def clean(self):
        rtn_array = self.img.copy()
        if self.color_flag:
            red = rtn_array[:,:,0]
            green = rtn_array[:,:,1]
            blue = rtn_array[:,:,2]
            a = numpy.array([red,green,blue])
            rtn_array = numpy.bitwise_and(a.flatten(),numpy.uint(254))
            rtn_array = rtn_array.reshape(3,-1)
            rtn_array = numpy.dstack(tuple(rtn_array))
            rtn_array = rtn_array.reshape(self.img_size[0],self.img_size[1],3)
        else:
            a = numpy.array([rtn_array])
            rtn_array = numpy.bitwise_and(a.flatten(),numpy.uint(254))
            rtn_array = rtn_array.reshape(self.img_size[0],self.img_size[1])

        rtn_img = Payload(rtn_array)
        return rtn_img.img

    def extractPayload(self):
        if not self.payloadExists():
            raise Exception("Payload is missing, can't extract!")

        img_cpy = self.img.copy()
        if self.color_flag:
            red = img_cpy[:,:,0]
            green = img_cpy[:,:,1]
            blue = img_cpy[:,:,2]
            a = numpy.array([red,green,blue])
        else:
            a = numpy.array([img_cpy])

        img_1d = a.flatten()
        xml_list = numpy.bitwise_and(img_1d,numpy.uint8(1))
        xml_list = numpy.packbits(xml_list)

        xml_str = ""
        ind = 0
        totem = ">"
        for item in xml_list:
            char = chr(item)
            xml_str += char

            if char == totem:
                ind += 1
                if ind == 3:
                    break

        return Payload(None,-1,xml_str)

    def payloadExists(self):
        buffer = []
        if self.color_flag:
            row = self.img[0]
            stop_flag = 0
            for col in row:
                if col[0] & numpy.uint8(1) == 1:
                    buffer.append(1)
                else:
                    buffer.append(0)

                if stop_flag == 7:
                    print(buffer)
                    valid = chr(numpy.packbits(buffer)[0])
                    if valid == "<":
                        return True
                    else:
                        return False
                stop_flag += 1
        else:
            i = 0
            row = self.img[0]
            while i < 8:
                if row[i] & numpy.uint8(1) == 1:
                    buffer.append(1)
                else:
                    buffer.append(0)
                i+= 1
            valid = chr(numpy.packbits(buffer)[0])
            if valid == "<":
                return True
            else:
                return False

if __name__ == "__main__":
    pass

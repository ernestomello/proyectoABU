export interface CuotaInterface {
  id:                number;
  id_socio:          IDSocio;
  estado:            string;
  importe:           number;
  mes_anio:          Date;
  fecha_generada:    Date;
  fecha_vencimiento: Date;
  referencia:        string;
  metodo_pago:       number;
}

export interface IDSocio extends CuotaInterface{
  id_persona:      IDPersona;
  categoria_socio: CategoriaSocio;
  frecuencia_pago: string;
  estado:          string;
}

export interface CategoriaSocio extends CuotaInterface{
  descripcion: string;
}

export interface IDPersona extends CuotaInterface{
  nombre:           string;
  apellido_paterno: string;
  apellido_materno: string;
  fecha_nacimiento: Date;
  direccion:        string;
  telefono:         string;
}


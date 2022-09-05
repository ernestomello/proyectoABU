export interface CuotaInterface {
  id:                number;
  id_socio:          number;
  estado:            string;
  importe:           number;
  mes_anio:          Date;
  fecha_generada:    Date;
  fecha_vencimiento: Date;
  referencia:        string;
  metodo_pago:       number;
  nombre_socio:      string;
}


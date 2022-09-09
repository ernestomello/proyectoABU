
export type Roles = 'ADMIN' | 'USER';

export interface Socio{
  email:string;
  password:string;
}

export interface SocioResponse{
  id_socio: number;
  token: string;
  name:string;
  rol: Roles;
}

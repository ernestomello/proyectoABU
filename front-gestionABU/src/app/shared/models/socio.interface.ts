
export type Roles = 'ADMIN' | 'USER';

export interface Socio{
  email:string;
  password:string;
}

export interface SocioResponse{
  message: string;
  token: string;
  rol: Roles;
}

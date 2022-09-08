import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-academic-data',
  templateUrl: './academic-data.component.html',
  styleUrls: ['./academic-data.component.css','../profile.component.css']
})
export class AcademicDataComponent implements OnInit {

  @Input() id_socio: number = 0;

  constructor() { }

  ngOnInit(): void {
  }

}

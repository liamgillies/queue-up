import { Component, OnInit } from '@angular/core';
import { FormsModule, FormArray, FormControl, FormGroup, Validators } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { UserService } from '../_services/user.service';
@Component({
  selector: 'app-create-profile',
  templateUrl: './create-profile.component.html',
  styleUrls: ['./create-profile.component.css']
})
export class CreateProfileComponent implements OnInit {

  LOL_RANKS = [
    {name: 'Challenger', rank: 26},
    {name: 'Grandmaster', rank: 25},
    {name: 'Master', rank: 24},
    {name: 'Diamond I', rank: 23},
    {name: 'Diamond II', rank: 22},
    {name: 'Diamond III', rank: 21},
    {name: 'Diamond IV', rank: 20},
    {name: 'Platinum I', rank: 19},
    {name: 'Platinum II', rank: 18},
    {name: 'Platinum III', rank: 17},
    {name: 'Platinum IV', rank: 16},
    {name: 'Gold I', rank: 15},
    {name: 'Gold II', rank: 14},
    {name: 'Gold III', rank: 13},
    {name: 'Gold IV', rank: 12},
    {name: 'Silver I', rank: 11},
    {name: 'Silver II', rank: 10},
    {name: 'Silver III', rank: 9},
    {name: 'Silver IV', rank: 8},
    {name: 'Bronze I', rank: 7},
    {name: 'Bronze II', rank: 6},
    {name: 'Bronze III', rank: 5},
    {name: 'Bronze IV', rank: 4},
    {name: 'Iron I', rank: 3},
    {name: 'Iron II', rank: 2},
    {name: 'Iron III', rank: 1},
    {name: 'Iron IV', rank: 0}]

  LOL_ROLES = [
    { name: 'Top', value: 'top' },
    { name: 'Jungle', value: 'jungle' },
    { name: 'Middle', value: 'middle' },
    { name: 'Bottom', value: 'bottom' },
    { name: 'Support', value: 'support' },
]

  profileForm = new FormGroup({
    ign: new FormControl('', [Validators.required]),
    rank: new FormControl('', [Validators.required]),
    roles: new FormArray([], [Validators.required]),
    description: new FormControl('',[Validators.required, Validators.maxLength(100)]),
    opgg: new FormControl('', [Validators.required]),
    rolesLF: new FormArray([], [Validators.required]),
    lowRankLF: new FormControl('', [Validators.required]),
    highRankLF: new FormControl('', [Validators.required])
  });

  public submitted:boolean = false;
  public rankDifferenceError:boolean = false;
  constructor(private userService: UserService,
    private router: Router) {}

  ngOnInit(): void {
  }

  changeRank(e) {
    this.profileForm.controls.rank.setValue(e.target.value, {
      onlySelf: true
    });
  }

  changeRankLow(e) {
    this.profileForm.controls.lowRankLF.setValue(e.target.value, {
      onlySelf: true
    });
  }

  changeRankHigh(e) {
    this.profileForm.controls.highRankLF.setValue(e.target.value, {
      onlySelf: true
    });
  }

  onCheckboxChange(e) {
    const checkArray: FormArray = this.profileForm.get('roles') as FormArray;
  
    if (e.target.checked) {
      checkArray.push(new FormControl(e.target.value));
    } else {
      let i: number = 0;
      checkArray.controls.forEach((item: FormControl) => {
        if (item.value == e.target.value) {
          checkArray.removeAt(i);
          return;
        }
        i++;
      });
    }
  }

  onCheckboxChangeLF(e) {
    const checkArray: FormArray = this.profileForm.get('rolesLF') as FormArray;
  
    if (e.target.checked) {
      checkArray.push(new FormControl(e.target.value));
    } else {
      let i: number = 0;
      checkArray.controls.forEach((item: FormControl) => {
        if (item.value == e.target.value) {
          checkArray.removeAt(i);
          return;
        }
        i++;
      });
    }
  }

  register() {
    const rlen = this.profileForm.controls.rank.value.length
    const hlen = this.profileForm.controls.highRankLF.value.length
    const llen = this.profileForm.controls.lowRankLF.value.length
    const rank = parseInt(this.profileForm.controls.rank.value.substring(rlen-2,rlen))
    const highRank = parseInt(this.profileForm.controls.highRankLF.value.substring(hlen-2,hlen))
    const lowRank = parseInt(this.profileForm.controls.lowRankLF.value.substring(llen-2,llen))
    this.submitted = true;
    if (this.profileForm.invalid) {
      if(highRank < lowRank) {
        this.rankDifferenceError = true;
      }
      return;
    }
    else if(highRank < lowRank) {
      this.rankDifferenceError = true;
      return;
    }

    this.userService.createProfile({
      ign: this.profileForm.controls.ign.value,
      rank: rank,
      roles: this.profileForm.controls.roles.value,
      description: this.profileForm.controls.description.value,
      opgg: this.profileForm.controls.opgg.value,
      rolesLF: this.profileForm.controls.rolesLF.value,
      lowRankLF: lowRank,
      highRankLF: highRank
    }).subscribe(() => {
      //this.router.navigate(['/queue']);
    });
    
  }
}
